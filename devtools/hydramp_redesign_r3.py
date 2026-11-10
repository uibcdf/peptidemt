"""One fixed R3 experiment; preparation never grants model-execution authority."""

import argparse
import importlib.metadata
import json
import os
from pathlib import Path
from types import SimpleNamespace


def write(path, data):
    Path(path).write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def parents_for(plan):
    from peptidemt import SequenceRecord, prepare_sequences

    return prepare_sequences([SequenceRecord(**p) for p in plan["parents"]])


def verify(plan):
    """Check frozen artifacts and both installed consumer copies without loading models."""
    from peptidemt._hydramp_process import sha256, source_manifest

    for item in plan["pins"]:
        if sha256(item["path"]) != item["sha256"]:
            raise ValueError("Changed pinned file: " + item["path"])
    for profile in plan["profiles"].values():
        if source_manifest(profile["consumer_root"]) != plan["consumer_source"]:
            raise ValueError("Changed installed consumer source")
        inventory = {
            d.metadata["Name"].lower(): d.version
            for d in importlib.metadata.distributions(
                path=[str(Path(profile["consumer_root"]).parent)]
            )
        }
        if inventory != profile["inventory"]:
            raise ValueError("Changed installed profile inventory")
    if (
        source_manifest(plan["provider_root"])
        != plan["bundle"]["provider_source_sha256"]
    ):
        raise ValueError("Changed installed provider source")
    root = Path(plan["bundle"]["checkpoint_root"])
    assets = {
        str(p.relative_to(root)): sha256(p) for p in root.rglob("*") if p.is_file()
    }
    if assets != plan["bundle"]["checkpoint_sha256"]:
        raise ValueError("Changed checkpoint inventory")


def authorize(task, plan):
    """A human reply must be recorded separately; no command creates permission."""
    from peptidemt._hydramp_process import sha256

    approval = json.loads((task / "authorization.json").read_text())
    if (
        approval.get("plan_sha256") != sha256(task / "plan.json")
        or approval.get("explicit_investigator_approval") is not True
        or not approval.get("reply_reference")
    ):
        raise ValueError("Missing exact investigator authorization")
    verify(plan)


def network_guard(plan):
    """Block network and unrelated parameter stores in each scientific process."""
    import sys

    allowed = [Path(plan["bundle"]["checkpoint_root"]).resolve()]
    allowed += [Path(plan["macrel_model_root"]).resolve()]

    def audit(event, args):
        if event in ("socket.connect", "os.system"):
            raise RuntimeError("R3 prohibits network and shell execution")
        if event == "open" and isinstance(args[0], (str, bytes)):
            p = Path(os.fsdecode(args[0])).resolve()
            if p.suffix in {".npy", ".npz", ".pkl", ".joblib", ".h5", ".hdf5", ".onnx"}:
                if not any(p.is_relative_to(root) for root in allowed):
                    raise RuntimeError("Unrelated parameter store: " + str(p))

    sys.addaudithook(audit)


def native(plan, directory):
    """Call owner APIs directly, observing and bounding the seven evaluations."""
    import hydramp_torch as provider
    import torch

    from peptidemt import HydrAMPAnalogueReceipt, Provenance

    torch.set_num_threads(1)
    torch.set_num_interop_threads(1)
    if torch.version.cuda is not None:
        raise ValueError("CPU-only Torch build required")
    for name, expected in plan["bundle"]["expected_versions"].items():
        if importlib.metadata.version(name) != expected:
            raise ValueError("Unexpected direct runtime version: " + name)
    parents = parents_for(plan)
    indices = tuple(plan["submitted_parent_indices"])
    tokens = provider.encode_sequences([parents[i].proposal.sequence for i in indices])
    if tuple(provider.translate_tokens(tokens.numpy())) != tuple(
        parents[i].proposal.sequence for i in indices
    ):
        raise ValueError("Owner codec changed a prototype")
    bundle = plan["bundle"]
    encoder = provider.load_encoder_checkpoint(
        bundle["checkpoint_root"], bundle["checkpoint_sha256"]
    )
    core = provider.load_checkpoint(
        bundle["checkpoint_root"], bundle["checkpoint_sha256"]
    )
    ledger, counts = [], {"encoder": 0, "heads": 0, "decoder": 0}

    def tap(obj, attribute, name, maximum, weight):
        original = getattr(obj, attribute)

        def call(values):
            if counts[name] >= maximum:
                raise RuntimeError("Extra direct evaluation blocked")
            counts[name] += 1
            item = {
                "operation": name,
                "rows": len(values),
                "evaluations": weight,
                "completed": False,
            }
            ledger.append(item)
            write(directory / "ledger.json", ledger)
            result = original(values)
            item["completed"] = True
            write(directory / "ledger.json", ledger)
            return result

        setattr(obj, attribute, call)

    tap(encoder, "encode_tokens", "encoder", 2, 1)
    tap(core, "score_tokens", "heads", 2, 2)
    tap(core, "decode_conditioned", "decoder", 1, 1)
    trace = provider.HydrAMPAnalogueGenerator(
        encoder, core, max_proposals=16
    ).generate_with_trace(
        tokens,
        **plan["request"],
        mode="improvement",
        properties=False,
        filtering_options=None,
    )
    if counts != {"encoder": 2, "heads": 2, "decoder": 1}:
        raise ValueError("Incomplete direct operation ledger")
    return HydrAMPAnalogueReceipt.from_trace(
        trace,
        snapshot_id="R3-direct",
        parents=parents,
        submitted_parent_indices=indices,
        provenance=Provenance(
            "hydramp-torch",
            plan["bundle_id"],
            "native",
            plan["qualification_reference"],
        ),
    )


def compare_receipts(direct, adapter, repeat):
    for receipt in (direct, adapter, repeat):
        if receipt.issues:
            raise ValueError("Unreceived analogue evidence: " + repr(receipt.issues))
    for receipt in (adapter, repeat):
        if (
            receipt.parents != direct.parents
            or receipt.submitted_parent_indices != direct.submitted_parent_indices
            or receipt.original_trace != direct.original_trace
            or receipt.links != direct.links
            or receipt.outcomes != direct.outcomes
        ):
            raise ValueError("Direct/adapter/repeat analogue correspondence differs")


def check_assessment(result):
    if result.anomalies or result.failures:
        raise ValueError("Assessment has anomalous rows or reported failures")
    for item, outcome in zip(result.inputs, result.outcomes, strict=True):
        if outcome.issues != item.issues:
            raise ValueError("Unexpected assessment outcome: " + repr(outcome))


def saved_selection(receipt, result):
    from peptidemt import HydrAMPAnalogueReceipt, ResultSet, select

    received = HydrAMPAnalogueReceipt.from_json(receipt.to_json())
    detached = ResultSet.from_json(result.to_json())
    if received.proposals() != detached.inputs:
        raise ValueError("Assessment ancestry differs from returned proposals")
    choices = {}
    for policy in ("amp-first", "hemolysis-first"):
        choice = select(result, policy=policy, k=4)
        if choice != select(detached, policy=policy, k=4):
            raise ValueError("Saved selector replay differs")
        choices[policy] = {
            field: getattr(choice, field)
            for field in (
                "snapshot_id",
                "policy",
                "requested_count",
                "ranking",
                "selected",
                "unselected",
                "excluded",
            )
        }
    return choices


def stage(task, plan, name):
    import sys

    from peptidemt import (
        HydrAMPAnalogueBundle,
        HydrAMPAnalogueReceipt,
        HydrAMPLimits,
        MacrelLimits,
        assess_macrel,
        prepare_sequences,
        redesign_hydramp,
    )

    directory = task / "run" / name
    network_guard(plan)
    inventory = {
        d.metadata["Name"].lower(): d.version
        for d in importlib.metadata.distributions()
    }
    profile = plan["profiles"]["generation" if name == "direct" else "assessment"]
    if inventory != profile["inventory"]:
        raise ValueError("Changed executing profile inventory")
    write(
        directory / "runtime.json",
        {"python": sys.version, "prefix": sys.prefix, "inventory": inventory},
    )
    if name in ("direct", "adapter", "repeat"):
        if name == "direct":
            receipt = native(plan, directory)
        else:
            limits = {
                **plan["hydramp_limits"],
                "cpu_ids": tuple(plan["hydramp_limits"]["cpu_ids"]),
                "temporary_root": str(directory),
            }
            receipt = redesign_hydramp(
                parents_for(plan),
                snapshot_id="R3-" + name,
                bundle=HydrAMPAnalogueBundle(**plan["bundle"]),
                limits=HydrAMPLimits(**limits),
                worker_python=plan["profiles"]["generation"]["python"],
                qualification_reference=plan["qualification_reference"],
                **plan["request"],
            )
        (directory / "receipt.json").write_text(receipt.to_json())
        if receipt.issues:
            raise ValueError("Analogue receipt rejected: " + repr(receipt.issues))
        if name == "repeat":

            def load(tag):
                return HydrAMPAnalogueReceipt.from_json(
                    (task / "run" / tag / "receipt.json").read_text()
                )

            compare_receipts(load("direct"), load("adapter"), receipt)
        return
    receipt = HydrAMPAnalogueReceipt.from_json(
        (task / "run/adapter/receipt.json").read_text()
    )
    inputs = (
        prepare_sequences(plan["controls"])
        if name == "controls"
        else parents_for(plan)
        if name == "parents"
        else receipt.proposals()
    )
    # Reserve the complete possible pair before dispatch; a partial child consumes its slot.
    write(
        directory / "reserved.json",
        {
            "macrel_calls": 1,
            "maximum_onnx_evaluations": 2,
            "eligible_occurrences": sum(not p.issues for p in inputs),
        },
    )
    limits = {
        **plan["macrel_limits"],
        "cpu_ids": tuple(plan["macrel_limits"]["cpu_ids"]),
        "temporary_root": str(directory),
    }
    result = assess_macrel(
        inputs,
        snapshot_id="R3-" + name,
        limits=MacrelLimits(**limits),
        qualification_reference=plan["qualification_reference"],
    )
    (directory / "assessment.json").write_text(result.to_json())
    check_assessment(result)
    if name == "controls":
        expected = plan["control_native_values"]
        if any(
            dict(row.values) != expected[item.proposal.sequence]
            for item, row in zip(result.inputs, result.rows, strict=True)
        ):
            raise ValueError("Exact retained W3 control values differ")
    if name == "children":
        write(directory / "selection.json", saved_selection(receipt, result))
    write(
        directory / "outcome.json",
        {
            "completed": True,
            "evaluated_occurrences": len(result.rows),
            "incompatible_occurrences": sum(bool(p.issues) for p in inputs),
            "onnx_evaluations_confirmed_on_complete_pair": 2 if result.rows else 0,
            "returned_only_child_pool": name == "children",
        },
    )


def execute(task, plan):
    from peptidemt._hydramp_process import supervise

    authorize(task, plan)
    run = task / "run"
    run.mkdir()  # Exclusive directory prevents automatic re-entry or retry.
    outcomes = []
    for name in ("direct", "adapter", "repeat", "controls", "parents", "children"):
        directory = run / name
        directory.mkdir()
        write(directory / "attempt.json", {"stage": name, "retries": 0})
        python = plan["profiles"]["generation" if name == "direct" else "assessment"][
            "python"
        ]
        result = supervise(
            [
                python,
                "-B",
                "-I",
                str(Path(__file__).resolve()),
                str(task),
                "--stage",
                name,
            ],
            directory,
            SimpleNamespace(**plan["supervisor_limits"]),
        )
        write(directory / "supervision.json", result)
        outcomes.append({"stage": name, **result})
        write(run / "execution.json", outcomes)
        if result.get("failure") or result.get("returncode") != 0:
            raise RuntimeError(
                "R3 stopped; preserve evidence before any new authorization: " + name
            )


def main():
    import sys
    import traceback

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("task", type=Path)
    parser.add_argument(
        "--stage",
        choices=("direct", "adapter", "repeat", "controls", "parents", "children"),
    )
    args = parser.parse_args()
    task = args.task.resolve()
    plan = json.loads((task / "plan.json").read_text())
    if args.stage:
        directory = task / "run" / args.stage
        with (directory / "console.log").open("x") as log:
            old_out, old_err = sys.stdout, sys.stderr
            try:
                sys.stdout = sys.stderr = log
                from peptidemt._hydramp_process import configure_child

                configure_child(plan["child_limits"], os.getppid())
                authorize(task, plan)
                stage(task, plan, args.stage)
            except BaseException:
                traceback.print_exc(file=log)
                raise
            finally:
                sys.stdout, sys.stderr = old_out, old_err
    else:
        execute(task, plan)


if __name__ == "__main__":
    main()
