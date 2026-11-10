"""Isolated Python 3.8/3.14 owner-codec/head worker; exact approval precedes models."""

import argparse
import importlib.metadata
import importlib.util
import json
import os
import resource
import sys
import time
import traceback
from pathlib import Path


def local_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


core = local_module(
    "_historical_real", Path(__file__).with_name("hydramp_historical_real.py")
)


def write_new(path, value):
    blob = (
        json.dumps(value, ensure_ascii=False, allow_nan=False, indent=2) + "\n"
    ).encode()
    core.require(len(blob) <= 2 * 1024**2, "worker_output_size", "Bounded JSON output")
    with Path(path).open("xb") as stream:
        stream.write(blob)


def configure_site_metadata(site_packages):
    """Supply frozen-profile metadata without running site or .pth bootstrap."""
    import site

    prefix = str(Path(site_packages).parents[2])
    # -S leaves USER_SITE unset, but TensorFlow 2.2 iterates it as a path.
    # Point metadata only at the already approved profile, never the user home.
    site.ENABLE_USER_SITE = False
    site.USER_SITE = str(site_packages)
    site.USER_BASE = prefix
    site.PREFIXES = [prefix]


def schedule(proposal, provider, tokens, call, charge, retain):
    """Compose fixed requests; tests use method doubles, never artificial networks."""
    events = []
    for request in proposal["requests"]:
        charge(request)
        batch = tokens[request["indices"]]
        mic, amp = call(batch)
        event = {
            "tag": request["tag"],
            "indices": request["indices"],
            "MIC": mic,
            "auxiliary_AMP": amp if provider == "modern" else None,
        }
        retain(event)
        events.append(event)
    return events


def guards(mode, proposal):
    allowed = (
        {str(Path(x["path"]).resolve()) for x in proposal["assets"]}
        if mode == "score"
        else set()
    )
    opened, calls = [], []
    state = {"scoring": False, "legacy_model": None, "denied_dispatch": []}
    suffixes = {
        ".npy",
        ".npz",
        ".pkl",
        ".pickle",
        ".h5",
        ".hdf5",
        ".pt",
        ".pth",
        ".ckpt",
        ".onnx",
    }

    def audit(event, args):
        if event in (
            "socket.connect",
            "socket.connect_ex",
            "subprocess.Popen",
            "os.system",
            "os.posix_spawn",
            "os.fork",
        ):
            command = ""
            if event == "subprocess.Popen" and args:
                executable = Path(str(args[0])).name
                options = [
                    v
                    if isinstance(v, str) and v.startswith("-") and len(v) < 40
                    else "<arg>"
                    for v in (args[1] if isinstance(args[1], (list, tuple)) else [])
                ]
                state["denied_dispatch"].append(
                    {"event": event, "executable": executable, "options": options}
                )
                # Match OS denial semantics. Python 3.8 platform metadata handles
                # OSError and can report an unknown processor without spawning
                # uname. This permits no subprocess or alternate scientific route.
                raise PermissionError(
                    "Subprocess denied: " + executable + " " + repr(options)
                )
            raise RuntimeError(
                "Network/child dispatch is outside this worker: " + event + command
            )
        if event == "open" and isinstance(args[0], str):
            path = Path(args[0]).resolve()
            model_root = Path(proposal["model_root"]).resolve()
            is_model = path == model_root or model_root in path.parents
            if path.suffix.lower() in suffixes or is_model:
                if str(path) not in allowed:
                    raise RuntimeError("Unapproved parameter/PCA read: " + str(path))
                if str(path) not in opened:
                    opened.append(str(path))

    def profile(frame, event, arg):
        if (
            event == "c_call"
            and getattr(arg, "__module__", "") == "_pickle"
            and getattr(arg, "__name__", "") in ("load", "loads")
        ):
            raise RuntimeError("Pickle deserialization forbidden")
        if event != "call":
            return
        module, name = frame.f_globals.get("__name__", ""), frame.f_code.co_name
        if name in ("load", "loads") and module in ("pickle", "joblib.numpy_pickle"):
            raise RuntimeError("Pickle/PCA deserialization forbidden")
        native = module.startswith(
            ("keras.", "tensorflow.", "hydramp_torch.", "torch.nn.")
        )
        if native and name in (
            "fit",
            "fit_generator",
            "train_on_batch",
            "evaluate",
            "generate",
            "generate_unconstrained",
            "decode_conditioned",
            "load_encoder_checkpoint",
        ):
            raise RuntimeError("Uncommissioned model operation: " + name)
        if module.startswith("hydramp_torch") and name in (
            "load_checkpoint",
            "score_tokens",
        ):
            if mode != "score" or (name == "score_tokens" and not state["scoring"]):
                calls.append(name)
                raise RuntimeError("No model calls in codec-only mode")
        if (
            mode == "codec"
            and module.startswith("torch.nn.modules")
            and name in ("__init__", "_call_impl")
        ):
            raise RuntimeError("No neural modules in codec qualification")
        if native and name in ("predict", "predict_on_batch", "predict_generator"):
            if (
                mode != "score"
                or not state["scoring"]
                or frame.f_locals.get("self") is not state["legacy_model"]
            ):
                calls.append(name)
                raise RuntimeError("Unexpected prediction call")

    sys.addaudithook(audit)
    sys.setprofile(profile)
    return opened, calls, state


def runtime(proposal, provider, origins, start, denied_dispatch=None):
    site = proposal["profiles"][provider]["site_packages"]
    return {
        "executable": sys.executable,
        "python": sys.version,
        "inventory": {
            d.metadata["Name"]: d.version
            for d in importlib.metadata.distributions(path=[site])
        },
        "source_origins": origins,
        "cpu_ids": sorted(os.sched_getaffinity(0)),
        "numerical_threads": 1,
        "elapsed_seconds": time.monotonic() - start,
        "kernel_peak_rss_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        * 1024,
        "denied_dispatch": list(denied_dispatch or []),
    }


def native_array(values, dtype):
    return {
        "dtype": dtype,
        "shape": [len(values), 25],
        "values": values,
        "native_hex": core.native_bytes(values, dtype).hex(),
    }


def worker(mode, request_path, destination):
    request = core.data._parse(core.data._read(request_path))
    core.fields(
        request,
        "case provider plan execution_authority_json worker_sha256",
        "worker_request",
    )
    case, provider = request["case"], request["provider"]
    proposal, _ = core.raw_case(case)
    core.require(
        provider in core.PROVIDERS
        and core.identity(__file__)["sha256"] == request["worker_sha256"],
        "worker_binding",
        "Changed provider or worker source",
    )
    if mode == "score":
        # Check a fresh execution receipt before importing any scientific provider.
        core.execution_authority(
            request["plan"], request["execution_authority_json"], semantic=False
        )
    else:
        core.require(
            request["plan"] is None and request["execution_authority_json"] is None,
            "codec_authority",
            "D48 codec-only request required",
        )
    process = local_module(
        "_historical_process",
        Path(__file__).parents[1] / "src/peptidemt/_hydramp_process.py",
    )
    limits = {"address_space_bytes": 8 * 1024**3, "cpu_ids": [0, 1], "nice": 5}
    process.configure_child(limits, os.getppid())
    resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
    for key in (
        "OMP_NUM_THREADS",
        "OPENBLAS_NUM_THREADS",
        "MKL_NUM_THREADS",
        "NUMEXPR_NUM_THREADS",
        "TF_NUM_INTRAOP_THREADS",
        "TF_NUM_INTEROP_THREADS",
    ):
        os.environ[key] = "1"
    os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
    os.environ["KERAS_BACKEND"] = "tensorflow"
    os.environ["KERAS_HOME"] = str(Path(destination) / "keras-home")
    opened, calls, state = guards(mode, proposal)
    site = proposal["profiles"][provider]["site_packages"]
    # -I -S prevents executable .pth/bootstrap code. Only the exact frozen site
    # is exposed after guards, not any source worktree or shared fallback path.
    configure_site_metadata(site)
    sys.path.append(site)
    actual = {
        d.metadata["Name"]: d.version
        for d in importlib.metadata.distributions(path=[site])
    }
    core.require(
        core.normalized_inventory(actual)
        == core.normalized_inventory(proposal["profiles"][provider]["inventory"]),
        "runtime_inventory",
        "Changed exact frozen dependency profile",
    )
    destination = Path(destination)
    with (destination / "native-log.txt").open("xb") as log:
        os.dup2(log.fileno(), 1)
        os.dup2(log.fileno(), 2)
    start, origins = time.monotonic(), {}
    raw = None
    try:
        if provider == "legacy":
            import tensorflow as tf

            tf.config.threading.set_intra_op_parallelism_threads(1)
            tf.config.threading.set_inter_op_parallelism_threads(1)
            core.require(
                tf.config.threading.get_intra_op_parallelism_threads()
                == tf.config.threading.get_inter_op_parallelism_threads()
                == 1,
                "runtime_threads",
                "Unbounded TensorFlow threading",
            )
            from amp.data_utils import sequence

            origins["legacy_codec"] = core.identity(sequence.__file__)
            if mode == "codec":
                values = sequence.pad(
                    sequence.to_one_hot(core.source_views(case)), max_length=25
                )
                native = native_array(values.tolist(), str(values.dtype))
                core.require(
                    native["native_hex"] == values.tobytes(order="C").hex(),
                    "native_bytes",
                    "Original native byte order changed",
                )
                operations = {"to_one_hot": 1, "pad": 1}
            else:
                import numpy as np
                from amp.models.discriminators import veltri_amp_classifier
                from amp.utils import basic_model_serializer

                origins["legacy_loader"] = core.identity(
                    basic_model_serializer.__file__
                )
                origins["legacy_MIC_head"] = core.identity(
                    veltri_amp_classifier.__file__
                )
                np.random.seed(431)
                tf.random.set_seed(431)
        else:
            import torch

            torch.set_num_threads(1)
            torch.set_num_interop_threads(1)
            core.require(
                torch.get_num_threads() == torch.get_num_interop_threads() == 1,
                "runtime_threads",
                "Unbounded Torch threading",
            )
            import hydramp_torch
            from hydramp_torch import codec, inference

            origins["modern_codec"] = core.identity(codec.__file__)
            origins["modern_inference"] = core.identity(inference.__file__)
            if mode == "codec":
                values = hydramp_torch.encode_sequences(core.source_views(case))
                native = native_array(values.tolist(), str(values.dtype).split(".")[-1])
                core.require(
                    native["native_hex"] == values.numpy().tobytes(order="C").hex(),
                    "native_bytes",
                    "Modern native byte order changed",
                )
                operations = {"encode_sequences": 1}
            else:
                torch.manual_seed(431)
        if mode == "codec":
            core.check_tokens(case, provider, native)
            raw = {
                "schema": "peptidemt.hydramp_historical_codec_output@1",
                "provider": provider,
                "case_sha256": core.object_digest(case),
                "native": native,
                "runtime": runtime(
                    proposal, provider, origins, start, state["denied_dispatch"]
                ),
                "codec_operations": operations,
                "parameter_files_opened": opened,
                "neural_calls": len(calls),
            }
            write_new(destination / "result.json", raw)
            return 0
        plan = request["plan"]
        codec_result = core.data._parse(
            plan["codecs"]["captures"][provider]["raw_json"]
        )
        native = codec_result["native"]
        raw = {
            "schema": "peptidemt.hydramp_historical_score_output@1",
            "evidence_kind": "learned_model",
            "provider": provider,
            "plan_sha256": core.object_digest(plan),
            "native_input_sha256": core.digest(bytes.fromhex(native["native_hex"])),
            "head": "VeltriAMPClassifier_MIC",
            "events": [],
            "attempted": 0,
            "completed": 0,
            "parameter_files_opened": opened,
            "model_loads": 0,
            "failure": None,
            "runtime": runtime(
                proposal, provider, origins, start, state["denied_dispatch"]
            ),
        }
        if provider == "legacy":
            tokens = np.asarray(native["values"], dtype=np.int32)
            model = basic_model_serializer.load_master_model_components(
                proposal["model_root"], softmax=False
            )[3]
            state["legacy_model"] = model

            def score(batch):
                result = model.predict(batch, batch_size=len(batch), verbose=0)
                core.require(
                    str(result.dtype) == "float32" and result.shape == (len(batch), 1),
                    "native_score_shape",
                    "Original native MIC shape changed",
                )
                column = core.column(result.reshape(-1).tolist(), list(result.shape))
                core.require(
                    column["native_hex"] == result.tobytes(order="C").hex(),
                    "native_bytes",
                    "Original native score bytes changed",
                )
                return column, None
        else:
            tokens = torch.tensor(native["values"], dtype=torch.int64, device="cpu")
            hashes = {x["relative"]: x["sha256"] for x in proposal["assets"]}
            model = hydramp_torch.load_checkpoint(proposal["model_root"], hashes)

            def score(batch):
                amp, mic = model.score_tokens(batch)
                core.require(
                    str(mic.dtype) == str(amp.dtype) == "torch.float32"
                    and mic.device.type == amp.device.type == "cpu",
                    "native_score_dtype",
                    "Native CPU FP32 required",
                )
                mic_column, amp_column = (
                    core.column(mic.tolist(), list(mic.shape)),
                    core.column(amp.tolist(), list(amp.shape)),
                )
                core.require(
                    mic_column["native_hex"] == mic.numpy().tobytes(order="C").hex()
                    and amp_column["native_hex"]
                    == amp.numpy().tobytes(order="C").hex(),
                    "native_bytes",
                    "Modern native score bytes changed",
                )
                return mic_column, amp_column

        raw["model_loads"] = 1

        def charge(item):
            core.require(raw["attempted"] < 4, "call_cap", "No extra prediction")
            raw["attempted"] += 1
            write_new(
                destination / ("intent-" + item["tag"] + ".json"),
                {"tag": item["tag"], "attempted": raw["attempted"]},
            )
            state["scoring"] = True

        def retain(event):
            state["scoring"] = False
            raw["events"].append(event)
            raw["completed"] += 1
            write_new(destination / ("event-" + event["tag"] + ".json"), event)

        schedule(proposal, provider, tokens, score, charge, retain)
        raw["runtime"] = runtime(
            proposal, provider, origins, start, state["denied_dispatch"]
        )
        write_new(destination / "result.json", raw)
        return 0
    except Exception as error:
        if raw is None:
            raw = {
                "failure": {
                    "type": type(error).__name__,
                    "detail": str(error) + "\n" + traceback.format_exc(),
                },
                "parameter_files_opened": opened,
                "blocked_neural_calls": calls,
                "denied_dispatch": state["denied_dispatch"],
            }
        else:
            raw["failure"] = {"type": type(error).__name__, "detail": str(error)}
            raw["runtime"] = runtime(
                proposal, provider, origins, start, state["denied_dispatch"]
            )
        write_new(destination / "result.json", raw)
        return 1
    finally:
        sys.setprofile(None)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("codec", "score"))
    parser.add_argument("--request", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    return worker(args.mode, args.request, args.output)


if __name__ == "__main__":
    raise SystemExit(main())
