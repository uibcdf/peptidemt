# Three worked design problems

Date: **2026-10-26**. Navigation: [index](README.md) ·
[accepted decisions](decisions.md) · [architecture](architecture_alternatives.md).

**Accepted:** the conceptual separation of scientific problem, computational plan
and execution evidence (D09–D13).
**Proposed analysis:** every target choice, chemistry envelope, plan and example
outcome below. These are thought experiments, not selected demonstrators, executed
campaigns, discovered peptides or new API/storage decisions. No sequences, assay
results, model scores, runs or molecule identifiers are fabricated as real data.

The examples are complete at the level of scientific intent and responsibility.
Actual execution would additionally require frozen target/seed assets, model and
weight versions, configurations, budgets and operational policies. Missing assets
are preparation requirements, not silently assumed available. The illustrative
length/chemistry choices constrain these examples only, not PeptideMT's scope.

## 1. Common interpretation of the three layers

| Layer | Owns | Does not establish |
| --- | --- | --- |
| Scientific problem | Candidate domain, target roles and desired interactions, functional meaning, relevant context, exclusions and scientific priorities. | Which predictor is correct, or which generator will work. |
| Computational plan | Input preparation hypotheses, proposal/search methods, evaluators and mappings to objectives, model-specific cutoffs, budgets, selection/diversity policies and coverage obligations. | That surrogate satisfaction implies biological activity. |
| Execution evidence | What actually ran and on which identities/states, raw/derived evaluations, uncertainty/applicability, decisions, failures, deviations, costs and artifact references. | Experimental activity, mechanism or project-level Evidence unless separately supported/interpreted. |

A desired physical minimum, such as an affinity bound with units and conditions,
can be a scientific requirement. A cutoff on an uncalibrated binding score is a
plan-specific proxy. Neither kind of threshold is currently prescribed here.
Unknown or unmeasured scientific quantities remain explicit. Completing a
computation does not require satisfying every scientific objective.

One conceptual family entry can initially hold a human-readable definition,
scope/context, references and explicit unknowns. Its binding to classifiers,
learned proposal distributions or sampling conditions belongs to a plan. This is
a simple semantic sketch, not an approved schema or an ontology.

## 2. Case A — protein binder with CPP properties

### Scientific problem

**Intent:** propose peptides that recognize human GABARAP at its LIR docking
region while favoring cell penetration compatible with access to the cytosol.
Recognition is the requested molecular effect; inhibition of autophagy is not
inferred or required. GABARAPL1 is an illustrative negative target for a
selectivity objective, not an assumed nonbinder.

**Candidate domain for this example:** one linear chain of 12–30 canonical
L-amino-acid residues, free N and C termini, no inter-residue crosslinks,
conjugated cargo, fluorophore or delivery vehicle. Chemical stereochemistry and
terminal assignments must be declared; a one-letter sequence alone is insufficient.
Changing the domain to macrocycles would produce a related problem variant.

**Family intent:** CPP-compatible peptide, with cytosolic availability as the
desired access property. Generic uptake, passive permeability and cytosolic
delivery are distinguishable evidence, not synonyms. The molecule of interest
is the externally supplied peptide, not a peptide expressed as part of a fusion.

**Context and priorities:** human cellular context; target recognition and CPP
compatibility are joint goals. Selectivity and low nonspecific membrane damage
are additional preferences. Exact cell/assay conditions, if later used, must be
declared; their absence does not prevent computational family-compatibility search.
Retain chemically feasible, diverse candidates and tradeoffs rather than declaring
the highest scalar score the unique biological solution.

**Background evidence:** RFpeptides reports GABARAP binders, including structural
evaluation, in a macrocyclic domain. It supports the choice of a peptide-recognizing
target, not the success of this linear domain, CPP activity or the negative-target
objective. [Primary study](https://www.nature.com/articles/s41589-025-01929-w).

### Alternative computational plans for the same intent

| Plan | Proposal and optimization | Evaluation and selection | Declared limitation |
| --- | --- | --- | --- |
| A1. Target first | A target-sequence-conditioned linear generator proposes candidates; an outer search can refine them. | Enforce exact domain; evaluate CPP compatibility, structural recognition and negative-target evidence; retain diversity and objective vectors. | A sequence-conditioned proposal is not proof of a site-specific complex or cell entry. |
| A2. Seed first | Begin from an explicitly supplied compatible linear binder and use mutations or local model proposals. | Reevaluate recognition and CPP after edits; record edit limits and binding-preservation proxies. | Seeds and edit neighborhoods restrict exploration. No actual compatible seed is asserted here. |
| A3. Family first | Sample a CPP-enriched sequence model, then optimize target recognition under the same chemistry envelope. | Reevaluate CPP after recognition-driven changes and test site/negative-target evidence. | Family enrichment may produce poor binders; no objective is silently dropped if the search fails. |

Different models/cutoffs may be used in these plans; the scientific objective
remains the same. A model that cannot evaluate the declared termini must abstain
or label an explicit projection with its limitations. RFpeptides macrocycles
cannot be inserted unchanged as A1 outputs: they violate this example's domain.

### Execution evidence and a hypothetical interpretation

Retain target sequence/structure snapshots and selected regions; model, checkpoint
and training-domain information; exact candidate chemistry; proposal ancestry;
per-predictor outputs and applicability; prepared molecular states, conformers and
poses; raw selection rules; and computation/failure records.

An illustrative candidate may receive a favorable CPP classifier score and an
unfavorable score from a second classifier. A passive-permeability model might be
favorable too. Store the three claims separately: the latter is not a vote that
settles cytosolic access. A good GABARAP pose with no GABARAPL1 evaluation leaves
selectivity unassessed. A terminally amidated derivative is outside this problem's
domain even if stripping that modification yields an apparently acceptable input.

The run can finish with a diverse, mixed-evidence candidate list or with no
candidates satisfying its operational selection policy. Neither outcome asserts
measured CPP activity or a demonstrated intracellular binder.

## 3. Case B — antimicrobial peptide directed at a protein

### Scientific problem

**Intent:** propose peptides with antibacterial potential against the reference
organism E. coli K-12 and with molecular recognition intended to interfere with
the protein-interaction surface of its DnaN sliding clamp. Protein binding,
functional interference and whole-organism activity remain separate objectives.

**Candidate domain for this example:** single linear peptides of 15–35 canonical
L-amino-acid residues, free termini and no additional covalent modifications.
The intended candidates are externally supplied molecules. No mammalian CPP
requirement is imposed: bacterial entry is a separate property/context.

**Family intent:** AMP in the antibacterial sense used here, directed to this
organism context. Broad-spectrum antimicrobial activity and AFP activity are not
implied. Organism-specific potency and toxicity are unknown until appropriate
evidence exists. Avoid nonspecific host-cell damage; human PCNA is an illustrative
negative molecular target for a separate selectivity preference.

**Priorities and exclusions:** retain joint recognition/AMP potential, feasible
chemistry and diversity. A strong membrane-disruption signal alone does not
establish the desired DnaN-directed mechanism. It can be retained as a conflicting
or alternative mechanistic indication rather than erased. Lack of information
about access, inhibition or toxicity remains visible, not an inferred negative.

**Background evidence:** optimized griselimycins target DnaN in M. tuberculosis.
This supports DnaN as a precedent for peptide-mediated antibacterial action.
Those species/chemical results do not establish activity in E. coli K-12, and
the chemically different molecules are not compatible linear seeds automatically.
[Kling et al., Science 2015](https://pubmed.ncbi.nlm.nih.gov/26045430/).

### Alternative computational plans for the same intent

| Plan | Proposal and optimization | Evaluation and selection | Declared limitation |
| --- | --- | --- | --- |
| B1. Target first | Generate compatible linear proposals against the declared DnaN structure/site, then use external AMP evaluation and refinement. | Keep recognition, antibacterial compatibility, chemistry and negative-target evaluations separate. | Binding/pose confidence cannot be relabeled as DnaN inhibition or organism potency. |
| B2. Family first | Sample an AMP-enriched generator and use black-box or evolutionary search toward the DnaN interaction objective. | Recheck both objectives after edits; use an independent model/panel for comparison when available. | A generic AMP model may cover other organisms/mechanisms and be a weak proxy for this task. |
| B3. Compatible-seed redesign | Use a supplied linear peptide with relevant support, exploring a recorded neighborhood. | Preserve scientifically required interaction features where specified; quantify the operational proxies and failures. | Literature similarity is not evidence that a chosen seed meets this problem's chemistry or mechanism. |

Model thresholds, structural engines and experimental endpoints used as proxies
are plan bindings. The desired antimicrobial property is unchanged when the AMP
predictor is replaced. A predicted MIC is meaningful only with its organism,
conditions, units and model scope; it is not interchangeable with a binary score.

### Execution evidence and a hypothetical interpretation

In addition to common provenance, retain the organism/target/negative-target
identities, target-state assumptions, antibacterial-model dataset and negative
construction, any organism-conditioned outputs, interaction hypotheses and
unassessed entry/inhibition/host-toxicity objectives.

An illustrative candidate can have strong general AMP compatibility and a poor
DnaN recognition assessment. That is not a target-directed success. Another can
have favorable DnaN structural evidence with missing organism activity and
bacterial-access evidence: it remains a computational candidate, with those
gaps recorded. An unfavorable PCNA evaluation cannot automatically be compared
numerically with a DnaN score from another scoring method. Species-specific and
general predictors can disagree without either being silently overwritten.

Replacing the organism or deciding that membrane disruption alone now meets the
goal changes the scientific problem; it is not simply a different optimizer.

## 4. Case C — CPP + ACP conditioned on a molecular target

### Scientific problem

**Intent:** propose externally supplied peptides combining CPP-compatible access,
ACP potential and antagonism of the human MDM2–p53 interaction, in a context of
TP53-wild-type cancer cells whose response may depend on this pathway.
MDMX/MDM4 is an explicit secondary target to characterize, not silently a negative
target or a required positive target. The cancer cell line and nonmalignant
comparator would be declared before making context-specific efficacy claims.

**Candidate domain for this example:** peptides of 12–35 residues in two declared
modalities: linear canonical-L peptides, or singly hydrocarbon-stapled peptides
with explicitly specified noncanonical building blocks, stereochemistry and link
chemistry. Free versus specified terminal caps are permitted only as distinct
chemical candidates. No undefined crosslink is accepted. This envelope is an
illustrative stress test, not adoption of these chemistries as initial support.

**Family intent:** CPP compatibility and ACP potential are independent desired
functions. ACP denotes a context-dependent anticancer phenotype; the target
antagonism objective supplies an intended mechanistic connection. General cell
toxicity is not enough to meet that connection. Cytosolic access, antiproliferative
activity, pathway engagement and nonspecific membrane damage remain distinct.

**Priorities:** seek joint target/family support, selectivity over nonspecific
toxicity, chemical feasibility and diverse candidates. Demonstrated mechanism or
experimental joint activity is not required to finish a computational campaign.
The strength of the resulting claims is limited to available evidence.

**Background evidence:** ATSP-7041 studies connect binding, cellular access and
p53-dependent responses. Later work examines permeability and off-target effects
with separate counter-screens. These motivate preserving distinct claims rather
than treating a cancer-cell effect as automatic proof of target action.
[Initial study](https://pubmed.ncbi.nlm.nih.gov/23946421/),
[mechanistic study](https://pubmed.ncbi.nlm.nih.gov/27721413/),
[design/counter-screen study, 2024](https://www.nature.com/articles/s41467-023-43346-4).
These are references, not assay results for PeptideMT candidates.

### Alternative computational plans for the same intent

| Plan | Proposal and optimization | Evaluation and selection | Declared limitation |
| --- | --- | --- | --- |
| C1. Target first | A compatible target-conditioned generator supplies linear or supported stapled candidates, followed by CPP/ACP evaluation and external refinement. | Retain family and recognition vectors, chemical support and nonspecific-toxicity indicators. | Most canonical-sequence evaluators do not cover the full stapled domain. |
| C2. Multifamily search | Use family-enriched proposals or a compatible multilabel model with outer target-recognition optimization. | Preserve each model's definition/missing-label treatment; recheck recognition and chemistry. | Independent scores do not estimate joint activity; learned label dependence may reflect annotation bias. |
| C3. Compatible inference-time guidance or redesign | Guide completed rollouts with black-box scores, use compatible differentiable guidance, or edit a supported reference scaffold. | Record the actual intervention, parent identities, links/caps and target-preservation checks. | Guidance must have representation support; a classifier on linear clean sequences cannot automatically score partial SMILES or a stapled molecule. |

A plan may cover only the linear subdomain. It must state that limitation; it
cannot claim that failure there excludes the stapled domain. Compare plans on
matched subdomains or report modality-stratified coverage. A canonical projection
of a stapled peptide can be recorded as a limited surrogate if explicitly allowed
by the plan; its score does not become an assessment of the full molecule.

### Execution evidence and a hypothetical interpretation

Retain the exact linear/stapled chemical identity, terminal changes, all-L/D or
noncanonical stereochemistry where applicable, parent/derivative relationships,
which structure/state/pose each evaluation used, and any projection into a model's
input alphabet. A change of staple, cap or residue chirality creates a chemically
different candidate for this analysis; conformer/chemical-state identity is a
separate question still awaiting P07 approval.

An illustrative linear candidate can receive favorable CPP and unfavorable ACP
outputs; a second ACP model may disagree. Preserve both outputs, dataset scopes,
calibration and selection consequences. Do not multiply them into an invented
joint probability. A stapled candidate can have favorable target-interaction
evidence but no applicable CPP model. That is missing family evidence, not a
zero score or a demonstrated CPP. Generic ACP compatibility does not establish
activity in the requested TP53 context or its causal dependence on MDM2.

If experiments later arrive, attach their measured molecule identity, assay and
conditions as new evidence. Do not rewrite the historical prediction or transfer
an assay on a labeled/tagged analogue to its parent peptide without qualification.

## 5. Method substitution and comparability

| Must remain invariant to claim the same scientific problem | May change between computational plans | Must record what actually happened |
| --- | --- | --- |
| Desired functional meanings, target roles and biological scope | Predictors, generators, optimizers and operational score cutoffs | Model/weight versions, exact inputs and output semantics |
| Allowed chemical domain and scientifically required exclusions | Which admissible subset the search explores; proposal modes and seed neighborhoods | Actual coverage, unsupported modalities and rejected candidates |
| Scientifically required preservation/interaction criteria | Surrogate mappings, validation methods and numerical search settings | Unassessed requirements, conflicting evaluations, deviations and failures |
| Relevant scientific priorities or explicit physical bounds | Computational budget and selection implementation consistent with those priorities | Resource consumption, selection rationale and retained raw objective values |

These freedoms do not make unlike plans equally informative. A shared scientific
problem is not sufficient for a fair numerical benchmark. Match or normalize
budgets, candidate subdomains, target assets/states and evaluator-call accounting;
record the stopping rule and compare selection using an agreed common independent
panel when possible. Different proxy scales cannot be compared directly. The
panel need not be perfect; preserve its own scope and provenance.

An exploratory absence of a numerical biological bound is permitted. If a
scientist does specify a measured-affinity or potency requirement, all plans must
preserve its meaning even when they cannot assess it. Adding a preservation rule
only because a particular seed editor supports it must not silently become a
new scientific constraint binding every strategy.

## 6. Common concepts, exceptions and exposed insufficiencies

All cases need a candidate domain, target roles, family meanings, objectives and
constraints; plan bindings and capability checks; and execution-level candidate
identities, evaluations, selection history, uncertainty/applicability and lineage.
No special case requires redefining the accepted three-way separation.

The following are **proposed refinements**, not adopted schemas:

1. **Chemical identity versus views.** A sequence, SMILES and molecular file can
   represent one candidate with different fidelity. Changed caps/links/chirality
   can instead describe a derivative. Candidate identity cannot be a one-letter
   sequence alone. Molecular states/conformers/poses need qualified references;
   deciding their precise identity relationships is P07, not settled here.
   In particular, protonation/tautomer states may be grouped under a designed
   parent for some tasks while evaluations still refer to an exact chemical
   species. That grouping policy is open; neither "all states are one molecule"
   nor "every state is a new design candidate" is adopted by this exercise.
2. **Evaluation subject and claim.** Each output must identify the evaluated
   candidate, any representation/projection, state/pose and the property actually
   predicted. The intended family and the operational proxy stay related but
   distinct. This supports simple families without a full ontology.
3. **Contradictions versus noncomparability.** Opposite predictions on the same
   subject/property/context are a possible disagreement. Uptake versus PAMPA,
   different chemical forms, or distinct organisms are different claims. Retain
   both rather than inventing a consensus. A plan's aggregation rule is a decision
   with provenance, not newly discovered biological truth.
4. **Completion versus adequacy.** Record separately whether execution finished,
   whether chemistry/constraints were verified, which requested properties were
   assessable and which computational selection criteria were met. An empty
   selection, unsupported model or unfinished evaluator does not become success.
   A finished run with insufficient evidence remains finished but scientifically
   limited. Exact status vocabulary remains open.
5. **Evidence can outlive/reinterpret a run.** New evaluations or experiments
   should reference historical candidates and original results; preserve earlier
   states. A new interpretation is not a rewrite of the recorded computation.

## 7. Traceability and ecosystem ownership

At a minimum preserve references to the problem revision, requested plan,
realized settings/deviations, target/seed snapshots, model/checkpoint identities,
candidate parentage and chemistry, preparation/transformation reports, individual
evaluations and selection decisions. Threshold changes belong to a plan revision
or an explicit new selection operation; retain the earlier choices. This is a
semantic provenance requirement, not a new storage format or identifier syntax.

Use the [preserved audit](integration_audit.md) rather than assuming new support:

- MolSysMT owns molecular representation, preparation, conversion reports and
  maps. Its peptide-template factory is bounded and does not cover arbitrary
  staples/caps/cyclic chemistry or declare stereochemistry. Cases B/C do not
  automatically become executable through that factory.
- DockingMT owns docking execution and result semantics. Current Vina rejects
  nonempty constraints/search_guidance, so interaction/family goals must be
  handled by a compatible outer plan or another agreed backend.
- PharmacophoreMT consumes explicit prepared interaction observations; TopoMT
  supplies optional geometric context; ElastNetMT may supply target-motion
  analysis. None establishes a family or cellular mechanism by itself.
- PeptideMT owns peptide design operations and native evaluation/selection data.
  MolSysViewer presents them; MolSys-AI may invoke their future public tools.
- Praxis may represent reusable cross-tool methods. Recorda may observe declared
  operations without replacing native result provenance. Nextia owns contextual
  project Evidence/Decisions; execution evidence here is not that epistemic
  object automatically. A PeptideMT candidate's project role remains distinct.
- ArgDigest/DepDigest/SMonitor/PyUnitWizard support validation, optional execution,
  diagnostics and quantities; they do not decide family semantics or scientific
  adequacy. No new dependencies or adapters are implemented by these examples.

## 8. Assessment and next proposed decision

Alternative B passes this **conceptual consistency exercise**: each case supports
multiple plans while retaining its intent, and exposes differences in evidence
without redefining the desired function. This is not empirical validation,
implementation proof or approval of the proposed refinements.

The most foundational unresolved dependency is **what identifies the candidate
being designed and evaluated**. Proposed next discussion: accept a conceptual
distinction between chemical candidate, representation and molecular state/pose,
with explicit transformations/projections. Leave identifier syntax, MolSysMT
adapter design, chemical canonicalization and the initial supported domain open.
This would make evaluator bindings and family evidence interpretable before
designing an API. It is recorded as P07 and awaits investigator approval.
