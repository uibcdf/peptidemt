# Consolidated HydrAMP source/package baseline

Status: **isolated baseline locally committed and qualified**,
2026-11-05. Owner: [HydrAMP #4](https://github.com/uibcdf/hydramp/issues/4);
consumer: [PeptideMT #32](https://github.com/uibcdf/peptidemt/issues/32).
The investigator directs continuing the source/package consolidation after the
[current product review](hydramp_product_readiness_20261105.md). This is an
engineering commission, not a new scientific method, acceptance or release.

## Concrete baseline

The isolated `peptidemt-product-baseline` branch/worktree is
`../hydramp/local_data/product-baseline-20261105`, based on original reference
`6590d2f4c2963f25d30669052a4c4a857e0e7279`. Existing dirty worktrees, installed
profiles and accepted resources remain unchanged. Local source commit
`a77baff9de97e8ab4ae101b9b0c79122dea22ce3` contains the exact approved prepared
tree `2476a08a50d32779db2f43683928450e62b66f91`. It is a local history coordinate,
not a published source coordinate. Source, seventeen test modules, developer
helpers, current documentation and the installation lock are together in this
worktree. Only the isolated branch reference changed; its worktree is clean.

The private **0.0.0.dev7** candidate preserves all nine dev6 runtime modules
byte for byte. Package presentation adds a long description and repository/issue
URLs, plus an explicit source-distribution manifest. Build-only pins select
setuptools 84.0.0 /wheel 0.48.0, already installed alongside build 1.6.1 in the
shared development profile. Numerical dependencies and optional scientific
requirements stay unchanged; the 42-package uv lock differs only in the local
project version, and its offline check passes.

Original `amp/` and the original MIT notice stay at the reference bytes. No
legacy installer, scientific equation, dtype, descriptor, preprocessing,
selector/M1–M8 contract, model asset or old wheel is modified. Historical private
receipt JSON files remain local/ignored, outside the source commit. The modern
package builds without those historical records or real model data.

## Reproducible artifacts and installed qualification

| Artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| Source distribution | 141,198 | `c4e050d561a3736ed7b527e834175aec5156e436d7aae4312d556023b559581f` |
| Wheel | 21,771 | `18347066126c439279328224ef71b158f9077a1a67954c742839e0596393c83d` |

With `SOURCE_DATE_EPOCH=1732656418`, umask 0022 and normalized package modes
(files 0644/directories 0755), directory and extracted-source-archive builds
produce the **same wheel byte for byte**. The final archive contains no learned
weights, PCA dump or scientific-run payload. Its wheel is also byte-identical
to the wheel used by the completed installed check, so that check is reused
after a source-history navigation fix rather than run again.

A fresh isolated Python3.14 fixture receives seventeen faithful retained
dependency payloads/metadata from R3, excluding PeptideMT and its support
packages. uv 0.9.18 installs the new wheel offline with no dependency resolution
or upgrade. Native dependency checking passes for eighteen installed packages.
Third-party console scripts are not newly installed/qualified, and this is
**not a clean public dependency-install claim**. Public dependency/index and
other-platform delivery remain separate work.

All sixteen public exports are present from the fresh installed prefix. The
**seventeen existing codec-only checks pass**, with complete Pytest Receptor
evidence received through its supported reader. Neural module construction/
forward calls, learned/PCA reads, foreign models, network and child dispatch
are forbidden in the check. There are zero neural evaluations. The original
source/installed/numerical campaigns retain their exact prior scope and are not
repeated merely because package presentation changed.

The worker uses CPU0/1, one numerical thread, 180 s wall/120 s CPU, 8 GiB virtual
address space, sampled 2 GiB aggregate RSS stop and 8 GiB host reserve. It
completes in 17.44 s, peak sampled controller/worker RSS **292,663,296 bytes**
(about 279 MiB). No guard fires in the corrected final check; no GPU is used.

## Diagnosed engineering failures retained

- An initial build wrapper resolved Git from the wrong working directory,
  leaving an empty source epoch. An absolute owner path and explicit environment
  correct that wrapper; the failed attempt/artifacts remain retained.
- Initial wheels had identical payloads/order/timestamps but different ZIP
  permission bits for LICENSE/top-level metadata. Explicit modes/umask correct
  reproducibility without touching runtime content or the wheel backend.
- The first installed-check monitor incorrectly counted the pre-existing
  dependency fixture as new output. A dedicated output directory corrects the
  caller layout, retaining the same limits and unchanged common supervision
  helper. The stopped attempt is not a passing test run.
- A copied historical Markdown reference pointed outside the owner tree.
  Boundary checking removes it from the copied manifest; its referenced consumer
  file remains byte-identical. External authority is a reference, not an owner
  source file to relocate.

None of these diagnoses changes a sister component or the numerical model.
The [baseline receipt](evidence/hydramp_product_baseline.json) pins scripts,
source/staged tree, build/profile records, failures, final artifacts and checks.
Raw evidence is in `local_data/hydramp-product-baseline-uepif2a_`, owned by
#4/#32, retention review by 2026-11-19.

The [preparation closeout](evidence/hydramp_product_baseline_closeout.json) and
[initial issue updates](evidence/hydramp_product_baseline_issue_updates.json)
retain their pre-commit checkpoint unchanged. The investigator subsequently
[authorizes the single local commit](evidence/hydramp_product_baseline_commit_authorization.json).
The [commit receipt](evidence/hydramp_product_baseline_commit.json) records its
native exit, parent/tree identity, preserved branch references and clean
worktree. The [updated existing issue records](evidence/hydramp_product_baseline_commit_issue_updates.json)
carry the completed local source coordinate.
The [commit closeout](evidence/hydramp_product_baseline_commit_closeout.json)
records final navigation/status checks and reuse of the unchanged qualification.

## Remaining boundary

The authorized local Git action is complete. The committed source intentionally
retains its dated preparation checkpoint; the later commit receipt records its
completion without amending the exact approved tree. Git identity alone changes
no package/runtime bytes, so the successful build and installed checks are reused.

The subsequent [public dependency qualification](hydramp_public_installation.md)
installs freshly retrieved exact base/test wheels and the private own wheel in
a new environment; seventeen codec-only checks pass. This later milestone does
not relabel the retained-payload fixture above as a public installation.
Public HydrAMP distribution/source-build qualification and an independent
scientific result/workflow contract remain open product work under #4/#32.
No push, release, new schema/CLI, training, family/target extension or model
acceptance follows. Scientific and use limits from the current product/data
reviews remain unchanged.
