# MDM2 T1a proposal: source-scoped reported-affinity evidence

Status: **proposal for investigator review; not an implementation commission**,
2026-11-06. Owner: [PeptideMT #33](https://github.com/uibcdf/peptidemt/issues/33).
Context: [D52 objective](target_directed_demonstrator.md) and
[primary-source/provider review](target_directed_evidence_review.md).

## Scientific question and purpose

Can we reconstruct an auditable, internally coherent reference of the selected
article's **reported MDM2 affinities**, while retaining the information that
prevents its use as an unquestioned chemical/model benchmark?

Propose Li et al. (2010), DOI [10.1016/j.jmb.2010.03.005](https://pmc.ncbi.nlm.nih.gov/articles/PMC2856455/),
Tables 1 and 3 plus their notes/methods, as the finite first source. All expected
counts and assay/construct observations are in the linked review. T1a accepts
source-reported experimental evidence, not complete chemical identity, binding
prediction, target-aware generation or an activity/safety classification.

This is the evidence-admission step of T1, not the whole target-directed
demonstrator. The outcome should enable a justified evaluator decision or reject
this panel for that domain. It must not become a permanently smaller substitute
for the original design/selection objective.

## Proposed inputs and ownership

- Preserve the acquired source bytes, retrieval metadata, bibliographic identity,
  table/row/column locators and terms observation. No complete article or dataset
  is published as part of this local commission. A blocked source is recorded;
  no access control is bypassed.
- Curate a case-specific source table with literal reported peptide labels and
  sequence text, source order, series, target/construct, experimental method,
  conditions, raw measurement/uncertainty/unit strings and notes. Source strings
  remain uninterpreted evidence until a molecular view is approved.
- PeptideMT owns the study's evidence requirements, eligibility decisions,
  source-to-result correspondence and interpretation. Existing quantity handling
  uses PyUnitWizard; generic recording/attribution retains its supported owner
  route if actually consumed. This proposal adds no generic evidence framework.
- Molecular parsing, construction, chemical identity, capping, matching and
  sequence alignment remain MolSysMT operations. T1a does not need to execute
  them: no source chemical state or molecular model is admitted by this contract.

## Proposed outputs and invariants

Produce one private development artifact/report, not a new public API:

1. **Source-occurrence ledger.** Retain every displayed peptide row and both
   target measurement occurrences, including the repeated display. A stable
   source locator is a row identity, not a molecular grouping key.
2. **Reported-evidence view.** Link the explicit WT/self-substitution repeat to
   the same source-reported evidence without counting it as another independent
   experiment. Keep all original occurrences and the curation reason. Other
   apparent aliases/contradictions remain unresolved until justified.
3. **Quantity records.** Preserve raw values and the reported unit; represent
   finite reported Kd and SD separately with explicit molar concentration units.
   Validate positive Kd, nonnegative SD and target correspondence. SD does not
   become a standard error/CI; an unspecified replicate count remains unspecified
   alongside the source's lower-bound statement. No thermodynamic conversion,
   pKd, cutoff, label or pooled cross-method endpoint is introduced.
4. **Unavailable measurements.** Retain the source token and reason for a value
   that could not be determined. Do not assign zero, infinity, a guessed threshold,
   an exact censoring interval, a class or an excluded-row deletion.
5. **Chemical/source limits.** Record unestablished terminal chemistry, stereo,
   modifications and construct/coordinate relationships explicitly. These are
   reported-entity identifiers scoped to this source, not certified chemical
   identities or proven independently novel molecules.
6. **Audit/disposition.** Reconcile the finite source counts in the review;
   document the caption discrepancy, aliases, unavailable values, conflicts,
   prior result exposure and eligibility for later evaluation. Retain MDMX as
   separately attributed context; no co-target/off-target policy is inferred.

The expected reconciliation is a hypothesis to verify against acquired bytes,
not a passing test already executed. If the source differs, preserve it and
investigate before editing counts or criteria. No row is removed merely to
match an expected total.

## Failure behavior and acceptance evidence

Malformed numeric units, mismatched targets, contradictory source locators or
lost occurrences fail receiving. Missing chemistry does not fail faithful
reported-data retention; it blocks any stronger chemical/model admission.
Unknowns cannot pass as known simply because two fields are both absent.

Acceptance would require:

- Traceable extraction/cross-check against the exact local source, with every
  retained occurrence accounted for and source inconsistencies explained.
- Artificial controls for the scientifically meaningful failure mechanisms:
  duplicate-display inflation, target swap, unavailable-to-number coercion,
  unknown-chemistry promotion, incompatible units and omitted source rows.
- A saved-data replay that preserves raw values, explicit units, original
  provenance and unavailable/alias dispositions without loading molecular or
  learned providers. Any live owner integration has its own actual evidence.
- A final report answering whether this source can support the next declared
  evaluation domain, with remaining source/provider needs. Passing curation is
  not a prediction, independent benchmark, chemical validation or biological pass.

## Operational proposal and subsequent decision

After scientific agreement, use standing routine-execution authority for serial
data/engineering checks: CPUs 0/1, one numerical thread, no GPU/weights, a proposed
512 MiB aggregate task-RSS stop, at least 4 GiB available host RAM, 180 s wall,
120 s CPU, 8 GiB address space and 64 MiB output per job. Inspect RAM/load/disk
before substantial work; use existing supervision and preserve failed attempts.
This new proposed envelope does not reassign an old consumed allowance or alter
the other HydrAMP/T0 profiles. No new model evaluations are requested.

The next review after T1a must name the actual evaluation and proposal method,
its domain and provider, reference/baseline comparison and success/refutation
criteria. Docking, new models, chemical preparation/repair, sequence proposals,
training, feedback and experimental work are not commissioned by T1a. The
longer-horizon objective remains active until its full evidence is achieved.

[D14](design_methodology.md#progression-and-review) requires agreement on scientific
meaning, ownership, input/output obligations, failures and acceptance before
implementation. The investigator's D52 objective authorizes preparing this
proposal; the proposal does not record its own acceptance.
