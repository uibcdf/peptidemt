---
summary: Receive the official PeptideMT starter after accepted suite registration.
issue: uibcdf/peptidemt#1
status: active
opened: 2026-10-27
closed:
verification: measured
area: [governance, packaging, ci]
guard:
normative:
blocked_by: [uibcdf/molsyssuite#146]
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
| Shared development environment | PeptideMT is not in the qualified shared development cohort. Use its official member-specific Python 3.14 Conda environment. Shared admission needs an actual future integrated install/closure/test receipt, not an editable install alone. |

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
