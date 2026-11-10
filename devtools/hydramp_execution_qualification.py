"""One reviewed installed-adapter case; preflight never imports a model."""

import argparse
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def preflight(plan):
    if plan.get("schema") != "peptidemt.hydramp_execution_adapter_plan@1":
        raise ValueError("Unsupported qualification plan")
    if plan.get("request") != {
        "n_target": 16,
        "seed": 1001,
        "snapshot_id": "installed-HydrAMP-seed-1001",
        "qualification_reference": None,
    }:
        raise ValueError("Expected the exact single receiving case")
    expected = {
        "public_generation_calls": 1,
        "numeric_PCA_loads": 1,
        "checkpoint_loads": 1,
        "PCA_inverse_transforms": 1,
        "decoder_forwards": 1,
        "AMP_forwards": 1,
        "MIC_forwards": 1,
        "descriptor_bundles": 1,
        "neural_forwards_total": 3,
        "proposals": 16,
        "Macrel_calls": 0,
        "legacy_calls": 0,
        "retries": 0,
    }
    if plan.get("call_budget") != expected:
        raise ValueError("Expected the exact approved call budget")
    for path, expected_digest in plan["pinned_files"].items():
        if sha256(path) != expected_digest:
            raise ValueError("Pinned candidate changed: " + path)
    probe = (
        "import sys,json,importlib.metadata as m;"
        "names={d.metadata['Name'].lower().replace('_','-') for d in m.distributions()};"
        "print(json.dumps({'python_version':sys.version,'versions':{n:m.version(n) for n in sorted(names)}}))"
    )
    for python, expected in plan["runtime_profiles"].items():
        observed = json.loads(
            subprocess.check_output(
                [python, "-B", "-I", "-c", probe],
                text=True,
                timeout=20,
            )
        )
        if observed != expected:
            raise ValueError("Pinned interpreter/runtime inventory changed: " + python)
    return {"files_hashed": len(plan["pinned_files"]), "model_or_PCA_loads": 0}


def authorized(plan, digest):
    data = json.loads((Path(plan["work_dir"]) / "authorization.json").read_text())
    if data.get("plan_sha256") != digest or not data.get("investigator_reference"):
        raise ValueError("Exact fresh investigator execution approval required")


def configure_parent(plan):
    """Enforce the parent soft ceiling without lowering the child's hard cap."""
    import resource

    from peptidemt._hydramp_process import configure_child

    parent_soft = plan["resources"]["parent_address_space_bytes"]
    child_hard = plan["limits"]["address_space_bytes"]
    if not 0 < parent_soft <= child_hard:
        raise ValueError("Parent address-space ceiling must fit the worker hard cap")
    configure_child(plan["limits"], os.getppid())
    resource.setrlimit(resource.RLIMIT_AS, (parent_soft, child_hard))


def case(plan, digest):
    authorized(plan, digest)
    from peptidemt import HydrAMPBundle, HydrAMPLimits, HydrAMPReceipt, generate_hydramp

    configure_parent(plan)

    def audit(event, args):
        if event == "socket.connect":
            raise RuntimeError("Network prohibited during qualification")

    sys.addaudithook(audit)
    directory = Path(plan["work_dir"])
    with (directory / "model-attempt.json").open("x") as file:
        json.dump({"plan_sha256": digest, "attempted": True, "retry": False}, file)
    import ackredit

    with ackredit.session("installed-HydrAMP-qualification"):
        with ackredit.capture("enclosing-qualification") as enclosing:
            result = generate_hydramp(
                **plan["request"],
                bundle=HydrAMPBundle(**plan["bundle"]),
                limits=HydrAMPLimits(
                    **{**plan["limits"], "cpu_ids": tuple(plan["limits"]["cpu_ids"])}
                ),
                worker_python=plan["worker_python"],
            )
        (directory / "parent-attribution.json").write_text(
            json.dumps(enclosing.attribution.to_dict(), indent=2) + "\n"
        )
    (directory / "receipt.json").write_text(result.to_json() + "\n")
    reference = HydrAMPReceipt.from_json(
        Path(plan["comparison"]["retained_native_receipt"]).read_text()
    )
    replay = HydrAMPReceipt.from_json(result.to_json())
    attribution = result.provenance.details["scientific_attribution"]
    observations = {
        "completed": result.completed,
        "failures": list(result.failures),
        "receiving_issues": list(result.issues),
        "returned": len(result.native_results),
        "native_results_exact": result.native_results == reference.native_results,
        "returned_indices_exact": result.returned_input_indices
        == reference.returned_input_indices,
        "original_trace_exact": result.original_trace == reference.original_trace,
        "saved_roundtrip_exact": replay.to_json() == result.to_json(),
        "attribution_status": attribution["status"],
        "bibliography_records": len(attribution["bibliography"]),
        "confirmed_operations": list(
            result.provenance.details.get("state", {}).get("completed", ())
        ),
        "scientific_acceptance": False,
    }
    (directory / "observations.json").write_text(
        json.dumps(observations, indent=2) + "\n"
    )
    return observations


def run(plan_path, plan, digest):
    authorized(plan, digest)
    from peptidemt import HydrAMPLimits
    from peptidemt._hydramp_process import supervise

    directory = Path(plan["work_dir"])
    with (directory / "attempt.json").open("x") as file:
        json.dump({"plan_sha256": digest, "retry": False}, file)
    limits = HydrAMPLimits(
        **{
            **plan["limits"],
            "cpu_ids": tuple(plan["limits"]["cpu_ids"]),
            "wall_seconds": plan["resources"]["overall_case_wall_seconds"],
        }
    )
    result = supervise(
        [
            plan["parent_python"],
            "-B",
            "-I",
            str(Path(__file__).resolve()),
            "_case",
            "--plan",
            str(Path(plan_path).resolve()),
            "--approved-plan-sha256",
            digest,
        ],
        directory,
        limits,
    )
    (directory / "execution.json").write_text(json.dumps(result, indent=2) + "\n")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("preflight", "run", "_case"))
    parser.add_argument("--plan", required=True)
    parser.add_argument("--approved-plan-sha256")
    args = parser.parse_args()
    plan = json.loads(Path(args.plan).read_text())
    result = preflight(plan)
    if args.action != "preflight":
        digest = sha256(args.plan)
        if args.approved_plan_sha256 != digest:
            parser.error("Exact approved plan digest required before execution")
        result = (
            case(plan, digest)
            if args.action == "_case"
            else run(args.plan, plan, digest)
        )
    print(json.dumps(result, indent=2))
    return exit_code(result)


def exit_code(result):
    """Process success is not model success; retain observations on failure."""
    if "completed" in result:
        return int(
            not result["completed"]
            or bool(result.get("failures"))
            or bool(result.get("receiving_issues"))
            or not result.get("saved_roundtrip_exact", False)
            or result.get("attribution_status") != "captured"
        )
    return int(bool(result.get("failure")) or result.get("returncode", 0) != 0)


if __name__ == "__main__":
    sys.exit(main())
