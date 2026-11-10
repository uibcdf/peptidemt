"""One pinned analogue call; all model operations remain HydrAMP-owned."""

import importlib.metadata
import os
import resource
import sys
from dataclasses import replace
from pathlib import Path

from ._analogue_receiving import HydrAMPAnalogueReceipt
from ._data import decode, load_json
from ._hydramp_process import configure_child, source_manifest
from ._hydramp_worker import _load_provider, _save
from .inputs import InputRecord, SequenceRecord
from .results import Provenance

_SCHEMA = "peptidemt.hydramp_analogue_worker@1"


def run(request, state_path):
    from .analogue import HydrAMPAnalogueBundle, HydrAMPLimits

    bundle = HydrAMPAnalogueBundle(**request["bundle"])
    limits = HydrAMPLimits(
        **{**request["limits"], "cpu_ids": tuple(request["limits"]["cpu_ids"])}
    )
    parents = tuple(
        InputRecord(p["occurrence"], SequenceRecord(**p["proposal"]))
        for p in request["parents"]
    )
    provenance = Provenance(
        "hydramp-torch",
        bundle.bundle_id,
        bundle.evidence_kind,
        request["qualification_reference"],
    )
    base = HydrAMPAnalogueReceipt(
        request["snapshot_id"],
        parents,
        request["seed"],
        request["temperature"],
        request["n_attempts"],
        request["submitted_parent_indices"],
        provenance,
        completed=False,
    )
    compatible = tuple(
        p.parent_occurrence for p in base.outcomes if p.status != "incompatible"
    )
    b = len(compatible)
    if (
        request.get("schema") != "peptidemt.hydramp_analogue_request@1"
        or bundle.bundle_id != request["bundle_id"]
        or base.content_id != request["request_id"]
        or tuple(request["submitted_parent_indices"]) != compatible
        or not b
        or b * base.n_attempts > limits.max_records
    ):
        raise ValueError("Invalid/oversized analogue request or parent mapping")
    if (
        source_manifest(Path(__file__).parent)
        != dict(request["consumer_source_sha256"])
        or importlib.metadata.version("peptidemt") != request["consumer_version"]
    ):
        raise ValueError("Worker PeptideMT source/version differs from the caller")
    state = {
        "stage": "dependency",
        "attempted": {},
        "completed": [],
        "runtime": {},
        "neural_evaluations_attempted": 0,
        "neural_evaluations_completed": 0,
        "sampling_observation": "Confirmed only after returned trace; interrupted internal sampling may be unknown",
    }
    receipt = None

    def reserve(name, evaluations=0):
        if state["attempted"].get(name):
            raise RuntimeError("Single-operation budget exhausted: " + name)
        state["attempted"][name] = 1
        state["neural_evaluations_attempted"] += evaluations
        state["stage"] = name
        _save(state_path, state)

    def done(name, evaluations=0):
        state["completed"].append(name)
        state["neural_evaluations_completed"] += evaluations
        _save(state_path, state)

    _save(state_path, state)
    try:
        provider, np, torch = _load_provider(request["bundle"], state, analogue=True)
        if torch.version.cuda is not None:
            raise ValueError("Analogue route requires a CPU-only Torch build")
        torch.set_num_threads(limits.threads)
        torch.set_num_interop_threads(1)
        state["runtime"]["resource_controls"] = {
            "cpu_ids": sorted(os.sched_getaffinity(0)),
            "nice": os.nice(0),
            "address_space_bytes": resource.getrlimit(resource.RLIMIT_AS)[0],
            "torch_threads": torch.get_num_threads(),
            "torch_interop_threads": torch.get_num_interop_threads(),
            "cpu_only_build": True,
        }
        reserve("native_encoding")
        sequences = tuple(parents[i].proposal.sequence for i in compatible)
        tokens = provider.encode_sequences(sequences)
        if tuple(provider.translate_tokens(tokens.numpy())) != sequences:
            raise ValueError("Native codec changed a submitted sequence view")
        done("native_encoding")
        reserve("encoder_loading")
        encoder = provider.load_encoder_checkpoint(
            bundle.checkpoint_root, bundle.checkpoint_sha256
        )
        done("encoder_loading")
        reserve("checkpoint_loading")
        core = provider.load_checkpoint(
            bundle.checkpoint_root, bundle.checkpoint_sha256
        )
        done("checkpoint_loading")
        n = b * base.n_attempts
        encoder_calls, score_calls = 0, 0
        encode_tokens, score_tokens, decode_tokens = (
            encoder.encode_tokens,
            core.score_tokens,
            core.decode_conditioned,
        )

        def encode_tap(values):
            nonlocal encoder_calls
            if encoder_calls >= 2:
                raise RuntimeError("Extra encoder call blocked")
            name = ("native_encoder_scale", "native_encoder_mean")[encoder_calls]
            expected = (b, n)[encoder_calls]
            if len(values) != expected:
                raise ValueError("Wrong encoder batch")
            encoder_calls += 1
            reserve(name, 1)
            result = encode_tokens(values)
            done(name, 1)
            return result

        def score_tap(values):
            nonlocal score_calls
            if score_calls >= 2:
                raise RuntimeError("Extra paired-head call blocked")
            name = ("native_prototype_scoring", "native_generated_scoring")[score_calls]
            if len(values) != (b, n)[score_calls]:
                raise ValueError("Wrong scoring batch")
            score_calls += 1
            reserve(name, 2)
            result = score_tokens(values)
            done(name, 2)
            return result

        def decode_tap(values):
            if len(values) != n:
                raise ValueError("Wrong decoder batch")
            reserve("native_decoding", 1)
            result = decode_tokens(values)
            done("native_decoding", 1)
            return result

        encoder.encode_tokens, core.score_tokens, core.decode_conditioned = (
            encode_tap,
            score_tap,
            decode_tap,
        )
        generator = provider.HydrAMPAnalogueGenerator(
            encoder, core, max_proposals=limits.max_records
        )
        reserve("native_analogue")
        trace = generator.generate_with_trace(
            tokens,
            seed=base.seed,
            temperature=base.temperature,
            n_attempts=base.n_attempts,
            mode="improvement",
            properties=False,
            filtering_options=None,
        )
        if state["neural_evaluations_completed"] != 7:
            raise ValueError("Incomplete native analogue operation ledger")
        done("native_sampling")
        done("native_analogue")
        state["stage"] = "result_receiving"
        _save(state_path, state)
        receipt = HydrAMPAnalogueReceipt.from_trace(
            trace,
            snapshot_id=base.snapshot_id,
            parents=parents,
            submitted_parent_indices=compatible,
            provenance=provenance,
        )
        if receipt.issues:
            raise ValueError(
                "Unreceived native analogue output: " + ", ".join(receipt.issues)
            )
        state["stage"] = "completed"
        state["runtime"]["worker_kernel_hwm_rss_bytes"] = (
            resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024
        )
        _save(state_path, state)
        return {"schema": _SCHEMA, "receipt": receipt.to_json(), "state": state}
    except Exception as error:
        _save(state_path, state)
        result = {
            "schema": _SCHEMA,
            "failure": state["stage"],
            "cause_type": type(error).__name__,
            "cause_message": str(error)[:8192],
            "state": state,
        }
        if receipt is not None:
            result["receipt"] = replace(
                receipt, completed=False, failures=(state["stage"],)
            ).to_json()
        return result


def main():
    request_path, response_path = map(Path, sys.argv[1:])
    request = decode(load_json(request_path.read_text(encoding="utf-8")))

    def audit(event, args):
        if event == "socket.connect":
            raise RuntimeError("Network is prohibited in the analogue worker")

    try:
        configure_child(request["limits"], request["parent_pid"])
        sys.addaudithook(audit)
        result = run(request, request_path.parent / "state.json")
    except Exception as error:
        result = {
            "schema": _SCHEMA,
            "failure": "worker_preflight",
            "cause_type": type(error).__name__,
            "cause_message": str(error)[:8192],
            "state": {},
        }
    _save(response_path, result)
