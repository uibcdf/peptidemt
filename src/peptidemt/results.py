"""Receive and replay attributed provider data without loading its engine."""

import json
import math
from collections import Counter
from collections.abc import Mapping
from dataclasses import dataclass, field, fields

from ._data import decode, encode, mapping, nonempty_text
from .inputs import InputRecord, SequenceRecord

_REQUIRED = (
    "Sequence",
    "AMP_probability",
    "is_AMP",
    "Hemolytic_probability",
    "Hemolytic",
    "AMP_family",
)


@dataclass(frozen=True)
class Provenance:
    """One source bundle and evidence role; a reference is not certification.

    Controlled fixtures can exercise selection with explicit non-scientific
    attribution. Native/imported results require a qualification reference for
    ranking. The caller supplies the actual asset/environment/terms evidence.
    """

    provider: str
    bundle_id: str
    evidence_kind: str
    qualification_reference: str | None = None
    details: Mapping = field(default_factory=dict)

    def __post_init__(self):
        for name in ("provider", "bundle_id", "evidence_kind"):
            nonempty_text(getattr(self, name), name)
        if self.evidence_kind not in ("controlled-fixture", "native", "imported"):
            raise ValueError("Unknown evidence_kind")
        if self.qualification_reference is not None:
            nonempty_text(self.qualification_reference, "qualification_reference")
        object.__setattr__(self, "details", mapping(self.details))


@dataclass(frozen=True)
class ProviderRow:
    """Original native columns with an explicit provider-side occurrence token."""

    token: str
    values: Mapping

    def __post_init__(self):
        nonempty_text(self.token, "token")
        object.__setattr__(self, "values", mapping(self.values))


@dataclass(frozen=True)
class Outcome:
    token: str
    row_index: int | None
    issues: tuple[str, ...]

    @property
    def eligible(self) -> bool:
        return not self.issues


def _row_issues(row: ProviderRow, item: InputRecord) -> tuple[str, ...]:
    values = row.values
    reasons = [f"missing_field:{name}" for name in _REQUIRED if name not in values]
    if values.get("Sequence") != item.proposal.sequence:
        reasons.append("changed_sequence_view")
    for score_name, label_name, yes, no in (
        ("AMP_probability", "is_AMP", True, False),
        ("Hemolytic_probability", "Hemolytic", "Hemo", "NonHemo"),
    ):
        score = values.get(score_name)
        if (
            type(score) not in (int, float)
            or not 0 <= score <= 1
            or not math.isfinite(score)
        ):
            reasons.append(f"invalid_score:{score_name}")
            continue
        label = values.get(label_name)
        expected = yes if score > 0.5 else no
        if type(label) is not type(expected) or label != expected:
            reasons.append(f"inconsistent_label:{label_name}")
    if values.get("AMP_family") not in ("ADP", "ALP", "CDP", "CLP"):
        reasons.append("invalid_composition_category")
    return tuple(reasons)


@dataclass(frozen=True)
class ResultSet:
    """A named evidence snapshot containing every input and every returned row.

    This constructor receives saved data; it never executes a provider. Outcome
    checks are derived anew, including on deserialization, rather than trusted
    from a saved 'eligible' flag. Failures are producer-reported reasons keyed by
    occurrence token (e.g. unavailable_provider, load_failure, timeout).
    """

    snapshot_id: str
    inputs: tuple[InputRecord, ...]
    rows: tuple[ProviderRow, ...]
    provenance: Provenance
    failures: Mapping = field(default_factory=dict)

    def __post_init__(self):
        nonempty_text(self.snapshot_id, "snapshot_id")
        if not isinstance(self.provenance, Provenance):
            raise TypeError("provenance must be Provenance")
        object.__setattr__(self, "inputs", tuple(self.inputs))
        object.__setattr__(self, "rows", tuple(self.rows))
        if any(
            not isinstance(item, InputRecord) or item.occurrence != index
            for index, item in enumerate(self.inputs)
        ):
            raise ValueError("inputs must retain complete original occurrence order")
        if any(not isinstance(row, ProviderRow) for row in self.rows):
            raise TypeError("rows must contain ProviderRow objects")
        failures = mapping(self.failures)
        tokens = {item.token for item in self.inputs}
        for token, reason in failures.items():
            if token not in tokens:
                raise ValueError("Failure references an unknown input token")
            nonempty_text(reason, "failure reason")
        object.__setattr__(self, "failures", failures)

    @property
    def outcomes(self) -> tuple[Outcome, ...]:
        positions = {}
        for index, row in enumerate(self.rows):
            positions.setdefault(row.token, []).append(index)
        outcomes = []
        for item in self.inputs:
            reasons = list(item.issues)
            matches = positions.get(item.token, [])
            row_index = matches[0] if len(matches) == 1 else None
            if item.token in self.failures:
                reasons.append(f"reported_failure:{self.failures[item.token]}")
            if not matches and not item.issues and item.token not in self.failures:
                reasons.append("missing_provider_row")
            if len(matches) > 1:
                reasons.append("duplicate_provider_rows")
            if row_index is not None:
                reasons.extend(_row_issues(self.rows[row_index], item))
            if (
                self.provenance.evidence_kind != "controlled-fixture"
                and self.provenance.qualification_reference is None
            ):
                reasons.append("unqualified_bundle")
            outcomes.append(Outcome(item.token, row_index, tuple(reasons)))
        return tuple(outcomes)

    @property
    def anomalies(self) -> tuple[tuple[int, str], ...]:
        """Return anomalous original row indices without dropping their values."""
        tokens = {item.token for item in self.inputs}
        counts = Counter(row.token for row in self.rows)
        return tuple(
            (
                index,
                "unknown_provider_token"
                if row.token not in tokens
                else "duplicate_provider_rows",
            )
            for index, row in enumerate(self.rows)
            if row.token not in tokens or counts[row.token] > 1
        )

    def to_json(self) -> str:
        """Serialize detached data with exact float hex values, including anomalies."""
        data = {
            "snapshot_id": self.snapshot_id,
            "inputs": tuple(
                {
                    "occurrence": item.occurrence,
                    "proposal": {
                        f.name: getattr(item.proposal, f.name)
                        for f in fields(SequenceRecord)
                    },
                }
                for item in self.inputs
            ),
            "rows": tuple(
                {"token": row.token, "values": row.values} for row in self.rows
            ),
            "provenance": {
                f.name: getattr(self.provenance, f.name) for f in fields(Provenance)
            },
            "failures": self.failures,
        }
        return json.dumps(
            {"schema": "peptidemt.results@1", "data": encode(data)},
            ensure_ascii=False,
            allow_nan=False,
            indent=2,
        )

    @classmethod
    def from_json(cls, text: str) -> "ResultSet":
        """Read only the explicit v1 data schema; never unpickle or import engines."""

        def unique_pairs(pairs):
            result = {}
            for key, value in pairs:
                if key in result:
                    raise ValueError(f"Duplicate JSON key: {key}")
                result[key] = value
            return result

        document = json.loads(text, object_pairs_hook=unique_pairs)
        if (
            not isinstance(document, dict)
            or set(document) != {"schema", "data"}
            or document["schema"] != "peptidemt.results@1"
        ):
            raise ValueError("Unsupported PeptideMT result schema")
        data = decode(document["data"])
        if not isinstance(data, Mapping) or set(data) != {
            "snapshot_id",
            "inputs",
            "rows",
            "provenance",
            "failures",
        }:
            raise ValueError("Malformed PeptideMT result data fields")
        try:
            return cls(
                snapshot_id=data["snapshot_id"],
                inputs=tuple(
                    InputRecord(item["occurrence"], SequenceRecord(**item["proposal"]))
                    for item in data["inputs"]
                ),
                rows=tuple(ProviderRow(**row) for row in data["rows"]),
                provenance=Provenance(**data["provenance"]),
                failures=data["failures"],
            )
        except (KeyError, TypeError) as error:
            raise ValueError("Malformed PeptideMT result data") from error
