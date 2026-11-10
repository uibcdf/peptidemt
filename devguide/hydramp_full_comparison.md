# Original-versus-modern HydrAMP: full comparison

Status: **authorized execution completed; internal probability diagnostic remains FAIL**,
2026-11-03. PeptideMT #8 / D38–D40. No new scientific acceptance or superiority claim.
The [published preparation update](https://github.com/uibcdf/peptidemt/issues/8#issuecomment-6596674337)
and [provider feedback](https://github.com/uibcdf/molsysmt/issues/485#issuecomment-6596675645)
are verified in the [publication receipt](evidence/hydramp_full_comparison_issue_updates.json).
The [executed-result update](https://github.com/uibcdf/peptidemt/issues/8#issuecomment-6609787381)
is verified in its [separate receipt](evidence/hydramp_full_comparison_execution_issue_update.json).

## Executed outcome — 2026-11-03

The later [broader confidence campaign](hydramp_confidence_campaign.md) extends
coverage to 256 distinct latent rows and reveals global AMP near-tie pair changes.
Its separate approved allowance/outcome does not rewrite this twenty-input record.

The investigator explicitly instructed continuation in response to the exact
execution approval request. The [authorization](evidence/hydramp_full_comparison_authorization.json)
binds that approval to unchanged plan SHA-256
`b019e1dfa4e8c61ed667198b73dd7b09dfb5308459225399c84c9eb54beae929`.
Both scientific workers completed successfully, once, without a resource stop.
The [execution receipt](evidence/hydramp_full_comparison_execution.json) pins all
outputs/logs, resource observations and the original comparison's **exit 1**.
The frozen plan retains its historical proposed status; separate approval and
execution records establish what actually ran.

**Observed result fidelity is favorable on this finite fixture:**

- Exactly **22 network evaluations**, six generation calls and six generation
  descriptor bundles executed. One original PCA pickle load, one existing numeric
  PCA load, three inverse transforms per worker; no encoder forward, training,
  Macrel, retry, new export or GPU computation.
- **36 paired generation occurrences** returned (4 + 16 + 16 per implementation),
  representing **20 distinct latent inputs** because sixteen are an intentional
  repeat. All **900 token positions**, projected strings, actual native return
  indices and requested/returned counts match. Do not describe these as 36
  independent latent cases or 72 independently validated peptides.
- Raw sampled coordinates and PCA outputs are exact. All five native descriptors
  match exactly for every paired returned occurrence, including the repeated case.
- Generation AMP/MIC maximum score differences are `2.980232238769531e-7` /
  `5.960464477539062e-7`, within the unchanged head band. The separate eight-row
  input-string head control also passes (maxima `2.384185791015625e-7` /
  `1.1920928955078125e-7`). Archived hidden decoder tokens are not inferred.
- Same-seed native return dictionaries repeat exactly in each implementation.
  The saved raw latent/PCA/probability/head/order array bit patterns also repeat
  exactly within each worker. This says nothing about every seed/platform.

**Overall diagnostic result remains FAIL:** 58/18,900 internal decoder probability
values exceed unchanged `atol=2e-6, rtol=2e-5`; maximum absolute difference
`4.845857620239258e-5`. Counts include the intentional repeat: smoke has 2/2100,
then each size-16 call has 28/8400. The largest difference equals that observed in
the earlier core comparison. All token decisions remain unchanged; all 900 native
margins exceed twice their observed local probability perturbation. The minimum
observed top-two margin is approximately 0.0240; near-tie generalization remains
unestablished. No threshold or failed historical result is reclassified.

D40 remains its original limited dev0/twelve-input disposition. Assistant
assessment: this is evidence for native observable-result fidelity of dev3 on
these twenty latent cases, with a documented internal probability deviation.
It is a recommendation for investigator review, **not automatic broader dev3
acceptance**, H0–H4 completion or proof of improved biological peptide quality.
No code, other component, scientific definition or weights were changed to force
a pass. All original files, versions, environments and failures remain preserved.

### Runtime and memory observations

| Observation | Original | Modern dev3 |
| --- | ---: | ---: |
| Whole scientific worker | 16.524 s | 22.543 s |
| First generation, n=4 | 2.719 s | 0.445 s |
| First generation, n=16 | 1.305 s | 0.040 s |
| Same-seed repeat, n=16 | 1.229 s | 0.026 s |
| Sampled worker RSS peak | 527.22 MiB | 439.05 MiB |
| Conservative worker + supervisor peak | 550.19 MiB | 462.07 MiB |

Workers used **39.07 s total**, below 360 s, and RAM stayed well below the 4 GB
intent. Modern public generation calls were faster and its sampled RSS lower in
this observation, while **whole-worker time was longer**. Setup/import and model
construction were not timed separately; they cannot be inferred individually by
subtracting generation times because the total also includes head controls and
output/instrumentation. This is a timing-instrumentation limitation, not a reason
to rerun models without a new allowance. Single shared-host instrumented runs,
first-call effects and native logging do not establish a stable general speedup.

No GPU computation occurred. The legacy TensorFlow binary logged a failed CUDA
probe (`CUDA_ERROR_NO_DEVICE`, no `/dev/nvidia0`); actual work was forced to CPU.
Do not equate that with the absence of every driver probe.

The allowance is **exhausted**. No automatic rerun, additional diagnostic,
new model call or larger tolerance follows. Remaining work: investigator review
of this broader result; PeptideMT adapter and portable result/provenance/attribution;
actual direct/adapter receiving and remaining H0–H4 scientific acceptance. No
commit, push, package release or model redistribution is claimed.

## Preparation checkpoint — before the authorized execution

A separate `peptidemt-pytorch-comparison` worktree preserves all prior versions.
The candidate is **hydramp-torch 0.0.0.dev3**, wheel SHA-256
`81761e0d48d92f0956e0afc28b3b4154f16032de53c666fd2cfbb53606102ed7`.
Its decoder/head source, numeric PCA and generation wrapper are byte-identical
to dev2, which retains the original dev0 equations. The added explicit
`Modlamp433Properties` route uses modlAMP **4.3.3**. All fifty tracked original
amp/licence files still match upstream `6590d2f4c2963f25d30669052a4c4a857e0e7279`.
D40 remains limited to its original twelve-input dev0 deviation.

The isolated Python 3.14.7 profile retains all seventeen old base external versions,
including NumPy 2.4.6 and CPU PyTorch 2.15.0. With the properties extra, **41
installed distributions have clean native dependency closure**. No old dependency
metadata override is applied. modlAMP 4.3.3 makes MySQL optional; this is an
observed selected profile, not a public multi-platform support claim.

Modern modlAMP defaults differ from the reference: charge defaults to pH 7.4,
and pI defaults to amidation. The adapter explicitly preserves original HydrAMP
**charge pH 7 / amide=True, pI amide=False**, plus the original Eisenberg scale
and moment settings. It delegates calculations to the provider, with no copied
physicochemical formulas. These descriptor assumptions do not assign known
terminal chemistry to a generated molecular proposal. Modern sequence handling
and pI bracket initialization also differ in source; universal equivalence is
not presumed. Reusable scientific operations remain tracked in MolSysMT #485.

### Published reference and model-free descriptor check

Only the original `results/hydra_unconstrained.csv` member was obtained from
[Zenodo](https://zenodo.org/records/7420278/preview/results.zip?include_deleted=0):
19,799 bytes, SHA-256
`571cefae116331c26b846161940e206a14b063a18b2b730dc4e1584b1189e369`.
Two bounded HTTP ranges transferred **77,692 bytes**, including ZIP metadata;
the 378 MB archive was not downloaded. Member size/CRC and actual-byte SHA are
retained; the full archive MD5 has **not** been verified.

The file has 149 data rows. The fixture takes rows 0–6 and repeats row zero:
eight occurrences, seven distinct strings, lengths 9–17, fixed without selecting
by scores. No training dataset was acquired. `h_score` is preserved in the raw
source but excluded from the accepted native five-descriptor contract.

Two model-free descriptor bundles were executed sequentially under the current
instruction to resolve descriptors and fix the reference subset. Their operational
bounds were selected for preparation: eight occurrences each, one CPU worker at a
time, affinity 0/1, one native thread, nice 10, 120 s each, sampled RSS stop 1 GiB,
8 GiB virtual ceiling and 8 GiB available-host-RAM floor; no network/GPU/retry.
Both completed without a stop (12.88 s / 10.97 s, sampled peak RSS approximately
131 / 205 MiB). Deep-learning imports and scientific artifact deserialization were
blocked. **No neural model or PCA was loaded or evaluated.**

For all eight occurrences, the five fields match **exactly** across original
HydrAMP/modlAMP 4.2.3, the explicit modern route and the archived scalar values:
length, hydrophobicity, hydrophobic moment, charge and isoelectric point.
The duplicate also matches exactly. This is regression evidence on these inputs,
not independent predictive validation, global descriptor equivalence or full
HydrAMP acceptance. The [descriptor receipt](evidence/hydramp_descriptor_qualification.json)
retains the method, resource limits, acquired-source provenance and hashes.

The archived AMP/MIC scores are not taken as golden classifier values: original
hidden decoder tokens/configuration are not recoverable merely from strings.
The later head control uses the original explicit input-string codec and exactly
replays those padded token values in the modern worker.

### Preparation checks

- **76 installed-wheel artificial checks pass** for the core, generation and both
  provider call contracts. Actual descriptors/providers, real artifacts and
  network are blocked in this synthetic suite.
- **13 final controller tests pass** with artificial endpoints/weights, covering
  public-call taps, original order capture, exact input guards, pre-call blocking
  of additional model evaluations, restoration after failure, partial evidence
  and detection of differing/truncated saved results.
- Nine installed wheel payload members match the exact candidate. Native closure
  and byte-only model/worker/fixture preflight pass. Shared and earlier environments
  remain unchanged; code and reports remain local/uncommitted.

The [preparation receipt](evidence/hydramp_full_comparison_preparation.json) pins
candidate, source, environments, tests, source review and the exact pending plan.

## Exact approved neural comparison — retained plan

This is the historical approved specification. Both one-attempt stages below
have already executed; this block is not permission to rerun them.

Immutable local plan: `local_data/hydramp-comparison-qnbdpism/plan.json`, SHA-256
`b019e1dfa4e8c61ed667198b73dd7b09dfb5308459225399c84c9eb54beae929`.
The operator bound the separate investigator approval record to these exact
bytes before either `run-stage`. A digest flag alone was not treated as approval.

Original source: `6590d2f4c2963f25d30669052a4c4a857e0e7279`; official starter:
`7804df862872ccc6d09fe01c41bafbca194cfa31`. Reuse the existing 65-file asset
manifest, original Python 3.8 worker and previously exported numeric PCA. No new
checkpoint or training data is acquired and no new PCA export is needed.

| Per implementation | Requested outputs | Seed | Purpose |
| --- | ---: | ---: | --- |
| First generation | 4 | 101 | Small complete native return |
| Second generation | 16 | 202 | Broader matched input fixture |
| Third generation | 16 | 202 | Same-seed repeat on the same loaded worker |
| Separate native-head control | 8 published occurrences | None | Same original input-string tokens to both heads |

All generation calls retain `softmax=True`, `mode='amp'`, `filter_out=False`,
`properties=True`, `n_attempts=1`. There are **six generation API calls total**,
72 requested returned occurrences, plus four separate head evaluations on the
published fixture. This is **22 network forward evaluations**: six decoders,
eight AMP-head and eight MIC-head evaluations. There are **six new descriptor
bundles**, inside the generation calls; the already completed eight-row scalar
check is reused, not repeated. This allowance is separate from the unspent
D38 direct/PeptideMT-adapter four-call design; it does not qualify that adapter.

Load one native generator (its encoder graph is constructed, with zero encoder
forward evaluations) and one modern core. One original PCA pickle load is proposed
in the legacy worker; modern reads the existing pinned numeric PCA archive.
Each worker makes three inverse transforms. Raw 36x64 float64 latent bytes are
predeclared before model loading and checked against actual seeded draws.

Capture actual decoder/head outputs without extra inference. Native ordering
comes from the real pandas `nlargest` result indices, not guessed sequence
identity. The modern public method yields its actual occurrence mapping.
Taps restore methods on failure, block unplanned extra model calls **before**
execution and retain completed arrays/results if a later calculation fails.

### Host and stopping limits

- Two workers **sequentially**, one at a time, CPU affinity 0/1, one native thread,
  nice 10. **No GPU, network, training, retry/refill or additional model.**
- **180 seconds per worker, 360 seconds total**. All initial/repeated predictions
  are counted; there is no free model warm-up.
- Preserve the investigator's **4 GB task RAM intent**. Sample worker RSS every
  0.1 s and stop above **2 GiB**; measure the small supervisor separately. The
  **8 GiB virtual** ceiling is not RAM allocation; no kernel group/RSS cap is claimed.
- Require at least **8 GiB host RAM available** before/during execution, 1 GiB free
  disk before launch and a 128 MiB scientific-output stop.
- Each stage has a one-attempt file. A failed native stage prevents the modern
  stage. Preserve stops/errors and partial evidence without automatic rerun.

### Measurement and acceptance boundaries

Compare raw latents/PCA, captured probabilities/tokens, occurrence order, both
native scores, descriptor values, full return records and within-worker repeat.
Keep the original probability/head/PCA diagnostic bands and report every failed
criterion; descriptor differences are reported explicitly without a retrospective
larger tolerance. The existing failed reports and D40 scope stay unchanged.

Record startup/load, per-network and whole-return observations separately. First
size-4, first size-16 and repeated size-16 calls are distinct; shared-host/cache
variation and diagnostic taps prevent claiming a robust speedup from this sample.
A faster runtime or higher native score is not evidence of better biological
peptides. No scientific superiority, broader acceptance or complete H0–H4 result
is pre-granted even if all diagnostics pass.

## Execution-budget terminology

In this record, an execution budget means the agreed CPU/RAM/time limits for
this machine plus the finite number of model evaluations. Investigator approval
is the investigator's authorization in this session. A fresh budget means a new
allowance after an earlier one is consumed; it is not a separate permission
request for each call already covered by the approved plan. This explanation
clarifies the existing local qualification rule and changes no governance.

## Current disposition

Both authorized neural stages are complete, and the finite allowance is exhausted.
The earlier plan and prerequisites above are preserved with their actual execution
record. New model calls need a separately approved finite execution budget.
Portable PeptideMT result/provenance, adapter qualification, Macrel integration
and final scientific acceptance remain pending. No model redistribution, public package, commit or push
has occurred. Retain task resources for review by 2026-11-13.
