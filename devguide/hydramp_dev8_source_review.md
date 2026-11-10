# HydrAMP dev8: final source review and consolidation proposal

Status: **review complete; the exact authorized local source commit is consolidated**,
2026-11-05. Owners:
[HydrAMP #4](https://github.com/uibcdf/hydramp/issues/4),
[HydrAMP #2](https://github.com/uibcdf/hydramp/issues/2) and
[PeptideMT #32](https://github.com/uibcdf/peptidemt/issues/32).
The investigator requests continuation after the completed
[D50 qualification](hydramp_generation_result_implementation.md). This review
uses D49 and the approved D50 serial resource profile; it does not expand science
or infer commit/push authority from an editing instruction.

The later [constructor-invariant correction](hydramp_result_invariants.md)
addresses R2 in a separately qualified private dev9 candidate. This dev8 review,
commit and immutable receipts retain their original source/evidence scope;
no additional Git action follows from that correction.

## Review outcome

No correctness blocker is identified within the approved completed-generation
save/read/profile contract. This is a focused source review, supported by the
existing synthetic qualification, rather than proof of general correctness,
scientific equivalence or release readiness. Runtime/package/test bytes and the
qualified private wheel remain unchanged throughout this review.

| Boundary reviewed | Source observation and supporting evidence |
| --- | --- |
| Scientific payload | Five exact native arrays, projection/occurrence/return mapping, score ranges, descriptor values and declared configuration are checked; existing exact round-trip/corruption tests retain their own receipts |
| Native methods | Generation/analogue/encoder/prior/checkpoint bytes remain dev7; inference classes/other functions retain their ASTs; token projection resolves the same shared alphabet |
| Independent reading | Only NumPy/standard-library data operations; finite file/member/header/manifest limits, no pickle, regular-file checks and non-overwriting publication; existing cold-reader controls apply |
| Provenance | Original producer/resources/environment declarations and unknowns remain distinct from exporter identity; valid structure/digest does not attest execution or authenticity |
| Owner boundaries | NumPy owns array storage; Recorda references/checking and Ackredit detached readers/rendering remain explicit and caller-owned; no molecular-system or general FASTA implementation is copied from MolSysMT |
| Optional providers | Existing source/installed/development-SDK evidence stays separate; no provider or shared environment is updated by this review |
| Public result type | Save/load factories validate and freeze their outputs; direct dataclass construction does not enforce those invariants, as confirmed below |
| Product documentation | The current product map still described dev6 and gaps already addressed by dev7/dev8; corrected with exact historical preservation |

## Findings and disposition

**R1 — stale product state, corrected.** Owner
`devguide/pytorch_product_status.md` still called dev6 current, described project
URLs/long description as missing and treated independent result I/O as future
work. These statements disagreed with the delivered dev7 baseline and qualified
D50 slice. The current map now identifies exact dev8 source/artifacts, twenty
exports, fourteen modules, actual installation/SDK lanes, completed work and
remaining scientific/product limits. Its full original bytes are preserved in
`devguide/pytorch_product_status_dev6_20261105.md`; the guide index links the
current map. No accepted model card or original scientific record is rewritten.

**R2 — unchecked direct constructor, confirmed follow-up.** The public frozen
`GenerationResult` dataclass has no constructor validation/copy hook. Calling
it directly can retain caller-mutable arrays and arbitrary manifest/digest
strings; `dataclasses.replace` similarly bypasses the save/load validation path.
A model-free diagnostic against the exact installed wheel confirms that mutating
a caller array changes the manually constructed object's array. It does not
exercise a saved archive or contradict the validated immutable factory outputs.

The current product guide explicitly documents this boundary and directs retained
results through `save_generation_result` / `load_generation_result`. Existing
HydrAMP #4 receives the confirmed observation and an API follow-up: clarify or
enforce construction invariants before public API stabilization. No particular
constructor redesign is adopted by reporting it. This is not a blocker for the
approved factory contract or a claim that a manually constructed object attests
scientific execution. No code is changed merely to obtain a new passing count.

Transport maxima are format bounds, not measured worst-case RAM guarantees.
The focused tests do not qualify every filesystem, a full inference regression,
newer/public SDK routes, or future schema migrations. Those limits remain
explicit rather than becoming new acceptance claims.

## Evidence reused and one new diagnostic

The immutable [qualification receipt](evidence/hydramp_generation_result_qualification.json)
retains 52 source, 52 exact installed-wheel and five actual SDK passes, complete
published Pytest Receptor 1.2.2 artifacts, reproducible wheel bytes, installed
integrity/native closure, all previous failures and exact environments. Package
and test source hashes are checked against that receipt; these accepted tests
are not repeated for the documentation correction.

The one new constructor diagnostic exits 0 in **1.54 s**, with **62,324,736 bytes**
maximum sampled aggregate supervisor/worker RSS. Limits are one serial worker,
CPU0/1, one numerical thread, 30 s wall/10 s CPU, 512 MiB aggregate RSS stop,
4 GiB host reserve and 8 GiB virtual-address-space ceiling. Torch/model/SDK
imports, network/child dispatch and array/model payload reads are forbidden.
Neural evaluations, learned/PCA reads and real descriptor calculations are zero.
The native exit establishes that the stated constructor observation is confirmed;
it is not an additional scientific or ordinary pytest qualification.

The [review receipt](evidence/hydramp_dev8_source_review.json) pins current source,
diagnostic declaration/result, documentation checks, exact qualification reuse
and the concrete commit proposal. Suite inspection preserves the dirty PeptideMT
clone and clean Ackredit source fifteen commits behind fetched main; no pull,
merge, stash or shared-environment replacement occurs. Canonical suite guidance
matches the previously read revision. Existing source/artifact fixtures remain
owned by #4/#2/#32, retention review 2026-11-19.

## Reviewed Git proposal (pre-commit checkpoint)

Prepared action: **one local commit**, on `peptidemt-generation-results`, parent
`a77baff9de97e8ab4ae101b9b0c79122dea22ce3`, with exactly **21 owned paths**:
the nineteen qualified implementation/profile/test/metadata/document paths,
the refreshed product status and its preserved dev6 historical copy. The full
review patch, path list and English commit message are retained locally.

Proposed subject: `Add independent generation results and provenance profile`.
Expected tree: `cc2c11506e0df4a6238c774e85a12ce0ce82fc52`. This tree identity is
computed without writing Git objects/index and verified against the known base
tree algorithm. It is a proposed content identity, **not an existing commit,
accepted registration or public source coordinate**.

D50 and both root/owner `AGENTS.md` explicitly exclude commit/push from the
data-only commission. This reviewed proposal therefore awaited separate Git
authorization. The investigator subsequently approves exactly this action;
the original review/proposal receipts retain their pre-approval state.

## Authorized local commit completed — 2026-11-05

The [single-commit authorization](evidence/hydramp_dev8_commit_authorization.json)
is executed as local commit
`6a3ff905635a4bd744854cd540f8513916aa99f0`, subject
`Add independent generation results and provenance profile`, on
`peptidemt-generation-results`. Its parent is
`a77baff9de97e8ab4ae101b9b0c79122dea22ce3`; its tree is exactly the reviewed
`cc2c11506e0df4a6238c774e85a12ce0ce82fc52`. Exactly twenty-one paths change,
with one new commit, clean index and clean owner worktree. The
[commit receipt](evidence/hydramp_dev8_local_commit.json) records these checks.

An initial pre-stage helper assertion misread Git's first porcelain-status row
because it stripped a leading space. It stops before `git add` or `git commit`,
leaving HEAD/index unchanged. Diagnosis and the parser correction are retained;
the corrected invocation creates the sole authorized commit. This is a helper
failure, not a source or Git defect, and needs no second commit authorization.

The committed documentation preserves the exact reviewed pre-commit checkpoint;
this completion record supersedes its pending-Git descriptions. No amendment or
second owner commit changes the authorized tree. Package/test bytes, the wheel,
qualified environments and every earlier scientific/implementation receipt
remain unchanged. Accepted tests/builds are reused rather than rerun for Git
consolidation. No push, tag, merge, release, model call, scientific acceptance
or third-party contact occurs. Broader #4/#2/#32 remain open, including the
unchecked direct-constructor follow-up and scientific/product work.
