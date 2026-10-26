# Decisions and discussion history

Navigation: [index](README.md) · [scope](vision_scope.md) · [alternatives](architecture_alternatives.md).
Date of initial record: **2026-10-26**. Approval authority: the investigators.

## Accepted working directions

These are explicit user instructions, not approval of a final architecture.

| ID | Direction | Basis |
| --- | --- | --- |
| D01 | Library name PeptideMT; repository uibcdf/peptidemt; devguide is the design source of truth. | Investigator requests in the design discussion. |
| D02 | Build a versatile computational design tool; practical utility has priority over algorithmic novelty. | Investigator clarification. |
| D03 | Preserve target-directed and target-free family design, multifunctionality, de novo generation and redesign in conceptual scope. | Investigator clarification. |
| D04 | Treat functional families as reusable learned computational knowledge; distinguish predictors, distributions and generation conditions. | Investigator clarification. |
| D05 | A computational campaign can finish without experimental validation; maintain distinct prediction/evidence/activity statuses. | Investigator clarification. |
| D06 | No scientific implementation, fixed API, definitive generator or first experimental demonstrator now. | Investigator clarification. |
| D07 | No development issues without prior agreement; preserve pending proposals locally during this phase. | Investigator instruction. |
| D08 | Reuse existing ecosystem responsibilities and retain audit evidence, uncertainty and alternatives. | Investigator instruction. |

The provisional definition in vision_scope.md is adopted only as a **working
formulation for discussion**, not as an immutable scientific or API contract.
Initial MIT licensing and English documentation follow existing suite conventions;
they are repository setup choices, not scientific decisions.

## Pending proposals

| ID | Proposal | Decision still needed |
| --- | --- | --- |
| P01 | Separate a scientific design problem from its execution plan and run evidence. | Approve the conceptual boundary before choosing class names or schemas. |
| P02 | Represent functional-family concepts independently of predictor/generator implementations. | Define the minimal family semantics and provenance without building an ontology prematurely. |
| P03 | Keep a small sequence/design core with optional molecular and model adapters. | Compare dependency cost against uniform molecular integration. |
| P04 | Retain objective vectors, feasibility, applicability and diversity rather than only one scalar reward. | Decide which selection policies are required initially. |
| P05 | Use black-box external optimization and rollout/tree guidance as routes to reuse existing family models. | Select bounded comparison experiments later. |
| P06 | Formal suite admission and official Python starter generation. | Agree the central process; no issue or sibling-registry change is authorized by this initial documentation publication. |

## Research hypotheses

- H01: learned functional-family knowledge can enrich binder search more efficiently
  than filtering alone under a matched evaluation/computational budget.
- H02: starting from a family-enriched distribution and optimizing target recognition
  can complement starting from a target-conditioned binder generator.
- H03: combining family objectives can discover useful multifunctional candidates
  despite label dependence, multimodality and competing requirements.
- H04: uncertainty/applicability-aware selection can reduce predictor exploitation
  while retaining useful novelty. No universal OOD guarantee is assumed.

## Verified observations

The [integration audit](integration_audit.md) preserves source-level findings.
The [literature review](literature.md) separates primary reports, inspected public
implementations and unimplemented PeptideMT adaptations. No scientific model was
installed, trained, benchmarked or experimentally validated for this repository.

## Superseded recommendations and corrections

1. Earlier assistant wording reduced families to discovery labels. That was
   insufficient: classifiers, learned distributions and conditioning/guidance
   are distinct reusable assets.
2. An earlier framing made complete biological mechanism demonstration central
   to the first campaign. This is not a completion requirement for PeptideMT's
   computational workflows.
3. Redesign of a known binder was recommended as a first demonstrator. The user
   deferred that choice; it must not determine platform boundaries.
4. Protein-target binding is not a universal mechanism for CPP/AMP/ACP/AFP.
5. Proposal P01 is a recommendation only. Recording it does not adopt the
   two-layer alternative or freeze the words DesignProblem/ExecutionPlan.

## Change protocol

For each consequential discussion update, record date, approval or proposal
status, rationale, affected documents and evidence. Preserve superseded reasoning.
Do not manufacture meeting approvals, experiments, issue numbers or consensus.
Git history provides the document revision record; a more elaborate ADR system
is unnecessary at this stage.
