"""Explicit isolated HydrAMP analogue proposals; assessment remains separate."""

import hashlib
import importlib.metadata
import json
import os
import sys
import tempfile
from collections.abc import Mapping
from dataclasses import asdict, dataclass, fields, replace
from pathlib import Path

from smonitor import signal

from ._analogue_receiving import (
    HydrAMPAnalogueReceipt,
    _ordered_parents,
    analogue_input_issues,
)
from ._data import encode, freeze, mapping, nonempty_text
from ._diagnostics import PACKAGE_ROOT, HydrAMPFailureWarning
from ._diagnostics import bundle as diagnostics
from ._hydramp_process import source_manifest
from .hydramp import HydrAMPLimits, _execute_worker, _manifest
from .inputs import InputRecord, prepare_sequences
from .results import Provenance


@dataclass(frozen=True)
class HydrAMPAnalogueBundle:
    """Pinned modern analogue resources; neither PCA nor modlAMP is required.

    evidence_kind is a declared role, not authenticated origin. Controlled
    artifacts keep their role through worker receiving and saved replay.
    """

    checkpoint_root: str
    checkpoint_sha256: Mapping
    provider_source_sha256: Mapping
    expected_versions: Mapping
    source_commit: str
    starter_commit: str
    use_reference: str
    evidence_kind: str = "native"

    def __post_init__(self):
        nonempty_text(self.checkpoint_root, "checkpoint_root")
        if not Path(self.checkpoint_root).is_absolute():
            raise ValueError("checkpoint_root must be absolute")
        for name in ("source_commit", "starter_commit", "use_reference"):
            nonempty_text(getattr(self, name), name)
        for name in ("checkpoint_sha256", "provider_source_sha256"):
            object.__setattr__(self, name, _manifest(getattr(self, name)))
        versions = mapping(self.expected_versions)
        if not {"hydramp-torch", "numpy", "torch"} <= set(versions):
            raise ValueError("Expected exact HydrAMP/NumPy/Torch versions")
        for name, value in versions.items():
            nonempty_text(name, "distribution name")
            nonempty_text(value, "distribution version")
        object.__setattr__(self, "expected_versions", versions)
        if self.evidence_kind not in ("native", "controlled-fixture"):
            raise ValueError("Expected native or controlled-fixture evidence")

    @property
    def bundle_id(self):
        value = {
            f.name: getattr(self, f.name)
            for f in fields(self)
            if f.name != "checkpoint_root"
        }
        return (
            "sha256:"
            + hashlib.sha256(
                json.dumps(encode(freeze(value)), sort_keys=True).encode()
            ).hexdigest()
        )


@signal(tags=["generation", "hydramp", "redesign"])
def redesign_hydramp(
    parents,
    *,
    seed,
    temperature,
    n_attempts,
    snapshot_id,
    bundle,
    limits,
    worker_python,
    qualification_reference=None,
):
    """Produce analogue proposals only; no implicit Macrel call or selection.

    Use prepare_sequences/FASTA tools or supply unchanged SequenceRecords.
    All parents survive admission; compatible ones form one ordered native batch.
    Actual pretrained execution requires prior bundle/use and host/call approval.
    """
    if isinstance(parents, (str, bytes, Mapping)):
        raise TypeError("Expected a batch of parent records")
    parents = tuple(parents)
    parents = (
        _ordered_parents(parents)
        if any(isinstance(p, InputRecord) for p in parents)
        else prepare_sequences(parents)
    )
    if not isinstance(bundle, HydrAMPAnalogueBundle) or not isinstance(
        limits, HydrAMPLimits
    ):
        raise TypeError("Expected HydrAMPAnalogueBundle and HydrAMPLimits")
    nonempty_text(worker_python, "worker_python")
    if not Path(worker_python).is_absolute():
        raise ValueError("worker_python must be absolute")
    submitted = tuple(p.occurrence for p in parents if not analogue_input_issues(p))
    provenance = Provenance(
        "hydramp-torch", bundle.bundle_id, bundle.evidence_kind, qualification_reference
    )
    base = HydrAMPAnalogueReceipt(
        snapshot_id,
        parents,
        seed,
        temperature,
        n_attempts,
        submitted,
        provenance,
        completed=False,
    )
    request = {
        "schema": "peptidemt.hydramp_analogue_request@1",
        "request_id": base.content_id,
        "parents": base._data()["parents"],
        "submitted_parent_indices": submitted,
        "seed": seed,
        "temperature": temperature,
        "n_attempts": n_attempts,
        "snapshot_id": snapshot_id,
        "qualification_reference": qualification_reference,
        "bundle": {f.name: getattr(bundle, f.name) for f in fields(bundle)},
        "bundle_id": bundle.bundle_id,
        "limits": asdict(limits),
        "parent_pid": os.getpid(),
        "consumer_source_sha256": source_manifest(PACKAGE_ROOT),
        "consumer_version": importlib.metadata.version("peptidemt"),
    }
    response = {}
    if not submitted:
        receipt = replace(base, completed=True)
    elif (
        len(submitted) * n_attempts > limits.max_records
        or len(json.dumps(encode(freeze(request))).encode()) > limits.max_output_bytes
    ):
        response = {"failure": "input_limit", "cause_type": "ExecutionLimit"}
        receipt = base
    elif sys.platform != "linux":
        response = {"failure": "unsupported_host", "cause_type": "PlatformError"}
        receipt = base
    else:
        receipt = base
        try:
            with tempfile.TemporaryDirectory(
                prefix="peptidemt-analogue-", dir=limits.temporary_root
            ) as work:
                response = _execute_worker(
                    request,
                    Path(work),
                    limits,
                    worker_python,
                    request_module="peptidemt._hydramp_analogue_cli",
                    response_schema="peptidemt.hydramp_analogue_worker@1",
                )
        except (OSError, ValueError, TypeError, KeyError) as error:
            response = {
                "failure": "transport_failure",
                "cause_type": type(error).__name__,
            }
        if response.get("receipt") is not None:
            try:
                received = HydrAMPAnalogueReceipt.from_json(response["receipt"])
                a, b = received._data(), base._data()
                if any(
                    encode(a[k]) != encode(b[k])
                    for k in (
                        "snapshot_id",
                        "parents",
                        "seed",
                        "temperature",
                        "n_attempts",
                        "submitted_parent_indices",
                        "provenance",
                    )
                ):
                    raise ValueError(
                        "Worker analogue receipt does not match the request"
                    )
                if not response.get("failure") and (
                    not received.completed or received.issues
                ):
                    raise ValueError("Worker analogue evidence did not pass receiving")
                receipt = received
            except (ValueError, TypeError, KeyError, AttributeError) as error:
                response = {
                    **response,
                    "unreceived_receipt": response["receipt"],
                    "failure": "output_failure",
                    "cause_type": type(error).__name__,
                }
    state = response.get("state", {})
    if response.get("failure"):
        receipt = replace(
            receipt, completed=False, failures=(*receipt.failures, response["failure"])
        )
    from ._attribution import hydramp_attribution

    details = {
        "route": "installed-python/linux-cpu/analogue",
        "request_id": request["request_id"],
        "bundle": request["bundle"],
        "limits": request["limits"],
        "consumer_source_sha256": request["consumer_source_sha256"],
        "state": state,
        "supervision": response.get("supervision", {}),
        "retries": 0,
        "execution": "not-requested:no-compatible-parents"
        if not submitted
        else "requested",
        "scientific_attribution": hydramp_attribution(
            state, snapshot_id, analogue=True
        ),
    }
    for name in ("failure", "cause_type", "cause_message", "unreceived_receipt"):
        if name in response:
            details[name] = response[name]
    receipt = replace(
        receipt, progress=state, provenance=replace(provenance, details=details)
    )
    if response.get("failure"):
        diagnostics.warn(
            HydrAMPFailureWarning(
                stage=response["failure"], cause_type=response["cause_type"]
            )
        )
    return receipt
