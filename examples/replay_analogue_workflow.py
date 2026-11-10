"""Inspect saved analogue ancestry and optional assessment; no model execution."""

import argparse
import json
from dataclasses import asdict
from pathlib import Path

from peptidemt import HydrAMPAnalogueReceipt, ResultSet, select


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("receipt", type=Path)
    parser.add_argument("--assessment", type=Path)
    parser.add_argument("--k", type=int, default=4)
    args = parser.parse_args()
    receipt = HydrAMPAnalogueReceipt.from_json(args.receipt.read_text(encoding="utf-8"))
    output = {
        "generation_evidence_kind": receipt.provenance.evidence_kind,
        "receipt_id": receipt.content_id,
        "issues": receipt.issues,
        "parents": [asdict(o) for o in receipt.outcomes],
        "new_model_or_assessment_calls": 0,
    }
    if receipt.issues:
        print(json.dumps(output, indent=2))
        return 2
    inputs = receipt.proposals()
    output["candidate_links"] = [asdict(link) for link in receipt.links]
    output["proposed_occurrences"] = len(inputs)
    if args.assessment:
        results = ResultSet.from_json(args.assessment.read_text(encoding="utf-8"))
        if results.inputs != inputs:
            raise ValueError("Assessment inputs/ancestry differ from this generation")
        output["assessment_evidence_kind"] = results.provenance.evidence_kind
        output["selection"] = {
            policy: list(select(results, policy=policy, k=args.k).selected)
            for policy in ("amp-first", "hemolysis-first")
        }
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
