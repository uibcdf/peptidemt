# PeptideMT development governance

Read this map and root `AGENTS.md` before starting work. The root
[MOLSYSSUITE_GUIDE.md](../MOLSYSSUITE_GUIDE.md) is the synchronized operational
summary; its linked central policies and registered inventories are authoritative.
This local map applies them to PeptideMT. It does not freeze another policy copy,
replace the full guide or make every optional capability a dependency.

## Everyday contributor actions

| Topic | Required action and authority |
| --- | --- |
| Development environment | Use `molsyssuite@uibcdf_3.14` on Linux. Install participating clones with `python -m pip install --no-deps --editable PATH`; use declared native tools and `--no-build-isolation` when needed. Verify Python, dependency findings and neutral editable origins. Member Conda YAMLs remain CI/clean-qualification fixtures. |
| Local tests | Use `python -m pytest --receptor=llm`; CI uses `--receptor=ci`. Read [Pytest Receptor's registered guide](../PYTEST_RECEPTOR_GUIDE.md). Preserve pytest assertions, selection, exit status and required gates. |
| Actions inspection | First use the published GH Run Receptor under [its guide](../GH_RUN_RECEPTOR_GUIDE.md). Inspect authoritative GitHub run/job/step evidence when incomplete or before exact-candidate acceptance/publication. Identify any explicitly reviewed experimental tool pin honestly. |
| Internal contribution | Work by or directly supervised by Diego (`dprada`) or Liliana (`LMMV`) uses the authorized commit/direct-push route within its granted scope; retain authorization across commits. No new blanket write authority is inferred for other contributors/repositories. |
| Other contributors and PRs | Use an owner-reviewed PR and execute the complete required suite before integration. Internal maintainers choosing a PR follow its same gates. |
| Local checks and checkpoints | Select checks by affected code/inputs/scope and retain still-applicable results. Follow [the common CI route](../MOLSYSSUITE_GUIDE.md#direct-pushes-and-validation-checkpoints); ordinary direct pushes need no full scientific suite every step. Finish with an inspected unskipped head or exact manually verified gates. Skip/deferred debt needs the existing recovery route and owner; it is never automatically cleared by administrative checks. |
| Findings anywhere in the ecosystem | Open or update the owning issue with observation, reproduction/context, impact and uncertainty; cross-link the consumer and workaround/removal condition. A defect in a provider belongs there. Shared decisions belong to MolSysSuite; cross-MOLI contracts belong to MOLI. Reporting does not promise implementation. |
| Human/private feedback | Surface uncertain or nonblocking actionable findings. Use existing reporting authorization, respect declined/deferred disclosure and report confidential/exploitable findings privately. The earlier W0-only issue restriction does not block normal feedback. |
| Durable records | Follow [the local protocol](reporting_protocol.md): owning issue first, queued record when durable analysis is needed, synchronized indexes, meaningful guard or normative resolution and permanent archive. Put technical findings in issues/tests/maintained guidance; only lasting contributor actions belong in instructions. |
| Cross-repository changes | Run the central suite-status tool before coordinated work; preserve dirty/human work. Report provider needs first; ready fixes use owner-reviewed PRs unless the relevant principal-maintainer direct route is explicitly authorized. Do not silently fork a missing capability. |
| Shared-provider changes | Before a shared change with plausible consumer impact, update its impact issue, identify consumers from registered inventories and hand off immutable versions/commits, migration, evidence, limits and owners. Notice, source adoption and tested/public artifacts are separate. |
| Python, lint and platforms | Follow the pinned policy and actual compatibility matrix: routine Python 3.14, required 3.11–3.14 compatibility, declared Ruff gates. Claim only executed support; macOS targets arm64, Windows is optional. W0's Linux checks make no public OS/GUI/model claim. |
| Release identities | Public tag, package/project version and GitHub Release title are exactly `X.Y.Z`: no project name, comment, `v` prefix or public prerelease tag. Descriptions belong in notes. Stable `archive/<description>` tags retain experiments without being releases; do not move published identities. Read [release guidance](release_titles.md). |
| Publication | A future commissioned release needs its exact-source/installed gates, declared dependency closure, applicable platform/Python evidence and immutable artifacts. Use the shared noarch route when the payload qualifies, or a reviewed equivalent/exception. Do not infer publication authority from W0 or publish without evidence. |
| Release notices | Every component release, even source-only, and every new package version/build/route needs a release-specific MolSysSuite issue with actual availability, identities, digests/evidence and ecosystem follow-up. |
| Resources, badges and exceptions | Keep task-owned temporary resources only while useful and clean them at closeout, preserving human/shared resources. Badges state actual evidence. Deviations need owning issues, reasons, owners, interim controls, review/expiry and removal conditions; configuration/copies alone prove no execution. |

## Domain owners and reuse

Before implementing a capability, inspect the
[central roster](https://github.com/uibcdf/molsyssuite#registered-molsyssuite-components),
`suite.toml`, the owner's supported APIs and applicable registered guides.
Registration is not a stability or implemented-capability claim.

| Need encountered in PeptideMT | Owner and PeptideMT responsibility |
| --- | --- |
| Molecular-system representation, manipulation, conversion/interoperability or general molecular analysis | [MolSysMT](https://github.com/uibcdf/molsysmt). PeptideMT owns its peptide-specific question and consumes or proposes the general operation there. |
| Molecular visualization | [MolSysViewer](https://github.com/uibcdf/molsysviewer). PeptideMT selects what to display and interprets it; reusable rendering/interaction belongs to the viewer. |
| Cavities, pockets and molecular topography | [TopoMT](https://github.com/uibcdf/topomt). PeptideMT defines its use case and selection/interpretation; TopoMT owns the reusable boundary. Do not bypass that owner merely because it is incubating or a backend is missing. |
| Pharmacophores, elastic networks or docking | [PharmacophoreMT](https://github.com/uibcdf/pharmacophoremt), [ElastNetMT](https://github.com/uibcdf/elastnetmt) or [DockingMT](https://github.com/uibcdf/dockingmt), respectively. Report the needed reusable operation to its owner. |
| Public input validation, optional dependencies, diagnostics or physical quantities | ArgDigest, DepDigest, SMonitor and PyUnitWizard, respectively, where the actual boundary exists. Review their published contracts and guides before requiring features. No unused dependency is required for the empty W0 package. |
| Optional scientific attribution | Ackredit's optional published contract and application-owned sessions, preserving original provider/output provenance. Reporting/citation does not establish scientific validity or licensing permission. |
| Peptide-specific design and evaluation | PeptideMT owns design intent, scientific requirements, occurrence mappings, evaluation/selection policy, composition and interpretation under its approved scientific work order. Keep general reusable molecular operations in their owners. |

A missing owner capability starts an owning issue with consumer evidence. The
provider decides priority and supported implementation; a linked PR or an
already authorized direct contribution can propose a fix. Temporary local
workarounds need linked issues, reason, owner, review/expiry and removal condition.
Do not make all these owners eager runtime dependencies in anticipation of work.

Before introducing an optional engine, use [the local review](optional_engine_review.md)
and the canonical optional-engine contract: truthful absence versus failure,
lazy loading, explicit provider/access route, original outputs and actual installed
qualification. Physical quantities retain units and scientific meaning across
serialization and component boundaries; use PyUnitWizard's negotiated codec and
explicit boundary units with non-default-policy regressions where applicable.
Keep the distinct responsibilities of the direct MOLI components, including
Praxis, Recorda and Sabueso, under their own platform contracts.

## Current evidence and limits

[W0 engineering receiving](archive/complete_w0.md) records the official starter,
genuine immutable policy/admission, baseline source/installed checks and fresh
fifteen-member shared integration. Tool/guide delivery, active instruction review,
runtime adoption, scientific tests and public artifacts are different claims.

The investigator's governance clarification supersedes only the historical
W0-only reporting restriction. D35/D36, M1–M8, scientific acceptance and publication
authority remain unchanged. No source-only engineering check qualifies Macrel
or another scientific model. This local map must be updated with the owning
change when an applicable boundary or accepted working instruction changes.
