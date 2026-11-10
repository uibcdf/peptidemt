# Independent numerical reference and numerical admissibility review

Status: **two numerical forwards completed; later D40 disposition limited to twelve inputs**,
2026-11-02. Owner: `uibcdf/hydramp`; consumer work record: PeptideMT #8 / D39.
The fork issue board remains disabled (rechecked 2026-11-02); this existing issue
retains the review and consumer evidence until a provider issue can receive it.
The [published review and numerical results](https://github.com/uibcdf/peptidemt/issues/8#issuecomment-6593862430)
are verified in the [publication receipt](evidence/hydramp_numeric_reference_issue_update.json).
No upstream issue, repository settings change or duplicate issue is needed.

## Executed outcome

The investigator explicitly instructed proceeding with the prepared two-forward
NumPy FP64 diagnostic. The [authorization](evidence/hydramp_numeric_reference_authorization.json)
binds that instruction to unchanged plan SHA-256
`bd5ad87eb20b1542ed21d8b07c0e91ec628126d23afa6ff708dc18d5166b1c19`.
The [execution receipt](evidence/hydramp_numeric_reference_execution.json)
pins exact source, assets, outputs, log, inventory and resource observations.
No source or package changed between preparation and execution.

Both mathematical formulations passed the internal `atol=rtol=1e-10` check:
maximum probability difference **3.9190872769268026e-14**, maximum logit
difference **1.4921397450962104e-13**. This checks grouping sensitivity within
the shared NumPy/BLAS implementation; it is not a formal error bound or a
comparison between two independently implemented elementary-function libraries.

Errors of retained float32 probabilities relative to the separate FP64 formulation:

| Retained implementation | Maximum absolute error | RMS error | Outside original diagnostic band | Tokens equal FP64 |
| --- | ---: | ---: | ---: | --- |
| Native TensorFlow | 2.6977310753961703e-5 | 9.494061026004748e-7 | 16/6300 | 300/300 |
| PyTorch dev0 | 2.8850079310305254e-5 | 9.610597610086768e-7 | 16/6300 | 300/300 |
| PyTorch dev1 layout candidate | 2.4908532523015836e-5 | 9.880168818084032e-7 | 16/6300 | 300/300 |

The native and port errors relative to this approximate reference are similar.
This supports **numerical drift on this finite fixture** as a plausible account;
it does not prove which primitive/rounding sequence caused the discrepancy.
A smaller dev1 maximum here does not establish overall superiority: its RMS is
larger, and its original native-versus-port comparison still failed. Neither the
legacy output nor this FP64 result is biological ground truth.

The worker completed once in **0.515 seconds**, sampled worker RSS **42.84 MiB**;
conservative sampled worker-plus-supervisor maximum **65.62 MiB**. One set of
eight original parameter arrays was loaded and reused for exactly two forwards
on the same twelve retained rows, first rounded to float32. Python 3.14.7 /
NumPy 2.4.6, seven pinned packages, no deep-learning framework imported. No
resource stop, retry, GPU computation, new PCA/head/Macrel/native-generation
call occurred. All fifty tracked original `amp/` and MIT licence files still
match `6590d2f4c2963f25d30669052a4c4a857e0e7279` byte for byte.

The two-forward allowance is exhausted. Preserve all previous failed reports,
workers and artifacts; dev1 is not adopted and the production precision,
thresholds and complete generator contract are unchanged. Source and reports
remain local/uncommitted; these are not published code or package evidence.
Task-owned resources remain retained for this review, with review by 2026-11-13.

## Explicit issue review for later scientific evaluation

The subsequent [behavioral acceptance proposal](hydramp_behavioral_acceptance.md)
adds saved-score ordering, margin diagnostics, synthetic near-tie checks and
raw NumPy draw comparisons without another model/PCA evaluation.

The investigator asks that admissibility receive serious, durable issue review.
Reuse **PeptideMT #8**. The subsequent D40 decision accepts the measured deviation
only on these twelve inputs for continued dev0 qualification. Broader acceptance
remains open; neither a small absolute error, exact tokens nor a diagnostic FAIL
alone establishes the general scientific verdict.
The owning fork issue board must eventually receive the handoff when available;
consumer tracking is a visible interim limitation, not completed provider triage.

Recommended review agenda, **proposed for investigator evaluation**:

1. Verify equation/parameter/input fidelity, preserving reset-before GRU semantics,
   input quantization, conditions and token mappings. Audit the independent
   reference and synthetic checks; framework similarity alone is insufficient.
2. Specify numerical acceptance according to exposed scientific outputs. Preserve
   the original failed `atol=2e-6, rtol=2e-5` result as diagnostic evidence; approve
   any revised criterion explicitly with a reason and a prospective test plan.
   No new tolerance value is proposed or silently applied by this experiment.
3. Design broader output/boundary fixtures: near ties, seeds/latent regions,
   native heads, duplicate/order/tie handling, descriptors and direct-versus-adapter
   results. The existing twelve rows have a comfortable minimum native top-two
   margin of about 0.024 and cannot establish behavior near a decision boundary.
   Distinguish fixed-input comparisons from cross-framework RNG equivalence.
4. Record accepted/rejected/deferred disposition, scope and remaining limitations
   in #8 and this work record. Full H0–H4 qualification and investigator acceptance
   remain necessary; any further learned-parameter evaluations require a new
   exact finite budget before execution. Preserve attribution/use restrictions.

The original assistant assessment was that this drift was likely admissible for
the fixed-input deterministic token output. The later investigator D40 decision
now explicitly accepts that limited deviation. **General port acceptance remains open**.
Further deployment patches intended only to reproduce legacy last bits are not
justified by these measurements. Molecular-system operations remain MolSysMT-owned.

# Historical preparation and execution proposal — 2026-10-30

Historical status at preparation: **prepared; two numerical forwards pending approval**.
The executed outcome above supersedes those pending-execution statements.
PeptideMT #8 / D39. The original and GRU-layout candidates both remain failed
under the unchanged probability criterion. The
[last controlled experiment](hydramp_gru_candidate.md) did not support grouping
alone as a sufficient correction. Do not keep changing deployment code to chase
the previous binary's last bits without an independent mathematical comparison.

## Scientific question and limits

Test whether the saved native TensorFlow, PyTorch dev0 and dev1 float32 outputs
are consistent with a separately implemented **approximate float64 mathematical
reference** for the same decoder equations. This can inform a later correction
or a reasoned review of numerical criteria. It does not itself change the
accepted criterion, deployment dtype, weights, scientific model or acceptance.
Float64 is still finite precision; this is neither exact arithmetic nor biological
ground truth. The investigator retains the acceptance decision.

Installed library headers show different possible CPU elementary-function
implementations, including Eigen's float logistic approximation and a PyTorch
vector tanh implementation using SLEEF. These static observations are context,
not measured runtime dispatch or proof of the trained-case cause. The existing
traces already establish endpoint reproducibility and the early GRU difference;
they cannot decide which backend is mathematically more accurate.

## Exact proposed computation

Use the **same saved twelve conditioned rows** and the original eight decoder
NPY parameter arrays (GRU, LSTM and dense only), with their existing hashes.
First round inputs to float32 exactly as the framework inputs do; **then** convert
those already-rounded values to float64. Convert the exact float32 weight values
to float64 without changing coefficients. This avoids comparing a different,
higher-precision PCA/input preprocessing route.

Make **two complete NumPy float64 decoder forwards in one worker**:

1. Independent gate-by-gate matrix products.
2. Grouped matrix products implementing the same real-number equations.

Load the eight parameter arrays once and reuse them for both evaluations.
Capture autoregressive states, LSTM states, logits and probabilities. Check
agreement between the two formulations with the proposed internal diagnostic
band `atol=rtol=1e-10` and exact argmax tokens; disagreement means the numerical
reference itself needs review. Both formulations share NumPy elementary
functions/BLAS; agreement checks grouping sensitivity, not formal error bounds
or two independently implemented libraries. Compare all three retained float32 traces against
that reference, reporting errors and token correspondence. The original
float32 comparison remains failed and its `atol=2e-6, rtol=2e-5` is not widened.
This is not an automatic correction/replacement or a new production engine.

No TensorFlow/PyTorch execution, new PCA load/inverse transform, classifier,
Macrel, native generation-API call, descriptor, new seed or training. Original
`6590d2f4c2963f25d30669052a4c4a857e0e7279` / starter
`7804df862872ccc6d09fe01c41bafbca194cfa31`, licences, all previous workers,
artifacts and failed outputs remain preserved.

## Isolated environment and preparation evidence

The provider owns `ports/pytorch/devtools/numeric_reference.py` in the local
`peptidemt-pytorch-gru-layout` worktree. It imports NumPy and standard-library
tools only. A new isolated Python 3.14.7 environment contains **seven pinned
NumPy/test packages**, no Torch, TensorFlow, Keras or HydrAMP package. The versions
and official wheel hashes come from the already reviewed lock; no upgrade or
dependency substitution is involved. Native dependency checking passes.

Offline name/direct-URL installation could not reuse the needed cache entries;
the initial errors are retained. Preparation fetched the same seven hash-pinned
official PyPI wheels, without changing versions. That acquisition is separate
from model execution, which prohibits network access.

Thirteen artificial-data tests pass: native input rounding, independently
calculated scalar GRU equations/reset ordering, stored LSTM forget bias,
closed-form zero-recurrence/softmax results, two-formulation agreement, extreme
sigmoid stability, invalid inputs and absence of deep-learning imports. Tests
block real array/checkpoint opens and network access. These are synthetic
preparation checks, not a result for learned parameters.

The [preparation receipt](evidence/hydramp_numeric_reference_preparation.json)
pins source, environment, wheel requirements, data, exact plan and all checks.
No real numerical-reference stage has started. The proposed plan deliberately
counts both NumPy decoder evaluations as learned-parameter forward computations,
despite invoking no deep-learning framework.

## Same host envelope, fresh finite allowance

One NumPy worker, two twelve-row numerical forwards, **180 seconds total**.
Retain **4 GB task RAM**, 2 GiB sampled worker RSS stop, CPU affinity 0,1,
one native thread and nice 10. The 8 GiB virtual ceiling is not a RAM reservation;
keep the 8 GiB available-host-RAM floor, 1 GiB free-disk check and 128 MiB
scientific-output stop. No GPU, model-time network or automatic retry.

The preceding one-forward candidate allowance is exhausted. Obtain explicit
approval of this new **diagnostic arithmetic precision and two-forward budget**
before loading the parameters. Do not infer a deployment precision change,
threshold waiver, scientific acceptance or additional evaluation authority.
