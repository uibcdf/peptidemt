# GRU arithmetic-layout candidate: preparation and validation proposal

Status: **single-forward validation executed; candidate failed**, 2026-10-30.
Owner: `uibcdf/hydramp`; consumer: PeptideMT #8 / D39. The
[diagnostic](hydramp_decoder_trace.md) identifies the GRU path as the earliest
observed divergence and reproduces both original endpoints exactly. It does
not prove the individual operation responsible. The original failed comparison
remains failed; this candidate is not an accepted correction or scientific model.

## Executed outcome and disposition

The investigator explicitly instructed continuation in response to the exact
single-forward request, plan
`9ebb32814d91e05a94a7a879eb918a0b86230e676d5634a39e53eb7f0f700396`.
The worker completed once in **2.23 seconds**, maximum conservative sampled
worker-plus-supervisor RSS **285.89 MiB**, with no limit stop or retry. The
[authorization](evidence/hydramp_gru_candidate_authorization.json) and
[execution receipt](evidence/hydramp_gru_candidate_execution.json) retain the
exact artifact, inputs, output arrays and failure.
The aggregate failure and next proposed diagnostic are
[recorded in existing PeptideMT #8](https://github.com/uibcdf/peptidemt/issues/8#issuecomment-6536244085).

The candidate still has **17/6300 decoder probabilities outside tolerance**,
maximum absolute error `5.188584327697754e-5`, versus dev0's 18/6300 and
`4.845857620239258e-5`. RMS probability error increases from approximately
`1.3890e-6` to `1.5485e-6`; the slightly smaller failure count is not a correction.
All tokens and strings remain exact on the twelve inputs.

The operation grouping changes values from timestep 0 but does **not** remove
the original discrepancy. Thus it is not a sufficient explanation/correction.
Do not adopt this candidate or make more deployment-code changes on that guess.
Keep the failed branch, wheel and primary data as negative evidence, with the
original source and dev0 experiment intact. No new TensorFlow/PCA/head/Macrel
evaluation or GPU computation occurred.

The subsequent [independent numerical reference](hydramp_numeric_reference.md)
has now completed its separately approved two-forward diagnostic (2026-11-02).
Native and port FP32 errors relative to it are similar; all tokens match. This
supports an explicit review of numerical admissibility before another correction,
without changing deployment precision or the original failed criterion.

The original preparation/proposal below is retained as the completed experiment's
historical scope.

## Admissibility discussion — provisional assessment, not acceptance

The investigator asks whether this numerical discrepancy is admissible. The
[saved-output assessment](evidence/hydramp_error_admissibility.json) adds no model
evaluation. In the twelve-row fixture, minimum native top-two token probability
margin is `0.024026036262512207`; twice the global maximum observed error is
approximately `0.000103772`. Thus that minimum margin is over 230 times larger
than the perturbation bound needed to reverse a top-two comparison, and all
300 argmax tokens already match. Maximum absolute probability error corresponds
to approximately 0.0052 percentage points.

Assistant assessment: this is likely admissible numerical drift for the current
deterministic decoded output on this finite fixture. It does not yet establish
general equivalence, near-tie behavior, complete result ordering or scientific
acceptance. The initial `atol=2e-6, rtol=2e-5` band was proposed as a diagnostic;
its scientific impact boundary was not independently established. Its failure
alone does not demonstrate an implementation error. Preserve that formal failed
result rather than silently changing the band.

[PyTorch's numerical-accuracy guidance](https://docs.pytorch.org/docs/main/notes/numerical_accuracy.html)
explains why mathematically equivalent floating-point computations need not be
bitwise identical across operation ordering, backends or platforms. That general
fact does not prove the origin of this particular discrepancy. Prefer the
completed independent numerical reference and wider output/boundary fixtures
over further guessed deployment-code changes. The later explicit two-forward
authorization and outcome are recorded in that reference report. This provisional
assessment itself grants no scientific acceptance, revised criterion or new calls.

## Concrete isolated change

Local branch/worktree: `peptidemt-pytorch-gru-layout` at
`../hydramp/local_data/pytorch-gru-layout`, based on original upstream
`6590d2f4c2963f25d30669052a4c4a857e0e7279`. Preserve the original
`peptidemt-pytorch` source/worker/wheel and both experiment directories.

Keras 2.3.1 GRU `implementation=2` computes the update/reset recurrent projections
in one matrix product. The dev0 port computed them separately. The candidate
groups those two projections together, retaining the z/r/h order, reset-before
candidate equation, biases, weights, float32 precision and all other scientific
source. This follows the inspected reference operation layout; it does not yet
demonstrate resolution of the observed error.

The new internal artifact is `hydramp-torch==0.0.0.dev1`, SHA-256
`1ea26260899236549d77cb36a206c55e91e2cf6e9080d1fa9a1a5369c1718fc8`.
It was built offline and installed as an exact wheel in a new isolated Python
3.14.7 worker. The same seventeen external versions are retained, including CPU
PyTorch 2.15.0+cpu and NumPy 2.4.6. Native checking reports eighteen compatible
distributions; all seven wheel payload members except installer-updated RECORD
match installed bytes. The installer retains no archive digest, so the wheel
SHA is operator-recorded, not attributed to `direct_url.json`.

Twenty-nine relevant artificial-weight tests pass against that installed wheel:
twenty-five core equations/full-pipeline/input tests, two trace transparency/
restoration checks and two finite candidate-worker control checks. The legacy
worker and dev0 package are unchanged. No real candidate checkpoint had loaded
at that preparation milestone.
This is a local uncommitted artifact, without publication or a general support
claim. The [preparation receipt](evidence/hydramp_gru_candidate_preparation.json)
pins source, wheel, environments, exact validation plan and evidence.

## Requested single-forward validation

Load only the candidate in its new CPU worker and make **one decoder forward
on the same twelve conditioned rows**, capturing the four existing intermediates
within that single pass. Compare with the retained native trace whose final
output was bitwise identical to the original canonical reference. Also require
the original tokens/strings exactly and the unchanged final probability
criterion `atol=2e-6, rtol=2e-5`. Intermediate metrics remain diagnostic only.

No new TensorFlow run, PCA load/inverse transform, AMP/MIC forward, native
generation-API call, descriptor, Macrel, new seed, precision experiment or retry.
The same sixty-five checkpoint/provenance files and original MIT/local-research
use conditions apply. Only candidate decoder execution is proposed; even a
passing result does not complete native descriptors/ordering/RNG/provenance,
consumer integration, H0–H4 or scientific acceptance.

Retain **4 GB task RAM**, 2 GiB sampled worker RSS stop, CPU affinity 0,1, one
native thread, nice 10, **180 seconds total** for the one worker, 8 GiB virtual
ceiling, 8 GiB available host-RAM floor, 1 GiB free-disk preflight and 128 MiB
scientific outputs. No GPU computation or network. Scientific outputs have their
own validation directory, separate from the installed environment/build cache.
Measure the small supervisor separately. RSS monitoring is sampled, not an
instantaneous kernel group cap.

The control helper permits only the pinned `torch` stage and verifies retained
reference hashes; it does not fabricate a new successful legacy attempt. One
attempt is allowed; a failed criterion/resource stop is reported without a
second evaluation or tolerance adjustment. The prior two-forward diagnostic
allowance is exhausted, so obtain explicit authorization of this exact new
artifact/plan before loading it on the real checkpoint.
