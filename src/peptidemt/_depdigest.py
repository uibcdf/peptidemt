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
        "conda": "molsysmt",
        "channel": "uibcdf",
    },
}
EXCEPTION_CLASS = RequiredDependencyError
DOC_URL = "https://github.com/uibcdf/peptidemt/blob/main/devguide/w2_macrel.md"
