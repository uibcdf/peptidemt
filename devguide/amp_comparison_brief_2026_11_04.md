# AMP comparison brief: paired sequence-order control

Status: **concrete proposal for scientific review; no execution authorized by
preparation**, 2026-11-04. Owner: [PeptideMT #33](https://github.com/uibcdf/peptidemt/issues/33).
Basis: [worked evidence report](amp_worked_report_2026_11_04.md).

## Question and interpretable contrast

Within the selected experimental HydrAMP/Macrel route, does the generated residue
order provide a different qualified predictive profile from a paired permutation
that preserves length, composition and the first residue? This isolates an
order-related contrast beyond those preserved features. It does not compare an
independently trained generator or establish biological utility in general.

Each generated string is paired with one seeded permutation of positions after
the first residue, retaining the first residue so initial-M incompatibility is
not silently changed between arms. A permutation can equal the original; retain
it without retry or novelty requirements. Empty/unsupported inputs have an
explicit unavailable-control outcome and remain in the accounting. No empirical
negative or inactive label is assigned to a permutation.

This proposed transformation needs an actual supported owner route and a
reviewed scientific definition before implementation. Molecular sequence/system
manipulation remains MolSysMT-owned; inspect its capabilities and report a
missing reusable function there if needed. No local molecular parser, mutation
or permutation utility has been added to PeptideMT. If a suitable route is
unavailable, the control arm is blocked and returns to review rather than being
silently approximated.

## Candidate pilot design

Propose eight declared independent seeded generation blocks, 16 raw occurrences
per block: 128 generated occurrences and at most 128 paired controls. This is a
bounded exploratory pilot, not a powered superiority test or a promise of
precision. The investigator must approve the scientific choices, control and
cost before execution. Generation and control seeds, exact dev3/Macrel assets,
views, descriptors/settings, assessment order and failure handling are frozen
in the eventual execution plan. No reuse of exhausted allowances is implied.

Use the same native Macrel route and both existing selectors at k=4 for the
two arms of each block. Preserve every returned occurrence, incompatible view,
native result and tie rule. Fixed requested counts are not quotas to refill;
source-internal work is reported only where observed. The cost of the shared
generation producing both paired arms is disclosed rather than attributed to
an independent cheap generator.

## Outcomes and decision rule

Primary descriptive contrast: per-block difference in the number of **observed
complete native AMP-positive/NonHemo results per 16 proposed occurrences**.
Alongside it, report counts per assessed occurrence and assessment coverage so
an absent/failed evaluation is not treated as observed inactivity. Do not
replace this metric after seeing all zeros or adopt it as biological acceptance.

Secondary outcomes: paired native-score differences, all native labels,
selection membership, exact-string uniqueness, no-progress/unchanged controls,
failures and actual cost. The eight blocks, with their shared parent pairing,
are the unit for describing run-level variation; do not treat 256 related
sequences as independent biological replicates. No statistical superiority
threshold, calibration claim or effect size is inferred from the old two seeds.

If the primary contrast is uninformative, report that outcome and inspect the
predeclared secondary profiles as exploratory evidence only. A difference would
support further investigation of the named predictive criterion; no difference
would constrain that hypothesis under this control. Either result can motivate
a different assessor/endpoint or independent data review, but cannot establish
experimental equivalence or superiority. Predeclare any later confirmatory
precision/effect requirement using the pilot's cost/data context before another
campaign.

## Execution readiness still required

Before any generation, transformation or assessment: approve the control
scientifically; identify its supported owner implementation; pin exact artifacts,
terms and inputs; audit data dependence/available reference corpora; provide the
actual call ledger, order, installed qualification and shared-host limits.
The earlier CPU-only/4 GB task intent remains guidance, not a fresh call budget.
Do not publish generated sequences, acquire data or contact third parties under
this preparation alone. This proposal can be accepted, narrowed or declined.
