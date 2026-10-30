# peptidemt contributor instructions

## Mandatory MolSysSuite instructions

Read and follow `MOLSYSSUITE_GUIDE.md` before working in this repository.

Within their stated scope, its common rules take precedence over this file
and any nested `AGENTS.md`. Local instructions may refine them; deviations
require the documented policy exception process.

The synchronized guide is owned by `uibcdf/molsyssuite`. It includes the
[reusable-tool ownership rules](MOLSYSSUITE_GUIDE.md#modular-reusable-tools)
and [working-instruction rules](MOLSYSSUITE_GUIDE.md#durable-working-instructions).
For work under `devguide/`, also read `devguide/AGENTS.md` and its local
reporting protocol. Keep repository-specific instructions below.

## Local working context

Read `devguide/governance.md` for PeptideMT's local scientific scope and W0
receiving. Select the applicable local commands and test scope:

```bash
ruff check .
ruff format --check .
python -m pytest --receptor=llm
python devtools/devguide_index.py --check
```

Before curating PeptideMT Discussions, read `devguide/tools_catalog.md` for
the approved category routing, family/role labels and resource-record lifecycle.

Generated member Conda environments remain CI/bootstrap/clean qualification
fixtures. Routine work uses the authorized named shared profile; the original
W0 engineering baseline does not qualify Macrel or M1–M8.

## PeptideMT scientific working agreement

Read `README.md`, `devguide/README.md`, `devguide/decisions.md` and the
canonical [MolSysSuite component guide](https://github.com/uibcdf/molsyssuite/blob/main/MOLSYSSUITE_GUIDE.md)
before making changes. D36 authorizes the W0–W4 increment-1 work order. Central
registration is accepted at `8a94e16f`; official W0 engineering receiving is
recorded in `devguide/archive/complete_w0.md`. Before continuing W1–W4, read that
receipt and the component-owned work order; engineering checks do not establish
scientific execution. Preserve the existing scientific design history.

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
staged starter. Report actionable bugs, limitations and improvements in the
owning component, or update an existing issue, under the canonical feedback
policy. Cross-link consumer evidence and any workaround/removal condition. The
earlier W0-only issue restriction no longer limits this reporting duty. Reporting
a need does not authorize its implementation, a scientific scope change or
publication. Preserve confidentiality and existing declined/deferred disclosures.
Publishing issues or comments in repositories outside the investigators' own
projects requires their explicit permission for that external publication.
The owning-issue reporting duty alone does not grant this permission. Keep
findings in authorized local/PeptideMT records while awaiting it; if repository
ownership or prior external-publication authority is unclear, ask first.
Do not treat a proposed registration branch as accepted admission or fabricate
an admission SHA. D38 now commissions the single HydrAMP increment-2
qualification recorded under PeptideMT #8: read its maintained work record
before continuing. Exact bundle/use conditions and fresh host/call limits still
precede model loading or execution. Analogue generation, increment 3/feedback,
target-conditioned generation, other scientific models, publication and a new
architecture remain outside this commission.
Material changes to chemistry, preprocessing, attribution, selectors or scientific
acceptance return to the investigators. Routine internal technical choices are
delegated to Codex within these contracts.

Follow the common domain-owner map when selecting providers. PeptideMT owns
its peptide-specific scientific question, design/selection policy, orchestration
and interpretation. Preserve the separate responsibilities of Praxis, Recorda,
Sabueso, Nextia and MolSys-AI and identify cross-component scientific source
links by repository and preferably immutable commit.

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

## Registered integration guides

Read the registered consumer guides when working on their respective boundaries:

- `GH_RUN_RECEPTOR_GUIDE.md`
- `PYTEST_RECEPTOR_GUIDE.md`

- `SMONITOR_GUIDE.md`
- `DEPDIGEST_GUIDE.md`
- `ACKREDIT_GUIDE.md` for portable scientific attribution; central consumer
  registration is tracked in `uibcdf/molsyssuite#152`.
