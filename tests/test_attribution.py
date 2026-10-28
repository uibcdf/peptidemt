"""Real portable-provider receiving with controlled completion evidence only.

The native tables below are stand-ins. No Macrel package or model is executed.
Ackredit is an explicit test dependency; absence must fail this receiving lane.
"""

import json
import subprocess
import sys
import warnings
from importlib.metadata import distribution
from pathlib import Path
from types import SimpleNamespace

import ackredit
import pytest

from peptidemt import ResultSet, assess_macrel, prepare_sequences
from peptidemt import _attribution as boundary
from peptidemt import macrel as route
from peptidemt._diagnostics import AttributionWarning


@pytest.fixture
def completed():
    return {
        "transport_sha256": "controlled-not-a-real-file-digest",
        "molsysmt": {"version": "controlled-MolSysMT-version"},
        "macrel": {"version": "1.6.1"},
        "native_features": {"values": []},
        "native_predictions": {"values": []},
    }


def test_real_provider_reuses_references_in_two_results_and_enclosing_workflow(
    completed,
):
    with ackredit.session("controlled-attribution-workflow"):
        with ackredit.capture("enclosing-application") as enclosing:
            first = boundary.completed_attribution(completed, "controlled-first")
            second = boundary.completed_attribution(completed, "controlled-second")
        workflow = ackredit.get_attribution().to_dict()
    assert first["status"] == second["status"] == "captured"
    first_items = {item["id"] for item in first["ackredit"]["items"]}
    assert first_items == {item["id"] for item in second["ackredit"]["items"]}
    assert len(first_items) == 5
    assert first_items == {
        item["id"] for item in enclosing.attribution.to_dict()["items"]
    }
    assert len(workflow["uses"]) == 10
    assert {use["context"]["snapshot_id"] for use in workflow["uses"]} == {
        "controlled-first",
        "controlled-second",
    }
    assert first["ackredit"]["context"]["snapshot_id"] == "controlled-first"


def test_detached_payload_and_fresh_reader_preserve_original_producer_versions(
    completed, tmp_path
):
    with ackredit.session("controlled-producer"):
        original = boundary.completed_attribution(completed, "saved-controlled")
        portable = original["ackredit"]
        assert "10.7717/peerj.10555" in ackredit.Attribution.from_dict(portable).report(
            format="bibtex"
        )
    saved = tmp_path / "attribution.json"
    saved.write_text(json.dumps(original))
    program = """
import json,sys,ackredit
with ackredit.session('fresh-reader'):
    original=json.load(open(sys.argv[1]))
    restored=ackredit.Attribution.from_dict(original['ackredit']).to_dict()
    assert restored==original['ackredit']
    assert any(i.get('version')=='controlled-MolSysMT-version' for i in restored['items'])
    assert not ackredit.get_attribution().to_dict()['uses']
    assert 'macrel' not in sys.modules and 'molsysmt' not in sys.modules
"""
    subprocess.run(
        [sys.executable, "-I", "-c", program, str(saved)], cwd=tmp_path, check=True
    )
    portable["items"].clear()
    assert len(original["bibliography"]) == 5


def test_evaluated_empty_completion_keeps_credit_but_no_execution_loads_nothing(
    completed, monkeypatch
):
    with ackredit.session("controlled-empty"):
        result = boundary.completed_attribution(completed, "controlled-evaluated-empty")
    assert result["status"] == "captured" and result["ackredit"]["uses"]
    monkeypatch.setattr(
        boundary,
        "is_installed",
        lambda name: pytest.fail("Availability probed without execution"),
    )
    result = boundary.completed_attribution({}, "unexecuted")
    assert result["status"] == "not-executed"
    assert result["bibliography"] == [] and result["ackredit"] is None


def test_genuine_optional_absence_keeps_offline_bibliography(completed, monkeypatch):
    monkeypatch.setattr(boundary, "is_installed", lambda name: False)
    monkeypatch.setattr(
        boundary, "_load_backend", lambda: pytest.fail("Absent provider loaded")
    )
    result = boundary.completed_attribution(completed, "controlled-absence")
    assert result["status"] == "provider-unavailable"
    assert len(result["bibliography"]) == 5 and result["ackredit"] is None


@pytest.mark.parametrize("stage", ["import", "capture", "track"])
def test_provider_failures_preserve_bibliography_and_do_not_claim_success(
    completed, monkeypatch, stage
):
    def broken(*args, **kwargs):
        raise RuntimeError("Controlled optional-provider failure")

    monkeypatch.setattr(boundary, "is_installed", lambda name: True)
    provider = SimpleNamespace(
        capture=ackredit.capture,
        scope=ackredit.scope,
        register_item=ackredit.register_item,
        track_item=ackredit.track_item,
    )
    if stage == "import":
        monkeypatch.setattr(boundary, "_load_backend", broken)
    else:
        setattr(provider, stage if stage == "capture" else "track_item", broken)
        monkeypatch.setattr(boundary, "_load_backend", lambda: provider)
    with pytest.warns(AttributionWarning):
        result = boundary.completed_attribution(
            completed, "controlled-provider-failure"
        )
    assert (
        result["status"] == "provider-failed"
        and result["failure_type"] == "RuntimeError"
    )
    assert len(result["bibliography"]) == 5 and result["ackredit"] is None


def test_warning_promotion_cannot_replace_completed_scores_or_saved_results(
    completed, monkeypatch
):
    def broken():
        raise RuntimeError("controlled provider failure")

    monkeypatch.setattr(boundary, "is_installed", lambda name: True)
    monkeypatch.setattr(boundary, "_load_backend", broken)
    native_values = {
        "Sequence": "ACD",
        "AMP_probability": 0.5000000000000001,
        "is_AMP": True,
        "Hemolytic_probability": 0.125,
        "Hemolytic": "NonHemo",
        "AMP_family": "ALP",
    }
    monkeypatch.setattr(
        route,
        "_execute_worker",
        lambda *args: {
            "rows": [{"token": "input-0", "values": native_values}],
            "details": completed,
        },
    )
    with warnings.catch_warnings():
        warnings.simplefilter("error", AttributionWarning)
        result = assess_macrel(
            prepare_sequences(["ACD"]),
            snapshot_id="controlled-warning-promotion",
            limits=route.MacrelLimits(1, 64, 10, 2 * 1024**3),
        )
    assert (
        result.rows[0].values["AMP_probability"].hex()
        == native_values["AMP_probability"].hex()
    )
    saved = ResultSet.from_json(result.to_json())
    assert (
        saved.provenance.details["scientific_attribution"]["status"]
        == "provider-failed"
    )
    assert len(saved.provenance.details["scientific_attribution"]["bibliography"]) == 5


def test_partial_native_completion_credits_only_the_completed_children(completed):
    del completed["native_predictions"]
    with ackredit.session("controlled-feature-only"):
        result = boundary.completed_attribution(completed, "controlled-partial")
    assert result["completed_operations"] == [
        "molecular_serialization",
        "native_features",
    ]
    assert all(
        "native_predictions" not in use["context"]["completed_operations"]
        for use in result["ackredit"]["uses"]
    )
    reference = next(
        record
        for record in result["bibliography"]
        if "reference_implementation" in record["roles"]
    )
    assert reference["context"]["executed_dependency"] is False
    assert (
        type(AttributionWarning(cause_type="ControlledFailure"))(
            *AttributionWarning(cause_type="ControlledFailure").args
        ).args
        == AttributionWarning(cause_type="ControlledFailure").args
    )


def test_fresh_host_import_and_unexecuted_assessment_do_not_import_ackredit(tmp_path):
    program = """
import sys
import peptidemt
assert 'ackredit' not in sys.modules
from peptidemt import assess_macrel,MacrelLimits,prepare_sequences
result=assess_macrel(prepare_sequences([]),snapshot_id='empty',limits=MacrelLimits(1,64,1,1024**3))
assert 'ackredit' not in sys.modules
assert result.provenance.details['scientific_attribution']['status']=='not-executed'
"""
    subprocess.run([sys.executable, "-I", "-c", program], cwd=tmp_path, check=True)


def test_fresh_process_with_no_ackredit_available_retains_offline_results(tmp_path):
    import depdigest
    import smonitor

    import peptidemt

    # An isolated stdlib process sees only the consumer and its two dependency-
    # free support providers. No site-packages or editable finder exposes Ackredit.
    overlay = tmp_path / "available-packages"
    overlay.mkdir()
    for module in (peptidemt, depdigest, smonitor):
        (overlay / module.__name__).symlink_to(
            Path(module.__file__).parent, target_is_directory=True
        )
    metadata = overlay / "peptidemt.dist-info"
    metadata.mkdir()
    installed = distribution("peptidemt")
    (metadata / "METADATA").write_text(
        installed.read_text("METADATA") or installed.read_text("PKG-INFO")
    )
    program = """
import sys,importlib.util
sys.path.insert(0,sys.argv[1])
assert importlib.util.find_spec('ackredit') is None
from peptidemt._attribution import completed_attribution
result=completed_attribution({'macrel':{'version':'1.6.1'},'native_features':{}},'controlled-no-provider')
assert result['status']=='provider-unavailable' and result['ackredit'] is None
assert result['bibliography']
assert 'ackredit' not in sys.modules
"""
    subprocess.run(
        [sys.executable, "-I", "-S", "-c", program, str(overlay)],
        cwd=tmp_path,
        check=True,
    )
