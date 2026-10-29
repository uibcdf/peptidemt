"""Selected-route dependencies; no installer or model download is automatic."""

from ._diagnostics import RequiredDependencyError

LIBRARIES = {
    "ackredit": {
        "type": "soft",
        "pypi": None,
        "conda": "ackredit>=0.9.0",
        "channel": "uibcdf",
    },
    "macrel": {"type": "soft", "pypi": "macrel==1.6.1", "conda": None},
    "molsysmt": {
        "type": "soft",
        "pypi": None,
        # Public 0.23.0 lacks the recognition fix and source-preserving reader.
        # Development uses the owner-source route recorded under #5/#6;
        # public installer hints await a file that passes those boundaries.
        "conda": None,
    },
}
EXCEPTION_CLASS = RequiredDependencyError
DOC_URL = "https://github.com/uibcdf/peptidemt/blob/main/devguide/w2_macrel.md"
