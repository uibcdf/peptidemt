"""Detached analogue evidence and occurrence receiving; no scientific imports."""

import hashlib
import json
import math
from collections.abc import Mapping
from dataclasses import dataclass, field, fields

from ._data import decode, encode, freeze, load_json, mapping, nonempty_text
from .inputs import _ALPHABET, InputRecord, SequenceRecord, prepare_sequences
from .results import Provenance

_SCHEMA = "peptidemt.hydramp_analogue_receipt@1"
_ARRAYS = {
    "prototype_tokens": ("B", 25, "token"),
    "prototype_mean": ("B", 64, "finite"),
    "prototype_log_variance": ("B", 64, "finite"),
    "prototype_std": ("B", 64, "nonnegative"),
    "prototype_scale": ("B", 64, "nonnegative"),
    "std_underflow": ("B", 64, "bool"),
    "scale_underflow": ("B", 64, "bool"),
    "prototype_amp": ("B", None, "score"),
    "prototype_mic": ("B", None, "score"),
    "prototype_indices": ("N", None, "index"),
    "attempt_indices": ("N", None, "index"),
    "submitted_tokens": ("N", 25, "token"),
    "means": ("N", 64, "finite"),
    "noise": ("N", 64, "finite"),
    "latents": ("N", 64, "finite"),
    "conditioned": ("N", 66, "finite"),
    "decoder_inputs": ("N", 66, "finite"),
    "tokens": ("N", 25, "token"),
    "sequences": ("N", None, "str"),
    "amp": ("N", None, "score"),
    "mic": ("N", None, "score"),
    **{
        name: ("N", None, "bool")
        for name in (
            "improves",
            "excludes_self",
            "projected_empty",
            "duplicate",
            "retained",
        )
    },
}


def analogue_input_issues(item):
    """HydrAMP-specific admission, distinct from Macrel's initial-M policy."""
    if not isinstance(item, InputRecord):
        raise TypeError("Expected an InputRecord")
    s = item.proposal.sequence
    reasons = []
    if s is None:
        reasons.append("incomplete_sequence")
    elif not s:
        reasons.append("empty_sequence")
    else:
        if not set(s) <= _ALPHABET:
            reasons.append("unsupported_symbols")
        if len(s) > 25:
            reasons.append("outside_hydramp_length_scope")
    if item.proposal.chemistry:
        reasons.append("unassessed_explicit_chemistry")
    return tuple(reasons)


def _valid(value, kind):
    if kind == "bool":
        return type(value) is bool
    if kind == "str":
        return type(value) is str
    if kind in ("token", "index"):
        return type(value) is int and 0 <= value and (kind != "token" or value <= 20)
    if type(value) not in (int, float):
        return False
    try:
        if not math.isfinite(value):
            return False
    except OverflowError:
        return False
    return (kind != "score" or 0 <= value <= 1) and (
        kind != "nonnegative" or value >= 0
    )


def _vector(value, size, kind):
    return (
        isinstance(value, tuple)
        and len(value) == size
        and all(_valid(v, kind) for v in value)
    )


def _ordered_parents(parents):
    parents = tuple(parents)
    if any(
        not isinstance(p, InputRecord) or p.occurrence != i
        for i, p in enumerate(parents)
    ):
        raise ValueError("Parents must retain complete original occurrence order")
    return parents


def _record_data(record):
    return {f.name: getattr(record, f.name) for f in fields(record)}


@dataclass(frozen=True)
class AnalogueParentOutcome:
    parent_occurrence: int
    provider_index: int | None
    status: str
    issues: tuple[str, ...] = ()


@dataclass(frozen=True)
class AnalogueLink:
    child_occurrence: int
    parent_occurrence: int
    provider_index: int
    attempt_index: int
    trace_row: int


@dataclass(frozen=True)
class HydrAMPAnalogueReceipt:
    """Analogue-specific native evidence, separate from the de novo receipt.

    Raw malformed data remain inspectable. Extraction requires complete,
    consistent receiving; declared provenance/digests are not authentication.
    """

    snapshot_id: str
    parents: tuple[InputRecord, ...]
    seed: int
    temperature: float
    n_attempts: int
    submitted_parent_indices: tuple
    provenance: Provenance
    original_trace: Mapping = field(default_factory=dict)
    completed: bool = True
    failures: tuple[str, ...] = ()
    progress: Mapping = field(default_factory=dict)

    def __post_init__(self):
        nonempty_text(self.snapshot_id, "snapshot_id")
        object.__setattr__(self, "parents", _ordered_parents(self.parents))
        if type(self.seed) is not int or not 0 <= self.seed < 2**32:
            raise ValueError("seed must be an explicit uint32-range integer")
        if (
            not _valid(self.temperature, "nonnegative")
            or type(self.temperature) is bool
        ):
            raise ValueError("temperature must be finite and nonnegative")
        # The native composer converts this dimensionless numeric argument to float.
        object.__setattr__(self, "temperature", float(self.temperature))
        if type(self.n_attempts) is not int or self.n_attempts < 1:
            raise ValueError("n_attempts must be a positive integer")
        if (
            not isinstance(self.provenance, Provenance)
            or type(self.completed) is not bool
        ):
            raise TypeError("Expected Provenance and boolean completion")
        object.__setattr__(
            self,
            "submitted_parent_indices",
            freeze(tuple(self.submitted_parent_indices)),
        )
        for name in ("original_trace", "progress"):
            object.__setattr__(self, name, mapping(getattr(self, name)))
        object.__setattr__(self, "failures", tuple(self.failures))
        for reason in self.failures:
            nonempty_text(reason, "failure reason")

    @property
    def issues(self):
        """Recheck shape, occurrence and native-decision fidelity, never weights."""
        compatible = tuple(
            p.occurrence for p in self.parents if not analogue_input_issues(p)
        )
        submitted = self.submitted_parent_indices
        if any(type(v) is not int for v in submitted) or submitted != compatible:
            return ("invalid_parent_submission_mapping",)
        if not self.completed or self.failures:
            return ("incomplete_execution", *self.failures)
        b = len(submitted)
        if not b:
            return ("unexpected_unsubmitted_trace",) if self.original_trace else ()
        n = b * self.n_attempts
        t = self.original_trace
        problems = []
        for name, (rows, columns, kind) in _ARRAYS.items():
            count = b if rows == "B" else n
            data = t.get(name)
            valid = (
                _vector(data, count, kind)
                if columns is None
                else isinstance(data, tuple)
                and len(data) == count
                and all(_vector(row, columns, kind) for row in data)
            )
            if not valid:
                problems.append("invalid_trace:" + name)
        for name in ("seed", "temperature", "n_attempts"):
            if type(t.get(name)) is bool or t.get(name) != getattr(self, name):
                problems.append("changed_request:" + name)
        results = t.get("results")
        if not isinstance(results, tuple) or len(results) != b:
            problems.append("invalid_results")
        if problems:
            return tuple(problems)
        for i, tokens in enumerate(t["prototype_tokens"]):
            nonzero = [j for j, v in enumerate(tokens) if v]
            if (
                not nonzero
                or nonzero != list(range(len(nonzero)))
                or len(nonzero) != len(self.parents[submitted[i]].proposal.sequence)
            ):
                problems.append("invalid_prototype_padding")
        expected_results = []
        for i, parent_index in enumerate(submitted):
            first = {}
            parent_sequence = self.parents[parent_index].proposal.sequence
            for row in range(i, n, b):
                sequence = t["sequences"][row]
                improves = (
                    t["amp"][row] > t["prototype_amp"][i]
                    and t["mic"][row] > t["prototype_mic"][i]
                )
                is_self = sequence == parent_sequence
                duplicate = improves and not is_self and sequence in first
                if (
                    t["prototype_indices"][row] != i
                    or t["attempt_indices"][row] != row // b
                    or t["submitted_tokens"][row] != t["prototype_tokens"][i]
                ):
                    problems.append("invalid_attempt_correspondence")
                if (
                    t["improves"][row] != improves
                    or t["excludes_self"][row] != is_self
                    or t["projected_empty"][row] != (sequence == "")
                    or t["duplicate"][row] != duplicate
                ):
                    problems.append("changed_native_decision")
                if improves and not is_self and not duplicate:
                    first[sequence] = row
            candidates = tuple(
                {
                    "sequence": s,
                    "trace_row": row,
                    "attempt_index": row // b,
                    "amp": t["amp"][row],
                    "mic": t["mic"][row],
                }
                for s, row in sorted(first.items())
            )
            expected_results.append(
                {
                    "prototype_index": i,
                    "prototype_sequence": parent_sequence,
                    "amp": t["prototype_amp"][i],
                    "mic": t["prototype_mic"][i],
                    "candidates": candidates,
                }
            )
            retained = set(first.values())
            if any(t["retained"][row] != (row in retained) for row in range(i, n, b)):
                problems.append("changed_retained_mapping")
        # Equality alone accepts bool-as-int indices; check their exact type too.
        for actual, expected in zip(results, expected_results):
            if not isinstance(actual, Mapping) or actual != expected:
                problems.append("changed_candidate_bucket")
                continue
            if type(actual["prototype_index"]) is not int or any(
                type(c[k]) is not int
                for c in actual["candidates"]
                for k in ("trace_row", "attempt_index")
            ):
                problems.append("invalid_candidate_index")
            if any(not _valid(actual[k], "score") for k in ("amp", "mic")) or any(
                not _valid(c[k], "score")
                for c in actual["candidates"]
                for k in ("amp", "mic")
            ):
                problems.append("invalid_candidate_score")
        return tuple(dict.fromkeys(problems))

    @property
    def outcomes(self):
        valid = not self.issues
        indices = {
            v: i for i, v in enumerate(self.submitted_parent_indices) if type(v) is int
        }
        attempted = (
            bool(self.progress.get("attempted", {}).get("native_analogue"))
            if isinstance(self.progress.get("attempted", {}), Mapping)
            else False
        )
        outcomes = []
        for p in self.parents:
            incompatible = analogue_input_issues(p)
            i = indices.get(p.occurrence)
            if incompatible:
                status, issues = "incompatible", incompatible
            elif not self.completed:
                status, issues = (
                    ("interrupted" if attempted else "not_attempted"),
                    self.issues,
                )
            elif not valid:
                status, issues = "invalid_output", self.issues
            else:
                candidates = self.original_trace["results"][i]["candidates"]
                status, issues = ("candidates" if candidates else "no_hit"), ()
            outcomes.append(AnalogueParentOutcome(p.occurrence, i, status, issues))
        return tuple(outcomes)

    @property
    def links(self):
        if self.issues:
            return ()
        links = []
        for i, result in enumerate(self.original_trace.get("results", ())):
            for c in result["candidates"]:
                links.append(
                    AnalogueLink(
                        len(links),
                        self.submitted_parent_indices[i],
                        i,
                        c["attempt_index"],
                        c["trace_row"],
                    )
                )
        return tuple(links)

    def proposals(self):
        """Unchanged returned sequence views; empty/initial-M views stay excluded."""
        if self.issues:
            raise ValueError("Unreceived analogue evidence: " + ", ".join(self.issues))
        content_id = self.content_id
        return prepare_sequences(
            [
                SequenceRecord(
                    self.original_trace["sequences"][link.trace_row],
                    source=self.snapshot_id,
                    context={
                        "generation": {
                            "receipt_id": content_id,
                            "view": "native_zero_removed_sequence",
                            **_record_data(link),
                        }
                    },
                )
                for link in self.links
            ]
        )

    def _data(self):
        data = {f.name: getattr(self, f.name) for f in fields(self)}
        data["parents"] = tuple(
            {"occurrence": p.occurrence, "proposal": _record_data(p.proposal)}
            for p in self.parents
        )
        data["provenance"] = _record_data(self.provenance)
        return freeze(data)

    @property
    def content_id(self):
        return (
            "sha256:"
            + hashlib.sha256(
                json.dumps(encode(self._data()), sort_keys=True).encode()
            ).hexdigest()
        )

    def to_json(self):
        return json.dumps(
            encode(
                freeze(
                    {
                        "schema": _SCHEMA,
                        "content_id": self.content_id,
                        "data": self._data(),
                    }
                )
            ),
            allow_nan=False,
        )

    @classmethod
    def from_json(cls, text):
        value = decode(load_json(text))
        if (
            not isinstance(value, Mapping)
            or set(value) != {"schema", "content_id", "data"}
            or value["schema"] != _SCHEMA
        ):
            raise ValueError("Unsupported analogue receipt schema")
        data = dict(value["data"])
        if set(data) != {f.name for f in fields(cls)}:
            raise ValueError("Unexpected analogue receipt fields")
        data["parents"] = tuple(
            InputRecord(p["occurrence"], SequenceRecord(**p["proposal"]))
            for p in data["parents"]
        )
        data["provenance"] = Provenance(**data["provenance"])
        receipt = cls(**data)
        if receipt.content_id != value["content_id"]:
            raise ValueError("Analogue receipt content digest mismatch")
        return receipt

    @classmethod
    def from_trace(
        cls, trace, *, snapshot_id, parents, submitted_parent_indices, provenance
    ):
        """Detach an already returned native trace using its public fields only."""
        data = {
            name: getattr(trace, name).tolist()
            for name in _ARRAYS
            if name != "sequences"
        }
        data.update(
            sequences=trace.sequences,
            seed=trace.seed,
            temperature=trace.temperature,
            n_attempts=trace.n_attempts,
            results=tuple(
                {
                    **{
                        name: getattr(r, name)
                        for name in (
                            "prototype_index",
                            "prototype_sequence",
                            "amp",
                            "mic",
                        )
                    },
                    "candidates": tuple(_record_data(c) for c in r.candidates),
                }
                for r in trace.results
            ),
        )
        return cls(
            snapshot_id,
            parents,
            trace.seed,
            trace.temperature,
            trace.n_attempts,
            submitted_parent_indices,
            provenance,
            data,
        )
