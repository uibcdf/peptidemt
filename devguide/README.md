# PeptideMT design guide

Updated: **2026-10-26**. This is the maintained design source of truth.
It supports scientific discussion rather than replacing it with a completed
specification. No scientific implementation or public API is defined.

## Reading path

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
6. [Four worked design problems](design_examples.md): scientific intent,
   alternative plans, execution evidence, incomplete proposals and contradictions;
   target-free CPP + AMP and brief probes of additional functional meanings.
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
12. [Capabilities and composition](capabilities_and_composition.md): accepted P09
    owners, compatibility and domain/access principles; pending minimum semantics
    tested with RFD4 rewards, Chaperone workflows and exploratory short-peptide use;
    matching alternatives, original five-model matrix and implementation boundaries.
13. [Protein and peptide design engines](protein_peptide_design_engines.md):
    expanded evidence matrices, Chaperone/RFD4 source review, short-peptide
    benchmarks, optional integration routes and revised P09 recommendations.
14. [Future scientific horizons — V0.2](future_horizons.md):
    long-term peptide engineering, combinatorial libraries, TCR–pMHC design,
    pharmacokinetics, proteolytic transformations, massive screening and
    nontherapeutic applications, with architectural triage and S1–S12 stress tests.

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
comparison references. The current pending discussion is
[P09's capability/composition organization](capabilities_and_composition.md).
Provider availability, strategy requirements, plan selection and actual use are
accepted responsibilities (D21); operational/runtime/scientific compatibility are
accepted dimensions (D22). D23–D24 accept origin-independent, domain-aware support
and optional individual/composite access without inherited internal capabilities.
No mandatory Chaperone dependency or obligation to implement both routes follows.
The organizational alternative, minimum semantic obligations and concrete contracts
remain pending. The [three semantic cases](capabilities_and_composition.md#8-three-tests-of-minimum-capability-meaning)
test fundamental/contextual/optional information and matching alternatives using
the [expanded engine evidence](protein_peptide_design_engines.md). No model,
universal interface or mandatory execution stages are selected.

The [future horizons](future_horizons.md) are strategic research opportunities,
not accepted specifications, a revised implementation roadmap or new mandatory
work before the first useful release.

De novo generation and redesign remain equally in scope. No first experimental
demonstrator has been chosen. Completion of a computational campaign does not
require demonstrating a complete biological mechanism.

## Repository status

The repository follows the suite's naming, English documentation, owner-boundary
and evidence conventions. It is not yet registered or qualified as a MolSysSuite
Python component. The central starter procedure and synchronized-policy adoption
are future work requiring agreement; no development issues were opened.
