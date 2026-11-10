"""Peptide design and attributable functional evaluation."""

from ._analogue_receiving import (
    AnalogueLink,
    AnalogueParentOutcome,
    HydrAMPAnalogueReceipt,
    analogue_input_issues,
)
from ._hydramp_receiving import HydrAMPReceipt
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
    "AnalogueLink",
    "AnalogueParentOutcome",
    "HydrAMPAnalogueReceipt",
    "analogue_input_issues",
    "HydrAMPReceipt",
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
    "HydrAMPBundle",
    "HydrAMPLimits",
    "generate_hydramp",
    "HydrAMPAnalogueBundle",
    "redesign_hydramp",
]


def __getattr__(name):
    # Core imports and saved replay do not even initialize the optional route.
    if name in ("MacrelLimits", "assess_macrel"):
        from .macrel import MacrelLimits, assess_macrel

        return {"MacrelLimits": MacrelLimits, "assess_macrel": assess_macrel}[name]
    if name in ("HydrAMPBundle", "HydrAMPLimits", "generate_hydramp"):
        from .hydramp import HydrAMPBundle, HydrAMPLimits, generate_hydramp

        return {
            "HydrAMPBundle": HydrAMPBundle,
            "HydrAMPLimits": HydrAMPLimits,
            "generate_hydramp": generate_hydramp,
        }[name]
    if name in ("HydrAMPAnalogueBundle", "redesign_hydramp"):
        from .analogue import HydrAMPAnalogueBundle, redesign_hydramp

        return {
            "HydrAMPAnalogueBundle": HydrAMPAnalogueBundle,
            "redesign_hydramp": redesign_hydramp,
        }[name]
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
