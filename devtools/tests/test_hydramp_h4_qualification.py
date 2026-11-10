"""Artificial budget/transport tests; every scientific provider import blocked."""

import importlib.util
import json
import os
import sys
from pathlib import Path

import pytest

from peptidemt import Provenance, ProviderRow, ResultSet, prepare_sequences
from peptidemt._hydramp_receiving import HydrAMPReceipt

spec = importlib.util.spec_from_file_location(
    "h4_qualification_test", Path(__file__).parents[1] / "hydramp_h4_qualification.py"
)
tool = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tool)


@pytest.fixture
def plan(tmp_path):
    return {
        "schema": "peptidemt.hydramp_h4_plan@1",
        "requests": [{"seed": 1001, "count": 16}, {"seed": 1002, "count": 16}],
        "control_sequences": ["ACD", "RRK", "AA", "F"],
        "call_budget": {
            "generation_calls": 2,
            "decoder_forwards": 2,
            "amp_forwards": 2,
            "mic_forwards": 2,
            "descriptor_bundles": 2,
            "pca_numeric_loads": 1,
            "pca_inverse_transforms": 2,
            "macrel_calls": 3,
            "macrel_proposed_records_max": 36,
            "onnx_head_executions_max": 6,
            "retries": 0,
        },
        "pinned_files": {},
        "work_dir": str(tmp_path),
    }


@pytest.mark.parametrize(
    "key",
    [
        "generation_calls",
        "decoder_forwards",
        "macrel_calls",
        "macrel_proposed_records_max",
        "retries",
    ],
)
def test_expanded_budget_is_rejected(plan, key):
    tool.validate(plan)
    plan["call_budget"][key] += 1
    with pytest.raises(ValueError, match="budget"):
        tool.validate(plan)


def test_changed_seed_or_control_size_rejected(plan):
    plan["requests"][0]["seed"] = 999
    with pytest.raises(ValueError, match="requests"):
        tool.validate(plan)
    plan["requests"][0]["seed"] = 1001
    plan["control_sequences"].pop()
    with pytest.raises(ValueError, match="controls"):
        tool.validate(plan)


def test_no_authorization_blocks_before_any_scientific_worker(plan, monkeypatch):
    called = []
    monkeypatch.setattr(tool, "generation_worker", lambda *a: called.append(True))
    with pytest.raises(FileNotFoundError):
        tool.worker(plan, "generation", "not-approved")
    assert not called


def test_approval_for_different_plan_is_not_accepted(plan):
    (Path(plan["work_dir"]) / "authorization.json").write_text(
        json.dumps(
            {"plan_sha256": "other", "investigator_reference": "artificial test"}
        )
    )
    with pytest.raises(ValueError, match="approval"):
        tool.authorized(plan, "current")


def test_ledger_records_attempt_before_call_and_blocks_refill(tmp_path):
    path = tmp_path / "ledger.json"
    ledger = tool.Ledger(path, {"model": 1})
    ledger.reserve("model")
    assert json.loads(path.read_text())["attempted"] == {"model": 1}
    assert not json.loads(path.read_text())["completed"]
    ledger.done("model")
    with pytest.raises(RuntimeError, match="exhausted"):
        ledger.reserve("model")
    with pytest.raises(FileExistsError):
        tool.Ledger(path, {"model": 1})


def test_pinned_source_change_stops_in_preflight(plan, tmp_path):
    p = tmp_path / "source.py"
    p.write_text("original")
    plan["pinned_files"][str(p)] = tool.digest(p)
    assert tool.preflight(plan)["model_weight_pca_loads"] == 0
    p.write_text("changed")
    with pytest.raises(ValueError, match="changed"):
        tool.preflight(plan)


def payload():
    return {
        "request": {"seed": 1001, "count": 1},
        "seed": 1001,
        "native_results": [
            {
                "sequence": "ACD",
                "amp": 0.5,
                "mic": 0.25,
                "length": 3,
                "hydrophobicity": 0.1,
                "hydrophobic_moment": 0.2,
                "charge": 1.0,
                "isoelectric_point": 7.0,
            }
        ],
        "returned_input_indices": [0],
        "sequences": ["ACD"],
        "arrays": {
            name: {"dtype": dtype, "values": values}
            for name, dtype, values in [
                ("sampled_latents", "float64", [[1 + 2**-30]]),
                ("conditioned", "float64", [[1 + 2**-30]]),
                ("tokens", "int64", [[1, 0, 2, 3]]),
                ("amp", "float32", [0.5]),
                ("mic", "float32", [0.25]),
                ("decoder_input", "float32", [[1.0]]),
                ("pca_projected", "float64", [[1 + 2**-30]]),
            ]
        },
    }


def test_worker_transport_preserves_zero_tokens_and_precision_without_models():
    receipt = tool.receive_payload(
        payload(),
        HydrAMPReceipt,
        Provenance("invented", "fixture", "controlled-fixture"),
    )
    assert receipt.issues == ()
    trace = receipt.inputs[0].proposal.context["generation"]["original_trace"]
    assert trace["tokens"] == (1, 0, 2, 3)
    assert trace["conditioned"] == (1 + 2**-30,)
    assert trace["decoder_input"] == (1.0,)


def test_worker_transport_rejects_object_arrays():
    data = payload()
    data["arrays"]["tokens"]["dtype"] = "object"
    with pytest.raises(ValueError, match="dtype"):
        tool.receive_payload(
            data,
            HydrAMPReceipt,
            Provenance("invented", "fixture", "controlled-fixture"),
        )


def test_portable_generator_provenance_keeps_terms_and_descriptor_meanings():
    plan = {
        "generation_profile": {
            "inventory": [
                {"name": n, "version": v}
                for n, v in [
                    ("hydramp-torch", "0.0.0.dev3"),
                    ("torch", "2.15.0+cpu"),
                    ("numpy", "2.4.6"),
                    ("modlamp", "4.3.3"),
                ]
            ],
            "python_version": "artificial runtime",
        },
        "hydramp_source_commit": "original-source",
        "starter_commit": "original-starter",
        "executing_plan_sha256": "current-plan",
        "checkpoint_hashes": {"layer.npy": "pinned"},
        "numeric_pca": "pca.npz",
        "receiving_source": "receiving.py",
        "pinned_files": {"pca.npz": "pca-digest", "receiving.py": "consumer-digest"},
    }
    details = tool.generation_provenance_details(
        plan, {"sha256": "payload-digest", "cached_same_provider_return_exact": False}
    )
    assert details["qualification_plan_sha256"] == "current-plan"
    assert details["descriptor_profile"]["charge"] == {"pH": 7, "amide": True}
    assert details["descriptor_profile"]["isoelectric_point"] == {"amide": False}
    assert not details["scientific_acceptance"]
    assert details["numeric_pca_sha256"] == "pca-digest"


def result(sequences, rows):
    return ResultSet(
        "fixture",
        prepare_sequences(sequences),
        rows,
        Provenance("invented", "fixture", "controlled-fixture"),
    )


def row(token, sequence):
    return ProviderRow(
        token,
        {
            "Sequence": sequence,
            "AMP_probability": 0.1,
            "is_AMP": False,
            "Hemolytic_probability": 0.1,
            "Hemolytic": "NonHemo",
            "AMP_family": "ALP",
        },
    )


def test_control_cannot_pass_with_a_missing_compatible_output():
    with pytest.raises(ValueError, match="Compatible"):
        tool.check_assessment_result(result(["ACD", "RRK"], [row("input-0", "ACD")]))


def test_incompatible_inputs_are_retained_and_negatives_are_usable():
    data = result(["ACD", "MKW"], [row("input-0", "ACD")])
    assert len(tool.check_assessment_result(data)) == 1
    assert len(data.inputs) == 2


def test_process_tree_rss_sums_descendants_without_counting_threads(monkeypatch):
    monkeypatch.setattr(tool, "process_tree", lambda pid: {10, 11})
    original = Path.read_text

    def status(path, *args, **kwargs):
        if str(path) == "/proc/10/status":
            return "VmRSS:\t100 kB\n"
        if str(path) == "/proc/11/status":
            return "VmRSS:\t200 kB\n"
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "read_text", status)
    assert tool.tree_rss(10) == 300 * 1024


def test_output_measurement_survives_removed_transport_file(tmp_path, monkeypatch):
    (tmp_path / "kept").write_bytes(b"data")
    removed = tmp_path / "removed"
    removed.write_bytes(b"temporary")
    original = Path.stat

    def missing(path, *args, **kwargs):
        if path == removed:
            raise FileNotFoundError
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "stat", missing)
    assert tool.output_size(tmp_path) == 4


def test_wall_stop_terminates_artificial_worker_process_group(
    plan, tmp_path, monkeypatch
):
    script = tmp_path / "artificial_worker.py"
    script.write_text(
        "import subprocess,sys,time\nfrom pathlib import Path\np=subprocess.Popen([sys.executable,'-I','-c','import time;time.sleep(10)'])\nPath('child-pid').write_text(str(p.pid))\ntime.sleep(10)\n"
    )
    plan.update(
        resource_limits={
            "minimum_available_bytes": 0,
            "minimum_free_disk_bytes": 0,
            "worker_address_space_bytes": 1024**3,
            "generation_wall_seconds": 0.2,
            "tree_rss_stop_bytes": 512 * 1024**2,
            "output_stop_bytes": 1024**2,
        },
        generation_profile={"python": sys.executable},
    )
    plan["pinned_files"][str(script)] = tool.digest(script)
    path = tmp_path / "plan.json"
    path.write_text(json.dumps(plan))
    sha = tool.digest(path)
    (tmp_path / "authorization.json").write_text(
        json.dumps(
            {
                "plan_sha256": sha,
                "investigator_reference": "artificial process-control fixture,not scientific authorization",
            }
        )
    )
    (tmp_path / "logs").mkdir()
    monkeypatch.setattr(tool, "__file__", str(script))
    result = tool.run_stage(path, "generation", sha)
    assert result["stop_reason"] == "stage wall limit" and result["exit_code"] != 0
    child_pid = int((tmp_path / "child-pid").read_text())
    try:
        state = Path(f"/proc/{child_pid}/status").read_text()
    except FileNotFoundError:
        return
    assert "State:\tZ" in state
    try:
        assert os.getpgid(child_pid) != os.getpgrp()
    except ProcessLookupError:
        pass
