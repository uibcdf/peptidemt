"""Replay linked generation/assessment receipts; never invoke a scientific engine.

Supply authorized local JSON files and their reviewed SHA-256 digests. This
example reports occurrence tokens and counts, without printing peptide sequences.
"""

import argparse
import hashlib
import json
from pathlib import Path

from peptidemt import HydrAMPReceipt, ResultSet, select


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--generation", required=True, type=Path)
    parser.add_argument("--generation-sha256", required=True)
    parser.add_argument("--assessment", required=True, type=Path)
    parser.add_argument("--assessment-sha256", required=True)
    parser.add_argument("--k", type=int, default=4)
    args = parser.parse_args()
    try:
        generation_bytes = args.generation.read_bytes()
        assessment_bytes = args.assessment.read_bytes()
        if hashlib.sha256(generation_bytes).hexdigest() != args.generation_sha256:
            raise ValueError("Generation SHA-256 does not match the reviewed file")
        if hashlib.sha256(assessment_bytes).hexdigest() != args.assessment_sha256:
            raise ValueError("Assessment SHA-256 does not match the reviewed file")

        generation = HydrAMPReceipt.from_json(generation_bytes.decode("utf-8"))
        results = ResultSet.from_json(assessment_bytes.decode("utf-8"))
        if not generation.completed or generation.failures or generation.issues:
            raise ValueError(
                "Inspect the incomplete or anomalous generation before replay"
            )
        if generation.inputs != results.inputs:
            raise ValueError(
                "Assessment inputs differ from the complete generation inputs/provenance"
            )
        amp = select(results, policy="amp-first", k=args.k)
        hemo = select(results, policy="hemolysis-first", k=args.k)
    except (OSError, UnicodeError, ValueError, TypeError) as error:
        parser.error(str(error))

    eligible = [results.rows[o.row_index] for o in results.outcomes if o.eligible]
    summary = {
        "mode": "saved-data replay; no scientific engine execution",
        "generation_snapshot": generation.snapshot_id,
        "assessment_snapshot": results.snapshot_id,
        "generation_sha256": args.generation_sha256,
        "assessment_sha256": args.assessment_sha256,
        "proposed_occurrences": len(generation.inputs),
        "eligible_occurrences": len(eligible),
        "excluded": amp.excluded,
        "reported_failures": dict(results.failures),
        "row_anomalies": results.anomalies,
        "eligible_native_labels": {
            "AMP_positive": sum(row.values["is_AMP"] is True for row in eligible),
            "AMP_positive_and_NonHemo": sum(
                row.values["is_AMP"] is True and row.values["Hemolytic"] == "NonHemo"
                for row in eligible
            ),
        },
        "selections": {
            choice.policy: {
                "requested_count": choice.requested_count,
                "ranking": choice.ranking,
                "selected": choice.selected,
                "unselected": choice.unselected,
            }
            for choice in (amp, hemo)
        },
        "new_scientific_calls": 0,
    }
    print(json.dumps(summary, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
