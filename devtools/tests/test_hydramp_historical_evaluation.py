"""D47 endpoint/paired ranking logic; all scores are explicitly artificial."""

import builtins
import copy
import hashlib
import importlib.util
import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "historical_evaluation_test", ROOT / "devtools/hydramp_historical_evaluation.py"
)
tool = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(tool)


@pytest.fixture
def case(monkeypatch):
    # Minimal fake source-adapter result; real digest receiving is separately
    # qualified by the existing D46 tests and actual-data guarded integration.
    snapshot = {
        "synthetic_source_only": True,
        "source_annotations": {"amide": True, "unknown": None},
    }
    rows = []
    for group, number, raw, comparator in (
        ("a", 1, "4", "="),
        ("b", 2, ">512", ">"),
        ("c", 3, "16", "="),
        ("c", 4, "128", "="),
    ):
        rows.append(
            {
                "sequence_sha256": group * 64,
                "source_occurrence_id": f"synthetic-row-{number}",
                "source_name": f"synthetic-{group}",
                "proposed_assay_scope": {
                    "strain": "ATCC 25922",
                    "endpoint": "MIC",
                    "unit_as_reported": "µg/mL",
                    "raw_value": raw,
                    "reported_numeric_text": raw.lstrip(">"),
                    "comparator": comparator,
                },
            }
        )

    def inspection(value):
        assert value == snapshot
        return {"observations": copy.deepcopy(rows)}

    monkeypatch.setattr(tool.historical, "inspect", inspection)
    approval = json.dumps(
        {
            "decision": "D47",
            "schema": "peptidemt.hydramp_historical_endpoint_authorization@1",
        }
    )
    monkeypatch.setattr(
        tool, "_APPROVAL_SHA", hashlib.sha256(approval.encode()).hexdigest()
    )
    endpoint = tool._derive(copy.deepcopy(snapshot), approval)
    return endpoint, approval, snapshot


def controls(endpoint, original=(0.9, 0.1, 0.7), modern=(0.1, 0.9, 0.3)):
    return {
        "schema": tool._SCORES,
        "kind": "synthetic_control",
        "endpoint_sha256": tool._digest(endpoint),
        "scores": [
            {"group_id": g["group_id"], "original": a, "modern": b}
            for g, a, b in zip(endpoint["groups"], original, modern, strict=True)
        ],
    }


def test_endpoint_keeps_all_observations_and_labels_only_a_separate_record(
    case, monkeypatch
):
    endpoint, _, source = case
    before = copy.deepcopy(source)
    monkeypatch.setattr(
        tool, "_provider", lambda: pytest.fail("Metric loaded for data-only endpoint")
    )
    checked = tool.validate_endpoint(endpoint)
    assert checked["counts"] == {
        "source_observations": 4,
        "raw_string_groups": 3,
        "primary_groups": 2,
        "primary_positive": 1,
        "primary_negative": 1,
        "excluded_groups": 1,
    }
    assert source == before == endpoint["source_snapshot"]
    assert [g["primary_label"] for g in checked["groups"]] == [1, 0, None]
    assert checked["groups"][1]["source_observations"][0]["raw_value"] == ">512"
    assert checked["groups"][2]["exclusion_reason"] == "conflicting_reported_classes"
    assert [r["raw_value"] for r in checked["groups"][2]["source_observations"]] == [
        "16",
        "128",
    ]


@pytest.mark.parametrize(
    "value,relation,expected",
    [
        ("31", "=", 1),
        ("32", "=", 1),
        ("33", "=", 0),
        ("512", ">", 0),
        ("32", ">", 0),
        ("31", ">", None),
    ],
)
def test_strict_right_censoring_does_not_become_a_point(value, relation, expected):
    assert tool._reported_class(value, relation) == expected


def test_changed_authority_or_cutoff_does_not_get_approved(case):
    endpoint, approval, source = case
    with pytest.raises(tool.Error) as error:
        tool._derive(source, approval + "\n")
    assert error.value.code == "endpoint_authority"
    endpoint["policy"]["criterion"] = "<=128 µg/mL"
    with pytest.raises(tool.Error) as error:
        tool.validate_endpoint(endpoint)
    assert error.value.code == "endpoint_changed"


def test_cache_or_group_exclusions_cannot_be_relabelled(case):
    endpoint, _, _ = case
    endpoint["groups"][2]["primary_label"] = 1
    endpoint["groups"][2]["primary_eligible"] = True
    with pytest.raises(tool.Error) as error:
        tool.validate_endpoint(endpoint)
    assert error.value.code == "endpoint_changed"


def test_public_provider_perfect_and_reversed_controls(case):
    endpoint, _, _ = case
    result = tool.evaluate_synthetic(endpoint, controls(endpoint))["result"]
    assert result["status"] == "synthetic_control_only_not_a_HydrAMP_comparison"
    assert result["provider"]["callable"] == "sklearn.metrics.roc_auc_score"
    assert result["provider"]["distributions"] == tool._VERSIONS
    assert result["provider"]["native_thread_limit"] == 1
    for metric in result["metrics"]:
        assert metric["original_slot_auc"] == 1.0
        assert metric["modern_slot_auc"] == 0.0
        assert metric["paired_difference"] == -1.0
    assert len(result["metrics"][0]["changed_pair_relations"]) == 1
    assert result["source_observations_retained"] == 4
    assert result["biological_efficacy_or_equivalence_claim"] is False


def test_ties_get_half_credit_without_an_epsilon(case):
    endpoint, _, _ = case
    scores = controls(endpoint, (0.5, 0.5, 0.5), (math.nextafter(0.5, 1.0), 0.5, 0.5))
    metric = tool.evaluate_synthetic(endpoint, scores)["result"]["metrics"][0]
    assert metric["original_slot_auc"] == 0.5
    assert metric["modern_slot_auc"] == 1.0
    assert metric["changed_pair_relations"][0]["original_relation"] == 0
    assert metric["changed_pair_relations"][0]["modern_relation"] == 1
    assert scores["scores"][0]["modern"].hex() == math.nextafter(0.5, 1.0).hex()


def test_ambiguity_uses_same_scenario_in_both_columns_not_independent_bounds(case):
    endpoint, _, _ = case
    vectors = (0.8, 0.2, 0.95)
    result = tool.evaluate_synthetic(endpoint, controls(endpoint, vectors, vectors))[
        "result"
    ]
    assert [m["original_slot_auc"] for m in result["metrics"]] == [1.0, 0.5, 1.0]
    assert [m["modern_slot_auc"] for m in result["metrics"]] == [1.0, 0.5, 1.0]
    assert result["paired_ambiguity_sensitivity_range"]["minimum"] == 0.0
    assert result["paired_ambiguity_sensitivity_range"]["maximum"] == 0.0


def test_ambiguity_can_change_the_paired_difference_without_changing_primary(case):
    endpoint, _, _ = case
    result = tool.evaluate_synthetic(
        endpoint, controls(endpoint, (0.8, 0.2, 0.5), (0.8, 0.2, 0.95))
    )["result"]
    assert [m["paired_difference"] for m in result["metrics"]] == [0.0, -0.5, 0.0]
    assert result["paired_ambiguity_sensitivity_range"]["minimum"] == -0.5
    assert result["paired_ambiguity_sensitivity_range"]["maximum"] == 0.0


@pytest.mark.parametrize(
    "mutation,code",
    [
        ("kind", "score_kind"),
        ("provenance", "score_fields"),
        ("binding", "score_binding"),
        ("missing", "score_pairing"),
        ("duplicate", "score_pairing"),
        ("reorder", "score_pairing"),
        ("foreign", "score_pairing"),
        ("missing_slot", "score_rows"),
        ("nan", "score_value"),
        ("inf", "score_value"),
        ("bool", "score_value"),
        ("string", "score_value"),
        ("negative", "score_value"),
        ("over_one", "score_value"),
    ],
)
def test_bad_scores_rejected_before_metric_loading(case, monkeypatch, mutation, code):
    endpoint, _, _ = case
    scores = controls(endpoint)
    if mutation == "kind":
        scores["kind"] = "learned_model_result"
    elif mutation == "provenance":
        scores["model_checkpoint"] = "pretend-real"
    elif mutation == "binding":
        scores["endpoint_sha256"] = "0" * 64
    elif mutation == "missing":
        scores["scores"].pop()
    elif mutation == "duplicate":
        scores["scores"][1]["group_id"] = scores["scores"][0]["group_id"]
    elif mutation == "reorder":
        scores["scores"].reverse()
    elif mutation == "foreign":
        scores["scores"][0]["group_id"] = "foreign"
    elif mutation == "missing_slot":
        del scores["scores"][0]["modern"]
    else:
        scores["scores"][0]["modern"] = {
            "nan": float("nan"),
            "inf": float("inf"),
            "bool": True,
            "string": "0.5",
            "negative": -0.1,
            "over_one": 1.1,
        }[mutation]
    monkeypatch.setattr(
        tool, "_provider", lambda: pytest.fail("Invalid data reached statistics")
    )
    with pytest.raises(tool.Error) as error:
        tool.evaluate_synthetic(endpoint, scores)
    assert error.value.code == code


def test_statistical_profile_or_source_change_requires_qualification(monkeypatch):
    monkeypatch.setattr(tool, "version", lambda name: "changed")
    with pytest.raises(tool.Error) as error:
        tool._provider()
    assert error.value.code == "statistics_profile"


def test_statistical_source_fingerprint_is_checked(monkeypatch):
    monkeypatch.setattr(tool, "_METRIC_SOURCE_SHA", "0" * 64)
    with pytest.raises(tool.Error) as error:
        tool._provider()
    assert error.value.code == "statistics_source"


def test_provider_import_failure_is_explicit_without_fallback(monkeypatch):
    original = builtins.__import__

    def unavailable(name, *args, **kwargs):
        if name == "sklearn.metrics":
            raise ImportError("controlled provider failure")
        return original(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", unavailable)
    with pytest.raises(tool.Error) as error:
        tool._provider()
    assert error.value.code == "statistics_unavailable"


def test_self_contained_result_replay_and_cache_tamper_detection(case, tmp_path):
    endpoint, _, _ = case
    record = tool.evaluate_synthetic(endpoint, controls(endpoint))
    path = tmp_path / "synthetic.json"
    tool.save(record, path)
    assert tool.inspect(tool.load(path)) == record["result"]
    record["result"]["metrics"][0]["modern_slot_auc"] = 1.0
    with pytest.raises(tool.Error) as error:
        tool.inspect(record)
    assert error.value.code == "comparison_changed"


def test_cli_data_and_synthetic_routes_never_offer_execution(
    case, tmp_path, monkeypatch, capsys
):
    endpoint, approval, snapshot = case
    source_path = tmp_path / "source.json"
    source_path.write_text(json.dumps(snapshot))
    approval_path = tmp_path / "approval.json"
    approval_path.write_text(approval)
    monkeypatch.setattr(
        tool.historical, "load", lambda path: json.loads(Path(path).read_text())
    )
    endpoint_path = tmp_path / "endpoint.json"
    assert (
        tool.main(
            [
                "prepare",
                "--source-snapshot",
                str(source_path),
                "--approval",
                str(approval_path),
                "--output",
                str(endpoint_path),
            ]
        )
        == 0
    )
    assert json.loads(capsys.readouterr().out)["counts"]["primary_groups"] == 2
    source_path.unlink()
    approval_path.unlink()
    assert tool.main(["inspect", str(endpoint_path)]) == 0
    capsys.readouterr()
    scores_path = tmp_path / "scores.json"
    scores_path.write_text(json.dumps(controls(endpoint)))
    output = tmp_path / "comparison.json"
    assert (
        tool.main(
            [
                "evaluate-synthetic",
                "--endpoint",
                str(endpoint_path),
                "--scores",
                str(scores_path),
                "--output",
                str(output),
            ]
        )
        == 0
    )
    assert json.loads(capsys.readouterr().out)["model_payloads_or_calls"] == 0
    assert tool.main(["inspect", str(output)]) == 0
    capsys.readouterr()
    assert (
        tool.main(
            [
                "evaluate-synthetic",
                "--endpoint",
                str(endpoint_path),
                "--scores",
                str(scores_path),
                "--output",
                str(output),
            ]
        )
        == 2
    )
    assert json.loads(capsys.readouterr().err)["code"] == "invalid_data"  # no overwrite
    with pytest.raises(SystemExit) as error:
        tool.main(["execute"])
    assert error.value.code == 2
