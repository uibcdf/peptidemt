"""Peptide design and attributable functional evaluation."""

from .inputs import (
    InputRecord,
    SequenceRecord,
    parse_fasta,
    prepare_sequences,
    read_fasta,
)
from .results import Outcome, Provenance, ProviderRow, ResultSet
from .selection import Selection, select

__all__ = [
    "InputRecord",
    "SequenceRecord",
    "parse_fasta",
    "prepare_sequences",
    "read_fasta",
    "Outcome",
    "Provenance",
    "ProviderRow",
    "ResultSet",
    "Selection",
    "select",
    "MacrelLimits",
    "assess_macrel",
]


def __getattr__(name):
    # Core imports and saved replay do not even initialize the optional route.
    if name in ("MacrelLimits", "assess_macrel"):
        from .macrel import MacrelLimits, assess_macrel

        return {"MacrelLimits": MacrelLimits, "assess_macrel": assess_macrel}[name]
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
