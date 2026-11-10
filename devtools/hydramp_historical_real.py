"""D48 finite source/codec/learned-score receiving; no engine imports or dispatch.

Synthetic method-double records and learned results have distinct evidence kinds.
Real inference requires a separate exact execution receipt; D48 grants none.
"""

import argparse
import hashlib
import importlib.util
import json
import math
import re
import struct
import sys
from pathlib import Path


def _module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


evaluation = _module(
    "_historical_evaluation",
    Path(__file__).with_name("hydramp_historical_evaluation.py"),
)
data = evaluation.historical
Error, require = data.HistoricalDataError, data._require
AUTH_SHA = "d51992f9d6c7bd55af8400582fa7ddbbb8ba3e8de2901189de640ea47f373024"
DELEGATION_SHA = "302702ca76abfedb2977c3071384ceb9d011ee3e30be8c793f12cca1aec4ed03"
PROPOSAL_SHA = "8ecf7787f48bd5eb29ca693ffa0f2c4f439e639635e6c8c461f2bd1c01ecf89a"
CASE = "peptidemt.hydramp_historical_real_case@1"
CODECS = "peptidemt.hydramp_historical_codecs@1"
READY = "peptidemt.hydramp_historical_real_ready_plan@1"
COMPARISON = "peptidemt.hydramp_historical_learned_comparison@1"
EXECUTION = "peptidemt.hydramp_historical_real_execution_authorization@1"
PROVIDERS = ("legacy", "modern")
KINDS = ("instrumented_method_double", "learned_model")


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return evaluation._canonical(value)


def object_digest(value):
    return digest(canonical(value).encode("utf-8"))


def identity(path):
    path = Path(path)
    raw = path.read_bytes()
    # Preserve the qualified entry point (including interpreter symlinks).
    # Reading bytes still verifies the resolved content; changing the command
    # to its target would change the declared environment/origin contract.
    return {"path": str(path.absolute()), "bytes": len(raw), "sha256": digest(raw)}


def fields(value, expected, code):
    require(type(value) is dict and set(value) == set(expected.split()), code, expected)


def raw_case(case):
    """Pin exact texts before semantic receiving; also usable in Python 3.8."""
    fields(
        case,
        "schema proposal_json authority_json endpoint_json audit_json",
        "case_fields",
    )
    require(case["schema"] == CASE, "case_schema", "D48 case required")
    for name, expected in (
        ("authority_json", AUTH_SHA),
        ("proposal_json", PROPOSAL_SHA),
    ):
        require(
            type(case[name]) is str and digest(case[name].encode()) == expected,
            "case_authority",
            "Changed authority/proposal; no override",
        )
    proposal = data._parse(case["proposal_json"])
    authority = data._parse(case["authority_json"])
    require(
        authority["decision"] == "D48"
        and authority["not_authorized"]["neural_evaluations"] == 0,
        "case_authority",
        "D48 implementation/codec-only authority required",
    )
    for name, pin in (
        ("endpoint_json", proposal["D47_endpoint"]),
        ("audit_json", proposal["static_audit"]),
    ):
        require(
            type(case[name]) is str and digest(case[name].encode()) == pin["sha256"],
            "case_source",
            "Changed source endpoint/audit",
        )
    return proposal, data._parse(case["endpoint_json"])


def validate_case(case):
    proposal, endpoint = raw_case(case)
    evaluation.validate_endpoint(endpoint)
    require(
        endpoint["counts"] == proposal["endpoint_counts"],
        "case_counts",
        "Source counts differ",
    )
    require(
        [g["group_id"] for g in endpoint["groups"]]
        == [g["group_id"] for g in proposal["source_groups"]],
        "case_pairing",
        "Source group correspondence changed",
    )
    return proposal, endpoint


def prepare(proposal, authority, endpoint, audit):
    result = {"schema": CASE}
    for key, path in (
        ("proposal_json", proposal),
        ("authority_json", authority),
        ("endpoint_json", endpoint),
        ("audit_json", audit),
    ):
        result[key] = data._read(path).decode("utf-8")
    validate_case(result)
    return result


def source_views(case):
    """Read literal reviewed cells, never interpret a molecular format/chemistry."""
    proposal, endpoint = raw_case(case)
    source = data._parse(endpoint["source_snapshot"]["source_json"]["source"])
    by_id = {}
    for row in source["hydramps_original_measured_tables"]["records"]:
        by_id.setdefault(row["raw_sequence_sha256"], row["raw_cells"][2])
    views = [by_id[g["group_id"]] for g in proposal["source_groups"]]
    require(
        all(
            digest(s.encode()) == g["group_id"] and len(s) == g["sequence_length"]
            for s, g in zip(views, proposal["source_groups"])
        ),
        "source_views",
        "Literal reviewed view changed",
    )
    return views


def normalized_inventory(value):
    require(type(value) is dict, "runtime_inventory", "Distribution map required")
    result = {re.sub(r"[-_.]+", "-", k).lower(): v for k, v in value.items()}
    require(
        len(result) == len(value), "runtime_inventory", "Duplicate project identities"
    )
    return result


def native_bytes(values, dtype):
    formats = {"int32": "i", "int64": "q", "float32": "f"}
    require(dtype in formats, "native_dtype", "Only native int32/int64/float32")
    flat = [v for row in values for v in row] if dtype != "float32" else values
    try:
        return struct.pack("<" + formats[dtype] * len(flat), *flat)
    except (struct.error, OverflowError, TypeError) as error:
        raise Error("native_values", str(error)) from error


def check_tokens(case, provider, native):
    proposal, _ = raw_case(case)
    fields(native, "dtype shape values native_hex", "native_fields")
    rows, dtype = native["values"], "int32" if provider == "legacy" else "int64"
    require(
        native["dtype"] == dtype, "native_dtype", "Preserve each owner's native dtype"
    )
    require(
        type(rows) is list
        and len(rows) == len(proposal["source_groups"])
        and native["shape"] == [len(rows), 25],
        "native_shape",
        "Exact full native panel required",
    )
    for row, group in zip(rows, proposal["source_groups"]):
        n = group["sequence_length"]
        require(
            type(row) is list
            and len(row) == 25
            and all(type(v) is int and 0 <= v <= 20 for v in row)
            and all(v != 0 for v in row[:n])
            and all(v == 0 for v in row[n:]),
            "native_values",
            "No internal zeros, truncation or changed post-padding",
        )
    require(
        native_bytes(rows, dtype).hex() == native["native_hex"],
        "native_bytes",
        "Native bytes differ",
    )
    return rows


def check_runtime(case, provider, runtime):
    require(
        type(runtime) is dict
        and {
            "executable",
            "inventory",
            "cpu_ids",
            "numerical_threads",
            "source_origins",
        }
        <= set(runtime),
        "runtime_fields",
        "Observed runtime fields required",
    )
    proposal, _ = raw_case(case)
    profile = proposal["profiles"][provider]
    require(
        runtime["executable"] == profile["python"]["path"],
        "runtime_origin",
        "Unexpected interpreter",
    )
    require(
        normalized_inventory(runtime["inventory"])
        == normalized_inventory(profile["inventory"]),
        "runtime_inventory",
        "Exact retained versions required",
    )
    require(
        canonical(runtime["cpu_ids"]) == "[0,1]"
        and type(runtime["numerical_threads"]) is int
        and runtime["numerical_threads"] == 1,
        "runtime_limits",
        "CPU 0/1 and one numerical thread required",
    )
    audit = data._parse(case["audit_json"])
    for name, observed in runtime["source_origins"].items():
        require(
            name in audit["selected_source"]
            and observed == audit["selected_source"][name],
            "runtime_source",
            "Changed executed source origin",
        )
    expected = {provider + "_codec"} if provider == "legacy" else {"modern_codec"}
    require(
        expected <= set(runtime["source_origins"]),
        "runtime_source",
        "Missing owner codec origin",
    )


def validate_codecs(record):
    fields(record, "schema case captures attribution", "codec_record")
    require(record["schema"] == CODECS, "codec_schema", "D48 codec record required")
    validate_case(record["case"])
    require(
        set(record["captures"]) == set(PROVIDERS),
        "codec_providers",
        "Both owner codecs required",
    )
    rows = {}
    for provider in PROVIDERS:
        capture = record["captures"][provider]
        fields(capture, "raw_json supervision command worker", "codec_capture")
        facts = capture["supervision"]
        require(type(facts) is dict, "codec_process", "Supervision object required")
        require(
            facts.get("failure") is None
            and facts.get("returncode") == 0
            and facts.get("rss_scope") == "supervisor_and_descendants",
            "codec_process",
            "Codec must complete under aggregate supervision",
        )
        raw = data._parse(capture["raw_json"])
        fields(
            raw,
            "schema provider case_sha256 native runtime codec_operations parameter_files_opened neural_calls",
            "codec_output",
        )
        require(
            raw["schema"] == "peptidemt.hydramp_historical_codec_output@1"
            and raw["provider"] == provider
            and raw["case_sha256"] == object_digest(record["case"]),
            "codec_binding",
            "Codec source/provider binding changed",
        )
        require(
            type(raw["neural_calls"]) is int
            and raw["neural_calls"] == 0
            and raw["parameter_files_opened"] == [],
            "codec_scope",
            "Codec-only means no parameters/networks",
        )
        expected = (
            {"to_one_hot": 1, "pad": 1}
            if provider == "legacy"
            else {"encode_sequences": 1}
        )
        require(
            canonical(raw["codec_operations"]) == canonical(expected),
            "codec_calls",
            "Exactly one composite owner encoding",
        )
        check_runtime(record["case"], provider, raw["runtime"])
        rows[provider] = check_tokens(record["case"], provider, raw["native"])
        command = capture["command"]
        proposal, _ = raw_case(record["case"])
        require(
            type(command) is list
            and len(command) >= 6
            and command[:4]
            == [proposal["profiles"][provider]["python"]["path"], "-I", "-S", "-B"]
            and command[4] == capture["worker"]["path"]
            and command[5] == "codec",
            "codec_command",
            "Observed codec command changed",
        )
    require(
        rows["legacy"] == rows["modern"], "codec_mismatch", "Owner token values differ"
    )
    return {
        "status": "codec_values_equal_no_model_execution",
        "shape": [len(rows["legacy"]), 25],
        "neural_calls": 0,
    }


def validate_ready(plan):
    fields(plan, "schema codecs pins proposal_sha256", "ready_fields")
    require(
        plan["schema"] == READY and plan["proposal_sha256"] == PROPOSAL_SHA,
        "ready_profile",
        "D48 frozen profile required",
    )
    validate_codecs(plan["codecs"])
    require(
        type(plan["pins"]) is dict
        and set(plan["pins"])
        == {"operator", "worker", "receiver", "evaluation", "data", "supervision"},
        "ready_pins",
        "Actual code identities required",
    )
    # Each input artifact retains its actual qualifying worker identity. The
    # future inference worker is separately frozen in pins; data-only diagnostic
    # changes do not justify rerunning an unchanged owner's successful codec.
    return raw_case(plan["codecs"]["case"])


def authorized_execution_record(receipt):
    """Preserve old per-plan approvals; accept truthful standing delegation."""
    if receipt.get("explicit_investigator_approval") is True:
        return True
    text = receipt.get("standing_authority_json")
    if (
        receipt.get("authorization_basis") != "standing_investigator_delegation"
        or receipt.get("run_specific_investigator_review") is not False
        or type(text) is not str
        or digest(text.encode()) != DELEGATION_SHA
    ):
        return False
    authority = data._parse(text)
    return (
        authority.get("decision") == "D49"
        and authority.get("routine_execution_within_approved_work") is True
        and authority.get("individual_run_confirmation_required") is False
    )


def execution_authority(plan, text, semantic=True):
    if semantic:
        validate_ready(plan)
    else:
        # The original interpreter is 3.8; full D46 semantic receiving runs in
        # the 3.14 controller. The worker still checks exact immutable texts
        # and fresh ready-plan authority before importing any engine.
        require(
            plan["schema"] == READY and plan["proposal_sha256"] == PROPOSAL_SHA,
            "ready_profile",
            "Wrong frozen worker profile",
        )
        raw_case(plan["codecs"]["case"])
    require(
        type(text) is str,
        "execution_authority",
        "Exact execution provenance and resource authority required",
    )
    receipt = data._parse(text)
    require(
        receipt.get("schema") == EXECUTION
        and authorized_execution_record(receipt)
        and receipt.get("stage") == "real_scoring"
        and receipt.get("ready_plan_sha256") == object_digest(plan)
        and type(receipt.get("reply_reference")) is str
        and bool(receipt["reply_reference"].strip())
        and receipt.get("neural_evaluations") == 12,
        "execution_authority",
        "D48 alone grants no inference; wrong/missing new receipt",
    )
    return receipt


def column(values, shape):
    """Exact native FP32 values and bytes, also for fabricated test doubles."""
    return {
        "dtype": "float32",
        "shape": shape,
        "values": values,
        "native_hex": native_bytes(values, "float32").hex(),
    }


def check_column(value, n, shape):
    fields(value, "dtype shape values native_hex", "score_fields")
    scores = value["values"]
    require(
        value["dtype"] == "float32"
        and canonical(value["shape"]) == canonical(shape)
        and type(scores) is list
        and len(scores) == n,
        "score_shape",
        "Preserve native score dtype/shape",
    )
    require(
        all(
            type(v) in (int, float) and 0 <= v <= 1 and math.isfinite(v) for v in scores
        ),
        "score_value",
        "Finite native values without filling/coercion",
    )
    raw = native_bytes(scores, "float32")
    require(
        list(struct.unpack("<" + "f" * n, raw)) == scores
        and raw.hex() == value["native_hex"],
        "score_precision",
        "No rounded or substituted FP32 values",
    )
    return scores


def check_capture(plan, provider, capture, kind):
    proposal, _ = validate_ready(plan)
    fields(capture, "raw_json supervision command", "score_capture")
    raw = data._parse(capture["raw_json"])
    fields(
        raw,
        "schema evidence_kind provider plan_sha256 native_input_sha256 head events attempted completed parameter_files_opened model_loads failure runtime",
        "score_output",
    )
    require(
        raw["schema"] == "peptidemt.hydramp_historical_score_output@1"
        and raw["evidence_kind"] == kind
        and raw["provider"] == provider
        and raw["plan_sha256"] == object_digest(plan)
        and raw["head"] == "VeltriAMPClassifier_MIC",
        "score_binding",
        "Wrong evidence kind/provider/head/plan",
    )
    native = data._parse(plan["codecs"]["captures"][provider]["raw_json"])["native"]
    require(
        raw["native_input_sha256"] == digest(bytes.fromhex(native["native_hex"])),
        "score_input",
        "Do not reuse scores behind a different native array",
    )
    check_runtime(plan["codecs"]["case"], provider, raw["runtime"])
    required_sources = (
        {"legacy_loader", "legacy_MIC_head"}
        if provider == "legacy"
        else {"modern_inference"}
    )
    require(
        required_sources <= set(raw["runtime"]["source_origins"]),
        "runtime_source",
        "Actual scored-head source required",
    )
    events = raw["events"]
    require(
        type(events) is list and len(events) <= len(proposal["requests"]),
        "score_requests",
        "Unexpected requests",
    )
    for event, request in zip(events, proposal["requests"]):
        fields(event, "tag indices MIC auxiliary_AMP", "score_event")
        require(
            event["tag"] == request["tag"]
            and canonical(event["indices"]) == canonical(request["indices"]),
            "score_pairing",
            "Missing/foreign/reordered source group",
        )
        n = len(request["indices"])
        check_column(event["MIC"], n, [n, 1] if provider == "legacy" else [n])
        if provider == "modern":
            check_column(event["auxiliary_AMP"], n, [n])
        else:
            require(
                event["auxiliary_AMP"] is None,
                "score_head",
                "No original AMP forward commissioned",
            )
    require(
        type(raw["attempted"]) is int
        and type(raw["completed"]) is int
        and raw["completed"] == len(events)
        and len(events) <= raw["attempted"] <= min(4, len(events) + 1),
        "score_accounting",
        "Unexplained attempted/completed API counts",
    )
    success = raw["failure"] is None
    require(
        success
        or (
            type(raw["failure"]) is dict
            and set(raw["failure"]) == {"type", "detail"}
            and all(type(v) is str for v in raw["failure"].values())
        ),
        "score_failure",
        "Retain an explicit worker failure cause",
    )
    require(
        not success or len(events) == raw["attempted"] == 4,
        "score_incomplete",
        "Success requires all requests",
    )
    facts = capture["supervision"]
    require(type(facts) is dict, "score_process", "Supervision object required")
    require(
        (not success or (facts.get("returncode") == 0 and facts.get("failure") is None))
        and facts.get("rss_scope") == "supervisor_and_descendants",
        "score_process",
        "Observed process contradicts completion",
    )
    if kind == "instrumented_method_double":
        require(
            raw["parameter_files_opened"] == []
            and type(raw["model_loads"]) is int
            and raw["model_loads"] == 0,
            "score_kind",
            "Method doubles cannot claim model use",
        )
    else:
        allowed = {x["path"] for x in proposal["assets"]}
        require(
            type(raw["parameter_files_opened"]) is list
            and set(raw["parameter_files_opened"]) <= allowed
            and raw["model_loads"] in (0, 1)
            and (
                not success
                or (raw["model_loads"] == 1 and bool(raw["parameter_files_opened"]))
            ),
            "score_assets",
            "Unexpected/unobserved learned assets",
        )
        expected = [
            proposal["profiles"][provider]["python"]["path"],
            "-I",
            "-S",
            "-B",
            plan["pins"]["worker"]["path"],
            "score",
        ]
        require(
            capture["command"][:6] == expected, "score_command", "Wrong worker command"
        )
    return raw


def _context_events(raw, context):
    events = raw["events"]
    slots = {e["tag"]: e for e in events}
    tags = {
        "primary": ["primary_full"],
        "repeat": ["repeat_full"],
        "split": ["split_first", "split_last"],
    }[context]
    if not all(tag in slots for tag in tags):
        return None
    return [v for tag in tags for v in slots[tag]["MIC"]["values"]]


def result(plan, authority_text, captures, kind):
    proposal, endpoint = validate_ready(plan)
    require(
        kind in KINDS and set(captures) == set(PROVIDERS),
        "comparison_kind",
        "Both paired providers and a truthful evidence kind required",
    )
    if kind == "learned_model":
        execution_authority(plan, authority_text)
    else:
        require(
            authority_text is None,
            "comparison_kind",
            "Controls have no learned execution receipt",
        )
    raw = {p: check_capture(plan, p, captures[p], kind) for p in PROVIDERS}
    results, vectors = {}, {}
    metric = None
    groups = endpoint["groups"]
    for context in ("primary", "repeat", "split"):
        scores = {p: _context_events(raw[p], context) for p in PROVIDERS}
        vectors[context] = scores
        if any(v is None for v in scores.values()):
            results[context] = {"status": "incomplete_paired_context_no_AUC"}
            continue
        if metric is None:
            metric, limit, provider = evaluation._provider()
        pairs = {
            g["group_id"]: {"original": a, "modern": b}
            for g, a, b in zip(groups, scores["legacy"], scores["modern"])
        }
        primary = [g for g in groups if g["primary_eligible"]]
        with limit(limits=1):
            scenarios = [
                evaluation._scenario(
                    "primary_stable",
                    [g["group_id"] for g in primary],
                    [g["primary_label"] for g in primary],
                    pairs,
                    metric,
                )
            ]
            for label, name in ((0, "ambiguous_inactive"), (1, "ambiguous_active")):
                labels = [
                    g["primary_label"] if g["primary_eligible"] else label
                    for g in groups
                ]
                scenarios.append(
                    evaluation._scenario(
                        name, [g["group_id"] for g in groups], labels, pairs, metric
                    )
                )
        results[context] = {
            "status": "descriptive_only",
            "metrics": scenarios,
            "provider": provider,
            "paired_ambiguity_range": [
                min(s["paired_difference"] for s in scenarios[1:]),
                max(s["paired_difference"] for s in scenarios[1:]),
            ],
        }
    cross_provider = {}
    for context, pair in vectors.items():
        cross_provider[context] = (
            None
            if any(v is None for v in pair.values())
            else [
                {
                    "group_id": group["group_id"],
                    "legacy": a,
                    "modern": b,
                    "modern_minus_legacy": b - a,
                }
                for group, a, b in zip(groups, pair["legacy"], pair["modern"])
            ]
        )
    diagnostics = {}
    for p in PROVIDERS:
        baseline = vectors["primary"][p]
        diagnostics[p] = {}
        for context in ("repeat", "split"):
            other = vectors[context][p]
            if baseline is None or other is None:
                diagnostics[p][context] = {"status": "incomplete"}
            else:
                changed = [
                    g["group_id"]
                    for g, a, b in zip(groups, baseline, other)
                    if native_bytes([a], "float32") != native_bytes([b], "float32")
                ]
                diagnostics[p][context] = {
                    "status": "unchanged"
                    if not changed
                    else "repeat_FAIL"
                    if context == "repeat"
                    else "batch_sensitive",
                    "changed_group_ids": changed,
                    "max_abs_difference": max(
                        abs(a - b) for a, b in zip(baseline, other)
                    ),
                }
                if metric is not None:
                    stable = [g for g in groups if g["primary_eligible"]]
                    pairs = {
                        g["group_id"]: {"original": a, "modern": b}
                        for g, a, b in zip(groups, baseline, other)
                    }
                    with limit(limits=1):
                        delta = evaluation._scenario(
                            context,
                            [g["group_id"] for g in stable],
                            [g["primary_label"] for g in stable],
                            pairs,
                            metric,
                        )
                    diagnostics[p][context]["primary_binary_rank_changes"] = [
                        {
                            "positive_group": row["positive_group"],
                            "negative_group": row["negative_group"],
                            "baseline_relation": row["original_relation"],
                            "other_relation": row["modern_relation"],
                        }
                        for row in delta["changed_pair_relations"]
                    ]
    return {
        "status": "method_double_only_not_HydrAMP_performance"
        if kind == "instrumented_method_double"
        else "learned_descriptive_comparison_not_equivalence",
        "complete": all(raw[p]["failure"] is None for p in PROVIDERS),
        "headline_context": "primary",
        "contexts": results,
        "diagnostics": diagnostics,
        "raw_cross_provider_differences": cross_provider,
        "charged_neural_evaluations": sum(
            raw[p]["attempted"] * (1 if p == "legacy" else 2) for p in PROVIDERS
        )
        if kind == "learned_model"
        else 0,
        "source_observations_retained": endpoint["counts"]["source_observations"],
        "biological_or_equivalence_claim": False,
    }


def receive(plan, authority_text, captures, kind, attribution=None):
    computed = result(plan, authority_text, captures, kind)
    if attribution is None:
        require(
            kind == "instrumented_method_double",
            "comparison_attribution",
            "Learned results require detached observed attribution",
        )
        attribution = {
            "status": "method_double_only",
            "completed_operations": [],
            "bibliography": [],
        }
    record = {
        "schema": COMPARISON,
        "evidence_kind": kind,
        "plan": plan,
        "execution_authority_json": authority_text,
        "captures": captures,
        "attribution": attribution,
        "result": computed,
    }
    check_attribution(record)
    return record


def check_attribution(record):
    value = record["attribution"]
    require(
        type(value) is dict
        and {"completed_operations", "bibliography", "status"} <= set(value),
        "comparison_attribution",
        "Detached attribution required",
    )
    if record["evidence_kind"] == "instrumented_method_double":
        require(
            value["completed_operations"] == []
            and value["bibliography"] == []
            and value["status"] == "method_double_only",
            "comparison_attribution",
            "Controls credit no model operation",
        )
    else:
        operations = [
            p + "_native_MIC_scoring"
            for p in PROVIDERS
            if data._parse(record["captures"][p]["raw_json"])["events"]
        ]
        require(
            value["completed_operations"] == operations,
            "comparison_attribution",
            "Credit only confirmed scoring branches",
        )


def inspect(record):
    require(type(record) is dict, "record_form", "JSON record object required")
    if record.get("schema") == CASE:
        proposal, endpoint = validate_case(record)
        return {
            "status": "D48_case_no_model_allowance",
            "counts": endpoint["counts"],
            "groups": len(proposal["source_groups"]),
        }
    if record.get("schema") == CODECS:
        return validate_codecs(record)
    if record.get("schema") == READY:
        validate_ready(record)
        return {
            "status": "ready_for_exact_model_review_not_authorized",
            "neural_allowance": 0,
        }
    fields(
        record,
        "schema evidence_kind plan execution_authority_json captures attribution result",
        "comparison_fields",
    )
    require(
        record["schema"] == COMPARISON, "comparison_schema", "Wrong comparison schema"
    )
    check_attribution(record)
    expected = result(
        record["plan"],
        record["execution_authority_json"],
        record["captures"],
        record["evidence_kind"],
    )
    require(
        canonical(expected) == canonical(record["result"]),
        "comparison_cache",
        "Cached result changed",
    )
    return expected


def load(path):
    record = data._parse(data._read(path))
    inspect(record)
    return record


def save(record, path):
    inspect(record)
    blob = (
        json.dumps(record, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    ).encode()
    require(
        len(blob) <= data._LIMIT and Path(path).suffix.lower() == ".json",
        "record_size",
        "Bounded JSON only",
    )
    with Path(path).open("xb") as stream:
        stream.write(blob)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", type=Path)
    args = parser.parse_args(argv)
    try:
        print(
            json.dumps(inspect(load(args.record)), ensure_ascii=False, allow_nan=False)
        )
    except (Error, OSError, ValueError, KeyError, TypeError) as error:
        print(
            json.dumps(
                {
                    "status": "rejected",
                    "code": getattr(error, "code", "invalid_record"),
                    "detail": str(error),
                }
            ),
            file=sys.stderr,
        )
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
