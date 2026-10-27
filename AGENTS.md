# peptidemt contributor instructions

Read `MOLSYSSUITE_GUIDE.md` before making changes. It routes suite-wide policy,
compatibility, tooling and cross-component proposals to `uibcdf/molsyssuite` while this
repository remains authoritative for its implementation and product behavior.

Use English in code, documentation, issues and commits. Keep changes focused, test
user-visible behavior, preserve human work and never commit secrets.

Routine development and pytest use Python 3.14 in a compatible Conda environment.
Install the local clone with `python -m pip install --no-deps --editable .` after
Conda supplies dependencies; verify interpreter, dependency closure and import
origins. Use the suite's named Linux development profile when this member is
eligible; otherwise track the missing integration as the canonical guide directs.
Native builds may need declared in-environment tools and `--no-build-isolation`.

Choose local gates before committing from the changed code, inputs and scope:

- For documentation, instructions or evidence, run applicable reporting/index,
  link and synchronized-guide checks. Run `python devtools/devguide_index.py
  --check` for developer-guide changes; do not require scientific pytest merely
  because prose changed.
- For executable behavior, dependencies, metadata, packaging or integration,
  run relevant code/contract tests and applicable Ruff checks. Broaden to the
  full suite when the affected boundary, PR, admission or release requires it.
- For scientific exploration, run informative hypothesis cases and record
  their limits; do not infer broader equivalence from an administrative CI run.

Available commands (select the applicable checks and test scope):

```bash
ruff check .
ruff format --check .
python -m pytest --receptor=llm
python devtools/devguide_index.py --check
```

Retain completed local results while tested code, inputs, environment and scope
remain applicable; rerun or broaden when changes or failures invalidate them.
Follow [the common checkpoint route](MOLSYSSUITE_GUIDE.md#direct-pushes-and-validation-checkpoints)
for conditional internal batching/skips, exact-head CI verification and visible
recovery debt. Full PR and release gates remain mandatory.

Follow `devguide/reporting_protocol.md` for every durable bug or proposal record. Open
the owning GitHub issue first, regenerate indexes after lifecycle changes, and archive
resolved records instead of deleting them.

Before publishing or rolling out a shared provider change with plausible consumer
impact, follow
[the shared-provider notice rule](MOLSYSSUITE_GUIDE.md#shared-stewardship-across-components):
update the impact issue, identify consumers from registered inventories and send an
actionable handoff to their owning issues. Keep notice, adoption and tested artifact
evidence separate.

For a fix in another owner's repository, follow the canonical guide's
cross-repository contribution route: issue for a need, owner-reviewed PR for a
proposed fix, or an explicitly authorized route for urgent work by or directly
with Diego or Liliana. Existing authorization remains valid within its scope.

Report defects and needs in their owning issues; put source behavior, edge
cases and workarounds in code, regression tests and technical documentation,
not in `AGENTS.md`. Only when normal repository review accepts a lasting rule
about how contributors or agents should work across future tasks, place a
repository-wide working instruction here or a directory-specific one in the
appropriate nested `AGENTS.md`. Open an adoption issue only if that accepted
instruction cannot be placed with the fix or decision. Do not ask for a
separate `AGENTS.md` decision for every defect. Propose a shared member
working instruction to `uibcdf/molsyssuite` only with evidence beyond this
repository; raise a cross-MOLI contract in `uibcdf/moli`. For work under
`devguide/`, also read `devguide/AGENTS.md`.

Before adding a required MolSysSuite sibling to `project.dependencies`, consult
`uibcdf/molsyssuite/devguide/ci_dependency_resolution.md` and replace the generated
pip-only CI lane with a verified dependency acquisition route.

## Public release titles

When preparing, publishing or intentionally editing a public GitHub Release, use
exactly `X.Y.Z` as its title/name, matching the canonical tag and package/project
version. Put descriptions in the body/notes. Read
[the local release-title guide](devguide/release_titles.md) and
[the canonical rule](MOLSYSSUITE_GUIDE.md#github-release-titles).

## Release and package-publication notices

For every new component release, with or without a published package, and every
new package version/build/distribution route, open or update a release-specific
issue in `uibcdf/molsyssuite` as part of closeout. Include exact version/tag/source,
actual package availability and verification evidence, and ecosystem follow-up.
Follow [the notice policy](MOLSYSSUITE_GUIDE.md#release-and-package-publication-notices).

## Modular reusable tools

Before adding a feature, inspect existing tools and identify the owning module or
component. Implement or extend independently useful operations as documented reusable
tools in that owner, with their own contracts and tests; have consumers call them.
Keep task-specific decisions local and report missing sibling capabilities to the
provider with linked consumer evidence. Follow
[MOLSYSSUITE_GUIDE.md#modular-reusable-tools](MOLSYSSUITE_GUIDE.md#modular-reusable-tools)
for applicability, compatibility, performance and tracked exceptions.

## Temporary development resources

Follow [the common resource policy](MOLSYSSUITE_GUIDE.md#temporary-development-resources).
Keep ownership clear, retain temporary resources and evidence while needed,
and remove them when their usefulness ends. Review retention at task/release
closeout; preserve active/human work and report cleanup failures.

## Durable working instructions

Follow [the canonical instruction policy](MOLSYSSUITE_GUIDE.md#durable-working-instructions)
when placing accepted lasting contributor actions. Keep technical findings in
owning issues, tests and maintained guidance. For work in `devguide/`, read
[devguide/AGENTS.md](devguide/AGENTS.md) and its local reporting protocol.

## Human-facing issue feedback

Surface actionable suspected defects, inconsistencies, missing analyses and
improvements, including uncertain or nonblocking findings. When working with a
human, offer an owning issue at a natural pause; retain existing reporting
authorization and respect declined/deferred disclosure. Follow
[the accepted feedback route](MOLSYSSUITE_GUIDE.md#human-facing-issue-feedback)
for ownership, uncertainty, privacy and exceptions.

## PeptideMT scientific working agreement

Read `README.md`, `devguide/README.md`, `devguide/decisions.md` and the
canonical [MolSysSuite component guide](https://github.com/uibcdf/molsyssuite/blob/main/MOLSYSSUITE_GUIDE.md)
before making changes. D36 authorizes the W0–W4 increment-1 work order. Central
registration is accepted at `8a94e16f`; W0 component bootstrap and qualification
are in progress. W1–W4 remain gated on actual W0 receiving. Preserve the existing
scientific design history.

Use English for maintained documentation and commits. Keep changes focused,
preserve human work and do not publish secrets, private attachments or raw
conversation transcripts.

The user has authorized maintaining `devguide/` as the design source of truth
when important scientific or architectural matters are discussed. Update related
documents consistently and preserve the reasoning and sources behind changes.
Do not convert an assistant recommendation, hypothetical API or research
hypothesis into an accepted decision without explicit investigator approval.
A provisional definition remains provisional.
Follow the investigator-approved responsibilities and implementation-readiness
agreement in `devguide/design_methodology.md`; major design changes return to discussion.

Follow D35, M1–M8 and the authorized W0–W4 work order. W1 begins only after W0
completes through accepted published central registration and the official
staged starter. Issue authority is limited to the central admission theme
`uibcdf/molsyssuite#146` and the explicitly authorized local W0 evidence issue
`uibcdf/peptidemt#1`; do not create other development issues without approval.
Do not treat a proposed registration branch as accepted admission or fabricate
an admission SHA. HydrAMP, increments 2/3, target-conditioned generation, other
scientific models, package publication and a new architecture are not authorized.
Material changes to chemistry, preprocessing, attribution, selectors or scientific
acceptance return to the investigators. Routine internal technical choices are
delegated to Codex within these contracts.

Check existing owner APIs before proposing new functionality. Reuse MolSysSuite
molecular operations; preserve the separate responsibilities of Praxis, Recorda,
Sabueso, Nextia and MolSys-AI. Cross-component source links must identify a
repository and preferably an immutable commit.

For documentation changes, check relative links, navigation, status consistency,
citations and whitespace. Do not claim scientific tests or CI qualification from
a documentation check. The official reporting checker and baseline package tests
are present; they do not qualify Macrel or execute the scientific M1–M8 gates.

Before scientific implementation, complete official W0 receiving. The integrated
starter supplies policy workflows, package metadata, development environments and
guide synchronization; retain its real gates and applicable release controls. Do not fabricate policy pins, admission commits, badges or support
claims. This initial repository publication is not a versioned software release.

For work in `devguide/`, also read `devguide/AGENTS.md`.

Use the published GH Run Receptor for the first inspection of Actions, then
verify required native job/step conclusions. Record both surfaces in the W0
evidence issue. Never infer scientific execution from the baseline CI.
