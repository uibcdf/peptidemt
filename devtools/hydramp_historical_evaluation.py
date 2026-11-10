"""D47 reported-activity endpoint and synthetic-score evaluation, without models.

Developer-only finite profile. Reuse the D46 data receiver and sklearn ROC-AUC;
there is no learned-score mode, native input preparation or execution command.
"""

import argparse
import hashlib
import importlib.util
import inspect as python_inspect
import json
import math
import sys
from decimal import Decimal
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "_historical_source_receiver",
    Path(__file__).with_name("hydramp_historical_data.py"),
)
historical = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(historical)
Error = historical.HistoricalDataError
_require = historical._require

_APPROVAL_SHA = "f2868f7d6865ead963f8c26fa908a9c6acd062bdc5decbbafd6500a8067b2afe"
_ENDPOINT = "peptidemt.hydramp_historical_endpoint@1"
_SCORES = "peptidemt.hydramp_historical_artificial_scores@1"
_COMPARISON = "peptidemt.hydramp_historical_synthetic_comparison@1"
_VERSIONS = {
    "scikit-learn": "1.9.1",
    "numpy": "2.4.6",
    "scipy": "1.18.1",
    "threadpoolctl": "3.7.0",
    "joblib": "1.6.0",
}
_METRIC_SOURCE_SHA = "b1d16d4108a66708dd797ecead322f4bfce290d7f08eb2e659eb61721a94ed15"


def _canonical(value):
    try:
        return json.dumps(
            value,
            sort_keys=True,
            ensure_ascii=False,
            allow_nan=False,
            separators=(",", ":"),
        )
    except (ValueError, TypeError, RecursionError) as error:
        raise Error("record_json", str(error)) from error


def _digest(value):
    return hashlib.sha256(_canonical(value).encode("utf-8")).hexdigest()


def _reported_class(value, comparator):
    number = Decimal(value)
    _require(
        number.is_finite() and number > 0,
        "endpoint_value",
        "Positive finite reported number required",
    )
    if comparator == "=":
        return int(number <= Decimal("32"))
    _require(comparator == ">", "endpoint_comparator", "Unreviewed censoring relation")
    return 0 if number >= Decimal("32") else None


def _derive(snapshot, approval_text):
    _require(
        type(approval_text) is str, "endpoint_authority", "Exact D47 JSON text required"
    )
    try:
        digest = hashlib.sha256(approval_text.encode("utf-8")).hexdigest()
    except UnicodeError as error:
        raise Error("endpoint_authority", str(error)) from error
    _require(
        digest == _APPROVAL_SHA,
        "endpoint_authority",
        "Changed/missing D47 approval; no policy override",
    )
    approval = historical._parse(approval_text)
    _require(
        approval.get("decision") == "D47"
        and approval.get("schema")
        == "peptidemt.hydramp_historical_endpoint_authorization@1",
        "endpoint_authority",
        "D47 endpoint approval required",
    )
    source = historical.inspect(snapshot)
    groups = {}
    for row in source["observations"]:
        group = groups.setdefault(
            row["sequence_sha256"],
            {
                "group_id": row["sequence_sha256"],
                "source_observations": [],
            },
        )
        assay = row["proposed_assay_scope"]
        _require(
            (assay["strain"], assay["endpoint"], assay["unit_as_reported"])
            == ("ATCC 25922", "MIC", "µg/mL"),
            "endpoint_scope",
            "No strain, endpoint or unit substitution",
        )
        group["source_observations"].append(
            {
                "source_occurrence_id": row["source_occurrence_id"],
                "source_name": row["source_name"],
                "raw_value": assay["raw_value"],
                "comparator": assay["comparator"],
                "unit": "µg/mL",
                "reported_activity_label": _reported_class(
                    assay["reported_numeric_text"], assay["comparator"]
                ),
            }
        )
    for group in groups.values():
        classes = {
            row["reported_activity_label"] for row in group["source_observations"]
        }
        stable = classes == {0} or classes == {1}
        group["primary_label"] = next(iter(classes)) if stable else None
        group["primary_eligible"] = stable
        group["exclusion_reason"] = (
            None
            if stable
            else (
                "undetermined_censoring"
                if None in classes
                else "conflicting_reported_classes"
            )
        )
    labels = [g["primary_label"] for g in groups.values() if g["primary_eligible"]]
    return {
        "schema": _ENDPOINT,
        "approval_json": approval_text,
        "source_snapshot": snapshot,
        "policy": {
            "decision": "D47",
            "organism": "E. coli",
            "strain": "ATCC 25922",
            "endpoint": "displayed MIC",
            "criterion": "<=32 µg/mL",
            "interpretation": "reported activity, not native molar class or calibrated probability",
            "grouping": "literal source-string hash, not chemical identity/independence",
            "sensitivity": ["ambiguous_inactive", "ambiguous_active"],
        },
        "groups": list(groups.values()),
        "counts": {
            "source_observations": len(source["observations"]),
            "raw_string_groups": len(groups),
            "primary_groups": len(labels),
            "primary_positive": labels.count(1),
            "primary_negative": labels.count(0),
            "excluded_groups": len(groups) - len(labels),
        },
        "native_payloads_or_model_calls": 0,
    }


def prepare(snapshot_path, approval_path):
    """Derive a separate endpoint without editing the pinned D46 snapshot."""
    return _derive(
        historical.load(snapshot_path), historical._read(approval_path).decode("utf-8")
    )


def validate_endpoint(endpoint):
    _require(
        type(endpoint) is dict
        and set(endpoint)
        == {
            "schema",
            "approval_json",
            "source_snapshot",
            "policy",
            "groups",
            "counts",
            "native_payloads_or_model_calls",
        },
        "endpoint_fields",
        "Unreviewed endpoint fields",
    )
    expected = _derive(endpoint["source_snapshot"], endpoint["approval_json"])
    _require(
        _canonical(endpoint) == _canonical(expected),
        "endpoint_changed",
        "Endpoint differs from the approved source-derived policy",
    )
    return expected


def _checked_scores(endpoint, scores):
    _require(
        type(scores) is dict
        and set(scores) == {"schema", "kind", "endpoint_sha256", "scores"},
        "score_fields",
        "Only the artificial-score contract is supported",
    )
    _require(
        scores["schema"] == _SCORES and scores["kind"] == "synthetic_control",
        "score_kind",
        "Only declared synthetic controls, never model-result claims",
    )
    _require(
        scores["endpoint_sha256"] == _digest(endpoint),
        "score_binding",
        "Scores belong to another endpoint/source/policy",
    )
    rows = scores["scores"]
    _require(
        type(rows) is list
        and all(
            type(r) is dict and set(r) == {"group_id", "original", "modern"}
            for r in rows
        ),
        "score_rows",
        "Exact paired-score fields required",
    )
    ids = [g["group_id"] for g in endpoint["groups"]]
    _require(
        [r["group_id"] for r in rows] == ids and len(set(ids)) == len(ids),
        "score_pairing",
        "All groups, including ambiguity, must match once in source order",
    )
    _require(
        all(
            type(r[slot]) in (int, float)
            and 0 <= r[slot] <= 1
            and math.isfinite(r[slot])
            for r in rows
            for slot in ("original", "modern")
        ),
        "score_value",
        "Finite numeric control scores in [0,1]; no booleans, filling or coercion",
    )
    return {r["group_id"]: r for r in rows}


def _provider():
    try:
        actual = {name: version(name) for name in _VERSIONS}
    except PackageNotFoundError as error:
        raise Error(
            "statistics_unavailable", "Use the qualified optional developer profile"
        ) from error
    _require(
        actual == _VERSIONS,
        "statistics_profile",
        "Changed statistical profile requires qualification; no fallback",
    )
    try:
        from sklearn.metrics import roc_auc_score
        from threadpoolctl import threadpool_limits
    except ImportError as error:
        raise Error(
            "statistics_unavailable", "Qualified statistics import failed"
        ) from error

    path = python_inspect.getsourcefile(python_inspect.unwrap(roc_auc_score))
    _require(
        path is not None and Path(path).name == "_ranking.py",
        "statistics_source",
        "Unqualified public metric implementation",
    )
    source_hash = hashlib.sha256(Path(path).read_bytes()).hexdigest()
    _require(
        source_hash == _METRIC_SOURCE_SHA,
        "statistics_source",
        "Metric source changed; requalification required",
    )
    return (
        roc_auc_score,
        threadpool_limits,
        {
            "callable": "sklearn.metrics.roc_auc_score",
            "distributions": actual,
            "public_callable_source_sha256": source_hash,
            "native_thread_limit": 1,
        },
    )


def _scenario(name, ids, labels, pairs, auc):
    _require(
        set(labels) == {0, 1}, "metric_classes", "Both reported classes are required"
    )
    old = float(auc(labels, [pairs[i]["original"] for i in ids]))
    new = float(auc(labels, [pairs[i]["modern"] for i in ids]))
    changed = []
    for positive, y_positive in zip(ids, labels, strict=True):
        if not y_positive:
            continue
        for negative, y_negative in zip(ids, labels, strict=True):
            if y_negative:
                continue
            relations = {}
            for slot in ("original", "modern"):
                p, n = pairs[positive][slot], pairs[negative][slot]
                relations[slot] = 1 if p > n else (-1 if p < n else 0)
            if relations["original"] != relations["modern"]:
                changed.append(
                    {
                        "positive_group": positive,
                        "negative_group": negative,
                        "original_relation": relations["original"],
                        "modern_relation": relations["modern"],
                    }
                )
    return {
        "scenario": name,
        "groups": len(ids),
        "positive_groups": labels.count(1),
        "negative_groups": labels.count(0),
        "original_slot_auc": old,
        "modern_slot_auc": new,
        "paired_difference": new - old,
        "changed_pair_relations": changed,
    }


def _result(endpoint, scores):
    endpoint = validate_endpoint(endpoint)
    pairs = _checked_scores(endpoint, scores)
    groups = endpoint["groups"]
    ambiguous = [g for g in groups if not g["primary_eligible"]]
    _require(
        len(ambiguous) == 1
        and ambiguous[0]["exclusion_reason"] == "conflicting_reported_classes",
        "ambiguity_profile",
        "Only the reviewed single conflicting group is supported",
    )
    primary = [g for g in groups if g["primary_eligible"]]
    _require(
        {g["primary_label"] for g in primary} == {0, 1},
        "metric_classes",
        "Both classes required before metric loading",
    )
    auc, thread_limit, provider = _provider()
    with thread_limit(limits=1):
        results = [
            _scenario(
                "primary_stable",
                [g["group_id"] for g in primary],
                [g["primary_label"] for g in primary],
                pairs,
                auc,
            )
        ]
        for value, name in ((0, "ambiguous_inactive"), (1, "ambiguous_active")):
            labels = [
                g["primary_label"] if g["primary_eligible"] else value for g in groups
            ]
            results.append(
                _scenario(name, [g["group_id"] for g in groups], labels, pairs, auc)
            )
    return {
        "status": "synthetic_control_only_not_a_HydrAMP_comparison",
        "provider": provider,
        "endpoint_counts": endpoint["counts"],
        "metrics": results,
        "paired_ambiguity_sensitivity_range": {
            "minimum": min(r["paired_difference"] for r in results[1:]),
            "maximum": max(r["paired_difference"] for r in results[1:]),
            "interpretation": "shared observed-class scenarios, not a confidence interval or adopted truth",
        },
        "source_observations_retained": endpoint["counts"]["source_observations"],
        "model_payloads_or_calls": 0,
        "biological_efficacy_or_equivalence_claim": False,
    }


def evaluate_synthetic(endpoint, scores):
    """Validate explicit artificial pairs and use the qualified public metric."""
    return {
        "schema": _COMPARISON,
        "evidence_kind": "synthetic_control",
        "endpoint": endpoint,
        "score_vectors": scores,
        "result": _result(endpoint, scores),
    }


def inspect(record):
    """Recompute source policy/results; cached success is never authoritative."""
    _require(type(record) is dict, "record_form", "A JSON object is required")
    if record.get("schema") == _ENDPOINT:
        endpoint = validate_endpoint(record)
        return {
            "status": "D47_endpoint_only_no_model_scores",
            "policy": endpoint["policy"],
            "counts": endpoint["counts"],
            "groups": endpoint["groups"],
            "native_payloads_or_model_calls": 0,
        }
    _require(
        set(record)
        == {"schema", "evidence_kind", "endpoint", "score_vectors", "result"}
        and record.get("schema") == _COMPARISON
        and record.get("evidence_kind") == "synthetic_control",
        "comparison_fields",
        "Only the declared synthetic comparison record is supported",
    )
    expected = _result(record["endpoint"], record["score_vectors"])
    _require(
        _canonical(expected) == _canonical(record["result"]),
        "comparison_changed",
        "Cached result or provider fingerprint changed",
    )
    return expected


def load(path):
    record = historical._parse(historical._read(path))
    inspect(record)
    return record


def save(record, destination):
    inspect(record)
    path = Path(destination)
    _require(path.suffix.lower() == ".json", "input_form", "JSON only")
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(record, stream, ensure_ascii=False, indent=2, allow_nan=False)
        stream.write("\n")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    preparation = commands.add_parser("prepare")
    for name in ("source-snapshot", "approval", "output"):
        preparation.add_argument("--" + name, type=Path, required=True)
    evaluation = commands.add_parser("evaluate-synthetic")
    for name in ("endpoint", "scores", "output"):
        evaluation.add_argument("--" + name, type=Path, required=True)
    replay = commands.add_parser("inspect")
    replay.add_argument("record", type=Path)
    args = parser.parse_args(argv)
    try:
        if args.command == "prepare":
            record = prepare(args.source_snapshot, args.approval)
            save(record, args.output)
        elif args.command == "evaluate-synthetic":
            record = evaluate_synthetic(
                load(args.endpoint), historical._parse(historical._read(args.scores))
            )
            save(record, args.output)
        else:
            record = load(args.record)
        print(
            json.dumps(
                inspect(record), ensure_ascii=False, sort_keys=True, allow_nan=False
            )
        )
    except (Error, OSError, ValueError) as error:
        print(
            json.dumps(
                {
                    "status": "rejected",
                    "code": getattr(error, "code", "invalid_data"),
                    "detail": str(error),
                }
            ),
            file=sys.stderr,
        )
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
