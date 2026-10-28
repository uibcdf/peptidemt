"""Host-owned bibliography and optional portable Ackredit capture after execution.

No scientific operation runs inside the provider error boundary. The application
owns sessions. Saving or reading a ResultSet does not call this module.
"""

import logging
from importlib.metadata import version

from depdigest import dep_digest, is_installed

from ._diagnostics import AttributionWarning, bundle
from ._private.smonitor import CODES

_TARGET = "peptidemt.assess_macrel"
_ARTICLE = {
    "id": "doi:10.7717/peerj.10555",
    "type": "article",
    "title": "Macrel: antimicrobial peptide screening in genomes and metagenomes",
    "author": "Santos-Júnior CD and Pan S and Zhao X and Coelho LP",
    "year": "2020",
    "journal": "PeerJ",
    "volume": "8",
    "pages": "e10555",
    "doi": "10.7717/peerj.10555",
}
_REFERENCE = {
    "id": "implementation:macrel:1.6.1:modlamp-descriptors",
    "type": "software",
    "title": "modlAMP-derived descriptors adapted inside Macrel",
    "url": "https://github.com/BigDataBiology/macrel/blob/190462605913844dca74b184869755609fbb20b2/macrel/macrel_features.py",
}


@dep_digest("ackredit")
def _load_backend():
    import ackredit

    return ackredit


def _references(details, producer):
    """Credit completed child operations without upgrading overall completion."""
    operations = []
    if "transport_sha256" in details:
        operations.append("molecular_serialization")
    for name in ("native_features", "native_predictions"):
        if name in details:
            operations.append(name)
    records = []

    def software(name, observed_version, url, role_operations):
        if observed_version is None:
            return
        records.append(
            {
                "item": {
                    "id": f"software:{name}:{observed_version}",
                    "type": "software",
                    "title": name,
                    "version": observed_version,
                    "url": url,
                },
                "roles": ["executed_software"],
                "context": {
                    "software": name,
                    "version": observed_version,
                    "completed_operations": role_operations,
                },
            }
        )

    if operations:
        software(
            "PeptideMT",
            producer["version"],
            "https://github.com/uibcdf/peptidemt",
            operations,
        )
    if "molecular_serialization" in operations:
        software(
            "MolSysMT",
            details.get("molsysmt", {}).get("version"),
            "https://github.com/uibcdf/molsysmt",
            ["molecular_serialization"],
        )
    native = [name for name in operations if name.startswith("native_")]
    if native:
        macrel_version = details.get("macrel", {}).get("version")
        software(
            "Macrel", macrel_version, "https://github.com/BigDataBiology/macrel", native
        )
        records.append(
            {
                "item": dict(_ARTICLE),
                "roles": ["scientific_criterion", "software_description"],
                "context": {
                    "software": "Macrel",
                    "version": macrel_version,
                    "completed_operations": native,
                },
            }
        )
        if "native_features" in operations:
            records.append(
                {
                    "item": dict(_REFERENCE),
                    "roles": ["reference_implementation"],
                    "context": {
                        "software": "modlAMP",
                        "version": None,
                        "executed_dependency": False,
                        "adapted_in": "Macrel 1.6.1",
                        "completed_operations": ["native_features"],
                    },
                }
            )
    return operations, records


def _diagnose(error):
    diagnostic = None
    try:
        diagnostic = AttributionWarning(cause_type=type(error).__name__)
        bundle.warn(diagnostic)
    except Exception as emission_error:
        if emission_error is diagnostic:
            return  # The catalog event was already emitted before warning promotion.
        template = CODES["PEP-WARN-ATTR-001"]["user_message"]
        logging.getLogger("peptidemt.attribution").warning(
            "%s: %s",
            "PEP-WARN-ATTR-001",
            template.format(cause_type=type(error).__name__),
            extra={
                "code": "PEP-WARN-ATTR-001",
                "cause_type": type(error).__name__,
                "diagnostic_failure_type": type(emission_error).__name__,
            },
        )


def completed_attribution(details, snapshot_id):
    """Return detached references even when the optional provider cannot capture."""
    producer = {"name": "PeptideMT", "version": version("peptidemt")}
    operations, bibliography = _references(details, producer)
    result = {
        "schema": "peptidemt.scientific_attribution@1",
        "producer": producer,
        "completed_operations": operations,
        "bibliography": bibliography,
        "status": "not-executed",
        "ackredit": None,
        "provider_version": None,
    }
    if not operations:
        return result
    try:
        if not is_installed("ackredit"):
            result["status"] = "provider-unavailable"
            return result
        provider = _load_backend()
        result["provider_version"] = version("ackredit")
        with provider.capture(
            snapshot_id,
            context={
                "producer": producer,
                "snapshot_id": snapshot_id,
                "completed_operations": operations,
            },
        ) as observed:
            with provider.scope(_TARGET):
                for record in bibliography:
                    provider.register_item(**record["item"])
                    provider.track_item(
                        record["item"]["id"],
                        used_by=_TARGET,
                        roles=record["roles"],
                        context={**record["context"], "snapshot_id": snapshot_id},
                    )
        result["ackredit"] = observed.attribution.to_dict()
        result["status"] = "captured"
    except Exception as error:
        result["status"] = "provider-failed"
        result["failure_type"] = type(error).__name__
        _diagnose(error)
    return result
