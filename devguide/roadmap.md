# Preliminary roadmap

Status: **proposal**, with no dates or implementation authorization.
Navigation: [index](README.md) · [decisions](decisions.md).

The tracks below are incremental capabilities, not a commitment to one
demonstrator or a redesign-only entry point.
The separate [future horizons review](future_horizons.md) records potential
chemical, mechanistic, multi-state, delivery, experimental and interactive
extensions plus design stress tests. They do **not** extend this preliminary
implementation plan or authorize work.

| Stage | Candidate deliverable | Evidence to retain |
| --- | --- | --- |
| 0. Design | Test accepted problem/plan/evidence, proposal/realization, function/resource, capability/composition and evaluation/selection semantics with cases; compare strategies without choosing an API. | D09–D28, conceptual counterexamples, investigator decisions and preserved audit. |
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
P08's conceptual separation and qualified guidance are accepted under D17–D20;
concrete catalogs, evidence encodings, interfaces and reward policies remain open.
The [five-strategy comparison](generative_strategies.md) is pending analysis under
P05, not a definitive generator or mandatory implementation sequence. This
roadmap does not authorize programming.

P09's conceptual organization and seven principles are accepted under D25–D26;
operation-specific contracts/interfaces remain future work. The bounded V0.2
review introduces no new implementation stage or MVP requirement. P04 is the
[current discussion block](open_questions.md#p04-proposed-discussion-sequence),
now examined in [evaluation_and_selection.md](evaluation_and_selection.md),
starting with evaluation meaning and constraints/evidence before selecting
multiobjective or diversity policies. The library distinction P10 stays pending.

P04 alternative 2 and its seven principles are accepted under D27–D28, with no
mandatory classes/states or global project-interpretation engine. The X/Y case
continues the pending restriction/check/evidence discussion; no selectivity
threshold, optimization policy or implementation deliverable is adopted by it.

Before Python implementation, agree formal admission to MolSysSuite and use
its official registered-component starter. Pin model/license/weight provenance
and select in-process, subprocess or service adapters from real environment
requirements. Plan Recorda/Praxis integration without requiring Nextia or an
agent runtime to exist.
