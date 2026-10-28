"""One bounded native Python route; core replay never imports this provider."""

import json
import math
import os
import subprocess
import sys
import tempfile
import time
from dataclasses import asdict, dataclass
from pathlib import Path

from smonitor import signal
from smonitor.integrations import register_provider

from ._attribution import completed_attribution
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
    There are no retries. Optional CPU/thread controls apply only to the child.
    """

    max_records: int
    max_input_bytes: int
    wall_seconds: float
    memory_bytes: int
    intra_op_threads: int | None = None
    blas_threads: int | None = None
    cpu_ids: tuple[int, ...] | None = None
    nice: int = 0
    min_available_memory_bytes: int = 0
    temporary_root: str | None = None

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
        for name in ("intra_op_threads", "blas_threads"):
            value = getattr(self, name)
            if value is not None and (type(value) is not int or value <= 0):
                raise ValueError(f"{name} must be None or a positive integer")
        if self.cpu_ids is not None and (
            not isinstance(self.cpu_ids, tuple)
            or not self.cpu_ids
            or any(type(cpu) is not int or cpu < 0 for cpu in self.cpu_ids)
            or len(set(self.cpu_ids)) != len(self.cpu_ids)
        ):
            raise ValueError(
                "cpu_ids must be None or distinct nonnegative integers in a tuple"
            )
        if type(self.nice) is not int or not 0 <= self.nice <= 19:
            raise ValueError("nice must be an integer from 0 through 19")
        if (
            type(self.min_available_memory_bytes) is not int
            or self.min_available_memory_bytes < 0
        ):
            raise ValueError("min_available_memory_bytes must be a nonnegative integer")
        if self.temporary_root is not None:
            nonempty_text(self.temporary_root, "temporary_root")
            if not Path(self.temporary_root).is_absolute():
                raise ValueError("temporary_root must be an absolute path")


def _available_memory_bytes():
    for line in Path("/proc/meminfo").read_text().splitlines():
        if line.startswith("MemAvailable:"):
            return int(line.split()[1]) * 1024
    raise OSError("Linux MemAvailable is unavailable")


def _worker_environment(limits):
    environment = os.environ.copy()
    if limits.blas_threads is not None:
        for name in (
            "OPENBLAS_NUM_THREADS",
            "OMP_NUM_THREADS",
            "MKL_NUM_THREADS",
            "NUMEXPR_NUM_THREADS",
        ):
            environment[name] = str(limits.blas_threads)
    return environment


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
        env=_worker_environment(limits),
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
            if (
                limits.min_available_memory_bytes
                and _available_memory_bytes() < limits.min_available_memory_bytes
            ):
                raise MemoryError(
                    "Host MemAvailable is below the caller's required headroom"
                )
            with tempfile.TemporaryDirectory(
                prefix="peptidemt-macrel-", dir=limits.temporary_root
            ) as work:
                response = _execute_worker(
                    {
                        "records": submitted,
                        "memory_bytes": limits.memory_bytes,
                        "intra_op_threads": limits.intra_op_threads,
                        "cpu_ids": limits.cpu_ids,
                        "nice": limits.nice,
                    },
                    Path(work),
                    limits,
                )
        except subprocess.TimeoutExpired:
            response = {"failure": "timeout", "cause_type": "TimeoutExpired"}
        except MemoryError:
            response = {"failure": "host_memory_guard", "cause_type": "MemoryError"}
        except (OSError, ValueError, TypeError, KeyError) as error:
            response = {
                "failure": "transport_failure",
                "cause_type": type(error).__name__,
            }
    details["elapsed_seconds"] = time.monotonic() - started
    details.update(response.get("details", {}))
    details["scientific_attribution"] = completed_attribution(details, snapshot_id)
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
