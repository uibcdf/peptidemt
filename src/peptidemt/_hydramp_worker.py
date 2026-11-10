"""Private installed-worker protocol; all learned operations belong to HydrAMP."""

import importlib.metadata
import importlib.util
import json
import os
import resource
import sys
from dataclasses import replace
from pathlib import Path

from ._data import decode, encode, freeze, load_json
from ._hydramp_process import configure_child, sha256, source_manifest


def _save(path, data):
    temporary = path.with_suffix(".writing")
    temporary.write_text(json.dumps(encode(freeze(data))), encoding="utf-8")
    temporary.replace(path)


def _provider_identity(config, observed=None, *, analogue=False):
    observed = observed if observed is not None else {}
    versions = {
        name: importlib.metadata.version(name) for name in config["expected_versions"]
    }
    observed["versions"] = versions
    if versions != dict(config["expected_versions"]):
        raise ValueError("Pinned scientific runtime versions changed")
    import_origins = {}
    packages = [("numpy", "numpy"), ("torch", "torch")]
    if not analogue:
        packages.append(("modlamp", "modlamp"))
    for distribution_name, import_name in packages:
        expected_origin = Path(
            importlib.metadata.distribution(distribution_name).locate_file(
                import_name + "/__init__.py"
            )
        ).resolve()
        candidate = importlib.util.find_spec(import_name)
        if (
            candidate is None
            or candidate.origin is None
            or Path(candidate.origin).resolve() != expected_origin
        ):
            raise ValueError("Installed runtime package is shadowed: " + import_name)
        import_origins[import_name] = str(expected_origin)
    observed["import_origins"] = import_origins
    distribution = importlib.metadata.distribution("hydramp-torch")
    origin = Path(distribution.locate_file("hydramp_torch/__init__.py")).resolve()
    observed["provider_origin"] = str(origin)
    spec = importlib.util.find_spec("hydramp_torch")
    if spec is None or spec.origin is None or Path(spec.origin).resolve() != origin:
        raise ValueError("Installed HydrAMP distribution is shadowed or editable")
    if source_manifest(origin.parent) != dict(config["provider_source_sha256"]):
        raise ValueError("Pinned installed HydrAMP source changed")
    root = Path(config["checkpoint_root"]).resolve()
    for relative, expected in config["checkpoint_sha256"].items():
        path = (root / relative).resolve()
        if not path.is_relative_to(root) or sha256(path) != expected:
            raise ValueError("Pinned checkpoint bytes changed: " + relative)
    if not analogue and sha256(config["pca_path"]) != config["pca_sha256"]:
        raise ValueError("Pinned numeric PCA changed")
    return {
        "versions": versions,
        "import_origins": {**import_origins, "hydramp_torch": str(origin)},
        "provider_origin": str(origin),
        "source_commit": config["source_commit"],
        "starter_commit": config["starter_commit"],
        "python": sys.version,
        "executable": sys.executable,
    }


def _load_provider(config, state, *, analogue=False):
    from depdigest import dep_digest

    @dep_digest("hydramp_torch")
    def load():
        state["stage"] = "runtime_identity"
        state["runtime"] = {}
        state["runtime"].update(
            _provider_identity(config, state["runtime"], analogue=True)
            if analogue
            else _provider_identity(config, state["runtime"])
        )
        state["stage"] = "provider_import"
        import hydramp_torch
        import numpy
        import torch

        imported_versions = {
            "numpy": str(numpy.__version__),
            "torch": str(torch.__version__),
        }
        state["runtime"]["imported_versions"] = imported_versions
        if any(
            imported_versions[name] != config["expected_versions"][name]
            for name in imported_versions
        ):
            raise ValueError(
                "Imported numerical runtime differs from its distribution metadata"
            )
        return hydramp_torch, numpy, torch

    return load()


def run(request, state_path):
    """Only main configures process bounds. Unit controls use invented providers."""
    from .hydramp import HydrAMPBundle, HydrAMPLimits

    config = request["bundle"]
    bundle = HydrAMPBundle(**config)
    limits = HydrAMPLimits(
        **{**request["limits"], "cpu_ids": tuple(request["limits"]["cpu_ids"])}
    )
    if (
        type(request["n_target"]) is not int
        or not 1 <= request["n_target"] <= limits.max_records
    ):
        raise ValueError("Invalid or oversized worker record request")
    if type(request["seed"]) is not int or not 0 <= request["seed"] < 2**32:
        raise ValueError("Invalid worker seed")
    from .results import Provenance

    Provenance(
        "hydramp-torch", bundle.bundle_id, "native", request["qualification_reference"]
    )
    if not isinstance(request["snapshot_id"], str) or not request["snapshot_id"]:
        raise ValueError("Invalid worker snapshot identifier")
    if (
        request.get("schema") != "peptidemt.hydramp_request@1"
        or bundle.bundle_id != request["bundle_id"]
    ):
        raise ValueError("Invalid worker request/bundle identity")
    if source_manifest(Path(__file__).parent) != dict(
        request["consumer_source_sha256"]
    ):
        raise ValueError("Worker PeptideMT source differs from the caller")
    if importlib.metadata.version("peptidemt") != request["consumer_version"]:
        raise ValueError("Worker PeptideMT version differs from the caller")
    state = {"stage": "dependency", "attempted": {}, "completed": [], "runtime": {}}

    def stage(name):
        state["stage"] = name
        _save(state_path, state)

    def reserve(name):
        if state["attempted"].get(name):
            raise RuntimeError("Single-operation budget exhausted: " + name)
        state["attempted"][name] = 1
        stage(name)

    def done(name):
        state["completed"].append(name)
        _save(state_path, state)

    stage("dependency")
    try:
        provider, np, torch = _load_provider(config, state)
        if torch.version.cuda is not None:
            raise ValueError("This route requires a CPU-only Torch build")
        torch.set_num_threads(limits.threads)
        torch.set_num_interop_threads(1)
        state["runtime"]["resource_controls"] = {
            "cpu_ids": sorted(os.sched_getaffinity(0)),
            "nice": os.nice(0),
            "address_space_bytes": resource.getrlimit(resource.RLIMIT_AS)[0],
            "torch_threads": torch.get_num_threads(),
            "torch_interop_threads": torch.get_num_interop_threads(),
            "cpu_only_build": torch.version.cuda is None,
        }
        native_properties = provider.Modlamp433Properties()
        native_properties.prepare()
        reserve("numeric_pca_loading")
        with np.load(config["pca_path"], allow_pickle=False) as archive:
            projection = provider.PCAProjection(
                archive["components"],
                archive["mean"],
                whiten=bool(archive["whiten"]),
                explained_variance=archive["explained_variance"],
            )
        done("numeric_pca_loading")
        reserve("checkpoint_loading")
        model = provider.load_checkpoint(
            config["checkpoint_root"], config["checkpoint_sha256"]
        )
        done("checkpoint_loading")
        captured = {}

        def tap(obj, name, operation):
            original = getattr(obj, name)

            def call(value):
                reserve(operation)
                result = original(value)
                if operation == "native_decoding":
                    captured["decoder_input"] = value.numpy().tolist()
                elif operation == "numeric_pca_inversion":
                    captured["pca_projected"] = result.tolist()
                done(operation)
                return result

            setattr(obj, name, call)

        class Properties:
            def prepare(self):
                native_properties.prepare()

            def __call__(self, sequences):
                reserve("native_descriptors")
                result = native_properties(sequences)
                done("native_descriptors")
                return result

        tap(model, "decode_conditioned", "native_decoding")
        tap(model, "score_tokens", "native_scoring")
        tap(projection, "inverse_transform", "numeric_pca_inversion")
        generator = provider.HydrAMPGenerator(
            model, projection, property_provider=Properties()
        )
        reserve("native_generation")
        trace = generator.generate_with_trace(
            mode="amp",
            n_target=request["n_target"],
            seed=request["seed"],
            filter_out=False,
            properties=True,
            n_attempts=1,
        )
        done("native_generation")
        stage("result_receiving")
        from . import HydrAMPReceipt, Provenance

        receipt = HydrAMPReceipt.from_trace(
            trace,
            snapshot_id=request["snapshot_id"],
            requested_count=request["n_target"],
            provenance=Provenance(
                "hydramp-torch",
                bundle.bundle_id,
                "native",
                request["qualification_reference"],
            ),
        )
        receipt = replace(
            receipt, original_trace={**receipt.original_trace, **captured}
        )
        stage("completed")
        state["runtime"]["worker_kernel_hwm_rss_bytes"] = (
            resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024
        )
        return {
            "schema": "peptidemt.hydramp_worker@1",
            "receipt": receipt.to_json(),
            "state": state,
        }
    except Exception as error:
        _save(state_path, state)
        return {
            "schema": "peptidemt.hydramp_worker@1",
            "failure": state["stage"],
            "cause_type": type(error).__name__,
            "cause_message": str(error)[:8192],
            "state": state,
        }


def main():
    request_path, response_path = map(Path, sys.argv[1:])
    request = decode(load_json(request_path.read_text(encoding="utf-8")))

    def audit(event, args):
        if event == "socket.connect":
            raise RuntimeError("Network is prohibited in this worker")

    try:
        configure_child(request["limits"], request["parent_pid"])
        sys.addaudithook(audit)
        result = run(request, request_path.parent / "state.json")
    except Exception as error:
        result = {
            "schema": "peptidemt.hydramp_worker@1",
            "failure": "worker_preflight",
            "cause_type": type(error).__name__,
            "cause_message": str(error)[:8192],
            "state": {},
        }
    _save(response_path, result)
