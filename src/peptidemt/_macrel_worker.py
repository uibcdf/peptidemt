"""Private isolated transport for the single approved native Macrel route."""

import hashlib
import importlib.metadata
import json
import os
import shutil
import sys
from contextlib import contextmanager
from importlib.resources import files
from pathlib import Path

from depdigest import dep_digest

from ._data import decode, encode, freeze
from ._diagnostics import RequiredDependencyError
from ._molsysmt import _load_molsysmt


@dep_digest("macrel")
def _load_macrel():
    import macrel
    from macrel.AMP_features import fasta_features
    from macrel.AMP_predict import predict

    return macrel, fasta_features, predict


def _sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _identity(name, module):
    distribution = importlib.metadata.distribution(name)
    return {
        "version": distribution.version,
        "import_origin": str(Path(module.__file__).resolve()),
        "distribution_root": str(Path(distribution.locate_file("")).resolve()),
    }


def _write_transport(msm, records, directory):
    """Join owner-serialized records; no format parsing or local FASTA grammar."""
    path = directory / "submitted.fasta"
    piece = directory / "occurrence.fasta"
    with path.open("wb") as output:
        for token, sequence in records:
            # The released 0.23.0 route supports canonical bare strings. Explicit
            # amino_acids_1: prefixes exist only in newer inspected owner source.
            record = msm.convert(sequence, to_form="biopython.SeqRecord")
            if str(record.seq) != sequence:
                raise ValueError("MolSysMT changed the submitted sequence")
            # Opaque transport identity belongs to the consumer's occurrence map.
            record.id = token
            record.name = token
            record.description = ""
            msm.convert(record, to_form=str(piece))
            with piece.open("rb") as source:
                shutil.copyfileobj(source, output)
    piece.unlink(missing_ok=True)
    return path


def _scalar(value):
    if type(value) in (str, bool, int, float) or value is None:
        return value
    # NumPy scalar.item() preserves the exact value in a Python scalar, with
    # original DataFrame dtypes retained separately. No decimal formatting.
    result = value.item()
    if type(result) not in (str, bool, int, float) and result is not None:
        raise TypeError("Unsupported native scalar")
    return result


def _frame(frame):
    columns = [_scalar(column) for column in frame.columns]
    if any(not isinstance(column, str) for column in columns) or len(
        set(columns)
    ) != len(columns):
        raise ValueError("Native columns must be unique strings")
    index = [_scalar(token) for token in frame.index]
    if any(not isinstance(token, str) or not token for token in index):
        raise ValueError("Native rows require nonempty occurrence tokens")
    return {
        "columns": columns,
        "dtypes": [str(dtype) for dtype in frame.dtypes],
        "index": index,
        "values": [
            [_scalar(frame.iloc[row, col]) for col in range(len(columns))]
            for row in range(len(frame))
        ],
    }


def _configure_process(request, state):
    import resource

    memory = request["memory_bytes"]
    resource.setrlimit(resource.RLIMIT_AS, (memory, memory))
    cpus = request.get("cpu_ids")
    if cpus is not None:
        if not set(cpus) <= os.sched_getaffinity(0):
            raise ValueError("Requested CPUs exceed the inherited allowed affinity")
        os.sched_setaffinity(0, set(cpus))
    requested_nice = request.get("nice", 0)
    if requested_nice and os.getpriority(os.PRIO_PROCESS, 0) < requested_nice:
        os.setpriority(os.PRIO_PROCESS, 0, requested_nice)
    state["intra_op_threads"] = request.get("intra_op_threads")
    state["details"]["resource_controls"] = {
        "address_space_bytes": memory,
        "cpu_ids": sorted(os.sched_getaffinity(0)),
        "nice": os.getpriority(os.PRIO_PROCESS, 0),
        "numerical_environment": {
            name: os.environ.get(name)
            for name in (
                "OPENBLAS_NUM_THREADS",
                "OMP_NUM_THREADS",
                "MKL_NUM_THREADS",
                "NUMEXPR_NUM_THREADS",
            )
        },
    }


def _resource_usage():
    import resource

    usage = resource.getrusage(resource.RUSAGE_SELF)
    return {
        "peak_rss_bytes": usage.ru_maxrss * 1024,
        "user_cpu_seconds": usage.ru_utime,
        "system_cpu_seconds": usage.ru_stime,
    }


@contextmanager
def _onnx_threads(threads):
    """Set public runtime options only inside this isolated Macrel operation."""
    if threads is None:
        yield "Macrel defaults; no ONNX session overrides"
        return
    import onnxruntime as rt

    original = rt.InferenceSession

    def bounded_session(*args, **kwargs):
        options = rt.SessionOptions()
        options.intra_op_num_threads = threads
        options.inter_op_num_threads = 1
        options.execution_mode = rt.ExecutionMode.ORT_SEQUENTIAL
        options.add_session_config_entry("session.intra_op.allow_spinning", "0")
        options.add_session_config_entry("session.inter_op.allow_spinning", "0")
        if kwargs.get("sess_options") is not None:
            raise ValueError("Unexpected upstream ONNX session configuration")
        kwargs["sess_options"] = options
        return original(*args, **kwargs)

    rt.InferenceSession = bounded_session
    try:
        yield {
            "intra_op_num_threads": threads,
            "inter_op_num_threads": 1,
            "execution_mode": "ORT_SEQUENTIAL",
            "spinning": False,
        }
    finally:
        rt.InferenceSession = original


def _run_native(records, directory, state):
    details = state["details"]
    state["stage"] = "provider_load_failure"
    macrel, fasta_features, predict = _load_macrel()
    identity = _identity("macrel", macrel)
    details["macrel"] = identity
    distribution = importlib.metadata.distribution("macrel")
    if identity["version"] != "1.6.1":
        raise ValueError("Only the commissioned Macrel 1.6.1 bundle is supported")
    if (
        Path(macrel.__file__).resolve()
        != Path(distribution.locate_file("macrel/__init__.py")).resolve()
    ):
        raise ValueError("A source checkout shadows the installed Macrel distribution")
    root = Path(str(files("macrel")))
    details["native_source_sha256"] = {
        name: _sha256(root / name)
        for name in (
            "AMP_features.py",
            "AMP_predict.py",
            "macrel_features.py",
            "fasta.py",
        )
    }
    state["stage"] = "asset_load_failure"
    models = [root / "data/models" / name for name in ("AMP.onnx.gz", "Hemo.onnx.gz")]
    details["assets"] = {
        path.name: {"path": str(path), "sha256": _sha256(path)} for path in models
    }
    state["stage"] = "molecular_transport_failure"
    msm = _load_molsysmt()
    details["molsysmt"] = _identity("molsysmt", msm)
    transport = _write_transport(msm, records, directory)
    details["transport_sha256"] = _sha256(transport)
    state["stage"] = "feature_failure"
    features = fasta_features(str(transport))
    details["native_features"] = _frame(features)
    state["stage"] = "prediction_failure"
    with _onnx_threads(state.get("intra_op_threads")) as configuration:
        prediction = predict(
            str(models[0]), str(models[1]), features, keep_negatives=True
        )
    details["native_configuration"] = configuration
    state["stage"] = "native_output_failure"
    detached = _frame(prediction)
    details["native_predictions"] = detached
    details["runtime"] = {
        name: importlib.metadata.version(name)
        for name in (
            "numpy",
            "pandas",
            "onnxruntime",
            "biopython",
            "depdigest",
            "smonitor",
        )
    }
    details["python"] = sys.version
    details["executable"] = sys.executable
    details["cpu_provider"] = "CPUExecutionProvider"
    return {
        "bundle_id": "macrel-1.6.1:" + ":".join(_sha256(path) for path in models),
        "rows": [
            {
                "token": token,
                "values": dict(zip(detached["columns"], values, strict=True)),
            }
            for token, values in zip(detached["index"], detached["values"], strict=True)
        ],
        "details": details,
    }


def main():
    request_path, response_path = map(Path, sys.argv[1:])
    request = decode(json.loads(request_path.read_text(encoding="utf-8")))
    state = {"stage": "resource_limit_failure", "details": {}}
    try:
        _configure_process(request, state)
        response = _run_native(request["records"], request_path.parent, state)
    except Exception as error:
        response = {
            "failure": (
                "unavailable_dependency"
                if isinstance(error, RequiredDependencyError)
                else state["stage"]
            ),
            "cause_type": type(error).__name__,
            # Returned evidence, never interpolated into diagnostic events.
            "cause_message": str(error),
            "details": state["details"],
        }
    response.setdefault("details", {})["resource_usage"] = _resource_usage()
    response_path.write_text(json.dumps(encode(freeze(response))), encoding="utf-8")
