# HydrAMP result-constructor invariant correction

Status: **private dev9 source and exact installed-candidate qualification complete;
source remains uncommitted in its separate branch**, 2026-11-05.
Owners: [HydrAMP #4](https://github.com/uibcdf/hydramp/issues/4) and
[PeptideMT #32](https://github.com/uibcdf/peptidemt/issues/32).
This follows the [dev8 source review and local commit](hydramp_dev8_source_review.md).
The investigator's continuation commissions the routine internal correction of
that recorded API limitation within the existing D50 data-result contract.
No new scientific definition, schema, model acceptance or Git action is adopted.

## Change and preserved boundaries

The new `peptidemt-result-invariants` worktree at
`../hydramp/local_data/result-invariants-20261105` starts from clean dev8 commit
`6a3ff905635a4bd744854cd540f8513916aa99f0`. Private **0.0.0.dev9** adds
`GenerationResult.__post_init__`: direct construction and `dataclasses.replace`
validate bounded manifest JSON, SHA-256 declaration syntax, NumPy array types/
total size and the existing native cross-field validator, then retain immutable
snapshots of caller arrays. Invalid replacements fail without mutating the
original object. Public field signatures, saved schema and scientific meanings
are unchanged. Factories use the same constructor; duplicate `_record` validation
is removed without changing save/load, JSON/array reader or validator ASTs.

Manual digests must be lowercase 64-character SHA-256 declarations. A well-formed
declaration does not prove an external file exists, matches the object or was
produced by a scientific execution. `replace` retains that declaration; it does
not invent an archive or recompute ZIP bytes. The loader still hashes actual
retained file bytes. Array snapshots consume memory; format bounds are not a
worst-case RAM guarantee. Original producer/exporter identities and unknowns
remain separate, including older exporter versions in existing archives.

Only `results.py` and `_version.py` differ among the fourteen runtime modules.
All twelve other modules, native scientific kernels, optional SDK adapters and
accepted resources are preserved. The 42-package lock graph changes only its
root version. No generic recorder, resolver, attribution parser or molecular
operation is copied into PeptideMT; molecular systems remain MolSysMT-owned.
The clean dev8 branch and all earlier artifacts/receipts remain intact.

## Executed checks

| Stage | Native outcome | Supervised wall | Peak aggregate RSS |
| --- | --- | --- | --- |
| Source constructor/save/load/profile/codec selection | 73 passed; exit 0 | 30.87 s | 331,837,440 bytes |
| Directory and sdist builds | Both exit 0; identical reproduced wheel | 4.77 s | 115,752,960 bytes |
| Isolated offline install and dependency check | 18 compatible distributions; exit 0 | 10.69 s | 94,433,280 bytes |
| Exact installed-wheel selection | 73 passed; exit 0 | 6.88 s | 355,373,056 bytes |
| Actual editable SDK integrations | Five passed; exit 0 | 1.65 s | 89,968,640 bytes |
| Installed integrity and actual dev8 cold reading | Pass; exit 0 | 0.46 s | 68,141,056 bytes |

The 73-test selection includes twenty-one new constructor/replace cases and
fifty-two affected save/load/profile/codec controls. New cases cover caller-buffer
aliasing, irreversible read-only snapshots, invalid replacement without mutation,
malformed/ambiguous metadata, digest declarations, native dtype/shape/value
consistency, size bounds and preservation of older exporter identities. Existing
cold-reader and RNG controls remain relevant. All three published Pytest Receptor
1.2.2 event artifacts are complete, with no skips, failures or warnings.

The new installed reader additionally reads the actual retained dev8 synthetic
archive (7,231 bytes), SHA-256
`136c2c3180c59782ad10c6fa2a9ce94e5194c654980c0c37bc9f65c41ec5b9d0`.
It preserves that digest, native data/immutable buffers and dev8 exporter, without
Torch/SDK imports or changing archive bytes. Fourteen source/wheel/installed
modules agree; wheel and installed RECORD hashes/sizes verify.

The wheel is 32,385 bytes, SHA-256
`b808cd4c3af28fc4b1c786ecf82b59c9f0cab381949821d9fad9338273827453`;
sdist 157,610 bytes, SHA-256
`0c57a196877d9ef61e1f8b9c73b33bf4c450c374c1a5708d39916158f5f9a162`.
The exact Linux/CPython 3.14.7 fixture reuses seventeen reverified retained public
archives with NumPy 2.4.6/Torch 2.15.0+cpu. No new third-party dependency download
or shared-environment update occurs. Actual editable Recorda 0.3.3 and Ackredit
`0.12.0+11.g74f865d` retain their earlier exact sources; the latter stays fifteen
commits behind fetched main. This is not public/newer SDK or other-platform
qualification, a full inference suite or scientific acceptance.

## Resources, evidence and remaining work

All six supervised jobs complete without a guard failure. Maximum aggregate RSS
is about **339 MiB**, under the approved 512 MiB stop. Workers are serial on
CPU0/1 with one numerical thread, 4 GiB available-host reserve and bounded
wall/CPU/output/virtual memory. Neural construction/evaluation, learned/PCA reads,
real descriptors, live attribution and GPU use are zero. Source/installed core
workers import Torch for existing data controls but forbid neural construction;
the SDK lane and independent cold reader never import it.

Source preparation catches one import-order lint finding, corrected before
qualification. All runtime qualifications pass on the first invocation; retained
static/failure records distinguish preparation from scientific execution. Ruff
lint/format and compilation pass for affected files. The
[exact receipt](evidence/hydramp_result_invariants.json) pins sources, scripts,
run declarations, environment, artifacts, compatibility and existing owners.
Candidate source/evidence and the installed fixture remain for #4/#32 review on
2026-11-19; only this task's disposable installer cache is removed after checks.

The constructor gap is corrected in this qualified isolated candidate; source
consolidation and delivery/integration remain separate. The earlier one-off
permission for the dev8 commit is spent. No new commit/push, merge, package
publication, scientific acceptance, learned call, other archive kind, family/
target expansion, training/feedback or original-author contact follows. Existing
#4/#32 keep their broader product/scientific work.
