# PeptideMT design guide

Updated: **2026-10-28**. This is the maintained design source of truth.
It supports scientific discussion rather than replacing it with a completed
specification. The bounded W1 core is implemented; one installed Macrel CPU
bundle now has W3 computational qualification evidence, with scientific
acceptance and separate provider/consumer follow-up retained.

## Reading path

For implemented W1 tools, see [sequence inputs, saved results and selection](w1_core.md).
The core works without Macrel. The [W2 native boundary](w2_macrel.md) uses
in-memory inputs and MolSysMT transport. The [W3 assessment](w3_assessment.md)
records the actual native execution, exact comparisons, limits and saved replay.
FASTA ingestion now delegates to MolSysMT's source-preserving development API;
in-memory inputs and saved-result replay remain independent of that provider.
The [W3 preparation](w3_qualification.md) records candidate bytes, upstream
fixtures, optional scientific attribution and proposed host execution bounds.

1. [Scientific vision and scope](vision_scope.md): the current provisional
   definition, boundaries and the computational role of functional families.
2. [Integration audit](integration_audit.md): preserved findings from all eleven
   MolSysSuite repositories and six MolI repositories, pinned to inspected source.
3. [Bioactive functional families and multifunctional datasets](functional_families.md):
   verified 20/21/47-label precedents and accepted P08 conceptual separation of
   functions, source labels and qualified resources.
4. [Literature and learned functional spaces](literature.md): primary references,
   public implementations, negative-data caveats and inference-time guidance.
5. [Architectural alternatives](architecture_alternatives.md): alternative B
   accepted conceptually; P07 alternative III accepted as semantic responsibilities.
6. [Five worked design problems](design_examples.md): the original four
   conceptual cases plus a published-evidence-anchored intracellular CPP-like,
   MDM2/MDMX-directed anticancer peptide case (ATSP-7041); not a V0.1 gate.
7. [Preliminary roadmap](roadmap.md): incremental capabilities without selecting
   a definitive model or experimental demonstrator.
8. [Decisions and discussion history](decisions.md): accepted working directions,
   proposals, hypotheses and the correction of earlier recommendations.
9. [Open questions](open_questions.md): prioritized scientific and technical
   decisions for discussion, one at a time.
10. [Design and implementation methodology](design_methodology.md): scientific
    discussion and approval, implementation readiness and technical freedom.
11. [Generative strategy comparison](generative_strategies.md): five approaches,
    mathematical limits, actual engine access, cost, diversity and training needs.
12. [Capabilities and composition](capabilities_and_composition.md): conceptually
    resolved P09, accepted seven principles and context-sensitive semantic meaning;
    RFD4/Chaperone/short-peptide probes and deferred concrete contracts.
13. [Protein and peptide design engines](protein_peptide_design_engines.md):
    expanded evidence matrices, Chaperone/RFD4 source review, short-peptide
    benchmarks, optional integration routes and the evidence underlying P09.
14. [Future scientific horizons — V0.2](future_horizons.md):
    long-term peptide engineering, combinatorial libraries, TCR–pMHC design,
    pharmacokinetics, proteolytic transformations, massive screening and
    nontherapeutic applications, with architectural triage, S1–S12 stress tests
    and a bounded library/state/transformation review after P09 approval.
15. [Evaluation, feasibility, selection and claims](evaluation_and_selection.md):
    accepted P04 alternative 2 and seven principles, bounded MOLI responsibility,
    A/B/C cases and accepted X/Y requirement/check/evidence separation (D29).
16. [Multiobjective optimization](multiobjective_optimization.md): scalar, Pareto,
    hierarchical/constrained, uncertainty-aware and diversity alternatives; invented
    X/Y/CPP/hemolysis examples and reproducible policy versus search comparisons.
    Accepted search/results/selection separation (D30), a three-purpose operational
    case, accepted scoped-restriction reasoning (D31) and proposed scientific
    obligations for future implementable components.
17. [Uncertainty, diversity, budget and P04 synthesis](uncertainty_diversity_budget.md):
    F/I evidence limits, optional diversity measures, decision-relevant evaluation
    allocation and cost/reuse accounting. C1–C5 and conceptual P04 closure are
    accepted under D32; concrete capability contracts remain to be specified.
18. [PeptideMT V0.1 alternatives and minimum contracts](v0_1_alternatives.md):
    A/B/C compared, actual candidate resources/terms/environment evidence, proposed
    capability contracts, acceptance cases and bounded P02/P03/P05/P06 decisions.
    B with A as its first increment is now accepted under D33; no model selected.
19. [V0.1 bounded scope and implementation proposal](v0_1_scope.md): accepted
    increments versus pending resource/domain choices; targeted feasibility,
    generation/selection/feedback controls, shared-bias limits, failure contracts,
    acceptance cases, ownership and the priority target-directed milestone.
20. [Increment 1 specification and HydrAMP qualification](v0_1_increment_1.md):
    D35 accepts the Macrel scientific contract, conservative leading-M treatment,
    provisional chemistry/length scope, two exact selectors and M1–M8. H0–H4
    remains a bounded generator qualification proposal; no gates executed.
21. [Increment 1 commissioning and readiness brief](increment_1_work_order.md):
    scientific closure versus operational prerequisites; draft central admission,
    staged starter integration, W0–W4 deliverables, engine-free/live test lanes,
    Codex discretion and required evidence. Authorized under D36; W0 engineering
    received, W1–W4 retain their own scientific gates.
22. [Scientific north star and milestone trajectory](scientific_trajectory.md):
    original target+functional-family hypothesis, differentiating value, risks,
    evidence-based progress milestones and no-implementation-scope guardrails.
23. [Case-guided CPP-like anticancer binder: ATSP-7041](case_study_cpp_anticancer_mdm2_mdmx.md):
    published MDM2/MDMX-p53 mechanism, PDB 4N5T chemical/construct caveats,
    separate access, recognition and cellular endpoints, plus E0–E7 future tests.
24. [Representative CPP case-guided project pool](cpp_guided_projects.md):
    twelve complementary guides spanning arginine-rich/penetratin CPPs,
    cargo delivery and endosomal escape, p28 anticancer target engagement,
    iRGD tissue penetration, pHLIP pH dependence, cyclic CPPs, stapled binders,
    joint CPP+AMP guidance, oligonucleotide delivery and proteolytically
    activatable CPPs; future references, not V0.1 commitments.
25. [Supplementary CPP guide cases](cpp_case_portfolio.md): four non-overlapping
    extensions to the canonical twelve: Pep-1 noncovalent protein cargo,
    GALA acid-fusogenic helper, mitochondrial peptide targeting, and
    buforin II bacterial intracellular AMP behavior.

## Engineering receiving and reporting

- [Development governance map](governance.md): required tools, direct-push/PR
  routes, release identities, owning issues and component responsibility boundaries.

- [W0 integration and qualification](archive/complete_w0.md): genuine
  admission/starter provenance, applicability reviews and executed evidence.
- [Local reporting protocol](reporting_protocol.md) and generated
  [pending proposals](pending_proposals/README.md), [pending bugs](pending_bugs/README.md)
  and [archive](archive/README.md). Scientific topical discussions remain outside
  those issue-backed queues.
- [Optional-engine review](optional_engine_review.md): no implemented route in W0;
  revisit with W2. [Release titles](release_titles.md) apply only when commissioned.

## Evidence and status

- **Accepted direction:** explicitly requested/approved by the investigators.
- **Pending proposal:** recommendation or alternative awaiting approval.
- **Research hypothesis:** a claim to test, not an established capability.
- **Verified observation:** bounded source/document inspection, with its scope.
- **Open question:** an unresolved choice or missing evidence.
- **Superseded recommendation:** retained to explain a change in reasoning.

Code presence is not runtime success; runtime success is not scientific
validation. A published paper's claim, an inspected implementation and a
PeptideMT integration are separate evidence levels.

## Current discussion

The investigators approved separating scientific design intent, computational
plan and execution evidence, with functional families independent of their
models (D09–D13). Desired bioactivity remains distinct from operational score
criteria; no complex ontology is required.

The [worked examples](design_examples.md) test this separation. A newer
[literature-grounded function review](functional_families.md) expands beyond the
three frequently discussed labels (CPP, AMP, ACP) to many potentially overlapping
functions. P07 alternative III and explicit hypothetical-realization evaluations
are accepted (D15–D16), with traceability, no automatic score transfer and no
mandatory stages. Canonical identity, state grouping, identifiers, persistence,
concrete interfaces and initial chemistry support remain open; see
[Q3](open_questions.md#q3-candidate-chemistry-and-representation).

[P08 alternative 2](functional_families.md#p08-conceptual-alternatives-and-generative-use)
is accepted (D17–D20): an extensible scientific catalog, qualified source/resource
associations and relations, justified indirect/exploratory guidance, and distinct
reward versus independent assessment roles. No formal ontology, evidence-state
enum, API or definitive model is adopted.

The [strategy comparison](generative_strategies.md) under P05 remains relevant;
the investigators endorse potentially complementary strategies and simple
comparison references. [P09's capability/composition organization](capabilities_and_composition.md)
is now **resolved conceptually**.
Provider availability, strategy requirements, plan selection and actual use are
accepted responsibilities (D21); operational/runtime/scientific compatibility are
accepted dimensions (D22). D23–D24 accept origin-independent, domain-aware support
and optional individual/composite access without inherited internal capabilities.
No mandatory Chaperone dependency or obligation to implement both routes follows.
D25–D26 adopt alternative B, all seven principles and sufficient fundamental/
contextual/optional information for actual use. Unknown operations remain unknown;
exploratory applicability cannot supply a missing operation. Concrete contracts,
interfaces, schemas and implementation remain deferred. The [three semantic cases](capabilities_and_composition.md#8-three-tests-of-minimum-capability-meaning)
and [expanded engine evidence](protein_peptide_design_engines.md) preserve the
reasoning. No model, universal interface or mandatory execution stages are selected.

The [future horizons](future_horizons.md) are strategic research opportunities,
not accepted specifications, a revised implementation roadmap or new mandatory
work before the first useful release.
The [bounded review](future_horizons.md#9-bounded-extensibility-review-after-p09-approval)
proposes only a collective-design distinction (P10); it does not adopt library,
ensemble or reaction capabilities. P10 remains pending as explicitly requested.
The current [P04 analysis](evaluation_and_selection.md) distinguishes evaluation,
feasibility, selection purpose and bounded scientific claims without classes or
mandatory states. Alternative 2 and all seven principles are accepted under
D27–D28, including the boundary with global project interpretation and Nextia.
The [X/Y selectivity case](evaluation_and_selection.md#7-selectivity-case-bind-x-while-avoiding-homolog-y)
compares requirements, checks, evidence and eligibility for three actions. Its
alternative 2 and all seven qualifications are now accepted under D29. The
[multiobjective discussion](multiobjective_optimization.md) advances to concrete
policy effects and alternative optimizers without choosing one. D30 accepts
preserving original objectives/evaluations while separating exploration,
results/tradeoffs and purpose-specific selection. Pareto membership is contextual,
and an archive is optional. The [operational extension](multiobjective_optimization.md#11-operational-stress-test-four-candidates-three-purposes)
compares missing Y, contradictory CPP, a chemical violation and adverse hemolysis
evidence for generation, further evaluation and synthesis/experimental selection.
D31 accepts the scoped-restriction reasoning with seven qualifications: no
reward compensation against applicable required conditions, authorized relaxation,
honest guarantees and valid empty/failed/unresolved outcomes. Concrete policies
and the entire future contract table are not thereby adopted. The
[bounded integrated synthesis](uncertainty_diversity_budget.md) now examines
uncertainty, diversity and budget, finds no unresolved conceptual contradiction
in the current cases. **The investigators have accepted C1–C5 and closed P04
conceptually under D32.** No universal threshold, fitness, confidence scale,
diversity metric, probabilistic model or general decision system is adopted.
Concrete contracts are specified for the capabilities selected next rather than
reopening the general architectural block.

The current task is the [bounded PeptideMT V0.1 proposal](v0_1_scope.md).
**D33 accepts B with A as its first internal increment**. Real generation/redesign,
functional evaluation and reproducible selection constitute the minimum useful
increment 2; genuine feedback is a priority extension conditional on viability.
C structural integration is deferred. Target/family-directed design stays central,
with an explicit priority target milestone after the functional core; target
conditioning does not itself establish recognition. **D34 accepts the first bounded
coverage (AMP compatibility plus adverse hemolysis) and qualification order
(Macrel, then HydrAMP).** No version/checkpoint or deployment is adopted. The
[increment-1 specification](v0_1_increment_1.md) is now **accepted under D35**:
conservative sequence preservation, native output/precision/mapping, both exact
selectors, M1–M8 and provisional canonical single-peptide/<100 operational scope.
Its scientific design is closed within those limits. Actual qualification,
operational conditions and suite admission remain pending. **D36 authorizes
W0–W4**, with the specific central admission issue exception. W0 engineering is
received in [MolSysSuite #146](https://github.com/uibcdf/molsyssuite/issues/146).
W1–W4 retain their scientific acceptance gates and have not been executed here. The
[work order](increment_1_work_order.md) tracks the handoff and required evidence.
H0–H4, package publication and horizon expansion remain outside this assignment.
Normal owning-issue feedback follows [the governance map](governance.md).

De novo generation and redesign remain equally in scope. No first experimental
demonstrator has been chosen. Completion of a computational campaign does not
require demonstrating a complete biological mechanism.

## Repository status

PeptideMT is registered as a primary incubating scientific Python component at
`uibcdf/molsyssuite@8a94e16f1ba26122304df264e89c4eca15afaf5a`. The official
starter is integrated and W0 engineering receiving is complete in
uibcdf/molsyssuite#146 and the expressly authorized uibcdf/peptidemt#1. Routine development uses the
shared `molsyssuite@uibcdf_3.14` environment; member Conda recipes remain clean
qualification fixtures. The [governance map](governance.md) explains normal owning-issue reporting,
authorized internal direct pushes, required PRs and domain owners. Reporting
is not restricted to W0; scientific scope changes and publication retain their
own authorization.
