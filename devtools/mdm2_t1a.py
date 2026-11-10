"""Receive the approved D53 finite reported-affinity source; no molecular work.

This private developer case transcribes article tables, not a molecular format.
PyUnitWizard owns quantity/uncertainty codecs. Original source text and precision
remain evidence; no chemical identity, numerical affinity prediction or class is
inferred. See devguide/mdm2_t1a_work_order.md.
"""

import argparse
import base64
import copy
import hashlib
import importlib.metadata
import importlib.util
import json
import math
import os
import re
import resource
import sys
import tempfile
import traceback
from decimal import Decimal
from html.parser import HTMLParser
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = "peptidemt.mdm2_t1a@1"
SOURCE_SHA = "99f361fdab13c2971362fbe5e96b255e8a32dd5f8d605154bcd98918268f1264"
PROPOSAL_SHA = "069247bf4b46e8fafba553ecb5311f67b0bfd6748ea4a06822053c3285c05e56"
AUTH_SHA = "41b2e0d0f7f522dd8a1c625f49139e77a5e66c995556e0c8be6909e702ef6495"
ACQUISITION_SHA = "c46c8fa359d1454ae5426163f1897764b850c4ef786670180781927e80088229"
UNIT = "mole/liter"
DIMENSION = {"[L]": -3, "[mol]": 1}
FORBIDDEN = (
    "molsysmt",
    "rdkit",
    "openmm",
    "pdbfixer",
    "torch",
    "tensorflow",
    "keras",
    "onnxruntime",
    "macrel",
    "hydramp",
    "hydramps",
)
LIMITS = {
    "min_available_memory_bytes": 4 * 1024**3,
    "min_free_disk_bytes": 1024**3,
    "threads": 1,
    "wall_seconds": 180,
    "rss_stop_bytes": 512 * 1024**2,
    "max_output_bytes": 64 * 1024**2,
}
CHEMISTRY = dict.fromkeys(
    (
        "n_terminus",
        "c_terminus",
        "stereochemistry",
        "modifications",
        "coordinate_mapping",
    ),
    "unassessed",
)


class EvidenceError(ValueError):
    """Refuse a changed or scientifically inconsistent finite-source record."""


def require(condition, message):
    if not condition:
        raise EvidenceError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def identity(path):
    path = Path(path).resolve()
    data = path.read_bytes()
    return {"path": str(path), "bytes": len(data), "sha256": digest(data)}


def write_new(path, value):
    with Path(path).open("x") as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False, allow_nan=False)
        stream.write("\n")


class ArticleTables(HTMLParser):
    """Literal, source-specific HTML table/paragraph transcription only."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tables, self.paragraphs = [], {}
        self.table, self.row, self.cell, self.paragraph = None, None, None, None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "table":
            require(self.table is None, "Unexpected nested article table")
            self.table = []
        elif tag == "tr" and self.table is not None:
            self.row = []
        elif tag in ("td", "th") and self.row is not None:
            self.cell = []
        if tag == "p" and attrs.get("id") in ("P7", "P39", "P40"):
            self.paragraph = (attrs["id"], [])

    def handle_data(self, data):
        if self.cell is not None:
            self.cell.append(data)
        if self.paragraph is not None:
            self.paragraph[1].append(data)

    def handle_endtag(self, tag):
        if tag in ("td", "th") and self.cell is not None:
            self.row.append("".join(self.cell))
            self.cell = None
        elif tag == "tr" and self.row is not None:
            self.table.append(self.row)
            self.row = None
        elif tag == "table" and self.table is not None:
            self.tables.append(self.table)
            self.table = None
        if tag == "p" and self.paragraph is not None:
            name, text = self.paragraph
            self.paragraphs[name] = "".join(text)
            self.paragraph = None


def stated_measurement(raw):
    """Read the table's printed shared exponent, retaining exact source tokens."""
    token = "".join(raw.split())
    if token == "n.d.a":
        return {
            "status": "not_quantified_weak_binding",
            "kd_decimal": None,
            "sd_decimal": None,
            "unit": UNIT,
            "raw_unit": "M",
        }
    match = re.fullmatch(r"(\d+(?:\.\d+)?)±(\d+(?:\.\d+)?)E([+-]\d+)", token)
    require(match is not None, "Unsupported reported Kd/SD token")
    mean, spread, exponent = match.groups()
    kd, sd = Decimal(mean).scaleb(int(exponent)), Decimal(spread).scaleb(int(exponent))
    require(
        kd > 0 and sd >= 0 and math.isfinite(float(kd)) and math.isfinite(float(sd)),
        "Invalid finite reported Kd/SD",
    )
    return {
        "status": "quantified",
        "kd_decimal": str(kd),
        "sd_decimal": str(sd),
        "unit": UNIT,
        "raw_unit": "M",
    }


def transcribe(data, *, pinned=True):
    require(not pinned or digest(data) == SOURCE_SHA, "Unreviewed source bytes")
    parser = ArticleTables()
    parser.feed(data.decode("utf-8"))
    require(len(parser.tables) == 3, "Changed article table inventory")
    require(set(parser.paragraphs) == {"P7", "P39", "P40"}, "Missing source context")
    require(
        "At least three independent measurements" in parser.paragraphs["P7"],
        "Changed source replicate statement",
    )
    occurrences, evidence = [], []
    for table_id, table_index, heading, series in (
        ("T1", 0, "PMI", "PMI"),
        ("T3", 2, "P53", "17–28 p53"),
    ):
        rows = parser.tables[table_index]
        require(
            len(rows) == 22
            and rows[0] == ["Peptide Sequence", heading + "-MDM2", heading + "-MDMX"],
            "Changed target headers",
        )
        require(rows[2][0] == rows[2][3] == "Kd (M)", "Changed source Kd units")
        require(
            len(rows[2]) == 6 and rows[1] == rows[16] == [""], "Changed table structure"
        )
        require(
            all(len(rows[i]) == 18 for i in (*range(3, 16), *range(17, 22))),
            "Missing/changed source row",
        )
        if table_id == "T1":
            require(rows[7] == rows[3], "WT/self-substitution repeat differs")
        for ordinal, row_index in enumerate((*range(3, 16), *range(17, 22))):
            cells = rows[row_index]
            source_id = f"li2010:{table_id}:tr-{row_index}"
            canonical_row = 3 if table_id == "T1" and row_index == 7 else row_index
            entity_id = f"li2010:{table_id}:tr-{canonical_row}"
            for target, column, construct in (
                ("MDM2", 12, "25–109"),
                ("MDMX", 15, "24–108"),
            ):
                occurrence_id = source_id + ":" + target
                evidence_id = entity_id + ":" + target
                number = stated_measurement(cells[column])
                item = {
                    "occurrence_id": occurrence_id,
                    "evidence_id": evidence_id,
                    "reported_entity_id": entity_id,
                    "table": table_id,
                    "html_table_index": table_index,
                    "html_tr_index": row_index,
                    "peptide_row_ordinal": ordinal,
                    "target": target,
                    "target_column_index": column,
                    "target_construct_reported": construct,
                    "series_reported": series,
                    "raw_cells": list(cells),
                    "source_sequence_cells": list(cells[:12]),
                    "literal_sequence_display": "".join(cells[:12]),
                    "raw_measurement": cells[column],
                    **number,
                    "chemical_identity": copy.deepcopy(CHEMISTRY),
                    "source_scoped_identity_only": True,
                    "replicate_n": None,
                    "source_replicate_lower_bound": 3,
                    "uncertainty_kind": "sd",
                    "confidence_level": None,
                    "measurement_limit": None,
                    "activity_class": None,
                    "alias_of": evidence_id if source_id != entity_id else None,
                    "alias_reason": "Explicit WT/self-substitution repeated display"
                    if source_id != entity_id
                    else None,
                }
                if number["status"] != "quantified":
                    item["unavailable_reason"] = (
                        "Table 3 footnote a: binding too weak to reliably measure; "
                        "reported as not determined. No quantitative censoring limit admitted."
                    )
                else:
                    item["unavailable_reason"] = None
                occurrences.append(item)
                if item["alias_of"] is None:
                    evidence.append(
                        {
                            "evidence_id": evidence_id,
                            "source_occurrence_ids": [occurrence_id],
                            "measurement_record": None,
                        }
                    )
                else:
                    expected = next(
                        x for x in evidence if x["evidence_id"] == evidence_id
                    )
                    expected["source_occurrence_ids"].append(occurrence_id)
    return {
        "occurrences": occurrences,
        "reported_evidence": evidence,
        "source_context": {
            "paragraphs": parser.paragraphs,
            "assay": "SPR-based competition Kd",
            "experimental_producer": "Li et al. (2010), not the data transcriber",
            "temperature_reported": "room temperature",
            "temperature_numeric": None,
            "source_doi": "10.1016/j.jmb.2010.03.005",
            "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC2856455/",
            "uncertainty_source": "Tables 1 and 3 captions explicitly state SD",
            "unavailable_source": "Table 3 footnote a",
            "terms_observation": "Publicly readable author manuscript; general redistribution license unestablished",
        },
        "limitations": {
            "chemical_identity_qualified": False,
            "independence_qualified": False,
            "prospective_blinding": False,
            "source_result_exposure": "Reviewed before method choice",
            "table_3_caption_discrepancy": "Caption says p53 and 15 analogs; 18 peptide rows are displayed",
            "MDMX_objective_role": "unassigned; separate experimental context",
            "supplement": "not received; no contents assumed",
            "public_dataset_release": "not commissioned; terms review remains separate",
        },
    }


def quantities():
    import pyunitwizard as puw
    from pyunitwizard.measurement import MeasurementRecord

    return puw, MeasurementRecord


def encode_measurements(reference):
    puw, measurement = quantities()
    by_id = {x["occurrence_id"]: x for x in reference["occurrences"]}
    for row in reference["reported_evidence"]:
        original = by_id[row["source_occurrence_ids"][0]]
        if original["status"] == "quantified":
            row["measurement_record"] = measurement.from_quantity(
                puw.quantity(float(original["kd_decimal"]), UNIT, form="pint"),
                half_width=puw.quantity(
                    float(original["sd_decimal"]), UNIT, form="pint"
                ),
                kind="sd",
                n=None,
                field=row["evidence_id"] + ".kd",
            ).to_dict()


def validate(reference, *, pinned=True):
    """Recheck source correspondence and owner records on every saved read."""
    require(reference.get("schema") == SCHEMA, "Wrong T1a schema")
    require(
        reference.get("approved_proposal_sha256") == PROPOSAL_SHA
        and reference.get("authorization_sha256") == AUTH_SHA,
        "Changed scientific authority",
    )
    try:
        data = base64.b64decode(reference["source_html_base64"], validate=True)
    except (KeyError, ValueError) as exc:
        raise EvidenceError("Invalid embedded source") from exc
    require(digest(data) == reference.get("source_sha256"), "Source hash differs")
    acquisition_text = reference.get("source_acquisition_text")
    require(isinstance(acquisition_text, str), "Missing original acquisition record")
    require(
        not pinned or digest(acquisition_text.encode()) == ACQUISITION_SHA,
        "Changed original acquisition provenance",
    )
    acquisition = json.loads(acquisition_text)
    require(
        acquisition == reference.get("source_acquisition")
        and acquisition["sha256"] == digest(data)
        and acquisition["bytes"] == len(data),
        "Changed source acquisition correspondence",
    )
    expected = transcribe(data, pinned=pinned)
    for key in ("occurrences", "source_context", "limitations"):
        require(
            reference.get(key) == expected[key], "Changed source correspondence: " + key
        )
    rows = reference.get("reported_evidence")
    require(
        isinstance(rows, list) and len(rows) == len(expected["reported_evidence"]),
        "Changed unique reported-evidence population",
    )
    puw, measurement = quantities()
    by_id = {x["occurrence_id"]: x for x in expected["occurrences"]}
    for saved, original in zip(rows, expected["reported_evidence"], strict=True):
        require(
            set(saved) == set(original)
            and saved["evidence_id"] == original["evidence_id"]
            and saved["source_occurrence_ids"] == original["source_occurrence_ids"],
            "Changed evidence alias/target correspondence",
        )
        source = by_id[original["source_occurrence_ids"][0]]
        if source["status"] != "quantified":
            require(
                saved["measurement_record"] is None,
                "Unquantified measurement became numeric",
            )
            continue
        decoded = measurement.from_dict(saved["measurement_record"])
        record_metadata = saved["measurement_record"]["metadata"]
        require(
            record_metadata["n"] is None and record_metadata["level"] is None,
            "Invented exact replicate count or confidence level",
        )
        q = decoded.to_quantities(
            field=saved["evidence_id"] + ".kd",
            kind="sd",
            unit=UNIT,
            dimensionality=DIMENSION,
            form="pint",
        )
        require(
            puw.get_value(q["value"], to_unit=UNIT) == float(source["kd_decimal"])
            and puw.get_value(q["half_width"], to_unit=UNIT)
            == float(source["sd_decimal"]),
            "Quantity differs from the printed Kd/SD",
        )
    quantified = sum(x["measurement_record"] is not None for x in rows)
    return {
        "source_occurrences": len(expected["occurrences"]),
        "reported_peptide_entities": len(
            {x["reported_entity_id"] for x in expected["occurrences"]}
        ),
        "reported_peptide_target_evidence": len(rows),
        "quantified": quantified,
        "not_quantified": len(rows) - quantified,
        "duplicate_display_occurrences": sum(
            x["alias_of"] is not None for x in expected["occurrences"]
        ),
        "chemical_identity_qualified": False,
        "prediction_validated": False,
    }


def receive(path):
    data = Path(path).read_bytes()
    reference = transcribe(data)
    acquisition_text = Path(path).with_name("acquisition.json").read_text()
    require(
        digest(acquisition_text.encode()) == ACQUISITION_SHA,
        "Unreviewed acquisition record",
    )
    acquisition = json.loads(acquisition_text)
    require(
        acquisition["sha256"] == SOURCE_SHA and acquisition["bytes"] == len(data),
        "Source acquisition receipt does not match article bytes",
    )
    reference.update(
        schema=SCHEMA,
        source_sha256=digest(data),
        source_acquisition=acquisition,
        source_acquisition_text=acquisition_text,
        source_html_base64=base64.b64encode(data).decode("ascii"),
        approved_proposal_sha256=PROPOSAL_SHA,
        authorization_sha256=AUTH_SHA,
        producer={
            "code": identity(__file__),
            "python": sys.version,
            "pyunitwizard": importlib.metadata.version("pyunitwizard"),
            "pint": importlib.metadata.version("pint"),
        },
    )
    encode_measurements(reference)
    return reference, validate(reference)


def read_saved(path):
    require(Path(path).stat().st_size <= 4 * 1024**2, "Saved artifact too large")

    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, "Duplicate saved JSON key")
            result[key] = value
        return result

    def constant(value):
        raise EvidenceError("Nonfinite saved JSON: " + value)

    reference = json.loads(
        Path(path).read_text(), object_pairs_hook=pairs, parse_constant=constant
    )
    return reference, validate(reference)


def supervisor():
    spec = importlib.util.spec_from_file_location(
        "t1a_process", ROOT / "src/peptidemt/_hydramp_process.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def guard_process(operation, parent_pid):
    supervisor().configure_child(
        {"cpu_ids": [0, 1], "nice": 10, "address_space_bytes": 8 * 1024**3}, parent_pid
    )
    resource.setrlimit(resource.RLIMIT_CPU, (120, 120))

    def audit(event, args):
        if event in (
            "socket.connect",
            "socket.getaddrinfo",
            "subprocess.Popen",
            "os.system",
        ):
            raise RuntimeError("T1a forbids network and unplanned children")
        if (
            operation == "inspect"
            and event == "open"
            and isinstance(args[0], (str, bytes))
        ):
            name = os.fsdecode(args[0])
            if (
                "peptidemt-target-study-3l7pirsi/source/" in name
                or "/source/li2010.html" in name
            ):
                raise RuntimeError(
                    "Saved T1a reader cannot access original article files"
                )

    sys.addaudithook(audit)


def worker(args):
    guard_process(args.operation.removeprefix("_"), args.parent_pid)
    with (args.directory / "worker.log").open("x") as log:
        sys.stdout = sys.stderr = log
        try:
            import pyunitwizard as puw

            def policy_state():
                report = puw.configure.report()
                return {
                    key: report.get(key)
                    for key in (
                        "default_form",
                        "default_parser",
                        "standard_units",
                        "provenance",
                    )
                }

            before = policy_state()
            with puw.context(standard_units=["micromolar", "angstrom", "fs"]):
                policy = policy_state()
                if args.operation == "_receive":
                    reference, report = receive(args.input)
                    write_new(args.directory / "reference.json", reference)
                elif args.operation == "_inspect":
                    reference, report = read_saved(args.input)
                else:
                    raise EvidenceError("Unknown worker operation")
                require(policy_state() == policy, "T1a changed active unit policy")
            require(policy_state() == before, "T1a did not restore caller policy")
            forbidden = [
                name for name in sys.modules if name.split(".")[0] in FORBIDDEN
            ]
            require(
                not forbidden, "Molecular/learned provider imported: " + repr(forbidden)
            )
            report.update(
                status="pass",
                forbidden_modules=forbidden,
                active_policy_preserved=True,
                original_source_needed=args.operation != "_inspect",
                producer=reference["producer"],
                reader_code=identity(__file__),
                reader_pyunitwizard=importlib.metadata.version("pyunitwizard"),
                quantity_provider_file=identity(puw.__file__),
            )
            write_new(args.directory / "result.json", report)
        except BaseException as exc:
            traceback.print_exc()
            write_new(
                args.directory / "failure.json",
                {"type": type(exc).__name__, "message": str(exc)},
            )
            return 1
    return 0


def run(operation, input_path, task):
    authority = ROOT / "devguide/evidence/mdm2_t1a_authorization.json"
    require(
        identity(authority)["sha256"] == AUTH_SHA, "Changed T1a execution authority"
    )
    if operation == "receive":
        require(identity(input_path)["sha256"] == SOURCE_SHA, "Unreviewed source bytes")
    directory = Path(tempfile.mkdtemp(prefix=operation + "-", dir=task)).resolve()
    import shutil

    (directory / "executed-source").mkdir()
    shutil.copy2(__file__, directory / "executed-source/mdm2_t1a.py")
    command = [
        sys.executable,
        "-B",
        str(Path(__file__).resolve()),
        "_" + operation,
        "--input",
        str(input_path.resolve()),
        "--directory",
        str(directory),
        "--parent-pid",
        str(os.getpid()),
    ]
    write_new(
        directory / "declaration.json",
        {
            "operation": operation,
            "authority": identity(authority),
            "input": identity(input_path),
            "code": identity(__file__),
            "command": command,
            "limits": LIMITS,
            "molecular_calls": 0,
            "model_evaluations": 0,
        },
    )
    facts = supervisor().supervise(
        command, directory, SimpleNamespace(**LIMITS), include_supervisor_rss=True
    )
    write_new(directory / "supervision.json", facts)
    print(json.dumps({"directory": str(directory), **facts}, indent=2))
    return int(facts.get("failure") is not None or facts.get("returncode") != 0)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "operation", choices=("receive", "inspect", "_receive", "_inspect")
    )
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--task", type=Path)
    parser.add_argument("--directory", type=Path)
    parser.add_argument("--parent-pid", type=int)
    args = parser.parse_args()
    if args.operation.startswith("_"):
        return worker(args)
    require(
        args.task is not None and args.task.is_dir(), "Existing task directory required"
    )
    return run(args.operation, args.input, args.task)


if __name__ == "__main__":
    sys.exit(main())
