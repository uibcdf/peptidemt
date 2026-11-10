# HydrAMP AMP numerical differences: mechanism and causal trace

Status: **approved pretrained trace completed; final sigmoid explains ten changed pair relations**,
2026-11-03. Provider owner: [uibcdf/hydramp #1](https://github.com/uibcdf/hydramp/issues/1);
consumer commission: [PeptideMT #8](https://github.com/uibcdf/peptidemt/issues/8), D39.

The investigator requests explaining the differences and explicitly authorizes
reporting them in the owned fork, retaining demonstrated modern numerical
improvements where justified. This does not establish full-model superiority,
admit every dev3 deviation or authorize an unspecified number of learned calls.
The fork now has Issues enabled by the investigator; #1 supersedes the earlier
provider-handoff limitation. No issue is published to an external upstream.
The [provider preparation update](https://github.com/uibcdf/hydramp/issues/1#issuecomment-6612315093)
and [consumer handoff](https://github.com/uibcdf/peptidemt/issues/8#issuecomment-6612316275)
are verified in the [publication receipt](evidence/hydramp_amp_issue_updates.json).

## What is established without learned weights

The [ranking relevance review](hydramp_rank_relevance.md) shows identical original
head tokens but changed global AMP near-tie relations. The prior decoder FP64
diagnostic does not qualify these AMP-head computations. Source inspection now
identifies distinct float32 CPU sigmoid implementations:

- The installed TensorFlow 2.2.1
  [sigmoid functor](https://github.com/tensorflow/tensorflow/blob/v2.2.1/tensorflow/core/kernels/cwise_ops.h)
  uses Eigen's float logistic specialization. Its installed header describes a
  vector rational approximation and early positive cutoff; the exact header hash
  is recorded in the [probe receipt](evidence/hydramp_amp_sigmoid_probe.json).
- The installed PyTorch 2.15.0+cpu wheel identifies commit
  `d0f2af8b66b20da4baa50644c0cd3f887a2eae2e`; its
  [CPU kernel](https://github.com/pytorch/pytorch/blob/d0f2af8b66b20da4baa50644c0cd3f887a2eae2e/aten/src/ATen/native/cpu/UnaryOpsKernel.cpp)
  uses an exponential/reciprocal expression. The TensorFlow source matches the
  installed functor header, ignoring terminal whitespace; source bytes are pinned.

One standalone CPU activation call in each frozen framework on **272 artificial
float32 logits**, with weights/PCA/artifacts blocked, yields **185 differing
outputs**. Against the NumPy FP64 reference, modern has lower absolute error at
162 points, legacy at 23, with 87 ties. Maximum errors are approximately
`7.6234e-8` modern and `1.4450e-7` legacy. Two FP64 formulations agree to
`2.22e-16` absolute and round identically on nonnegative inputs.

An additional [80-digit Decimal/libmpdec reference](evidence/hydramp_amp_decimal_reference.json), using exact conversions of
the same artificial binary inputs, independently confirms the 162/23/87 counts.
It evaluates no model, weights or real hidden activations. This is high finite
precision, not a formal exact-arithmetic proof.

| Artificial logit | Legacy TF float32 | Modern Torch float32 | FP64 reference |
| --- | ---: | ---: | ---: |
| 14 | 0.9999991059303284 | 0.9999991655349731 | 0.9999991684719722 |
| 16 | 1.0 | 0.9999998807907104 | 0.9999998874648379 |

The legacy kernel also has a monotonicity counterexample in this grid: raising
the input from `13.999999046325684` to `14.0` lowers its output from
`0.9999992847442627` to `0.9999991059303284`. Modern has no decrease in this
sample. A mathematically increasing sigmoid should not produce that decrease;
this demonstrates a concrete legacy numerical artifact independent of weights.
The probe workers completed in 2.11 s / 1.92 s, CPU-only, with approximately
293/239 MiB sampled RSS, one numerical thread and no network or retry.

**Interpretation:** retaining modern operation-level accuracy is supported on these
cases. It is not established that modern is always more accurate, that the entire
head/model is improved, or that every real rank change is caused by final sigmoid.
Sigmoid is also used inside recurrence; dot products and tanh may contribute.
Do not alter the port merely to reproduce the demonstrated legacy artifacts.
Any production change or broader scientific acceptance still needs investigator
review, preserving the existing numerical and observable FAIL reports.

## Executed diagnostic: original token contexts

The [prepared trace receipt](evidence/hydramp_amp_trace_preparation.json) binds plan
SHA-256 `0e8b7b09234f92991f2f41e33b9b2f6f306986046674ca91d6d9b3122f0c93b5`.
Task: `local_data/hydramp-head-cause-2q_m3p18`; one approved attempt per engine completed.
The [authorization](evidence/hydramp_amp_trace_authorization.json) and
[execution receipt](evidence/hydramp_amp_trace_execution.json) retain exact counts,
sources, environments, resource observations and output hashes.

Candidate stays **hydramp-torch 0.0.0.dev3**, wheel SHA-256
`81761e0d48d92f0956e0afc28b3b4154f16032de53c666fd2cfbb53606102ed7`.
Reference source/starter remain `6590d2f4c2963f25d30669052a4c4a857e0e7279` /
`7804df862872ccc6d09fe01c41bafbca194cfa31`. No scientific source, weights,
descriptor, preprocessing, selector or installed environment is changed.

Reuse the **twelve original sixteen-row token batches** containing all eighteen
affected occurrences: seeds 1001,1002,1003,1004,1006,1007,1008,1009,1010,1012,
1013,1014. All **192 original token contexts** and saved AMP/MIC endpoints are
frozen before execution. This is post-hoc causal localization, not new latent
sampling or an unbiased additional validation cohort.

Capture the actual embedding, first LSTM, pooling, second LSTM, dense pre-sigmoid
logits and final AMP output. Native uses the original graph tensors through
`K.function`, matching the pinned Keras prediction input/learning-phase handling;
no new Dense computation is substituted. Port taps the unchanged paired-head
method. Every captured AMP endpoint must reproduce its saved value **bitwise**;
the port also reproduces its unavoidable MIC pass. Otherwise stop and preserve
partial evidence without a correction/retry. A native failure prevents port work.

| Declared operation | Count |
| --- | ---: |
| Native AMP forwards | 12 |
| Modern AMP forwards | 12 |
| Modern MIC forwards (unchanged paired API) | 12 |
| **All learned network forwards** | **36** |
| Modern sigmoid replay vectors, sixteen values each | 24 |
| Parameter-free FP64 sigmoid formula vectors, 384 retained logits each | 2 |
| New decoder/encoder/PCA/generation/descriptor/Macrel evaluations | 0 |

Native constructs the original full component graph set once; only AMP executes.
Port constructs the unchanged strict core once. No PCA pickle/numeric archive is
deserialized or evaluated, no prior is sampled and no new checkpoint is acquired.
Byte-hash preflight still verifies the original pinned bundle. The additional
sigmoid probes apply the modern kernel to both native and modern captured logits,
preserving each sixteen-row shape. Own-logit replay must reproduce the modern
score bitwise. This separates the final-kernel contribution at fixed logits from
upstream logit changes; it does not make the FP64 activation a whole-head oracle.

The approved report was designed to quantify the first differing stage, compare final activations
at identical native logits, decompose the score difference and inspect which of
the ten pair relations are reproduced by changing the final kernel alone. Original
FAILs, raw values and D35/M1–M8 remain unchanged. No rounding, new ranking rule,
prefilter or scientific correction is included.

## Prepared controls and executed resource boundary

Use two sequential model workers: affinity CPU 0/1, one numerical thread, nice 10,
**180 s each / 360 s model-worker total**. The saved-output/FP64 report has a
separate **30 s** limit, so **390 s total including analysis**. Preserve the
**4 GB task RAM intent** with **2 GiB sampled worker RSS stop**, separately measured
supervisor and **8 GiB virtual ceiling** for model workers; the latter is not RAM
allocation. Report runs under a 1 GiB address-space ceiling. Require 8 GiB available
host RAM and 1 GiB free workspace disk, with a 128 MiB output stop. No GPU,
network, concurrent model worker, training, automatic retry or budget refill.

**Sixteen guarded artificial PyTorch/controller checks pass.** The native original
NoConvAMPClassifier zero-weight graph smoke also passes: all six captured shapes
match and its two artificial AMP predictions have bitwise-identical endpoints.
The initial wrapper session-API error, a timeout during high host I/O pressure
and Keras raw-output metadata restriction are retained. Only the instrument was
corrected: raw tensors use the backend function rather than requiring Keras layer
metadata. No third-party component, runtime or real scientific output was patched.

Both isolated interpreter entrypoints are explicit, with prefix/inventory checks;
published Pytest Receptor 1.2.2 is used for the artificial pytest checks. The reused
frozen supervisor has a specialized explicit-token byte preflight, retaining its
source/asset checks and attempt/resource controls without an unrelated latent/PCA
fixture. Byte-only preflight and source hashes bind the concrete plan; a digest
flag is not investigator approval. The subsequent explicit investigator approval
authorized precisely this prepared trace, which has now completed.

The exact approved learned/activation allowance is now fully consumed. No further
learned/reference evaluation or retry follows from this result.
The current source/use scope is unchanged local research, with original notices;
Drive-versus-starter byte identity and full H0–H4 receiving remain pending. All old
model allowances remain exhausted. No scientific acceptance, package/model
publication, commit or push follows. Retain exact resources/evidence for review
by 2026-11-13 and recheck shared-host resources, including I/O pressure, at launch.

## Measured causal result — 2026-11-03

Both engines completed once, with **all twelve AMP endpoints bitwise identical
to their saved campaign values**. The paired modern MIC endpoints and all twelve
own-logit sigmoid replays also reproduce their saved endpoints bitwise. The
instrument therefore preserves the tested original computation. The 192 rows
are selected original contexts, not an independent validation sample.

| Observed surface | Maximum absolute native/modern difference |
| --- | ---: |
| Embedding | 0 (bitwise identical) |
| First LSTM | 1.9297003746032715e-6 |
| Pool | 1.8477439880371094e-6 |
| Second LSTM | 1.7434358596801758e-6 |
| Dense logits | 5.4836273193359375e-6 |
| AMP output | 8.344650268554688e-7 |

The first **recorded layer** difference is the first LSTM. This does not identify
an individual recurrent primitive or timestep; matrix accumulation, sigmoid and
tanh remain possible contributors there.

At exactly the native saved logits, replacing only the final sigmoid with the
modern kernel changes **120/192 scores** and reproduces **all ten previously
changed AMP pair relations**. The score decomposition into fixed-logit kernel
change and upstream-logit change has zero residual. Thus the final-kernel switch
is sufficient to reproduce these ten relations; it is not proof that all score
differences originate exclusively in that kernel.

The two FP64 final-activation formulations agree within `1.11e-16`. Against the
FP64 activation evaluated on each engine's **own FP32 logits**, maximum error is
`1.546973398269813e-7` native versus `7.723589601216219e-8` modern; 88/192 native
and 117/192 modern values equal the respective FP64 result rounded to float32.
These conditional references do not independently evaluate the entire head.

For the ten affected relations, both conditional FP64 references agree:

- Modern corrects **one native order reversal**. For this pair the two engines'
  logits are bitwise identical, establishing a final-activation ordering artifact
  in the original runtime on a real retained context.
- Modern splits **two native ties** in the FP64 direction.
- Modern creates **seven ties** where FP64 retains a strict relation and native
  has that same strict direction. Modern is therefore not uniformly better at
  preserving strict global ordering. These ties are not declared scientifically
  acceptable or automatically justified by correct float32 rounding.

Model workers used **42.09 s / 48.38 s**, about **415/264 MiB sampled worker RSS**,
with separately sampled supervisor peaks around **24.3/24.5 MiB**. The controller's
`RUSAGE_CHILDREN` value includes descendants and is not exclusive supervisor RAM.
The saved-trace report took **24.33 s**, with **62.4 MiB** child RSS high-water.
Model plus report elapsed time was **114.81 s**, within the 390 s envelope. All
stages exited zero; no resource stop, retry, GPU computation or new generation
occurred. The shared-host timings do not establish a performance improvement.

**Disposition:** the demonstrated legacy final-sigmoid artifact should not be
copied into production merely to force matching values. At this trace checkpoint, whole-head numerical
superiority/equivalence remained unestablished; the subsequent full-head reference
is reported below. Biological prediction and generative efficacy need separate
scientific evidence.
No runtime source/wheel, equation, weight, tolerance, ranking policy or selector
was changed. Original probability/global-rank FAILs, D40's limited scope and
pending H0–H4 receiving remain intact. All **36 learned forwards, 24 sigmoid
replay vectors and two FP64 activation vectors** are spent.

The [provider execution update](https://github.com/uibcdf/hydramp/issues/1#issuecomment-6612701937)
and [consumer receiving update](https://github.com/uibcdf/peptidemt/issues/8#issuecomment-6612708223)
were fetched back and verified exactly; the [publication receipt](evidence/hydramp_amp_trace_execution_issue_updates.json)
records both comment identities and the owning issue's updated checklist.

The subsequent [full AMP-head FP64 reference](hydramp_amp_reference.md) has now
completed its separately approved 24-forward plan. Modern has lower aggregate
maximum/mean/RMS error at every nontrivial recorded stage on this cohort; AMP is
closer in 91 cases, original in 58, with 43 ties. Seven modern rank ties persist.
This extends the numerical evidence to the whole AMP head on retained inputs,
without general/biological acceptance. Both exact allowances are exhausted.
