"""Finite source/chemistry/observation protection; synthetic data, no networks."""

import copy
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "historical_data_tool", ROOT / "devtools/hydramp_historical_data.py"
)
tool = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(tool)


def encode(value):
    return json.dumps(value, ensure_ascii=False, indent=2).encode()


def digest(value):
    return hashlib.sha256(value).hexdigest()


@pytest.fixture
def data(tmp_path, monkeypatch):
    # Three deliberately artificial observations, not an approved real cohort.
    originals, rows = [], []
    for table, index, name, sequence, value in [
        ("Tab1", 1, "synthetic-a", "ACD", "4"),
        ("Tab1", 2, "synthetic-b", "MNP", ">512"),
        ("Tab2", 3, "synthetic-a", "ACD", "16"),
    ]:
        seqhash = digest(sequence.encode())
        cells = [str(index), name, sequence] + [""] * (3 if table == "Tab1" else 11)
        column = 5 if table == "Tab1" else 6
        cells[column] = value
        overlap = ["synthetic-pool"] if name == "synthetic-a" else []
        originals.append(
            {
                "source_table": table,
                "xml_row_index": index,
                "source_id": str(index),
                "source_name": name,
                "raw_cells": cells,
                "raw_sequence_sha256": seqhash,
                "length": len(sequence),
                "chemistry": {"c_terminus": "amide"},
                "sequence_only_issues": [],
                "annotated_record_issues": ["unassessed_explicit_chemistry"],
                "raw_exact_overlap_members": overlap,
            }
        )
        rows.append(
            {
                "source_occurrence_id": f"hydramp2023:{table}:xml-tr-{index}",
                "source_table": table,
                "xml_row_index": index,
                "raw_source_id": str(index),
                "source_name": name,
                "sequence_sha256": seqhash,
                "sequence_length": len(sequence),
                "chemical_entity_evidence": {
                    "c_terminus": {
                        "value": "amide",
                        "evidence": "HydrAMP main article peptide-synthesis Methods",
                    },
                    "other_required_fields": "unresolved at this audit; no complete entity identity assigned",
                },
                "proposed_model_view": {
                    "state": "review_proposal_only_not_constructed_or_submitted",
                    "residue_string_sha256_if_approved": seqhash,
                    "sequence_change_allowed": False,
                    "chemistry_erasure_from_source_allowed": False,
                    "chemical_equivalence_claimed": False,
                    "known_omitted_feature": "C-terminal amide is not encoded by the native residue-token input",
                    "current_annotated_consumer_issues": [
                        "unassessed_explicit_chemistry"
                    ],
                },
                "proposed_assay_scope": {
                    "organism": "E. coli",
                    "strain": "ATCC 25922",
                    "endpoint": "MIC",
                    "unit_as_reported": "µg/mL",
                    "source_cell_index": column,
                    "raw_value": value,
                    "comparator": ">" if value.startswith(">") else "=",
                    "reported_numeric_text": value.lstrip(">"),
                    "class_label": None,
                    "new_unit_conversion": False,
                    "strain_scope_status": "proposal; no selection outcome or model score used",
                },
                "raw_published_pool_overlap_members": overlap,
                "checkpoint_fitting_or_model_selection_exposure": "unresolved",
                "independent_test_member": False,
            }
        )
    source = {
        "schema": "peptidemt.hydramp_C0_measured_panel@1",
        "hydramps_original_measured_tables": {"records": originals},
    }
    review = {
        "schema": "peptidemt.hydramp_historical_view_preparation@1",
        "source": {"sha256": digest(encode(source))},
        "occurrences": rows,
        "totals": {
            "table_occurrences": 3,
            "distinct_raw_strings": 2,
            "table_occurrences_by_table": {"Tab1": 2, "Tab2": 1},
            "raw_MIC_comparators": {"=": 2, ">": 1},
            "repeated_strings_with_different_table_observations": 1,
            "exact_published_pool_overlap_distinct_strings": 1,
            "current_annotated_consumer_compatible_occurrences": 0,
            "independent_test_members_qualified": 0,
        },
        "repeated_sequence_observations": [
            {
                "sequence_sha256": rows[0]["sequence_sha256"],
                "source_names": ["synthetic-a", "synthetic-a"],
                "source_occurrence_ids": [
                    rows[0]["source_occurrence_id"],
                    rows[2]["source_occurrence_id"],
                ],
                "raw_MIC_values_ug_per_mL": ["4", "16"],
                "distinct_reported_values": 2,
                "interpretation": "distinct table observations; no averaged, minimum, preferred, independent-replicate or corrected label assigned",
            }
        ],
    }
    auth = {
        "schema": "peptidemt.hydramp_historical_view_authorization@1",
        "decision": "D46",
        "approved": {"finite_synthetic_test_only": True},
        "additional_permissions": {"native_execution": False},
        "original_review_manifest": {"sha256": digest(encode(review))},
    }
    values = {"authorization": auth, "review": review, "source": source}
    paths = {}
    for role, value in values.items():
        paths[role] = tmp_path / f"{role}.json"
        paths[role].write_bytes(encode(value))
    pins = {role: digest(path.read_bytes()) for role, path in paths.items()}
    # A private test replacement only. No CLI/profile override exists.
    monkeypatch.setattr(tool, "_PINS", pins)
    return values, paths, pins


def test_retains_all_observations_chemistry_unknowns_and_bounds(data, tmp_path):
    values, paths, _ = data
    original_bytes = {k: p.read_bytes() for k, p in paths.items()}
    snapshot = tool.receive(**paths)
    report = tool.inspect(snapshot)
    assert report["observations"] == values["review"]["occurrences"]
    assert report["counts"]["table_occurrences"] == 3
    assert report["counts"]["distinct_raw_strings"] == 2
    assert report["repeated_sequence_observations"][0]["raw_MIC_values_ug_per_mL"] == [
        "4",
        "16",
    ]
    assert report["observations"][1]["proposed_assay_scope"]["raw_value"] == ">512"
    assert report["observations"][1]["sequence_length"] == 3  # initial M retained
    assert report["current_authority"]["native_execution_authorized"] is False
    assert report["model_payloads_or_calls"] == 0
    assert {k: p.read_bytes() for k, p in paths.items()} == original_bytes
    saved = tmp_path / "saved.json"
    tool.save(snapshot, saved)
    for path in paths.values():
        path.unlink()
    assert tool.inspect(tool.load(saved)) == report
    # Returned inspection dictionaries cannot mutate saved original JSON texts.
    report["observations"][0]["chemical_entity_evidence"].clear()
    assert (
        tool.inspect(tool.load(saved))["observations"]
        == values["review"]["occurrences"]
    )


@pytest.mark.parametrize("role", ["authorization", "review", "source"])
def test_mutated_approval_or_source_cannot_be_reapproved_by_input_metadata(data, role):
    _, paths, _ = data
    paths[role].write_bytes(paths[role].read_bytes() + b"\n")
    with pytest.raises(tool.HistoricalDataError) as error:
        tool.receive(**paths)
    assert error.value.code == "source_digest"


@pytest.mark.parametrize(
    "mutation,code",
    [
        ("remove_occurrence", "occurrence_order"),
        ("reorder", "occurrence_order"),
        ("foreign_id", "occurrence_order"),
        ("erase_amide", "chemistry_changed"),
        ("NME", "chemistry_changed"),
        ("invent_identity", "chemistry_changed"),
        ("clip_M", "sequence_changed"),
        ("truncate", "sequence_changed"),
        ("permit_projection", "view_changed"),
        ("drop_overlap", "exposure_changed"),
        ("clean_independence", "exposure_changed"),
        ("exact_bound", "assay_value"),
        ("minimum_value", "assay_value"),
        ("average_repeats", "observation_summary"),
        ("native_class", "invented_label"),
        ("molar_unit", "assay_scope"),
        ("other_strain", "assay_scope"),
        ("payload_field", "record_fields"),
    ],
)
def test_scientific_mutations_have_explicit_causes(data, mutation, code):
    values, _, _ = data
    review = copy.deepcopy(values["review"])
    rows = review["occurrences"]
    if mutation == "remove_occurrence":
        rows.pop()
    elif mutation == "reorder":
        rows.reverse()
    elif mutation == "foreign_id":
        rows[0]["source_occurrence_id"] = "foreign"
    elif mutation == "erase_amide":
        rows[0]["chemical_entity_evidence"] = {}
    elif mutation == "NME":
        rows[0]["chemical_entity_evidence"]["c_terminus"]["value"] = "NME"
    elif mutation == "invent_identity":
        rows[0]["chemical_entity_evidence"]["other_required_fields"] = "complete"
    elif mutation in ("clip_M", "truncate"):
        rows[1 if mutation == "clip_M" else 0]["sequence_sha256"] = digest(
            b"NP" if mutation == "clip_M" else b"AC"
        )
    elif mutation == "permit_projection":
        rows[0]["proposed_model_view"]["chemistry_erasure_from_source_allowed"] = True
    elif mutation == "drop_overlap":
        rows[0]["raw_published_pool_overlap_members"] = []
    elif mutation == "clean_independence":
        rows[0]["independent_test_member"] = True
    elif mutation == "exact_bound":
        rows[1]["proposed_assay_scope"].update(raw_value="512", comparator="=")
    elif mutation == "minimum_value":
        rows[2]["proposed_assay_scope"].update(raw_value="4", reported_numeric_text="4")
    elif mutation == "average_repeats":
        review["repeated_sequence_observations"][0]["raw_MIC_values_ug_per_mL"] = ["10"]
    elif mutation == "native_class":
        rows[0]["proposed_assay_scope"]["class_label"] = 1
    elif mutation == "molar_unit":
        rows[0]["proposed_assay_scope"]["unit_as_reported"] = "µM"
    elif mutation == "other_strain":
        rows[0]["proposed_assay_scope"]["strain"] = "ATCC 43827"
    elif mutation == "payload_field":
        rows[0]["native_tokens"] = [1, 2, 3]
    with pytest.raises(tool.HistoricalDataError) as error:
        tool._validate_records(review, values["source"])
    assert error.value.code == code


def test_empty_historical_fixture_is_not_successful_empty_result(data):
    values, _, _ = data
    values["source"]["hydramps_original_measured_tables"]["records"] = []
    values["review"]["occurrences"] = []
    with pytest.raises(tool.HistoricalDataError) as error:
        tool._validate_records(values["review"], values["source"])
    assert error.value.code == "empty_source"


@pytest.mark.parametrize(
    "text,code",
    [
        ('{"a":1,"a":2}', "duplicate_key"),
        ('{"a":NaN}', "nonfinite_json"),
        ('{"a":Infinity}', "nonfinite_json"),
        ('{"a":1e309}', "nonfinite_json"),
        ("{", "invalid_json"),
    ],
)
def test_json_does_not_silently_overwrite_or_accept_nonfinite_data(text, code):
    with pytest.raises(tool.HistoricalDataError) as error:
        tool._parse(text)
    assert error.value.code == code


@pytest.mark.parametrize(
    "change,code",
    [
        ("cached_success", "snapshot_fields"),
        ("profile", "snapshot_profile"),
        ("inputs", "input_roles"),
    ],
)
def test_saved_verdict_or_profile_cannot_bypass_revalidation(data, change, code):
    _, paths, _ = data
    snapshot = tool.receive(**paths)
    if change == "cached_success":
        snapshot["success"] = True
    elif change == "profile":
        snapshot["profile"] = "another-dataset"
    else:
        del snapshot["source_json"]["review"]
    with pytest.raises(tool.HistoricalDataError) as error:
        tool.inspect(snapshot)
    assert error.value.code == code


def test_saved_source_changes_are_rejected(data):
    _, paths, _ = data
    snapshot = tool.receive(**paths)
    snapshot["source_json"]["review"] += "\n"
    with pytest.raises(tool.HistoricalDataError) as error:
        tool.inspect(snapshot)
    assert error.value.code == "source_digest"


def test_saved_lone_surrogate_is_an_explicit_text_rejection(data):
    _, paths, _ = data
    snapshot = tool.receive(**paths)
    snapshot["source_json"]["review"] = "\ud800"
    with pytest.raises(tool.HistoricalDataError) as error:
        tool.inspect(snapshot)
    assert error.value.code == "invalid_utf8"


def test_no_overwrite_and_no_parameter_file_read(data, tmp_path, monkeypatch):
    _, paths, _ = data
    snapshot = tool.receive(**paths)
    saved = tmp_path / "saved.json"
    saved.write_text("human work")
    with pytest.raises(FileExistsError):
        tool.save(snapshot, saved)
    assert saved.read_text() == "human work"

    def forbidden(*args, **kwargs):
        pytest.fail("Parameter file opened")

    monkeypatch.setattr(Path, "open", forbidden)
    with pytest.raises(tool.HistoricalDataError) as error:
        tool._read(tmp_path / "weights.pt")
    assert error.value.code == "input_form"


def test_input_size_is_bounded(tmp_path):
    path = tmp_path / "large.json"
    path.write_bytes(b" " * (tool._LIMIT + 1))
    with pytest.raises(tool.HistoricalDataError) as error:
        tool._read(path)
    assert error.value.code == "input_size"


def test_cli_receive_replay_and_rejection(data, tmp_path, capsys):
    _, paths, _ = data
    saved = tmp_path / "saved.json"
    argv = ["receive", "--output", str(saved)]
    for role, path in paths.items():
        argv.extend(["--" + role, str(path)])
    assert tool.main(argv) == 0
    first = json.loads(capsys.readouterr().out)
    assert tool.main(["inspect", str(saved)]) == 0
    assert json.loads(capsys.readouterr().out) == first
    paths["review"].write_text("{}")
    failed = tmp_path / "must-not-exist.json"
    argv[argv.index(str(saved))] = str(failed)
    assert tool.main(argv) == 2
    assert json.loads(capsys.readouterr().err)["code"] == "source_digest"
    assert not failed.exists()
    with pytest.raises(SystemExit) as error:
        tool.main(["execute"])
    assert error.value.code == 2


def test_public_chemistry_admission_remains_rejected():
    from peptidemt import InputRecord, SequenceRecord, analogue_input_issues

    record = InputRecord(0, SequenceRecord("ACD", chemistry={"c_terminus": "amide"}))
    assert "unassessed_explicit_chemistry" in record.issues
    assert analogue_input_issues(record) == ("unassessed_explicit_chemistry",)


def test_fresh_receiver_and_replay_under_model_file_network_dispatch_guards(
    data, tmp_path
):
    _, paths, pins = data
    program = r"""
import importlib.abc,importlib.util,json,pathlib,sys
blocked={'torch','tensorflow','keras','onnxruntime','hydramp_torch','amp','molsysmt','macrel'}
class Guard(importlib.abc.MetaPathFinder):
    def find_spec(self,fullname,path=None,target=None):
        if fullname.split('.')[0] in blocked: raise AssertionError('engine import: '+fullname)
sys.meta_path.insert(0,Guard())
def audit(event,args):
    if event in ('subprocess.Popen','socket.connect','socket.connect_ex'): raise AssertionError(event)
    if event=='open' and isinstance(args[0],str) and args[0].endswith(('.h5','.pkl','.pt','.npz','.onnx')): raise AssertionError('parameter read')
sys.addaudithook(audit)
spec=importlib.util.spec_from_file_location('guarded_historical',sys.argv[1])
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
module._PINS=json.loads(sys.argv[2]) # private synthetic test binding, not a CLI feature
paths=json.loads(sys.argv[3]);snapshot=module.receive(**paths)
saved=pathlib.Path(sys.argv[4]);module.save(snapshot,saved)
first=module.inspect(snapshot)
for path in paths.values():pathlib.Path(path).unlink()
assert module.inspect(module.load(saved))==first
assert not blocked & {name.split('.')[0] for name in sys.modules}
print(json.dumps({'guarded':True,'model_calls':0,'original_sources_deleted_before_replay':True}))
"""
    completed = subprocess.run(
        [
            sys.executable,
            "-I",
            "-B",
            "-c",
            program,
            str(Path(tool.__file__)),
            json.dumps(pins),
            json.dumps({k: str(p) for k, p in paths.items()}),
            str(tmp_path / "guarded.json"),
        ],
        capture_output=True,
        text=True,
        timeout=20,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr
    assert json.loads(completed.stdout) == {
        "guarded": True,
        "model_calls": 0,
        "original_sources_deleted_before_replay": True,
    }
