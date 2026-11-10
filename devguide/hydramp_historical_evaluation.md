# Historical HydrAMP endpoint and synthetic-score comparator

Status: **D47 approved; local developer implementation and synthetic controls
pass**, 2026-11-05. This is not an original–modern HydrAMP experiment.
Owners: [PeptideMT #32](https://github.com/uibcdf/peptidemt/issues/32) and the
investigator-owned [HydrAMP #3](https://github.com/uibcdf/hydramp/issues/3).
Independent-product review remains with HydrAMP #4.

## Authority and scientific meaning

The investigator explicitly approves the endpoint/policy and the data-only
comparator implementation using artificial score vectors. The
[D47 authorization](evidence/hydramp_historical_endpoint_authorization.json)
binds proposal SHA-256
`e7bf019ec410bb02ef5a01ee12fba625159d7c71e9b76b704787d9005ed223ed`.
The [source review and proposal](hydramp_historical_endpoint_review.md) retain
their exact pre-approval bytes; their earlier unapproved status is historical.
[D46 receiving](hydramp_historical_data.md) remains unchanged. No native model
input, learned-score receiving or new model allowance is commissioned here.

The endpoint is **reported E. coli ATCC 25922 MIC ≤32 µg/mL**, applied to the
displayed measurements, not a molar conversion or reconstruction of the native
classifier target. Native training uses pooled logged molar measurements; the
source review documents its discrepancy with the paper's training-unit prose.
No inverse score-to-MIC mapping, probability calibration or port correction
follows from this endpoint.

All **42 source observations** remain separate in the embedded unchanged D46
snapshot and endpoint record. The **39 literal source-string groups** are a
finite descriptive grouping, not a claim of chemical identity or independence.
The primary metric uses the **38 groups** whose observations agree in reported
class: **12 active and 26 inactive**. Numeric values at 32 are active; a strict
`>32` lower bound is inactive. A censored bound below 32 would be undetermined;
no bound is replaced by an exact MIC. The seven actual `>512` values are inactive.

Hydraganan-2 retains its conflicting 16 and 128 observations and is excluded
from the primary binary summary. Two additional 39-group scenarios assign it
inactive or active. Each scenario applies the **same class to both score
columns**, yielding two paired differences and their sensitivity range. The
range is not a confidence interval, an adopted truth or a difference formed by
subtracting unrelated scenario extremes. The 128 µg/mL counterfactual endpoint
is not implemented. Twelve primary positive groups do not satisfy the broader
unapproved C2 proposal's 16-positive minimum; this is not a C2 pass.

## Developer implementation and reuse

[`devtools/hydramp_historical_evaluation.py`](../devtools/hydramp_historical_evaluation.py)
reuses the existing D46 receiver for source validation and bounded strict JSON
I/O. It creates a separate endpoint bound to exact D47 authority, without
editing any source label, assay, chemical annotation or source artifact.
Endpoint preparation and inspection use the standard library only.

The comparative statistic delegates to public `sklearn.metrics.roc_auc_score`;
there is no local ROC-AUC implementation. The tool owns the PeptideMT endpoint,
pairing, ambiguity scenarios, interpretation and diagnostic list of positive–
negative pairs whose ordering or exact tie differs between columns. It does
not perform molecular parsing, mass/unit operations, sequence alignment or
model preprocessing. Existing MolSysMT ownership and public admission persist.

The optional [developer qualification profile](../devtools/historical_evaluation_requirements.txt)
records the versions already present in `molsyssuite@uibcdf_3.14`: scikit-learn
1.9.1, NumPy 2.4.6, SciPy 1.18.1, threadpoolctl 3.7.0 and joblib 1.6.0. The metric
source SHA-256 is
`b1d16d4108a66708dd797ecead322f4bfce290d7f08eb2e659eb61721a94ed15`.
The tool verifies these versions and source bytes and limits native numerical
pools to one thread. Missing/import-failed or changed providers are explicit
rejections, without a fallback. A changed profile requires requalification;
these exact pins are a finite developer fixture, not public package dependency
floors or a supported platform matrix. No dependency was installed or public
runtime/Conda recipe changed.

Only vectors declared `synthetic_control` are supported. Every group, including
the ambiguous one, requires exactly one ordered pair of finite numeric values
in [0,1], bound to the complete endpoint digest. Missing, duplicated, reordered,
foreign, coerced or nonfinite scores and model-provenance fields are rejected
before statistical-provider loading. Raw supplied precision and exact ties
are retained; there is no rounding, epsilon, filling or selective case removal.

The two slots are named `original` and `modern` to exercise the intended pairing;
their names do not turn artificial numbers into model outputs. A declared kind
cannot independently prove the origin of arbitrary externally supplied numbers.
The qualified controls below are explicitly fabricated under import/file/call
guards, and every comparison is marked
`synthetic_control_only_not_a_HydrAMP_comparison`. Real learned-score evidence
has no qualified receiving route in this tool.

Saved endpoint and comparison JSON records embed their source/approval text,
derived endpoint, exact score vectors and statistical-provider identity. Every
inspection revalidates sources and authority and recomputes cached results;
modified masks, policy, scores, provider identity or cached statistics cannot
be accepted as an unchanged record. Replay needs the qualified statistics
provider for comparisons, but not the old source paths or model artifacts.
Save uses exclusive creation and never overwrites an existing destination.

## Commands

Use the authorized shared environment. The first command needs the exact
local D46 snapshot, not a substitute panel:

```bash
python devtools/hydramp_historical_evaluation.py prepare \
  --source-snapshot local_data/hydramp-historical-data-4lk7py03/received.json \
  --approval devguide/evidence/hydramp_historical_endpoint_authorization.json \
  --output /tmp/hydramp-reported-endpoint.json

python devtools/hydramp_historical_evaluation.py evaluate-synthetic \
  --endpoint /tmp/hydramp-reported-endpoint.json \
  --scores /tmp/explicitly-artificial-paired-scores.json \
  --output /tmp/hydramp-synthetic-comparison.json

python devtools/hydramp_historical_evaluation.py inspect \
  /tmp/hydramp-synthetic-comparison.json
```

The scores file must contain exactly `schema`, `kind`, `endpoint_sha256` and
`scores`: schema `peptidemt.hydramp_historical_artificial_scores@1`, kind
`synthetic_control`, canonical endpoint SHA-256 and all ordered
`{group_id, original, modern}` rows. The tests and retained qualification script
show construction of fabricated controls. No model/codec command or profile/
authority override exists. Success prints an inspection; data/provider rejection
prints a structured cause to stderr and exits 2. Existing output paths reject.
Ignored local source/control records are not distributed package data.

## Executed evidence and limits

The [implementation receipt](evidence/hydramp_historical_evaluation_implementation.json)
records exact inputs, code, tests, provider, artifacts and commands.
[`devtools/tests/test_hydramp_historical_evaluation.py`](../devtools/tests/test_hydramp_historical_evaluation.py)
has **32 passing controlled cases**, plus one reporting-protocol case: **33
selected tests**, native exit zero through Pytest Receptor. Tests are explicitly
selected developer qualifications, outside the default package test selection;
they require the optional numeric profile. They cover correct/inverted/tied
rankings, the smallest representable score change, paired ambiguity, malformed
pairing, changed authority/provider/cache, CLI rejection and saved replay.
Repository Ruff lint passes; all 178 Python files pass its format check.

One guarded process prepares the actual 42-observation endpoint, saves it,
removes its two disposable input copies and evaluates/replays three fabricated
control pairs. Perfect, reversed and tied controls yield respectively
(1,1), (1,0) and (0.5,0.5) ROC-AUC in every scenario. These values describe the
controls, **not HydrAMP performance**. Saved reports reproduce exactly after
the input copies are removed and other scientific JSON reads are denied.
The qualification delegates 90 statistic calls, with **zero neural/model calls**;
the latter count is not the former. It takes 3.59 s and peaks at 207.54 MiB RSS
on CPU 0/1 with one numerical thread. Model/molecular imports, parameter/PCA
files, estimator fitting/prediction, network and child dispatch are guarded.
No installed scientific package or CI/platform matrix is qualified.

No equivalence margin, biological efficacy, safety, superiority or absolute
quality threshold is established. The historical panel has selected examples,
unknown checkpoint exposure and literal source-pool overlaps; it is not an
independent benchmark, and its 312 primary positive–negative pairs are not 312
independent experiments. Source-use/exposure and assay/chemical qualifications
remain material limits. Native input preparation and actual original–modern
scoring still require a separate exact bundle/input/batch/host/call plan and
investigator approval. Original and modern codec behavior must be reviewed
explicitly; a bare-string match cannot authorize reuse of generated scores.

D35/M1–M8, both selectors, D41/D44/D45/D46 and exhausted execution allowances
persist. This cycle changes no public API, chemistry admission or accepted model
bundle and includes no installation, model work, training, generation, GPU,
commit/push/release or third-party contact. The work remains local/uncommitted.
Retained evidence is owned by HydrAMP #3 / PeptideMT #32; review by 2026-11-19.
