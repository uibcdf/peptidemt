"""One explicit isolated CPU HydrAMP route; no engine import in the host."""

import hashlib
import importlib.metadata
import json
import math
import os
import sys
import tempfile
from collections.abc import Mapping
from dataclasses import asdict, dataclass, fields, replace
from pathlib import Path, PurePosixPath

from smonitor import signal
from smonitor.integrations import register_provider

from ._data import decode, encode, freeze, load_json, mapping, nonempty_text
from ._diagnostics import PACKAGE_ROOT, HydrAMPFailureWarning
from ._diagnostics import bundle as diagnostics
from ._hydramp_process import source_manifest, supervise
from ._hydramp_receiving import HydrAMPReceipt
from .results import Provenance

register_provider(PACKAGE_ROOT, provider="peptidemt")


def _digest_text(value):
    if (
        not isinstance(value, str)
        or len(value) != 64
        or any(c not in "0123456789abcdef" for c in value)
    ):
        raise ValueError("Expected a lowercase SHA-256 digest")


def _manifest(value):
    if not isinstance(value, Mapping) or not value:
        raise ValueError("Expected a nonempty relative-path SHA-256 manifest")
    for name, digest in value.items():
        if (
            not isinstance(name, str)
            or not name
            or "\\" in name
            or PurePosixPath(name).is_absolute()
            or any(p in ("", ".", "..") for p in name.split("/"))
        ):
            raise ValueError("Manifest paths must be safe relative POSIX paths")
        _digest_text(digest)
    return mapping(value)


@dataclass(frozen=True)
class HydrAMPBundle:
    """Caller-reviewed local artifacts and installed runtime identity.

    No acquisition, model loading or scientific approval follows construction.
    Provider source hashes cover its complete installed Python package. Versions
    are exact qualification pins, not public reusable dependency ceilings.
    """

    checkpoint_root: str
    checkpoint_sha256: Mapping
    pca_path: str
    pca_sha256: str
    provider_source_sha256: Mapping
    expected_versions: Mapping
    source_commit: str
    starter_commit: str
    use_reference: str

    def __post_init__(self):
        for name in ("checkpoint_root", "pca_path"):
            nonempty_text(getattr(self, name), name)
            if not Path(getattr(self, name)).is_absolute():
                raise ValueError(f"{name} must be absolute")
        for name in ("source_commit", "starter_commit", "use_reference"):
            nonempty_text(getattr(self, name), name)
        for name in ("checkpoint_sha256", "provider_source_sha256"):
            object.__setattr__(self, name, _manifest(getattr(self, name)))
        _digest_text(self.pca_sha256)
        versions = mapping(self.expected_versions)
        if not {"hydramp-torch", "numpy", "torch", "modlamp"} <= set(versions):
            raise ValueError("Expected exact provider/NumPy/Torch/modlAMP versions")
        for name, version in versions.items():
            nonempty_text(name, "distribution name")
            nonempty_text(version, "distribution version")
        object.__setattr__(self, "expected_versions", versions)

    @property
    def bundle_id(self):
        data = {f.name: getattr(self, f.name) for f in fields(self)}
        del data["checkpoint_root"], data["pca_path"]
        return (
            "sha256:"
            + hashlib.sha256(
                json.dumps(encode(freeze(data)), sort_keys=True).encode()
            ).hexdigest()
        )


@dataclass(frozen=True)
class HydrAMPLimits:
    """Explicit caller-authorized bounds for one synchronous Linux CPU call.

    Address space is virtual memory. RSS is a sampled sum over the worker tree,
    not a hard kernel allocation. No GPU, network, retry or refill is selected.
    """

    max_records: int
    wall_seconds: float
    address_space_bytes: int
    rss_stop_bytes: int
    max_output_bytes: int
    cpu_ids: tuple[int, ...]
    threads: int = 1
    nice: int = 10
    min_available_memory_bytes: int = 0
    min_free_disk_bytes: int = 0
    temporary_root: str | None = None

    def __post_init__(self):
        for name in (
            "max_records",
            "address_space_bytes",
            "rss_stop_bytes",
            "max_output_bytes",
            "threads",
        ):
            if type(getattr(self, name)) is not int or getattr(self, name) < 1:
                raise ValueError(f"{name} must be a positive integer")
        if (
            type(self.wall_seconds) not in (int, float)
            or not math.isfinite(self.wall_seconds)
            or self.wall_seconds <= 0
        ):
            raise ValueError("wall_seconds must be positive and finite")
        if (
            not isinstance(self.cpu_ids, tuple)
            or not self.cpu_ids
            or any(type(v) is not int or v < 0 for v in self.cpu_ids)
            or len(set(self.cpu_ids)) != len(self.cpu_ids)
        ):
            raise ValueError("cpu_ids must be distinct nonnegative integers")
        if type(self.nice) is not int or not 0 <= self.nice <= 19:
            raise ValueError("nice must be an integer from 0 through 19")
        for name in ("min_available_memory_bytes", "min_free_disk_bytes"):
            if type(getattr(self, name)) is not int or getattr(self, name) < 0:
                raise ValueError(f"{name} must be a nonnegative integer")
        if self.temporary_root is not None:
            nonempty_text(self.temporary_root, "temporary_root")
            if not Path(self.temporary_root).is_absolute():
                raise ValueError("temporary_root must be absolute")


def _execute_worker(
    request,
    directory,
    limits,
    worker_python,
    *,
    request_module="peptidemt._hydramp_cli",
    response_schema="peptidemt.hydramp_worker@1",
):
    request_path, response_path = (
        directory / "request.json",
        directory / "response.json",
    )
    request_path.write_text(json.dumps(encode(freeze(request))), encoding="utf-8")
    run = supervise(
        [
            worker_python,
            "-B",
            "-I",
            "-m",
            request_module,
            str(request_path),
            str(response_path),
        ],
        directory,
        limits,
    )
    state_path = directory / "state.json"
    state = {}
    if state_path.is_file() and state_path.stat().st_size <= limits.max_output_bytes:
        try:
            state = decode(load_json(state_path.read_text(encoding="utf-8")))
        except (OSError, ValueError):
            state = {"state_unreadable": True}
    if run.get("failure"):
        return {
            "failure": run["failure"],
            "cause_type": "WorkerProcessError",
            "state": state,
            "supervision": run,
        }
    if (
        not response_path.is_file()
        or response_path.stat().st_size > limits.max_output_bytes
    ):
        return {
            "failure": "output_failure",
            "cause_type": "MissingResponse",
            "state": state,
            "supervision": run,
        }
    try:
        response = decode(load_json(response_path.read_text(encoding="utf-8")))
        if (
            not isinstance(response, Mapping)
            or response.get("schema") != response_schema
            or not isinstance(response.get("state", {}), Mapping)
        ):
            raise ValueError("Unsupported worker response")
    except (OSError, ValueError, TypeError) as error:
        return {
            "failure": "output_failure",
            "cause_type": type(error).__name__,
            "state": state,
            "supervision": run,
        }
    return {**response, "supervision": run}


@signal(tags=["generation", "hydramp"])
def generate_hydramp(
    *,
    n_target,
    seed,
    snapshot_id,
    bundle,
    limits,
    worker_python,
    qualification_reference=None,
):
    """Run one unfiltered AMP batch through the explicit installed CPU worker.

    The worker must contain this exact PeptideMT source and the pinned installed
    HydrAMP runtime. Returns native evidence, including failures/incompatibilities;
    it does not assess with Macrel, select candidates or certify scientific use.
    Caller review of artifacts/use and host/call permission precedes invocation.
    """
    nonempty_text(snapshot_id, "snapshot_id")
    if type(n_target) is not int or n_target < 1:
        raise ValueError("n_target must be a positive integer")
    if type(seed) is not int or not 0 <= seed < 2**32:
        raise ValueError("seed must be an explicit uint32-range integer")
    if not isinstance(bundle, HydrAMPBundle) or not isinstance(limits, HydrAMPLimits):
        raise TypeError("Expected HydrAMPBundle and HydrAMPLimits")
    nonempty_text(worker_python, "worker_python")
    if not Path(worker_python).is_absolute():
        raise ValueError("worker_python must be absolute; no executable resolution")
    provenance = Provenance(
        "hydramp-torch", bundle.bundle_id, "native", qualification_reference
    )
    request = {
        "schema": "peptidemt.hydramp_request@1",
        "n_target": n_target,
        "seed": seed,
        "snapshot_id": snapshot_id,
        "bundle": {f.name: getattr(bundle, f.name) for f in fields(bundle)},
        "limits": asdict(limits),
        "parent_pid": os.getpid(),
        "consumer_source_sha256": source_manifest(PACKAGE_ROOT),
        "consumer_version": importlib.metadata.version("peptidemt"),
        "bundle_id": bundle.bundle_id,
        "qualification_reference": qualification_reference,
    }
    response = {}
    if n_target > limits.max_records:
        response = {"failure": "input_limit", "cause_type": "RecordLimit"}
    elif sys.platform != "linux":
        response = {"failure": "unsupported_host", "cause_type": "PlatformError"}
    else:
        try:
            with tempfile.TemporaryDirectory(
                prefix="peptidemt-hydramp-", dir=limits.temporary_root
            ) as name:
                response = _execute_worker(request, Path(name), limits, worker_python)
        except (OSError, ValueError, TypeError, KeyError) as error:
            response = {
                "failure": "transport_failure",
                "cause_type": type(error).__name__,
            }
    state = response.get("state", {})
    details = {
        "route": "installed-python/linux-cpu",
        "worker_python": worker_python,
        "bundle": request["bundle"],
        "limits": request["limits"],
        "consumer_source_sha256": request["consumer_source_sha256"],
        "state": state,
        "supervision": response.get("supervision", {}),
        "retries": 0,
        "native_configuration": {
            "mode": "amp",
            "filter_out": False,
            "properties": True,
            "n_attempts": 1,
        },
    }
    if response.get("receipt") is not None:
        try:
            receipt = HydrAMPReceipt.from_json(response["receipt"])
            if (
                receipt.snapshot_id != snapshot_id
                or receipt.seed != seed
                or receipt.requested_count != n_target
                or receipt.provenance.bundle_id != bundle.bundle_id
                or receipt.provenance.provider != "hydramp-torch"
                or receipt.provenance.evidence_kind != "native"
                or receipt.provenance.qualification_reference != qualification_reference
            ):
                raise ValueError("Worker receipt does not match submitted request")
        except (ValueError, TypeError, KeyError) as error:
            details["unreceived_receipt"] = response["receipt"]
            response = {
                **response,
                "failure": "output_failure",
                "cause_type": type(error).__name__,
            }
            receipt = HydrAMPReceipt(
                snapshot_id, n_target, seed, (), (), provenance, completed=False
            )
    else:
        receipt = HydrAMPReceipt(
            snapshot_id, n_target, seed, (), (), provenance, completed=False
        )
    if response.get("failure"):
        details["failure"] = {k: response[k] for k in ("failure", "cause_type")}
        if "cause_message" in response:
            details["failure"]["cause_message"] = response["cause_message"]
        receipt = replace(
            receipt, completed=False, failures=(*receipt.failures, response["failure"])
        )
    from ._attribution import hydramp_attribution

    details["scientific_attribution"] = hydramp_attribution(state, snapshot_id)
    receipt = replace(
        receipt,
        provenance=replace(
            provenance, details={**dict(receipt.provenance.details), **details}
        ),
    )
    if response.get("failure"):
        diagnostics.warn(
            HydrAMPFailureWarning(
                stage=response["failure"], cause_type=response["cause_type"]
            )
        )
    return receipt
