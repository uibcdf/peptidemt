# Historical HydrAMP endpoint: verified target provenance and proposed study

Status: **source audit complete; scientific endpoint/evaluation proposal v1,
not approved**, 2026-11-05. Owner:
[HydrAMP #3](https://github.com/uibcdf/hydramp/issues/3); consumer:
[PeptideMT #32](https://github.com/uibcdf/peptidemt/issues/32).
This follows the [data receiver](hydramp_historical_data.md) and retains D46's
approved entity/sequence view. It changes no source record, receiver pin,
model, public admission, selector or accepted execution allowance.

## Verified source meaning

The [evidence receipt](evidence/hydramp_historical_endpoint_review.json) pins
the exact external sources, local notebooks, read-only analysis and outputs.
Source inspection and independent data reconstruction establish this chain:

| Stage | Meaning established by the inspected source | Consequence |
| --- | --- | --- |
| GRAMPA loader | Standardize concentration to µM, then store log10 of that number; `unit` still says `uM` | The numeric `value` column is logged, not a directly usable unlogged physical quantity |
| HydrAMP data preparation | Filter source records, select E. coli, then average `value` by literal sequence | This averages logged values: algebraically the log of a geometric mean of the source molar values, not an arithmetic mean of original MICs |
| MIC training notebook | Label the aggregate with strict `value < 1.5`; append assumed-negative examples and oversample positives | A coded classifier target, not direct MIC regression or guaranteed calibration on measured records |
| Native/modern MIC head | Final sigmoid classifier output, with larger score corresponding to the coded positive class | Retain a dimensionless score; do not apply an inverse sigmoid to invent a physical MIC |
| Historical experimental table | Strain-specific MIC displayed in µg/mL, with numeric values or explicit bounds | A distinct measurement/estimand, not automatically the native class target |

Primary implementation sources are GRAMPA
[`src/load_data.py`](https://github.com/zswitten/Antimicrobial-Peptides/blob/a6819dcd671291af8013627a2d2fbc32858346bc/src/load_data.py)
and HydrAMP's
[preparation notebook](https://github.com/szczurek-lab/hydramp/blob/6590d2f4c2963f25d30669052a4c4a857e0e7279/scripts/dataset_preparation.ipynb)
and [classifier notebook](https://github.com/szczurek-lab/hydramp/blob/6590d2f4c2963f25d30669052a4c4a857e0e7279/scripts/mic_classifier_training_prodecure.ipynb).
No upstream function/notebook is imported or executed.

The [article Methods](https://www.nature.com/articles/s41467-023-36994-z)
instead describes the training cutoff in µg/mL and uses a non-strict inequality.
The supplied PDF's page 17 was rendered and visually checked: this is not just
an XML extraction artefact. The contradiction is retained. It does not authorize
changing the port, archived values or checkpoint definitions to match prose.

## Independent reconstruction of the published aggregate

Only the public GRAMPA CSV was acquired, at commit
`a6819dcd671291af8013627a2d2fbc32858346bc`. Its 7,830,941 bytes match Git blob
`f9fe90dbe3c07b0c4d9bdd9550ce6071dc9db908`; SHA-256 is
`9e33122afb3bdd169e8bed620b1040bf1601d60cf25b6c8c8d9870bf37522b6f`.
Five relevant source files also match their pinned Git blobs. Two initial text
copies had an added final newline; exact-byte acquisition corrected those copies
and retained the originals of that copying step for provenance.

Standard-library CSV/Decimal analysis reconstructs the notebook's filtering and
arithmetic aggregation of already-logged numbers. It selects **8,049 records**
and **4,546 literal sequences**, with no missing/nonfinite selected values.
All 4,546 strings match `data/mic_data.csv` in the already accepted Zenodo ZIP;
none is missing in either direction. Maximum absolute aggregate difference is
**7×10⁻¹⁶**. The 1e-12 diagnostic comparison bound concerns decimal/float source
serialization only; it is not a changed model probability tolerance or biological
acceptance criterion.

This verifies the published data convention and aggregate correspondence, not
the accuracy of every original source conversion or the fitting history of a
particular checkpoint.

Applying the notebook's literal length and strict cutoff to the archived numbers
gives **3,444 rows: 2,126 below 1.5 and 1,318 at or above it**. None equals 1.5.
The source reconstruction changes no such classification. These are diagnostic
counts of an existing training-source rule, not labels adopted for the historical
experimental panel or proof of checkpoint-specific fitting history.

Across the 4,546-group source aggregate, 604 groups contain multiple nonempty
**literal strain strings**, 3,356 of its 8,049 selected rows have an empty strain
field, and 466 groups contain both True and False
amidation flags. Literal strain names have not been harmonized into biological
identities; flags are source metadata, not a newly verified chemical identity.
These facts reinforce that the aggregate is not one named chemical entity in
one ATCC 25922 assay.

The loader's mass-concentration conversion uses `ProteinAnalysis(sequence)`
without passing its amidation metadata. This demonstrates a sequence-based
conversion convention, not an exact experimental-entity mass. Some source values
may already be molar; this review neither estimates the number affected nor
calculates a terminal correction. A future physical-mass route must use MolSysMT
and adequate entity information; units remain PyUnitWizard's responsibility.
Do not transplant the upstream conversion code into PeptideMT.

## Recommended first endpoint for investigator review

Use **descriptive discrimination of the paper's reported ATCC 25922 activity**,
defined prospectively as displayed MIC **≤32 µg/mL**. Use the native MIC-head
score as a ranking score, with larger scores oriented toward activity. This
changes the question to historical assay discrimination; it does not reconstruct
the trained molar class or establish calibrated probabilities.

This recommendation deliberately requires no mass/unit conversion. A separate
future analysis could compare a properly specified physical molar target or the
legacy source convention, but those require different scientific definitions
and provenance. D46's sequence view does not approve an unmodified mass proxy.

The candidate policy below is **for review only**. No labels, eligibility flags
or native payloads have been written into the authoritative 42-row data or the
existing receiver. Counts use only the saved, hash-verified data report; no model
scores or outcomes informed the candidate criterion.

| Candidate source criterion | Observation bookkeeping | Raw-string groups with stable reported class | Conflicting groups |
| --- | --- | --- | --- |
| ≤32 µg/mL, recommended primary | 15 reported active / 27 inactive | 12 active / 26 inactive = **38** | Hydraganan-2: 16 versus 128 µg/mL |
| ≤128 µg/mL, audit comparison only | 25 reported active / 17 inactive | 22 active / 17 inactive = 39 | None |

The 128 criterion is shown to expose the endpoint choice, not to improve class
balance or provide an authorized secondary metric. It is not selected for the
proposed model comparison. Do not choose a more favorable criterion after scores.
The primary has only 12 positive groups: it **does not meet** the broader C2
proposal's 16-per-class recommendation or qualify that unapproved 128-case study.

## Censoring and repeated observations

Use a reported-value convention, not invented experimental uncertainty:

1. A displayed numeric value is classified by the proposed ≤32 rule as reported.
   Do not silently reinterpret it as an exact continuous concentration or invent
   a half-dilution interval, standard error or replicate distribution.
2. For `MIC > L`, the reported class is definitely inactive under this criterion
   when L ≥32. If L <32, it remains undetermined. All seven current bounds are
   `>512`, so their proposed reported class is inactive without substituting 512
   for the unknown MIC. No arithmetic or rank position is assigned to the bound.
3. Keep all **42 source observations** and their values/chemistry. For the primary
   binary summary, use one descriptive raw-string group only when all its source
   observations give the same determinate reported class. This grouping does
   not assign molecular identity or independent experimental units.
4. Retain Hydraganan-2's two rows and flag the conflict. Exclude its group from
   the proposed primary binary metric with that explicit reason; do not average,
   prefer the lower value or choose a table. Pexiganan and Hydraganan-1 retain
   both differing values but have stable reported class under this criterion.

Thus the source ledger stays at 42, while the **proposed** primary metric has
38 raw-string groups. No overlapping source-pool group is removed to manufacture
independence. Source/preselection bias and unresolved fitting/fragment exposure
remain visible. Report the excluded group's model behavior separately if a later
execution is approved, without choosing a primary class for it.

## Proposed comparison statistic and its limits

Report original and modern **ROC-AUC** on the same proposed 38 groups, and their
paired difference. AUC measures score ordering and can use unthresholded scores;
it does not require treating the scores as calibrated probabilities. This is
consistent with the [official metric contract](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html).
There are 312 positive–negative comparisons, not 312 independent samples.
Use raw returned precision, exact score ties and the conventional half-credit
for ties; no epsilon, rounding, score threshold, inversion, recalibration or
cutoff tuning. Retain the actual paired scores and every changed pair relation.

This is a descriptive conditional result on a selected historical panel.
Do not attach an independence-based confidence interval, population performance,
statistical significance, formal equivalence, noninferiority or clinical claim.
No absolute pass threshold or equivalence margin is justified by this review.
Both implementations could discriminate poorly; numerical fidelity and assay
discrimination require separate descriptions. The AMP head may supply transfer
evidence, not truth for general AMP membership; higher MIC is not general
AMP-negative ground truth.

Use one specified score per raw-string group for the proposed metric; preserve
the many-to-one observation links. Exact canonical native inputs, any prediction
reuse, batches/order and duplicate/batch-context handling must be fixed in the
later execution plan. A shared projected string does not prove equal native
token arrays: internal zeros from generation differ from canonical post-padding.
Do not reuse a generated score solely on string equality. Reuse the owner's
codec when separately commissioned; do not create a local encoder.

Prespecify an **ambiguity sensitivity** for Hydraganan-2: additionally report
the 39-group AUC under each of its two observed-class scenarios, with its class
set first to inactive and then to active. Neither scenario becomes an adopted
truth or replaces its two source observations. Show both results and their
sensitivity range, not a preferred result or a confidence interval. For the
original–modern contrast, apply the **same scenario to both engines** and show
both paired differences; do not subtract unrelated per-engine extreme bounds.
This retains visibility of the potentially favorable exclusion without changing
the primary 38-group endpoint or adding the 128 µg/mL criterion.

## Decision requested and next authorized boundary

Approval is requested for the **≤32 reported-activity endpoint, explicit
conflict/censoring policy and descriptive paired ROC-AUC study with the two
ambiguity scenarios** above, and the
bounded **data-only endpoint/evaluation implementation with artificial-score
tests** described below. This remains uncommissioned until that decision.

The proposed developer-side cycle would:

1. Receive the unchanged D46 snapshot and an explicit endpoint approval record;
   derive a separate source-linked endpoint record while retaining all 42
   observations, the proposed 38-group eligibility and the conflict reason.
   Do not write native class labels into the existing receiver or source data.
2. Receive paired, explicitly artificial score vectors for controlled tests,
   keyed to exact raw-string groups. Reject missing/foreign IDs, changed scope,
   nonfinite scores or invented native/model provenance. No native token or
   learned score is prepared by that cycle.
3. Reuse a supported statistics routine for the proposed paired AUC report,
   preserving raw scores, exact ties, source links, excluded groups and the
   conditional interpretation, including both shared ambiguity scenarios.
   Do not add a local generic AUC algorithm.
4. Verify synthetic perfect/reversed/tied rankings, exact pairing, immutable
   source data and saved replay under model/parameter/network/dispatch guards.
   These would be algorithm/receiving checks, not measured biological results.

The generic metric provider/dependency route still needs actual technical
qualification before use. That is delegated implementation work within these
obligations, not a new scientific endpoint or package architecture. No new
public API, generic methodology system or permission to fit/calibrate a model.

Shared-profile metadata reports scikit-learn **1.9.1**, matching the inspected
official metric contract; no statistics routine is imported or called here.
Praxis's current README keeps reusable methodology/catalogue promotion separate
from scientific APIs. This proposal promotes no generic Praxis Protocol and
creates no new methodology service. Actual numerical-provider qualification
remains a bounded implementation check, not a claim from metadata alone.

Such approval would not supply real scores, model loading, native payloads,
GPU, training, new generation, independent-cohort qualification or a release.
Any real comparison still requires an exact bundle/input/batch/host/call plan
and separate execution approval. The molar-target/calibration C2 question remains
separate. Preserve D35/M1–M8, D41/D44/D45/D46 and all exhausted budgets.

No upstream issue or author contact is made. The owned fork's #3 and consumer
#32 retain the documentation/target-provenance discrepancy. Public availability
and the inspected sources do not complete every incorporated database's use/
redistribution review. Current delivery is source evidence and this proposal;
the existing receiver and its accepted 38 tests are unchanged and not rerun.
