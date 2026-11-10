# D50 generation results: implementation and qualification checkpoint

Status: **D50 synthetic-data source and exact installed-candidate qualification
complete; isolated private source consolidated by the separately authorized
local commit**, 2026-11-05.
Owners: [HydrAMP #4](https://github.com/uibcdf/hydramp/issues/4),
[HydrAMP #2](https://github.com/uibcdf/hydramp/issues/2) and
[PeptideMT #32](https://github.com/uibcdf/peptidemt/issues/32).
The [approved contract](hydramp_result_contract.md) and
[D50 authorization](evidence/hydramp_generation_result_authorization.json)
commission implementation with synthetic data and zero neural evaluations.

The subsequent [final source review](hydramp_dev8_source_review.md) finds no
blocker for this factory contract, corrects stale owner product navigation and
records the unchecked manual-dataclass constructor as an explicit API follow-up.
The separately approved twenty-one-path local commit is now complete; its
[receipt](evidence/hydramp_dev8_local_commit.json) records the exact reviewed tree.

## Concrete implementation

The separate `peptidemt-generation-results` worktree is
`../hydramp/local_data/generation-results-20261105`, based on local commit
`a77baff9de97e8ab4ae101b9b0c79122dea22ce3`. Private **0.0.0.dev8** is now
consolidated at `6a3ff905635a4bd744854cd540f8513916aa99f0` on that isolated
branch. The clean dev7 worktree and accepted resources are untouched.
Code belongs to HydrAMP; no scientific provider core is copied into PeptideMT.

- `generation_profile` returns detached selected route/score/vocabulary metadata
  and actual declared descriptor settings, or explicit missing/custom states.
  Its descriptor kwargs and native delegation share one owner definition,
  including the Eisenberg moment-constructor scale. It never prepares an engine
  or calculates a descriptor.
- `save_generation_result` snapshots completed GenerationTrace data;
  `load_generation_result` restores a `GenerationResult` without Torch, models,
  optional SDKs or another calculation. Five native arrays, dtype/shape/element
  bytes, zero positions, projected strings, duplicates, native return mapping,
  scores and retained descriptor values remain distinct.
- The owner NPZ/JSON schema has finite file/expanded/manifest/header bounds,
  typed and cross-field checks, no pickle/compression, duplicate-key/member
  rejection and non-overwriting temporary-file publication. Model/PCA history
  is caller-declared or unknown; original producer is separate from exporter.
- Explicit `integrations.result_reference` delegates to Recorda; the caller
  owns sessions/resolution/checking. `read_attribution`/`render_attribution`
  delegate existing detached payloads to Ackredit. Core data remains readable
  without either SDK; no automatic sessions, bibliography registrations or
  new scientific credits are introduced.
- Existing vocabulary projection is factored into one light owner module and
  re-exported at the former inference path. The package lazily resolves public
  exports. Data-only import is distinct from removing Torch's declared runtime
  requirement; no Torch-free installation is claimed.

Native inference classes and other inference functions retain their ASTs;
`generation.py`, `analogue.py`, `encoder.py`, `prior.py` and `_checkpoint.py`
remain byte-identical to dev7. Scientific descriptor formulas remain delegated.
The 42-package uv graph changes only the root project version to dev8. The
original `amp/` implementation, MIT notice, numerical pins and assets are not
changed. New I/O/import source is a separate candidate, not new resource acceptance.

Owner usage, constraints and errors are documented in its
`ports/pytorch/README.md` and `devguide/generation_results.md`. Existing root and
guide history is retained beneath current navigation banners.

## Actual tests, with identities kept separate

The initial implementation ran in the retained exact public-dependency fixture,
using Torch 2.15.0+cpu /NumPy 2.4.6 and published Pytest Receptor 1.2.2. Neural
module construction/evaluation and external model/array reads were blocked.
Only the explicitly declared lightweight cold-reader child was allowed.

| Stage | Observed native outcome | Scope |
| --- | --- | --- |
| Initial source core/profile/old codec | Exit 1: 46 pass, one harness-caused failure | The harness blocked `find_spec(recorda)` during the genuine-absence control |
| Diagnosed single-selector retry | Exit 0: one pass | Remove only that harness blocker; SDKs are actually absent from the clean fixture |
| Actual optional SDK source checks | Exit 0: five pass | Recorda references, changed/missing files and unchanged execution state; Ackredit original context, detached data, caller session, no new credit and provider failures |

The successful 46 checks and original failing artifact are retained, not
silently replaced by a new passing session. Peak sampled aggregate RSS was
331,735,040 bytes for the initial core worker, 288,174,080 for its retry and
87,044,096 for SDK checks; supervised walls were 19.73 s, 5.80 s and 2.17 s.
All three have zero neural/learned/PCA calls; the SDK worker never imports Torch.
The SDK lane uses actual editable Recorda 0.3.3 and Ackredit
`0.12.0+11.g74f865d` plus their shared development provider closure. It uses
published Pytest Receptor from the retained fixture, not the editable frontend.
It does not qualify public SDK installation or newer Ackredit 0.12.1.

After these precursor checks, the profile description was completed with
sampler/cast/conditioning and the shared moment-constructor scale. Regressions
were strengthened for Torch RNG, duplicate JSON, object headers, truncation,
explicit unavailable/failed attribution and preservation of all sixteen old
exports. The earlier checkpoint left the final 52-test core selection and exact
installed-candidate checks pending. Those later identities now have their own
passing evidence below; precursor outcomes are retained separately.

## Historical build interruption and diagnosed continuation

The initial build supervisor refuses before starting a child. After observed
memory recovery, a second bounded build starts but is killed when available
host memory falls below the retained **8 GiB reserve**. Peak aggregate RSS is
only 110,358,528 bytes; this is host pressure, not evidence of a build/backend
defect. No candidate wheel/sdist is produced or qualified. The native build's
buffered output was not yet persisted when its group was killed; its exception
must not be invented. A resumed driver now streams native logs to files.

The resumed qualification uses fresh run directories and keeps all old attempts:

1. Run the final focused source selection with zero neural evaluations.
2. Build dev8 source/wheel and reproduce its wheel from the source archive.
3. Install that exact wheel in a new isolated fixture with the already verified
   seventeen locked public dependencies; inspect native dependency closure.
4. Check the installed source/RECORD identities and run the final core and SDK
   controls, including fresh reading without Torch and actual SDK absence.

Drivers, declarations and source snapshots are retained under
`local_data/hydramp-result-implementation-w5p9gdfz`. The earlier 10 GiB start /
8 GiB runtime-reserve proposal is historical. The investigator subsequently
[approves a scoped serial profile](evidence/hydramp_generation_result_serial_authorization.json)
for these synthetic-data and packaging checks: one job at a time, CPU0/1, one
numerical thread, sampled 512 MiB aggregate supervisor/worker RSS stop, and at
least 4 GiB available host RAM before and throughout each job. The 8 GiB virtual
address-space ceiling remains distinct from physical RAM. D49 delegates routine
checks/retries within this profile; other work keeps its existing envelope.

The [implementation receipt](evidence/hydramp_generation_result_implementation.json)
pins final local source, earlier test sources, scripts, native failures and
resource facts. The [closeout](evidence/hydramp_generation_result_closeout.json)
records navigation checks and the
[owning issue updates](evidence/hydramp_generation_result_issue_updates.json).
Retain task-owned source/evidence and useful synthetic artifacts, owned by
#4/#2/#32, review 2026-11-19. Existing environments/resources are preserved;
the earlier checkpoint creates no installed environment; the resumed qualification
adds only the task-owned fixture described below.

## Completed final qualification — 2026-11-05

| Stage | Native outcome | Supervised wall | Peak aggregate RSS |
| --- | --- | --- | --- |
| Final source selection | 52 pass; exit 0 | 22.11 s | 333,975,552 bytes |
| Source/wheel build and wheel reproduction from sdist | Both builds exit 0; reproduced wheel bytes identical | 7.48 s | 115,892,224 bytes |
| Offline isolated installation and native dependency check | 18 compatible distributions; exit 0 | 24.05 s | 94,388,224 bytes |
| Exact installed-wheel core/profile/codec selection | 52 pass; exit 0 | 49.67 s | 353,996,800 bytes |
| Installed candidate with actual editable SDKs | Five pass; exit 0 | 5.21 s | 86,855,680 bytes |

All five jobs finish without a supervision guard failure. The largest observed
aggregate RSS is about 338 MiB. All pytest event artifacts are complete and read
through published Pytest Receptor 1.2.2; counts, zero skips/warnings and exit
statuses agree. This is the focused D50 selection, not a full inference suite.

The wheel SHA-256 is
`21d2313c761e4fb8eb76e2f506615dc8e296a74c25cd440b863f78240c7f353f`
(31,630 bytes); the source archive is
`94f760081293583621b5aebd9ef36955cc375dae46dc7c24c2f09db9790bb286`
(155,427 bytes). Both are private local artifacts. The new Linux/CPython 3.14.7
fixture reuses seventeen retained, reverified public archives with no new
third-party download, keeping NumPy 2.4.6 and Torch 2.15.0+cpu. Fourteen runtime
modules match source/wheel/installation. Wheel-declared hashes and sizes and
all installed RECORD hashes verify. One audit-helper assertion first required
identical wheel/installed RECORD text; diagnosis shows uv legitimately adds four
installation metadata files. The corrected audit verifies both sets of hashes;
no package change or repeat of passing tests is needed.

The actual SDK lane retains clean Recorda
`ff52fa5d8628d796f413b833c8abe73907990cf9` and Ackredit
`74f865d7eca1f5386235885d4ea001e53b5b822d`; the latter remains fifteen commits
behind fetched main. It does not silently update the shared environment or
qualify public SDK installation. Model-free cold reading, genuine SDK absence,
opaque/missing/failed attribution and caller-owned SDK use are exercised;
no neural construction/evaluation or learned/PCA read occurs. The SDK lane
never imports Torch. Existing inference classes/functions retain their ASTs;
vocabulary projection is equivalent after resolving the shared unchanged
alphabet constant. An initial overly strict static-helper AST assertion is
recorded separately; it requires no scientific source change.

The [qualification receipt](evidence/hydramp_generation_result_qualification.json)
pins artifacts, final source, installed modules, environment, run declarations,
failures and limits. The earlier implementation/closeout receipts are unchanged
historical evidence. The task-owned installer cache is disposable after verification;
retain exact artifacts, source, locked archive fixture and installed environment
for #4/#2/#32 review on 2026-11-19. Current qualification and remaining work are
synchronized through the existing owning issues.

This completes the approved first data-only qualification block. The later
separately authorized source consolidation creates only local commit
`6a3ff905635a4bd744854cd540f8513916aa99f0`, preserving the exact reviewed tree
and clean owner worktree. Its [source-review completion](hydramp_dev8_source_review.md)
records authority and the diagnosed pre-stage helper failure. No push, tag,
publication, third-party contact, learned/artificial neural evaluation, GPU,
live attribution, analogue/encoder archive, scientific acceptance, feedback or
family/target expansion follows. #4/#2/#32 stay open for their broader work.
