"""D48 receiving/control tests: scalar/method doubles, never neural networks."""

import copy
import importlib.abc
import importlib.util
import json
import os
import struct
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

ROOT = Path(__file__).resolve().parents[2]


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


tool = module("real_test", ROOT / "devtools/hydramp_historical_real.py")
worker = module("worker_test", ROOT / "devtools/hydramp_historical_native_worker.py")
operator = module("operator_test", ROOT / "devtools/hydramp_historical_operator.py")


def fp32(value):
    return struct.unpack("<f", struct.pack("<f", value))[0]


@pytest.fixture
def case(monkeypatch, tmp_path):
    # Three artificial source views, with deliberately invented authority pins.
    # These private test bindings are never accepted by production CLI/profile.
    ids = [tool.digest(s.encode()) for s in ("A", "C", "AA")]
    groups = [
        {"group_id": i, "primary_label": y, "primary_eligible": y is not None}
        for i, y in zip(ids, (1, 0, None))
    ]
    sources = [
        {"raw_sequence_sha256": i, "raw_cells": ["", "", s]}
        for i, s in zip(ids, ("A", "C", "AA"))
    ]
    endpoint = {
        "groups": groups,
        "counts": {"source_observations": 4},
        "source_snapshot": {
            "source_json": {
                "source": json.dumps(
                    {"hydramps_original_measured_tables": {"records": sources}}
                )
            }
        },
    }

    def source(name):
        return {"path": str(tmp_path / name), "bytes": 7, "sha256": "a" * 64}

    audit = {
        "selected_source": {
            k: source(k)
            for k in (
                "legacy_codec",
                "legacy_loader",
                "legacy_MIC_head",
                "modern_codec",
                "modern_inference",
            )
        }
    }
    texts = {"endpoint_json": json.dumps(endpoint), "audit_json": json.dumps(audit)}
    profiles = {
        p: {
            "python": {"path": str(tmp_path / p / "python")},
            "inventory": {"Example": "1"},
        }
        for p in tool.PROVIDERS
    }
    proposal = {
        "D47_endpoint": {"sha256": tool.digest(texts["endpoint_json"].encode())},
        "static_audit": {"sha256": tool.digest(texts["audit_json"].encode())},
        "endpoint_counts": endpoint["counts"],
        "profiles": profiles,
        "source_groups": [
            {"group_id": i, "sequence_length": n} for i, n in zip(ids, (1, 1, 2))
        ],
        "assets": [],
        "requests": [
            {"tag": tag, "indices": indices}
            for tag, indices in (
                ("primary_full", [0, 1, 2]),
                ("repeat_full", [0, 1, 2]),
                ("split_first", [0, 1]),
                ("split_last", [2]),
            )
        ],
    }
    authority = {
        "decision": "D48",
        "not_authorized": {"neural_evaluations": 0},
        "approved_contract_copy": {"path": str(tmp_path / "contract.md")},
    }
    binding = {
        "schema": tool.CASE,
        **texts,
        "authority_json": json.dumps(authority),
        "proposal_json": json.dumps(proposal),
    }
    monkeypatch.setattr(
        tool, "AUTH_SHA", tool.digest(binding["authority_json"].encode())
    )
    monkeypatch.setattr(
        tool, "PROPOSAL_SHA", tool.digest(binding["proposal_json"].encode())
    )
    expected = copy.deepcopy(endpoint)

    def validate(value):
        assert value == expected
        return value

    monkeypatch.setattr(tool.evaluation, "validate_endpoint", validate)
    pin = {"path": str(tmp_path / "worker.py"), "bytes": 1, "sha256": "b" * 64}
    captures = {}
    for p in tool.PROVIDERS:
        rows = [[1] + [0] * 24, [2] + [0] * 24, [1, 1] + [0] * 23]
        dtype = "int32" if p == "legacy" else "int64"
        native = {
            "dtype": dtype,
            "shape": [3, 25],
            "values": rows,
            "native_hex": tool.native_bytes(rows, dtype).hex(),
        }
        runtime = {
            "executable": profiles[p]["python"]["path"],
            "inventory": {"Example": "1"},
            "cpu_ids": [0, 1],
            "numerical_threads": 1,
            "source_origins": {
                k: v for k, v in audit["selected_source"].items() if k.startswith(p)
            },
        }
        raw = {
            "schema": "peptidemt.hydramp_historical_codec_output@1",
            "provider": p,
            "case_sha256": tool.object_digest(binding),
            "native": native,
            "runtime": runtime,
            "codec_operations": {"to_one_hot": 1, "pad": 1}
            if p == "legacy"
            else {"encode_sequences": 1},
            "parameter_files_opened": [],
            "neural_calls": 0,
        }
        facts = {
            "failure": None,
            "returncode": 0,
            "rss_scope": "supervisor_and_descendants",
        }
        command = [
            profiles[p]["python"]["path"],
            "-I",
            "-S",
            "-B",
            pin["path"],
            "codec",
        ]
        captures[p] = {
            "raw_json": json.dumps(raw),
            "worker": pin,
            "command": command,
            "supervision": facts,
        }
    codecs = {
        "schema": tool.CODECS,
        "case": binding,
        "captures": captures,
        "attribution": {
            "status": "control_fixture",
            "completed_operations": [],
            "bibliography": [],
        },
    }
    ready = {
        "schema": tool.READY,
        "codecs": codecs,
        "pins": {
            k: copy.deepcopy(pin)
            for k in (
                "operator",
                "worker",
                "receiver",
                "evaluation",
                "data",
                "supervision",
            )
        },
        "proposal_sha256": tool.PROPOSAL_SHA,
    }
    return ready


def controls(plan, modern=(0.25, 0.75, 0.5)):
    proposal, _ = tool.validate_ready(plan)
    captures = {}
    for p in tool.PROVIDERS:
        codec = json.loads(plan["codecs"]["captures"][p]["raw_json"])
        scores = [0.75, 0.25, 0.5] if p == "legacy" else list(modern)
        events = []
        for request in proposal["requests"]:
            values = [scores[i] for i in request["indices"]]
            n = len(values)
            events.append(
                {
                    "tag": request["tag"],
                    "indices": request["indices"],
                    "MIC": tool.column(values, [n, 1] if p == "legacy" else [n]),
                    "auxiliary_AMP": tool.column([0.5] * n, [n])
                    if p == "modern"
                    else None,
                }
            )
        raw = {
            "schema": "peptidemt.hydramp_historical_score_output@1",
            "evidence_kind": "instrumented_method_double",
            "provider": p,
            "plan_sha256": tool.object_digest(plan),
            "native_input_sha256": tool.digest(
                bytes.fromhex(codec["native"]["native_hex"])
            ),
            "head": "VeltriAMPClassifier_MIC",
            "events": events,
            "attempted": 4,
            "completed": 4,
            "parameter_files_opened": [],
            "model_loads": 0,
            "failure": None,
            "runtime": codec["runtime"],
        }
        captures[p] = {
            "raw_json": json.dumps(raw),
            "supervision": copy.deepcopy(plan["codecs"]["captures"][p]["supervision"]),
            "command": ["explicit_method_double_no_child"],
        }
    return captures


def alter(captures, provider, mutate):
    raw = json.loads(captures[provider]["raw_json"])
    mutate(raw)
    captures[provider]["raw_json"] = json.dumps(raw)


def test_immutable_case_and_original_cells_are_received_without_a_codec(case):
    assert tool.source_views(case["codecs"]["case"]) == ["A", "C", "AA"]
    assert tool.validate_codecs(case["codecs"])["neural_calls"] == 0
    assert tool.inspect(case)["neural_allowance"] == 0


def test_changed_authority_cannot_be_approved_by_metadata(case):
    case["codecs"]["case"]["authority_json"] += "\n"
    with pytest.raises(tool.Error, match="authority/proposal"):
        tool.validate_ready(case)


@pytest.mark.parametrize(
    "mutate,code",
    [
        (lambda x: x["native"]["values"][0].__setitem__(0, 2), "native_bytes"),
        (lambda x: x["native"]["values"][2].__setitem__(0, 0), "native_values"),
        (lambda x: x["native"].__setitem__("dtype", "int32"), "native_dtype"),
        (lambda x: x.__setitem__("neural_calls", 1), "codec_scope"),
        (lambda x: x.__setitem__("neural_calls", False), "codec_scope"),
        (
            lambda x: x["codec_operations"].__setitem__("encode_sequences", 2),
            "codec_calls",
        ),
        (
            lambda x: x["runtime"]["inventory"].__setitem__("Example", "2"),
            "runtime_inventory",
        ),
    ],
)
def test_native_provenance_mutations_reject(case, mutate, code):
    alter(case["codecs"]["captures"], "modern", mutate)
    with pytest.raises(tool.Error) as err:
        tool.validate_ready(case)
    assert err.value.code == code


def test_equal_projection_does_not_justify_different_native_tokens(case):
    def mutate(raw):
        raw["native"]["values"][0][0] = 2
        raw["native"]["native_hex"] = tool.native_bytes(
            raw["native"]["values"], "int64"
        ).hex()

    alter(case["codecs"]["captures"], "modern", mutate)
    with pytest.raises(tool.Error) as err:
        tool.validate_ready(case)
    assert err.value.code == "codec_mismatch"


def test_method_double_perfect_reversed_and_tied_ranking(case):
    for values, expected in (
        ((0.75, 0.25, 0.5), 1.0),
        ((0.25, 0.75, 0.5), 0.0),
        ((0.5, 0.5, 0.5), 0.5),
    ):
        record = tool.receive(
            case, None, controls(case, values), "instrumented_method_double"
        )
        assert (
            record["result"]["contexts"]["primary"]["metrics"][0]["modern_slot_auc"]
            == expected
        )
        assert record["result"]["headline_context"] == "primary"
        assert record["result"]["charged_neural_evaluations"] == 0
        assert (
            record["result"]["status"] == "method_double_only_not_HydrAMP_performance"
        )


def test_repeat_fail_and_favorable_split_cannot_replace_primary(case):
    captures = controls(case)

    def mutate(raw):
        raw["events"][1]["MIC"] = tool.column([0.75, 0.25, 0.5], [3])
        raw["events"][2]["MIC"] = tool.column([0.75, 0.25], [2])

    alter(captures, "modern", mutate)
    result = tool.receive(case, None, captures, "instrumented_method_double")["result"]
    assert result["contexts"]["primary"]["metrics"][0]["modern_slot_auc"] == 0
    assert result["contexts"]["split"]["metrics"][0]["modern_slot_auc"] == 1
    assert result["diagnostics"]["modern"]["repeat"]["status"] == "repeat_FAIL"
    assert result["diagnostics"]["modern"]["split"]["status"] == "batch_sensitive"
    assert result["headline_context"] == "primary"
    assert result["diagnostics"]["modern"]["split"]["primary_binary_rank_changes"]


def test_shared_ambiguity_with_equal_columns_has_no_invented_difference(case):
    result = tool.receive(
        case, None, controls(case, (0.75, 0.25, 0.5)), "instrumented_method_double"
    )["result"]
    for context in result["contexts"].values():
        assert context["paired_ambiguity_range"] == [0, 0]
        assert all(item["paired_difference"] == 0 for item in context["metrics"])


@pytest.mark.parametrize(
    "mutation,code",
    [
        (lambda x: x.__setitem__("head", "NoConvAMPClassifier"), "score_binding"),
        (lambda x: x.__setitem__("provider", "legacy"), "score_binding"),
        (lambda x: x.__setitem__("plan_sha256", "0" * 64), "score_binding"),
        (lambda x: x.__setitem__("native_input_sha256", "0" * 64), "score_input"),
        (lambda x: x["events"][0].__setitem__("indices", [0, 0, 2]), "score_pairing"),
        (
            lambda x: x["events"][0].__setitem__("indices", [False, 1, 2]),
            "score_pairing",
        ),
        (lambda x: x["events"][0]["MIC"]["values"].__setitem__(0, True), "score_value"),
        (
            lambda x: x["events"][0]["MIC"]["values"].__setitem__(0, "0.25"),
            "score_value",
        ),
        (lambda x: x["events"][0]["MIC"]["values"].__setitem__(0, 1.01), "score_value"),
        (
            lambda x: x["events"][0]["MIC"]["values"].__setitem__(0, 0.9),
            "score_precision",
        ),
        (
            lambda x: x["events"][0]["MIC"].__setitem__("native_hex", "00000000"),
            "score_precision",
        ),
        (
            lambda x: x["events"][0]["MIC"].__setitem__("dtype", "float64"),
            "score_shape",
        ),
        (lambda x: x.__setitem__("attempted", 5), "score_accounting"),
        (lambda x: x.__setitem__("completed", 3), "score_accounting"),
        (lambda x: x.__setitem__("model_loads", 1), "score_kind"),
        (lambda x: x.__setitem__("parameter_files_opened", ["fake.npy"]), "score_kind"),
        (
            lambda x: x["runtime"]["source_origins"]["modern_inference"].__setitem__(
                "sha256", "0" * 64
            ),
            "runtime_source",
        ),
    ],
)
def test_bad_learned_pair_provenance_rejects_before_metrics(
    case, monkeypatch, mutation, code
):
    captures = controls(case)
    alter(captures, "modern", mutation)
    monkeypatch.setattr(
        tool.evaluation,
        "_provider",
        lambda: pytest.fail("Metric before input validation"),
    )
    with pytest.raises(tool.Error) as err:
        tool.receive(case, None, captures, "instrumented_method_double")
    assert err.value.code == code


def test_partial_stage_is_retained_and_has_no_imputed_auc(case):
    captures = controls(case)

    def mutate(raw):
        raw["events"] = raw["events"][:1]
        raw["completed"] = 1
        raw["attempted"] = 2
        raw["failure"] = {
            "type": "SimulatedFailure",
            "detail": "method double failed after primary",
        }

    alter(captures, "modern", mutate)
    captures["modern"]["supervision"]["returncode"] = 1
    captures["modern"]["supervision"]["failure"] = "worker_failure"
    record = tool.receive(case, None, captures, "instrumented_method_double")
    assert not record["result"]["complete"]
    assert record["result"]["contexts"]["primary"]["metrics"][0]["modern_slot_auc"] == 0
    assert (
        record["result"]["contexts"]["repeat"]["status"]
        == "incomplete_paired_context_no_AUC"
    )
    assert (
        record["result"]["contexts"]["split"]["status"]
        == "incomplete_paired_context_no_AUC"
    )
    assert (
        json.loads(record["captures"]["modern"]["raw_json"])["failure"]["type"]
        == "SimulatedFailure"
    )


def test_new_real_authority_required_before_dispatch(case, monkeypatch, tmp_path):
    monkeypatch.setattr(operator, "core", tool)
    monkeypatch.setattr(
        operator.process,
        "supervise",
        lambda *a, **k: pytest.fail("D48 dispatched real inference"),
    )
    with pytest.raises(tool.Error) as err:
        operator.run_scoring(case, None, tmp_path / "forbidden")
    assert err.value.code == "execution_authority"
    assert not (tmp_path / "forbidden").exists()
    with pytest.raises(tool.Error):
        tool.receive(case, None, controls(case), "learned_model")


def test_d48_receipt_cannot_be_reused_as_a_real_model_receipt(case):
    with pytest.raises(tool.Error):
        tool.execution_authority(case, case["codecs"]["case"]["authority_json"])
    fake = {
        "schema": tool.EXECUTION,
        "stage": "real_scoring",
        "explicit_investigator_approval": True,
        "ready_plan_sha256": "0" * 64,
        "reply_reference": "test control only",
        "neural_evaluations": 12,
    }
    with pytest.raises(tool.Error):
        tool.execution_authority(case, json.dumps(fake))


def test_native_precision_tie_and_smallest_fp32_increment_are_not_rounded(case):
    next_score = struct.unpack("<f", struct.pack("<I", 0x3F000001))[0]
    captures = controls(case, (next_score, 0.5, 0.5))
    result = tool.receive(case, None, captures, "instrumented_method_double")["result"]
    assert result["contexts"]["primary"]["metrics"][0]["modern_slot_auc"] == 1


def test_saved_replay_has_no_source_or_model_dependency_and_detects_cache_tamper(
    case, tmp_path, monkeypatch
):
    record = tool.receive(case, None, controls(case), "instrumented_method_double")
    output = tmp_path / "record.json"
    tool.save(record, output)

    class Guard(importlib.abc.MetaPathFinder):
        def find_spec(self, fullname, path=None, target=None):
            if fullname.split(".")[0] in {
                "torch",
                "tensorflow",
                "keras",
                "amp",
                "hydramp_torch",
                "molsysmt",
                "macrel",
            }:
                pytest.fail("Model import during replay")

    guard = Guard()
    sys.meta_path.insert(0, guard)
    try:
        assert tool.inspect(tool.load(output)) == record["result"]
    finally:
        sys.meta_path.remove(guard)
    with pytest.raises(FileExistsError):
        tool.save(record, output)
    changed = copy.deepcopy(record)
    changed["result"]["headline_context"] = "split"
    with pytest.raises(tool.Error) as err:
        tool.inspect(changed)
    assert err.value.code == "comparison_cache"
    assert tool.main([str(output)]) == 0
    assert tool.main([str(tmp_path / "missing.json")]) == 2


def test_worker_schedule_uses_exact_existing_methods_and_retains_failure_prefix(case):
    proposal, _ = tool.validate_ready(case)

    class Rows:
        def __getitem__(self, indices):
            return indices

    charged = []
    events = []

    def call(indices):
        return tool.column([0.5] * len(indices), [len(indices)]), tool.column(
            [0.5] * len(indices), [len(indices)]
        )

    result = worker.schedule(
        proposal,
        "modern",
        Rows(),
        call,
        lambda r: charged.append(r["tag"]),
        events.append,
    )
    assert charged == [r["tag"] for r in proposal["requests"]]
    assert result == events and sum(len(x["indices"]) for x in result) == 9
    charged.clear()
    events.clear()

    def fail(indices):
        if len(charged) > 1:
            raise ValueError("injected method-double failure")
        return call(indices)

    with pytest.raises(ValueError):
        worker.schedule(
            proposal,
            "modern",
            Rows(),
            fail,
            lambda r: charged.append(r["tag"]),
            events.append,
        )
    assert len(charged) == 2 and len(events) == 1


def test_aggregate_supervision_counts_controller_as_well_as_real_stdlib_child(tmp_path):
    process = operator.process
    limit = SimpleNamespace(
        min_available_memory_bytes=1,
        min_free_disk_bytes=1,
        threads=1,
        wall_seconds=3,
        rss_stop_bytes=process.tree_rss(os.getpid()) // 2,
        max_output_bytes=1024**2,
    )
    command = [sys.executable, "-I", "-c", "import time;time.sleep(.2)"]
    old = tmp_path / "old"
    old.mkdir()
    new = tmp_path / "aggregate"
    new.mkdir()
    normal = process.supervise(command, old, limit)
    aggregate = process.supervise(command, new, limit, include_supervisor_rss=True)
    assert normal["failure"] is None and "rss_scope" not in normal
    assert aggregate["failure"] == "resident_memory_guard"
    assert aggregate["rss_scope"] == "supervisor_and_descendants"


def test_operator_has_no_scoring_authority_cli_flag(capsys):
    with pytest.raises(SystemExit) as error:
        operator.main(["run-scoring", "--plan", "x.json", "--directory", "y"])
    assert error.value.code == 2
    assert "execution-authority" in capsys.readouterr().err


def test_codec_allowance_cannot_be_retried_in_another_directory(
    case, monkeypatch, tmp_path
):
    monkeypatch.setattr(operator, "core", tool)
    proposal, _ = tool.validate_ready(case)
    monkeypatch.setattr(operator, "preflight", lambda value: proposal)
    launches = []
    monkeypatch.setattr(
        operator.process,
        "supervise",
        lambda *a, **k: launches.append(a[0]) or {"returncode": 0, "failure": None},
    )
    operator.one_child(case["codecs"]["case"], "legacy", "codec", tmp_path / "first")
    with pytest.raises(FileExistsError):
        operator.one_child(
            case["codecs"]["case"], "legacy", "codec", tmp_path / "retry"
        )
    assert len(launches) == 1


def test_spent_legacy_codec_requires_fresh_execution_provenance(
    case, monkeypatch, tmp_path
):
    monkeypatch.setattr(operator, "core", tool)
    monkeypatch.setattr(
        operator.process,
        "supervise",
        lambda *a, **k: pytest.fail("Unapproved codec retry"),
    )
    previous = {
        "supervision": {"returncode": 1},
        "command": ["python", "-I", "-S", "-B", "worker.py", "codec"],
    }
    for text in (None, case["codecs"]["case"]["authority_json"]):
        with pytest.raises(tool.Error) as err:
            operator.retry_codec(
                case["codecs"]["case"], previous, text, tmp_path / "not_started"
            )
        assert err.value.code == "codec_retry_authority"
    assert not (tmp_path / "not_started").exists()


def test_failed_codec_cannot_be_credited_or_frozen_as_complete(case, monkeypatch):
    monkeypatch.setattr(operator, "core", tool)
    monkeypatch.setattr(
        operator, "attribution", lambda *a: pytest.fail("Failed codec credited")
    )
    case["codecs"]["captures"]["legacy"]["supervision"]["returncode"] = 1
    case["codecs"]["captures"]["legacy"]["supervision"]["failure"] = "worker_failure"
    with pytest.raises(tool.Error):
        operator.receive_codecs(case["codecs"]["case"], case["codecs"]["captures"])
    with pytest.raises(tool.Error):
        operator.freeze(case["codecs"])


def test_fresh_worker_guards_block_parameters_network_dispatch_and_neural_method_doubles(
    tmp_path,
):
    # A fresh stdlib process makes the nonremovable audit hook harmless to pytest.
    path = ROOT / "devtools/hydramp_historical_native_worker.py"
    script = """
import importlib.util,sys,subprocess,pickle
from pathlib import Path
spec=importlib.util.spec_from_file_location('worker',sys.argv[1])
worker=importlib.util.module_from_spec(spec);spec.loader.exec_module(worker)
root=Path(sys.argv[2]); parameter=root/'fake.npy';parameter.write_bytes(b'control-not-a-model')
opened,calls,state=worker.guards('codec',{'assets':[],'model_root':str(root/'nonexistent-real-model')})
hook=sys.getprofile()
namespace={'__name__':'hydramp_torch.inference'}
exec('def score_tokens(): return 0',namespace)
checks=[lambda:parameter.read_bytes(),lambda:subprocess.Popen([sys.executable,'-c','pass']),
        lambda:sys.audit('socket.connect',None,('127.0.0.1',9)),lambda:pickle.loads(b'control'),namespace['score_tokens']]
for check in checks:
    # CPython removes a profile callback when it raises. Each control models
    # a fresh fail-stop worker; restore the hook before the next independent challenge.
    sys.setprofile(hook)
    try:check()
    except (RuntimeError,PermissionError):pass
    else:raise AssertionError('Guard allowed prohibited control')
sys.setprofile(None)
assert opened==[] and calls==['score_tokens']
assert not {'torch','tensorflow','keras','amp','hydramp_torch'} & {name.split('.')[0] for name in sys.modules}
print('guard controls PASS; zero scientific calls')
"""
    result = subprocess.run(
        [sys.executable, "-I", "-S", "-B", "-c", script, str(path), str(tmp_path)],
        capture_output=True,
        text=True,
        timeout=15,
    )
    assert result.returncode == 0, result.stderr
    assert "guard controls PASS" in result.stdout


def test_isolated_site_metadata_does_not_enable_user_packages_or_pth(tmp_path):
    path = ROOT / "devtools/hydramp_historical_native_worker.py"
    script = """
import importlib.util,site,sys
from pathlib import Path
spec=importlib.util.spec_from_file_location('worker',sys.argv[1])
worker=importlib.util.module_from_spec(spec);spec.loader.exec_module(worker)
root=Path(sys.argv[2]); version='python'+str(sys.version_info.major)+'.'+str(sys.version_info.minor)
frozen=root/'lib'/version/'site-packages'
frozen.mkdir(parents=True)
marker=root/'unexpected-bootstrap'
(frozen/'unsafe.pth').write_text('import pathlib; pathlib.Path('+repr(str(marker))+').touch()\\n')
assert site.USER_SITE is None
before=list(sys.path)
def denied(*args,**kwargs): raise AssertionError('Site bootstrap must stay disabled')
site.main=site.addsitedir=denied
worker.configure_site_metadata(str(frozen))
assert sys.path==before and not marker.exists()
assert site.ENABLE_USER_SITE is False
assert site.USER_SITE==str(frozen) and site.USER_BASE==str(root)
assert site.PREFIXES==[str(root)] and site.getsitepackages()==[str(frozen)]
assert not {'tensorflow','torch','keras','amp','hydramp_torch'} & {n.split('.')[0] for n in sys.modules}
print('isolated site metadata PASS; no bootstrap or scientific imports')
"""
    result = subprocess.run(
        [sys.executable, "-I", "-S", "-B", "-c", script, str(path), str(tmp_path)],
        capture_output=True,
        text=True,
        timeout=15,
    )
    assert result.returncode == 0, result.stderr
    assert "isolated site metadata PASS" in result.stdout


@pytest.mark.parametrize("kind", ["codec", "score"])
def test_operation_counts_do_not_coerce_booleans(case, kind):
    if kind == "codec":
        alter(
            case["codecs"]["captures"],
            "modern",
            lambda raw: raw["codec_operations"].__setitem__("encode_sequences", True),
        )
        with pytest.raises(tool.Error) as err:
            tool.validate_ready(case)
        assert err.value.code == "codec_calls"
    else:
        captures = controls(case)
        alter(captures, "modern", lambda raw: raw.__setitem__("model_loads", False))
        with pytest.raises(tool.Error) as err:
            tool.receive(case, None, captures, "instrumented_method_double")
        assert err.value.code == "score_kind"


@pytest.mark.parametrize("changed_delegation", [False, True])
def test_standing_authority_is_not_misreported_as_per_run_investigator_review(
    case, monkeypatch, changed_delegation
):
    monkeypatch.setattr(operator, "core", tool)
    text = (
        ROOT / "devguide/evidence/shared_host_execution_delegation.json"
    ).read_text()
    if changed_delegation:
        text += "\n"
    base = {
        "explicit_investigator_approval": False,
        "authorization_basis": "standing_investigator_delegation",
        "run_specific_investigator_review": False,
        "standing_authority_json": text,
        "reply_reference": "Investigator D49 standing delegation; test control only",
    }
    receipt = {
        **base,
        "schema": tool.EXECUTION,
        "stage": "real_scoring",
        "ready_plan_sha256": tool.object_digest(case),
        "neural_evaluations": 12,
    }
    previous = {
        "supervision": {"returncode": 1},
        "command": ["python", "-I", "-S", "-B", "worker.py", "codec"],
    }
    retry = {
        **base,
        "schema": "peptidemt.hydramp_historical_codec_retry_authorization@1",
        "stage": "legacy_codec_retry",
        "case_sha256": tool.object_digest(case["codecs"]["case"]),
        "previous_capture_sha256": tool.object_digest(previous),
        "implementation_pins": operator.pins(),
        "children": 1,
        "neural_evaluations": 0,
    }
    if changed_delegation:
        with pytest.raises(tool.Error):
            tool.execution_authority(case, json.dumps(receipt))
        with pytest.raises(tool.Error):
            operator.validate_retry(case["codecs"]["case"], previous, json.dumps(retry))
    else:
        checked = tool.execution_authority(case, json.dumps(receipt))
        assert checked["explicit_investigator_approval"] is False
        assert checked["run_specific_investigator_review"] is False
        assert operator.validate_retry(
            case["codecs"]["case"], previous, json.dumps(retry)
        )
