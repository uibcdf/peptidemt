# PeptideMT redesign with the accepted HydrAMP analogue route

Status: **contract approved under D45; R1/R2 implemented and artificially
qualified; exact real R3 technical case completed**, 2026-11-04. Owner:
[PeptideMT #32](https://github.com/uibcdf/peptidemt/issues/32). Provider work:
[HydrAMP #4](https://github.com/uibcdf/hydramp/issues/4), with precision findings
retained in [#1](https://github.com/uibcdf/hydramp/issues/1). This concretizes the
[receiving brief](hydramp_analogue_receiving_brief.md) and continuation package 4a;
it does not reopen D35/M1–M8 or the general architecture.

The investigator accepts the [exact dev5 analogue resource under D44](hydramp_dev5_acceptance.md).
Provider acceptance and this consumer contract are separate decisions.
The investigator approves R1/R2 in response to the concrete contract question;
the [authorization](evidence/hydramp_redesign_authorization.json) pins the original
SHA-256 876ef80c5629dc74cf9e541bcf5f1d257ed37f28a0148f5e435a738c8a47fd71.
Its exact pre-approval bytes are retained; these current-status annotations do
not change the approved scientific obligations. The
[implementation outcome](hydramp_redesign_implementation.md) records delivery.
No real model budget follows from this contract.
Public names, internal organization and storage mechanics remain technical
choices within the reviewed obligations below.
The [preparation receipt](evidence/hydramp_redesign_preparation.json) records
exact inspected sources, provider ownership, workspace state and check scope.

## Scientific purpose and first delivered workflow

Given ordered prototype sequence proposals, produce native-score analogue
proposals, assess the returned compatible sequence views with existing Macrel,
and apply either unchanged D35 selector. Report which prototype and attempted
row produced every proposal, including incompatible and failed assessments.
This is experimental redesign by learned native scores, not demonstrated
improvement of AMP activity or reduced hemolysis.

The first implementation must provide independently usable data receiving,
proposal extraction, existing assessment and existing selection. A caller can
inspect/replay saved data without HydrAMP, Torch, Macrel or model assets. Live
generation and live assessment are explicit operations with distinct budgets;
there is no automatic expensive end-to-end call, retry, refill or extra model.

Parent assessment is a separate explicit call to the existing assessment route,
or reuse of exactly bound saved results. It is useful for paired interpretation,
but is never an implicit extra invocation or an extra selector entrant. Without
an appropriate parent baseline, claim selected analogue proposals, not an
independently measured predictive improvement over the parent. Even a favorable
Macrel contrast is predicted behavior, not biological confirmation.

## Ownership and real prerequisites

| Operation | Owner and selected boundary |
| --- | --- |
| FASTA and general molecular-system/file transport | Existing MolSysMT source-preserving FASTA operations; no local parser or chemical converter |
| Strict canonical sequence to HydrAMP-native tokens | **HydrAMP-owned missing public codec**, reported under existing #4; no consumer alphabet encoder or legacy Keras import |
| Encoder, latent perturbation, decoding, native scoring and bucket decisions | Accepted HydrAMP method; native arrays/mappings and original semantics preserved |
| Parent/candidate occurrence relationships, operation-specific compatibility, composition and interpretation | PeptideMT; bounded scientific result records, not a generic provenance service |
| Macrel evaluation and current eligible rankings | Existing PeptideMT assessment, ResultSet and select operations |
| Portable scientific attribution | Existing Ackredit capture and method/software references, extended only to operations actually completed |
| General execution journals and reusable methodology | Recorda and Praxis retain their domains; no new journal, workflow engine, knowledge graph or generic serializer in PeptideMT |

Static inspection of dev5's public exports finds `translate_tokens` and token
model operations, but no canonical sequence-to-token operation. Legacy
`amp.data_utils.sequence.to_one_hot`/`pad` exists but imports Keras and allows
native truncation; it is not a supported modern consumer codec. The owner should
offer a documented operation producing CPU int64 [B,25], preserving order and
duplicates, zero-padding after the sequence, accepting canonical uppercase
letters including initial M, and rejecting empty, unsupported or overlength
inputs before model work. No trimming, case normalization or truncation.
Its exact public name/array representation is an owner technical decision.

A codec addition requires its own identified candidate/source and artificial
tests. Do not pretend the unchanged accepted dev5 wheel already contains it or
alter that wheel in place. Reuse/pin unchanged inference modules and review
actual provider-to-consumer compatibility before a later live case.

The inspected Recorda API can reference existing scientific results through
`Reference(owner, identifier, revision, digest)` in explicit operations; its
journal does not replace native results. No new Recorda dependency is necessary
for this first data/result boundary. A later actual journal integration must use
its supported operation/reference API. Praxis methodology promotion is separate;
one successful run does not establish a reusable validated protocol.

## Prototype admission and stochastic correspondence

Receive existing ordered SequenceRecord/InputRecord objects and keep their
original sequence, raw/source/header, context and unresolved chemistry.
For this route, a compatible prototype is a nonempty, unchanged canonical
uppercase sequence of length 1–25 with no explicit chemical annotation.
Unknown chemistry stays unknown. Explicit terminal/residue/stereo/cyclic
annotations are preserved and reported incompatible, not removed or projected.
The technical token range does not establish biological applicability.

HydrAMP admission **must not use InputRecord.issues/provider_sequence** as its
decision: those properties describe the current Macrel boundary, including its
initial-M and length restrictions. Initial M is representable for HydrAMP and
must not be stripped. Macrel keeps its own independent compatibility checks.
This does not change existing InputRecord/ResultSet behavior.

Preserve an ordered outcome for every original parent. Submit only compatible
parents, in their original relative order, in **one batch**. Record the dense
provider prototype index to original parent occurrence mapping. Incompatible
parents consume no provider attempts and are not called no-hit. If none are
compatible, complete the admission record with zero model calls. A truly empty
input batch likewise returns an empty, unexecuted record.

Reject an oversized compatible batch or attempt total before dispatch; do not
chunk, sort or deduplicate it. The exact submitted batch, seed, temperature and
attempt count are part of execution identity. Random-slice assignment and FP32
scores can depend on batch context, so adding/removing/reordering a prototype
does not promise identical per-prototype results at the same seed.

For B submitted parents and A attempts, preserve row `a*B+i`, the dense provider
index i, original parent occurrence and attempt a. Keep all raw native tokens,
projected strings, noise/latent/score traces, masks and exclusion/return mappings.
Do not recompute the scores on re-encoded projections or insert a score epsilon.

## Results, candidate pool and assessment

Distinguish incompatible parent, not attempted, attempted but interrupted,
completed with no hit, and completed with returned candidates. Retain the
provider's actual progress; unknown internal completion stays unknown. Never
fabricate B*A completed attempts from an interrupted request or infer an unused
call allowance. Inspection retains malformed/ambiguous evidence but cannot turn
it into usable proposal correspondence.

Keep provider-ordered results per parent, including repeated sequence strings.
Within each parent retain native lexical/first-accepted candidate order. Flatten
the **returned candidates only**, in original parent order then native bucket
order, to the Macrel proposal pool. This defines the input occurrence order used
by the unchanged selector tie rule. It is deterministic and favors earlier
parents on exact score ties; it is not a fairness or diversity guarantee.

Do not globally deduplicate equal candidates from different parents or execution
occurrences. The provider's within-parent deduplication remains unchanged and
every discarded attempt remains in its trace. Preserve separate run-local child
occurrence, parent occurrence, provider index, attempt index and raw trace row.
They are correspondence identifiers, not molecular identities.

Every child keeps the exact native projected sequence and an explicit projection
role. Do not inherit parent chemistry, biological labels or measured properties
into the new proposal. Parent context remains attached to the ancestor; links
do not make it evidence about the child. Molecular realization is not inferred.
Internal/zero token information stays in native evidence even where display
projection omits it; native scores apply to those raw tokens, not a re-encoding.

An empty generated projection is retained as anomalous native evidence, never
repaired or passed to Macrel as a qualified molecule. A returned nonempty view
may still be incompatible with Macrel, for example initial M; preserve that child
and its assessment exclusion. Missing, duplicate, malformed or failed assessment
rows retain current ResultSet diagnoses. Both existing selectors use only the
same eligible Macrel evidence, without an added native-label gate, rounding,
deduplication, imputation or threshold. Native AMP/low-MIC and Macrel AMP/hemolysis
scores are distinct fields with distinct meanings.

## Evidence and execution boundary

Keep an analogue-specific receipt separate from the current de novo
HydrAMPReceipt schema. Its detached payload must bind original parents,
submission mapping, effective request, native trace/results, progress/failures,
provider/model/environment/source identity, actual resource use and attribution.
Retain exact scientific fields rather than adopting an unreviewed provider
portable schema. A label such as snapshot_id is not content identity or proof
of execution; bind content and source/row correspondence using the existing
bounded result/provenance conventions. Do not create a generic provenance graph.

Saved replay validates the required relationships afresh and preserves malformed
raw evidence with explicit issues. Wrong schema/digest, mixed executions,
ambiguous parents/rows or altered projected views must not yield eligible
proposals. A fixture records controlled-fixture provenance and cannot become
native by supplying a qualification-reference string. Replay adds no new
scientific execution credit.

Content digests and these checks establish byte/relationship consistency, not
authentication of an external producer or proof that a caller-declared native
run occurred. Preserve reported evidence role, actual observed worker facts and
qualification references separately; a reference string alone never upgrades
controlled data into verified scientific execution. No signing/attestation
service is proposed.

Live generation reuses the existing isolated-process supervision with a separate
analogue request/response meaning. Preserve lazy selected-engine guards,
installed-source/asset/inventory verification, absence versus provider failure,
CPU/thread/address-space/RSS/wall/headroom/output bounds and failed/partial
ledgers. The modern analogue bundle needs encoder+decoder+heads, **no PCA or
modlAMP**; do not force those de novo bundle fields onto this route.

Capture completed native encoding/loading/encoder/sampling/decoding/scoring/
analogue work and actual software/method identity through the existing Ackredit
boundary. A failed request may have completed earlier operations; preserve that
scope without crediting a successful generation that did not finish. Host
attribution requires no heavy model import. Optional attribution failure remains
distinct from the scientific provider result. Macrel retains separate attribution.

## Approved bounded implementation and acceptance cases

**R1: model-free receiving and controlled composition.** Implement the specific
receipt, mapping/diagnostics and proposal extraction after contract approval.
Exercise the existing assessment/selection boundary with explicitly artificial
provider outputs; keep a saved-data example engine-free. No learned weights.

**R2: owner codec and isolated artificial execution.** Implement the missing
reusable codec in HydrAMP and use it from the consumer; identify a separate
candidate rather than rebuilding dev5 in place. Exercise input/worker limits,
binding, failures and attribution with controlled fixtures and applicable
installed checks. Do not rerun accepted mathematical/real-weight campaigns.
Public names and internal organization remain delegated technical choices.

Required behavior to verify:

1. Mixed compatible/incompatible, initial-M, empty/incomplete, explicit chemistry,
   lowercase/unsupported and lengths 1/25/26; no normalization or lost metadata.
2. Duplicate parents with distinct nonempty candidate buckets/noise; dense-to-
   original parent and attempt-major row mapping, with no dictionary overwrite.
3. Mixed hit/no-hit, all-no-hit, empty projection, self/duplicate exclusions and
   the first accepted duplicate attempt; exact native order and raw-token binding.
4. Equal child strings across parents remain separate Macrel occurrences; tie
   order follows the declared flattening and both unchanged selectors agree.
5. Macrel-incompatible children, missing/failing rows and attribution failures
   remain inspectable; malformed/ambiguous/altered replay cannot pass receiving.
6. No compatible parents triggers no worker; limits fail before dispatch; partial
   failures keep known versus unknown progress, with no retry/refill or invented
   candidate. Missing provider does not silently choose another method.
7. Separate parent baseline may disagree with higher native scores. No claimed
   Macrel improvement follows from the reward alone, and parents are not silently
   added to the selector pool.
8. Saved replay works with scientific engine imports/assets/network blocked;
   controlled provenance is honest; the current de novo receipt/adapter and all
   existing Macrel/selector behavior are preserved by focused regressions.

**R3: separately proposed real consumer qualification.** Only after R1/R2,
freeze exact installed consumer/provider bundles, use conditions, correspondence
cases, prospective criteria, all actual neural/Macrel calls and fresh host limits.
Reuse A1/A2 numerical evidence instead of reproducing it. R3 approval is not
part of the present R1/R2 implementation request. No GPU, feedback, training,
target route, other family, release or original-author contact is included.

## Preparation check on existing boundaries

A guarded [controlled-data probe](evidence/hydramp_redesign_existing_boundary_probe.json)
uses the existing SequenceRecord, ResultSet and both selectors, with all
scientific imports, parameter reads, network and child execution blocked.
It performs zero model/Macrel calls. Its provider/ancestry data are **declared
artificial fixtures**, not produced or validated by an implemented analogue
adapter. This verifies a useful existing composition property, not R1/R2.

The example has original parent occurrences 0 (ACD), 1 (incomplete), 2 (ACD)
and 3 (MAA). A declared compatible provider mapping is [0,2,3], B=3, A=2.

| Child occurrence | Parent occurrence | Provider index | Attempt | Raw row | Projected child |
| --- | ---: | ---: | ---: | ---: | --- |
| 0 | 0 | 0 | 0 | 0 | KAAAA |
| 1 | 2 | 1 | 1 | 4 | KAAAA |
| 2 | 3 | 2 | 0 | 2 | MAAAA |

With equal, explicitly artificial Macrel scores on the first two children,
both selectors preserve their separate occurrences and choose [0,1] in tie order.
The third child is retained but excluded by the existing initial-M rule.
No native-score comparison, compatibility dispatcher or ancestry reader has
been newly implemented by this example. R1 must verify those mappings against
actual controlled provider payloads rather than trusting this declared table.

D45 records the completed review and R1/R2 commission under D14 and
[design_methodology.md](design_methodology.md). Scientific revisions or R3
execution retain their own review: agree meanings, responsibility boundaries,
important failures and acceptance criteria before extending the capability.

The [R3 record](hydramp_redesign_R3_qualification.md) retains its separate exact
plan and subsequent investigator execution authorization. Its single real case
now passes technical receiving/replay and consumes all 27 evaluations. Native
improvement produces one child with worse Macrel scores than its parent; this
does not establish scientific usefulness or change D44/D45 acceptance. Further
real work has no remaining execution allowance.
