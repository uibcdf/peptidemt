"""One bounded native Python route; core replay never imports this provider."""

import json
import math
import subprocess
import sys
import tempfile
import time
from dataclasses import asdict, dataclass
from pathlib import Path

from smonitor import signal
from smonitor.integrations import register_provider

from ._data import decode, encode, freeze, nonempty_text
from ._diagnostics import PACKAGE_ROOT, MacrelFailureWarning, bundle
from .inputs import InputRecord
from .results import Provenance, ProviderRow, ResultSet

register_provider(PACKAGE_ROOT, provider="peptidemt")


@dataclass(frozen=True)
class MacrelLimits:
    """Caller-authorized engineering bounds; no implicit host-use authorization.

    Record/UTF-8 byte limits cover submitted sequences and occurrence tokens.
    Wall time covers the single child, including imports and both heads.
    Linux RLIMIT_AS limits child virtual address space, not resident memory.
    There are no retries. ONNX retains its native CPU/thread configuration.
    """

    max_records: int
    max_input_bytes: int
    wall_seconds: float
    memory_bytes: int

    def __post_init__(self):
        for name in ("max_records", "max_input_bytes", "memory_bytes"):
            if type(getattr(self, name)) is not int or getattr(self, name) <= 0:
                raise ValueError(f"{name} must be a positive integer")
        if (
            type(self.wall_seconds) not in (int, float)
            or not math.isfinite(self.wall_seconds)
            or self.wall_seconds <= 0
        ):
            raise ValueError("wall_seconds must be a positive finite number")


def _execute_worker(request, directory, limits):
    request_path = directory / "request.json"
    response_path = directory / "response.json"
    request_path.write_text(json.dumps(encode(freeze(request))), encoding="utf-8")
    completed = subprocess.run(
        [
            sys.executable,
            "-I",
            "-m",
            "peptidemt._macrel_cli",
            str(request_path),
            str(response_path),
        ],
        cwd=directory,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        timeout=limits.wall_seconds,
        check=False,
    )
    if completed.returncode:
        return {
            "failure": "worker_failure",
            "cause_type": "ChildProcessError",
            "returncode": completed.returncode,
        }
    return decode(json.loads(response_path.read_text(encoding="utf-8")))


@signal(tags=["assessment", "macrel"])
def assess_macrel(
    inputs,
    *,
    snapshot_id: str,
    limits: MacrelLimits,
    qualification_reference: str | None = None,
) -> ResultSet:
    """Assess prepared in-memory occurrences, preserving incompatible proposals.

    The selected route is installed Macrel 1.6.1 on Linux CPU. MolSysMT
    serializes compatible views; no local FASTA reader is called. Operational
    failures are returned with diagnostics and per-submitted-occurrence causes.
    Missing/malformed native rows remain explicit through ResultSet validation.
    A qualification reference is a caller assertion, never certification.
    """
    nonempty_text(snapshot_id, "snapshot_id")
    if not isinstance(limits, MacrelLimits):
        raise TypeError("limits must be MacrelLimits")
    inputs = tuple(inputs)
    if any(
        not isinstance(item, InputRecord) or item.occurrence != index
        for index, item in enumerate(inputs)
    ):
        raise ValueError("inputs must retain complete original occurrence order")
    # Validate attribution before any provider-side effects.
    provenance = Provenance(
        "Macrel", "macrel-1.6.1:unexecuted", "native", qualification_reference
    )
    submitted = [
        (item.token, item.provider_sequence)
        for item in inputs
        if item.provider_sequence is not None
    ]
    details = {
        "route": "installed-python/linux-cpu",
        "keep_negatives": True,
        "submitted": submitted,
        "limits": asdict(limits),
        "retries": 0,
    }
    response = {"rows": []}
    started = time.monotonic()
    if not submitted:
        details["execution"] = "not-requested:no-compatible-inputs"
    elif (
        len(submitted) > limits.max_records
        or sum(len(t.encode()) + len(s.encode()) for t, s in submitted)
        > limits.max_input_bytes
    ):
        response = {"failure": "input_limit", "cause_type": "ExecutionLimit"}
    elif sys.platform != "linux":
        response = {"failure": "unsupported_host", "cause_type": "PlatformError"}
    else:
        try:
            with tempfile.TemporaryDirectory(prefix="peptidemt-macrel-") as work:
                response = _execute_worker(
                    {"records": submitted, "memory_bytes": limits.memory_bytes},
                    Path(work),
                    limits,
                )
        except subprocess.TimeoutExpired:
            response = {"failure": "timeout", "cause_type": "TimeoutExpired"}
        except (OSError, ValueError, TypeError, KeyError) as error:
            response = {
                "failure": "transport_failure",
                "cause_type": type(error).__name__,
            }
    details["elapsed_seconds"] = time.monotonic() - started
    details.update(response.get("details", {}))
    failures = {}
    if "failure" in response:
        failures = {token: response["failure"] for token, _ in submitted}
        details["failure"] = {k: v for k, v in response.items() if k != "details"}
        bundle.warn(
            MacrelFailureWarning(
                stage=response["failure"], cause_type=response["cause_type"]
            )
        )
    return ResultSet(
        snapshot_id,
        inputs,
        tuple(
            ProviderRow(row["token"], row["values"]) for row in response.get("rows", [])
        ),
        Provenance(
            provenance.provider,
            response.get("bundle_id", provenance.bundle_id),
            provenance.evidence_kind,
            provenance.qualification_reference,
            details,
        ),
        failures,
    )
