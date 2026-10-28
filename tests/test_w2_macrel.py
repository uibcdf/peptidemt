"""Engine-free W2 controls. No Macrel models, formulas or scientific outputs."""

import json
import math
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest
import smonitor

from peptidemt import (
    MacrelLimits,
    ResultSet,
    SequenceRecord,
    assess_macrel,
    prepare_sequences,
)
from peptidemt import _macrel_worker as worker
from peptidemt import macrel as route
from peptidemt._data import decode, encode, freeze
from peptidemt._diagnostics import (
    MacrelFailureWarning,
    RequiredDependencyError,
)
from peptidemt._private.smonitor import CATALOG, CODES


@pytest.fixture
def limits():
    # Only controlled tests use these values; no live host envelope is implied.
    return MacrelLimits(8, 1024, 10, 2 * 1024**3)


def values(sequence="ACD", amp=0.5000000000000001, hemo=0.125):
    return dict(
        Sequence=sequence,
        AMP_probability=amp,
        is_AMP=amp > 0.5,
        Hemolytic_probability=hemo,
        Hemolytic="Hemo" if hemo > 0.5 else "NonHemo",
        AMP_family="ALP",
        extra_native_column="preserved",
    )


def assess(sequences, limits, **kwargs):
    return assess_macrel(
        prepare_sequences(sequences),
        snapshot_id="controlled-W2",
        limits=limits,
        **kwargs,
    )


def test_no_compatible_input_never_starts_provider_or_local_reader(monkeypatch, limits):
    def forbidden(*args, **kwargs):
        pytest.fail("Incompatible/empty pool must not start a child or parse FASTA")

    monkeypatch.setattr(route, "_execute_worker", forbidden)
    monkeypatch.setattr("peptidemt.inputs.parse_fasta", forbidden)
    for sequences in (
        [],
        ["MACD", "", "acD", SequenceRecord("ACD", chemistry={"cap": True})],
    ):
        result = assess(sequences, limits)
        assert not result.rows
        assert not result.failures
        assert result.provenance.details["execution"].startswith("not-requested")


def test_occurrence_submission_negatives_precision_anomalies_and_replay(
    monkeypatch, limits
):
    def controlled(request, directory, bound):
        assert request["records"] == [("input-0", "ACD"), ("input-2", "ACD")]
        assert bound == limits
        assert directory.is_dir()
        return {
            "bundle_id": "controlled:never-a-qualified-bundle",
            "rows": [
                {"token": "input-2", "values": values(amp=0.25)},
                {"token": "input-0", "values": values()},
                {"token": "unknown", "values": values(amp=math.nan)},
            ],
            "details": {"native_predictions": {"dtypes": ["float32", "bool"]}},
        }

    monkeypatch.setattr(route, "_execute_worker", controlled)
    result = assess(["ACD", "MACD", "ACD"], limits)
    assert result.rows[0].values["is_AMP"] is False
    assert result.rows[1].values["AMP_probability"].hex() == (0.5000000000000001).hex()
    assert result.outcomes[0].row_index == 1
    assert result.outcomes[2].row_index == 0
    assert "unqualified_bundle" in result.outcomes[0].issues
    assert result.anomalies == ((2, "unknown_provider_token"),)
    replay = ResultSet.from_json(result.to_json())
    assert replay.rows[1].values == result.rows[1].values
    assert math.isnan(replay.rows[2].values["AMP_probability"])
    assert replay.provenance.details["native_predictions"]["dtypes"] == (
        "float32",
        "bool",
    )


@pytest.mark.parametrize(
    "kind",
    [
        "timeout",
        "provider_load_failure",
        "asset_load_failure",
        "feature_failure",
        "prediction_failure",
        "unavailable_dependency",
        "native_output_failure",
        "worker_failure",
    ],
)
def test_failures_are_explicit_and_never_retried(monkeypatch, limits, kind):
    calls = []

    def controlled(*args):
        calls.append(args)
        if kind == "timeout":
            raise subprocess.TimeoutExpired("controlled", 10)
        return {"failure": kind, "cause_type": "ControlledFailure"}

    monkeypatch.setattr(route, "_execute_worker", controlled)
    with pytest.warns(MacrelFailureWarning, match=kind):
        result = assess(["ACD", "MACD", "ACD"], limits)
    assert len(calls) == 1
    assert result.failures == {"input-0": kind, "input-2": kind}
    assert not result.rows
    assert not any(outcome.eligible for outcome in result.outcomes)
    assert result.provenance.details["retries"] == 0


def test_limits_are_checked_before_child_and_include_occurrence_token_bytes(
    monkeypatch,
):
    monkeypatch.setattr(
        route, "_execute_worker", lambda *args: pytest.fail("Child started")
    )
    for limits in (MacrelLimits(1, 100, 1, 1000), MacrelLimits(8, 5, 1, 1000)):
        with pytest.warns(MacrelFailureWarning, match="input_limit"):
            result = assess(["ACD", "ACD"], limits)
        assert set(result.failures.values()) == {"input_limit"}


@pytest.mark.parametrize(
    "changes",
    [
        {"max_records": True},
        {"max_records": 0},
        {"memory_bytes": -1},
        {"max_input_bytes": 1.5},
        {"wall_seconds": math.inf},
        {"wall_seconds": math.nan},
        {"wall_seconds": False},
    ],
)
def test_invalid_limits(changes):
    fields = dict(max_records=1, max_input_bytes=100, wall_seconds=1, memory_bytes=1000)
    with pytest.raises(ValueError):
        MacrelLimits(**(fields | changes))


def test_selected_absence_uses_depdigest_with_truthful_hint(monkeypatch):
    from depdigest.core import checker

    checker.is_installed.cache_clear()
    monkeypatch.setattr(checker, "find_spec", lambda name: None)
    try:
        with pytest.raises(RequiredDependencyError) as caught:
            worker._load_macrel()
        assert "pip install macrel==1.6.1" in str(caught.value)
        assert "conda install" not in str(caught.value)
    finally:
        checker.is_installed.cache_clear()


def test_transitive_import_failure_is_not_absence(monkeypatch):
    from depdigest.core import checker

    checker.is_installed.cache_clear()
    monkeypatch.setattr(checker, "find_spec", lambda name: SimpleNamespace())
    monkeypatch.setitem(sys.modules, "macrel", None)
    try:
        with pytest.raises(ModuleNotFoundError):
            worker._load_macrel()
    finally:
        checker.is_installed.cache_clear()


def test_unqualified_molsysmt_installers_are_not_invented(monkeypatch):
    from depdigest.core import checker

    checker.is_installed.cache_clear()
    monkeypatch.setattr(checker, "find_spec", lambda name: None)
    try:
        with pytest.raises(RequiredDependencyError) as caught:
            worker._load_molsysmt()
        message = str(caught.value)
        assert "conda install" not in message and "pip install" not in message
        assert "peptidemt/blob/main/devguide/w2_macrel.md" in message
    finally:
        checker.is_installed.cache_clear()


def test_transport_delegates_each_occurrence_to_molsysmt(monkeypatch, tmp_path):
    calls = []

    def convert(item, *, to_form):
        calls.append((item, to_form))
        if to_form == "biopython.SeqRecord":
            assert item == "ACD"
            return SimpleNamespace(seq="ACD")
        assert item.id in ("input-0", "input-2")
        assert item.name == item.id and item.description == ""
        # Opaque stand-in for bytes produced by the owner, not a FASTA writer.
        Path(to_form).write_bytes(("owner-record:" + item.id + "\n").encode())

    result = worker._write_transport(
        SimpleNamespace(convert=convert),
        [("input-0", "ACD"), ("input-2", "ACD")],
        tmp_path,
    )
    assert result.read_bytes() == b"owner-record:input-0\nowner-record:input-2\n"
    assert len(calls) == 4
    assert not (tmp_path / "occurrence.fasta").exists()


def test_transport_rejects_changed_owner_view(tmp_path):
    msm = SimpleNamespace(convert=lambda *args, **kwargs: SimpleNamespace(seq="A"))
    with pytest.raises(ValueError, match="changed"):
        worker._write_transport(msm, [("input-0", "ACD")], tmp_path)


class Frame:
    """Small controlled provider table implementing only the consumed protocol."""

    def __init__(self, tokens, columns, rows, dtypes):
        self.index, self.columns, self.rows, self.dtypes = tokens, columns, rows, dtypes
        self.iloc = self

    def __len__(self):
        return len(self.rows)

    def __getitem__(self, key):
        row, column = key
        return self.rows[row][column]


def test_native_orchestration_uses_owner_features_both_assets_and_keep_negatives(
    monkeypatch, tmp_path
):
    root = tmp_path / "macrel"
    root.mkdir()
    (root / "data/models").mkdir(parents=True)
    for name in (
        "AMP_features.py",
        "AMP_predict.py",
        "macrel_features.py",
        "fasta.py",
        "__init__.py",
        "data/models/AMP.onnx.gz",
        "data/models/Hemo.onnx.gz",
    ):
        (root / name).write_bytes(b"controlled-non-executable-artifact")
    macrel = SimpleNamespace(__file__=str(root / "__init__.py"))
    native = values(amp=0.125)
    features = Frame(
        ["input-0"],
        ["sequence", "group", "charge"],
        [["ACD", "Unk", -1.0]],
        ["str", "str", "float64"],
    )
    prediction = Frame(
        ["input-0"], list(native), [list(native.values())], ["object"] * len(native)
    )
    calls = []

    def extract(path):
        assert Path(path).read_bytes() == b"owner-serialized"
        calls.append("features")
        return features

    def predict(amp, hemo, frame, *, keep_negatives):
        assert Path(amp).name == "AMP.onnx.gz"
        assert Path(hemo).name == "Hemo.onnx.gz"
        assert frame is features and keep_negatives is True
        calls.append("both-native-heads-requested")
        return prediction

    monkeypatch.setattr(worker, "_load_macrel", lambda: (macrel, extract, predict))
    monkeypatch.setattr(worker, "_identity", lambda *args: {"version": "1.6.1"})
    monkeypatch.setattr(worker, "files", lambda name: root)
    monkeypatch.setattr(
        worker.importlib.metadata,
        "distribution",
        lambda name: SimpleNamespace(locate_file=lambda name: tmp_path / name),
    )
    monkeypatch.setattr(
        worker.importlib.metadata, "version", lambda name: "controlled-version"
    )
    monkeypatch.setattr(worker, "_load_molsysmt", lambda: object())

    def transport(msm, records, directory):
        path = directory / "submitted.fasta"
        path.write_bytes(b"owner-serialized")
        return path

    monkeypatch.setattr(worker, "_write_transport", transport)
    response = worker._run_native(
        [("input-0", "ACD")], tmp_path, {"stage": "initial", "details": {}}
    )
    assert calls == ["features", "both-native-heads-requested"]
    assert response["rows"] == [{"token": "input-0", "values": native}]
    assert response["details"]["native_features"]["dtypes"][-1] == "float64"
    assert len(response["details"]["assets"]) == 2
    assert response["bundle_id"].startswith("macrel-1.6.1:")


def test_frame_keeps_dtype_and_exact_scalar_values():
    original = 0.5000000000000001
    scalar = SimpleNamespace(item=lambda: original)
    frame = Frame(["input-0"], ["AMP_probability"], [[scalar]], ["float64"])
    detached = decode(json.loads(json.dumps(encode(freeze(worker._frame(frame))))))
    assert detached["values"][0][0].hex() == original.hex()
    assert detached["dtypes"] == ("float64",)
    with pytest.raises(ValueError, match="unique"):
        worker._frame(Frame([], ["x", "x"], [], []))


def test_child_command_is_isolated_bounded_and_has_no_retry(
    monkeypatch, tmp_path, limits
):
    calls = []

    def run(command, **kwargs):
        calls.append((command, kwargs))
        assert command[:4] == [sys.executable, "-I", "-m", "peptidemt._macrel_cli"]
        assert kwargs["timeout"] == limits.wall_seconds
        assert kwargs["cwd"] == tmp_path
        request = decode(json.loads(Path(command[-2]).read_text()))
        assert request["memory_bytes"] == limits.memory_bytes
        Path(command[-1]).write_text(json.dumps(encode({"rows": []})))
        return SimpleNamespace(returncode=0)

    monkeypatch.setattr(route.subprocess, "run", run)
    assert (
        route._execute_worker(
            {"records": [], "memory_bytes": limits.memory_bytes}, tmp_path, limits
        )["rows"]
        == ()
    )
    assert len(calls) == 1


def test_worker_protocol_retains_exact_values_and_applies_memory_limit(
    monkeypatch, tmp_path
):
    import resource

    request_path, response_path = tmp_path / "request.json", tmp_path / "response.json"
    request_path.write_text(
        json.dumps(
            encode(freeze({"records": [("input-0", "ACD")], "memory_bytes": 123456}))
        )
    )
    monkeypatch.setattr(sys, "argv", ["worker", str(request_path), str(response_path)])
    calls = []
    monkeypatch.setattr(
        resource, "setrlimit", lambda kind, bounds: calls.append((kind, bounds))
    )

    def controlled(records, directory, state):
        assert calls == [(resource.RLIMIT_AS, (123456, 123456))]
        assert records == (("input-0", "ACD"),)
        return {
            "rows": [{"token": "input-0", "values": values()}],
            "details": {"count": 1},
        }

    monkeypatch.setattr(worker, "_run_native", controlled)
    worker.main()
    response = decode(json.loads(response_path.read_text()))
    assert (
        response["rows"][0]["values"]["AMP_probability"].hex()
        == (0.5000000000000001).hex()
    )


def test_worker_preserves_transitive_failure_stage_and_cause(monkeypatch, tmp_path):
    import resource

    request_path, response_path = tmp_path / "request.json", tmp_path / "response.json"
    request_path.write_text(
        json.dumps(encode(freeze({"records": [], "memory_bytes": 123456})))
    )
    monkeypatch.setattr(sys, "argv", ["worker", str(request_path), str(response_path)])
    monkeypatch.setattr(resource, "setrlimit", lambda *args: None)

    def broken(records, directory, state):
        state["stage"] = "provider_load_failure"
        raise ModuleNotFoundError("controlled transitive dependency")

    monkeypatch.setattr(worker, "_run_native", broken)
    worker.main()
    response = decode(json.loads(response_path.read_text()))
    assert response["failure"] == "provider_load_failure"
    assert response["cause_type"] == "ModuleNotFoundError"
    assert "transitive" in response["cause_message"]


def test_catalog_templates_render_and_types_reconstruct():
    from smonitor.config import validate_project_config
    from smonitor.config.discovery import load_config_from_path

    from peptidemt._diagnostics import PACKAGE_ROOT

    assert not validate_project_config(
        load_config_from_path(PACKAGE_ROOT / "_smonitor.py")
    )
    for entry in CATALOG.values():
        assert entry["code"] in CODES
        for profile in ("user", "dev", "qa", "agent"):
            message, _ = smonitor.resolve(
                code=entry["code"],
                profile=profile,
                extra={
                    "library": "macrel",
                    "stage": "timeout",
                    "cause_type": "TimeoutExpired",
                },
            )
            assert message
    for diagnostic in (
        RequiredDependencyError(library="macrel"),
        MacrelFailureWarning(stage="timeout", cause_type="TimeoutExpired"),
    ):
        assert type(diagnostic)(*diagnostic.args).args == diagnostic.args


def test_core_import_does_not_initialize_route_or_scientific_providers():
    program = """
import sys
import peptidemt
assert not any(n in sys.modules for n in ('macrel', 'molsysmt', 'Bio', 'peptidemt.macrel'))
"""
    subprocess.run([sys.executable, "-I", "-c", program], check=True)


def test_separate_process_guard_retains_consumer_configuration(tmp_path):
    request_path, response_path = tmp_path / "request.json", tmp_path / "response.json"
    request_path.write_text(
        json.dumps(
            encode(
                freeze({"records": [("input-0", "ACD")], "memory_bytes": 2 * 1024**3})
            )
        )
    )
    # Force genuine guarded absence inside this child even on a provider-equipped
    # developer host. No Macrel import/model can be reached by this control.
    program = """
from peptidemt._macrel_cli import main
from depdigest.core import checker
checker.is_installed.cache_clear()
checker.find_spec = lambda name: None
main()
"""
    subprocess.run(
        [sys.executable, "-I", "-c", program, str(request_path), str(response_path)],
        cwd=tmp_path,
        timeout=10,
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    response = decode(json.loads(response_path.read_text()))
    assert response["failure"] == "unavailable_dependency"
    assert "pip install macrel==1.6.1" in response["cause_message"]
    assert "conda install" not in response["cause_message"]


def test_diagnostic_bundle_export_has_the_emitted_consumer_identity(tmp_path):
    from peptidemt._diagnostics import bundle

    smonitor.configure(
        profile="agent", level="DEBUG", handlers=[], event_buffer_size=20, enabled=True
    )
    with pytest.warns(MacrelFailureWarning):
        bundle.warn(
            MacrelFailureWarning(
                stage="controlled-export", cause_type="ControlledFailure"
            )
        )
    path = smonitor.export_bundle(tmp_path / "diagnostics.json")
    exported = json.loads(path.read_text())
    assert "triage" in exported
    assert exported["triage"]["events_by_code"]["PEP-WARN-RUN-001"] >= 1
