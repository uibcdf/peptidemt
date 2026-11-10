"""Controlled route/worker seams; no real scientific provider is loaded."""

import inspect
import sys
from dataclasses import dataclass, fields, replace
from pathlib import Path
from types import SimpleNamespace

import pytest
from analogue_fixtures import artificial_receipt

import peptidemt
from peptidemt import (
    HydrAMPAnalogueBundle,
    HydrAMPAnalogueReceipt,
    HydrAMPLimits,
    SequenceRecord,
)
from peptidemt import _analogue_worker as worker
from peptidemt import _attribution as attribution
from peptidemt import _hydramp_worker as identity
from peptidemt import analogue as route
from peptidemt._diagnostics import HydrAMPAttributionWarning, HydrAMPFailureWarning
from peptidemt._hydramp_process import sha256, source_manifest


@pytest.fixture
def bundle(tmp_path):
    checkpoint = tmp_path / "checkpoint"
    checkpoint.mkdir()
    (checkpoint / "invented.txt").write_text("controlled artifact, no numerical data")
    provider = tmp_path / "hydramp_torch"
    provider.mkdir()
    (provider / "__init__.py").write_text("# invented runtime\n")
    return HydrAMPAnalogueBundle(
        str(checkpoint),
        {"invented.txt": sha256(checkpoint / "invented.txt")},
        source_manifest(provider),
        {"hydramp-torch": "0.0.0.dev6", "numpy": "2.4.6", "torch": "2.15.0+cpu"},
        "01" * 20,
        "02" * 20,
        "Controlled fixtures only, no biological use",
        evidence_kind="controlled-fixture",
    )


@pytest.fixture
def limits():
    return HydrAMPLimits(9, 10, 1024**3, 512 * 1024**2, 1024**2, (0, 1))


class Array:
    def __init__(self, values):
        self.values = values

    def __len__(self):
        return len(self.values)

    def tolist(self):
        return self.values


class Tokens(Array):
    def __init__(self, sequences):
        self.sequences = sequences
        super().__init__([None] * len(sequences))

    def numpy(self):
        return self


@dataclass
class Candidate:
    trace_row: int
    attempt_index: int
    sequence: str
    amp: float
    mic: float


def fake_provider(events, fail=None, extra_encoder=False):
    evidence = artificial_receipt()

    def operation(name, value=None):
        events.append(name)
        if fail == name:
            raise RuntimeError("controlled " + name + " failure")
        return value

    class Encoder:
        calls = 0

        def encode_tokens(self, values):
            self.calls += 1
            return operation("scale" if self.calls == 1 else "mean")

    class Core:
        calls = 0

        def score_tokens(self, values):
            self.calls += 1
            return operation(
                "prototype_score" if self.calls == 1 else "generated_score"
            )

        def decode_conditioned(self, values):
            return operation("decoder")

    class Generator:
        def __init__(self, encoder, core, **kwargs):
            self.encoder = encoder
            self.core = core

        def generate_with_trace(self, tokens, **kwargs):
            operation("analogue")
            self.encoder.encode_tokens(Array([None] * 3))
            self.core.score_tokens(Array([None] * 3))
            self.encoder.encode_tokens(Array([None] * 9))
            if extra_encoder:
                self.encoder.encode_tokens(Array([None] * 9))
            self.core.decode_conditioned(Array([None] * 9))
            self.core.score_tokens(Array([None] * 9))
            data = {
                k: Array(v)
                for k, v in evidence.original_trace.items()
                if k
                not in ("results", "sequences", "seed", "temperature", "n_attempts")
            }
            data.update(
                seed=7,
                temperature=1.0,
                n_attempts=3,
                sequences=evidence.original_trace["sequences"],
                results=tuple(
                    SimpleNamespace(
                        **{
                            **dict(r),
                            "candidates": tuple(
                                Candidate(**c) for c in r["candidates"]
                            ),
                        }
                    )
                    for r in evidence.original_trace["results"]
                ),
            )
            return SimpleNamespace(**data)

    return SimpleNamespace(
        encode_sequences=lambda seqs: operation("codec", Tokens(seqs)),
        translate_tokens=lambda values: values.sequences,
        load_encoder_checkpoint=lambda *a: operation("encoder_load", Encoder()),
        load_checkpoint=lambda *a: operation("core_load", Core()),
        HydrAMPAnalogueGenerator=Generator,
    )


def load_control(monkeypatch, events, **kwargs):
    provider = fake_provider(events, **kwargs)
    fake_torch = SimpleNamespace(
        version=SimpleNamespace(cuda=None),
        set_num_threads=lambda n: None,
        set_num_interop_threads=lambda n: None,
        get_num_threads=lambda: 1,
        get_num_interop_threads=lambda: 1,
    )

    def load(config, state, *, analogue=False):
        assert analogue
        state["runtime"] = {
            "versions": config["expected_versions"],
            "source_commit": config["source_commit"],
        }
        return provider, object(), fake_torch

    monkeypatch.setattr(worker, "_load_provider", load)


def call(bundle, limits, **changes):
    args = dict(
        parents=artificial_receipt().parents,
        seed=7,
        temperature=1.0,
        n_attempts=3,
        snapshot_id="controlled-route",
        bundle=bundle,
        limits=limits,
        worker_python=sys.executable,
    )
    args.update(changes)
    return route.redesign_hydramp(**args)


def in_process_worker(monkeypatch, events, **kwargs):
    load_control(monkeypatch, events, **kwargs)

    def execute(request, directory, limits, python, **kwargs):
        assert kwargs == {
            "request_module": "peptidemt._hydramp_analogue_cli",
            "response_schema": "peptidemt.hydramp_analogue_worker@1",
        }
        return worker.run(request, directory / "state.json")

    monkeypatch.setattr(route, "_execute_worker", execute)


def test_complete_artificial_flow_uses_owner_codec_and_separate_assessment(
    bundle, limits, monkeypatch
):
    events = []
    in_process_worker(monkeypatch, events)
    receipt = call(bundle, limits)
    assert receipt.completed and receipt.issues == ()
    assert receipt.provenance.evidence_kind == "controlled-fixture"
    assert [x.trace_row for x in receipt.links] == [6, 0, 1, 4, 2]
    assert (
        receipt.progress["neural_evaluations_attempted"]
        == receipt.progress["neural_evaluations_completed"]
        == 7
    )
    assert events == [
        "codec",
        "encoder_load",
        "core_load",
        "analogue",
        "scale",
        "prototype_score",
        "mean",
        "decoder",
        "generated_score",
    ]
    assert "native_sampling" in receipt.progress["completed"]
    assert not any(
        "pca" in op or "descriptor" in op for op in receipt.progress["completed"]
    )
    assert receipt.provenance.details["retries"] == 0
    assert (
        HydrAMPAnalogueReceipt.from_json(receipt.to_json()).content_id
        == receipt.content_id
    )
    assert len(receipt.proposals()) == 5


def test_integer_temperature_uses_the_native_float_request_semantics(
    bundle, limits, monkeypatch
):
    events = []
    in_process_worker(monkeypatch, events)
    receipt = call(bundle, limits, temperature=1)
    assert receipt.completed and not receipt.issues
    assert type(receipt.temperature) is float and receipt.temperature == 1.0


@pytest.mark.parametrize(
    "failure,completed",
    [
        ("codec", 0),
        ("encoder_load", 0),
        ("core_load", 0),
        ("scale", 0),
        ("prototype_score", 1),
        ("mean", 3),
        ("decoder", 4),
        ("generated_score", 5),
    ],
)
def test_each_partial_stage_preserves_known_completion_without_retry(
    bundle, limits, monkeypatch, failure, completed
):
    events = []
    in_process_worker(monkeypatch, events, fail=failure)
    with pytest.warns(HydrAMPFailureWarning):
        receipt = call(bundle, limits)
    assert not receipt.completed and not receipt.links
    assert receipt.progress["neural_evaluations_completed"] == completed
    assert "native_sampling" not in receipt.progress["completed"]
    assert receipt.provenance.details["retries"] == 0
    assert events.count(failure) == 1
    assert receipt.outcomes[0].status == (
        "interrupted" if "analogue" in events else "not_attempted"
    )


def test_extra_provider_call_blocked_before_dispatch(bundle, limits, monkeypatch):
    events = []
    in_process_worker(monkeypatch, events, extra_encoder=True)
    with pytest.warns(HydrAMPFailureWarning):
        receipt = call(bundle, limits)
    assert not receipt.completed and events.count("mean") == 1
    assert receipt.progress["neural_evaluations_completed"] == 4
    assert "decoder" not in events


def test_empty_and_all_incompatible_batches_do_not_start_worker(
    bundle, limits, monkeypatch
):
    def forbidden(*args, **kwargs):
        raise AssertionError("Worker must not start")

    monkeypatch.setattr(route, "_execute_worker", forbidden)
    for parents in (
        [],
        [
            SequenceRecord(None),
            "",
            SequenceRecord("ACD", chemistry={"terminal": "modified"}),
        ],
    ):
        receipt = call(bundle, limits, parents=parents)
        assert receipt.completed and receipt.issues == () and receipt.proposals() == ()
        assert (
            receipt.provenance.details["execution"]
            == "not-requested:no-compatible-parents"
        )
        assert not receipt.progress


def test_row_limit_checked_before_worker(bundle, limits, monkeypatch):
    monkeypatch.setattr(
        route, "_execute_worker", lambda *a, **k: pytest.fail("Worker started")
    )
    with pytest.warns(HydrAMPFailureWarning):
        receipt = call(bundle, replace(limits, max_records=8))
    assert not receipt.completed and receipt.failures == ("input_limit",)
    assert all(o.status in ("not_attempted", "incompatible") for o in receipt.outcomes)


@pytest.mark.parametrize(
    "change",
    [
        {"seed": True},
        {"seed": -1},
        {"temperature": float("nan")},
        {"temperature": 10**1000},
        {"temperature": True},
        {"n_attempts": 0},
        {"n_attempts": True},
        {"snapshot_id": ""},
        {"worker_python": "python"},
    ],
)
def test_bad_arguments_raise_before_provider_or_worker(
    bundle, limits, monkeypatch, change
):
    monkeypatch.setattr(
        route, "_execute_worker", lambda *a, **k: pytest.fail("Worker started")
    )
    with pytest.raises((ValueError, TypeError)):
        call(bundle, limits, **change)


def test_parent_source_binding_rejects_wrong_returned_evidence(
    bundle, limits, monkeypatch
):
    events = []
    in_process_worker(monkeypatch, events)
    original = route._execute_worker

    def wrong(*args, **kwargs):
        response = original(*args, **kwargs)
        receipt = HydrAMPAnalogueReceipt.from_json(response["receipt"])
        response["receipt"] = replace(receipt, snapshot_id="other-execution").to_json()
        return response

    monkeypatch.setattr(route, "_execute_worker", wrong)
    with pytest.warns(HydrAMPFailureWarning):
        receipt = call(bundle, limits)
    assert receipt.failures == ("output_failure",) and not receipt.links
    assert "unreceived_receipt" in receipt.provenance.details


def test_attribution_failure_is_separate_from_completed_science(
    bundle, limits, monkeypatch
):
    events = []
    in_process_worker(monkeypatch, events)

    def unavailable():
        raise RuntimeError("controlled attribution failure")

    monkeypatch.setattr(attribution, "_load_backend", unavailable)
    monkeypatch.setattr(attribution, "is_installed", lambda name: True)
    with pytest.warns(HydrAMPAttributionWarning):
        receipt = call(bundle, limits)
    assert receipt.completed and not receipt.issues and len(receipt.links) == 5
    assert (
        receipt.provenance.details["scientific_attribution"]["status"]
        == "provider-failed"
    )
    assert (
        receipt.provenance.details["scientific_attribution"]["failure_type"]
        == "RuntimeError"
    )


def test_bundle_no_pca_modlamp_or_implicit_public_installer(bundle):
    assert not {"pca_path", "pca_sha256"} & {f.name for f in fields(bundle)}
    assert "modlamp" not in bundle.expected_versions
    assert replace(bundle, checkpoint_root="/relocated").bundle_id == bundle.bundle_id
    with pytest.raises(ValueError):
        replace(bundle, evidence_kind="invented-unqualified-kind")
    assert "encode_sequences" not in inspect.getsource(route)


def test_worker_preflight_source_mismatch_precedes_provider(
    bundle, limits, monkeypatch, tmp_path
):
    captured = {}

    def capture(request, *args, **kwargs):
        captured.update(request)
        return {"failure": "controlled", "cause_type": "Fixture"}

    monkeypatch.setattr(route, "_execute_worker", capture)
    with pytest.warns(HydrAMPFailureWarning):
        call(bundle, limits)
    captured["consumer_source_sha256"] = {"invented.py": "0" * 64}
    monkeypatch.setattr(
        worker, "_load_provider", lambda *a, **k: pytest.fail("Provider imported")
    )
    with pytest.raises(ValueError, match="source/version"):
        worker.run(captured, tmp_path / "state.json")


def test_identity_preflight_of_analogue_requires_neither_pca_nor_modlamp(
    bundle, monkeypatch, tmp_path
):
    roots = {}
    for dist, package in [
        ("hydramp-torch", "hydramp_torch"),
        ("numpy", "numpy"),
        ("torch", "torch"),
    ]:
        root = tmp_path / package
        root.mkdir(exist_ok=True)
        (root / "__init__.py").write_text(
            "# invented runtime\n" if package == "hydramp_torch" else "# test\n"
        )
        roots[dist] = root
    monkeypatch.setattr(
        identity.importlib.metadata,
        "version",
        lambda name: bundle.expected_versions[name],
    )
    monkeypatch.setattr(
        identity.importlib.metadata,
        "distribution",
        lambda name: SimpleNamespace(
            locate_file=lambda path: roots[name].parent / path
        ),
    )
    monkeypatch.setattr(
        identity.importlib.util,
        "find_spec",
        lambda name: SimpleNamespace(origin=str(tmp_path / name / "__init__.py")),
    )
    config = {f.name: getattr(bundle, f.name) for f in fields(bundle)}
    data = identity._provider_identity(config, analogue=True)
    assert set(data["import_origins"]) == {"numpy", "torch", "hydramp_torch"}
    (Path(bundle.checkpoint_root) / "invented.txt").write_text("changed")
    with pytest.raises(ValueError, match="checkpoint"):
        identity._provider_identity(config, analogue=True)


def test_public_new_names_are_lazy_and_reachable():
    assert peptidemt.HydrAMPAnalogueBundle is route.HydrAMPAnalogueBundle
    assert peptidemt.redesign_hydramp is route.redesign_hydramp
    with pytest.raises(AttributeError):
        getattr(peptidemt, "invented_missing_name")
