# HydrAMP analogue generation: proposed first contract

Status: **A1 artificial contract approved under D43; implementation resumed
after the audit**, 2026-11-04. Owner:
[HydrAMP #4](https://github.com/uibcdf/hydramp/issues/4).
Existing filter review: [#7](https://github.com/uibcdf/hydramp/issues/7).
Consumer: [PeptideMT #32](https://github.com/uibcdf/peptidemt/issues/32).
This follows the [completed finite encoder E2 comparison](hydramp_encoder_E2.md);
its exhausted allowance grants no analogue/model execution.

Current authority: [A1 authorization](evidence/hydramp_analogue_A1_authorization.json)
binds the accepted contract to SHA-256
`11c1a85ec9233ba5a09ee18be377d41a577831793b9d7b7a2eef817a3415d360`.
The investigator now directs implementing the reviewed continuation plan, lifting
the audit pause for that unchanged artificial scope. Earlier proposal wording
below records A0 history. The subsequent [A2 record](hydramp_analogue_A2.md)
has its own exact real-execution authorization; do not reinterpret A1 artificial
success as trained or biological qualification.

The [installed artificial A1 outcome](hydramp_analogue_A1.md) now records separate
dev5 with 156 passing checks. The original contract and dev3/dev4 are preserved.

## Recommendation for review

Start with **improvement by both original native scores**, explicit seed,
dimensionless latent-noise temperature and attempt count, deterministic softmax
decoding, and no optional sequence filters or descriptors. Retain every input
and attempted output occurrence, including rejects and empty/no-hit outcomes.
Use the qualified encoder/core as independently reusable tools in **HydrAMP**;
PeptideMT orchestrates and keeps its current Macrel-based selectors unchanged.
This source review commissions no implementation or new scientific decision.

The detailed owner proposal is `devguide/pytorch_analogue_work_order.md` in
`../hydramp/local_data/pytorch-encoder`. The
[source/preparation receipt](evidence/hydramp_analogue_preparation.json) pins
its exact bytes, original source inventory, current unchanged artifacts and
reported findings. No new issue is needed: use #4/#7/#32.

## What the original actually does

Frozen source:
[HydrAMP 6590d2f analogue_generation](https://github.com/szczurek-lab/hydramp/blob/6590d2f4c2963f25d30669052a4c4a857e0e7279/amp/inference/inference.py#L271).
For B prototypes and A attempts, scale is `exp(raw_log_variance/2)` and each
attempt draws a new Gaussian perturbation multiplied by temperature. Means
come from the repeated prototype-token batch. The decoder receives those
latent coordinates with conditions `[1,1]`, **without PCA**. Native heads
score generated tokens before the zero-removing display projection.

Attempt rows are ordered `a*B+i`, then grouped by prototype occurrence.
Improvement requires **strictly higher AMP and strictly higher native MIC-class
score** than the prototype. The latter denotes compatibility with the low-MIC
class, not a measured MIC or demonstrated calibration. It is not hemolysis,
biological superiority or either PeptideMT selector. Equality on either score
does not improve. Original bucket behavior excludes the prototype string,
deduplicates accepted strings in lexical order with the first accepted attempt's
scores, and preserves a no-hit bucket. Those mappings must remain auditable.

Three compatibility problems need to stay explicit:

1. The original final dictionary is keyed by prototype string and overwrites
   earlier repeated inputs. Recommend an **ordered occurrence-preserving primary
   result**, retaining this deliberate interface difference from the original.
2. #7 already records a combined optional filter mask that is not passed to
   the bucket helper, plus dispatch problems. Recommend rejecting enabled
   optional filters in this first module; no silent copy or correction.
3. Original README says lower P(MIC) in its improvement description, while
   the implemented comparison is greater-than and the same README labels the
   output as probability of low MIC. Its two-prototype example also omits a
   comma, causing Python literal concatenation, which interacts with native
   silent length truncation. The default-softmax attempt advice overlooks
   different sampled latent inputs. These are source-level product findings
   under #4, not newly executed model/biological failures.

## Proposed A1 boundary

- **Inputs:** nonempty CPU int64 `[B,25]` rows representing nonempty canonical
  post-padded prototypes, indices 1..20 then zeros; preserve order/duplicates.
  Reject invalid/all-zero/internal-zero rows, truncation, dtype/device errors
  and invalid numerical arguments. General molecular/file handling remains
  MolSysMT-owned; no new FASTA parser or molecular realization is proposed.
- **Sampling:** local seeded MT19937, the original scaled normal draw/order and
  float64 noise/conditioned data until the FP32 decoder boundary; no caller RNG
  reset, automatic refill or PCA. Repeated input prototypes keep distinct noise
  slices and occurrence identity; no up-front deduplication. T=0 means zero perturbation, not guaranteed
  identical reconstructed sequence. Numeric overflow/nonfinite values fail
  explicitly rather than being clipped; numeric underflow is distinguished.
- **Reuse:** initially retain native encoder batch structure B and B*A. Two
  encoder evaluations, two prototype heads, one decoder and two generated
  heads give **seven neural evaluations per future analogue call**. A paired
  head Python method still evaluates two networks. This is accounting for a
  future plan, not a granted model allowance.
- **Results:** preserve all attempts/tokens/noise/scores and prototype/attempt
  indices, exact native-score decisions, self/duplicate exclusions and returned
  indices. Output one ordered record per input occurrence, with explicit no-hit;
  no silently collapsing dictionary or new universal storage schema.

Generated internal/all-zero tokens remain raw model outputs with explicit
display/empty diagnostics; do not repair or interpret them as qualified
molecular systems. Native-score predictions and trace data never supply missing
chemistry or biological evidence.

A1 requires predeclared **artificial** oracle, RNG, strict-threshold, attempt/order,
raw-token/projection, duplicate/self/no-hit and argument-failure cases, plus
applicable installed core regressions. Proposal: retain `atol=2e-6, rtol=2e-5`
for bounded synthetic formulas and exact policy/mapping assertions; this is not
a pretrained analogue acceptance criterion. Preserve separate dev3/dev4 and use
a new local candidate if commissioned. No code/model test is executed in A0.

## Later gates and current approval boundary

After A1, A2 needs a frozen exact candidate/assets/prototype/seed/temperature/
attempt matrix, prospective numerical/token/selection criteria, actual original
graph/loader/RNG/descriptor accounting and fresh finite host/call approval.
The reference's `get_sigma` fetches its three-output graph, including an unused
sampled latent; encoder E2's two-output reference does not automatically qualify
that behavior. Its constructor effects also need their own accounting. Compare
supplied-noise math separately from same-seed draws, retaining all failures and
modern numerical advantages. No tolerance-based alteration of greater-than
selection is proposed. Existing decoder/near-tie FAILs retain their original scope.

Discovery mode, descriptors, optional filters, sequence-facing and PeptideMT
transport follow as independently reviewed extensions; the full-modernization
goal remains. Training, other families, feedback/target conditioning, GPU,
release, commit/push and original-author contact remain outside this proposal.
No new accepted D-number, E2 adoption or resource allowance is inferred.

**Requested next decision:** approve/narrow/defer this first scientific contract
and A1 artificial-only implementation. Exact API names/internal organization
remain delegated technical choices; real execution is a later request.
