# HydrAMP analogue A1: installed artificial qualification

Status: **D43 artificial implementation delivered**, 2026-11-04. Provider:
[HydrAMP #4](https://github.com/uibcdf/hydramp/issues/4); consumer:
[PeptideMT #32](https://github.com/uibcdf/peptidemt/issues/32).
The [evidence receipt](evidence/hydramp_analogue_A1.json) pins exact source,
artifact, runtime and test records. The [scientific contract](hydramp_analogue_work_order.md)
and original proposal SHA are unchanged.

## Delivered scope

Separate local `hydramp-torch==0.0.0.dev5` adds AnalogueCandidate, AnalogueResult,
AnalogueTrace and HydrAMPAnalogueGenerator. It composes the existing owner encoder,
decoder, heads and vocabulary projection. No native numerical equation, weight,
dependency pin or accepted dev3/dev4 artifact was changed. Original `amp/` remains
the reference. Modern source remains local/uncommitted; its original Git base
is not a commit of the port.

The implementation retains attempt-major occurrences, duplicate prototypes,
original scaled Gaussian noise and FP64-to-FP32 boundary, strict native-score
improvement, self/duplicate exclusions, lexical first-accepted output and explicit
no-hit/empty diagnostics. It rejects unsupported modes/filters/descriptors,
invalid inputs and numerical overflow before silently repairing anything. A
matching-type/device probability check avoids dependence on global PyTorch
float defaults in the new composer. Its proposal-row cap is not a hard RAM cap;
execution supervision remains external.

## Exact artifact and artificial evidence

Wheel SHA-256: `f6b9e30609ddde675418a2e6696b1026656212921c2b47cf0c6d182bcfc5433e`.
Offline build/install succeeds, and the exact installed dependency metadata
passes `uv pip check` for 41 distributions. Linux CPU/Python 3.14.7,
NumPy 2.4.6, Torch 2.15.0+cpu, published Pytest Receptor 1.2.2.

**156 installed artificial tests pass**: 61 analogue cases and 95 applicable
encoder/core/generation/property-spy regressions. The final worker completes in
7.012 seconds (pytest 4.58 seconds), with peak sampled process-tree RSS
345,468,928 bytes (about 329 MiB). CPU 0/1, one numerical/inter-op thread,
nice 10, 120-second wall limit, 2 GiB sampled RSS stop and 8 GiB virtual-address
ceiling; host headroom guards and 128 MiB retained-output cap remain enabled.
No pretrained weights, PCA, descriptors, Macrel, GPU or network were used.

The first installed invocation had 155 passes and one failed repetition case.
Cause: the artificial score provider treated only its second score call as
generated data, instead of alternating prototype/generated calls across repeated
invocations. Its corrected state logic changes only the test fixture; candidate
runtime and wheel bytes stay unchanged. Failed logs/tests and the final outcome
are retained. This was not a pretrained-model discrepancy or a tolerance change.

Tests include independent mathematical scale/closed-form checks, fixed RNG
prefix/order, no caller RNG mutation, exact occurrence/decision mapping, raw
token scoring, distinct projected views, empty/no-hit outcomes, underflow and
failure contracts, repeated calls and nondefault global float dtype.

## Qualification boundary and next work

This is artificial installed implementation evidence, not analogue scientific
acceptance or A2 authority. Dependency payloads are reused from the frozen E1
profile with exact copied metadata; no new public solver/installer or platform
claim follows. Original generation/core numerical sources remain unchanged;
the separately suspected old generator default-dtype issue stays with #4.

The [consumer receiving brief](hydramp_analogue_receiving_brief.md) is prepared
before A2 planning. Next define the exact original/modern real comparison,
including native constructor/get_sigma stochastic graph behavior, observability,
criteria, artifacts and fresh host/call envelope. A new consumer redesign API,
descriptors/filters/discovery, training, feedback, other families, targets,
publication and author contact retain their separate review boundaries.

The subsequent [A2 comparison](hydramp_analogue_A2.md) has now executed under
separate exact approval: joint results agree and the probability diagnostic
fails. Its allowance is exhausted and scientific disposition remains pending.
The A1 artifact and evidence above are unchanged.
