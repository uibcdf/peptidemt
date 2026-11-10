# HydrAMP modernization: broader confidence campaign

Status: **approved execution complete; numerical and global AMP pair diagnostics FAIL**,
2026-11-03. Provider: investigator-owned HydrAMP fork; consumer: PeptideMT #8 / D39.
The investigator instructed proceeding with the confidence expansion, aiming for
the confidence warranted by the original on the ported route. No dev3 scientific
acceptance, D40 extension or unspecified additional calls follow.
The [published preparation update](https://github.com/uibcdf/peptidemt/issues/8#issuecomment-6610438413)
is verified in its [publication receipt](evidence/hydramp_confidence_issue_update.json).

## Executed outcome — 2026-11-03

The [published outcome](https://github.com/uibcdf/peptidemt/issues/8#issuecomment-6610652523)
is verified in its [execution publication receipt](evidence/hydramp_confidence_execution_issue_update.json).

The investigator explicitly approved the exact CPU plan and bounds. The
[authorization](evidence/hydramp_confidence_authorization.json) and
[execution receipt](evidence/hydramp_confidence_execution.json) bind the run to the
unchanged plan below. Both workers completed once, exit 0, without resource stops:
**132 network forwards, 34 public generation calls and 34 descriptor bundles**.
This allowance is exhausted; no additional model call, correction or retry ran.

- All **7,700 paired token positions**, including repeats/controls, agree.
  Distinct-input coverage is **256 latent inputs / 6,400 positions**.
  All seventeen public batches per implementation have identical sequence/order/
  occurrence views and all five descriptors. No actual public batch order changed.
- Every AMP/MIC score remains within the unchanged band. Maximum differences are
  `8.344650268554688e-7` / `2.5033950805664062e-6`. Both workers repeat the first
  seeded batch bitwise, including full return records. Core partition/reorder/
  duplicate controls preserve tokens and head pair relations in both workers.
- The **unchanged probability diagnostic remains FAIL**: 421/161,700 values
  outside band including reuses; 346/134,400 on distinct inputs alone. Maximum
  difference is `2.2727251052856445e-4`, larger than in the earlier fixture. Minimum
  native token margin is `1.9609928131103516e-5`; fourteen positions are at/below
  `1e-2`, three at/below `1e-3`, two at/below `1e-4`. All observed margins exceed
  twice their corresponding local probability perturbation; none changed token.
- The **global AMP pair-relation criterion also FAILS**. Of 32,640 pairs, one
  reverses, two native ties split and seven port ties appear. All ten pairs involve
  different public batches and different peptides/tokens, with AMP scores near 1
  and gaps at about `6e-8`–`1.2e-7`. Example: native scores
  `0.9999725818634033` / `0.9999727010726929` swap in the port. MIC has zero pair
  changes. These are genuine global ranking differences, not changed within-batch
  returned order. The report's observable verdict remains **false**; do not relabel
  it merely because each public batch agrees.
- The native reference itself has batch-size-dependent probabilities: the
  three-row partition has five values outside the same diagnostic band relative
  to its original sixteen-row batch, while retaining tokens/order. Both engines
  show small score/layout variations. This demonstrates reference sensitivity;
  it does not prove the primitive responsible for cross-engine differences.

Measured worker wall time / sampled worker peak RSS: original **53.874 s /
524.64 MiB**, modern **14.516 s / 403.68 MiB**, total **68.39 s** below 360 s.
Import/construction/collection regions are retained separately; this one shared-
host sample is not a stable speedup estimate. The old outer-supervision field
`supervisor_maxrss_bytes` uses `RUSAGE_CHILDREN`, which can include descendants;
it is not exclusive supervisor RAM. Modern exclusive controller RSS/HWM was also
observed (~25.39 MiB). No instantaneous whole-task/kernel RAM cap is claimed.

Assessment: substantially broader evidence for sequence/return fidelity and
repeatability on the ported route, with a retained internal numerical deviation
and demonstrated global near-tie ranking sensitivity. The exact comparisons and
case IDs are saved locally. Float32 sensitivity is a plausible explanation, not
a proven individual arithmetic cause or permission to round scores/change
selectors. Keep both FAIL verdicts, all thresholds, previous evidence and D40's
original twelve-input scope. Broader scientific disposition, asset provenance
and PeptideMT H0–H4 receiving remain pending; no universal equivalence is claimed.

The subsequent [ranking relevance review](hydramp_rank_relevance.md) examines all
saved-score cutoffs without another model call. Global AMP-only top-k membership
changes by one occurrence at k=2,5,9,10,23,42,50; this diagnostic is separate from
PeptideMT's Macrel/hemolysis selectors. Its limited dev3 disposition is proposed
for investigator decision, not accepted or a reclassification of either FAIL.

## Approved specification retained from preparation

The following specification was prepared before execution and then approved as
the exact bounded run above. It is retained for audit, not permission to rerun.

## Question, candidate and reference

Does the modern implementation preserve observable results on broader fixed inputs
and introduce no observed decision/occurrence changes under declared batch layouts?
This concerns deterministic, unfiltered AMP generation. Other HydrAMP features,
antimicrobial efficacy and safety are not qualified by computational fidelity.

Reuse the [completed comparison](hydramp_full_comparison.md) and
[FP64 diagnostic](hydramp_numeric_reference.md), without repeating accepted cases.
The candidate remains **hydramp-torch 0.0.0.dev3**, wheel SHA-256
`81761e0d48d92f0956e0afc28b3b4154f16032de53c666fd2cfbb53606102ed7`.
Only developer validation tools/tests are added; the numerical core, generation,
PCA, weights and descriptor definitions remain unchanged.

Reference source: `6590d2f4c2963f25d30669052a4c4a857e0e7279`; starter:
`7804df862872ccc6d09fe01c41bafbca194cfa31`. Fifty tracked original amp/licence
files and all sixty-five selected artifact digests remain preserved. Both workers
use the same publisher-attributed epoch-37 bundle. Its byte identity against the
original Google Drive archive remains unverified; this comparison does not settle
that provenance gap. Local research/use conditions and attribution are unchanged;
no redistribution, commercial/output-rights clearance or broader adoption follows.

## Exact inputs and calls

Task: `local_data/hydramp-confidence-pvxbhixg`; plan SHA-256:
`eec881986bdacd41b3409a9de33afecc5460ce561d8d6e319ffebb1c576a7b59`.
The [preparation receipt](evidence/hydramp_confidence_preparation.json) pins inputs,
tools, environments, candidate, checks and retained evidence.

- Seeds **1001–1016**, sixteen normal latent rows of width 64 per seed:
  **256 distinct inputs**, fixed before any new model load. NumPy 1.18.5 and
  2.4.6 model-free probes produce identical raw bytes and NPY files. Raw array
  SHA-256: `661b644ad19f328c2c89a8796cc59adf108fca2c3387c0c6d3042f017c738fb2`.
- Seventeen public generation calls per worker: sixteen batches plus a repeat of
  seed 1001, with `softmax=True, mode='amp', filter_out=False, properties=True,
  n_attempts=1`. Preserve original descriptor parameters explicitly.
- Five core controls per worker reuse the first batch's measured PCA values:
  partitions **1 + 3 + 12**, reverse sixteen rows and duplicate indices
  **[0, 1, 0, 1]**. Each evaluates decoder/AMP/MIC once. These are core layout
  controls, not extra public seeded-generation calls or descriptor bundles.
- Per worker: **272 public occurrences + 36 control occurrences**. There are
  **7,700 paired token positions including reuse**, with **6,400 positions from
  256 distinct inputs**. Neither token positions nor seed-derived cases are
  independent biological trials; this sample supplies no universal error bound.

| Operation | Original | Modern | Total |
| --- | ---: | ---: | ---: |
| Public generation calls | 17 | 17 | 34 |
| Additional core layout batches | 5 | 5 | 10 |
| Decoder forwards | 22 | 22 | 44 |
| AMP-head forwards | 22 | 22 | 44 |
| MIC-head forwards | 22 | 22 | 44 |
| **All network forwards** | **66** | **66** | **132** |
| Descriptor bundles | 17 | 17 | 34 |
| PCA inverse transforms | 17 | 17 | 34 |

One generator/core construction per worker; one original PCA pickle load and one
existing numeric PCA load, no coefficient export. Original encoder graph
construction entails **zero encoder forwards**. No warm-up, public-fixture head
rerun, new FP64 evaluation, Macrel, training or retry/refill. Separate H2/H4 designs
are not consumed or silently revised by this migration campaign.

## Measurement and review

Provider tool `ports/pytorch/devtools/confidence.py` reuses frozen `parity.py`.
Byte-only preflight verifies sources, wheel, assets, numeric PCA and extra pins.
Taps reserve each phase/row/call before execution and retain original tokens for
head attribution. Failures restore methods and preserve partial data; one-attempt
files prevent automatic reruns. Reports read saved arrays without engine imports.

- Compare inputs/PCA, all probabilities/tokens, native scores, occurrence counts,
  actual native order, strings and five descriptors. Align scientific fields by
  occurrence even if order changes. Keep `atol=2e-6, rtol=2e-5` for probability/head
  diagnostics and the `1e-10` PCA band; descriptor/occurrence checks remain exact.
- Keep numerical and observable verdicts separate. A tiny error changing a token,
  tie or order cannot be hidden by passing a numerical band. Preserve every FAIL;
  do not change thresholds after results. Broader acceptance is an investigator
  disposition, not a report boolean or automatic D40 extension.
- Report minimum token margins per seed, largest discrepancies and counts of
  margins at/below `1e-2`, `1e-3`, `1e-4`, plus margins not above twice their local
  perturbation. These are descriptive bins, not new acceptance thresholds.
  Report absent near-tie coverage; no additional seed search follows automatically.
- Inspect **32,640 pair relations per head** across the distinct inputs, including
  reversals, split native ties and new port ties. MIC ordering is diagnostic;
  AMP remains the commissioned ordering key, and selectors are unchanged.
- Compare repeat bit patterns/records and layout effects within each worker as
  well as across engines. Distinguish native batch effects from port changes.
  Existing artificial duplicate/zero/tie/error contracts are retained, not relabeled
  as observed pretrained coverage. Any changed scientific result needs review.
- Measure import, provider/model construction and collection regions separately,
  plus whole-worker wall/RSS. This is an instrumented shared-host observation,
  not a general speed benchmark. Preserve the old worker's native metadata
  discrepancies; the same modern 41-distribution profile remains unchanged.

## Proposed execution limits

- Two workers **sequentially**, affinity CPU 0/1, one numerical thread, nice 10;
  batch at most sixteen, **CPU only**, no network or concurrent scientific worker.
- **180 seconds per worker, 360 seconds total**, with no automatic retries.
- Preserve the **4 GB task RAM intent**: stop above **2 GiB sampled worker RSS**,
  measuring the supervisor separately. The **8 GiB virtual address-space** ceiling
  is not physical RAM allocation or an instantaneous kernel RSS cap.
- Require **8 GiB host RAM available** before/during execution, **1 GiB disk free**
  before launch and at most **128 MiB task outputs**. Preserve all stops/partials;
  a failed/stopped reference worker prevents the modern stage.

The host preflight observes ten physical cores/twenty threads, approximately
30.7 GiB RAM and ample workspace disk. The available-RAM floor is satisfied;
swap is nearly full, so retain the RSS stop and recheck resources at launch.
This reserves no resources. Legacy TensorFlow may log a failed CUDA probe even
with actual computation forced to CPU, as already observed.

## Preparation checkpoint and remaining boundary

**31 artificial checks pass**: 28 initial checks, then three added approval/pin/count
guards without repeating the accepted initial checks. Coverage includes call caps,
input/head attribution, partial preservation, tiny-error token flips, tie changes,
descriptor/return corruption, repeat bits and incomplete data. Real scientific
artifacts/providers and network are blocked. Both interpreters parse the worker,
raw inputs match, byte-only preflight and lint/format pass. That preparation
checkpoint loaded no learned model/PCA and ran no descriptor/Macrel call; the
subsequent separately authorized execution is recorded above.

The investigator subsequently approved this exact candidate, 132-forward allowance
and resource limits under [the working instructions](../AGENTS.md). It is now
exhausted. No scientific acceptance, commit, push, package release or raw-sequence
publication follows. New model evaluations require a new exact finite approval.
Source and existing concurrent work remain local and preserved. Retain task
resources for review by 2026-11-13.

After review, a bounded port-fidelity disposition can precede the separate portable
PeptideMT provenance, direct/adapter receiving and H0–H4 integration with Macrel
and selectors. Experimental benchmarks and laboratory validation require their
own scientific design. HydrAMP–Macrel agreement is not independent biological
evidence and cannot establish better peptides than the original.
