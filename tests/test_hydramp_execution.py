"""Controlled execution/transport tests. No real model, PCA or descriptor runs."""

import inspect
import json
import os
import shutil
import signal
import subprocess
import sys
import time
import venv
from dataclasses import fields, replace
from pathlib import Path
from types import SimpleNamespace

import ackredit
import pytest

if sys.platform != "linux":
    pytest.skip(
        "The isolated HydrAMP execution route is Linux CPU only",
        allow_module_level=True,
    )

import peptidemt
from peptidemt import HydrAMPBundle, HydrAMPLimits, HydrAMPReceipt, Provenance
from peptidemt import _attribution as attribution
from peptidemt import _hydramp_process as process
from peptidemt import _hydramp_worker as worker
from peptidemt import hydramp as route
from peptidemt._diagnostics import (
    HydrAMPAttributionWarning,
    HydrAMPFailureWarning,
    RequiredDependencyError,
)


@pytest.fixture
def bundle(tmp_path):
    root = tmp_path / "checkpoint"
    root.mkdir()
    (root / "fixture.dat").write_text("invented, never parsed as a weight")
    pca = tmp_path / "fixture.numeric"
    pca.write_text("invented, never parsed as PCA")
    source = tmp_path / "hydramp_torch"
    source.mkdir()
    (source / "__init__.py").write_text("# invented installed provider identity\n")
    return HydrAMPBundle(
        str(root),
        {"fixture.dat": process.sha256(root / "fixture.dat")},
        str(pca),
        process.sha256(pca),
        process.source_manifest(source),
        {
            "hydramp-torch": "0.0.0.dev3",
            "numpy": "2.4.6",
            "torch": "2.15.0+cpu",
            "modlamp": "4.3.3",
        },
        "01" * 20,
        "02" * 20,
        "Invented fixture: no scientific use or execution",
    )


@pytest.fixture
def limits():
    return HydrAMPLimits(2, 10, 1024**3, 512 * 1024**2, 1024**2, (0, 1))


def request(bundle, limits):
    return {
        "schema": "peptidemt.hydramp_request@1",
        "n_target": 2,
        "seed": 7,
        "snapshot_id": "controlled",
        "bundle_id": bundle.bundle_id,
        "bundle": {f.name: getattr(bundle, f.name) for f in fields(bundle)},
        "limits": {f.name: getattr(limits, f.name) for f in fields(limits)},
        "consumer_source_sha256": process.source_manifest(
            Path(peptidemt.__file__).parent
        ),
        "qualification_reference": None,
        "consumer_version": worker.importlib.metadata.version("peptidemt"),
    }


def call(bundle, limits, **changes):
    arguments = dict(
        n_target=2,
        seed=7,
        snapshot_id="controlled",
        bundle=bundle,
        limits=limits,
        worker_python=sys.executable,
    )
    arguments.update(changes)
    return route.generate_hydramp(**arguments)


def test_bundle_identity_is_detached_and_independent_of_artifact_location(bundle):
    relocated = replace(
        bundle, checkpoint_root="/another/checkpoint", pca_path="/another/pca"
    )
    assert relocated.bundle_id == bundle.bundle_id
    with pytest.raises(TypeError):
        bundle.expected_versions["torch"] = "changed"
    with pytest.raises(ValueError, match="relative"):
        replace(bundle, checkpoint_sha256={"../outside": "a" * 64})
    with pytest.raises(ValueError, match="SHA-256"):
        replace(bundle, pca_sha256="not-a-digest")


@pytest.mark.parametrize(
    "change",
    [
        {"max_records": True},
        {"wall_seconds": float("nan")},
        {"rss_stop_bytes": 0},
        {"cpu_ids": (0, 0)},
        {"nice": -1},
    ],
)
def test_invalid_limits_rejected_before_any_child(limits, change):
    with pytest.raises(ValueError):
        replace(limits, **change)


def test_record_and_platform_guards_never_launch_a_worker(bundle, limits, monkeypatch):
    monkeypatch.setattr(
        route, "_execute_worker", lambda *a: pytest.fail("Unexpected child")
    )
    with pytest.warns(HydrAMPFailureWarning):
        result = call(bundle, limits, n_target=3)
    assert result.failures == ("input_limit",) and not result.native_results
    monkeypatch.setattr(route.sys, "platform", "not-linux")
    with pytest.warns(HydrAMPFailureWarning):
        result = call(bundle, limits)
    assert result.failures == ("unsupported_host",)


class Array:
    def __init__(self, values):
        self.values = values

    def tolist(self):
        return self.values

    def numpy(self):
        return self


def native(sequence, amp, mic):
    return dict(
        sequence=sequence,
        amp=amp,
        mic=mic,
        length=len(sequence),
        hydrophobicity=0.1,
        hydrophobic_moment=0.2,
        charge=1.0,
        isoelectric_point=7.0,
    )


def fake_provider(events, descriptor_failure=False):
    class Properties:
        def prepare(self):
            events.append("prepare")

        def __call__(self, sequences):
            events.append(("properties", sequences))
            if descriptor_failure:
                raise ValueError("Controlled descriptor failure")
            return {"controlled": True}

    class Projection:
        def __init__(self, *args, **kwargs):
            events.append(("projection", args, kwargs))

        def inverse_transform(self, values):
            events.append("inverse")
            return Array([[1 + 2**-30], [2 + 2**-30]])

    class Model:
        def decode_conditioned(self, values):
            events.append("decode")

        def score_tokens(self, values):
            events.append("score")

    def load(*args):
        events.append("checkpoint")
        return Model()

    class Generator:
        def __init__(self, model, projection, *, property_provider):
            self.model, self.projection, self.properties = (
                model,
                projection,
                property_provider,
            )

        def generate_with_trace(self, **kwargs):
            assert kwargs == dict(
                mode="amp",
                n_target=2,
                seed=7,
                filter_out=False,
                properties=True,
                n_attempts=1,
            )
            self.properties.prepare()
            self.projection.inverse_transform(Array([[0.0], [1.0]]))
            self.model.decode_conditioned(Array([[1.0], [2.0]]))
            self.model.score_tokens(Array([[1, 0, 2], [0, 3, 4]]))
            self.properties(["MKW", "ACD"])
            return SimpleNamespace(
                seed=7,
                native_results=(native("MKW", 0.75, 0.1), native("ACD", 0.25, 0.2)),
                returned_input_indices=(1, 0),
                sequences=("ACD", "MKW"),
                sampled_latents=Array([[0.0], [1.0]]),
                conditioned=Array([[1 + 2**-30], [2 + 2**-30]]),
                tokens=Array([[1, 0, 2], [0, 3, 4]]),
                amp=Array([0.25, 0.75]),
                mic=Array([0.2, 0.1]),
            )

    class Archive(dict):
        def __enter__(self):
            return self

        def __exit__(self, *args):
            pass

    def load_pca(path, *, allow_pickle):
        assert allow_pickle is False
        events.append("pca_load")
        return Archive(
            components="fixture",
            mean="fixture",
            whiten=False,
            explained_variance="fixture",
        )

    torch = SimpleNamespace(
        version=SimpleNamespace(cuda=None),
        set_num_threads=lambda n: events.append(("threads", n)),
        set_num_interop_threads=lambda n: events.append(("interop", n)),
        get_num_threads=lambda: 1,
        get_num_interop_threads=lambda: 1,
    )
    provider = SimpleNamespace(
        Modlamp433Properties=Properties,
        PCAProjection=Projection,
        load_checkpoint=load,
        HydrAMPGenerator=Generator,
    )
    return provider, SimpleNamespace(load=load_pca), torch


def runtime(bundle):
    return {
        "versions": dict(bundle.expected_versions),
        "source_commit": bundle.source_commit,
    }


def controlled_worker(bundle, limits, monkeypatch, path, *, fail=False):
    events = []

    def load(config, state):
        state["runtime"] = runtime(bundle)
        return fake_provider(events, fail)

    monkeypatch.setattr(worker, "_load_provider", load)
    return worker.run(request(bundle, limits), path), events


def test_worker_delegates_once_and_preserves_original_trace_precision(
    bundle, limits, tmp_path, monkeypatch
):
    response, events = controlled_worker(
        bundle, limits, monkeypatch, tmp_path / "state.json"
    )
    receipt = HydrAMPReceipt.from_json(response["receipt"])
    assert receipt.issues == () and receipt.returned_input_indices == (1, 0)
    assert [v.proposal.sequence for v in receipt.inputs] == ["MKW", "ACD"]
    assert receipt.inputs[0].issues == ("sequence_changing_native_preprocessing",)
    trace = receipt.inputs[0].proposal.context["generation"]["original_trace"]
    assert trace["tokens"] == (0, 3, 4)
    assert trace["conditioned"] == (2 + 2**-30,) and trace["decoder_input"] == (2.0,)
    for name in ("pca_load", "checkpoint", "inverse", "decode", "score"):
        assert events.count(name) == 1
    assert all(value == 1 for value in response["state"]["attempted"].values())
    assert len(response["state"]["completed"]) == 7


def test_failed_descriptors_preserve_completed_branches_without_retry(
    bundle, limits, tmp_path, monkeypatch
):
    response, events = controlled_worker(
        bundle, limits, monkeypatch, tmp_path / "state.json", fail=True
    )
    assert response["failure"] == "native_descriptors" and "receipt" not in response
    assert "native_scoring" in response["state"]["completed"]
    assert "native_descriptors" not in response["state"]["completed"]
    assert events.count("decode") == events.count("score") == 1


def test_parent_receiving_attribution_and_saved_reader_are_separate(
    bundle, limits, tmp_path, monkeypatch
):
    response, _ = controlled_worker(
        bundle, limits, monkeypatch, tmp_path / "state.json"
    )

    def execution(submitted, *args):
        receipt = HydrAMPReceipt.from_json(response["receipt"])
        return {
            **response,
            "receipt": replace(receipt, snapshot_id=submitted["snapshot_id"]).to_json(),
        }

    monkeypatch.setattr(route, "_execute_worker", execution)
    with ackredit.session("controlled-parent"):
        with ackredit.capture("enclosing") as enclosing:
            first = call(bundle, limits)
            second = call(bundle, limits, snapshot_id="controlled-repeat")
        assert first.native_results == second.native_results
        info = first.provenance.details["scientific_attribution"]
        assert info["status"] == "captured" and len(info["bibliography"]) == 7
        assert any(
            i["id"] == "doi:10.1038/s41467-023-36994-z"
            for i in info["ackredit"]["items"]
        )
        assert len(enclosing.attribution.to_dict()["uses"]) == 14
        before = ackredit.get_attribution().to_dict()
        replay = HydrAMPReceipt.from_json(first.to_json())
        assert replay.to_json() == first.to_json()
        assert ackredit.get_attribution().to_dict() == before
    assert not replay.provenance.qualification_reference


def test_partial_attribution_omits_uncompleted_descriptors_and_survives_provider_failure(
    bundle, limits, tmp_path, monkeypatch
):
    response, _ = controlled_worker(
        bundle, limits, monkeypatch, tmp_path / "state.json", fail=True
    )
    monkeypatch.setattr(route, "_execute_worker", lambda *a: response)
    monkeypatch.setattr(
        attribution,
        "_load_backend",
        lambda: (_ for _ in ()).throw(RuntimeError("controlled")),
    )
    with pytest.warns((HydrAMPFailureWarning, HydrAMPAttributionWarning)):
        receipt = call(bundle, limits)
    assert not receipt.completed and receipt.failures == ("native_descriptors",)
    info = receipt.provenance.details["scientific_attribution"]
    assert info["status"] == "provider-failed"
    assert not any(x["item"].get("title") == "modlAMP" for x in info["bibliography"])
    assert len(info["bibliography"]) == 6


def test_wrong_receipt_cannot_replace_request_identity(bundle, limits, monkeypatch):
    wrong = HydrAMPReceipt(
        "other", 2, 7, (), (), Provenance("hydramp-torch", bundle.bundle_id, "native")
    )
    monkeypatch.setattr(
        route, "_execute_worker", lambda *a: {"receipt": wrong.to_json()}
    )
    with pytest.warns(HydrAMPFailureWarning):
        result = call(bundle, limits)
    assert result.failures == ("output_failure",) and not result.native_results
    assert result.snapshot_id == "controlled"
    assert result.provenance.details["unreceived_receipt"] == wrong.to_json()


def test_identity_preflight_rejects_asset_or_source_changes_without_importing_provider(
    bundle, tmp_path, monkeypatch
):
    origin = tmp_path / "hydramp_torch/__init__.py"
    monkeypatch.setattr(
        worker.importlib.metadata, "version", lambda n: bundle.expected_versions[n]
    )
    monkeypatch.setattr(
        worker.importlib.metadata,
        "distribution",
        lambda n: SimpleNamespace(locate_file=lambda p: tmp_path / p),
    )
    monkeypatch.setattr(
        worker.importlib.util,
        "find_spec",
        lambda n: SimpleNamespace(origin=str(tmp_path / n / "__init__.py")),
    )
    config = {f.name: getattr(bundle, f.name) for f in fields(bundle)}
    assert worker._provider_identity(config)["versions"] == bundle.expected_versions
    Path(bundle.pca_path).write_text("changed")
    with pytest.raises(ValueError, match="PCA"):
        worker._provider_identity(config)
    origin.write_text("# changed provider")
    with pytest.raises(ValueError, match="source"):
        worker._provider_identity(config)


def test_absent_provider_uses_guard_with_installers_disabled(bundle, monkeypatch):
    import depdigest.core.checker as checker

    original = checker.find_spec
    monkeypatch.setattr(
        checker,
        "find_spec",
        lambda name, *a: None if name == "hydramp_torch" else original(name, *a),
    )
    with pytest.raises(RequiredDependencyError) as observed:
        worker._load_provider(
            {f.name: getattr(bundle, f.name) for f in fields(bundle)}, {}
        )
    assert "hydramp_torch" in str(observed.value)
    assert "pip install hydramp_torch" not in str(observed.value)


def test_tampered_worker_budget_rejected_before_provider(
    bundle, limits, tmp_path, monkeypatch
):
    submitted = request(bundle, limits)
    submitted["n_target"] = 3
    monkeypatch.setattr(
        worker, "_load_provider", lambda *args: pytest.fail("Loaded a provider")
    )
    with pytest.raises(ValueError, match="record"):
        worker.run(submitted, tmp_path / "state.json")


def test_missing_or_ambiguous_protocol_response_is_not_a_completed_run(
    bundle, limits, tmp_path, monkeypatch
):
    monkeypatch.setattr(
        route, "supervise", lambda *args: {"failure": None, "returncode": 0}
    )
    submitted = request(bundle, limits)
    response = route._execute_worker(submitted, tmp_path, limits, sys.executable)
    assert response["failure"] == "output_failure"
    (tmp_path / "response.json").write_text('{"schema":"a","schema":"b"}')
    response = route._execute_worker(submitted, tmp_path, limits, sys.executable)
    assert (
        response["failure"] == "output_failure"
        and response["cause_type"] == "ValueError"
    )


def test_full_public_route_across_process_with_explicit_artificial_provider(
    bundle, limits, tmp_path
):
    """A model-shaped stand-in tests transport; no learned library/array loads."""
    prefix = tmp_path / "artificial-worker"
    venv.EnvBuilder(with_pip=False, system_site_packages=True).create(prefix)
    site = (
        prefix
        / f"lib/python{sys.version_info.major}.{sys.version_info.minor}/site-packages"
    )
    shutil.copytree(
        Path(peptidemt.__file__).parent,
        site / "peptidemt",
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
    )
    version = worker.importlib.metadata.version("peptidemt")
    distribution = site / ("peptidemt-" + version + ".dist-info")
    distribution.mkdir()
    (distribution / "METADATA").write_text(
        "Metadata-Version: 2.1\nName: peptidemt\nVersion: " + version + "\n"
    )
    native_source = (
        "from types import SimpleNamespace\n"
        + "\n".join(inspect.getsource(obj) for obj in (Array, native, fake_provider))
        + "\n_events=[]\n_provider,_numpy,_torch=fake_provider(_events)\nglobals().update(vars(_provider))\n"
    )
    code = {
        "hydramp_torch": native_source,
        "numpy": "from hydramp_torch import _numpy\nload=_numpy.load\n__version__='0.0.0'\n",
        "torch": "from hydramp_torch import _torch\nglobals().update(vars(_torch))\n__version__='0.0.0'\n",
        "modlamp": "# Artificial identity only; no descriptor library.\n",
    }
    for name, contents in code.items():
        package = site / name
        package.mkdir()
        (package / "__init__.py").write_text(contents)
        dist_name = "hydramp-torch" if name == "hydramp_torch" else name
        info = site / (dist_name.replace("-", "_") + "-0.0.0.dist-info")
        info.mkdir()
        (info / "METADATA").write_text(
            f"Metadata-Version: 2.1\nName: {dist_name}\nVersion: 0.0.0\n"
        )
    config = replace(
        bundle,
        provider_source_sha256=process.source_manifest(site / "hydramp_torch"),
        expected_versions={
            "hydramp-torch": "0.0.0",
            "numpy": "0.0.0",
            "torch": "0.0.0",
            "modlamp": "0.0.0",
        },
    )
    result = call(config, limits, worker_python=str(prefix / "bin/python"))
    assert result.completed and not result.failures and not result.issues
    assert [row["sequence"] for row in result.native_results] == ["MKW", "ACD"]
    assert result.returned_input_indices == (1, 0)
    assert result.provenance.details["state"]["runtime"]["executable"] == str(
        prefix / "bin/python"
    )
    assert result.provenance.details["scientific_attribution"]["status"] == "captured"
    assert HydrAMPReceipt.from_json(result.to_json()).to_json() == result.to_json()


@pytest.mark.parametrize("warning", [HydrAMPFailureWarning, HydrAMPAttributionWarning])
def test_new_diagnostics_render_and_reconstruct(warning):
    if warning is HydrAMPFailureWarning:
        event = warning(stage="controlled", cause_type="ValueError")
    else:
        event = warning(cause_type="ValueError")
    assert "HydrAMP" in str(event)
    assert type(event)(*event.args).args == event.args


def test_timeout_kills_owned_worker_and_descendant(limits, tmp_path):
    directory = tmp_path / "process"
    directory.mkdir()
    program = "import subprocess,sys,time;from pathlib import Path;p=subprocess.Popen([sys.executable,'-c','import time;time.sleep(30)']);Path('pid').write_text(str(p.pid));time.sleep(30)"
    result = process.supervise(
        [sys.executable, "-B", "-I", "-c", program],
        directory,
        replace(limits, wall_seconds=0.2),
    )
    assert result["failure"] == "timeout"
    pid = int((directory / "pid").read_text())
    try:
        assert "State:\tZ" in Path(f"/proc/{pid}/status").read_text()
    except FileNotFoundError:
        pass


def test_fast_oversized_output_and_host_memory_guard(limits, tmp_path, monkeypatch):
    work = tmp_path / "process"
    work.mkdir()
    result = process.supervise(
        [
            sys.executable,
            "-B",
            "-I",
            "-c",
            "from pathlib import Path;Path('output').write_bytes(b'x'*1000)",
        ],
        work,
        replace(limits, max_output_bytes=10),
    )
    assert result["failure"] == "output_limit"
    monkeypatch.setattr(process, "available_memory", lambda: 0)
    monkeypatch.setattr(
        process.subprocess, "Popen", lambda *a, **k: pytest.fail("Should not launch")
    )
    result = process.supervise([], work, replace(limits, min_available_memory_bytes=1))
    assert result == {"failure": "host_resource_guard", "started": False}


def test_parent_death_kills_worker_group_without_changing_host_signal_policy(
    limits, tmp_path
):
    work = tmp_path / "death"
    work.mkdir()
    package = str(Path(peptidemt.__file__).parent.parent)
    child_code = "import sys,json,subprocess,time,os;from pathlib import Path;sys.path.insert(0,sys.argv[1]);from peptidemt._hydramp_process import configure_child;configure_child(json.loads(sys.argv[2]),int(sys.argv[3]));p=subprocess.Popen([sys.executable,'-I','-c','import time;time.sleep(30)']);Path('group').write_text(json.dumps([os.getpid(),p.pid]));time.sleep(30)"
    parent_code = "import subprocess,sys,os;subprocess.Popen([sys.executable,'-B','-I','-c',sys.argv[1],sys.argv[2],sys.argv[3],str(os.getpid())],start_new_session=True).wait()"
    data = json.dumps({f.name: getattr(limits, f.name) for f in fields(limits)})
    parent = subprocess.Popen(
        [sys.executable, "-B", "-I", "-c", parent_code, child_code, package, data],
        cwd=work,
    )
    group = []
    try:
        deadline = time.monotonic() + 3
        while not (work / "group").exists() and time.monotonic() < deadline:
            time.sleep(0.02)
        group = json.loads((work / "group").read_text())
        parent.kill()
        parent.wait(timeout=3)
        deadline = time.monotonic() + 3
        for pid in group:
            while time.monotonic() < deadline:
                try:
                    if "State:\tZ" in Path(f"/proc/{pid}/status").read_text():
                        break
                except FileNotFoundError:
                    break
                time.sleep(0.02)
            else:
                pytest.fail("Owned child survived parent death")
    finally:
        if parent.poll() is None:
            parent.kill()
            parent.wait()
        if group:
            try:
                os.killpg(group[0], signal.SIGKILL)
            except ProcessLookupError:
                pass
