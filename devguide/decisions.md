# Decisions and discussion history

Navigation: [index](README.md) · [scope](vision_scope.md) · [alternatives](architecture_alternatives.md).
Date of initial record: **2026-10-26**. Approval authority: the investigators.

Updated: **2026-10-26**. P07/P08 remain accepted within their limits. P09's four
responsibility owners and three compatibility dimensions are accepted under
D21–D22. Its organization and additional principles remain open after the
expanded protein/peptide-engine review; no algorithm or API is selected.

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
| D10 | Functional families remain scientific/computational concepts independent of predictors and generative models. | P08 refines conceptual semantics under D17; concrete interfaces/bindings remain to be designed. |
| D11 | Distinguish a desired functional property from operational criteria used to select candidates. | A score threshold does not define or establish bioactivity. A scientifically meaningful numerical requirement can still belong to the problem. |
| D12 | Keep family representation initially simple and extensible. | No complex family ontology is authorized. |
| D13 | Simultaneous target- and family-conditioned design remains central, while target-free tasks stay in scope. | Target-free support does not dilute the central joint-design objective. |
| D15 | Adopt P07 alternative III: admit potentially incomplete peptide proposals explicitly related to chemical realizations, representations, molecular states and evaluations. | Explicit investigator approval. Semantic responsibilities only; no mandatory stages, class hierarchy, API or persistence schema. Preserve convergent generation provenance. |
| D16 | Allow evaluations of explicit hypothetical chemical realizations when a method needs information absent from the original proposal. | The plan may branch into several realizations; retain actual inputs, chemistry, assumptions, transformations, model and attribution limits without retroactively completing the original. Computational reuse needs justified equivalence and does not by itself establish scientific transfer. |
| D17 | Adopt P08 alternative 2: a simple extensible catalog of scientific functional concepts explicitly associated with source labels and computational resources. | Functions can lack qualified models; one multi-label predictor remains one resource with multiple outputs. Distinguish scientific relations, database co-annotations and model correlations; retain justified context/provenance without automatic biological implication or a general inference engine. No closed catalog or formal ontology. |
| D18 | Permit justified indirect predictors and exploratory use beyond validated empirical scope to guide generation/optimization. | Keep desired function, actual predicted property, search signal and result evidence distinct. Declare input compatibility, extrapolation limits and whether utility is a hypothesis. Perfect calibration is not required for useful search rankings; scores are not automatically real bioactivity probabilities or comparable across models. |
| D19 | Distinguish guidance/reward/selection roles from candidate assessment and independent evaluation. | One model may serve several roles, but improved reward is not independent confirmation. Preserve direct prediction, indirect/partial support, absent evaluation and doubtful applicability as conceptual distinctions, without a fixed state taxonomy or universal confidence scale. No experimental validation is required for computational completion. |
| D20 | Preserve independent computational capabilities and compatible adapters. | Distinguish predictors, learned distributions, conditioned generators, rewards, search/guidance and datasets/evidence. No common internal representation, differentiability or ML architecture is required; no concrete interface or model selection is approved. |
| D21 | Providers and adapters declare effective capabilities; search strategies define requirements; computational plans select/configure compatible compositions; executions record actual operations, results and limitations. | Explicit conceptual agreement in the P09 expansion request. Responsibilities, not mandatory stages or objects. P09 remains open; no capability schema, API, automatic planner or organizational alternative is approved. |
| D22 | Distinguish operational, runtime/resource and scientific compatibility. | Explicit conceptual agreement in the same request. Technical input acceptance and successful execution do not establish scientific validity. No fixed compatibility taxonomy, scoring rule or admission threshold is approved. |

The [four worked examples](design_examples.md) are conceptual stress tests and
conceptual analysis, not selected demonstrators or executed campaigns. Their
individual targets, chemistry envelopes and plans are not approved architecture;
the semantic responsibilities adopted through P07 are recorded under D15–D16.

## Pending proposals

| ID | Proposal | Decision still needed |
| --- | --- | --- |
| P02 | Refine context, qualified label/resource mappings and evaluator bindings within D10/D17–D20. | Conceptual separation is accepted; concrete fields, mapping policies and interfaces remain open. |
| P03 | Keep a small sequence/design core with optional molecular and model adapters. | Compare dependency cost against uniform molecular integration. |
| P04 | Retain objective vectors, feasibility, applicability and diversity rather than only one scalar reward. | Decide which selection policies are required initially. |
| P05 | Compare and compose filtering, external optimization, sampling-time guidance, functional distributions and learned conditioning through explicit capabilities. | Current [strategy analysis](generative_strategies.md); no definitive generator, common API, capability schema or first comparison experiment selected. |
| P06 | Formal suite admission and official Python starter generation. | Agree the central process; no issue or sibling-registry change is authorized by this initial documentation publication. |
| P09 | Organize capability descriptions and compatible compositions, including general protein engines and composite/external workflows. | D21–D22 accept the responsibility owners and three compatibility dimensions. [Revised alternative B and engine evidence](protein_peptide_design_engines.md#8-revised-p09-recommendation-and-next-approvals) remain recommendations: domain-aware support, optional direct/composite routes and non-transitive access. No schema, contracts, classes, automatic planner or universal API approved. |

### Proposal disposition

P01 was proposed in the initial publication and **accepted conceptually as D09**
on 2026-10-26. This resolves the architectural choice without approving names,
schemas or implementation. P02's independence principle is accepted as D10;
P08 adds conceptual semantics under D17–D20, while concrete bindings remain open.

P07 alternative III is **accepted conceptually as D15**, together with explicit
hypothetical-realization evaluation under D16, after the revised analysis.
This approval includes seven principles: useful incomplete outputs and supported
direct evaluation; explicit hypothetical branching; actual-input/assumption/model
traceability; distinct completion, conversion and redesign; no automatic score
attribution and justified reuse; preservation of convergent provenance; and no
mandatory order of stages. MolSysMT continues to own molecular representation
and manipulation; PeptideMT retains design-specific meaning.

Canonical molecular identity, chemical-state grouping, identifier schemes,
persistence, concrete interfaces and the initial chemical support envelope remain
open. These questions are not silently resolved by P07 or P08.

P08 alternative 2 is **accepted conceptually as D17–D20**, including the
investigators' qualifications. Functions, source definitions and resources stay
distinct, with many-to-many associations and a single multi-label resource's
per-output meaning. Scientific relations differ from co-annotation and learned
correlation. Indirect or extrapolative signals may guide exploratory search with
justification and limitations; their practical utility can remain a hypothesis.
Guide and assessment roles may share a model but cannot turn reward improvement
into independent validation. Direct prediction remains computational evidence;
indirect, unavailable and doubtful-applicability assessments remain distinguishable
without a rigid evidence hierarchy. Computational resource types remain separate.

Approval does not adopt storage, API, classes, a formal ontology, fixed evidence
states, reward policies or definitive models. The new [strategy comparison](generative_strategies.md)
is analysis and pending recommendations under P05, not an approved algorithm.

The investigators endorse retaining the five strategy families as potentially
complementary and establishing simple computational references before comparing
more sophisticated procedures. This does not select an engine or implementation
order. The subsequent P09 expansion request explicitly accepts its four-role
responsibility separation and three compatibility dimensions (D21–D22), while
requiring more investigation before closing the organizational decision.

The dated discussion updates below preserve the status at each revision. Current
approval status is given in the accepted decisions and proposal disposition above.

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
   At that revision this correction did not approve P07. The subsequent explicit
   approval adopts its semantic alternative III under D15–D16, without a hierarchy.
7. The phrase 'capabilities a plan must declare' obscured provider ownership.
   P09 now distinguishes provider availability, strategy requirements, selected
   composition and actual execution. This corrects the discussion without
   treating the proposed organization or its contracts as approved.

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

## P07 approval and P08 discussion — 2026-10-26

The investigators explicitly adopted revised P07 alternative III and hypothetical
realization evaluation with the seven principles above (D15–D16). Updated current
status and limits across the guide; retained the preceding alternatives and dated
pending records as history. The four examples remain illustrative.

Expanded functional_families.md with pending P08 alternatives, qualified relations,
five resource roles and a 21-label sequence-predictor/structural target-generator
integration exercise. Added source-level PrMFTP observations in literature.md;
no model was executed or adapter implemented. P08, selection rules, concrete
interfaces and the explicitly deferred identity/storage questions remain open.
No scientific code, development issue or new demonstrator is introduced.

## P08 approval and generative-strategy discussion — 2026-10-26

Recorded explicit conceptual approval of P08 alternative 2 with the qualifications
in D17–D20. Updated current status across the guide and preserved earlier pending
records as history. Split rewards from search/guidance resource roles; clarified
that uncalibrated rankings and justified extrapolation can aid exploration without
claiming reliable functional evidence. Applicability is not a universal confidence
score or a fixed evidence taxonomy.

Added generative_strategies.md comparing five reusable approaches, actual engine
access, cost/diversity/training requirements and illustrative mathematical search
targets. Extended the literature with FK steering/correctors and bounded source
observations. The existing integration audit remains unchanged. No scientific
code, issues, new model training, executed benchmark or generator selection.

## Capability and composition review — 2026-10-26

Added capabilities_and_composition.md under pending P09: critical assessment of
the four proposed responsibilities, generative/evaluator capability families,
representation-dependent requirements, three compatibility alternatives, a
source-pinned five-model matrix, seven proposed principles and boundaries of
future implementation freedom. Recommended small capability descriptions and
explicit compositions rather than a universal interface or automatic planner.

Rechecked the public HEAD revisions of PepMLM, DiffPepBuilder, PepTune, HydrAMP
and PrMFTP; they match the earlier pinned revisions. Inspected additional source
for trajectory export versus continuation, target-conditioned rewards versus a
conditioned denoiser, and internal generation/filtering policies. All verification
is source-level; no engine was installed or executed. Updated earlier plan-centric
wording and navigation consistently. The ecosystem audit is unchanged. No new
scientific code, development issue, software contract or architecture approval.

## Expanded engines and partial P09 approval — 2026-10-26

Recorded only the investigators' explicit conceptual agreements as D21–D22.
P09 is **not closed**. The proposed architecture/origin-independent but
domain/capability/evidence-aware principle is being investigated, not treated as
an approved contract. Organizational alternative B remains recommended.

Added [protein_peptide_design_engines.md](protein_peptide_design_engines.md):
general and specialized engine matrices, auxiliary-model roles, costs/terms,
source-pinned Chaperone and RFD4 analyses, direct/composite/hybrid alternatives,
the GyrA and GPCR evidence limits, and implications for functional guidance.
Verified native RFD4 search/metric seams separately from differentiable guidance;
no named RFD4 block was observed in Chaperone's inspected inventory. Preserved
the opposite direction and failed quality gates of its peptide-binder example.

Reused the existing MolSysSuite/MolI audit without changing its snapshots.
Updated navigation, strategy/capability discussion, literature and open questions.
No engine was installed or executed, benchmark reproduced, scientific code
implemented, model/demonstrator selected, issue created or pending interface
decision resolved. Provider-reported execution and published experiments are
explicitly attributed to their producers.

## Change protocol

For each consequential discussion update, record date, approval or proposal
status, rationale, affected documents and evidence. Preserve superseded reasoning.
Do not manufacture meeting approvals, experiments, issue numbers or consensus.
Git history provides the document revision record; a more elaborate ADR system
is unnecessary at this stage.
