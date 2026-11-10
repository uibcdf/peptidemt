# MDM2 T1b proposal: molecular admission before evaluator qualification

Status: **proposal for scientific review; implementation not commissioned**,
2026-11-10. Owner: [PeptideMT #33](https://github.com/uibcdf/peptidemt/issues/33).
Authority for this preparation: [D52](target_directed_demonstrator.md).
The completed [D53 T1a reference](mdm2_t1a_qualification.md) is preserved.
Investigator clarification, 2026-11-10: discuss and explore protein–peptide
docking and binder-design alternatives before starting that work. The
[broader comparative survey](peptide_protein_binding_survey_2026_11_10.md)
now informs the next decision. This proposal is a possible molecular-admission
subproblem, not a selected mandatory next stage or an adopted HADDOCK3 route.
Read-only source/provider observations are recorded in
[the preparation receipt](evidence/mdm2_t1b_preparation.json).

## Recommended next question

Can a documented molecular representation be associated with the historical
experimental entities, and does a suitable structural reference support a
defensible subsequent peptide-evaluator protocol?

Recommend **one bounded molecular-admission stage first**, followed by a
separately specified owner peptide-pose pilot and then an affinity/selection
comparison. These stages answer different questions. Another successful file
conversion or pose comparison alone would not complete the original D52
independently evaluated design/selection objective.

Do not start an affinity benchmark by assigning plausible chemistry to unknown
experimental entities. A declared computational hypothesis can be useful, but
its relationship to the experimental molecule must remain an explicit question.

## Evidence that changes the next step

The unchanged saved T1a artifact is SHA-256
`b9af350ef8a39febcb807c18c7d56d8a11391c2c6284ab689ac9d3293007cea6`.
An inspection of its existing source-row fields, without sequence parsing or
molecular operations, gives this candidate study population:

| Source block, MDM2 only | Source-scoped entities | Quantified | Unquantified |
| --- | ---: | ---: | ---: |
| Table 1 full-length block, explicit WT repeat linked | 12 | 12 | 0 |
| Table 3 full-length block | 13 | 11 | 2 |

These are reported full-length source blocks, not chemically admitted cohorts.
Their locators are HTML rows 3–15, with Table 1 row 7 linked to row 3. Ten
reported truncation entities, all MDMX evidence and every original occurrence
remain in the reference. Restricting an initial comparison to one length/series
would reduce length and parent-series confounding; it does not establish
independence or justify discarding other records. The proposed first quantitative
pilot would use the Table 1 series **only after chemistry admission**. The p53
series is a separate subsequent check; its unavailable results cannot become
numbers or convenient exclusions from a selection claim.

The [2009 primary article](https://pmc.ncbi.nlm.nih.gov/articles/PMC2660734/)
connects PMI and synthetic human MDM2 to
[PDB 3EQS](https://www.rcsb.org/structure/3EQS). Its public entry is revision 1.2,
with deposited entity lengths 85 and 12, two listed biological assemblies,
95 modelled versus 97 deposited residues, and a guanidine component. This makes
3EQS a relevant **candidate** for the synthetic-construct context. It does not
certify correspondence to every assayed molecule or replace T0's accepted 1YCR
case. Assembly/model/chain choice, missing material and nonprotein components
need explicit treatment rather than automatic removal.

The accessible 2009 main text does not resolve the 2010 panel's unknown chemical
declarations. Its linked supplement returns a browser challenge in this review;
no PDF content is assumed and no challenge is solved. The alternative
[Yadahalli 2019 study](https://www.nature.com/articles/s41598-018-36589-5)
states acetylated/amidated peptides and a different experimental domain. It
remains a possible separate future study, not a substitute pooled into Li 2010.
Its individually requested table pages were unavailable in this inspection;
no new complete table extraction or numerical reference is claimed.

## Proposed T1b implementation contract

This is the finite scope submitted for review, **not permission to implement it**:

1. Freeze the actual official 3EQS revision-1.2 source bytes, source metadata,
   selected source model/assembly and provider composition before molecular work.
   If source revision or identity differs, preserve the response and investigate.
   Use MolSysMT's source readers and public conversion/query operations.
2. Receive source entity/chain/group/atom correspondence and available chemistry,
   coordinate coverage and missing fields. Keep source IDs, model IDs and native
   indices distinct. Inspect the entire source inventory before proposing any
   subset; no water, ion, cofactor or other component is automatically deleted.
   The initial observation domain is the deposited source model. Any biological
   assembly used later needs a declared owner-supported transformation/mapping.
3. Build a **source-evidence admission ledger**, linking the 35 T1a reported
   entities to their actual chemical declarations, source locators and unresolved
   fields. A reported parent label can be associated with a cited structure;
   that association is not complete atom-level chemical equivalence. Missing
   termini, stereo, modifications, protonation and construct correspondence
   remain unassessed. Do not infer them from PAM resin, coordinates or sequence.
4. Use public MolSysMT assessments/correspondences only within their documented
   prerequisites. An incomplete graph or unassigned stereo must retain its
   refusal/unknown disposition. There is no local parser, cap editor, graph
   assembler, sequence aligner or chemical matcher in PeptideMT.
5. Preserve a source/native round trip through the owner's supported persistence,
   with original producer/history, molecular axes, values/null masks and explicit
   units. Keep T1a experimental quantities unchanged through PyUnitWizard.
   General molecular storage/comparison remains owner-provided. Any case-specific
   report remains a private developer artifact, not a new public API.
6. Deliver an admissibility/gap report and an explicit subsequent molecular-model
   recipe for review. An incomplete source can be received faithfully while
   remaining ineligible for affinity comparison. Report both outcomes; do not
   manufacture a common chemical state to obtain a passing admission.

Meaningful controls must reject source/revision/model mismatches, invented exact
chemical declarations, lost source occurrences, false equivalence of missing
fields and ID/index confusion. Check source and caller unit-policy preservation.
Original and saved inspection must agree within the actual owner storage
contract, without an unnecessary rerun of accepted T0 geometry or T1a receiving.
Failure/partial/unsupported outcomes remain evidence, not silently repaired cases.

No H addition, heavy-atom completion, capping, mutation, protonation assignment,
minimization, energy calculation, docking, learned model, new sequence or training
is part of this proposed T1b contract. Its technical completion cannot accept
experimental chemistry or a scientific predictor that the evidence does not support.

## Owner routes and current gaps

MolSysMT's inspected public peptide-template factory at
[`c9bb16eab13bac7c0ea91607ef61a576c07ee82b`](https://github.com/uibcdf/molsysmt/blob/c9bb16eab13bac7c0ea91607ef61a576c07ee82b/molsysmt/physchem/get_peptide_chemical_template.py)
requires caller-declared states, excludes capped/modified backbones and leaves
stereochemistry unspecified. Public CCD, template assessment/application,
sequence and declared-state correspondence tools are reusable building blocks;
source inspection is not receiving of this newer runtime.
[MolSysMT #685](https://github.com/uibcdf/molsysmt/issues/685#issuecomment-6760190105)
has now been reviewed into the owner's design/backlog, with no implementation
promise or new release gate. The separate terminal-recognition defect
[#686](https://github.com/uibcdf/molsysmt/issues/686) is already owner-tracked;
T1b proposes no terminal-completion operation or workaround for it.

DockingMT's inspected
[`ac459ca7ba4d029b317c653c9af17e258050e752` starting profile](https://github.com/uibcdf/dockingmt/blob/ac459ca7ba4d029b317c653c9af17e258050e752/README.md)
is rigid protein–small-molecule/Vina. Its valuable reference/preparation evidence
does not qualify a peptide profile. The existing
[consumer request](https://github.com/uibcdf/dockingmt/issues/33#issuecomment-6679884695)
owns the question whether a supported composition exists or a bounded extension
is needed. PeptideMT must not write its own external docking adapter to bypass it.

For a later pose pilot, retain the [method review](target_directed_method_review.md)
recommendation to assess **HADDOCK3 through DockingMT**. Its
[official peptide guide](https://www.bonvinlab.org/haddock3-user-manual/bpg/peptides.html)
recommends conformational ensembles. Its
[installation guide](https://www.bonvinlab.org/haddock3-user-manual/download-haddock3.html)
identifies separately governed CNS acquisition/use terms. These are reasons to
freeze the actual workflow, engine/binary/data and terms before installation;
they do not establish that this host can run it within the current limits.
Rosetta and ADCP remain alternatives under the prior review, without a new port
or method adoption. No third-party issue, contact, installation or execution follows.

## Route from this stage to selection utility

After molecular admission, propose a **holo-site-conditioned pose pilot**, with
the actual molecular recipe, ensembles, restraint information, seed/search
budget, output mappings, score definition and structural/adverse controls agreed
through DockingMT. An intact reference pose is not an independent docking
success. Receptor-aligned peptide comparisons belong to MolSysMT. Limits and
success/refutation criteria must be fixed before that new method executes.

Only after that technical/scientific assessment should a fixed affinity-ordering
pilot evaluate the admitted Table 1 series. Candidate comparisons are within-series
rank association and fixed-budget selection versus retaining the parent and a
uniform-selection reference. Freeze selection size, ties, missing-score handling,
equal sampling effort and uncertainty treatment before producing predictions.
Use supported statistics tools for general calculations. No new numerical
endpoint, significance threshold or positive acceptance criterion is adopted here.
Engine scores retain their original meaning/units; no Kd/free-energy calibration
is assumed. A null or adverse result must remain reportable without outcome-driven
retuning or selecting the best budget after inspection.

This source is already exposed and retrospective. Audit method/training exposure
separately from computational-versus-experimental independence. A later useful
design claim needs a justified separate evaluation reference or an honestly
bounded retrospective protocol; random row splitting of related variants will
not supply broad molecular or target generalization. New sequence generation
would be a later separately reviewed capability.

## Resource and decision boundary

The proposed read-only molecular-admission implementation can use serial CPU0/1,
one numerical thread, a 2 GiB aggregate sampled task-RSS stop and a 4 GiB
available-host-RAM reserve, within the investigator's stated host ceiling.
Keep bounded 180 s wall/120 s CPU/8 GiB address space/64 MiB output jobs and no
GPU. D49 delegates reasonable per-run technical limits and diagnosed retries;
this is not a request to reapprove each routine test. A future docking workload
must demonstrate feasibility rather than silently exceed this allocation.

[D14](design_methodology.md#progression-and-review) requires agreement on this
new molecular source/scope before implementation. This proposal approves no
chemical recipe, provider implementation, engine run, predictive acceptance,
commit/push or public package/dataset release. Current delivered work is the
source/provider review, cohort outline and concrete T1b proposal only.
