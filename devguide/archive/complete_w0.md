---
summary: Receive the official PeptideMT starter after accepted suite registration.
issue: uibcdf/peptidemt#1
status: resolved
opened: 2026-10-27
closed: 2026-10-27
verification: measured
area: [governance, packaging, ci]
guard:
normative: MOLSYSSUITE_GUIDE.md
blocked_by: []
supersedes: []
---

# W0: official starter integration and qualification

## What and ownership

Diego Prada-Gracia/UIBCDF owns PeptideMT. The investigators authorized W0–W4
under D35–D36, conditional on completed W0, and expressly authorized this one
local receiving issue on 2026-10-27. No other issue, scientific implementation,
model execution, release or package publication is included in W0.

Central registration is accepted: scientific-component / primary / incubating /
active / python-package. [MolSysSuite #146](https://github.com/uibcdf/molsyssuite/issues/146)
remains partial until the component is received. W1 has not started.

## Genuine generation and preserved history

- Design parent: `7781293d7aba96bac526de8fa051dd517bc3cc30`.
- Central accepted admission: `8a94e16f1ba26122304df264e89c4eca15afaf5a`
  through [PR #147](https://github.com/uibcdf/molsyssuite/pull/147).
- Generator/source checkpoint: `784d7cb7a948ee539372592142e6d7004dea77b1`.
- Immutable `policy-v1.5.10` resolves to
  `1c38d50337ffd67e20eb02f5e02b24152073b3b4`; tag object
  `0cb9555ace0a62ef3b8fdae261a9e55bb22ad660` is unchanged.
- The admission commit was verified on fetched central main ancestry. The
  official generator was invoked from the central checkout as a module, into
  the absent/empty task-owned `/tmp/peptidemt-w0-dealNh/starter` destination:

```bash
python -m devtools.scripts.bootstrap_component /tmp/peptidemt-w0-dealNh/starter \
  --repository uibcdf/peptidemt \
  --description 'Peptide design and attributable functional evaluation' \
  --admission-sha 8a94e16f1ba26122304df264e89c4eca15afaf5a
```

The generated source package, metadata, environments, workflows and report tools
were integrated. Existing README, root/nested instructions and ignore rules were
explicitly merged, preserving scientific working rules and design navigation.
All existing scientific documents and decisions remain, with dated receiving
updates where applicable. No repository or Git history was replaced. The weekly
schedule is staggered at `47 6 * * 3`. Routine and matrix lanes additionally
check dependency closure and installed import from a neutral directory, outside
pytest's deliberate source path. No native model or scientific operation exists.

The canonical guide was synchronized with the official
`sync_vendored_guides --guide MOLSYSSUITE_GUIDE.md --repository peptidemt --write`
route. Its SHA-256 is
`caf48e39e3ba0dc044114c6b775ab799b541c4e342bab24435afbcef40005e5d`.
Guide bytes and policy adoption are separate evidence.

## Applicability reviews for this source-only baseline

| Boundary | Finding and next obligation |
| --- | --- |
| ArgDigest | No scientific public argument operation exists in W0. No unused runtime dependency. Reassess W1's nontrivial input/selection contracts. |
| DepDigest and SMonitor | No optional engine/execution or user diagnostic boundary exists yet. Reassess and use at W2's selected Macrel route; their absence now is not a runtime exception. |
| PyUnitWizard | No physical quantities or quantity exchange exist in the empty package. Unitless future predictive scores do not create physical units. |
| Pytest Receptor | Exact published `1.1.0` is in the generated test extra and both Conda environments; actual test use is recorded below. It changes reporting, not assertions or exit status. |
| GH Run Receptor | First hosted inspection uses the published operator tool; native run/job/step verification remains authoritative. No runtime dependency. |
| Optional engines / Ackredit | No implemented scientific/provider boundary. Non-applicable for W0 only; `optional_engine_review.md` must be completed when W2 introduces one. |
| CI and platforms | Full baseline tests for routine Linux/Python 3.14 push/PR; weekly/manual Linux 3.11–3.14 matrix. No skip markers or deferred expensive suite. No public OS support claim yet; no macOS/Windows claim or Intel macOS target. Configured jobs do not prove execution. |
| Distribution | Source-only developer installation, no runtime dependencies and no vendored scientific assets. No Conda recipe, credential request, package-channel claim, public version/tag, release, DOI or archival claim. Publication controls are not applicable until separately commissioned. |
| Resources and coverage | No generated/binary scientific resources. Baseline import and reporting tests are engineering evidence, not meaningful scientific coverage; no coverage percentage badge. Reassess under the same W0 issue when W1 introduces behavior. |
| Shared development environment | The investigator confirms `molsyssuite@uibcdf_3.14` for routine development. PeptideMT installs editable there with verified neutral import and no added dependency findings. The original clean member fixture remains qualification evidence; central fresh expanded-cohort integration is a separate gate. |

No required runtime edges exist. The test extra's Pytest Receptor and actual GH
Run Receptor operator use must be represented as distinct test-tooling/ci-tooling
edges in the central inventory using the eventual exact component commit.
No molecular operations duplicate MolSysMT; no other suite member or model is
made a runtime requirement by documentation mentions.

## Executed evidence and receiving obligations

Official generation succeeded. Current central source conformance passed after
integration. The initial manifest audit correctly reported the new unrecorded
`test: pytest-receptor` relationship; central receiving must record it rather
than changing the generated dependency or weakening the audit. The genuine
frozen-policy/admission route, local checks, installed package, hosted routine
and full matrix evidence are recorded below as they execute. Pending evidence
is not a pass.

Acceptance requires:

1. Correct source and frozen-policy/admission conformance, byte-identical guide,
   reporting/index, Ruff and relevant local baseline tests.
2. Actual Python 3.14 Conda resolution, import origins and dependency closure;
   separately a neutral installed-package check, not source-shadowed pytest alone.
3. Required native hosted routine/full cells on the exact component candidate,
   all required install/test steps executed; skipped cells are not passes.
4. Member-specific ecosystem/CI/distribution review evidence tied to this issue;
   central inventory and guide/dependency/vendored-guide audit recovery.
5. Actual central W0 receiving before W1. Inspect repository administration and
   state missing authority/evidence explicitly; never imply branch protection
   from green workflow checks.

## What is not established

There is no scientific API, Macrel installation/execution, AMP/hemolysis model
qualification, M1–M8 execution, HydrAMP work or completed V0.1. Neither the empty
package import nor admission CI proves biological utility or public distribution.
No failed, skipped, missing or incompatible check is relabeled successful.

## Temporary-resource ownership

`/tmp/peptidemt-w0-dealNh` belongs to the admission task. It contains the official
staged starter, central/frozen-policy source, disposable qualification environments
and logs. Retain only while needed for actual W0 receiving; remove task-owned
resources at closeout and preserve primary checkouts and shared environments.

## Local baseline evidence — 2026-10-27

- The official member-specific Conda environment resolved from the generated
  development YAML on Linux x86_64: Python 3.14.10, pytest 9.1.1,
  pytest-receptor 1.1.0, Ruff 0.16.5. No Macrel distribution or weights installed.
- Editable installation with `--no-deps --no-build-isolation --editable .`
  succeeded. Its precommit development identity was
  `0.1.0+33.g7781293.dirty`, not a release identity. Import resolves to this
  checkout's `src/peptidemt/__init__.py`; `pip check` reports no broken requirements.
- `python -m pytest --receptor=llm`: **2 passed**, no skips. This is the complete
  starter baseline suite, solely package import and reporting/index validity.
- `devtools/devguide_index.py --check`, Ruff lint/format, relative file-link and
  whitespace checks passed. No scientific assertion is tested by these checks.
- Current central conformance passed. The real frozen-policy checker at
  `1c38d503` with the central admission root and full `--admission-sha`, plus
  `--skip-guide-content`, also passed. Canonical guide SHA-256 separately matches.
- Native administration inspection: Actions enabled; main initially unprotected;
  connected maintainer has administration authority. Required-check/protection
  completion is pending real hosted check names and must remain visible.

Pending: exact committed installed artifact and hosted routine/full matrix,
actual operator inspection, central dependency/review inventory and failed-audit
recovery, and central W0 receiving. W1 remains gated.

## Executed committed-source and hosted evidence

The published starter integration candidate is
**`bed3df6908cee7e3c3325e1205afdf3d1f96aa13`**, with design parent `7781293`.
The complete two-test baseline passes locally, with no skips.

| Gate | Exact-candidate evidence | Scope |
| --- | --- | --- |
| Routine push / quality | [40568925289](https://github.com/uibcdf/peptidemt/actions/runs/40568925289), attempt 1, test job `122417570461`, quality job `122417571120` | Actual build/install, `pip check`, neutral installed import and 2-test full baseline; Ruff lint/format. Scheduled-only matrix skipped here by design. |
| Frozen policy / admission | [40568925878](https://github.com/uibcdf/peptidemt/actions/runs/40568925878), attempt 1, `122417574381` | Actual admission validation, frozen policy checkout and conformance, lint and format; no scientific evidence. |
| Complete Linux matrix | [40568960388](https://github.com/uibcdf/peptidemt/actions/runs/40568960388), attempt 1 | Python 3.11 job `122417696779`, 3.12 `122417696624`, 3.13 `122417696903`, 3.14 `122417696804`: all installed/closure/import and full baseline test steps executed and succeeded. Quality job `122417696189` passed. Push-only routine job skipped, not counted. |

Native run identity and required job/step conclusions were inspected separately.
GH Run Receptor **1.3.0**, from the actual `uibcdf` noarch Conda artifact, reports
PASS for the matrix (5 executed jobs, one event-inapplicable skipped job).
The initially requested 1.2.0 was not available through PyPI or current UIBCDF
solver records; no use of that version is claimed. A partial `/tmp` operator
installation hit the host's quota and was removed; the actual operator was
installed in a task-owned workspace directory. No shared environment was repaired.

The local exact-source wheel is
`peptidemt-0.1.0+34.gbed3df6-py3-none-any.whl`, SHA-256
`145f3e0ce01ba65e962e7467231c5c07a8e0e3900945495f582701caeb5cfc20`.
It was installed with `--no-deps --force-reinstall` into the task's dependency-clean
Python 3.14.10 environment. From `/tmp`, isolated Python verifies the import
matches the installed distribution's `peptidemt/__init__.py`, rather than the
source tree. This development wheel was not uploaded or publicly distributed.

Native administration now verifies Actions enabled and main protection with
strict required checks `test`, `quality`, `policy / conformance`; force pushes
and deletions disabled. Ordinary changes require PR checks; administrator
bypass remains available for the explicitly authorized internal direct-push
route (`enforce_admins=false`). No new scientific approval or peer-review count
was imposed (`required_approving_review_count=0`).

The hosted baseline at `bed3df6` establishes engineering compatibility only.
Any later receiving-document commit has its own run identity; original candidate
and wheel provenance remain unchanged. No actual PR-event run was used for the
above evidence; the full PR suite is configured as the same tested routine gate.
Central receiving must judge that distinction, not treat a configured event as an
executed PR. No science or Macrel test was run, omitted or relabeled.

Still due: publish the central test-/CI-tooling edges and member review evidence,
recover the applicable central audits, and obtain actual W0 receiving. The
source-only distribution review can remain partial for future publication work;
no Conda recipe/public artifact is commissioned. Keep both #1 and central #146
open until receiving. W1 has not started.

## Pause requested by the investigators — 2026-10-27

**W0 is partial and paused; W1 has not started.** The investigators request a
clean, reported handoff before continuing implementation with Codex. This does
not revoke D35–D36 or authorize skipping any gate. Retain the existing issues;
no replacement admission issue, alternative starter or new architecture is needed.

The [durable evidence receipt](../evidence/w0_baseline.json) records source,
policy/admission, exact local wheel, actual Conda package identities and tested
scope. All three baseline hosted runs also received a PASS from published
GH Run Receptor 1.3.0; native job/step verification is independent. The receipt
contains no model binaries, private transcript or credentials.

### Resume in this order

1. Read D35–D36, `increment_1_work_order.md`, this record, PeptideMT #1 and
   central #146. Inspect actual current heads and preserve concurrent changes.
2. Return the existing W0 evidence to central review; record the actual test-/CI-
   tooling relationships and member-specific applicability reviews. The initial
   manifest failure is the unrecorded `test: pytest-receptor` extra edge, not a
   runtime dependency or failed native model. GH Run Receptor's actual operator
   use is a separate CI-tooling edge. Use exact component source references.
3. Rerun/inspect central component-guide, dependency and vendored-guide audits.
   The earlier global vendored-guide failure did not expose paths; do not assert
   that it was exclusively PeptideMT or fix unrelated components silently.
4. Obtain actual central W0 receiving. Keep #1 and #146 open until that result;
   archive this local record only upon genuine completion. The full PR lane is
   configured but no PR-event execution is claimed by the baseline evidence.
5. Only then execute W1–W4 within the existing authorization. First W1 must work
   without Macrel. W2 integrates one genuine Macrel route. W3 needs Macrel 1.6.1
   and both actual ONNX heads on the Linux CPU/Python 3.14 qualification target,
   with assets/terms/fixtures/effective resource bounds identified first.
   M1–M8 remain entirely unexecuted at this pause. W4 supplies reproducible
   example, tests/docs and exact evidence; incomplete work remains incomplete.

HydrAMP, increments 2/3, target-conditioned generation, new scientific models,
package publication and other development issues remain excluded. Scientific
changes return to the investigators. Temporary source/environments/artifact and
receptor caches are task-owned and may be removed after durable evidence and
issue handoff; reproduce from the official routes, not those transient paths.

## Central W0 receiving follow-up — 2026-10-27

The investigator confirmed the named shared Linux development environment,
`molsyssuite@uibcdf_3.14`, rather than a separate member environment for daily
work. Actual Python 3.14.7 installation from source
`d1d6b1c3949a95abed1e4072f6b6fb0223a971cd` succeeds using
`pip install --no-deps --no-build-isolation --editable`. Neutral-directory
`python -I` resolves the primary clone's `src/peptidemt/__init__.py`. The two
baseline tests pass. Twelve pre-existing host dependency findings remain
unchanged, with zero new findings; this does not assert globally clean closure.
Seven are earlier external Amber-related findings and five concern stale local
Recorda/Praxis metadata, separately tracked under uibcdf/molsyssuite#135.
Neither those sources nor the local editable receptor installations were changed.

The central native receiver independently verifies the original exact-candidate
routine, manual full-matrix and policy gates: 40568925289, 40568960388 and
40568925878. All ten qualification input files remain identical through
`6be2d6ad4d9ef7148200d17dde1b2fcf1c5deec0`. Subsequent scientific design
prose is preserved. Original installed-wheel identity remains attached to its
original source; it is not rebound to a later commit.

The registered Pytest Receptor and GH Run Receptor guides are delivered with the
official synchronizer from committed canonical provider sources. Root
instructions require them. Central inventory records the existing test-tooling
and CI-tooling edges, W0 applicability reviews, full routine baseline policy and
source-only distribution review. No unused runtime support dependency, Conda
publisher, public platform claim or model execution is introduced.

The central receipt is
`uibcdf/molsyssuite:devguide/rollouts/peptidemt_w0_receiving_146_20261027.json`.
Final consumer gates, central guide/dependency audits and expanded-cohort
integration must succeed before W0 is marked received. The frozen policy and
admission SHA remain unchanged. Public Python admission is distinct from
shared-development authorization and the executed source compatibility matrix.

## Resolution — 2026-10-27

Central W0 engineering receiving is accepted under the investigator-authorized
route. The baseline candidate `9fb287b6bbf4ef2c5817ea203e56b4616d9a0ac7`
passes routine CI 40579200735, full Linux/Python 3.11–3.14 matrix 40579199849
and frozen-policy/admission 40579201439, with native required job/step facts
verified. The original wheel remains tied to its original candidate.

Central delivery `8f4222591f67ffa7eb26cb347dfa82a1db12c294` passes the
16-Python-member manifest audit (40579261933), 17-member common-guide/AGENTS
audit (40579262139) and the fresh fifteen-member shared editable integration
(40579262099, Python 3.14.10). The latter includes this exact PeptideMT baseline,
clean dependency closure, native C/Rust probes and source/official-Qt imports.
The recovered central governance gate at `73b9055a8432b4422848dac80ebbf63bfc1b6591`
passes 544 tests with one existing opt-in native Mamba test skipped
(40579703176). The PeptideMT baseline has no skipped test.

All three registered PeptideMT guide copies match committed canonical sources.
The global vendored-guide run 40579262061 still fails for twelve pre-existing
GH Run Receptor guide copies in other members; it is not reported green and
that provider rollout is outside this PeptideMT-only scope. This does not erase
its debt or establish adoption by those consumers. Central retains its bounded
diagnostic and independent PeptideMT comparison in the receiving receipt.

The durable policy is `MOLSYSSUITE_GUIDE.md`, the genuine frozen-policy caller
and central registration/reviews. The existing full baseline tests and native
policy/quality gates protect their respective import, reporting and engineering
contracts; the reporting test alone does not prove scientific readiness.
W1–W4, Macrel/M1–M8 and publication remain separate, unexecuted component work.
Final documentation-only closeout is followed by its own applicable native gates.
