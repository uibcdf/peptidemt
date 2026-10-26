# PeptideMT design guide

Updated: **2026-10-26**. This is the maintained design source of truth.
It supports scientific discussion rather than replacing it with a completed
specification. No scientific implementation or public API is defined.

## Reading path

1. [Scientific vision and scope](vision_scope.md): the current provisional
   definition, boundaries and the computational role of functional families.
2. [Integration audit](integration_audit.md): preserved findings from all eleven
   MolSysSuite repositories and six MolI repositories, pinned to inspected source.
3. [Literature and learned functional spaces](literature.md): primary references,
   public implementations, negative-data caveats and inference-time guidance.
4. [Architectural alternatives](architecture_alternatives.md): three ways to
   represent a design problem and unresolved ownership boundaries.
5. [Preliminary roadmap](roadmap.md): incremental capabilities without selecting
   a definitive model or experimental demonstrator.
6. [Decisions and discussion history](decisions.md): accepted working directions,
   proposals, hypotheses and the correction of earlier recommendations.
7. [Open questions](open_questions.md): prioritized scientific and technical
   decisions for discussion, one at a time.

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

The first architectural question is how to represent scientific design intent
independently of its computational realization, while making functional families
first-class concepts independent of any predictor. See
[alternatives](architecture_alternatives.md) and [Q1](open_questions.md#q1-design-intent-and-execution).

De novo generation and redesign remain equally in scope. No first experimental
demonstrator has been chosen. Completion of a computational campaign does not
require demonstrating a complete biological mechanism.

## Repository status

The repository follows the suite's naming, English documentation, owner-boundary
and evidence conventions. It is not yet registered or qualified as a MolSysSuite
Python component. The central starter procedure and synchronized-policy adoption
are future work requiring agreement; no development issues were opened.
