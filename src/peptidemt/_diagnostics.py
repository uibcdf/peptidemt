"""Catalog-owned operational diagnostics, separate from scientific result data."""

from smonitor.integrations import CatalogException, CatalogWarning, DiagnosticBundle

from ._private.smonitor import CATALOG, META, PACKAGE_ROOT


class RequiredDependencyError(CatalogException, ImportError):
    catalog_key = "RequiredDependencyError"

    def __init__(self, message=None, *, library=None, caller=None):
        super().__init__(
            message,
            catalog=CATALOG,
            meta=META,
            extra={"library": library, "caller": caller},
        )


class MacrelFailureWarning(CatalogWarning):
    catalog_key = "MacrelFailureWarning"

    def __init__(self, message=None, *, stage=None, cause_type=None):
        super().__init__(
            message,
            catalog=CATALOG,
            meta=META,
            extra={
                key: value
                for key, value in {"stage": stage, "cause_type": cause_type}.items()
                if value is not None
            },
        )


class AttributionWarning(CatalogWarning):
    catalog_key = "AttributionWarning"

    def __init__(self, message=None, *, cause_type=None):
        super().__init__(
            message,
            catalog=CATALOG,
            meta=META,
            extra={"cause_type": cause_type} if cause_type is not None else {},
        )


bundle = DiagnosticBundle(CATALOG, META, PACKAGE_ROOT)
