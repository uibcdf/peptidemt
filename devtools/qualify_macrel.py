"""Opt-in, bounded W3 evidence runner; default operation only prints the plan.

Native reference calls invoke upstream functions directly. Shared consumer
helpers serialize with MolSysMT and detach tables; no feature/scoring formula
is implemented here. Models and raw training data never enter the repository.
"""

import argparse
import hashlib
import json
import logging
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

PRIMARY = "FLPVLAGLTPSIVPKLVCLLTKKC"
SECONDARY = "HGRHVTLKDIVLDLQPPDPVGLHCYEQLVDSSEDEVDEVDGQDSQPLKQHFQIVTC"
LIMITS = dict(
    max_records=32,
    max_input_bytes=8192,
    wall_seconds=120,
    memory_bytes=4 * 1024**3,
    intra_op_threads=2,
    blas_threads=1,
    cpu_ids=(0, 1),
    nice=10,
    min_available_memory_bytes=8 * 1024**3,
)
ASSETS = {
    "AMP.onnx.gz": "0a674ef6f774c26e6d2f80d550df3fc54973ae05bfeee1b9dfd905e027a4a388",
    "Hemo.onnx.gz": "6c68af240d43f6fde2eff64645f7f5cedf215b619e510b75c47b257b0713e8b1",
}


def boundary_sequence(length):
    return (PRIMARY * ((length + len(PRIMARY) - 1) // len(PRIMARY)))[:length]


def plan():
    return {
        "status": "not-executed",
        "limits": LIMITS,
        "max_live_calls": 4,
        "max_total_wall_seconds": 480,
        "retries": 0,
        "fixtures": [PRIMARY, SECONDARY, "AA", "F"],
        "length_probes": [99, 100, 109, 110],
        "source": "Macrel 1.6.1 upstream code-test fixtures; generated boundary probes",
        "requires": "explicit host-envelope authorization and verified isolated environment",
    }


def write_data(path, value):
    from peptidemt._data import encode, freeze

    path.write_text(json.dumps(encode(freeze(value)), indent=2), encoding="utf-8")


def read_data(path):
    from peptidemt._data import decode

    return decode(json.loads(path.read_text(encoding="utf-8")))


def direct_native(request_path, response_path):
    """One fresh-process upstream call with real ONNX sessions observed."""
    request = json.loads(request_path.read_text())
    response = {"sessions": [], "warnings": []}
    from peptidemt._macrel_worker import _configure_process, _resource_usage

    state = {"details": {}}
    try:
        _configure_process(LIMITS, state)
        import importlib.metadata as metadata
        from importlib.resources import files

        import macrel
        import molsysmt
        import onnxruntime
        from macrel.AMP_features import fasta_features
        from macrel.AMP_predict import predict

        from peptidemt._macrel_worker import _frame, _identity, _write_transport

        distribution = metadata.distribution("macrel")
        assert distribution.version == "1.6.1"
        assert (
            Path(macrel.__file__).resolve()
            == Path(distribution.locate_file("macrel/__init__.py")).resolve()
        )
        root = Path(str(files("macrel")))
        models = [root / "data/models" / name for name in ASSETS]
        assert {
            p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in models
        } == ASSETS
        response["identities"] = {
            "macrel": _identity("macrel", macrel),
            "molsysmt": _identity("molsysmt", molsysmt),
            "onnxruntime": _identity("onnxruntime", onnxruntime),
        }

        class Warnings(logging.Handler):
            def emit(self, record):
                response["warnings"].append(
                    {"level": record.levelname, "message": record.getMessage()}
                )

        logging.getLogger("macrel").addHandler(Warnings())
        original_session = onnxruntime.InferenceSession

        class ObservedSession:
            def __init__(self, model, **kwargs):
                options = onnxruntime.SessionOptions()
                options.intra_op_num_threads = LIMITS["intra_op_threads"]
                options.inter_op_num_threads = 1
                options.execution_mode = onnxruntime.ExecutionMode.ORT_SEQUENTIAL
                options.add_session_config_entry("session.intra_op.allow_spinning", "0")
                options.add_session_config_entry("session.inter_op.allow_spinning", "0")
                kwargs["sess_options"] = options
                self.native = original_session(model, **kwargs)
                self.evidence = {
                    "model_bytes_sha256": hashlib.sha256(model).hexdigest(),
                    "providers": self.native.get_providers(),
                    "runs": [],
                    "intra_op_threads": self.native.get_session_options().intra_op_num_threads,
                    "inter_op_threads": self.native.get_session_options().inter_op_num_threads,
                    "spinning": self.native.get_session_options().get_session_config_entry(
                        "session.intra_op.allow_spinning"
                    ),
                }
                response["sessions"].append(self.evidence)

            def run(self, outputs, feeds):
                result = self.native.run(outputs, feeds)
                self.evidence["runs"].append(
                    {
                        "outputs": outputs,
                        "inputs": {
                            name: {
                                "shape": list(value.shape),
                                "dtype": str(value.dtype),
                            }
                            for name, value in feeds.items()
                        },
                    }
                )
                return result

        onnxruntime.InferenceSession = ObservedSession
        records = [(r["token"], r["sequence"]) for r in request["records"]]
        assert len(records) <= LIMITS["max_records"]
        assert (
            sum(len(t.encode()) + len(s.encode()) for t, s in records)
            <= LIMITS["max_input_bytes"]
        )
        transport = _write_transport(molsysmt, records, request_path.parent)
        features = fasta_features(str(transport))
        predictions = predict(
            str(models[0]), str(models[1]), features, keep_negatives=True
        )
        response["features"] = _frame(features)
        response["predictions"] = _frame(predictions)
        assert len(response["sessions"]) == 2 and all(
            s["runs"] and s["providers"] == ["CPUExecutionProvider"]
            for s in response["sessions"]
        )
    except Exception as error:
        response["failure"] = {"type": type(error).__name__, "message": str(error)}
    response["resource_controls"] = state["details"].get("resource_controls")
    response["resource_usage"] = _resource_usage()
    write_data(response_path, response)


def run_qualification(args):
    from dataclasses import replace

    from peptidemt import (
        MacrelLimits,
        ResultSet,
        SequenceRecord,
        assess_macrel,
        prepare_sequences,
        select,
    )
    from peptidemt._data import encode, freeze
    from peptidemt.macrel import _available_memory_bytes, _worker_environment

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    adapter_work = output / "adapter-work"
    adapter_work.mkdir()
    limits = MacrelLimits(**LIMITS, temporary_root=str(adapter_work))
    receipt = {
        "schema": "peptidemt.macrel_qualification@1",
        "plan": plan(),
        "authorization_reference": args.authorization_reference,
        "status": "incomplete",
        "calls": [],
        "gates": {},
        "python": sys.version,
        "executable": sys.executable,
    }

    def same(left, right):
        return encode(freeze(left)) == encode(freeze(right))

    def call(name, function):
        assert len(receipt["calls"]) < 4
        available = _available_memory_bytes()
        assert available >= LIMITS["min_available_memory_bytes"], (
            "Insufficient current host memory headroom"
        )
        usage = subprocess.run(
            ["du", "-sk", str(Path(sys.prefix).parent)],
            capture_output=True,
            text=True,
            check=True,
        )
        storage_bytes = int(usage.stdout.split()[0]) * 1024
        assert storage_bytes <= 3 * 1024**3, (
            "Owned qualification storage budget exceeded"
        )
        assert shutil.disk_usage(output).free >= 256 * 1024**2
        started = time.monotonic()
        entry = {
            "name": name,
            "host_available_memory_bytes": available,
            "owned_storage_bytes": storage_bytes,
        }
        receipt["calls"].append(entry)
        try:
            return function()
        finally:
            entry["elapsed_seconds"] = time.monotonic() - started
            assert sum(c.get("elapsed_seconds", 0) for c in receipt["calls"]) <= 480

    def direct(name, records):
        work = output / name
        work.mkdir()
        request_path, response_path = work / "request.json", work / "native.json"
        request_path.write_text(
            json.dumps({"records": [{"token": t, "sequence": s} for t, s in records]})
        )
        with (work / "native.log").open("w") as log:
            subprocess.run(
                [
                    sys.executable,
                    "-I",
                    str(Path(__file__).resolve()),
                    "--allow-live",
                    "--authorization-reference",
                    args.authorization_reference,
                    "--native-request",
                    str(request_path),
                    "--native-response",
                    str(response_path),
                ],
                cwd=work,
                stdin=subprocess.DEVNULL,
                stdout=log,
                stderr=subprocess.STDOUT,
                timeout=120,
                check=True,
                env=_worker_environment(limits),
            )
        data = read_data(response_path)
        assert "failure" not in data, data.get("failure")
        return data

    try:
        assert sys.platform == "linux" and sys.version_info[:2] == (3, 14)
        assert set(LIMITS["cpu_ids"]) <= os.sched_getaffinity(0)
        physical_cores = [
            (
                Path(f"/sys/devices/system/cpu/cpu{cpu}/topology/physical_package_id")
                .read_text()
                .strip(),
                Path(f"/sys/devices/system/cpu/cpu{cpu}/topology/core_id")
                .read_text()
                .strip(),
            )
            for cpu in LIMITS["cpu_ids"]
        ]
        assert len(set(physical_cores)) == 2
        receipt["physical_cores"] = physical_cores
        closure = subprocess.run(
            [sys.executable, "-m", "pip", "check"],
            capture_output=True,
            text=True,
            check=False,
        )
        receipt["pip_check"] = {
            "exit_code": closure.returncode,
            "stdout": closure.stdout,
            "stderr": closure.stderr,
        }
        assert closure.returncode == 0, (
            "Dependency closure must pass before any model call"
        )
        inputs = prepare_sequences(
            [
                SequenceRecord(PRIMARY, header="same full upstream header"),
                SECONDARY,
                "AA",
                "F",
                SequenceRecord(PRIMARY, header="same full upstream header"),
                "M" + PRIMARY,
                PRIMARY + "*",
                PRIMARY.lower(),
                None,
                "",
                SequenceRecord(PRIMARY, chemistry={"n_terminal": "acetylated"}),
                "ACDX",
                "ACD*EF",
                *(boundary_sequence(length) for length in (99, 100, 109, 110)),
            ]
        )
        compatible = [
            (i.token, i.provider_sequence)
            for i in inputs
            if i.provider_sequence is not None
        ]
        reference = call(
            "direct-compatible", lambda: direct("direct-compatible", compatible)
        )
        assessed = call(
            "adapter-mixed",
            lambda: assess_macrel(inputs, snapshot_id="W3-mixed-pool", limits=limits),
        )
        (output / "adapter-original.json").write_text(assessed.to_json())
        native = reference["predictions"]
        expected_rows = [
            {
                "token": token,
                "values": dict(zip(native["columns"], values, strict=True)),
            }
            for token, values in zip(native["index"], native["values"], strict=True)
        ]
        assert not assessed.failures, dict(assessed.failures)
        assert same(
            expected_rows,
            [{"token": r.token, "values": r.values} for r in assessed.rows],
        ), "Nonidentical native predictions: no tolerance is silently introduced"
        assert same(
            reference["features"], assessed.provenance.details["native_features"]
        ), "Nonidentical native feature tables"
        receipt["gates"]["M1"] = (
            "pass: exact tables and two real observed native ONNX heads"
        )
        by_token = {r.token: r.values for r in assessed.rows}
        assert {v["is_AMP"] for v in by_token.values()} == {True, False}, (
            "M2 AMP sign coverage incomplete"
        )
        assert {v["Hemolytic"] for v in by_token.values()} == {"Hemo", "NonHemo"}, (
            "M2 Hemo sign coverage incomplete"
        )
        receipt["gates"]["M2"] = (
            "pass: actual bundle covers both signs for each head; no activity claim"
        )
        assert set(by_token) == {t for t, _ in compatible}
        assert same(by_token["input-0"], by_token["input-4"])
        receipt["gates"]["M3"] = (
            "pass: real mixed pool and duplicate/full-header occurrences; malformed mapping controls remain engine-free"
        )
        assert all(
            inputs[i].issues and inputs[i].token not in by_token for i in range(5, 13)
        )
        qualified = replace(
            assessed,
            provenance=replace(
                assessed.provenance,
                qualification_reference=str(output / "manifest.json"),
            ),
        )
        assert sum(o.eligible for o in qualified.outcomes) == len(compatible)
        receipt["gates"]["M6"] = (
            "pass: native unchanged values and labels plus existing controlled malformed/0.5/precision tests"
        )
        boundaries = call(
            "direct-length-boundaries",
            lambda: direct(
                "direct-length-boundaries",
                [(f"length-{n}", boundary_sequence(n)) for n in (99, 100, 109, 110)],
            ),
        )
        assert list(
            map(
                len,
                [
                    row[boundaries["predictions"]["columns"].index("Sequence")]
                    for row in boundaries["predictions"]["values"]
                ],
            )
        ) == [99, 100, 109, 110]
        assert boundaries["warnings"], (
            "Expected native >=110 length warning was not observed"
        )
        receipt["gates"]["M5"] = (
            "pass: upstream F/AA and direct 99/100/109/110 probes; ordinary admission stays <100; empirical applicability remains limited"
        )
        preprocessing = call(
            "direct-leading-M",
            lambda: direct(
                "direct-leading-M",
                [("original", PRIMARY), ("leading-M", "M" + PRIMARY)],
            ),
        )
        seq_col = preprocessing["predictions"]["columns"].index("Sequence")
        assert [r[seq_col] for r in preprocessing["predictions"]["values"]] == [
            PRIMARY,
            PRIMARY,
        ]
        receipt["gates"]["M4"] = (
            "pass: leading-M native clipping observed only in qualification; original adapter proposal excluded; chemistry/invalid forms retained"
        )
        restored = ResultSet.from_json(qualified.to_json())
        receipt["selections"] = {}
        assert qualified.to_json() == restored.to_json()
        for policy in ("amp-first", "hemolysis-first"):
            chosen, replay = (
                select(qualified, policy=policy, k=3),
                select(restored, policy=policy, k=3),
            )
            assert (chosen.ranking, chosen.selected, chosen.excluded) == (
                replay.ranking,
                replay.selected,
                replay.excluded,
            )
            assert not select(restored, policy=policy, k=0).selected
            receipt["selections"][policy] = {
                "selected": chosen.selected,
                "ranking": chosen.ranking,
            }
        (output / "qualified-computational.json").write_text(qualified.to_json())
        reader = "from pathlib import Path;import sys;from peptidemt import ResultSet,select;r=ResultSet.from_json(Path(sys.argv[1]).read_text());select(r,policy='amp-first',k=3);select(r,policy='hemolysis-first',k=3);assert 'macrel' not in sys.modules and 'ackredit' not in sys.modules"
        subprocess.run(
            [
                sys.executable,
                "-I",
                "-c",
                reader,
                str(output / "qualified-computational.json"),
            ],
            cwd=output,
            timeout=10,
            check=True,
        )
        receipt["gates"]["M7"] = (
            "pass: unchanged live evaluations replay both policies in a fresh engine-free reader; invented contrasting fixture retained separately"
        )
        for pool in ([], ["MACD", ""]):
            empty = assess_macrel(
                prepare_sequences(pool),
                snapshot_id="W3-no-execution",
                limits=limits,
            )
            assert not empty.rows and empty.provenance.details["execution"].startswith(
                "not-requested"
            )
        receipt["gates"]["M8"] = (
            "pass: real empty/incompatible pools start no provider; absence/load/corruption/interruption controls remain separately engine-free"
        )
        receipt["status"] = (
            "computational-qualification-evidence-complete; investigator-acceptance-pending"
        )
    except Exception as error:
        receipt["failure"] = {"type": type(error).__name__, "message": str(error)}
    finally:
        write_data(output / "manifest.json", receipt)
    print(
        json.dumps(
            {
                "status": receipt["status"],
                "live_calls": len(receipt["calls"]),
                "output": str(output),
                "failure": receipt.get("failure"),
            }
        )
    )
    return 0 if "failure" not in receipt else 1


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--allow-live", action="store_true")
    parser.add_argument("--authorization-reference")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--native-request", type=Path, help=argparse.SUPPRESS)
    parser.add_argument("--native-response", type=Path, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    if not args.allow_live:
        print(json.dumps(plan(), indent=2))
        return 0
    if not args.authorization_reference:
        parser.error(
            "--allow-live requires the actual host-envelope authorization reference"
        )
    if args.native_request:
        if args.native_response is None:
            parser.error("The private native invocation requires a response path")
        direct_native(args.native_request, args.native_response)
        return 0
    if args.output is None:
        parser.error("--allow-live requires a new --output directory")
    return run_qualification(args)


if __name__ == "__main__":
    raise SystemExit(main())
