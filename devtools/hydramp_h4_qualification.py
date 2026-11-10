"""Prepared two-worker HydrAMP receiving qualification; never auto-authorized.

Only preflight is model-free. Both execution entrypoints require a separately
recorded investigator approval of the exact plan. No package/public API claim.
"""

import argparse
import hashlib
import importlib.metadata
import importlib.util
import json
import os
import resource
import shutil
import signal
import stat
import subprocess
import sys
import time
from pathlib import Path
from types import SimpleNamespace

STAGES = ("generation", "assessment")
REQUESTS = ((1001, 16), (1002, 16))


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def validate(plan):
    if plan.get("schema") != "peptidemt.hydramp_h4_plan@1":
        raise ValueError("Unsupported H4 qualification plan")
    if plan.get("requests") != [
        {"seed": seed, "count": count} for seed, count in REQUESTS
    ]:
        raise ValueError("Expected the two fixed sixteen-row receiving requests")
    expected = {
        "generation_calls": 2,
        "decoder_forwards": 2,
        "amp_forwards": 2,
        "mic_forwards": 2,
        "descriptor_bundles": 2,
        "pca_numeric_loads": 1,
        "pca_inverse_transforms": 2,
        "macrel_calls": 3,
        "macrel_proposed_records_max": 36,
        "onnx_head_executions_max": 6,
        "retries": 0,
    }
    if any(plan.get("call_budget", {}).get(k) != v for k, v in expected.items()):
        raise ValueError("Expected the exact receiving call budget")
    if len(plan.get("control_sequences", [])) != 4:
        raise ValueError("Expected the four frozen W3 computational controls")


def preflight(plan):
    """Read bytes only; no installed scientific provider import/parameter load."""
    validate(plan)
    for path, expected in plan["pinned_files"].items():
        if digest(path) != expected:
            raise ValueError("Pinned qualification source/input changed: " + path)
    return {"files_hashed": len(plan["pinned_files"]), "model_weight_pca_loads": 0}


def authorized(plan, sha):
    approval = json.loads((Path(plan["work_dir"]) / "authorization.json").read_text())
    if approval.get("plan_sha256") != sha or not approval.get("investigator_reference"):
        raise ValueError("Exact fresh investigator approval is required")


class Ledger:
    def __init__(self, path, limits):
        self.path, self.limits, self.attempted, self.completed = (
            Path(path),
            limits,
            {},
            {},
        )
        with self.path.open("x") as file:
            json.dump({"attempted": {}, "completed": {}}, file)

    def save(self):
        self.path.write_text(
            json.dumps(
                {"attempted": self.attempted, "completed": self.completed}, indent=2
            )
            + "\n"
        )

    def reserve(self, key):
        if self.attempted.get(key, 0) >= self.limits[key]:
            raise RuntimeError("Call budget exhausted before " + key)
        self.attempted[key] = self.attempted.get(key, 0) + 1
        self.save()

    def done(self, key):
        self.completed[key] = self.completed.get(key, 0) + 1
        self.save()


def generation_worker(plan, directory):
    import numpy as np
    import torch
    from hydramp_torch import (
        HydrAMPGenerator,
        Modlamp433Properties,
        PCAProjection,
        load_checkpoint,
    )

    if (
        torch.version.cuda is not None
        or torch.__version__ != plan["torch_version"]
        or torch.get_num_threads() != 1
    ):
        raise ValueError("Expected the unchanged single-thread CPU Torch profile")
    ledger = Ledger(
        directory / "calls.json",
        {"generation": 2, "decoder": 2, "paired_heads": 2, "pca": 2, "properties": 2},
    )
    native_properties = Modlamp433Properties()

    class Properties:
        def prepare(self):
            native_properties.prepare()

        def __call__(self, sequences):
            ledger.reserve("properties")
            result = native_properties(sequences)
            ledger.done("properties")
            return result

    native_properties.prepare()
    with np.load(plan["numeric_pca"], allow_pickle=False) as archive:
        projection = PCAProjection(
            archive["components"],
            archive["mean"],
            whiten=bool(archive["whiten"]),
            explained_variance=archive["explained_variance"],
        )
    model = load_checkpoint(plan["checkpoint_root"], plan["checkpoint_hashes"])
    captured = {}

    def tap(obj, name, key):
        original = getattr(obj, name)

        def call(values):
            ledger.reserve(key)
            result = original(values)
            if key == "decoder":
                captured["decoder_input"] = values.numpy().copy()
            elif key == "pca":
                captured["pca_projected"] = np.array(result, copy=True)
            ledger.done(key)
            return result

        setattr(obj, name, call)

    tap(model, "decode_conditioned", "decoder")
    tap(model, "score_tokens", "paired_heads")
    tap(projection, "inverse_transform", "pca")
    generator = HydrAMPGenerator(model, projection, property_provider=Properties())
    reference = json.loads(Path(plan["cached_native_json"]).read_text())
    cases = []
    for request in plan["requests"]:
        ledger.reserve("generation")
        trace = generator.generate_with_trace(
            mode="amp",
            n_target=request["count"],
            seed=request["seed"],
            filter_out=False,
            properties=True,
            n_attempts=1,
        )
        ledger.done("generation")
        arrays = {
            name: getattr(trace, name)
            for name in ("sampled_latents", "conditioned", "tokens", "amp", "mic")
        }
        arrays.update(captured)
        payload = {
            "request": request,
            "seed": trace.seed,
            "native_results": trace.native_results,
            "returned_input_indices": trace.returned_input_indices,
            "sequences": trace.sequences,
            "arrays": {
                name: {"dtype": str(a.dtype), "values": a.tolist()}
                for name, a in arrays.items()
            },
        }
        tag = "seed_" + str(request["seed"])
        old = next(
            case for case in reference["phases"] if case["request"]["tag"] == tag
        )
        # Reproducibility observation, not an automatic legacy-equality gate.
        payload["cached_same_provider_return_exact"] = (
            list(trace.native_results) == old["rows"]
        )
        path = directory / (tag + ".json")
        path.write_text(json.dumps(payload, allow_nan=False) + "\n")
        cases.append(
            {
                "tag": tag,
                "rows": len(trace.native_results),
                "path": str(path),
                "sha256": digest(path),
                "cached_same_provider_return_exact": payload[
                    "cached_same_provider_return_exact"
                ],
            }
        )
    return {
        "cases": cases,
        "network_forwards": ledger.completed.get("decoder", 0)
        + 2 * ledger.completed.get("paired_heads", 0),
        "scientific_acceptance": False,
    }


def receive_payload(payload, receipt_type, provenance):
    """Data-only bridge; preserve numeric dtype and original provider order."""
    import numpy as np

    arrays = {}
    for name, value in payload["arrays"].items():
        if value["dtype"] not in ("float32", "float64", "int64", "int32"):
            raise ValueError("Unexpected retained trace dtype")
        arrays[name] = np.asarray(value["values"], dtype=value["dtype"])
    trace = SimpleNamespace(
        seed=payload["seed"],
        native_results=payload["native_results"],
        returned_input_indices=payload["returned_input_indices"],
        sequences=tuple(payload["sequences"]),
        **{
            k: v
            for k, v in arrays.items()
            if k in ("sampled_latents", "conditioned", "tokens", "amp", "mic")
        },
    )
    receipt = receipt_type.from_trace(
        trace,
        snapshot_id="H4-seed-" + str(trace.seed),
        requested_count=payload["request"]["count"],
        provenance=provenance,
    )
    from dataclasses import replace

    extra = {name: arrays[name].tolist() for name in ("decoder_input", "pca_projected")}
    return replace(receipt, original_trace={**receipt.original_trace, **extra})


def generation_provenance_details(plan, case):
    versions = {
        d["name"].lower().replace("_", "-"): d["version"]
        for d in plan["generation_profile"]["inventory"]
    }
    return {
        "source_commit": plan["hydramp_source_commit"],
        "starter_commit": plan["starter_commit"],
        "port_implementation": "uibcdf/hydramp native PyTorch inference",
        "payload_sha256": case["sha256"],
        "qualification_plan_sha256": plan["executing_plan_sha256"],
        "checkpoint_manifest_sha256": hashlib.sha256(
            json.dumps(plan["checkpoint_hashes"], sort_keys=True).encode()
        ).hexdigest(),
        "numeric_pca_sha256": plan["pinned_files"][plan["numeric_pca"]],
        "receiving_source_sha256": plan["pinned_files"][plan["receiving_source"]],
        "runtime_versions": {
            name: versions[name]
            for name in ("hydramp-torch", "torch", "numpy", "modlamp")
        },
        "python_version": plan["generation_profile"]["python_version"],
        "descriptor_profile": {
            "provider": "modlamp 4.3.3",
            "hydrophobicity": "Eisenberg",
            "hydrophobic_moment": {
                "window": 1000,
                "angle_degrees": 100,
                "modality": "max",
            },
            "charge": {"pH": 7, "amide": True},
            "isoelectric_point": {"amide": False},
        },
        "native_score_meaning": {
            "amp": "native AMP classifier output",
            "mic": "native low-MIC compatibility; not concentration or hemolysis",
        },
        "chemical_resolution": "Sequence view only; native descriptor conventions do not establish molecular termini/stereochemistry",
        "use_scope": "Same investigator-approved local research; no redistribution rights inferred",
        "cached_same_provider_return_exact": case["cached_same_provider_return_exact"],
        "scientific_acceptance": False,
    }


def assessment_worker(plan, directory):
    from peptidemt import MacrelLimits, Provenance, ResultSet, prepare_sequences, select
    from peptidemt._data import encode, freeze

    # Extend only this process with the new private module. Keep the accepted
    # installed Macrel/core worker and all existing scientific environments intact.
    spec = importlib.util.spec_from_file_location(
        "peptidemt._hydramp_receiving", plan["receiving_source"]
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    from peptidemt import assess_macrel

    generation = json.loads(
        (Path(plan["work_dir"]) / "generation/result.json").read_text()
    )
    ledger = Ledger(directory / "calls.json", {"macrel": 3})
    pools = [("control", prepare_sequences(plan["control_sequences"]))]
    for case in generation["cases"]:
        if digest(case["path"]) != case["sha256"]:
            raise ValueError("New generation payload changed")
        payload = json.loads(Path(case["path"]).read_text())
        provenance = Provenance(
            "hydramp-torch",
            "wheel:" + plan["torch_wheel_sha256"],
            "native",
            details=generation_provenance_details(plan, case),
        )
        receipt = receive_payload(payload, module.HydrAMPReceipt, provenance)
        (directory / (case["tag"] + "-generation.json")).write_text(
            receipt.to_json() + "\n"
        )
        if receipt.issues:
            raise ValueError(
                "Generation receiving issues; raw receipt retained: "
                + str(receipt.issues)
            )
        if (
            module.HydrAMPReceipt.from_json(receipt.to_json()).to_json()
            != receipt.to_json()
        ):
            raise ValueError("Generation receipt roundtrip changed data")
        pools.append((case["tag"], receipt.inputs))
    observations, proposed = [], 0
    for tag, inputs in pools:
        proposed += len(inputs)
        if proposed > 36:
            raise ValueError("Proposed record budget exceeded before assessment")
        ledger.reserve("macrel")
        result = assess_macrel(
            inputs,
            snapshot_id="H4-" + tag,
            limits=MacrelLimits(
                **{
                    **plan["macrel_limits"],
                    "cpu_ids": tuple(plan["macrel_limits"]["cpu_ids"]),
                    "temporary_root": str(directory),
                }
            ),
            qualification_reference=plan["macrel_qualification_reference"],
        )
        ledger.done("macrel")
        (directory / (tag + "-assessment.json")).write_text(result.to_json() + "\n")
        eligible = check_assessment_result(result)
        selections = {
            policy: select(result, policy=policy, k=4)
            for policy in ("amp-first", "hemolysis-first")
        }
        replay = ResultSet.from_json(result.to_json())
        if any(
            select(replay, policy=policy, k=4) != selection
            for policy, selection in selections.items()
        ):
            raise ValueError("Saved result selection changed")
        if tag == "control":
            expected = plan["control_native_values"]
            for row in result.rows:
                if encode(freeze(dict(row.values))) != encode(
                    freeze(expected[row.values["Sequence"]])
                ):
                    raise ValueError(
                        "Predeclared native control differs; preserve and review before further calls"
                    )
        observations.append(
            {
                "tag": tag,
                "proposed": len(inputs),
                "eligible": len(eligible),
                "excluded": [
                    [o.token, list(o.issues)] for o in result.outcomes if o.issues
                ],
                "selected": {p: list(s.selected) for p, s in selections.items()},
                "ranking": {p: list(s.ranking) for p, s in selections.items()},
                "replay_exact": True,
            }
        )
    return {
        "pools": observations,
        "macrel_calls": ledger.completed["macrel"],
        "proposed_records": proposed,
        "scientific_acceptance": False,
        "scope": "Source-extension receiving plus accepted installed Macrel composition. Not a public API/release, biological efficacy or investigator H0-H4 acceptance.",
    }


def check_assessment_result(result):
    """Keep declared incompatible inputs; reject missing/bad compatible rows."""
    if result.failures or result.anomalies:
        raise ValueError("Macrel failure/anomaly retained; no retry or later call")
    outcomes = result.outcomes
    if any(
        not item.issues and not outcome.eligible
        for item, outcome in zip(result.inputs, outcomes)
    ):
        raise ValueError("Compatible input lacks an eligible native result")
    eligible = [outcome for outcome in outcomes if outcome.eligible]
    if not eligible:
        raise ValueError("No usable Macrel outputs; qualification cannot pass")
    return eligible


def worker(plan, stage, sha):
    authorized(plan, sha)
    plan = {**plan, "executing_plan_sha256": sha}
    expected = plan[stage + "_profile"]
    if (
        Path(sys.prefix) != Path(expected["prefix"])
        or sys.version != expected["python_version"]
    ):
        raise ValueError("Exact scientific worker Python/prefix changed")
    actual = {
        d.metadata["Name"].lower().replace("_", "-"): d.version
        for d in importlib.metadata.distributions(
            path=[p for p in sys.path if p.endswith("site-packages")]
        )
    }
    if actual != {
        d["name"].lower().replace("_", "-"): d["version"] for d in expected["inventory"]
    }:
        raise ValueError("Exact scientific worker inventory changed")

    def audit(event, args):
        if event == "socket.connect":
            raise RuntimeError("Network prohibited during qualification")

    sys.addaudithook(audit)
    directory = Path(plan["work_dir"]) / stage
    directory.mkdir()  # Exclusive stage, no repeated scientific execution.
    result = (
        generation_worker(plan, directory)
        if stage == "generation"
        else assessment_worker(plan, directory)
    )
    (directory / "result.json").write_text(json.dumps(result, indent=2) + "\n")
    return result


def available():
    return next(
        int(line.split()[1]) * 1024
        for line in Path("/proc/meminfo").read_text().splitlines()
        if line.startswith("MemAvailable:")
    )


def process_tree(pid):
    pids, todo = set(), [pid]
    while todo:
        current = todo.pop()
        if current in pids:
            continue
        pids.add(current)
        try:
            todo.extend(
                int(p)
                for p in Path(f"/proc/{current}/task/{current}/children")
                .read_text()
                .split()
            )
        except (FileNotFoundError, ProcessLookupError):
            pass
    return pids


def tree_rss(pid):
    total = 0
    for current in process_tree(pid):
        try:
            total += next(
                int(s.split()[1]) * 1024
                for s in Path(f"/proc/{current}/status").read_text().splitlines()
                if s.startswith("VmRSS:")
            )
        except (FileNotFoundError, ProcessLookupError, StopIteration):
            pass
    return total


def output_size(directory):
    total = 0
    for path in directory.rglob("*"):
        try:
            details = path.stat()
        except FileNotFoundError:
            continue  # Native transport temporary files may disappear mid-sample.
        if stat.S_ISREG(details.st_mode):
            total += details.st_size
    return total


def run_stage(plan_path, stage, sha):
    plan = json.loads(Path(plan_path).read_text())
    preflight(plan)
    if digest(plan_path) != sha:
        raise ValueError("Reviewed plan bytes differ")
    authorized(plan, sha)
    work = Path(plan["work_dir"])
    if stage == "assessment":
        prior = json.loads((work / "attempt-generation.json").read_text())
        if prior.get("exit_code") != 0:
            raise ValueError("Generation did not complete; no assessment")
    limits = plan["resource_limits"]
    if (
        available() < limits["minimum_available_bytes"]
        or shutil.disk_usage(work).free < limits["minimum_free_disk_bytes"]
    ):
        raise RuntimeError("Host resource floor not met; no stage started")
    attempt = work / ("attempt-" + stage + ".json")
    with attempt.open("x") as file:
        json.dump({"started": True, "retry": False, "plan_sha256": sha}, file)
    env = os.environ.copy()
    env.update(
        CUDA_VISIBLE_DEVICES="-1",
        OMP_NUM_THREADS="1",
        OPENBLAS_NUM_THREADS="1",
        MKL_NUM_THREADS="1",
        PYTHONDONTWRITEBYTECODE="1",
        TMPDIR=str(work / "tmp"),
        MPLCONFIGDIR=str(work / "mpl"),
        TORCH_HOME=str(work / "torch-cache"),
    )
    for name in ("tmp", "mpl", "torch-cache"):
        (work / name).mkdir(exist_ok=True)

    def child_limits():
        os.sched_setaffinity(0, {0, 1})
        os.nice(10)
        resource.setrlimit(
            resource.RLIMIT_AS, (limits["worker_address_space_bytes"],) * 2
        )

    start, peak, stop = time.monotonic(), 0, None
    with (work / "logs" / (stage + ".log")).open("x") as log:
        child = subprocess.Popen(
            [
                plan[stage + "_profile"]["python"],
                "-B",
                "-I",
                str(Path(__file__).resolve()),
                "_worker",
                "--plan",
                str(Path(plan_path).resolve()),
                "--stage",
                stage,
                "--approved-plan-sha256",
                sha,
            ],
            cwd=work,
            env=env,
            stdin=subprocess.DEVNULL,
            stdout=log,
            stderr=subprocess.STDOUT,
            start_new_session=True,
            preexec_fn=child_limits,
        )
        previous_term = signal.getsignal(signal.SIGTERM)

        def terminate(signum, frame):
            raise KeyboardInterrupt("Qualification controller terminated")

        signal.signal(signal.SIGTERM, terminate)
        try:
            while child.poll() is None:
                peak = max(peak, tree_rss(child.pid))
                if time.monotonic() - start > limits[stage + "_wall_seconds"]:
                    stop = "stage wall limit"
                elif peak > limits["tree_rss_stop_bytes"]:
                    stop = "sampled process-tree RSS limit"
                elif available() < limits["minimum_available_bytes"]:
                    stop = "shared-host available memory floor"
                elif output_size(work) > limits["output_stop_bytes"]:
                    stop = "output size limit"
                if stop:
                    break
                time.sleep(0.1)
        except BaseException as error:
            stop = "controller exception:" + type(error).__name__
        finally:
            # Clean the owned group even if its leader exited unexpectedly while
            # the native Macrel child was still running. Qualified children do
            # not escape this newly created process group.
            try:
                os.killpg(child.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            code = child.wait()
            signal.signal(signal.SIGTERM, previous_term)
    result = {
        "exit_code": code,
        "stop_reason": stop,
        "wall_seconds": time.monotonic() - start,
        "peak_sampled_process_tree_rss_bytes": peak,
        "controller_hwm_rss_bytes": next(
            int(s.split()[1]) * 1024
            for s in Path("/proc/self/status").read_text().splitlines()
            if s.startswith("VmHWM:")
        ),
        "plan_sha256": sha,
        "retry_allowed": False,
    }
    attempt.write_text(json.dumps(result, indent=2) + "\n")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["preflight", "run-stage", "_worker"])
    parser.add_argument("--plan", required=True)
    parser.add_argument("--stage", choices=STAGES, default="generation")
    parser.add_argument("--approved-plan-sha256")
    args = parser.parse_args()
    plan = json.loads(Path(args.plan).read_text())
    preflight(plan)
    if args.action == "preflight":
        result = preflight(plan)
    else:
        if (
            not args.approved_plan_sha256
            or digest(args.plan) != args.approved_plan_sha256
        ):
            parser.error(
                "A separately approved exact plan is required before scientific execution"
            )
        result = (
            run_stage(args.plan, args.stage, args.approved_plan_sha256)
            if args.action == "run-stage"
            else worker(plan, args.stage, args.approved_plan_sha256)
        )
    print(json.dumps(result, indent=2))
    return int(result.get("exit_code", 0) != 0)


if __name__ == "__main__":
    sys.exit(main())
