# HydrAMP full AMP-head precision reference

Status: **approved full-head FP64 comparison completed; modern aggregate numerical error lower on this cohort**,
2026-11-03. Provider owner: [HydrAMP #1](https://github.com/uibcdf/hydramp/issues/1).
Consumer commission: [PeptideMT #8](https://github.com/uibcdf/peptidemt/issues/8), D39.

The [completed causal trace](hydramp_amp_numerics.md) explains the ten changed AMP
pair relations through the final sigmoid. It also observes upstream LSTM drift.
An FP64 activation evaluated on existing FP32 logits cannot establish the accuracy
of the whole neural head. This next diagnostic compares the complete nominal AMP
calculation against both retained implementations, including unfavorable results.

## Exact candidate, inputs and arithmetic

The [preparation receipt](evidence/hydramp_amp_reference_preparation.json) pins plan
SHA-256 `3035206916f0a95ef318f02f9195a12edc1ba031bf07584bca9c5d61fe432d3a`.
Task: `local_data/hydramp-amp-fp64-ft8c0prd`; one approved attempt completed.
The [authorization](evidence/hydramp_amp_reference_authorization.json) records
the investigator's direction to continue after the concrete plan was presented;
the [execution receipt](evidence/hydramp_amp_reference_execution.json) retains
all 24 completed forwards, reference arrays, report and resource observations.
Candidate remains **hydramp-torch 0.0.0.dev3**, wheel SHA-256
`81761e0d48d92f0956e0afc28b3b4154f16032de53c666fd2cfbb53606102ed7`.
Source/starter remain `6590d2f4c2963f25d30669052a4c4a857e0e7279` /
`7804df862872ccc6d09fe01c41bafbca194cfa31` and the selected publisher-attributed
epoch-37 checkpoint under unchanged local-research use conditions.

Use the same **twelve original sixteen-row token contexts**, seeds 1001,1002,
1003,1004,1006,1007,1008,1009,1010,1012,1013,1014: **192 retained rows** covering
all eighteen occurrences in the ten changed relations. No new latent, token or
sequence is generated. This selected cohort is post-hoc, not independent coverage.

Load **nine AMP parameter NPY arrays once**, with pickle disabled, checking pinned
bytes, float32 dtype, shape and finiteness. Promote the stored float32 values
exactly to float64; do not retrain or change the original weights. Compute the
unmasked embedding, 25-step 64-unit LSTM, VALID max pool (window/stride 5),
five-step 100-unit LSTM, dense logit and sigmoid. Stored biases already include
the trained forget bias; dropout is inactive at inference. Preserve all original
zero tokens and batch contexts.

Reuse the frozen independent NumPy recurrent reference from the earlier decoder
diagnostic, rather than adding another recurrence implementation. Evaluate two
mathematically equivalent layouts: separate per-gate products and packed products.
Both use NumPy FP64 sigmoid/tanh and BLAS. The two layouts provide a consistency
check, not wholly independent numerical libraries or a formal exact solution.
Neither TensorFlow, PyTorch, HydrAMP model code nor descriptor packages is imported.
The unchanged dev3 candidate is compared through its saved trace, not executed.

| Declared operation | Maximum count |
| --- | ---: |
| Independent FP64 AMP forwards: 12 contexts × 2 layouts | **24** |
| Rows per forward | **16** |
| AMP numeric parameter arrays, loaded once | **9** |
| New TensorFlow/PyTorch network forwards | **0** |
| Decoder/encoder/MIC/PCA/generation/descriptor/Macrel evaluations | **0** |
| Standalone activation replay calls | **0** |
| Retries or budget refills | **0** |

Save every reference stage and progress after each forward, including partial
evidence if execution fails. Report computation uses saved values without extra
learned or activation evaluations. No runtime package source, dependency, equation,
preprocessing, molecular-system handling, descriptor or selector is changed.

## Predeclared comparison and controls

Report both references separately for all six recorded stages: maximum absolute,
mean absolute and RMS error of each engine, and counts where native/modern has
smaller or equal scalar error. Inspect all ten changed pair relations and their
FP64 margins, explicitly retaining new modern ties. Do not select only a favorable
metric, reference or pair.

Reference-layout maximum-absolute consistency controls are zero for embedding,
`1e-10` for LSTM/pool/logits and `1e-12` for AMP. These are diagnostic instrument
checks, **not revised native-versus-port acceptance tolerances**. If consistency
fails, preserve the result without choosing a favorable reference. A pair's
reference-order flag requires matching layout directions and a score margin
larger than twice the observed maximum layout discrepancy; this is a conditional
diagnostic, not a proven error bound for unseen data.

**Seventeen guarded artificial tests pass**, including closed-form LSTM gates/
stored biases, unmasked zero tokens, pooling axes, nonzero two-layout consistency,
exact 24-forward scheduling, failure/partial preservation, altered budget/hash
rejection and reporting a modern tie without hiding it. Tests ran in 5.18 s
including interpreter startup, with about 64.7 MiB kernel child RSS high-water,
in the existing isolated Python 3.14.7 / NumPy 2.4.6 worker. Its seven-distribution
inventory includes pytest 9.2.0 and published Pytest Receptor 1.2.2; engine imports,
network and real scientific artifact opens were blocked. The shared environment
was not changed. Byte-only preflight verifies 22 pinned files and deserializes no
scientific parameter.

## Approved and executed host/call allowance

One worker, CPU affinity 0/1, one numerical thread, nice 10, **180 seconds total
for all 24 forwards and the report**, no GPU/network/retry. Retain the **4 GB task
RAM intent**, with a stricter **512 MiB sampled worker RSS stop** and **1 GiB
virtual address-space ceiling**. The latter is not a RAM allocation. Observe
supervisor memory separately; `RUSAGE_CHILDREN` includes descendants and cannot
be described as exclusive controller RAM. Require **8 GiB available host RAM**,
**1 GiB free disk**, and stop above **128 MiB outputs**. Recheck shared-host
memory, disk and I/O pressure immediately before launch. Use the existing isolated
interpreter entrypoint without resolving its symlink to the shared base Python.

The frozen process supervisor uses one exclusive attempt file and no automatic
retry. A supplied plan digest binds bytes; it does not establish human approval.
The previous trace allowance remains exhausted. The subsequent investigator
direction authorized this exact prepared reference budget, which has now also
been fully consumed. No additional real parameter/model/activation evaluation
or retry follows from either allowance.

The result can support or reject **numerical fidelity on these fixed contexts**.
It cannot establish better biological prediction, new-family generalization,
whole-generator equivalence or full H0–H4 receiving. Original FAIL reports,
diagnostic bands, D35/M1–M8 and D40's limited disposition remain unchanged.
Drive-versus-starter byte identity remains unresolved. No scientific acceptance,
deployment precision change, training, publication, commit or push follows.
Retain exact task resources for review by **2026-11-13**.

The [owning issue preparation update](https://github.com/uibcdf/hydramp/issues/1#issuecomment-6612843872)
and [consumer update](https://github.com/uibcdf/peptidemt/issues/8#issuecomment-6612848660)
were fetched back and verified exactly; the [publication receipt](evidence/hydramp_amp_reference_issue_updates.json)
records their identities and body digests. Those comments record preparation
before the subsequent investigator approval and execution.

## Executed full-head comparison — 2026-11-03

Exactly **24/24 FP64 full AMP-head forwards** completed, with nine parameter
arrays loaded once and **zero new TensorFlow/PyTorch network calls**. No other
model, PCA, descriptor or generator ran. The two FP64 layouts agree **bitwise at
all saved stages** on this cohort. This is a consistency result, not independent
library corroboration: both layouts share NumPy's activation and BLAS primitives.

Modern has lower maximum absolute, mean absolute and RMS error at **every
nontrivial recorded stage** (LSTM1, pool, LSTM2, logits and AMP); both embeddings
are exact. Both reference layouts give the same comparisons. The complete
six-stage metrics and counts remain in the execution receipt.

| Full-head output error versus FP64 | Original TF | Modern Torch | Relative reduction |
| --- | ---: | ---: | ---: |
| AMP maximum absolute | 1.2580579706e-6 | 1.0792440363e-6 | 14.2% |
| AMP mean absolute | 8.6661310827e-8 | 7.2463286623e-8 | 16.4% |
| AMP RMS | 1.6331376140e-7 | 1.3615489328e-7 | 16.6% |
| Logit maximum absolute | 9.1461975549e-6 | 5.8847354349e-6 | 35.7% |
| Logit mean absolute | 1.1304749652e-6 | 8.9949246940e-7 | 20.4% |
| Logit RMS | 1.6122940961e-6 | 1.2845176069e-6 | 20.3% |

Of 192 AMP outputs, **modern is closer in 91, original in 58, with 43 equal
errors**. For logits the corresponding counts are 94/59/39. This does not support
uniform pointwise superiority. The cohort was selected to explain known rank
changes; do not infer an unbiased population average or a statistical guarantee.

All ten critical pair directions in the **whole-head** FP64 reference agree with
the preceding conditional final-activation references. Modern corrects the native
reversal and splits two native ties in that direction; the seven modern ties
still collapse strict FP64 relations. All ten reference margins exceed the
observed two-layout discrepancy, which is zero here. This does not establish a
formal exact-arithmetic error bound or authorize changed ranking/tie policies.

The approved model/report worker completed in **3.748 s**, with **81.3 MiB sampled
RSS**. The separately observed controller peak was **27.3 MiB**; outer elapsed
time was **4.017 s**. `RUSAGE_CHILDREN` high-water was **97.5 MiB**, including
descendants, not exclusive controller memory. Saved outputs occupy **32,193,809
bytes**. Exit zero, no resource stop/retry/GPU/network; the 180 s/512 MiB worker
limits and 4 GB task intent were respected. No performance benchmark is claimed.

**Interpretation:** there is now evidence of **better aggregate numerical
fidelity of the complete modern AMP head on these retained inputs**, extending
the earlier operation-only finding. Preserve the modern candidate and original
failed diagnostics. This does not prove general whole-generator equivalence,
biological superiority, uniform ordering improvement, accepted dev3 deviations or
H0–H4 receiving. No new scientific decision, runtime precision/source/weight
change or altered acceptance band follows. All 24 reference forwards are spent.

The [provider execution report](https://github.com/uibcdf/hydramp/issues/1#issuecomment-6612963649)
and [consumer outcome](https://github.com/uibcdf/peptidemt/issues/8#issuecomment-6612969078)
were fetched back and verified exactly. The [execution publication receipt](evidence/hydramp_amp_reference_execution_issue_updates.json)
records their body digests and the updated owning-issue checkpoint. Investigator
disposition of the existing limited dev3 proposal remains pending.

## Subsequent investigation of the 58 native advantages

The [saved-error attribution](hydramp_amp_error_attribution.md) reuses the original
arrays without any new model/activation execution. Among the 58 native AMP wins,
native logits are closer in 39, modern logits in 12, and 7 logits are identical.
Switching only the final sigmoid at fixed native logits worsens full-head error
in 33, improves 11 and leaves 14 unchanged; 25 counterfactual outputs equal the actual
modern output. These are overlapping observations, not a disjoint causal partition.
Native final/logit errors have opposite signs in 20 cases, consistent with error
compensation; precise per-engine activation-error amounts remain unmeasured.

Across all 192 outputs, native matches the saved FP64 value cast to float32 in 48
cases, modern in 47. This additional criterion does not favor modern, despite its
lower maximum/mean/RMS error and 91 versus 58 closer outputs. Do not turn aggregate
improvement into a claim that every metric or every input improves. The own-logit
activation-reference counts in the earlier trace concern a different target
and do not contradict this whole-head rounded-target comparison.
