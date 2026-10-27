# Scientific design and implementation methodology

Status: **investigator-directed working agreement**, 2026-10-26 (D14).
Navigation: [index](README.md) · [decisions](decisions.md) · [questions](open_questions.md).

## Current phase and responsibilities

The general conceptual-design phase has reached P04/P09 closure. The current
task concerns the small capabilities accepted under D33–D35: B, with A first
and real generation/redesign as the minimum useful increment; AMP/hemolysis first,
Macrel then HydrAMP for qualification. The
[increment-1 specification](v0_1_increment_1.md) is scientifically accepted under
D35, including M1–M8 and both selectors. The
[commissioning brief](increment_1_work_order.md) now specifies operational/admission
prerequisites and the proposed executable assignment; avoid reopening broad
architecture without a concrete contradiction. No implementation is authorized
yet. Scientific utility, extensibility and MolSysSuite interoperability guide
choices; an elegant implementation alone is insufficient evidence.

The investigators, ChatGPT and Work formulate scientific problems, research
existing methods, compare alternatives, define requirements and assess risks.
The investigators approve scientific and architectural decisions. Work acts as
a critical scientific collaborator, researcher and design-document maintainer;
its recommendations do not constitute approval.

Codex will lead implementation once the relevant specifications are sufficiently
mature. It may propose improvements, identify incompatibilities and resolve
internal technical choices within approved contracts. A material change to
scientific meaning, architectural boundaries or an approved contract returns to
the investigators' discussion. These are responsibilities, not a prohibition on
technical input during design or scientific input during implementation.

## Progression and review

Discuss consequential choices progressively, using concrete cases and
counterexamples. Record accepted decisions, pending proposals, hypotheses and
open questions distinctly, with rationale, sources and document revisions.
Keep `devguide/` consistent; do not replace discussion with automatic specification
production. Do not create development issues or scientific code in this phase.

Before authorizing a capability's implementation, agree its scientific meaning,
responsibility boundaries, input/output obligations, important failure behavior
and acceptance criteria. Unresolved fundamentals are grounds to continue design.
This does not require settling every future capability or prescribing internal
classes, algorithms, identifiers or storage in advance. Codex retains technical
freedom within the approved contracts.

Review implementations against the previously agreed scientific requirements,
contracts and acceptance criteria, including limitations and unsupported cases.
Technical execution, computational performance and biological validation remain
different claims. Implementation findings can reopen a design question with
evidence; they must not silently redefine the scientific requirement.
