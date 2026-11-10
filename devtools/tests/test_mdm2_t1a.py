"""Artificial failure controls for D53; fixtures are not experimental peptides."""

import base64
import copy
import importlib.util
import json
from pathlib import Path

import pytest
from pyunitwizard.record import RecordError

spec = importlib.util.spec_from_file_location(
    "mdm2_t1a_case", Path(__file__).parents[1] / "mdm2_t1a.py"
)
case = importlib.util.module_from_spec(spec)
spec.loader.exec_module(case)


def artificial_source():
    """HTML presentation fixture, deliberately not the admitted article hash."""

    def table(name):
        rows = [
            ["Peptide Sequence", name + "-MDM2", name + "-MDMX"],
            [""],
            ["Kd (M)", "Kd ratio", "energy", "Kd (M)", "Kd ratio", "energy"],
        ]
        for i in range(3, 22):
            if i == 16:
                rows.append([""])
                continue
            cells = ["source-token"] * 12 + [
                "1.2±0.3E-09",
                "not-reinterpreted",
                "raw",
                "4.5±0.6E-09",
                "not-reinterpreted",
                "raw",
            ]
            if name == "P53" and i in (6, 10):
                cells[12] = cells[15] = "n.d.a\n"
            rows.append(cells)
        return (
            "<table>"
            + "".join(
                "<tr>" + "".join("<td>" + c + "</td>" for c in r) + "</tr>"
                for r in rows
            )
            + "</table>"
        )

    return (
        "<p id='P7'>At least three independent measurements</p>"
        "<p id='P39'>Uninterpreted synthesis context</p>"
        "<p id='P40'>Uninterpreted assay context</p>"
        + table("PMI")
        + "<table><tr><td>Other article table</td></tr></table>"
        + table("P53")
    ).encode()


@pytest.fixture(scope="module")
def artificial_reference():
    raw = artificial_source()
    result = case.transcribe(raw, pinned=False)
    result.update(
        schema=case.SCHEMA,
        source_sha256=case.digest(raw),
        source_html_base64=base64.b64encode(raw).decode(),
        approved_proposal_sha256=case.PROPOSAL_SHA,
        authorization_sha256=case.AUTH_SHA,
        producer={"scope": "artificial control only"},
    )
    result["source_acquisition"] = {
        "sha256": case.digest(raw),
        "bytes": len(raw),
        "status": "artificial provenance only",
    }
    result["source_acquisition_text"] = json.dumps(result["source_acquisition"])
    case.encode_measurements(result)
    return result


def test_shared_exponent_and_source_precision():
    result = case.stated_measurement("3.2±1.1E-09")
    assert result["kd_decimal"] == "3.2E-9"
    assert result["sd_decimal"] == "1.1E-9"
    assert case.stated_measurement("n.d.a\n")["kd_decimal"] is None


@pytest.mark.parametrize(
    "token", ["0±1E-09", "3.2", "NaN", "-3±1E-09", "3±-1E-09", "n.d."]
)
def test_unsupported_or_invalid_measurement_refused(token):
    with pytest.raises(case.EvidenceError):
        case.stated_measurement(token)


def test_artificial_population_and_aliases(artificial_reference):
    report = case.validate(artificial_reference, pinned=False)
    assert report["source_occurrences"] == 72
    assert report["reported_peptide_target_evidence"] == 70
    assert report["quantified"] == 66
    assert report["not_quantified"] == 4
    assert report["duplicate_display_occurrences"] == 2
    # No chemical alphabet, identity or equivalence is inferred from the tokens.
    assert (
        artificial_reference["occurrences"][0]["literal_sequence_display"]
        == "source-token" * 12
    )
    assert report["chemical_identity_qualified"] is False


@pytest.mark.parametrize(
    "mutation", ["duplicate", "target", "missing_row", "chemistry", "n", "nd_numeric"]
)
def test_source_semantics_cannot_be_promoted_or_lost(artificial_reference, mutation):
    result = copy.deepcopy(artificial_reference)
    if mutation == "duplicate":
        result["reported_evidence"].append(
            copy.deepcopy(result["reported_evidence"][0])
        )
    elif mutation == "target":
        result["reported_evidence"][0]["measurement_record"] = result[
            "reported_evidence"
        ][1]["measurement_record"]
    elif mutation == "missing_row":
        result["occurrences"].pop()
    elif mutation == "chemistry":
        result["occurrences"][0]["chemical_identity"]["c_terminus"] = "amide"
    elif mutation == "n":
        result["occurrences"][0]["replicate_n"] = 3
    else:
        row = next(
            x for x in result["reported_evidence"] if x["measurement_record"] is None
        )
        row["measurement_record"] = copy.deepcopy(
            result["reported_evidence"][0]["measurement_record"]
        )
    with pytest.raises((case.EvidenceError, RecordError)):
        case.validate(result, pinned=False)


def test_valid_owner_record_with_wrong_dimension_refused(artificial_reference):
    puw, measurement = case.quantities()
    result = copy.deepcopy(artificial_reference)
    row = result["reported_evidence"][0]
    row["measurement_record"] = measurement.from_quantity(
        puw.quantity(1.2e-9, "nm", form="pint"),
        kind="sd",
        half_width=puw.quantity(0.3e-9, "nm", form="pint"),
        field=row["evidence_id"] + ".kd",
    ).to_dict()
    with pytest.raises(RecordError):
        case.validate(result, pinned=False)


def test_changed_quantity_seal_refused(artificial_reference):
    result = copy.deepcopy(artificial_reference)
    result["reported_evidence"][0]["measurement_record"]["metadata"]["kind"] = "sem"
    with pytest.raises(RecordError):
        case.validate(result, pinned=False)


def test_source_pin_is_not_overridable_by_the_fixture():
    with pytest.raises(case.EvidenceError, match="Unreviewed source"):
        case.transcribe(artificial_source())


def test_changed_unit_headers_and_missing_source_row_refused():
    raw = artificial_source()
    for changed in (
        raw.replace(b"Kd (M)", b"Kd (nM)"),
        raw.replace(b"<tr><td>source-token", b"<tr><td>lost</td><td>source-token", 1),
    ):
        with pytest.raises(case.EvidenceError):
            case.transcribe(changed, pinned=False)


def test_record_codec_is_independent_of_application_unit_policy(artificial_reference):
    puw, _ = case.quantities()
    with puw.context(standard_units=["nanomolar", "angstrom", "fs"]):
        before = puw.configure.report()["standard_units"]
        assert case.validate(artificial_reference, pinned=False)["quantified"] == 66
        assert puw.configure.report()["standard_units"] == before


def test_duplicate_saved_json_key_refused(tmp_path):
    path = tmp_path / "duplicate.json"
    path.write_text('{"schema": "one", "schema": "two"}')
    with pytest.raises(case.EvidenceError, match="Duplicate"):
        case.read_saved(path)


def test_saved_json_nonfinite_refused(tmp_path):
    path = tmp_path / "invalid.json"
    path.write_text(json.dumps({"value": float("nan")}))
    with pytest.raises(case.EvidenceError, match="Nonfinite"):
        case.read_saved(path)


def test_lost_acquisition_provenance_refused(artificial_reference):
    result = copy.deepcopy(artificial_reference)
    del result["source_acquisition_text"]
    with pytest.raises(case.EvidenceError, match="acquisition"):
        case.validate(result, pinned=False)
