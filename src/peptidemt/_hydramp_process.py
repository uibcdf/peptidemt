"""Linux-only supervision for one explicitly configured HydrAMP worker."""

import hashlib
import os
import shutil
import signal
import stat
import subprocess
import time
from pathlib import Path


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def source_manifest(directory):
    root = Path(directory)
    return {
        str(path.relative_to(root)): sha256(path) for path in sorted(root.rglob("*.py"))
    }


def available_memory():
    return next(
        int(line.split()[1]) * 1024
        for line in Path("/proc/meminfo").read_text().splitlines()
        if line.startswith("MemAvailable:")
    )


def tree_rss(pid):
    total, seen, pending = 0, set(), [pid]
    while pending:
        current = pending.pop()
        if current in seen:
            continue
        seen.add(current)
        try:
            total += next(
                int(line.split()[1]) * 1024
                for line in Path(f"/proc/{current}/status").read_text().splitlines()
                if line.startswith("VmRSS:")
            )
            # A subprocess belongs to the creating thread's children list.
            # Inspect every task, while counting the shared process RSS once.
            for children in Path(f"/proc/{current}/task").glob("*/children"):
                try:
                    pending.extend(int(p) for p in children.read_text().split())
                except (FileNotFoundError, ProcessLookupError):
                    continue
        except (FileNotFoundError, ProcessLookupError, StopIteration):
            pass
    return total


def output_bytes(directory):
    total = 0
    for path in Path(directory).rglob("*"):
        try:
            details = path.stat()
        except FileNotFoundError:
            continue
        if stat.S_ISREG(details.st_mode):
            total += details.st_size
    return total


def supervise(command, directory, limits, *, include_supervisor_rss=False):
    """Return operational facts; interruptions propagate after group cleanup."""
    directory = Path(directory)
    if (
        available_memory() < limits.min_available_memory_bytes
        or shutil.disk_usage(directory).free < limits.min_free_disk_bytes
    ):
        return {"failure": "host_resource_guard", "started": False}
    environment = os.environ.copy()
    environment.update(
        CUDA_VISIBLE_DEVICES="-1",
        OMP_NUM_THREADS=str(limits.threads),
        OPENBLAS_NUM_THREADS=str(limits.threads),
        MKL_NUM_THREADS=str(limits.threads),
        NUMEXPR_NUM_THREADS=str(limits.threads),
        TMPDIR=str(directory),
        MPLCONFIGDIR=str(directory / "mpl"),
        TORCH_HOME=str(directory / "torch-cache"),
    )
    start, peak, stop = time.monotonic(), 0, None
    child = subprocess.Popen(
        command,
        cwd=directory,
        env=environment,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True,
    )
    try:
        while child.poll() is None:
            peak = max(
                peak, tree_rss(os.getpid() if include_supervisor_rss else child.pid)
            )
            if time.monotonic() - start > limits.wall_seconds:
                stop = "timeout"
            elif peak > limits.rss_stop_bytes:
                stop = "resident_memory_guard"
            elif available_memory() < limits.min_available_memory_bytes:
                stop = "host_resource_guard"
            elif output_bytes(directory) > limits.max_output_bytes:
                stop = "output_limit"
            if stop:
                break
            time.sleep(0.05)
    finally:
        try:
            os.killpg(child.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        code = child.wait()
    # A very fast worker can exit between samples. Check retained output too.
    if output_bytes(directory) > limits.max_output_bytes:
        stop = "output_limit"
    result = {
        "started": True,
        "returncode": code,
        "failure": stop or ("worker_failure" if code else None),
        "wall_seconds": time.monotonic() - start,
        "peak_sampled_process_tree_rss_bytes": peak,
        "retained_output_bytes": output_bytes(directory),
        "retry": False,
    }
    if include_supervisor_rss:
        result["rss_scope"] = "supervisor_and_descendants"
    return result


def configure_child(limits, parent_pid):
    """Apply bounds before providers; kill the owned group if its parent dies."""
    import ctypes
    import resource

    if os.getpid() != os.getpgrp():
        raise RuntimeError("Expected a dedicated worker process group")

    def parent_died(signum, frame):
        os.killpg(os.getpgrp(), signal.SIGKILL)

    signal.signal(signal.SIGTERM, parent_died)
    libc = ctypes.CDLL(None, use_errno=True)
    if libc.prctl(1, signal.SIGTERM, 0, 0, 0) != 0:
        raise OSError(ctypes.get_errno(), "Unable to set parent-death signal")
    if os.getppid() != parent_pid:
        parent_died(None, None)
    resource.setrlimit(resource.RLIMIT_AS, (limits["address_space_bytes"],) * 2)
    cpus = set(limits["cpu_ids"])
    if not cpus <= os.sched_getaffinity(0):
        raise ValueError("Requested CPUs exceed inherited affinity")
    os.sched_setaffinity(0, cpus)
    current_nice = os.nice(0)
    if limits["nice"] > current_nice:
        os.nice(limits["nice"] - current_nice)
