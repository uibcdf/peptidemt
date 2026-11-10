# Target-directed demonstrator: experimental evidence and provider review

Status: **inspected; feasibility findings and recommendations**, 2026-11-06.
Owner: [PeptideMT #33](https://github.com/uibcdf/peptidemt/issues/33).
Authority: [D52 preparation](target_directed_demonstrator.md).
Next proposed contract: [T1a reported-evidence curation](mdm2_t1a_proposal.md).

Current disposition, 2026-11-10: the T1a proposal/receiving statements below
describe the dated preparation. [D53 T1a is now completed](mdm2_t1a_qualification.md).
The next [T1b proposal](mdm2_t1b_proposal.md) preserves its molecular/chemical
unknowns and distinguishes the next admission question from predictive evidence.

## Finding and recommended progression

A bounded historical MDM2 evidence pilot is feasible. A qualified peptide
affinity evaluator and independent design-improvement claim are **not yet
established**. Start with faithful experimental-evidence curation, then choose
and qualify the evaluation/proposal route against the actual admitted domain.
Do not turn an available docking executable into an affinity reference or use
the accepted AMP resources as an MDM2 predictor.

This is meaningful progress beyond the [completed T0 geometry case](mdm2_t0_qualification.md),
but does not complete the target-directed demonstrator. The next proposal is
data-only; computational selection and subsequent experimental validation
remain distinct milestones of the original objective.

## Bounded primary-source comparison

**Li et al. (2010), DOI [10.1016/j.jmb.2010.03.005](https://pmc.ncbi.nlm.nih.gov/articles/PMC2856455/),
Tables 1 and 3, their footnote and Experimental Procedures.** The article reports
SPR-competition Kd and SD in M for synthetic MDM2(25–109) and MDMX(24–108), with
at least three independent measurements. Manual reconciliation finds 36 displayed
peptide rows: 18 per table, 35 reported peptide labels after recognizing the
PMI A4 self-substitution as its WT repeat. The two p53 substitutions F19A/W23A
are unquantified for both targets. Table 3's caption count conflicts with its
displayed rows. Explicit terminal/stereochemical identities remain unresolved
in the reviewed text; synthesis chemistry is not used to infer them. The linked
DOC supplement could not be received: one ordinary request returns a browser
challenge HTML page, not a document. Its content remains uninspected.

**Yadahalli et al. (2019), DOI [10.1038/s41598-018-36589-5](https://www.nature.com/articles/s41598-018-36589-5),
Tables 1–3 and Methods.** This provides a smaller, differently defined panel:
acetylated/amidated p53(17–29) variants, including phosphorylated species, and
MDM2(2–125). ITC, fluorescence and kinetic estimates are separate readouts. The
publisher states CC BY 4.0, subject to indicated third-party exceptions.
Recommendation: retain as a possible later assay/chemistry transfer challenge;
do not pool it into the first panel. This recommendation is ours, not an author
claim that its measurements validate the first study's endpoint.

**Touti et al. (2019), DOI [10.1038/s41589-019-0245-2](https://pmc.ncbi.nlm.nih.gov/articles/PMC6710073/),
Figure 1 and Methods/data availability.** The MDM2 comparisons distinguish
biotinylated, acetylated and noncanonical/cyclic compounds and kinetic versus
competition BLI routes. Data are reported in the article and linked supplements.
Recommendation: useful future scope, unsuitable for silent pooling as one
unmodified-sequence/one-assay panel. No supplement is downloaded in this review.

Reading publicly available HTML does not establish a general redistribution
license for the two author manuscripts. Initial local curation may retain source
locators and attributed factual observations; public dataset/package release is
separate and requires a source-specific terms review. No author contact is made.
The related 2009 source reached a browser check and was not bypassed; its
uninspected content supplies no chemical admission here.

The main 2010 HTML is retained locally (273,058 bytes; SHA-256
`99f361fdab13c2971362fbe5e96b255e8a32dd5f8d605154bcd98918268f1264`).
The supplement response is retained under its actual HTML disposition, with
its status/content type/hash and no document claim. These are source-preparation
receipts; they do not constitute a qualified extraction of the experimental table.

## Independence, identity and outcome limitations

These sources and some numerical results have already been inspected. This is
an exploratory retrospective pilot, not a blinded or prospectively withheld
benchmark. Record that exposure before method selection. Experimental measurement
is distinct from the proposed computational score, but model-training exposure,
method-development exposure and chemical/series independence must each be audited.
An unfamiliar external identifier or a different sequence string proves none
of those conditions by itself.

For a future qualified method, freeze input eligibility, preparation, parameters,
score direction, missing-result policy, comparison and stopping criteria before
producing panel predictions. If tuning is needed, keep the related peptide
series together; a random row split is inadequate. With only two related series,
do not claim broad scaffold/target generalization or robust train/test statistics.
Any later independent confirmation needs its own untouched evidence/protocol.

Preserve distinct meanings:

- A source row, its duplicate display and an independent experiment are different
  objects. Source-scoped reported identity is weaker than complete chemical identity.
- Reported SD is neither a confidence interval nor proof that every row has an
  independently known replicate count. No raw-replicate distribution is invented.
- Unquantified weak binding is retained with its source reason; it is not an
  exact Kd, a numerical assay limit or a confirmed nonbinder.
- MDMX is a separately measured target and may be a desired co-target. No adverse
  off-target or selectivity objective is assigned without an investigator decision.
- T0 source coordinates and artificial displacements are not experimental labels.
  Observed coordinate coverage does not establish the experimental construct,
  terminal chemistry, solution state or an interchangeable peptide length.
- Binding affinity, cellular activity, uptake, hemolysis and anticancer effect
  remain separate properties. Unknown adverse properties remain unknown.

## Owner capability assessment

Source-only inspection, **not execution or installed qualification**. MolSysMT
is inspected at `ed09f64539a5af6c1dbe9bd352c7ef65dcd4a7a6`; DockingMT at
`530a4cff5d18bb4283d07d22cc1e68298ddb8aac`. Exact inspected files/signatures and
SHA-256 values are in the [review receipt](evidence/target_directed_evidence_review.json).
The sibling primary worktrees, including concurrent DockingMT changes, are preserved.

| Need | Supported owner route and observed limit | Consumer action |
| --- | --- | --- |
| Molecular input/sequence projection | MolSysMT public conversion; `topology.get_sequence_alignment` and `get_sequence_identity` already exist. Identity is query-normalized percent, potentially asymmetric; caps do not contribute sequence letters | Reuse the public operations when a scientific sequence view is approved; never implement an alignment/parser here or mistake sequence agreement for chemical equality |
| Peptide construction | `build.build_peptide` already constructs supported ordered labels and initial geometry | This is construction, not validated conformation, complete chemical state or L-stereo assignment; no construction is executed in this review |
| Explicit chemical templates | `physchem.get_peptide_chemical_template`, `assess_chemical_template` and `apply_chemical_template` already exist | Respect free-terminal/state, mapping and coverage contracts. The factory excludes capped/modified backbones and leaves stereo unspecified; do not silently reinterpret amide as N-methyl amide |
| Terminal completion | `build.add_missing_terminal_cappings`, `get_missing_terminal_cappings`, `add_terminal_atoms` exist | Geometry completion is not chemical qualification or a source-identification method; preserve unknown source termini |
| Exact declared-state atom correspondence | `chemical_states.get_atom_correspondences` supports coordinate-independent constrained bijections over complete chemical context, including explicit chemical/stereo policy and refusal semantics | Reuse this composition where applicable. Partial/unassigned chemistry cannot be made complete to satisfy its own prerequisites. General identity/overlap feedback belongs in [MolSysMT #447](https://github.com/uibcdf/molsysmt/issues/447) |
| Attribute equality | `basic.compare` compares requested attributes and can equate matching missing values | Do not interpret an attribute comparison as proof of chemically complete equivalence |
| Docking/scoring workflow | DockingMT's inspected starting qualification concerns rigid protein–small-molecule docking; [#33](https://github.com/uibcdf/dockingmt/issues/33) retains preparation/scoring-profile acceptance limits | Ask the owner about a bounded peptide profile before adoption. Pose recovery/export acceptance does not establish peptide-affinity ranking; no local engine/scorer is written |
| Measurements and scientific decisions | PeptideMT owns source-specific eligibility, experimental meaning, selection and interpretation; PyUnitWizard owns quantity conversion/interchange | Keep reported quantities and reasons, reuse quantity tools, and choose any statistics provider before calculation; no generic persistence/workflow framework is added |

The existing owner operations refute a need for new local peptide builders,
terminal editors, graph matchers or sequence comparators. No molecular kernel
is implemented, changed or invoked here. A capability gap must be stated against
the actual selected domain; the provider chooses whether an existing composition
or an extension is appropriate. Unknown source chemistry remains a source gap,
not a MolSysMT defect that another API can repair automatically.

Provider feedback reuses [MolSysMT #447](https://github.com/uibcdf/molsysmt/issues/447#issuecomment-6679876257)
and [DockingMT #33](https://github.com/uibcdf/dockingmt/issues/33#issuecomment-6679884695),
with additive `component:peptidemt` relationships and exact comment readback.
No duplicate issue or provider implementation is created.
The [handoff receipt](evidence/target_directed_evidence_review_issue_updates.json)
retains the published comments and observed issue states. The later reciprocal
`component:dockingmt` label on PeptideMT #33 is recorded in the
[documentation closeout](evidence/target_directed_evidence_review_closeout.json).

## Decision needed and next falsifiable result

Review [T1a](mdm2_t1a_proposal.md) as one concrete next scientific contract:
faithful source-scoped reported-affinity curation, including every unavailable
and duplicated occurrence. It intentionally does not select an evaluator yet.
The outcome can reject the panel for a subsequent chemical/model domain; that
would be an informative source decision, not completion of the demonstrator.

After that, prepare a separate evaluation contract naming a qualified peptide
method and simple baselines, score/measurement relation, independence limits,
uncertainty and informative failure criteria. Only an executed comparison can
support a selection-utility statement. A null or adverse comparison must be
reported and must not trigger unrecorded tuning until a positive result appears.

## Provider refresh on 2026-11-09

The investigator reactivates the objective. The
[fresh source/provider receipt](evidence/target_directed_provider_refresh_2026_11_09.json)
preserves the earlier review and records the current remote/source state without
changing the submitted T1a proposal or its scientific authority.

DockingMT now [reports four complete original reference selections](https://github.com/uibcdf/dockingmt/blob/dfff57a34f0278fa6185e88df2098ba6d650e90c/devguide/validation/panel_references_editable_2026-11-08.md):
six coordinate-free protein references and one ligand reference, each under two
unit policies, on its named editable composition. This is valuable owner evidence
for chemical-reference construction, storage, comparisons and typed refusals.
It is not a PeptideMT receiving result, an MDM2 case, a qualified peptide-docking
profile, affinity ranking or a public installation. Two unit policies do not
double the independent case count. Its workspace/native/host identities remain
separate from this machine and T0's preserved profile.

At fetched MolSysMT `97a98578776291e6b2c048bcd876bdedc271967f`, the inspected
peptide-factory and template-application public modules have the same bytes as
the earlier source inspection. The factory still excludes capped/modified
backbones and does not assign residue stereochemistry. The atom-correspondence
module has changed internally but retains its public signature and complete
declared-chemistry requirements. Source inspection does not receive that newer
runtime for PeptideMT. DockingMT's current README still declares the rigid
protein–small-molecule/Vina starting profile; broader readiness is not inferred.

The official bounded workspace inspection finds clean primary sibling worktrees
behind their fetched mains; those worktrees are preserved without pulling,
rebuilding or altering an editable environment. Existing issues #447 and #33
retain their owners; no new PeptideMT-specific profile/identity answer or T1a
acceptance is observed. No duplicate issue is opened.

One ordinary supplement-availability request again returns HTML rather than the
DOC, now a JavaScript proof-of-work download interstitial. Its actual response
is retained, the initial recaptcha-only marker check is corrected by a separate
classification record, and no challenge is solved. Supplement content and source
chemical unknowns remain unassessed. No molecular/model execution, dataset
receiver or new scientific acceptance follows from this refresh.

Further source inspection finds the public CCD reference factory
`physchem.get_chemical_template` and CIP analysis; those routes will also be
reused where applicable. They do not by themselves establish whole-peptide
assembly from explicit capped/stereochemical residue declarations. After checking
existing issues, the concrete reusable need is proposed in
[MolSysMT #685](https://github.com/uibcdf/molsysmt/issues/685), asking first for a
supported composition or an owner-assessed extension. It concerns future
molecular-reference admission, not a defect or a blocker of T1a's reported-data
curation. No molecular constructor, cap editor or stereochemistry kernel is
implemented in PeptideMT. The owner retains API/scope/priority decisions.
The [verified handoff](evidence/target_directed_provider_handoff_2026_11_09.json)
binds the new owner proposal and its reciprocal PeptideMT #33 update.
