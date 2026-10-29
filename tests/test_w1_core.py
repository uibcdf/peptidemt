"""Controlled W1 fixtures, not Macrel outputs or live M1–M8 qualification."""

import json
import math
import subprocess
import sys

import pytest

from peptidemt import (
    InputRecord,
    Provenance,
    ProviderRow,
    ResultSet,
    SequenceRecord,
    parse_fasta,
    prepare_sequences,
    read_fasta,
    select,
)


def fixture_provenance(**changes):
    fields = dict(
        provider="invented-fixture",
        bundle_id="D35-toy-values",
        evidence_kind="controlled-fixture",
        details={"scientific_data": False, "provider_executed": False},
    )
    fields.update(changes)
    return Provenance(**fields)


def row(token, amp=0.9, hemo=0.2, sequence="ACD", **changes):
    values = dict(
        Sequence=sequence,
        AMP_probability=amp,
        is_AMP=amp > 0.5,
        Hemolytic_probability=hemo,
        Hemolytic="Hemo" if hemo > 0.5 else "NonHemo",
        AMP_family="ALP",
    )
    values.update(changes)
    return ProviderRow(token, values)


def result(rows=(), sequences=("ACD",), **changes):
    fields = dict(
        snapshot_id="controlled-snapshot",
        inputs=prepare_sequences(sequences),
        rows=rows,
        provenance=fixture_provenance(),
    )
    fields.update(changes)
    return ResultSet(**fields)


def test_fasta_preserves_full_repeated_headers_raw_records_and_empty_occurrences(
    tmp_path,
):
    text = ">same full header\r\nAC\r\nD\r\n>same full header\nACD\n>empty\n"
    path = tmp_path / "proposals.fasta"
    path.write_bytes(text.encode())
    records = read_fasta(path)
    inputs = prepare_sequences(records)
    assert [r.sequence for r in records] == ["ACD", "ACD", ""]
    assert [r.header for r in records] == [
        "same full header",
        "same full header",
        "empty",
    ]
    assert "".join(r.raw_record for r in records) == text
    assert all(r.source == str(path) for r in records)
    assert [r.token for r in inputs] == ["input-0", "input-1", "input-2"]
    assert inputs[2].issues == ("empty_sequence",)
    assert parse_fasta(" \n") == ()
    assert parse_fasta(">\n")[0].header == ""


def test_fasta_does_not_silently_remove_sequence_whitespace_or_accept_unnamed_records():
    records = parse_fasta(">raw\n acD \nA*\n")
    assert records[0].sequence == " acD A*"
    assert prepare_sequences(records)[0].issues == ("unsupported_symbols",)
    with pytest.raises(ValueError, match="before the first header at line 2"):
        parse_fasta("\nACD\n>named\nACD\n")


@pytest.mark.parametrize(
    "sequence,reason",
    [
        (None, "incomplete_sequence"),
        ("", "empty_sequence"),
        ("MACD", "sequence_changing_native_preprocessing"),
        ("M", "sequence_changing_native_preprocessing"),
        ("ACD*", "unsupported_symbols"),
        ("A*C", "unsupported_symbols"),
        ("acD", "unsupported_symbols"),
        ("AXD", "unsupported_symbols"),
        ("A-C", "unsupported_symbols"),
        ("A[mod]C", "unsupported_symbols"),
        ("A" * 100, "outside_provisional_length_scope"),
        ("A" * 109, "outside_provisional_length_scope"),
        ("A" * 110, "outside_provisional_length_scope"),
    ],
)
def test_sequence_scope_retains_incompatible_original(sequence, reason):
    item = prepare_sequences([SequenceRecord(sequence)])[0]
    assert item.proposal.sequence == sequence
    assert reason in item.issues
    assert item.provider_sequence is None


def test_scope_does_not_invent_a_lower_length_cutoff_or_chemical_realization():
    for sequence in ("A", "AC", "A" * 99, "ACM"):
        item = prepare_sequences([sequence])[0]
        assert item.provider_sequence == sequence
        assert not item.proposal.chemistry
    chemistry = {"cyclization": "head-to-tail", "stereochemistry": ["D", "L"]}
    context = {"target": "unused target context", "unknowns": ["termini"]}
    proposal = SequenceRecord("ACD", chemistry=chemistry, context=context)
    chemistry["stereochemistry"].append("L")
    context["unknowns"].clear()
    assert proposal.chemistry["stereochemistry"] == ("D", "L")
    assert proposal.context["unknowns"] == ("termini",)
    assert prepare_sequences([proposal])[0].issues == ("unassessed_explicit_chemistry",)
    with pytest.raises(TypeError):
        proposal.context["target"] = "changed"


@pytest.mark.parametrize("records", ["ACD", b"ACD", {"sequence": "ACD"}, [12]])
def test_wrong_record_shapes_are_not_silently_coerced(records):
    with pytest.raises(TypeError):
        prepare_sequences(records)


def test_reordered_rows_map_by_occurrence_and_keep_native_negatives_and_extra_columns():
    rows = (row("input-1", amp=0.4, hemo=0.1, extra={"native": [1, 2]}), row("input-0"))
    snapshot = result(rows, ("ACD", "ACD"))
    assert [o.row_index for o in snapshot.outcomes] == [1, 0]
    assert select(snapshot, policy="hemolysis-first", k=2).selected == (
        "input-1",
        "input-0",
    )
    assert snapshot.rows[0].values["is_AMP"] is False
    assert snapshot.rows[0].values["extra"]["native"] == (1, 2)


def test_duplicate_missing_extra_and_incompatible_rows_cannot_acquire_another_score():
    snapshot = result(
        (
            row("input-0"),
            row("input-0"),
            row("unknown"),
            row("input-3"),
            row("input-4", sequence="MACD"),
        ),
        ("ACD", "ACD", "ACD", "ACD", "MACD"),
    )
    assert snapshot.anomalies == (
        (0, "duplicate_provider_rows"),
        (1, "duplicate_provider_rows"),
        (2, "unknown_provider_token"),
    )
    assert snapshot.outcomes[0].row_index is None
    assert snapshot.outcomes[1].issues == ("missing_provider_row",)
    choice = select(snapshot, policy="amp-first", k=20)
    assert choice.selected == ("input-3",)
    assert len(choice.excluded) == 4
    assert len(snapshot.rows) == 5


@pytest.mark.parametrize(
    "changes,reason",
    [
        ({"Sequence": "AD"}, "changed_sequence_view"),
        ({"AMP_probability": float("nan")}, "invalid_score:AMP_probability"),
        ({"AMP_probability": float("inf")}, "invalid_score:AMP_probability"),
        ({"Hemolytic_probability": -0.1}, "invalid_score:Hemolytic_probability"),
        ({"AMP_probability": 1.01}, "invalid_score:AMP_probability"),
        ({"AMP_probability": 10**1000}, "invalid_score:AMP_probability"),
        ({"AMP_probability": True}, "invalid_score:AMP_probability"),
        ({"AMP_probability": "0.9"}, "invalid_score:AMP_probability"),
        ({"is_AMP": 1}, "inconsistent_label:is_AMP"),
        ({"is_AMP": False}, "inconsistent_label:is_AMP"),
        ({"Hemolytic": "Hemo"}, "inconsistent_label:Hemolytic"),
        ({"AMP_family": "activity"}, "invalid_composition_category"),
    ],
)
def test_invalid_outputs_are_retained_with_explicit_exclusion(changes, reason):
    native_row = row("input-0", **changes)
    snapshot = result((native_row,))
    assert reason in snapshot.outcomes[0].issues
    assert snapshot.rows[0] is native_row
    assert not select(snapshot, policy="amp-first", k=1).ranking


def test_missing_head_stays_missing_and_exact_point_five_uses_native_strict_rule():
    values = dict(row("input-0").values)
    del values["Hemolytic_probability"]
    snapshot = result((ProviderRow("input-0", values),))
    assert "missing_field:Hemolytic_probability" in snapshot.outcomes[0].issues
    exact = result((row("input-0", amp=0.5, hemo=0.5),))
    assert exact.outcomes[0].eligible
    assert exact.rows[0].values["is_AMP"] is False
    assert exact.rows[0].values["Hemolytic"] == "NonHemo"


def test_approved_d35_toy_fixture_and_two_policies_do_not_rewrite_evidence():
    rows = tuple(
        row(f"input-{i}", amp=amp, hemo=hemo)
        for i, (amp, hemo) in enumerate(
            ((0.9, 0.8), (0.4, 0.1), (0.9, 0.2), (0.9, 0.2))
        )
    )
    incomplete = dict(row("input-4", amp=0.95).values)
    del incomplete["Hemolytic_probability"]
    snapshot = result((*rows, ProviderRow("input-4", incomplete)), ("ACD",) * 5)
    before = snapshot.to_json()
    amp = select(snapshot, policy="amp-first", k=2)
    hemo = select(snapshot, policy="hemolysis-first", k=2)
    assert amp.ranking == ("input-2", "input-3", "input-0", "input-1")
    assert amp.selected == ("input-2", "input-3")
    assert hemo.ranking == ("input-1", "input-2", "input-3", "input-0")
    assert hemo.selected == ("input-1", "input-2")
    assert amp.unselected == ("input-0", "input-1")
    assert amp.excluded[0][0] == "input-4"
    assert select(snapshot, policy="amp-first", k=0).ranking == amp.ranking
    assert select(snapshot, policy="amp-first", k=0).selected == ()
    assert snapshot.to_json() == before
    assert amp.snapshot_id == snapshot.snapshot_id
    assert amp.provenance.evidence_kind == "controlled-fixture"


@pytest.mark.parametrize("k", [True, 1.0, "1", None])
def test_count_does_not_accept_boolean_or_coercion(k):
    with pytest.raises(TypeError):
        select(result(), policy="amp-first", k=k)


def test_invalid_policy_and_negative_count_fail_explicitly():
    with pytest.raises(ValueError, match="nonnegative"):
        select(result(), policy="amp-first", k=-1)
    with pytest.raises(ValueError, match="policy"):
        select(result(), policy="unapproved", k=1)


@pytest.mark.parametrize(
    "cause",
    [
        "unavailable_provider",
        "missing_assets",
        "load_failure",
        "feature_failure",
        "scoring_failure",
        "timeout",
    ],
)
def test_reported_failures_are_not_negative_predictions(cause):
    snapshot = result(failures={"input-0": cause})
    assert snapshot.outcomes[0].issues == (f"reported_failure:{cause}",)
    assert not snapshot.rows
    assert not select(snapshot, policy="amp-first", k=1).selected


def test_empty_and_all_incompatible_pools_and_unqualified_evidence():
    assert not select(result(sequences=()), policy="amp-first", k=1).ranking
    snapshot = result(sequences=("MACD", "", "ACD*"))
    assert len(select(snapshot, policy="amp-first", k=1).excluded) == 3
    unqualified = result(
        (row("input-0"),), provenance=fixture_provenance(evidence_kind="imported")
    )
    assert "unqualified_bundle" in unqualified.outcomes[0].issues
    imported = result(
        (row("input-0"),),
        provenance=fixture_provenance(
            evidence_kind="imported",
            qualification_reference="caller-supplied-reference",
        ),
    )
    assert imported.outcomes[0].eligible


def test_results_roundtrip_preserves_floats_originals_native_dtypes_and_anomalies():
    amp, hemo = math.nextafter(0.5, 1.0), math.nextafter(0.2, 0.0)
    inputs = prepare_sequences(
        parse_fasta(">same full header\r\nACD\r\n>same full header\nACD\n")
    )
    snapshot = result(
        (
            row("input-1", amp=amp, hemo=hemo),
            row("input-0"),
            row("unknown", amp=float("nan"), tag={"float_hex": "not a float"}),
        ),
        inputs=inputs,
        provenance=fixture_provenance(
            details={
                "dtypes": {"AMP_probability": "controlled float64"},
                "source": "invented",
                "provider_executed": False,
            }
        ),
    )
    restored = ResultSet.from_json(snapshot.to_json())
    assert restored.inputs == snapshot.inputs
    assert restored.rows[0].values["AMP_probability"].hex() == amp.hex()
    assert restored.rows[0].values["Hemolytic_probability"].hex() == hemo.hex()
    assert restored.provenance == snapshot.provenance
    assert restored.anomalies == snapshot.anomalies
    assert math.isnan(restored.rows[2].values["AMP_probability"])
    assert restored.rows[2].values["tag"]["float_hex"] == "not a float"
    for policy in ("amp-first", "hemolysis-first"):
        assert select(restored, policy=policy, k=2) == select(
            snapshot, policy=policy, k=2
        )
    json.loads(snapshot.to_json(), parse_constant=lambda value: pytest.fail(value))


def test_saved_data_cannot_replace_eligibility_or_original_occurrence_order():
    snapshot = result((row("input-0", Sequence="AD"),))
    restored = ResultSet.from_json(snapshot.to_json())
    assert "changed_sequence_view" in restored.outcomes[0].issues
    with pytest.raises(ValueError, match="original occurrence order"):
        result(inputs=(InputRecord(1, SequenceRecord("ACD")),))
    with pytest.raises(ValueError, match="unknown input"):
        result(failures={"wrong": "timeout"})
    with pytest.raises(ValueError, match="schema"):
        ResultSet.from_json('{"schema":"unknown", "data":null}')
    with pytest.raises(ValueError, match="Duplicate JSON key"):
        ResultSet.from_json('{"schema":"a", "schema":"b", "data":null}')


def test_core_import_and_saved_result_selection_with_macrel_import_blocked():
    saved = result((row("input-0"),)).to_json()
    code = """
import importlib.abc
import sys
class NoMacrel(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname == "macrel" or fullname.startswith("macrel."):
            raise AssertionError("W1 attempted a Macrel import")
sys.meta_path.insert(0, NoMacrel())
from peptidemt import ResultSet, select
results = ResultSet.from_json(sys.stdin.read())
assert select(results, policy="amp-first", k=1).selected == ("input-0",)
assert not any(n == "macrel" or n.startswith("macrel.") for n in sys.modules)
"""
    completed = subprocess.run(
        [sys.executable, "-c", code], input=saved, text=True, capture_output=True
    )
    assert completed.returncode == 0, completed.stdout + completed.stderr
