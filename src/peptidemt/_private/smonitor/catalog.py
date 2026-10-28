"""Authoritative operational diagnostic declarations."""

from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[2]
CATALOG = {
    "RequiredDependencyError": {
        "code": "PEP-ERR-DEP-001",
        "source": "peptidemt.macrel.dependency",
        "category": "dependency",
        "level": "ERROR",
    },
    "MacrelFailureWarning": {
        "code": "PEP-WARN-RUN-001",
        "source": "peptidemt.macrel.execution",
        "category": "execution",
        "level": "WARNING",
    },
}
CODES = {
    "PEP-ERR-DEP-001": {
        "user_message": "Selected Macrel route requires '{library}'.",
        "user_hint": "Consult the recorded dependency installation guidance.",
    },
    "PEP-WARN-RUN-001": {
        "user_message": "Macrel assessment failed at '{stage}' ({cause_type}).",
        "user_hint": "Inspect result provenance; no scores were invented or retried.",
    },
}
SIGNALS = {
    "peptidemt.macrel.dependency": {"extra_required": ["library"]},
    "peptidemt.macrel.execution": {"extra_required": ["stage", "cause_type"]},
}
