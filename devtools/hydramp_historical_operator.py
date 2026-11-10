"""D48 codec qualification and separately authorized fixed historical scoring.

No flag creates execution permission. A future real scoring receipt must bind
the exact frozen ready plan, actual code and native inputs; D48 is insufficient.
"""

import argparse
import importlib.util
import json
import sys
import warnings
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


ROOT = Path(__file__).resolve().parents[1]
core = module(
    "_historical_receiving", Path(__file__).with_name("hydramp_historical_real.py")
)
process = module("_historical_supervision", ROOT / "src/peptidemt/_hydramp_process.py")
WORKER = Path(__file__).with_name("hydramp_historical_native_worker.py")


def write_new(path, value):
    with Path(path).open("x", encoding="utf-8") as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2, allow_nan=False)
        stream.write("\n")


def pins():
    return {
        "operator": core.identity(__file__),
        "worker": core.identity(WORKER),
        "receiver": core.identity(core.__file__),
        "evaluation": core.identity(core.evaluation.__file__),
        "data": core.identity(core.data.__file__),
        "supervision": core.identity(process.__file__),
    }


def attribution(case, operations):
    """Reuse the host's public-Ackredit bridge after confirmed child operations."""
    from importlib.metadata import version

    from peptidemt._attribution import _capture
    from peptidemt._diagnostics import HydrAMPAttributionWarning

    proposal, _ = core.raw_case(case)
    bibliography = []
    for provider, name, url in (
        ("legacy", "HydrAMP", "https://github.com/szczurek-lab/hydramp"),
        ("modern", "hydramp-torch", "https://github.com/uibcdf/hydramp"),
    ):
        reached = [op for op in operations if op.startswith(provider + "_")]
        if reached:
            observed = proposal["profiles"][provider]["inventory"][name]
            bibliography.append(
                {
                    "item": {
                        "id": "software:" + name + ":" + observed,
                        "type": "software",
                        "title": name,
                        "version": observed,
                        "url": url,
                    },
                    "roles": ["executed_software"],
                    "context": {
                        "completed_operations": reached,
                        "reference_source_commit": proposal["original_commit"],
                        "executed_codec_source": core.data._parse(case["audit_json"])[
                            "selected_source"
                        ][provider + "_codec"],
                        "executed_wheel_sha256": proposal["profiles"]["modern"][
                            "wheel"
                        ]["sha256"]
                        if provider == "modern"
                        else None,
                        "scope": "native codec"
                        if all("encoding" in op for op in reached)
                        else "native MIC head",
                    },
                }
            )
    scoring = [op for op in operations if op.endswith("_MIC_scoring")]
    if scoring:
        bibliography.append(
            {
                "item": {
                    "id": "doi:10.1038/s41467-023-36994-z",
                    "type": "article",
                    "title": "Discovering highly potent antimicrobial peptides with deep generative model HydrAMP",
                    "doi": "10.1038/s41467-023-36994-z",
                    "year": "2023",
                    "journal": "Nature Communications",
                },
                "roles": ["scientific_criterion", "software_description"],
                "context": {"completed_operations": scoring},
            }
        )
    return _capture(
        operations,
        bibliography,
        {"name": "PeptideMT", "version": version("peptidemt")},
        core.object_digest(
            {"case": core.object_digest(case), "operations": operations}
        ),
        "peptidemt.historical_hydramp_qualification",
        HydrAMPAttributionWarning,
    )


def verify_files(items):
    for item in items:
        observed = core.identity(item["path"])
        core.require(
            all(observed[k] == item[k] for k in observed),
            "changed_pinned_file",
            item["path"],
        )


def preflight(case):
    proposal, _ = core.validate_case(case)
    audit = core.data._parse(case["audit_json"])
    # These are opaque hash checks, not model or array loading.
    verify_files(audit["legacy_source_files"] + audit["modern_source_files"])
    verify_files([v["python"] for v in proposal["profiles"].values()])
    core.require(
        process.available_memory() >= 8 * 1024**3,
        "host_resource_guard",
        "At least 8 GiB available RAM before an owned child",
    )
    return proposal


def validate_retry(case, previous, text):
    """Record a fresh bounded attempt under explicit or standing authority."""
    core.validate_case(case)
    core.require(
        type(text) is str,
        "codec_retry_authority",
        "Declared codec-only execution authority required",
    )
    receipt = core.data._parse(text)
    core.require(
        receipt.get("schema")
        == "peptidemt.hydramp_historical_codec_retry_authorization@1"
        and core.authorized_execution_record(receipt)
        and receipt.get("stage") == "legacy_codec_retry"
        and receipt.get("case_sha256") == core.object_digest(case)
        and receipt.get("previous_capture_sha256") == core.object_digest(previous)
        and receipt.get("implementation_pins") == pins()
        and receipt.get("children") == 1
        and receipt.get("neural_evaluations") == 0
        and type(receipt.get("reply_reference")) is str
        and bool(receipt["reply_reference"].strip()),
        "codec_retry_authority",
        "Wrong/missing new codec-only approval; D48 cannot be reused",
    )
    core.require(
        previous["supervision"].get("returncode") != 0
        and previous["command"][5] == "codec",
        "codec_retry_authority",
        "Retain the failed original codec attempt",
    )
    return core.digest(text.encode())


def one_child(
    case, provider, mode, directory, plan=None, authority_text=None, retry=None
):
    """One bounded attempt; exclusive claims preserve execution history."""
    proposal = preflight(case)
    if mode == "score":
        core.execution_authority(plan, authority_text)
        verify_files(plan["pins"].values())
        verify_files(proposal["assets"])
    else:
        core.require(
            mode == "codec" and plan is None and authority_text is None,
            "mode_authority",
            "Only codec work has D48 authority",
        )
    if retry is not None:
        core.require(
            mode == "codec" and provider == "legacy",
            "codec_retry_authority",
            "Only the failed original codec may be proposed for retry",
        )
        retry_id = validate_retry(case, retry[0], retry[1])
    directory = Path(directory)
    directory.mkdir()
    if mode == "codec":
        authority = core.data._parse(case["authority_json"])
        claim_name = (
            "codec-spent-" + provider
            if retry is None
            else "codec-retry-spent-legacy-" + retry_id
        )
        claim = Path(authority["approved_contract_copy"]["path"]).parent / (
            claim_name + ".json"
        )
        write_new(
            claim,
            {
                "directory": str(directory.resolve()),
                "provider": provider,
                "retry": False,
                "worker": core.identity(WORKER),
                "model_allowance": 0,
            },
        )
    write_new(
        directory / "attempt.json",
        {
            "mode": mode,
            "provider": provider,
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "retry": False,
            "model_allowance": 0
            if mode == "codec"
            else (4 if provider == "legacy" else 8),
        },
    )
    request = {
        "case": case,
        "provider": provider,
        "plan": plan,
        "execution_authority_json": authority_text,
        "worker_sha256": core.identity(WORKER)["sha256"],
    }
    request_path = directory / "request.json"
    write_new(request_path, request)
    command = [
        proposal["profiles"][provider]["python"]["path"],
        "-I",
        "-S",
        "-B",
        str(WORKER.resolve()),
        mode,
        "--request",
        str(request_path.resolve()),
        "--output",
        str(directory.resolve()),
    ]
    limits = SimpleNamespace(
        min_available_memory_bytes=8 * 1024**3,
        min_free_disk_bytes=2 * 1024**3,
        threads=1,
        wall_seconds=180,
        rss_stop_bytes=2 * 1024**3,
        max_output_bytes=64 * 1024**2,
    )
    supervision = process.supervise(
        command, directory, limits, include_supervisor_rss=True
    )
    write_new(directory / "supervision.json", supervision)
    result = directory / "result.json"
    raw = core.data._read(result).decode() if result.exists() else None
    if supervision.get("failure") is not None or supervision.get("returncode") != 0:
        from peptidemt._diagnostics import HydrAMPFailureWarning

        warnings.warn(
            HydrAMPFailureWarning(
                stage=provider + "_" + mode,
                cause_type=str(supervision.get("failure") or "worker_failure"),
            ),
            stacklevel=2,
        )
    capture = {"raw_json": raw, "supervision": supervision, "command": command}
    if mode == "codec":
        capture["worker"] = core.identity(WORKER)
    write_new(directory / "capture.json", capture)
    return capture


def retry_codec(case, previous, text, directory):
    validate_retry(case, previous, text)
    return one_child(case, "legacy", "codec", directory, retry=(previous, text))


def receive_codecs(case, captures):
    record = {
        "schema": core.CODECS,
        "case": case,
        "captures": captures,
        "attribution": {
            "status": "pending_capture",
            "completed_operations": [],
            "bibliography": [],
        },
    }
    core.validate_codecs(record)
    record["attribution"] = attribution(
        case, [p + "_native_input_encoding" for p in core.PROVIDERS]
    )
    return record


def qualify_codecs(case, directory):
    core.validate_case(case)
    directory = Path(directory)
    directory.mkdir()
    write_new(
        directory / "campaign-attempt.json",
        {
            "stage": "D48_codec_only",
            "retry": False,
            "case_sha256": core.object_digest(case),
            "children_cap": 2,
            "neural_allowance": 0,
        },
    )
    captures = {}
    for provider in core.PROVIDERS:
        captures[provider] = one_child(case, provider, "codec", directory / provider)
        facts = captures[provider]["supervision"]
        if facts.get("failure") is not None or facts.get("returncode") != 0:
            write_new(
                directory / "incomplete.json",
                {"status": "failed_no_retry", "captures": captures},
            )
            raise core.Error(
                "codec_process", "Retain failed codec attempt; no automatic retry"
            )
    record = receive_codecs(case, captures)
    core.save(record, directory / "codecs.json")
    return record


def freeze(codecs):
    core.validate_codecs(codecs)
    ready = {
        "schema": core.READY,
        "codecs": codecs,
        "pins": pins(),
        "proposal_sha256": core.PROPOSAL_SHA,
    }
    core.validate_ready(ready)
    return ready


def run_scoring(plan, authority_text, directory):
    core.execution_authority(plan, authority_text)
    verify_files(plan["pins"].values())
    directory = Path(directory)
    directory.mkdir()
    write_new(
        directory / "execution-attempt.json",
        {
            "ready_plan_sha256": core.object_digest(plan),
            "execution_authority_json": authority_text,
            "retry": False,
        },
    )
    captures = {}
    for provider in core.PROVIDERS:
        captures[provider] = one_child(
            plan["codecs"]["case"],
            provider,
            "score",
            directory / provider,
            plan,
            authority_text,
        )
        if captures[provider]["raw_json"] is None:
            write_new(
                directory / "incomplete.json",
                {
                    "status": "partial_raw_evidence_no_complete_comparison",
                    "captures": captures,
                },
            )
            raise core.Error(
                "incomplete_worker",
                "No complete worker record; preserve stage/intent/event files, do not retry",
            )
        raw = core.data._parse(captures[provider]["raw_json"])
        if not raw.get("schema"):
            write_new(
                directory / "incomplete.json",
                {"status": "worker_failed_before_scoring", "captures": captures},
            )
            raise core.Error("incomplete_worker", "Model/engine failure is not absence")
        core.check_capture(plan, provider, captures[provider], "learned_model")
    completed = [
        p + "_native_MIC_scoring"
        for p in core.PROVIDERS
        if core.data._parse(captures[p]["raw_json"])["events"]
    ]
    credit = attribution(plan["codecs"]["case"], completed)
    record = core.receive(plan, authority_text, captures, "learned_model", credit)
    core.save(record, directory / "comparison.json")
    return record


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="action", required=True)
    preparation = commands.add_parser("prepare")
    for name in ("proposal", "authority", "endpoint", "audit", "output"):
        preparation.add_argument("--" + name, type=Path, required=True)
    codec = commands.add_parser("qualify-codecs")
    codec.add_argument("--case", type=Path, required=True)
    codec.add_argument("--directory", type=Path, required=True)
    freezing = commands.add_parser("freeze")
    freezing.add_argument("--codecs", type=Path, required=True)
    freezing.add_argument("--output", type=Path, required=True)
    receiving = commands.add_parser("receive-codecs")
    for name in ("case", "legacy-capture", "modern-capture", "output"):
        receiving.add_argument("--" + name, type=Path, required=True)
    retrying = commands.add_parser("retry-codec")
    for name in ("case", "previous-capture", "retry-authority", "directory"):
        retrying.add_argument("--" + name, type=Path, required=True)
    scoring = commands.add_parser("run-scoring")
    for name in ("plan", "execution-authority", "directory"):
        scoring.add_argument("--" + name, type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        if args.action == "prepare":
            result = core.prepare(
                args.proposal, args.authority, args.endpoint, args.audit
            )
            core.save(result, args.output)
        elif args.action == "qualify-codecs":
            result = qualify_codecs(core.load(args.case), args.directory)
        elif args.action == "freeze":
            result = freeze(core.load(args.codecs))
            core.save(result, args.output)
        elif args.action == "receive-codecs":
            result = receive_codecs(
                core.load(args.case),
                {
                    "legacy": core.data._parse(core.data._read(args.legacy_capture)),
                    "modern": core.data._parse(core.data._read(args.modern_capture)),
                },
            )
            core.save(result, args.output)
        elif args.action == "retry-codec":
            capture = retry_codec(
                core.load(args.case),
                core.data._parse(core.data._read(args.previous_capture)),
                core.data._read(args.retry_authority).decode(),
                args.directory,
            )
            if (
                capture["supervision"].get("failure") is not None
                or capture["supervision"].get("returncode") != 0
            ):
                raise core.Error(
                    "codec_process",
                    "New single attempt failed; preserve evidence, no further retry",
                )
            raw = core.data._parse(capture["raw_json"])
            core.check_tokens(core.load(args.case), "legacy", raw["native"])
            print(
                json.dumps(
                    {
                        "status": "legacy_codec_attempt_complete",
                        "neural_calls": raw["neural_calls"],
                    }
                )
            )
            return 0
        else:
            result = run_scoring(
                core.load(args.plan),
                core.data._read(args.execution_authority).decode(),
                args.directory,
            )
        print(json.dumps(core.inspect(result), ensure_ascii=False, allow_nan=False))
    except (core.Error, OSError, ValueError, KeyError, TypeError) as error:
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
