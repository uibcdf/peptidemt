# HydrAMP PyTorch port: preparation and fidelity boundary

Status: **local implementation; twelve-input deviation accepted, full qualification pending**,
2026-11-02. The original real-checkpoint diagnostic remains failed.
Investigator authority: D39; consumer tracking: uibcdf/peptidemt#8.
The [handoff receipt](evidence/hydramp_pytorch_port.json) records exact local
source/artifact/environment and executed checks. This work does not complete
H0–H4, replace the commissioned native result contract or qualify training.

The investigator authorized moving to PyTorch after considering the legacy
TensorFlow/Keras stack. Native PyTorch inference is the selected implementation
direction. A later new algorithm or extension to other families remains a
separate scientific question, without training or generalization authority.

The [real-checkpoint comparison](hydramp_pytorch_comparison.md) has now executed
under the investigator-approved 4 GB task budget: six evaluations, one PCA load,
no retry. Exact tokens/strings, PCA and native heads pass on the twelve-row
fixture; eighteen decoder probability values exceed the unchanged tolerance.
Observed worker plus supervisor memory peaked around 0.5 GiB. The port is not
accepted as a qualified replacement; validation of a changed candidate needs
a new explicit finite budget.
The [intermediate diagnostic](hydramp_decoder_trace.md) has executed its two
approved forwards: endpoints reproduce the prior arrays bitwise, and the earliest
observed difference is already in the GRU. The separate [layout candidate](hydramp_gru_candidate.md)
has since failed its approved single-forward validation despite passing synthetic
tests. A [NumPy/float64 numerical reference](hydramp_numeric_reference.md) has
since completed its two separately approved forwards on 2026-11-02. Native and
port FP32 errors relative to that reference are similar; all 300 tokens match.
This supports finite-fixture numerical drift, without proving its exact cause,
changing deployment dtype/thresholds or granting scientific acceptance.

## Ownership and preserved reference

The implementation belongs to `uibcdf/hydramp`, branch `peptidemt-pytorch`, in
the separate local worktree `../hydramp/local_data/pytorch-port`. Its
`ports/pytorch/` directory contains the experimental package, lock and tests;
the provider's `devguide/pytorch_inference.md` records the detailed handoff.
The branch remains based on upstream
`6590d2f4c2963f25d30669052a4c4a857e0e7279`; no committed or published port is claimed.
The original dirty `peptidemt-inference` worktree, all legacy workers, upstream
`amp/` files and MIT licence are preserved. PeptideMT gains no runtime dependency
or scientific behavior change in this milestone. Molecular systems and file
handling remain with MolSysMT.

The fork's issues are disabled, as observed through GitHub. Do not bypass that
setting by posting upstream. #8 remains the existing consumer work record; no
new issue or settings change is made.

## Implemented computational path

The fixed 25-position decoder accepts 64 PCA-inverted latent values and the two
explicit native conditions. The port retains autoregressive feedback, both
condition reminders and deterministic softmax. Its GRU explicitly implements
the inspected Keras **reset-before** equation and z/r/h gate order. This matters:
[PyTorch's GRU documentation](https://docs.pytorch.org/docs/2.10/generated/torch.nn.GRU.html)
describes a different candidate-state equation. Directly substituting that
class would change the computation. The documentation version is a source for
that equation, not a claim that PyTorch 2.10 was tested here.

Both native heads retain i/f/c/o LSTM order, stored biases, unmasked zero-token
embeddings and valid max pooling. The MIC head preserves channels-last Conv1D
semantics, ReLU and asymmetric SAME padding for its even kernel. Scores remain
native AMP/MIC outputs, distinct from Macrel and from experimental activity.
Batch order, internal zero positions and duplicate occurrences are preserved.
The codec removes every zero only when projecting model tokens to strings;
those strings are not re-encoded for scoring.

The loader checks required SHA-256 digests, consumed JSON configuration, array
shapes, float32 dtype and finite values, with NumPy pickle loading disabled.
It does not load the encoder or deserialize the PCA. Numeric PCA inversion
uses the inspected scikit-learn 0.23.2 affine/whitening formula; float64 latent
values remain float64 until the eventual decoder cast. Exporting the real
coefficients remains a gated legacy-worker operation.

## Installation and mathematical checks

The candidate is Linux x86_64 / Python 3.14.7 / PyTorch 2.15.0+cpu / NumPy 2.4.6,
installed in a task-owned isolated environment. The exact CPU wheel comes from
the [official PyTorch CPU index](https://download.pytorch.org/whl/cpu/torch/).
The lock identifies this experimental candidate; exact pins do not establish
minimum reusable API floors or a public support range. The legacy environment
and shared MolSysSuite environment are separate and unchanged.

Twenty-five artificial-weight tests compare GRU/LSTM primitives, the complete
decoder and both heads against independent float64 NumPy references. They
exercise condition feedback, convolution boundaries, original zero tokens,
batch correspondence, PCA dtype/whitening and rejected altered/unsupported
artifacts. The suite explicitly discriminates reset-before from reset-after.
Reference tolerances are numerical checks, not empirical biological validation.
The receipt distinguishes preliminary source tests from final installed-wheel
checks and native dependency closure.

The earlier preparation used affinity to two logical CPUs, one native-library thread,
nice 10, an 8 GiB address-space ceiling and bounded wall times. Tests block
network access, legacy-provider imports and real checkpoint/PCA opens; only
artificial files under pytest temporary storage were read as weights. That
milestone loaded no real model/PCA. Later authorized checkpoint execution is
reported separately above, retaining its failed numerical criterion.

## Subsequent generation preparation

The [dev2 generation candidate](hydramp_generation_preparation.md) now composes
the byte-identical dev0 numerical core/PCA with seeded sampling, original-token
scoring, native result views and occurrence trace. Seventy-four installed-wheel
artificial checks pass. An explicit original-modlAMP adapter delegates descriptor
calculations, but its Python 3.14 installation/scientific outputs remain unqualified;
missing properties support fails before a model call. General reusable descriptor
needs are handed to MolSysMT #485. No real model/PCA or descriptor call follows.

The later [dev3 comparison preparation](hydramp_full_comparison.md) resolves a
clean modern descriptor deployment and measures exact five-field parity on eight
published occurrences, preserving original pH/amide semantics explicitly. Its
full native/modern neural comparison has now executed its approved 22 evaluations.
Tokens, strings, actual order, five descriptors and repeats agree on the tested
inputs; the strict probability diagnostic remains failed. No broad acceptance
or automatic call renewal follows.

## What remains before adoption

The first real-weight comparison inspected probabilities, argmax tokens, both
heads and PCA inversion on identical explicit latents. The probability criterion
failed despite exact tokens. The later approved trace adds intermediate states
and localizes the earliest observed difference to the GRU, with exact endpoint
reproduction. It still does not prove the individual responsible operation.
The isolated joint-projection candidate did not resolve the failure and is not
adopted. Before another source modification or a criterion discussion, the next
diagnostic used an independent approximate float64 reference under a separately
approved two-forward budget, now exhausted. Both formulations agree to about
4e-14 in probabilities. The measured native and port FP32 errors are comparable;
review numerical admissibility explicitly rather than assuming the legacy binary
is exact. The original failed reports and thresholds remain unchanged.

The original dev0 core has no generator wrapper. The later dev2 prepares the
native `properties=True` composition, while original modlAMP descriptor deployment,
actual pandas-order/tie parity, complete native RNG/seed behavior, portable
result/provenance and the PeptideMT adapter still need qualification. No native descriptor is replaced with a convenient formula
or newer unqualified provider. Original Drive-versus-starter byte parity and
bundle/use review remain open. The existing four-call/52-output H2 design does
not automatically authorize additional framework comparisons.

The [limited acceptance record](hydramp_behavioral_acceptance.md) adds saved-score
ordering and raw-draw reproducibility evidence. Under D40 the investigator accepts
the observed deviation only on these twelve inputs for continued dev0 qualification.
Original failed diagnostics remain unchanged; wider scientific acceptance is pending.
Prepare the exact broader fixture/candidate/use and finite call plan before further
model execution. Keep native D38
acceptance criteria and M1–M8 unchanged. No encoder,
analogue generation, training, target conditioning, feedback, GPU, package
publication or extrapolation to another family follows from this milestone.

## Current numerical and consumer preparation — 2026-11-03

The [finite activation attribution](hydramp_amp_activation_attribution.md)
explains the mixed pointwise winners, compensation and rounded ties without
changing dev3. The investigator directs preservation of justified modern
improvements rather than forced legacy numerical identity. No global scientific
superiority or new D40 scope follows. Issues are now enabled in the owned fork;
[HydrAMP #1](https://github.com/uibcdf/hydramp/issues/1) receives the diagnostics.
The earlier disabled-issue statement above describes the original milestone.

The [private data receiver](hydramp_receiving_preparation.md) and
[exact H3/H4 experiment](hydramp_h4_qualification.md) are prepared. Thirty-four
final guarded artificial receiver/controller tests and actual frozen-W3-core
model-free compatibility pass. No new live call is authorized or executed.
The old environments and dev3 wheel are retained byte-for-byte; the assessment
uses an explicit private source extension, not a newly installed public API.

## Approved functional composition result — 2026-11-03

The investigator subsequently approves the exact prepared CPU plan. The
[executed consumer experiment](hydramp_h4_qualification.md#approved-execution-and-independent-review--2026-11-03)
passes same-operation receiving of 32 dev3 proposals, exact cached native returns,
retained trace/provenance, 30 compatible Macrel assessments plus four unchanged
W3 controls, both selectors and exact saved replay. Two incompatible leading-M
inputs remain visible. Total stage time is 55.76 s, maximum sampled process-tree
RSS 553.5 MiB; no retry, model change or resource stop occurs.

All nine generated Macrel AMP-positive outputs are also Hemo-positive. This
small unfiltered experiment demonstrates functional composition and the
AMP/hemolysis tradeoff; it does not establish joint usefulness or biological
superiority. Broader dev3/H0–H4 acceptance remains for investigator disposition.
A public installed optional-backend/API and its full attribution boundary remain
future work. All new calls are exhausted; exact evidence and environments are
preserved in the [execution receipt](evidence/hydramp_h4_execution.json).

Saved-only review also verifies that these same 32 generated sequences and their
returned order match the original HydrAMP campaign for the fixed seeds. The
observed lack of a joint Macrel AMP-positive/NonHemo hit in this fixture is
therefore not evidence of a port-specific sequence regression. No additional
legacy or Macrel execution was required; the exact source digest and comparison
are retained in the [execution receipt](evidence/hydramp_h4_execution.json).
