"""Host-owned bibliography and optional portable Ackredit capture after execution.

No scientific operation runs inside the provider error boundary. The application
owns sessions. Saving or reading a ResultSet does not call this module.
"""

import logging
from importlib.metadata import version

from depdigest import dep_digest, is_installed

from ._diagnostics import AttributionWarning, HydrAMPAttributionWarning, bundle
from ._private.smonitor import CATALOG, CODES

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


def _diagnose(error, warning_type=None):
    warning_type = warning_type or AttributionWarning
    diagnostic = None
    try:
        diagnostic = warning_type(cause_type=type(error).__name__)
        bundle.warn(diagnostic)
    except Exception as emission_error:
        if emission_error is diagnostic:
            return  # The catalog event was already emitted before warning promotion.
        code = CATALOG[warning_type.catalog_key]["code"]
        template = CODES[code]["user_message"]
        logging.getLogger("peptidemt.attribution").warning(
            "%s: %s",
            code,
            template.format(cause_type=type(error).__name__),
            extra={
                "code": code,
                "cause_type": type(error).__name__,
                "diagnostic_failure_type": type(emission_error).__name__,
            },
        )


def completed_attribution(details, snapshot_id):
    """Return detached references even when the optional provider cannot capture."""
    producer = {"name": "PeptideMT", "version": version("peptidemt")}
    operations, bibliography = _references(details, producer)
    return _capture(
        operations, bibliography, producer, snapshot_id, _TARGET, AttributionWarning
    )


def _capture(operations, bibliography, producer, snapshot_id, target, warning_type):
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
            with provider.scope(target):
                for record in bibliography:
                    provider.register_item(**record["item"])
                    provider.track_item(
                        record["item"]["id"],
                        used_by=target,
                        roles=record["roles"],
                        context={**record["context"], "snapshot_id": snapshot_id},
                    )
        result["ackredit"] = observed.attribution.to_dict()
        result["status"] = "captured"
    except Exception as error:
        result["status"] = "provider-failed"
        result["failure_type"] = type(error).__name__
        _diagnose(error, warning_type)
    return result


def hydramp_attribution(state, snapshot_id, *, analogue=False):
    """Credit confirmed child branches in the application's parent session."""
    producer = {"name": "PeptideMT", "version": version("peptidemt")}
    operations = list(state.get("completed", ()))
    runtime = state.get("runtime", {})
    versions = runtime.get("versions", {})
    bibliography = []

    def software(name, observed_version, url, reached):
        if observed_version is not None and reached:
            bibliography.append(
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
                        "completed_operations": reached,
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
        software(
            "hydramp-torch",
            versions.get("hydramp-torch"),
            "https://github.com/uibcdf/hydramp",
            operations,
        )
    numpy_operations = [
        op
        for op in operations
        if op.startswith("numeric_pca")
        or (
            analogue
            and op in ("encoder_loading", "checkpoint_loading", "native_sampling")
        )
    ]
    torch_operations = [
        op
        for op in operations
        if op in ("checkpoint_loading", "native_decoding", "native_scoring")
        or (
            analogue
            and op
            in (
                "encoder_loading",
                "native_encoding",
                "native_encoder_scale",
                "native_encoder_mean",
                "native_prototype_scoring",
                "native_generated_scoring",
            )
        )
    ]
    software("NumPy", versions.get("numpy"), "https://numpy.org", numpy_operations)
    software("PyTorch", versions.get("torch"), "https://pytorch.org", torch_operations)
    software(
        "modlAMP",
        versions.get("modlamp"),
        "https://github.com/alexarnimueller/modlAMP",
        [op for op in operations if op == "native_descriptors"],
    )
    native = [
        op
        for op in operations
        if op in ("native_decoding", "native_scoring", "native_generation")
        or (
            analogue
            and op
            in (
                "native_encoder_scale",
                "native_encoder_mean",
                "native_prototype_scoring",
                "native_generated_scoring",
                "native_analogue",
            )
        )
    ]
    if native:
        bibliography.append(
            {
                "item": {
                    "id": "doi:10.1038/s41467-023-36994-z",
                    "type": "article",
                    "title": "Discovering highly potent antimicrobial peptides with deep generative model HydrAMP",
                    "year": "2023",
                    "journal": "Nature Communications",
                    "doi": "10.1038/s41467-023-36994-z",
                },
                "roles": ["scientific_criterion", "software_description"],
                "context": {"completed_operations": native},
            }
        )
        commit = runtime.get("source_commit")
        if commit:
            bibliography.append(
                {
                    "item": {
                        "id": "implementation:HydrAMP:" + commit,
                        "type": "software",
                        "title": "Original HydrAMP reference implementation",
                        "url": "https://github.com/szczurek-lab/hydramp/tree/" + commit,
                    },
                    "roles": ["reference_implementation"],
                    "context": {
                        "executed_dependency": False,
                        "source_commit": commit,
                        "completed_operations": native,
                    },
                }
            )
    return _capture(
        operations,
        bibliography,
        producer,
        snapshot_id,
        "peptidemt.redesign_hydramp" if analogue else "peptidemt.generate_hydramp",
        HydrAMPAttributionWarning,
    )
