"""Live qualification is explicitly selected; these tests execute no engine."""

import json
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

from peptidemt import MacrelLimits, assess_macrel, prepare_sequences
from peptidemt import _macrel_worker as worker
from peptidemt import macrel as route
from peptidemt._diagnostics import MacrelFailureWarning


def test_qualification_defaults_to_a_plan_without_importing_any_provider(tmp_path):
    script = Path(__file__).resolve().parents[1] / "devtools/qualify_macrel.py"
    program = """
import runpy,sys
script=sys.argv[1]
sys.argv=[script]
namespace=runpy.run_path(script,run_name='qualification_plan')
assert namespace['main']([])==0
assert not any(n in sys.modules for n in ('peptidemt','macrel','molsysmt','onnxruntime','ackredit'))
"""
    completed = subprocess.run(
        [sys.executable, "-I", "-c", program, str(script)],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        check=True,
    )
    plan = json.loads(completed.stdout)
    assert plan["status"] == "not-executed" and plan["retries"] == 0


def test_live_qualification_requires_an_explicit_authorization_reference(tmp_path):
    script = Path(__file__).resolve().parents[1] / "devtools/qualify_macrel.py"
    completed = subprocess.run(
        [
            sys.executable,
            "-I",
            str(script),
            "--allow-live",
            "--output",
            str(tmp_path / "must-not-exist"),
        ],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        check=False,
    )
    assert completed.returncode == 2
    assert "authorization reference" in completed.stderr
    assert not (tmp_path / "must-not-exist").exists()


def test_low_host_memory_prevents_any_worker(monkeypatch, tmp_path):
    monkeypatch.setattr(route, "_available_memory_bytes", lambda: 7 * 1024**3)
    monkeypatch.setattr(
        route,
        "_execute_worker",
        lambda *args: pytest.fail("Worker started without memory headroom"),
    )
    limits = MacrelLimits(
        32,
        8192,
        120,
        4 * 1024**3,
        intra_op_threads=2,
        blas_threads=1,
        min_available_memory_bytes=8 * 1024**3,
        temporary_root=str(tmp_path),
    )
    with pytest.warns(MacrelFailureWarning, match="host_memory_guard"):
        result = assess_macrel(
            prepare_sequences(["ACD"]),
            snapshot_id="controlled-low-memory",
            limits=limits,
        )
    assert result.failures == {"input-0": "host_memory_guard"}


def test_child_numerical_environment_does_not_modify_application(monkeypatch):
    monkeypatch.setenv("OPENBLAS_NUM_THREADS", "9")
    limits = MacrelLimits(1, 64, 10, 4 * 1024**3, blas_threads=1)
    child = route._worker_environment(limits)
    assert all(
        child[name] == "1"
        for name in (
            "OPENBLAS_NUM_THREADS",
            "OMP_NUM_THREADS",
            "MKL_NUM_THREADS",
            "NUMEXPR_NUM_THREADS",
        )
    )
    assert route.os.environ["OPENBLAS_NUM_THREADS"] == "9"


def test_worker_sets_only_allowed_affinity_and_lowers_its_priority(monkeypatch):
    import resource

    calls = []
    monkeypatch.setattr(
        resource, "setrlimit", lambda *args: calls.append(("memory", args))
    )
    monkeypatch.setattr(worker.os, "sched_getaffinity", lambda pid: {0, 1, 2, 3})
    monkeypatch.setattr(
        worker.os,
        "sched_setaffinity",
        lambda pid, cpus: calls.append(("affinity", cpus)),
    )
    monkeypatch.setattr(worker.os, "getpriority", lambda *args: 0)
    monkeypatch.setattr(
        worker.os, "setpriority", lambda *args: calls.append(("priority", args[-1]))
    )
    state = {"details": {}}
    worker._configure_process(
        {
            "memory_bytes": 4 * 1024**3,
            "cpu_ids": (0, 1),
            "nice": 10,
            "intra_op_threads": 2,
        },
        state,
    )
    assert ("affinity", {0, 1}) in calls and ("priority", 10) in calls
    assert state["intra_op_threads"] == 2
    with pytest.raises(ValueError, match="inherited"):
        worker._configure_process(
            {"memory_bytes": 4 * 1024**3, "cpu_ids": (9,)}, {"details": {}}
        )


def test_onnx_options_are_bounded_and_restored_even_when_prediction_fails(monkeypatch):
    captured = []

    class Options:
        def __init__(self):
            self.entries = {}

        def add_session_config_entry(self, key, value):
            self.entries[key] = value

    def original(*args, **kwargs):
        captured.append(kwargs["sess_options"])
        return "controlled-session-not-a-model"

    module = SimpleNamespace(
        InferenceSession=original,
        SessionOptions=Options,
        ExecutionMode=SimpleNamespace(ORT_SEQUENTIAL="sequential"),
    )
    monkeypatch.setitem(sys.modules, "onnxruntime", module)
    with pytest.raises(RuntimeError, match="controlled"):
        with worker._onnx_threads(2):
            assert (
                module.InferenceSession(b"not-a-model")
                == "controlled-session-not-a-model"
            )
            raise RuntimeError("controlled prediction failure")
    assert module.InferenceSession is original
    options = captured[0]
    assert options.intra_op_num_threads == 2 and options.inter_op_num_threads == 1
    assert options.execution_mode == "sequential"
    assert options.entries == {
        "session.intra_op.allow_spinning": "0",
        "session.inter_op.allow_spinning": "0",
    }
