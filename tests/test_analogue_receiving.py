"""Artificial analogue payloads only; no native model or Macrel execution."""

import json
import subprocess
import sys
from dataclasses import replace

import pytest
from analogue_fixtures import artificial_receipt

from peptidemt import (
    HydrAMPAnalogueReceipt,
    ProviderRow,
    ResultSet,
    SequenceRecord,
    analogue_input_issues,
    prepare_sequences,
    select,
)
from peptidemt._data import decode, encode, freeze, load_json


@pytest.fixture
def receipt():
    return artificial_receipt()


def change(receipt, edit):
    # JSON decoding yields tuples; ordinary JSON gives mutable fixture containers.
    def mutable(v):
        if hasattr(v, "items"):
            return {k: mutable(x) for k, x in v.items()}
        if isinstance(v, tuple):
            return [mutable(x) for x in v]
        return v

    t = mutable(receipt.original_trace)
    edit(t)
    return replace(receipt, original_trace=t)


def test_nonempty_duplicate_parent_pools_and_raw_attempt_mapping(receipt):
    assert receipt.issues == ()
    assert [o.status for o in receipt.outcomes] == [
        "candidates",
        "incompatible",
        "candidates",
        "candidates",
        "incompatible",
    ]
    assert [x.parent_occurrence for x in receipt.links] == [0, 0, 2, 2, 3]
    assert [x.trace_row for x in receipt.links] == [6, 0, 1, 4, 2]
    assert receipt.parents[0].proposal.header == "first"
    assert receipt.parents[4].proposal.chemistry["terminal"] == "explicit"
    assert receipt.original_trace["duplicate"][3]


def test_projection_pool_chemistry_and_unchanged_selectors(receipt):
    inputs = receipt.proposals()
    assert [p.proposal.sequence for p in inputs] == [
        "",
        "KAAAA",
        "KAAAA",
        "LAAAA",
        "MAAAA",
    ]
    assert all(not p.proposal.chemistry for p in inputs)
    assert "measured" not in inputs[1].proposal.context
    assert inputs[1].proposal.context["generation"]["parent_occurrence"] == 0
    assert inputs[2].proposal.context["generation"]["parent_occurrence"] == 2
    assert inputs[0].issues == ("empty_sequence",)
    assert inputs[4].issues == ("sequence_changing_native_preprocessing",)
    rows = tuple(
        ProviderRow(
            inputs[i].token,
            {
                "Sequence": inputs[i].proposal.sequence,
                "AMP_probability": 0.8,
                "is_AMP": True,
                "Hemolytic_probability": 0.2,
                "Hemolytic": "NonHemo",
                "AMP_family": "ADP",
            },
        )
        for i in (1, 2, 3)
    )
    results = ResultSet("controlled-assessment", inputs, rows, receipt.provenance)
    for policy in ("amp-first", "hemolysis-first"):
        selection = select(results, policy=policy, k=2)
        assert selection.ranking == ("input-1", "input-2", "input-3")
        assert selection.selected == ("input-1", "input-2")


@pytest.mark.parametrize(
    "sequence,chemistry,expected",
    [
        ("M", {}, ()),
        ("A" * 25, {}, ()),
        ("A" * 26, {}, ("outside_hydramp_length_scope",)),
        (None, {}, ("incomplete_sequence",)),
        ("", {}, ("empty_sequence",)),
        ("acd", {}, ("unsupported_symbols",)),
        ("AX", {}, ("unsupported_symbols",)),
        ("ACD", {"stereo": "D"}, ("unassessed_explicit_chemistry",)),
    ],
)
def test_admission_is_specific_and_never_changes_input(sequence, chemistry, expected):
    item = prepare_sequences([SequenceRecord(sequence, chemistry=chemistry)])[0]
    assert analogue_input_issues(item) == expected
    assert item.proposal.sequence == sequence
    assert dict(item.proposal.chemistry) == chemistry


@pytest.mark.parametrize(
    "field",
    ["amp", "prototype_mic", "noise", "latents", "conditioned", "prototype_std"],
)
@pytest.mark.parametrize("bad", [float("nan"), float("inf"), 10**1000, True])
def test_nonfinite_oversized_or_boolean_numbers_stay_inspectable(receipt, field, bad):
    def edit(t):
        if field in ("amp", "prototype_mic"):
            t[field][0] = bad
        else:
            t[field][0][0] = bad

    changed = change(receipt, edit)
    assert "invalid_trace:" + field in changed.issues
    assert HydrAMPAnalogueReceipt.from_json(changed.to_json()).issues == changed.issues
    with pytest.raises(ValueError, match="Unreceived"):
        changed.proposals()


@pytest.mark.parametrize(
    "edit",
    [
        lambda t: t["results"][0]["candidates"][1].update(trace_row=3, attempt_index=1),
        lambda t: t["results"][1].update(prototype_sequence="changed"),
        lambda t: t["improves"].__setitem__(8, True),
        lambda t: t["duplicate"].__setitem__(3, False),
        lambda t: t["retained"].__setitem__(3, True),
        lambda t: t["attempt_indices"].__setitem__(0, True),
        lambda t: t["submitted_tokens"][0].__setitem__(0, 20),
        lambda t: t["results"][1]["candidates"].reverse(),
        lambda t: t["sequences"].__setitem__(0, "altered"),
        lambda t: t["results"][0]["candidates"][0].update(trace_row=True),
        lambda t: t.pop("noise"),
        lambda t: t.update(seed=8),
    ],
)
def test_changed_decisions_and_ambiguous_source_cannot_yield_proposals(receipt, edit):
    changed = change(receipt, edit)
    assert changed.issues
    assert not changed.links
    assert any(o.status == "invalid_output" for o in changed.outcomes)
    with pytest.raises(ValueError):
        changed.proposals()


def test_no_hit_is_distinct_from_incompatible_and_failed(receipt):
    def edit(t):
        t["amp"] = [0.1] * 9
        t["improves"] = [False] * 9
        t["duplicate"] = [False] * 9
        t["retained"] = [False] * 9
        for r in t["results"]:
            r["candidates"] = []

    no_hit = change(receipt, edit)
    assert not no_hit.issues and no_hit.proposals() == ()
    assert [o.status for o in no_hit.outcomes] == [
        "no_hit",
        "incompatible",
        "no_hit",
        "no_hit",
        "incompatible",
    ]
    failed = replace(
        receipt,
        completed=False,
        failures=("timeout",),
        progress={"attempted": {"native_analogue": 1}},
    )
    assert failed.outcomes[0].status == "interrupted"
    assert failed.original_trace == receipt.original_trace
    assert replace(failed, progress={}).outcomes[0].status == "not_attempted"


def test_empty_or_no_compatible_inputs_need_no_trace(receipt):
    for parents in (
        (),
        prepare_sequences(
            [
                SequenceRecord(None),
                "",
                SequenceRecord("ACD", chemistry={"terminal": "x"}),
            ]
        ),
    ):
        value = replace(
            receipt, parents=parents, submitted_parent_indices=(), original_trace={}
        )
        assert value.issues == () and value.links == () and value.proposals() == ()


@pytest.mark.parametrize(
    "indices", [(0, 3, 2), (0, 0, 3), (0, 2), (False, 2, 3), (0, 2, 9)]
)
def test_submission_mapping_is_complete_ordered_and_not_a_bool(receipt, indices):
    assert replace(receipt, submitted_parent_indices=indices).issues == (
        "invalid_parent_submission_mapping",
    )


def test_content_bound_replay_and_source_is_immutable(receipt):
    replay = HydrAMPAnalogueReceipt.from_json(receipt.to_json())
    assert replay.content_id == receipt.content_id and replay.links == receipt.links
    with pytest.raises(TypeError):
        replay.original_trace["seed"] = 1
    payload = decode(load_json(receipt.to_json()))
    payload["data"]["snapshot_id"] = "other"
    with pytest.raises(ValueError, match="digest"):
        HydrAMPAnalogueReceipt.from_json(json.dumps(encode(freeze(payload))))
    with pytest.raises(ValueError, match="Duplicate"):
        HydrAMPAnalogueReceipt.from_json('{"mapping":{},"mapping":{}}')


def test_saved_receiving_has_no_scientific_engine_imports(receipt):
    script = """
import importlib.abc,sys
class Block(importlib.abc.MetaPathFinder):
 def find_spec(self,fullname,path=None,target=None):
  if fullname.split('.')[0] in {'numpy','torch','tensorflow','keras','macrel','hydramp_torch','molsysmt','ackredit'}:raise RuntimeError(fullname)
sys.meta_path.insert(0,Block())
from peptidemt import HydrAMPAnalogueReceipt
r=HydrAMPAnalogueReceipt.from_json(sys.stdin.read())
assert not r.issues and len(r.proposals())==5
"""
    run = subprocess.run(
        [sys.executable, "-I", "-c", script],
        input=receipt.to_json(),
        capture_output=True,
        text=True,
        timeout=10,
    )
    assert run.returncode == 0, run.stderr


def test_saved_example_composes_exact_assessment_and_rejects_mixed_ancestry(
    receipt, tmp_path
):
    from pathlib import Path

    inputs = receipt.proposals()
    rows = tuple(
        ProviderRow(
            inputs[i].token,
            {
                "Sequence": inputs[i].proposal.sequence,
                "AMP_probability": 0.8,
                "is_AMP": True,
                "Hemolytic_probability": 0.2,
                "Hemolytic": "NonHemo",
                "AMP_family": "ADP",
            },
        )
        for i in (1, 2, 3)
    )
    results = ResultSet("controlled-assessment", inputs, rows, receipt.provenance)
    path, assessment = tmp_path / "receipt.json", tmp_path / "assessment.json"
    path.write_text(receipt.to_json())
    assessment.write_text(results.to_json())
    example = (
        Path(__file__).resolve().parents[1] / "examples/replay_analogue_workflow.py"
    )
    script = """
import importlib.abc,runpy,sys
class Block(importlib.abc.MetaPathFinder):
 def find_spec(self,fullname,path=None,target=None):
  if fullname.split('.')[0] in {'numpy','torch','tensorflow','keras','hydramp_torch','macrel','molsysmt','ackredit'}:raise RuntimeError(fullname)
sys.meta_path.insert(0,Block())
sys.argv=sys.argv[1:]
runpy.run_path(sys.argv[0],run_name='__main__')
"""
    command = [
        sys.executable,
        "-I",
        "-c",
        script,
        str(example),
        str(path),
        "--assessment",
        str(assessment),
        "--k",
        "2",
    ]
    result = subprocess.run(command, capture_output=True, text=True, timeout=10)
    assert result.returncode == 0, result.stderr
    printed = json.loads(result.stdout)
    assert printed["new_model_or_assessment_calls"] == 0
    assert printed["selection"] == {
        "amp-first": ["input-1", "input-2"],
        "hemolysis-first": ["input-1", "input-2"],
    }
    path.write_text(replace(receipt, snapshot_id="other-execution").to_json())
    bad = subprocess.run(command, capture_output=True, text=True, timeout=10)
    assert bad.returncode != 0 and "ancestry differ" in bad.stderr
