# HydrAMP dev9: final source review and local commit proposal

Status: **focused source review complete; commit prepared but not authorized or
executed**, 2026-11-05. Owners:
[HydrAMP #4](https://github.com/uibcdf/hydramp/issues/4) and
[PeptideMT #32](https://github.com/uibcdf/peptidemt/issues/32).
The investigator continues after the
[constructor correction qualification](hydramp_result_invariants.md). This is a
review/consolidation preparation step, with no source edit or repeated worker.

## Outcome

No new blocker is identified for the corrected constructor/replace contract.
Public dataclass field signatures, native schema validator and save/load/
JSON/array-reader ASTs match the dev8 baseline. Constructor JSON/digest bounds,
array snapshots, invalid replacement behavior and declared-digest semantics
remain consistent with the existing D50 result contract. A declaration is not
file authentication or scientific attestation; extra snapshots have memory cost.

All twelve managed paths match the exact
[qualified dev9 receipt](evidence/hydramp_result_invariants.json), SHA-256
`15c5814cfec53531e51f5424d46ea54f028e0e345fd9b30f2bd0537cf77c81d3`.
Its 73 source /73 exact installed /five SDK passes, complete event artifacts,
reproducible wheel and old-archive compatibility evidence are reused. No new
pytest, build, installation, numerical test or model execution is performed.
The clean committed dev8 and all earlier resources remain preserved.

## Concrete proposal

Prepare **one local commit** on `peptidemt-result-invariants`, parent
`6a3ff905635a4bd744854cd540f8513916aa99f0`, exactly twelve owned paths.
Proposed subject: `Validate generation result construction and replacement`.
Expected content tree: `b8a334085bac8bf6c0d31c2cc9586ad1f311eb40`.
The complete patch, path list and English message are retained in the task.
Tree computation is verified against the existing base tree without writing Git
objects/index. This is a proposed content identity, not an existing commit,
source publication or scientific admission.

The previous permission covered only the completed dev8 commit. D50 and owner
instructions do not authorize another commit/push through local editing alone.
This proposal therefore awaits separate authorization; no commit, push, merge,
release or scientific scope change occurs. The separate
[target-case feasibility proposal](target_case_mdm2_reference_proposal.md) is an
analysis output under #33, not part of this provider source commit.
