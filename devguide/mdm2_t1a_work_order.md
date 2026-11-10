# MDM2 T1a work order

Status: **completed within the investigator-approved data-only scope**, 2026-11-09
(D53). Owner: [PeptideMT #33](https://github.com/uibcdf/peptidemt/issues/33).
Authority: [approval receipt](evidence/mdm2_t1a_authorization.json).
Outcome: [actual qualification](mdm2_t1a_qualification.md), with artificial
controls, one actual source receiving, source cross-check and fresh saved replay.
This is technical completion of D53, not new scientific bundle acceptance.

The investigator approves the [original T1a contract](mdm2_t1a_proposal.md),
SHA-256 `069247bf4b46e8fafba553ecb5311f67b0bfd6748ea4a06822053c3285c05e56`,
after the concrete implementation-scope question. Its original proposed status
is retained as the reviewed historical input; D53 is the current disposition.
The exact approved bytes are preserved separately by the approval receipt.
The earlier review holds are superseded for this data-only scope.

Implement faithful receiving of the fixed Li et al. (2010) HTML, all source
occurrences, the explicit repeated WT display, separate reported Kd/SD quantities,
unquantified outcomes and source chemical/assay limitations. Use PyUnitWizard's
supported quantity/measurement records; retain source precision and locators.
This is a private case-specific developer artifact, not a public API or generic
evidence framework. Source-table transcription is not molecular parsing, chemical
identity or sequence normalization. General molecular operations remain MolSysMT's.

Qualify the meaningful artificial failure controls and saved-data replay required
by the approved contract. Receive the actual source once after those guards pass;
preserve every failed attempt and diagnose it before a retry. The actual counts
must follow the source, not a weakened expected total. Report the resulting
reference and its suitability/remaining limits for the next evaluation domain.

Use serial jobs on CPUs 0/1, one numerical thread, a 512 MiB sampled aggregate
task-RSS stop and at least 4 GiB available host RAM. Each job keeps 180 s wall,
120 s CPU, 8 GiB address space and 64 MiB output limits. D49 delegates bounded
technical execution and diagnosed retries. No model/molecular calls or GPU.
No docking, chemical preparation/repair, new evaluator, sequence proposals,
training/feedback, public API, Git/package/dataset publication or author contact.
The full target-directed demonstrator remains incomplete after T1a.
