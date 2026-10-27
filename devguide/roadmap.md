# Preliminary roadmap

Status: **proposal**, with no dates or implementation authorization.
Navigation: [index](README.md) · [decisions](decisions.md).

The tracks below are incremental capabilities, not a commitment to one
demonstrator or a redesign-only entry point.

| Stage | Candidate deliverable | Evidence to retain |
| --- | --- | --- |
| 0. Design | Validate the accepted problem/plan/execution-evidence separation with worked cases; resolve minimal semantics without choosing an API. | D09–D13, conceptual counterexamples, investigator decisions and preserved audit. |
| 1. Common evaluation | Family/model bindings, proposal-to-candidate relations, evaluated views, hard constraints, provenance, selection and applicability. Accept supplied/generated and potentially incomplete proposals where evaluators support them. | Reproducible evaluation fixtures, determined/unknown chemistry, attribution limits, unsupported-input behavior and score meaning. |
| 2. Baseline proposal adapters | At least one de novo route and one seed-based route conceptually using the same evaluation/selection layer. Implementation order remains open. | Exact engine/checkpoint/configuration; compared coverage and costs. |
| 3. External optimization | Evolutionary, Bayesian or other black-box search over proposals; preserve edit constraints, diversity and objective vectors. | Matched-budget comparison with generate-and-filter; failures and discarded candidates. |
| 4. Inference-time guidance | Rollout/tree/resampling or compatible gradient methods with family evaluators and target recognition. | Actual sampling intervention, predictor calls, validity, diversity, target-score retention and independent evaluation. |
| 5. Learned conditioning | Reuse an existing conditional model or adapt one only if its benefit justifies new data/training. | Training labels/negatives, data splits, calibration, distribution shift and comparison to unmodified generators. |
| 6. Experimental feedback | Ingest assays and support active selection/retraining when experiments are available. | Assay conditions, replicates, censored results, measured negatives and independent validation. |

## Evaluation before claims

A computational run can complete at any stage without experimental data.
Report actual completion, feasibility, model coverage, score distributions,
diversity, novelty relative to training and reference sequences, target/family
tradeoffs, evaluation count and compute budget. These establish computational
outcomes only.

A target-aware generator plus a family filter is the initial comparison baseline,
not an adopted first implementation. Compare family-first proposals plus
target optimization, target-first proposals plus family optimization, and guided
proposals when supported. Do not compare methods under unmatched budgets or with
the same predictor as both search reward and sole validation oracle.

Use held-out predictors with different data where possible, temporal/clustered
splits and matched-length/composition controls. Experiments are a subsequent
evidence layer, not a definition of computational completion.

## Engineering transition

Follow the [agreed working methodology](design_methodology.md): mature scientific
requirements and acceptance criteria before authorizing a capability, without
prescribing all implementation details. P07's semantic responsibilities are
accepted under D15–D16; concrete identity/representation choices remain open.
P08 remains pending. This roadmap does not authorize programming.

Before Python implementation, agree formal admission to MolSysSuite and use
its official registered-component starter. Pin model/license/weight provenance
and select in-process, subprocess or service adapters from real environment
requirements. Plan Recorda/Praxis integration without requiring Nextia or an
agent runtime to exist.
