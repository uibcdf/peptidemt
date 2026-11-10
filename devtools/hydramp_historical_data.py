"""Receive/replay the finite D46 historical data; no model or molecular operations.

Developer-side, deliberately pinned to one reviewed source set. There is no
profile override, native input preparation, engine loader or execution command.
Snapshots retain the exact original JSON texts so saved replay needs no sources.
"""

import argparse
import hashlib
import json
import math
import sys
from collections import Counter, defaultdict
from pathlib import Path

_SCHEMA = "peptidemt.hydramp_historical_data@1"
_PROFILE = "D46-historical-ATCC25922"
_LIMIT = 2 * 1024 * 1024
_PINS = {
    "authorization": "aaad0147790da3af47ca1703e2ce117150126d832062975959d6025f7a86f4a6",
    "review": "e14fd7272e4894bb34cc4afe64ef8422c91474ace0c73cc201ea2e64fd5c049e",
    "source": "ae1ac16ad7f47f571a21a54dc4a45c3a3d7f1b0dae3e3eb62e6c8ccfc1eec9db",
}


class HistoricalDataError(ValueError):
    """A rejected finite-source record, with an actionable cause code."""

    def __init__(self, code, detail):
        self.code = code
        super().__init__(detail)


def _require(condition, code, detail):
    if not condition:
        raise HistoricalDataError(code, detail)


def _digest(data):
    return hashlib.sha256(data).hexdigest()


def _read(path):
    path = Path(path)
    _require(path.resolve().suffix.lower() == ".json", "input_form", "JSON only")
    with path.open("rb") as stream:
        data = stream.read(_LIMIT + 1)
    _require(len(data) <= _LIMIT, "input_size", "JSON exceeds the 2 MiB limit")
    return data


def _parse(text):
    def pairs(items):
        result = {}
        for key, value in items:
            _require(key not in result, "duplicate_key", f"Duplicate JSON key: {key}")
            result[key] = value
        return result

    def constant(value):
        raise HistoricalDataError("nonfinite_json", f"Nonfinite JSON: {value}")

    def floating(value):
        number = float(value)
        _require(math.isfinite(number), "nonfinite_json", "Nonfinite JSON number")
        return number

    try:
        return json.loads(
            text, object_pairs_hook=pairs, parse_constant=constant, parse_float=floating
        )
    except (UnicodeError, json.JSONDecodeError, RecursionError) as error:
        raise HistoricalDataError("invalid_json", str(error)) from error


def _validate_records(review, source):
    """Check scientific correspondence after the public digest boundary.

    Pure, private validation also permits minimal synthetic test controls.
    Public receive/replay always checks the fixed D46 digests first.
    """
    originals = source["hydramps_original_measured_tables"]["records"]
    rows = review["occurrences"]
    _require(
        type(originals) is list and type(rows) is list and bool(originals),
        "empty_source",
        "A finite nonempty historical source is required",
    )
    ids = [
        f"hydramp2023:{r['source_table']}:xml-tr-{r['xml_row_index']}"
        for r in originals
    ]
    actual_ids = [r["source_occurrence_id"] for r in rows]
    _require(
        actual_ids == ids and len(set(ids)) == len(ids),
        "occurrence_order",
        "Source occurrences must match exactly, in order",
    )
    groups = defaultdict(list)
    for row, original in zip(rows, originals, strict=True):
        table = original["source_table"]
        _require(table in ("Tab1", "Tab2"), "table_scope", "Unreviewed source table")
        cells = original["raw_cells"]
        column = 5 if table == "Tab1" else 6
        _require(
            len(cells) == (6 if table == "Tab1" else 14),
            "source_columns",
            "Changed source columns",
        )
        sequence = cells[2]
        digest = _digest(sequence.encode("utf-8"))
        _require(
            row["sequence_sha256"] == original["raw_sequence_sha256"] == digest
            and row["sequence_length"] == original["length"] == len(sequence),
            "sequence_changed",
            "Original residue string/hash/length changed",
        )
        _require(
            row["source_table"] == table
            and row["xml_row_index"] == original["xml_row_index"]
            and row["source_name"] == original["source_name"]
            and row["raw_source_id"] == original["source_id"],
            "source_identity",
            "Source table/row/name changed",
        )
        _require(
            original["chemistry"] == {"c_terminus": "amide"}
            and original["sequence_only_issues"] == []
            and original["annotated_record_issues"]
            == ["unassessed_explicit_chemistry"],
            "source_chemistry",
            "Source chemistry/admission evidence changed",
        )
        chemistry = {
            "c_terminus": {
                "value": "amide",
                "evidence": "HydrAMP main article peptide-synthesis Methods",
            },
            "other_required_fields": "unresolved at this audit; no complete entity identity assigned",
        }
        _require(
            row["chemical_entity_evidence"] == chemistry,
            "chemistry_changed",
            "Keep primary amide and unresolved identity; no NME or annotation erasure",
        )
        expected_view = {
            "state": "review_proposal_only_not_constructed_or_submitted",
            "residue_string_sha256_if_approved": digest,
            "sequence_change_allowed": False,
            "chemistry_erasure_from_source_allowed": False,
            "chemical_equivalence_claimed": False,
            "known_omitted_feature": "C-terminal amide is not encoded by the native residue-token input",
            "current_annotated_consumer_issues": ["unassessed_explicit_chemistry"],
        }
        _require(
            row["proposed_model_view"] == expected_view,
            "view_changed",
            "Historical view/omission evidence changed; no model payload",
        )
        assay = row["proposed_assay_scope"]
        _require(
            (
                assay["organism"],
                assay["strain"],
                assay["endpoint"],
                assay["unit_as_reported"],
                assay["source_cell_index"],
            )
            == ("E. coli", "ATCC 25922", "MIC", "µg/mL", column),
            "assay_scope",
            "Only the reviewed ATCC 25922 MIC column in original units",
        )
        raw = cells[column]
        comparator = ">" if raw.startswith(">") else "="
        number = raw[1:] if comparator == ">" else raw
        _require(
            number.isdecimal()
            and (
                assay["raw_value"],
                assay["comparator"],
                assay["reported_numeric_text"],
            )
            == (raw, comparator, number),
            "assay_value",
            "Preserve original measurement and censoring",
        )
        _require(
            assay["class_label"] is None
            and assay["new_unit_conversion"] is False
            and assay["strain_scope_status"]
            == "proposal; no selection outcome or model score used",
            "invented_label",
            "No new class, conversion or retrospective selection",
        )
        _require(
            row["raw_published_pool_overlap_members"]
            == original["raw_exact_overlap_members"]
            and row["checkpoint_fitting_or_model_selection_exposure"] == "unresolved"
            and row["independent_test_member"] is False,
            "exposure_changed",
            "Keep source-pool overlap and unresolved independence",
        )
        expected_keys = {
            "source_occurrence_id",
            "source_table",
            "xml_row_index",
            "source_name",
            "raw_source_id",
            "sequence_sha256",
            "sequence_length",
            "chemical_entity_evidence",
            "proposed_model_view",
            "proposed_assay_scope",
            "raw_published_pool_overlap_members",
            "checkpoint_fitting_or_model_selection_exposure",
            "independent_test_member",
        }
        _require(set(row) == expected_keys, "record_fields", "Unreviewed record fields")
        groups[digest].append(row)
    repeated = []
    for digest, members in groups.items():
        if len(members) > 1:
            values = [r["proposed_assay_scope"]["raw_value"] for r in members]
            repeated.append(
                {
                    "sequence_sha256": digest,
                    "source_names": [r["source_name"] for r in members],
                    "source_occurrence_ids": [
                        r["source_occurrence_id"] for r in members
                    ],
                    "raw_MIC_values_ug_per_mL": values,
                    "distinct_reported_values": len(set(values)),
                    "interpretation": "distinct table observations; no averaged, minimum, preferred, independent-replicate or corrected label assigned",
                }
            )
    totals = {
        "table_occurrences": len(rows),
        "distinct_raw_strings": len(groups),
        "table_occurrences_by_table": dict(Counter(r["source_table"] for r in rows)),
        "raw_MIC_comparators": dict(
            Counter(r["proposed_assay_scope"]["comparator"] for r in rows)
        ),
        "repeated_strings_with_different_table_observations": sum(
            r["distinct_reported_values"] > 1 for r in repeated
        ),
        "exact_published_pool_overlap_distinct_strings": sum(
            any(r["raw_published_pool_overlap_members"] for r in members)
            for members in groups.values()
        ),
        "current_annotated_consumer_compatible_occurrences": 0,
        "independent_test_members_qualified": 0,
    }
    _require(
        review["totals"] == totals
        and review["repeated_sequence_observations"] == repeated,
        "observation_summary",
        "Do not collapse, average or relabel source observations",
    )
    return totals


def inspect(snapshot):
    """Revalidate and describe a saved finite record, without original files."""
    _require(
        type(snapshot) is dict
        and set(snapshot) == {"schema", "profile", "source_json"},
        "snapshot_fields",
        "Unreviewed snapshot fields",
    )
    _require(
        snapshot["schema"] == _SCHEMA and snapshot["profile"] == _PROFILE,
        "snapshot_profile",
        "Wrong historical profile/schema",
    )
    texts = snapshot["source_json"]
    _require(
        type(texts) is dict and set(texts) == set(_PINS),
        "input_roles",
        "Authorization, review and source are all required",
    )
    data, identities = {}, {}
    for role, expected in _PINS.items():
        _require(
            type(texts[role]) is str, "input_text", f"{role} must retain JSON text"
        )
        try:
            blob = texts[role].encode("utf-8")
        except UnicodeError as error:
            raise HistoricalDataError("invalid_utf8", str(error)) from error
        _require(len(blob) <= _LIMIT, "input_size", f"{role} exceeds 2 MiB")
        _require(
            _digest(blob) == expected,
            "source_digest",
            f"Changed D46 {role} bytes; review required",
        )
        identities[role] = {"sha256": expected, "bytes": len(blob)}
        data[role] = _parse(texts[role])
    try:
        auth, review, source = (data[k] for k in ("authorization", "review", "source"))
        _require(
            auth["decision"] == "D46"
            and auth["schema"] == "peptidemt.hydramp_historical_view_authorization@1"
            and all(v is True for v in auth["approved"].values())
            and not any(auth["additional_permissions"].values()),
            "view_authority",
            "D46 finite view only; no inherited execution permission",
        )
        _require(
            auth["original_review_manifest"]["sha256"] == identities["review"]["sha256"]
            and review["source"]["sha256"] == identities["source"]["sha256"],
            "source_binding",
            "Broken authority/review/source binding",
        )
        _require(
            review["schema"] == "peptidemt.hydramp_historical_view_preparation@1"
            and source["schema"] == "peptidemt.hydramp_C0_measured_panel@1",
            "source_schema",
            "Unreviewed source schemas",
        )
        totals = _validate_records(review, source)
    except (KeyError, TypeError, IndexError, AttributeError) as error:
        raise HistoricalDataError("source_structure", str(error)) from error
    return {
        "schema": "peptidemt.hydramp_historical_inspection@1",
        "profile": _PROFILE,
        "status": "received_data_only_not_a_qualified_benchmark",
        "source_identities": identities,
        "counts": totals,
        "observations": review["occurrences"],
        "repeated_sequence_observations": review["repeated_sequence_observations"],
        "current_authority": {
            "D46_view_approved": True,
            "ATCC25922_review_scope_approved": True,
            "general_admission_changed": False,
            "native_execution_authorized": False,
        },
        "unresolved": [
            "source_use_terms",
            "checkpoint_and_fragment_exposure",
            "biological_estimand_and_entity_provenance",
            "mass_and_unit_route_if_needed",
            "independent_cohort_and_relatedness",
            "any_native_input_or_model_stage_requires_separate_approval",
        ],
        "model_payloads_or_calls": 0,
    }


def receive(authorization, review, source):
    """Read only the three explicit pinned JSON files; follow no source paths."""
    paths = {"authorization": authorization, "review": review, "source": source}
    texts = {}
    for role, path in paths.items():
        try:
            texts[role] = _read(path).decode("utf-8")
        except UnicodeError as error:
            raise HistoricalDataError("invalid_utf8", str(error)) from error
    snapshot = {"schema": _SCHEMA, "profile": _PROFILE, "source_json": texts}
    inspect(snapshot)
    return snapshot


def save(snapshot, destination):
    """Validate, then create a snapshot; never overwrite an existing file."""
    inspect(snapshot)
    destination = Path(destination)
    _require(destination.suffix.lower() == ".json", "input_form", "JSON only")
    with destination.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(snapshot, stream, ensure_ascii=False, indent=2, allow_nan=False)
        stream.write("\n")


def load(path):
    """Load and revalidate an autonomous snapshot, ignoring no cached verdicts."""
    snapshot = _parse(_read(path))
    inspect(snapshot)
    return snapshot


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    receiving = commands.add_parser(
        "receive", help="Receive the finite D46 JSON sources"
    )
    for name in ("authorization", "review", "source", "output"):
        receiving.add_argument("--" + name, required=True, type=Path)
    replay = commands.add_parser(
        "inspect", help="Revalidate a saved data-only snapshot"
    )
    replay.add_argument("snapshot", type=Path)
    args = parser.parse_args(argv)
    try:
        if args.command == "receive":
            snapshot = receive(args.authorization, args.review, args.source)
            save(snapshot, args.output)
        else:
            snapshot = load(args.snapshot)
        print(
            json.dumps(
                inspect(snapshot), ensure_ascii=False, sort_keys=True, allow_nan=False
            )
        )
    except (HistoricalDataError, OSError) as error:
        print(
            json.dumps(
                {
                    "status": "rejected",
                    "code": getattr(error, "code", "io_error"),
                    "detail": str(error),
                }
            ),
            file=sys.stderr,
        )
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
