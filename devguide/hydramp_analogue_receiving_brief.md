# Analogue consumer receiving and acceptance brief

Status: **pre-A2 brief retained; concrete consumer contract now prepared**,
2026-11-04. Owner: PeptideMT #32; provider: HydrAMP #4. This accompanies the
[A1 work order](hydramp_analogue_work_order.md) and
[continuation plan](continuation_plan_2026_11_04.md).

Subsequently, A2 executes and D44 accepts the experimental provider route. The
[concrete redesign work order](hydramp_redesign_work_order.md) now specifies
admission, ancestry, receiving, assessment/selection and controlled verification
for review. This earlier brief grants no implementation or new execution budget.

## Input and ownership

Preserve each prototype occurrence and its original SequenceRecord/source/context
and chemical unknowns. The first route must not strip explicit chemistry or
truncate/repair inputs to force compatibility. A future sequence-facing route
needs the provider's public native vocabulary codec and supported MolSysMT
transport; the A1 provider currently accepts CPU int64 [B,25] model tokens.
This brief does not add a PeptideMT token encoder or silently treat a raw token
batch as a fully specified molecular system.

## Correspondence and all outcomes

Retain an ordered result for every prototype, including repeated strings.
Link each attempt by prototype occurrence, attempt index and original trace row
(attempt-major a*B+i); preserve all attempted raw tokens, noise, latent inputs,
native scores and decisions, including rejected, self and duplicate views.
Within each prototype, accepted strings retain lexical/first-accepted-attempt
semantics. No-hit means no candidate survived that native procedure; distinguish
it from no returned work, provider failure, incompatible input and partial output.

Generated empty/internal-zero projections remain raw provider evidence. An empty
display is not silently repaired, relabelled a no-hit or passed off as an assessed
molecule. A compatible projected string can be assessed by an independently
qualified sequence route, with explicit attribution to that view; its native
token score must not be copied to a re-encoded token representation.

## Evaluation and attribution

Native strict AMP/low-MIC-class improvement is not measured improvement,
hemolysis or either current selector. Existing Macrel ResultSet/selector meanings
remain unchanged. Preserve links from returned proposal to its prototype and
attempt even when the Macrel route rejects it (for example initial M) or fails.
Keep generator and assessor versions, artifact/profile identity, actual resource
use and native attribution distinct. Review Recorda/Ackredit ownership before
adding generic provenance or persistence services.

The provider's in-memory AnalogueTrace is not an adopted portable schema. A
consumer record/public API needs concrete review, compatibility and honest
evidence binding; caller snapshot names alone are not content identity. Existing
HydrAMPReceipt is for its selected de novo route and must not be overloaded with
analogue meaning without an explicit reviewed change.

## Acceptance cases to prepare before real consumer execution

- Repeated prototypes, distinct attempt noise, exact order/mapping and preserved
  strict-score equality decisions; no prototype dictionary overwrite.
- Mixed hit/no-hit results, empty/generated projections, self/duplicate outputs
  and partial/failure data without invented counts or favorable replacements.
- Source/raw tokens and projected views remain distinguishable; no hidden codec,
  descriptor, filter, chemistry or native-score change.
- Macrel incompatibility, missing results and failures are kept per occurrence;
  selection uses exactly its current eligible evidence and no native-score gate.
- Engine-free saved replay and a separately approved live consumer case verify
  provider-to-consumer correspondence and ancestry. Reuse existing qualified
  math evidence rather than repeating the full numerical campaign.

A2 must expose the inputs/outputs needed for these cases before its exact plan
is approved. Neither A1 artificial tests nor this brief grants real analogue,
new consumer redesign, feedback or target-conditioned execution authority.
