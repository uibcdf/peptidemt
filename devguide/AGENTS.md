# peptidemt developer-guide instructions

Read `../AGENTS.md` for repository-wide rules and `reporting_protocol.md` for
the local issue and report lifecycle. Active issue-backed analyses live in
`pending_bugs/` and `pending_proposals/`; `archive/` preserves resolved and
superseded history. Use the generated indexes to find current work. Read an
archived report when tracing a decision, then check the current replacement
before treating it as a rule.

Keep technical facts and defect details in maintained documents, tests and
owning issues. Put only lasting working instructions specific to this
directory here, and repository-wide working instructions in the root
`AGENTS.md`. Follow the local reporting protocol to synchronize issues and
report states. After a report lifecycle change, run
`python devtools/devguide_index.py` to regenerate indexes, then run it with
`--check` to verify them.

Follow [the canonical instruction policy](../MOLSYSSUITE_GUIDE.md#durable-working-instructions)
for accepted lasting actions and feedback beyond this component.

## PeptideMT scientific working agreement

Read `../AGENTS.md` and `README.md` first. Keep this guide small and navigable.
Scientific details belong in the topical documents, not in working instructions.

Use the status vocabulary in `decisions.md`. Preserve rejected or superseded
reasoning with a dated disposition when it matters; do not silently rewrite a
proposal as a past agreement. Link verified code observations to exact revisions
and distinguish source inspection, implementation execution, installed-package
qualification and scientific validation.

Apply the canonical owning-issue reporting duty to actionable bugs, limitations
and improvements in PeptideMT or any provider. The investigator's governance
clarification supersedes the former W0-only issue restriction for reporting,
without expanding scientific implementation or publication authority. W0 history
remains in uibcdf/molsyssuite#146 and uibcdf/peptidemt#1. Read `governance.md`
for the operational map. Central issue-backed proposal queues and the official
starter's reporting machinery follow the real admission route;
the topical scientific documents are not counterfeit issue-backed lifecycle records.

Keep scientific review summaries separate from imported code or data. Cite
primary research and official implementations; record unavailable evidence.
