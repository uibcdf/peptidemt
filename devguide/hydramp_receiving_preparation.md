# HydrAMP receiving: private data bridge and H3/H4 preparation

Status: **private source preparation and saved-data replay pass; live H3/H4 pending**,
2026-11-03. Owner: [PeptideMT #8](https://github.com/uibcdf/peptidemt/issues/8);
provider investigation: [HydrAMP #1](https://github.com/uibcdf/hydramp/issues/1).

The investigator reiterates that explained, independently justified modern
results should be preserved. Legacy numerical identity is not the development
objective. The [bounded activation attribution](hydramp_amp_activation_attribution.md)
now distinguishes upstream error, activation approximation, compensation and
rounded ties. The unchanged dev3 model remains the preparation candidate; the
saved-only higher-precision sigmoid proposal is not implemented or adopted.

## Implemented data-only boundary

The private [HydrAMPReceipt](../src/peptidemt/_hydramp_receiving.py) receives the
selected native return and its original-draw mapping, seed, request count,
completion/failure state and caller-supplied provenance. It loads no engine,
weights or PCA and is not exported as a new public generation API.

- Preserve native **returned order**, every duplicate/empty/incompatible row and
  unknown native fields; do not sort, refill, repair or coerce a malformed value
  into a different peptide.
- Preserve `amp`, `mic` and descriptors as native evidence. Their names never
  become Macrel AMP/hemolysis measurements. `mic` does not become a concentration.
- Preserve original tokens, including zero positions, and available latent/PCA/
  conditioning/decoder-input evidence. FP32 submitted decoder input and FP64
  pre-cast conditioning remain distinct; unavailable arrays are not reconstructed.
- Attach per-occurrence trace only after unambiguous source correspondence;
  retain raw ambiguous/malformed output and explicit receiving issues separately.
- Delegate unchanged proposals to existing `SequenceRecord`, `prepare_sequences`,
  `ResultSet` and D35 selectors. Infer no termini, stereochemistry or other
  molecular realization from a sequence or amidated descriptor convention.
- Reuse existing detached data/float-hex JSON encoding. Replay requires neither
  HydrAMP nor Macrel, and never creates new execution attribution or qualification.

`from_trace` consumes an already produced owner `GenerationTrace` through its
retained fields and numeric-array export; it does not call the model or implement
its codec. This prepares the consumer's data path, not optional-engine execution,
resource supervision or the final installed-worker/API boundary.

## Executed verification

The [preparation receipt](evidence/hydramp_receiving_preparation.json) pins exact
consumer source/tests and all replay inputs. **Sixteen final guarded artificial
source tests pass**, including mapping corruption, duplicates, malformed/partial/
completed-empty outputs, nonfinite native values, exact float replay, unresolved
chemistry, trace precision and controlled composition with both selectors.
The invented Macrel scores deliberately disagree with native AMP preference;
the unchanged selectors use only Macrel's named values. This is not a native
Macrel or scientific H4 test. Preliminary 14/15-test checkpoints are retained
as development history, not additional distinct checks.

The real saved-data replay receives **17 original dev3 batches / 272 returned
occurrences**, covering 256 distinct latent inputs plus the declared repeat.
Every native field, occurrence, order and token vector survives exact JSON replay,
including **1,693 zero-token positions**. All rows remain present; **20** inputs
retain the existing leading-M incompatibility. Generator evidence stays imported
with `qualification_reference=None`; no scientific status is upgraded.

Source tests run in the existing isolated Python 3.14 worker with seven installed
distributions and published Pytest Receptor 1.2.2: 0.52 s, about 44.2 MiB child
kernel RSS high-water. Saved replay runs in 0.62 s / 38.2 MiB. Model/framework,
network and unreviewed scientific artifact access are blocked; the replay permits
only the two frozen confidence-campaign output files. Activation/matrix arithmetic
is blocked. There are **zero new model, PCA, descriptor or Macrel evaluations**.
No shared environment is changed. This is source qualification, not installed
PeptideMT wheel/CI qualification.

## Remaining executable receiving work

Prepare and freeze the exact live consumer worker and fresh resource/call plan
before executing it. Reuse existing native smoke/reference evidence; every new
call needs a stated receiving question rather than another legacy-identity test.
The remaining work is:

1. Choose and inspect the actual installed/source consumer route and isolated
   generator/runtime boundary, preserving the accepted model/asset/profile bytes.
2. Exercise direct modern results versus the consumer receipt for the same
   source operation, with explicit seed/completion and honest error handling.
3. Assess the unchanged generated pool with qualified Macrel, keeping every
   incompatible/failed proposal visible; freeze the small procedural control and
   its scientific purpose before execution.
4. Apply both existing selectors, compare the same pool before/after selection,
   and verify saved replay, portable provenance and applicable attribution.
5. Return H0–H4 evidence and unresolved limits for investigator disposition.

Same-provider transport equality protects subject/score attribution; it is
separate from cross-framework FP32 equality. The old numerical/global-rank FAILs
remain truthful historical diagnostics, not a reason to copy legacy artifacts.
Neither this preparation nor the investigator's conditional direction is broad
dev3 acceptance, a new execution allowance or a completed H0–H4 receipt. No new
chemical policy, molecular parser, scientific selector, training, release,
commit or push follows. Retain task resources for review by 2026-11-13.

## Exact executable experiment prepared — 2026-11-03

The [H3/H4 plan](hydramp_h4_qualification.md) now fixes the actual two-worker
route, source/asset/inventory pins, seeds 1001/1002, control, three proposed
Macrel calls and new host/call limits. The frozen W3 installed core accepts the
private source module in a guarded model-free compatibility probe. The final
combined receiver/controller check passes 34 artificial tests, including these
16 receiver cases; it does not add 34 new receiver tests or live execution.
The [preparation receipt](evidence/hydramp_h4_preparation.json) retains evidence.
Fresh investigator approval remains pending. The
[consumer update](https://github.com/uibcdf/peptidemt/issues/8#issuecomment-6614632869)
was fetched back and verified; [publication evidence](evidence/hydramp_activation_receiving_issue_updates.json)
retains its exact body alongside the owning numerical report.

## Live private receiving and composition completed — 2026-11-03

After the investigator approved the exact prepared plan, the
[actual H3/H4 experiment](hydramp_h4_qualification.md#approved-execution-and-independent-review--2026-11-03)
completed with no retry. Two 16-row native generation batches reproduce their
cached dev3 returns exactly. All 32 proposals and 212 zero-token positions
survive the same-operation receipt and detached replay; Macrel receives the
identical attributed inputs. Two leading-M strings remain explicit incompatible
proposals, leaving 30 generated assessments plus the four exact W3 controls.
Both unchanged selectors and complete saved rankings reproduce exactly.

The [execution evidence](evidence/hydramp_h4_execution.json) also preserves the
scientific limitation: all nine generated Macrel AMP-positive rows are also
Hemo-positive; neither batch contains a native AMP-positive/NonHemo row.
This is a finite computational tradeoff, not proof of biological quality or a
reason to alter selectors. No original numerical criterion is relaxed. Scientific
disposition and a future public installed optional-backend/API remain pending;
all six neural-forward and three Macrel-call allowances are exhausted.

Saved-only review also verifies that these same 32 generated sequences and their
returned order match the original HydrAMP campaign for the fixed seeds. The
observed lack of a joint Macrel AMP-positive/NonHemo hit in this fixture is
therefore not evidence of a port-specific sequence regression. No additional
legacy or Macrel execution was required; the exact source digest and comparison
are retained in the [execution receipt](evidence/hydramp_h4_execution.json).

## Public data boundary and installed reader — 2026-11-03

The [public receiving milestone](hydramp_public_receiving.md) now exports
`peptidemt.HydrAMPReceipt` and preserves the same v1 meanings. It shares the
existing ResultSet duplicate-key rejection through the private data layer.
Forty-one installed data/controller/W1 compatibility checks, exact saved H4
replay and warning-free documentation builds pass for a local unpublished wheel.
This adds no generation execution API or scientific calls. The earlier private
source preparation and live experiment above retain their original identities;
their exact pre-promotion source is preserved in the new milestone's receipt.
