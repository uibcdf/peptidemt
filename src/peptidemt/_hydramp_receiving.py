"""Data-only HydrAMP receiving; no engine execution.

Retain native return order and raw anomalous output. Importing or constructing a
receipt does not qualify its source or grant a model/assessment execution budget.
"""

import json
import math
from collections import Counter
from collections.abc import Mapping
from dataclasses import dataclass, field, fields

from ._data import decode, encode, freeze, load_json, mapping, nonempty_text
from .inputs import SequenceRecord, prepare_sequences
from .results import Provenance

_SCHEMA = "peptidemt.hydramp_receipt@1"
_NATIVE_FIELDS = (
    "sequence",
    "amp",
    "mic",
    "length",
    "hydrophobicity",
    "hydrophobic_moment",
    "charge",
    "isoelectric_point",
)
_TRACE_FIELDS = (
    "sampled_latents",
    "pca_projected",
    "conditioned",
    "decoder_input",
    "tokens",
    "sequences",
    "amp",
    "mic",
)


@dataclass(frozen=True)
class HydrAMPReceipt:
    """Detached output for the selected properties=True, unfiltered AMP route.

    native_results is in the provider's RETURNED order; original_trace arrays are
    in its input/draw order. Index claims are retained even when invalid, but row
    traces are attached only after unambiguous correspondence checks. No string
    re-encoding, sorting, trimming, repair, deduplication or molecular inference.
    The provisional public data contract uses the v1 receipt schema. Its
    same-operation fidelity has bounded H3/H4 evidence; construction alone does
    not qualify a generator, its scientific applicability or a public run API.
    """

    snapshot_id: str
    requested_count: int
    seed: int
    native_results: tuple
    returned_input_indices: tuple
    provenance: Provenance
    original_trace: Mapping = field(default_factory=dict)
    completed: bool = True
    failures: tuple[str, ...] = ()

    def __post_init__(self):
        nonempty_text(self.snapshot_id, "snapshot_id")
        if type(self.requested_count) is not int or self.requested_count < 1:
            raise ValueError("requested_count must be a positive integer")
        if type(self.seed) is not int or not 0 <= self.seed < 2**32:
            raise ValueError("seed must be an explicit uint32-range integer")
        if not isinstance(self.provenance, Provenance):
            raise TypeError("provenance must be Provenance")
        if type(self.completed) is not bool:
            raise TypeError("completed must be boolean")
        for name in ("native_results", "returned_input_indices", "failures"):
            if not isinstance(getattr(self, name), (list, tuple)):
                raise TypeError(f"{name} must be a list or tuple")
        object.__setattr__(self, "native_results", freeze(tuple(self.native_results)))
        object.__setattr__(
            self, "returned_input_indices", freeze(tuple(self.returned_input_indices))
        )
        object.__setattr__(self, "original_trace", mapping(self.original_trace))
        object.__setattr__(self, "failures", tuple(self.failures))
        for reason in self.failures:
            nonempty_text(reason, "failure reason")

    def _index(self, position):
        if position >= len(self.returned_input_indices):
            return None
        return self.returned_input_indices[position]

    def _row_issues(self, position, index_counts=None):
        raw = self.native_results[position]
        reasons = []
        index = self._index(position)
        if index_counts is None:
            index_counts = Counter(
                i for i in self.returned_input_indices if type(i) is int
            )
        valid_index = type(index) is int and 0 <= index < self.requested_count
        if not valid_index:
            reasons.append("invalid_source_correspondence")
        elif index_counts[index] != 1:
            reasons.append("ambiguous_source_correspondence")
        if not isinstance(raw, Mapping):
            return tuple([*reasons, "malformed_native_row"])
        reasons.extend(
            "missing_native_field:" + k for k in _NATIVE_FIELDS if k not in raw
        )
        sequence = raw.get("sequence")
        if not isinstance(sequence, str):
            reasons.append("invalid_native_sequence")
        for key in _NATIVE_FIELDS[1:]:
            value = raw.get(key)
            valid_number = type(value) in (int, float)
            if valid_number:
                try:
                    valid_number = math.isfinite(value)
                except OverflowError:
                    valid_number = False
            if not valid_number:
                reasons.append("invalid_native_value:" + key)
            elif key in ("amp", "mic") and not 0 <= value <= 1:
                reasons.append("invalid_native_value:" + key)
        if isinstance(sequence, str) and raw.get("length") != len(sequence):
            reasons.append("inconsistent_native_length")
        for key in _TRACE_FIELDS:
            if key not in self.original_trace:
                continue
            values = self.original_trace[key]
            if not isinstance(values, tuple) or len(values) != self.requested_count:
                reasons.append("invalid_source_trace:" + key)
            elif valid_index and key in ("sequences", "amp", "mic"):
                native_key = "sequence" if key == "sequences" else key
                if values[index] != raw.get(native_key):
                    reasons.append("inconsistent_source_trace:" + key)
        return tuple(reasons)

    @property
    def issues(self):
        """Observable receiving anomalies, not new scientific acceptance rules."""
        reasons = []
        if not self.completed:
            reasons.append("incomplete_run")
        if len(self.native_results) != self.requested_count:
            reasons.append("returned_count_mismatch")
        if len(self.returned_input_indices) != len(self.native_results):
            reasons.append("mapping_count_mismatch")
        reasons.extend("reported_failure:" + reason for reason in self.failures)
        index_counts = Counter(i for i in self.returned_input_indices if type(i) is int)
        for position in range(len(self.native_results)):
            reasons.extend(
                f"row:{position}:{reason}"
                for reason in self._row_issues(position, index_counts)
            )
        return tuple(reasons)

    @property
    def inputs(self):
        """Every returned occurrence as an unchanged proposal, including failures.

        Macrel's existing admission remains operation-specific. Generation issues
        and unresolved provenance remain visible in context and the receipt; a
        compatible string or a later Macrel result cannot qualify this generator.
        """
        records = []
        run_issues = self.issues
        index_counts = Counter(i for i in self.returned_input_indices if type(i) is int)
        for position, raw in enumerate(self.native_results):
            sequence = raw.get("sequence") if isinstance(raw, Mapping) else raw
            if not isinstance(sequence, (str, type(None))):
                sequence = None  # Keep the original uncoercible payload below.
            index = self._index(position)
            reasons = self._row_issues(position, index_counts)
            trace = {}
            if not reasons:
                trace = {
                    key: values[index]
                    for key, values in self.original_trace.items()
                    if key in _TRACE_FIELDS
                }
            records.append(
                SequenceRecord(
                    sequence,
                    source=f"{self.provenance.provider}:{self.snapshot_id}",
                    context={
                        "generation": {
                            "snapshot_id": self.snapshot_id,
                            "returned_occurrence": position,
                            "reported_draw_index": index,
                            "requested_count": self.requested_count,
                            "seed": self.seed,
                            "completed": self.completed,
                            "run_issues": run_issues,
                            "row_issues": reasons,
                            "native_result": raw,
                            "original_trace": trace,
                            "provenance": {
                                f.name: getattr(self.provenance, f.name)
                                for f in fields(self.provenance)
                            },
                        }
                    },
                )
            )
        return prepare_sequences(records)

    def to_json(self):
        data = {
            f.name: getattr(self, f.name)
            for f in fields(self)
            if f.name != "provenance"
        }
        data["provenance"] = {
            f.name: getattr(self.provenance, f.name) for f in fields(self.provenance)
        }
        return json.dumps(encode(freeze({"schema": _SCHEMA, **data})), allow_nan=False)

    @classmethod
    def from_trace(cls, trace, *, snapshot_id, requested_count, provenance):
        """Receive an already produced selected-route trace; never run its model.

        The provider owns its numeric arrays and codec. Its arrays' tolist()
        exports the retained values; PeptideMT neither computes descriptors nor
        reconstructs tokens/strings. This does not execute or qualify a run API.
        """
        return cls(
            snapshot_id,
            requested_count,
            trace.seed,
            trace.native_results,
            trace.returned_input_indices,
            provenance,
            original_trace={
                "sampled_latents": trace.sampled_latents.tolist(),
                "conditioned": trace.conditioned.tolist(),
                "tokens": trace.tokens.tolist(),
                "sequences": trace.sequences,
                "amp": trace.amp.tolist(),
                "mic": trace.mic.tolist(),
            },
        )

    @classmethod
    def from_json(cls, text):
        data = decode(load_json(text))
        if not isinstance(data, Mapping) or data.get("schema") != _SCHEMA:
            raise ValueError("Unsupported HydrAMP receipt schema")
        data = dict(data)
        del data["schema"]
        if set(data) != {f.name for f in fields(cls)}:
            raise ValueError("Unexpected HydrAMP receipt fields")
        data["provenance"] = Provenance(**data["provenance"])
        return cls(**data)
