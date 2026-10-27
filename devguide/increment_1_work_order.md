# Increment 1: implementation readiness and commissioning brief

Status: **scientific design closed within the agreed scope under D35;
commissioning/admission brief proposed, not authorized for execution**,
2026-10-27. No issue, central registration, bootstrap, scientific code, model
installation or execution is authorized by this document. HydrAMP remains outside
this implementation assignment; H0–H4 remain a qualification proposal.

Navigation: [index](README.md) · [accepted scientific contract](v0_1_increment_1.md)
· [decisions](decisions.md) · [working agreement](design_methodology.md).

## 1. Readiness finding and fixed scope

**Scientifically ready for a bounded implementation assignment; admission and
operational readiness are not yet established.** D35 approves the Macrel contract,
M1–M8 and both reference selection policies. Do not reopen general architecture
or compare more model families before implementing this agreed capability.

The approved deliverable is a small PeptideMT library that accepts external
single-peptide canonical sequence proposals/FASTA, retains per-occurrence input
and chemical metadata, evaluates compatible views with actual Macrel and selects
reproducibly from unchanged results. Preserve negatives, both native scores,
labels, compositional categories, precision, failures and provenance. Missing or
anomalous evaluations never receive invented scores. Empty results and inability
to execute the requested provider are legitimate explicit outcomes.

Approved sequence preservation means leading-M inputs are incompatible with the
native route that removes their initial residue; they remain valid proposals.
Neither clipping a derived peptide nor bypassing normalization with `compute_all`
belongs in this assignment. AMP training preparation also calls `fasta_features`;
unchanged-sequence feature calculation cannot inherit native qualification merely
because the function exists. The provisional 20-symbol, <100-residue operational
scope does not establish every length's empirical applicability or invent termini,
stereochemistry or a complete molecular realization. M5 preserves those distinctions.

Both selectors rank proposal occurrences, using original occurrence order for final
ties: AMP descending then hemolysis ascending, or hemolysis ascending then AMP
descending. These are computational reference policies, not biological acceptance,
selectivity, safety or synthesis rules. No universal fitness or biological threshold
is adopted. The detailed contract and invented selector fixture in
[v0_1_increment_1.md](v0_1_increment_1.md) are authoritative; this brief does not
replace them with a new specification.

Not commissioned: HydrAMP implementation/execution, feedback optimization, target
recognition, structural generation, chemistry expansion, a universal plugin system,
new model training, releases, package publication or development issues now.
The minimum useful generative V0.1 still requires increment 2; completing this
assignment must not be announced as completing B or the whole V0.1.

## 2. Operational decisions still required

These resolve execution, not scientific intent. The following are proposed
defaults or qualification tasks, not adopted assets/environments.

| Item | Concrete preparation and decision boundary |
| --- | --- |
| **Exact Macrel bundle and access route** | Prefer a real installed distribution and native Python extraction/prediction with `keep_negatives=True`, packaged AMP/Hemo assets and retained native precision. Freeze version/build, artifact origin/digests and feature/model identity before recording reference results. No mixing assets from another release or switching to rounded CLI output silently. |
| **A real first environment** | Propose Linux CPU/Python 3.14 for the first installed-provider gate, consistent with suite routine development. Check actual dependency resolution, interpreter/import origin and ONNX execution there. No laboratory environment is presumed. If this route fails, report the blocker and a concrete alternative access/environment proposal; do not lower the main package's baseline or claim qualification from a different interpreter. |
| **Permitted use and fixtures** | Record applicable code/notices, weight, fixture and data terms for the intended use. Prefer installed upstream assets and a small permitted fixture rather than redistributing weights/training data. Investigators approve use-dependent commitments or unresolved restrictions. Codex can select permitted fixtures covering M1–M8 and both heads' positive/negative labels, recording origins before comparison. No new experimental efficacy is required. |
| **Execution bounds** | Before live runs, record maximum submitted records, input size, wall time, available memory/process controls and retry rule for the actual environment. Propose no automatic retries in initial qualification. Bounds are engineering limits, not biological cutoffs. Codex can propose measured values; investigators/maintainers authorize the host use and resource envelope before execution. |
| **Reference/parity evidence** | Obtain direct native reference results from the exact bundle and compare the adapter against them. Start with unchanged native values as M1 requires. If separate native calls vary, return measured differences and a tolerance proposal before declaring parity; do not silently weaken tests or alter labels/ties/selections. |

Bounded public-source check on 2026-10-27: the official
[Macrel release v1.6.1](https://github.com/BigDataBiology/macrel/releases/tag/v1.6.1)
exists. Its tag resolves to commit
[`19046260`](https://github.com/BigDataBiology/macrel/tree/190462605913844dca74b184869755609fbb20b2).
The tag's `AMP_features.py`, `AMP_predict.py` and `macrel_features.py` blobs match
the three paths inspected at `8c1f7321`. This supplies a concrete release candidate
for qualification, **not selection of its installer artifact, packaged weights,
license closure or successful execution**. A source tag is not evidence that a
particular PyPI/Conda artifact contains identical files. No package was downloaded
or installed to make this check.

## 3. Official admission and starter: ordered prerequisites

Reviewed central source:
[`uibcdf/molsyssuite@14b2e74c`](https://github.com/uibcdf/molsyssuite/tree/14b2e74c4395e112a47cdcd51259767e7af7589d).
Its `suite.toml` does **not** register PeptideMT. The registry names
`policy-v1.5.10`; the published tag resolves to commit
[`1c38d503`](https://github.com/uibcdf/molsyssuite/tree/1c38d50337ffd67e20eb02f5e02b24152073b3b4).
Recheck current central state when authorized; these are observations, not a
new admission SHA or adopted member workflow pin.

The official [starter guide](https://github.com/uibcdf/molsyssuite/blob/14b2e74c4395e112a47cdcd51259767e7af7589d/devguide/new_component_starter_kit.md)
and [generator](https://github.com/uibcdf/molsyssuite/blob/14b2e74c4395e112a47cdcd51259767e7af7589d/devtools/scripts/bootstrap_component.py)
require the following sequence:

1. **Authorize and submit the central admission proposal.** Describe purpose,
   accountable owner and boundaries with existing tools. Proposed classification:
   `name=peptidemt`, `repository=uibcdf/peptidemt`, `role=scientific-component`,
   `membership=primary`, `maturity=incubating`, `development-mode=active`,
   `capabilities=[python-package]`. These classification values are a recommendation
   for approval, not a registry entry. Identify the responsible owner explicitly.
2. **Publish accepted registration in central `suite.toml`.** Central reporting
   uses an owning issue/proposal; reuse an existing one where appropriate rather
   than invent an identifier. The investigators currently prohibit opening issues,
   so this step remains unperformed pending separate authorization. Scientific
   D35 approval does not itself confer central admission or waive that procedure.
3. **Generate against real immutable policy/admission evidence.** Fetch the
   selected published policy tag and accepted central history. If PeptideMT is
   absent from the frozen policy registry, use the supported `--admission-sha`
   route with the actual full published central admission commit, verified on
   central main ancestry. It imports registration/classification only, not policy
   exceptions or new engineering rules. Never fabricate a pin or move a tag.
4. **Stage the starter in an empty temporary destination.** It refuses a nonempty
   target; do not run it over this documentation repository or delete its design
   history. Generate with repository `uibcdf/peptidemt` and a concrete description,
   then review/merge the baseline into the existing repository. Preserve every
   scientific document, decision identifier, existing Git history and the explicit
   design/implementation agreement. Reconcile generated instructions and indexes;
   do not overwrite them blindly or claim the result is already qualified.
5. **Qualify the real baseline and adopted boundaries.** Retain official package
   metadata/src layout, import tests, routine Python 3.14 development, supported
   minors 3.11–3.14, Ruff, reporting/index tooling, policy workflows and synchronized
   guides/exclusions. Complete applicable support-library, developer-tool and
   optional-engine reviews; do not add unused providers or mark unexecuted adoption.
6. **Return exact-candidate governance and CI evidence.** Execute the starter's
   devguide-index check, native pytest/receptor tests, Ruff lint/format and central
   repository conformance. Confirm real routine/full matrix runs and applicable
   protection/workflow settings before admission/CI claims. Record unavailable
   administration or hosted gates instead of treating them as passed.

The [Python policy](https://github.com/uibcdf/molsyssuite/blob/14b2e74c4395e112a47cdcd51259767e7af7589d/devguide/python_policy.md)
requires `>=3.11,<3.15`; ordinary local development uses verified Python 3.14.
A generated member-specific environment is a bootstrap, not automatic membership
in the named shared development environment. No main-host Python 3.8 requirement
is introduced. A future isolated HydrAMP environment remains a separate task.

Central registration, generated source, passing source/installed tests and public
distribution are different milestones. No public release, Conda recipe/publication,
token grant, public channel claim, DOI or broad OS-support badge is required or
authorized merely to deliver this source-level increment. Follow those separate
contracts when a release is later commissioned. Preserve mandatory admission
gates now; do not substitute a smoke-only or all-skipped run.

## 4. Proposed implementation work packages after authorization

| Package | Concrete result and boundary |
| --- | --- |
| **W0 — admission/bootstrap** | Actual accepted central registration, staged official starter integration, preserved design history and applicable governance/environment receipts. Stop before scientific implementation if admission cannot be completed. |
| **W1 — engine-independent input/results/selection** | Occurrence-preserving sequence/FASTA handling, chemical/preprocessing compatibility checks, truthful results/provenance and both exact selectors. Core import and saved-result selection work without Macrel installed. No molecular realization or coordinates are synthesized. |
| **W2 — one real Macrel route** | Lazy, selected optional provider boundary; native features and both classifiers; negatives/precision preserved; reconciled inputs/outputs and diagnostic/failure behavior. No duplicated feature formulas, secondary engine or silent fallback. |
| **W3 — installed qualification** | Exact permitted bundle/environment/fixture run, direct native parity and M1–M8 evidence with limits/applicability distinguished. Return blockers rather than declare completion from mocks. |
| **W4 — reviewable delivery** | Tests, small usage documentation and a reproducible assessment/selection example, source commit and evidence manifest. No model binaries/training corpus in the repository by default; no release or increment-2 claim. |

Codex can choose internal classes, names/signatures, module layout within the
starter, run-local row tokens, serialization, batching and test mechanics. Document
the resulting small public boundary. Technical discretion does not authorize a
new scientific policy or chemistry/representation equivalence. Researcher review
is required for changed scope/attribution, a different scientific provider/role,
new use commitments, altered selectors/eligibility, unresolved applicability that
changes the accepted task, or relaxed parity criteria. Routine candidate package/
dependency resolution can be investigated within the authorized budget, with all
actual choices recorded; final acceptance names the qualified bundle.

PeptideMT owns design attribution and selection; Macrel owns its native feature/
prediction operations. MolSysMT owns actual molecular operations if needed, but
this increment does not force coordinate building. Apply SMonitor/DepDigest to
the real optional boundary and ArgDigest where contracts require it; PyUnitWizard
does not calibrate unitless scores. Reuse audited Praxis/Recorda boundaries only
where actually used, without adding a MOLI orchestration prerequisite.

## 5. Test allocation: ordinary CI versus real provider

| Lane | Required scope; what it cannot establish |
| --- | --- |
| **Engine-free routine/compatibility CI** | Core import without Macrel; input/chemistry/leading-M/length guards; duplicate occurrence mapping; controlled missing/extra/reordered rows; output/precision/serialization validation; invented selector fixture, k/ties/empty results and saved-result replay; controlled absence/load/failure/timeout behavior. Covers engine-independent parts of M3–M8. Uses small permitted/generated text fixtures, no weights, downloads or model execution. Cannot establish native parity or scientific provider readiness. |
| **Designated installed-Macrel lane/environment** | Actual M1/M2; native sides of M3/M4/M6; direct boundary/very-short probes in M5; a real evaluation-to-selection case and relevant failures in M8. Both ONNX heads actually execute. Check package/asset/import provenance from a neutral working directory and distinguish the installed provider from a shadowing source checkout. Missing, broken, shadowed or unexecuted provider fails this lane; it cannot pass through broad skips. |
| **Admission/host-package verification** | Official routine and required full Python 3.11–3.14 gates, plus installed PeptideMT import/results boundary where applicable. Core compatibility without Macrel does not claim live Macrel support on every minor/platform. Initially qualify and document the particular installed-Macrel environment; broader provider support needs its own evidence. |

M3/M4/M6/M8 are split obligations, not reassigned as mock-only tests. A live
qualification lane may be a controlled separately provisioned environment with
retained receipts rather than an uncontrolled model download on every push.
Ordinary optional skips retain their reasons; they never clear W3. The accepted
suite CI schedule/admission gates remain applicable; no new universal CI engine
or unqualified Python-support claim is introduced.

## 6. Evidence Codex must return and stop conditions

Return a compact evidence record linking:

- The delivered source commit, changed-file scope and preserved scientific
  contract/decision revisions; central admission and immutable policy identities.
- Exact host/provider environment, installed distribution/import locations, both
  asset digests/origins, relevant terms/notices, fixture sources and actual bounds.
- M1–M8 pass/fail/not-executed matrix with real versus controlled evidence clearly
  marked; original native and adapter outputs/comparison, not only a test count.
- Both class outcomes for each head, all requested input occurrences accounted
  for, leading-M/chemical incompatibilities, length observations versus applicability,
  original precision and replay of both policies from unchanged evaluations.
- Actual core/installed/host-CI results, exact tested commits/artifacts, timing,
  failures/skips and their scope; no credentials or unsupported hardware claims.
- A reproducible small assessment/selection example, known limitations and
  remaining support gaps. Raw model binaries are not required as evidence files.

Investigators can accept increment 1 only when the applicable admission/operational
gates and approved M1–M8 have supporting evidence. If the provider cannot execute,
the software must report that failure correctly, but **the real integration is not
thereby complete**. Stop/return for review on incompatible terms, unresolvable
input/output identity, model/precision discrepancies, needed scientific scope changes
or lack of usable real-provider evidence. Do not weaken a gate or substitute a
mock to manufacture completion. No biological efficacy/safety claim follows.

## 7. Next authorization, not another design round

The next decision is whether to commission W0 and the bounded Macrel operational
qualification/implementation W1–W4, with an approved owner, environment/use/budget
and central issue/admission route. It need not select HydrAMP assets or authorize
H0–H4 execution. The scientific contract is already closed; package/asset findings
return to science only if they expose a material limitation of that agreed scope.

This brief is ready for explicit authorization. At present W0–W4 are **not
started**, PeptideMT remains unregistered, and no scientific model or executable
implementation has been produced by this readiness review.
