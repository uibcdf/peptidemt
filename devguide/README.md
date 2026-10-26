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
   verified 20/21/47-label precedents, a broadened function map, and catalog proposals.
4. [Literature and learned functional spaces](literature.md): primary references,
   public implementations, negative-data caveats and inference-time guidance.
5. [Architectural alternatives](architecture_alternatives.md): alternative B
   accepted conceptually; revised P07 alternatives for proposals, chemistry and evaluations.
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
functions; its catalog proposal has not been approved as an ontology or API. The next proposed
decision concerns incomplete proposals, chemical realizations, representations,
states and the concrete subject of evaluation;
see [Q3](open_questions.md#q3-candidate-chemistry-and-representation). This proposal
does not approve an API, identifier syntax or initial chemistry support envelope.

De novo generation and redesign remain equally in scope. No first experimental
demonstrator has been chosen. Completion of a computational campaign does not
require demonstrating a complete biological mechanism.

## Repository status

The repository follows the suite's naming, English documentation, owner-boundary
and evidence conventions. It is not yet registered or qualified as a MolSysSuite
Python component. The central starter procedure and synchronized-policy adoption
are future work requiring agreement; no development issues were opened.
