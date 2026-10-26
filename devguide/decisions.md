# Decisions and discussion history

Navigation: [index](README.md) · [scope](vision_scope.md) · [alternatives](architecture_alternatives.md).
Date of initial record: **2026-10-26**. Approval authority: the investigators.

Updated: **2026-10-26**, including the investigator-directed methodology and
reconsideration of P07 after the expanded functional-family review.

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
| D14 | Scientific design and approval precede implementation of a capability; investigators/ChatGPT/Work lead design, Codex leads later implementation within approved contracts. | Explicit investigator methodology instruction; see [working agreement](design_methodology.md). Major design changes return to discussion. |

The provisional definition in vision_scope.md is adopted only as a **working
formulation for discussion**, not as an immutable scientific or API contract.
Initial MIT licensing and English documentation follow existing suite conventions;
they are repository setup choices, not scientific decisions.

## Accepted conceptual architecture

| ID | Decision | Scope and limits |
| --- | --- | --- |
| D09 | Separate scientific design intent, the computational plan used to address it, and the evidence produced by each execution (alternative B). | Explicit investigator approval on 2026-10-26. No class names, API, serialization, storage or implementation approved. |
| D10 | Functional families remain scientific/computational concepts independent of predictors and generative models. | Minimal family semantics and evaluator bindings remain to be designed. |
| D11 | Distinguish a desired functional property from operational criteria used to select candidates. | A score threshold does not define or establish bioactivity. A scientifically meaningful numerical requirement can still belong to the problem. |
| D12 | Keep family representation initially simple and extensible. | No complex family ontology is authorized. |
| D13 | Simultaneous target- and family-conditioned design remains central, while target-free tasks stay in scope. | Target-free support does not dilute the central joint-design objective. |

The [four worked examples](design_examples.md) are conceptual stress tests and
pending analysis, not selected demonstrators, executed campaigns or additional
accepted architecture. They preserve the approved three-way separation.

## Pending proposals

| ID | Proposal | Decision still needed |
| --- | --- | --- |
| P02 | Define the minimal semantics of an independent functional-family requirement and its evaluator bindings. | Independence is accepted under D10; concrete representation remains open under D12. |
| P03 | Keep a small sequence/design core with optional molecular and model adapters. | Compare dependency cost against uniform molecular integration. |
| P04 | Retain objective vectors, feasibility, applicability and diversity rather than only one scalar reward. | Decide which selection policies are required initially. |
| P05 | Use black-box external optimization and rollout/tree guidance as routes to reuse existing family models. | Select bounded comparison experiments later. |
| P06 | Formal suite admission and official Python starter generation. | Agree the central process; no issue or sibling-registry change is authorized by this initial documentation publication. |
| P07 | Relate potentially incomplete peptide proposals, chemical realizations, representations/feature views, states/conformers/poses and concrete evaluation subjects. | Revised after investigator feedback: compare the [three alternatives](architecture_alternatives.md#p07-reconsidered-proposals-chemistry-views-and-evaluation-subjects), permit early sequence/backbone outputs and qualified evaluation, preserve branching and attribution. No hierarchy, identifiers, state grouping, storage or initial chemical envelope approved. |
| P08 | Explore a simple, extensible functional-concept catalog and source-specific label mappings, broader than CPP/AMP/ACP. | A literature inventory has been added; no fixed ontology, list of supported models, or schema is approved. |

### Proposal disposition

P01 was proposed in the initial publication and **accepted conceptually as D09**
on 2026-10-26. This resolves the architectural choice without approving names,
schemas or implementation. P02's independence principle is accepted as D10;
its minimal semantic contract remains pending.

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
5. At initial publication P01 was only a recommendation. The later explicit
   approval adopts the three-way conceptual separation under D09; names such
   as DesignProblem/ExecutionPlan remain illustrative and unapproved.
6. The original P07 wording started with a chemical candidate and omitted useful
   incomplete proposals. The revised analysis includes sequence/backbone-first
   outputs and distinguishes chemical completion from representation conversion.
   This correction does not adopt a new entity hierarchy or approve P07.

## Discussion update — 2026-10-26

Investigator approval: alternative B plus family independence, the distinction
between functional intent and operational proxies, a simple extensible family
representation, and continued emphasis on joint target/family conditioning.
Updated architecture_alternatives.md, vision_scope.md, roadmap.md, README.md and
open_questions.md consistently. Added design_examples.md to examine three cases,
method substitution, chemical identity, contradictory predictions and traceability.
The audit snapshot is unchanged. No code, development issue or experimental
result is introduced. P07 is a recommendation awaiting approval.

## Additional literature review — 2026-10-26

The investigators requested an expanded survey beyond CPP/AMP/ACP. Added
[functional_families.md](functional_families.md), a source-grounded review of
published 20/21-label multi-label predictors and Xiao et al.'s 15-major/47-label
dataset. Its taxonomies, candidate categories and catalog representation are
**research observations or pending proposals**, not new accepted scientific
architecture or implemented capabilities. No issues or code created.

## Proposal identity and working-method update — 2026-10-26

Reviewed and preserved the investigators' functional-family additions from
repository revision `e3a5e1613b086ccf484e62a6e41883dc343397a3`. The investigators
consider alternative B to have passed its first conceptual test; that is not
empirical validation or approval of the pending refinements.

Reformulated P07 to accommodate incomplete sequence/backbone proposals and
heterogeneous evaluators. Added explicit alternatives and a pending recommendation
in architecture_alternatives.md, the target-free CPP + AMP case and additional
functional probes in design_examples.md. No proposal is required to arrive as a
fully defined molecule; the proposed attribution/realization semantics remain
for discussion. Added the investigator-directed design_methodology.md (D14) and
aligned navigation, scope, roadmap and open questions. P07 and P08 remain pending.
The source-pinned integration audit is unchanged. No scientific code, execution
result, fixed API, selected experiment or development issue is introduced.

## Change protocol

For each consequential discussion update, record date, approval or proposal
status, rationale, affected documents and evidence. Preserve superseded reasoning.
Do not manufacture meeting approvals, experiments, issue numbers or consensus.
Git history provides the document revision record; a more elaborate ADR system
is unnecessary at this stage.
