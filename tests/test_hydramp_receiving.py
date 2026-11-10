"""Public data receiving and controlled composition, not model execution."""

import json
import math
import subprocess
import sys
from dataclasses import replace
from pathlib import Path
from types import SimpleNamespace

import pytest

import peptidemt
from peptidemt import HydrAMPReceipt, Provenance, ProviderRow, ResultSet, select


def native(sequence, amp=0.9, mic=0.8):
    return {
        "sequence": sequence,
        "amp": amp,
        "mic": mic,
        "length": len(sequence),
        "hydrophobicity": 0.1,
        "hydrophobic_moment": 0.2,
        "charge": 1.0,
        "isoelectric_point": 7.0,
    }


@pytest.fixture
def receipt():
    return HydrAMPReceipt(
        "controlled-generation",
        3,
        1001,
        (native("RRK", 0.99), native("ACD", 0.9), native("MKW", 0.1)),
        (2, 0, 1),
        Provenance(
            "invented-hydramp",
            "artificial-bundle",
            "controlled-fixture",
            details={"provider_executed": False, "charge_amide": True},
        ),
        original_trace={
            "sequences": ("ACD", "MKW", "RRK"),
            "tokens": ((1, 0, 2, 3), (4, 5, 6, 0), (7, 8, 0, 9)),
            "amp": (0.9, 0.1, 0.99),
            "mic": (0.8, 0.8, 0.8),
        },
    )


def test_returned_order_original_zero_tokens_and_unresolved_chemistry(receipt):
    assert receipt.issues == ()
    assert [x.proposal.sequence for x in receipt.inputs] == ["RRK", "ACD", "MKW"]
    assert [x.token for x in receipt.inputs] == ["input-0", "input-1", "input-2"]
    evidence = receipt.inputs[0].proposal.context["generation"]
    assert evidence["reported_draw_index"] == 2
    assert evidence["original_trace"]["tokens"] == (7, 8, 0, 9)
    assert evidence["native_result"]["amp"] == 0.99
    assert evidence["native_result"]["mic"] == 0.8
    assert not receipt.inputs[0].proposal.chemistry
    assert receipt.inputs[2].issues == ("sequence_changing_native_preprocessing",)


def test_json_replay_retains_exact_floats_order_and_source(receipt):
    restored = HydrAMPReceipt.from_json(receipt.to_json())
    assert restored.to_json() == receipt.to_json()
    assert restored.native_results[0]["amp"].hex() == float(0.99).hex()
    assert restored.inputs == receipt.inputs
    assert restored.provenance.details["provider_executed"] is False


@pytest.mark.parametrize("key", ["seed", "sequence", "provider", "float_hex"])
def test_duplicate_json_keys_cannot_overwrite_generation_evidence(receipt, key):
    text = receipt.to_json()
    marker = json.dumps(key) + ":"
    # Even an overwritten value that leaves the final document otherwise valid
    # is ambiguous evidence. Validate nested objects as well as the envelope.
    corrupted = text.replace(marker, marker + " null, " + marker, 1)
    assert corrupted != text
    with pytest.raises(ValueError, match="Duplicate JSON key: " + key):
        HydrAMPReceipt.from_json(corrupted)


def test_public_receipt_replays_in_fresh_reader_with_all_engines_blocked(receipt):
    code = """
import importlib.abc,sys
sys.path.insert(0,sys.argv[1])
class NoEngines(importlib.abc.MetaPathFinder):
    def find_spec(self,fullname,path=None,target=None):
        if fullname.split('.')[0] in {'numpy','torch','tensorflow','keras',
            'hydramp_torch','amp','modlamp','molsysmt','macrel','onnxruntime',
            'ackredit'} or fullname in {'peptidemt.macrel','peptidemt._attribution'}:
            raise AssertionError('Saved reading tried a scientific provider')
sys.meta_path.insert(0,NoEngines())
import peptidemt
from peptidemt import HydrAMPReceipt
assert 'HydrAMPReceipt' in peptidemt.__all__
saved=sys.stdin.read()
receipt=HydrAMPReceipt.from_json(saved)
assert receipt.to_json()==saved
assert [item.proposal.sequence for item in receipt.inputs]==['RRK','ACD','MKW']
assert receipt.inputs[0].proposal.context['generation']['original_trace']['tokens']==(7,8,0,9)
assert receipt.provenance.details['provider_executed'] is False
assert not any(name in sys.modules for name in ('torch','numpy','macrel','ackredit'))
"""
    completed = subprocess.run(
        [
            sys.executable,
            "-B",
            "-I",
            "-c",
            code,
            str(Path(peptidemt.__file__).parent.parent),
        ],
        input=receipt.to_json(),
        text=True,
        capture_output=True,
        timeout=10,
    )
    assert completed.returncode == 0, completed.stdout + completed.stderr


def test_captured_decoder_input_is_distinct_from_precast_conditioning(receipt):
    trace = dict(receipt.original_trace)
    trace["conditioned"] = ((1 + 2**-30,), (2.0,), (3.0,))
    trace["decoder_input"] = ((1.0,), (2.0,), (3.0,))
    data = replace(receipt, original_trace=trace)
    row = data.inputs[1].proposal.context["generation"]["original_trace"]
    assert row["conditioned"] == (1 + 2**-30,)
    assert row["decoder_input"] == (1.0,)


def test_receiving_an_already_produced_trace_uses_only_its_retained_values(receipt):
    class ArtificialArray:
        def __init__(self, values):
            self.values = values

        def tolist(self):
            return list(self.values)

    trace = SimpleNamespace(
        seed=receipt.seed,
        native_results=receipt.native_results,
        returned_input_indices=receipt.returned_input_indices,
        sampled_latents=ArtificialArray(((0.1,), (0.2,), (0.3,))),
        conditioned=ArtificialArray(((0.4,), (0.5,), (0.6,))),
        tokens=ArtificialArray(receipt.original_trace["tokens"]),
        sequences=receipt.original_trace["sequences"],
        amp=ArtificialArray(receipt.original_trace["amp"]),
        mic=ArtificialArray(receipt.original_trace["mic"]),
    )
    data = HydrAMPReceipt.from_trace(
        trace, snapshot_id="received", requested_count=3, provenance=receipt.provenance
    )
    assert data.issues == ()
    assert data.native_results == receipt.native_results
    assert data.inputs[0].proposal.context["generation"]["original_trace"][
        "sampled_latents"
    ] == (0.3,)


def test_mutable_source_is_detached_and_unknown_fields_retained(receipt):
    rows = [dict(row) for row in receipt.native_results]
    rows[0]["unknown_native_field"] = {"list": [1.0]}
    data = replace(receipt, native_results=rows)
    rows[0]["sequence"] = "CHANGED"
    rows[0]["unknown_native_field"]["list"][0] = 2.0
    assert data.native_results[0]["sequence"] == "RRK"
    assert data.native_results[0]["unknown_native_field"]["list"] == (1.0,)


def test_duplicates_empty_and_noncanonical_proposals_are_not_repaired(receipt):
    rows = (native("ACD"), native("ACD"), native(""), native("a*"))
    data = replace(
        receipt,
        requested_count=4,
        native_results=rows,
        returned_input_indices=(0, 1, 2, 3),
        original_trace={},
    )
    assert [x.proposal.sequence for x in data.inputs] == ["ACD", "ACD", "", "a*"]
    assert data.inputs[2].issues == ("empty_sequence",)
    assert data.inputs[3].issues == ("unsupported_symbols",)
    assert data.inputs[0].token != data.inputs[1].token


@pytest.mark.parametrize("indices", [(0,), (True, 0, 1), (0, 0, 1), (99, 0, 1)])
def test_broken_mapping_retains_rows_and_cannot_attach_a_false_trace(receipt, indices):
    data = replace(receipt, returned_input_indices=indices)
    assert len(data.inputs) == len(data.native_results) == 3
    assert data.issues
    for item in data.inputs:
        evidence = item.proposal.context["generation"]
        if evidence["row_issues"]:
            assert not evidence["original_trace"]
        elif evidence["original_trace"]:
            assert evidence["original_trace"]["sequences"] == item.proposal.sequence


def test_incomplete_and_completed_empty_results_remain_distinct(receipt):
    empty = replace(
        receipt, native_results=(), returned_input_indices=(), original_trace={}
    )
    failed = replace(empty, completed=False, failures=("timeout",))
    assert empty.completed and empty.inputs == ()
    assert empty.issues == ("returned_count_mismatch",)
    assert not failed.completed and "incomplete_run" in failed.issues
    assert "reported_failure:timeout" in failed.issues


def test_malformed_native_rows_and_nonfinite_scores_survive_portable_replay(receipt):
    bad = native("RRK", math.nan)
    data = replace(receipt, native_results=(bad, "ACD", 123), original_trace={})
    assert len(data.inputs) == 3
    assert data.inputs[1].proposal.sequence == "ACD"
    assert data.inputs[2].proposal.sequence is None
    assert data.inputs[2].proposal.context["generation"]["native_result"] == 123
    restored = HydrAMPReceipt.from_json(data.to_json())
    assert math.isnan(restored.native_results[0]["amp"])
    assert "row:0:invalid_native_value:amp" in restored.issues
    assert "row:1:malformed_native_row" in restored.issues


@pytest.mark.parametrize(
    "field",
    (
        "amp",
        "mic",
        "length",
        "hydrophobicity",
        "hydrophobic_moment",
        "charge",
        "isoelectric_point",
    ),
)
@pytest.mark.parametrize("sign", (-1, 1))
def test_oversized_numeric_values_remain_inspectable_after_replay(receipt, field, sign):
    value = sign * 10**400
    row = {**receipt.native_results[0], field: value}
    data = replace(
        receipt,
        native_results=(row, *receipt.native_results[1:]),
        original_trace={},
    )
    for candidate in (data, HydrAMPReceipt.from_json(data.to_json())):
        assert f"row:0:invalid_native_value:{field}" in candidate.issues
        assert candidate.native_results[0][field] == value
        evidence = candidate.inputs[0].proposal.context["generation"]
        assert evidence["native_result"][field] == value
        assert f"invalid_native_value:{field}" in evidence["row_issues"]
        assert evidence["original_trace"] == {}


def test_source_trace_mismatch_is_visible_and_not_attributed(receipt):
    trace = dict(receipt.original_trace)
    trace["amp"] = (0.9, 0.1, 0.123)
    data = replace(receipt, original_trace=trace)
    assert "row:0:inconsistent_source_trace:amp" in data.issues
    assert data.inputs[0].proposal.context["generation"]["original_trace"] == {}
    assert data.original_trace["amp"][2] == 0.123


def test_controlled_macrel_composition_uses_only_macrel_scores_and_no_prefilter(
    receipt,
):
    rows = []
    for token, seq, amp, hemo in [
        ("input-0", "RRK", 0.1, 0.01),
        ("input-1", "ACD", 0.9, 0.5),
    ]:
        rows.append(
            ProviderRow(
                token,
                {
                    "Sequence": seq,
                    "AMP_probability": amp,
                    "is_AMP": amp > 0.5,
                    "Hemolytic_probability": hemo,
                    "Hemolytic": "Hemo" if hemo > 0.5 else "NonHemo",
                    "AMP_family": "ALP",
                },
            )
        )
    result = ResultSet(
        "invented-assessment",
        receipt.inputs,
        rows,
        Provenance("invented-macrel", "controlled-values", "controlled-fixture"),
    )
    amp = select(result, policy="amp-first", k=1)
    hemo = select(result, policy="hemolysis-first", k=1)
    assert amp.selected == ("input-1",)  # Native AMP prefers input-0.
    assert hemo.selected == ("input-0",)
    assert len(result.inputs) == 3
    assert amp.excluded[0][0] == "input-2"
    replay = ResultSet.from_json(result.to_json())
    assert select(replay, policy="amp-first", k=1) == amp
    assert (
        replay.inputs[0].proposal.context["generation"]["native_result"]["amp"] == 0.99
    )


def test_imported_generator_evidence_is_not_promoted_to_qualified(receipt):
    data = replace(
        receipt,
        provenance=Provenance("hydramp-torch", "dev3-retained-data", "imported"),
    )
    evidence = data.inputs[0].proposal.context["generation"]["provenance"]
    assert evidence["evidence_kind"] == "imported"
    assert evidence["qualification_reference"] is None


def test_unknown_schema_or_extra_snapshot_fields_are_rejected(receipt):
    text = receipt.to_json().replace("peptidemt.hydramp_receipt@1", "unknown@1")
    with pytest.raises(ValueError, match="schema"):
        HydrAMPReceipt.from_json(text)
    text = json.loads(receipt.to_json())
    text["mapping"]["extra"] = True
    with pytest.raises(ValueError, match="fields"):
        HydrAMPReceipt.from_json(json.dumps(text))
