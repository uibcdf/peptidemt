# Historical HydrAMP panel: experimental chemistry and sequence-model view

Status: **review proposal v1; scientific view and implementation not approved**,
2026-11-04 (local date). Owner:
[HydrAMP #3](https://github.com/uibcdf/hydramp/issues/3); consumer:
[PeptideMT #32](https://github.com/uibcdf/peptidemt/issues/32).
This follows the [C0 data audit](hydramp_C0_data_audit.md) and refines one pending
entry decision in the [comparison protocol](hydramp_scientific_comparison_protocol.md).
Neither earlier record is rewritten or reinterpreted as permission to execute.

## Recommendation for investigator review

Prepare a finite **historical fixed-input comparison**, using the original
published residue strings and preserving the experimental entities' documented
C-terminal amidation. Permit a separately recorded, deliberately incomplete
sequence-model view **only for that research comparison**, after approval.
Do not change general PeptideMT admission or infer that an amidated molecule
and an unspecified molecule are chemically equivalent.

The immediate purpose is to ask whether original and modern implementations
behave comparably on the same historical inputs. Evaluating their predictions
against measured activity is a separate question with additional endpoint and
exposure requirements. Neither question, on this selected panel alone, establishes
independent generalization, superior proposals, de novo quality or formal
biological equivalence. Retain previous numerical improvements and failure
evidence; do not change the modern arithmetic to imitate original approximations.

This is a scoped research-view proposal under the existing design's distinction
between source proposal, chemical realization and computational view (D16/P07).
It selects no new general architecture, public class, storage format, evaluator
or selector. No sequence-model payload is constructed at preparation.

## Evidence and exact review inventory

The [preparation receipt](evidence/hydramp_historical_view_proposal.json) pins
the data inventory, source/code observations and proposed row correspondence.
It reuses the audited source data rather than downloading or re-parsing FASTA.
The original article's [Tables 1–2 and Methods](https://doi.org/10.1038/s41467-023-36994-z)
are the primary source. PDF table layout independently confirms the column
mapping used below.

The review inventory retains all **42 table occurrences / 39 distinct raw
strings**. Proposed assay scope is **E. coli ATCC 25922 MIC**, displayed in
µg/mL in both tables. This is a proposed scope, not a qualified training-class
label or frozen execution cohort. It avoids depending on the other Table 1
column's unresolved ATCC 43927/43827 discrepancy; that column and its ambiguity
remain preserved in the C0 source, not silently corrected.

There are 35 displayed numeric values and seven `>` bounds in this proposed
column selection. None is converted, thresholded, treated as an uncensored
boundary, or declared a model probability. Three strings appear in both tables,
with different reported values even for the named common strain:

| Published name | Table 1 MIC, µg/mL | Table 2 MIC, µg/mL | Proposed handling |
| --- | ---: | ---: | --- |
| Pexiganan | 4 | 16 | Retain both table observations |
| Hydraganan-1 | 2 | 8 | Retain both table observations |
| Hydraganan-2 | 16 | 128 | Retain both table observations |

This is reported variation, not an established typo, provider bug or proof of
two fully equivalent experimental preparations. Do not average values, select
the minimum, choose a preferred table after predictions, or count both as
independent peptide cases. The original table caption explicitly notes the
additional measurements. Preserve source occurrence IDs even if a future
approved analysis groups observations by raw string; a string group is not a
chemical-identity assignment. Batch layout and any prediction reuse require
their own prospective specification because previous scores show near-tie
batch-context sensitivity.

Six distinct strings overlap the inspected published reference pools, including
three in the MIC pool. The remaining strings retain unresolved checkpoint and
derived-fragment exposure. **Zero independent test members are qualified**.
Excluding only those six would not turn the remainder into a clean benchmark.
Deep_AMP's 39–49-residue functional designs remain outside this proposal.

## Proposed relation: retain the entity, declare the omitted information

| Record | What it preserves | What it does not assert |
| --- | --- | --- |
| Original experimental observation | Article/table/row, name, exact source string/hash, original cells, documented amide, assay identity, units and censoring | Complete chemical identity from uppercase letters alone; missing chemistry or conditions remain unresolved |
| Proposed sequence-model view | Same residue string and order, source-observation link, omitted-feature declaration, approved use and provenance | Chemical equivalence, amidation-sensitive features, an unmodified experimental entity or general model applicability |
| Future paired computational result | Exact provider/checkpoint/environment, actual native tokens/padding/batch, both engines' raw outputs and source/view links | Measured activity, calibrated probability, synthesis approval or independence |

For this finite comparison, the contemplated view contains the unchanged
canonical residue string of length 1–25. The source entity retains its C-terminal
amide annotation. The view explicitly states that the native residue-token
model does not encode that annotation. That is **information loss in a feature
representation**, not removal of the annotation from the source, a physical
reaction, a correction of the publication or a chemical-identity relation.

Unknown N-terminal state, stereochemistry, other modifications, preparation
identity and missing assay metadata stay unknown unless the source supports
them. Some unknowns may remain compatible with a finite implementation-fidelity
question; they do not thereby become adequate for molecular-mass calculation,
assay equivalence or biological applicability. A conflicting annotation or
unapproved realization requires separate review, not an inferred default.

The preparation manifest records the proposed relation but deliberately creates
no unannotated `SequenceRecord`, native token array or dispatchable model input.
Today, an annotated source record still receives
`unassessed_explicit_chemistry`. Do not remove annotations, put them only in
`context`, pass an unannotated copy through `redesign_hydramp`, add a skip flag,
or report the current gate as passed. The proposed future research fixture
requires explicit authorization of its own view; it is not an implicit exception
to D35/M1–M8 or D45 admission.

The relation is limited to these historical fixed inputs. It grants no amide
support claim for Macrel, analogue generation, new candidates, other terminal
groups, D-residues, cyclization or other families. It does not generalize unknown
chemistry into an accepted realization. Initial M, all residues and native
padding/token semantics stay unchanged.

## Two questions, with separate readiness requirements

**Implementation behavior on historical strings.** A later paired experiment
can compare exact original/modern inputs and outputs, retaining batch/order,
raw scores, ties and any decision differences. Source-pool exposure does not
invalidate that narrow implementation question, but cannot supply biological
independence. Reuse completed parity/reference campaigns first; a new campaign
must name the additional unresolved question it answers. Neither a new numerical
tolerance nor formal equivalence margin is approved here.

**Predictive usefulness for the measured chemical entities.** A later assessment
needs an approved assay estimand and adequate chemistry/source provenance.
The training notebook labels pooled E. coli `value < 1.5`; the starter describes
log10(MIC/µM). ATCC 25922 measurements from one publication are a strain-specific
transport question, not automatic reconstruction of that pooled target.
The paper's µg/mL activity thresholds cannot substitute for the native µM class
definition. Even an ordering in mass-concentration units need not be an ordering
in molar units across peptides with different molecular masses.

Do not compute Brier scores, calibration, class accuracy or class agreement
against invented labels. Any required mass belongs to a sufficiently specified
experimental entity and MolSysMT's qualified molecular-system operations; unit
conversion belongs to PyUnitWizard. Keep displayed numbers and `>` relations
until that route and the endpoint are reviewed. A censored interval can give a
class label only when the entire allowed interval is on one side of the approved
strict cutoff. Source uncertainty and repeated observations must remain visible.

No primary biological endpoint, pooling rule, acceptance threshold, independent
sample size, confirmatory analysis or new model budget is selected here. The
broader protocol's proposed 128 cases and 80% relation remain unapproved.

## Component boundaries and existing operations

PeptideMT owns the question, scientific permission to use a lossy view, assay
interpretation and source-to-result correspondence. HydrAMP owns its native
residue codec, checkpoint equations and fixed-input heads. MolSysMT owns
molecular representations, chemistry, general sequence/form interoperability,
mass and alignment; PyUnitWizard owns units. No duplicated parser, capping
implementation, molecular identity, mass formula or unit converter is proposed.

Static inspection of MolSysMT
[`71fbe4f4`](https://github.com/uibcdf/molsysmt/tree/71fbe4f46d3c70e4e973c8025f01752a8c9b1084)
finds an `NH2` terminal template and public `physchem.get_mass`. Its public
capping documentation distinguishes `NME` as N-methyl amide. **NME must not be
substituted for a primary C-terminal amide.** Template presence and a mass API
are not qualification of an exact preparation: no molecule, terminal group or
mass is constructed or evaluated in this work. Source-only inspection establishes
neither a missing MolSysMT operation nor a defect needing a new issue. A concrete
unsupported capability found during later qualified owner-tool use must be
reported to that owner, with this consumer evidence.

Generic journals, attribution and methodologies keep their existing owners;
this review manifest is an ignored task artifact, not a new shared persistence
system. HydrAMP #3 and PeptideMT #32 retain this proposal. HydrAMP #4 keeps the
independent product review; no new issue or third-party contact is needed.

## Approval boundary and observable next work

The requested decision is whether to adopt **this finite historical
experimental-entity/unchanged-sequence view and its E. coli ATCC 25922 review
scope** as a preparation direction. It would allow the next model-free work
order and controlled fixture design. It would not qualify the panel, change
general input admission, implement a new public API or authorize learned-model
execution. This document remains a proposal until that decision is explicit.

Before a later implementation commission, a concrete work order must specify:

1. Complete required source/view/result correspondence and unknowns; immutable
   source records, positive/negative authorization cases and fail-closed handling
   for an unapproved view. Prove existing public admission remains unchanged.
2. Original observation retention, repeated-string groups and unresolved values;
   no hidden deduplication, minimum selection, unit conversion or label creation.
3. Exact provider codec/ownership and read-only fixture receiving, preserving
   source hashes and every omitted feature. Additional molecular operations use
   actual owner APIs and their separately qualified inputs.
4. If measured performance is commissioned, the approved estimand, conversion,
   censoring/observation policy, source-use/exposure limits and uncertainty plan.
   A model-free review cannot award biological acceptance.
5. Before real model work, an exact bundle/input/batch plan, necessity relative
   to existing evidence, prospective diagnostics and fresh host/call approval.

Preparation here consists solely of source inspection, standard-library joining
of the existing C0 records, a non-dispatchable review manifest and documentation.
No ML/Macrel/PCA/descriptor/training/GPU, molecule-building, mass, conversion or
alignment call occurs. Existing accepted bundles, selectors, M1–M8 and all
exhausted execution allowances remain unchanged. No source installation,
runtime edit, commit, push, release or original-author contact is performed.
