# Decisions and discussion history

Navigation: [index](README.md) · [scope](vision_scope.md) · [alternatives](architecture_alternatives.md).
Date of initial record: **2026-10-26**. Approval authority: the investigators.

Updated: **2026-10-27**. P07/P08 remain accepted within their limits. P09 is
**resolved conceptually** under D21–D26: alternative B, all seven principles and
context-sensitive semantic obligations are accepted. Concrete contracts,
interfaces, schemas and implementation remain deferred. A bounded V0.2 horizon
review proposes a collective-design distinction without adopting it; P10 remains
pending by explicit request. P04 alternative 2 and its seven minimal principles
are accepted under D27, with the MOLI interpretation boundary under D28. P04
now also accepts the X/Y requirement/check/evidence separation under D29 and
distinct search, preserved results/tradeoffs and purpose-specific selection
under D30. D31 now accepts scoped restrictions, provisional exploration,
uncheckable requirements and contextual Pareto results with seven qualifications.
**P04 is now closed conceptually under D32**, accepting C1–C5 on the basis of
D27–D31. Concrete capability contracts/interfaces remain pending; no universal
algorithm, fitness, uncertainty scale or diversity metric is adopted. General
conceptual design now gives way to [V0.1 scope](v0_1_scope.md): **B is accepted
under D33**, with A as its first internal increment, real generation/redesign as
the minimum useful increment and feedback as a priority conditional extension.
Target-directed capability follows the first functional core as an explicit
priority; C remains a later option. **D34 accepts AMP compatibility plus adverse
hemolysis as the first bounded coverage, with Macrel then HydrAMP as qualification
candidates.** D35 now accepts the conservative sequence-preserving Macrel contract,
both reference selectors and M1–M8, closing increment 1's scientific design within
its provisional chemistry/length scope. Real qualification, operational conditions,
suite admission and operational execution remain to qualify. **D36 authorizes
W0–W4**, with W1 conditional on completed W0 and the specific central admission
issue exception. W0 has started in [MolSysSuite #146](https://github.com/uibcdf/molsyssuite/issues/146);
central acceptance/publication and the official starter are not yet complete.
See the [authorized work order](increment_1_work_order.md).

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

Earlier rows' statements that P04 remained open describe their approval stage.
D32 closes that conceptual question without retroactively changing those decisions.

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
| D21 | Providers and adapters declare effective capabilities; search strategies define requirements; computational plans select/configure compatible compositions; executions record actual operations, results and limitations. | Initially approved as responsibilities, not mandatory stages or objects. D25–D26 subsequently resolve P09's conceptual organization; no schema, API or automatic planner is approved. |
| D22 | Distinguish operational, runtime/resource and scientific compatibility. | Explicit conceptual agreement in the same request. Technical input acceptance and successful execution do not establish scientific validity. No fixed compatibility taxonomy, scoring rule or admission threshold is approved. |
| D23 | Admit design engines independently of their original architecture/purpose, with explicit chemical/scientific domains, effective capabilities and access-route evidence. | Explicit investigator approval following the expanded review. Associate support with an identifiable engine, version, checkpoint, adapter, configuration and conditions of use; a short-peptide input is not validated short-peptide design. PeptideMT's peptide-design scope is unchanged. No declaration schema or initial chemistry envelope is approved. |
| D24 | Permit individual and composite providers, with native, adapted or explicitly composed capabilities; distinguish underlying operations from actually exposed access. | Internal capabilities are not automatically inherited through workflows, services or adapters. Chaperone is an optional workflow/execution provider, not a mandatory dependency or replacement for PeptideMT's scientific responsibilities. Direct access to generative internals remains conceptually possible; no obligation to implement both adapter routes, export all states, reimplement engines or adopt concrete contracts. |
| D25 | Adopt P09 alternative B: small optional capabilities, evidence-linked semantic declarations and explicit compositions, including all seven principles in capabilities_and_composition.md. | Explicit investigator approval closes P09's conceptual organization. Preserve information/preservation meaning, optional specialized access, three compatibility dimensions, explicit mismatches/substitutions, provenance/attribution and ecosystem ownership. No Python interfaces, classes, schemas, registries, automatic composition or scientific implementation approved. |
| D26 | A capability declaration must justify the concrete use without a universal field inventory; distinguish fundamental, contextual and optional information. | Explicit investigator approval. Unknown restrictions do not demonstrate support. Required operations must actually be established; scientific uncertainty can permit justified exploration but cannot replace missing operations. Detailed attributes/checks are specified with particular implementable capabilities rather than reopened as separate conceptual approvals. |
| D27 | Adopt P04 alternative 2 and all seven minimal principles in evaluation_and_selection.md: evaluation, feasibility knowledge, purpose-specific selection and bounded scientific claims have distinct meanings. | Explicit investigator approval. No four classes/services/stages, state machine or mandatory global grade. Selection is purpose-relative; strictness and checkability are independent; preserve established violations, cutoff failures, missing/failed evaluations, contradiction and applicability limits without universal penalties. Retain original evidence, policies, operational criteria and selection reasons; different policies can address the same problem without rewriting results. P04 remains open for concrete restrictions and optimization/selection policies. |
| D28 | PeptideMT retains evaluations, selection grounds and computational conclusions scoped to their evidence; it is not a general scientific-interpretation or project-claim management engine. | Explicit investigator qualification of D27. Global interpretation and project decisions belong to investigators and, eventually, appropriate MOLI components, especially Nextia. This boundary must preserve scientifically interpretable native results; no dependency on a currently implemented Nextia runtime or automated claim adjudicator is approved. |
| D29 | Adopt X/Y alternative 2: distinguish scientific requirements, operational checks and explicit evidence links for assessing compliance, with all seven investigator qualifications. | Requirements exist independently of available evaluators. An exact score predicate is not an exact biological check. Preserve original subjects, representations, conditions, models, uncertainty and provenance. Many-to-many evidence links imply no automatic sufficiency. Distinguish favorable, adverse, contradictory, insufficient and absent evidence without a universal state scheme. Eligibility is action/policy-specific; absent Y evidence is not demonstrated selectivity. Comparisons respect meaning, units, conditions and domains; structural scores are not arbitrarily converted to affinities or selectivity ratios. No universal thresholds, rejection rules, Python classes or formal constraint engine. P04 remains open for optimization and selection. |
| D30 | Preserve original objectives and evaluations, and permit different optimization, exploration and selection policies on the same scientific problem. Distinguish generation/exploration, evaluated results/tradeoffs and selection for a concrete purpose. | Explicit investigator approval. Scalar search may coexist with nondominated results and a different subsequent selector, without redefining scientific intent. No universal algorithm, fitness or mandatory Pareto archive. Nondominance is derived relative to objectives, evaluators, contexts, comparable candidate subset and evidence snapshot, not an absolute scientific property. Preserve original evaluations, actually explored/observable sets, qualified derived fronts and action-specific selections distinctly; no fabricated scores for incomplete/incompatible/pending results. Compensatory exploration does not authorize compensation against every scientific restriction. Treatment of restrictions, uncertainty, diversity and budgeted policies remains open under P04. No API, classes or persistence schema approved. |
| D31 | Accept the proposed conceptual treatment of scoped restrictions, provisional exploration, uncheckable requirements and contextual Pareto results, with all seven investigator qualifications. | Scope belongs to problem/procedure/action, not a permanent candidate classification. Required conditions within an operation cannot be compensated by reward. Solution-acceptance requirements may differ explicitly and justifiably from exploratory criteria. Provisional relaxations need authorization and scope without silently changing science. Guarantees require actual operations/evaluators; checking final candidates does not establish all internal states' compliance. Empty selections, failed evaluations and inability to establish a requirement can be valid reported outcomes, without making failures successful predictions. Fronts are relative derived results retaining original evaluations and comparison provenance. No universal restriction policy, fitness, algorithm or implementation interface; P04 remains open. |
| D32 | Adopt all five C1–C5 principles and close P04 conceptually on the basis of D27–D31 and the agreed qualifications. | Explicit investigator approval. Preserve specific uncertainty meanings/dependencies without a universal confidence scale or unjustified aggregation; optional purpose/view-relative diversity; distinct score/diversity/uncertainty/decision-impact acquisition grounds; honest estimated/observed cost, failures, reuse and observability; reward optimization distinct from activity evidence with model bias/limitations retained. No particular algorithm, universal uncertainty policy, diversity metric, probabilistic model or general decision system. Concrete contracts/interfaces are specified for the selected capabilities. V0.1 capability/model/demonstrator selection and implementation remain unapproved. |
| D33 | Adopt B as PeptideMT V0.1's conceptual direction, using A as the first internal increment. A real generation/redesign route, real qualified functional evaluation and reproducible selection constitute the minimum useful second increment; simulated-only demonstrations do not suffice. | Explicit investigator approval. Retain supplied-proposal evaluation, all evaluations/failures and explicit policies. Functional feedback that changes later proposals/parents/edits/allocation is a priority third increment, with exact inclusion conditional on actual generator viability; postfiltering alone is not feedback. Joint target/family design stays central; initial target-free work is allowed without requiring recognition assessment or structural generation. Target-directed capability is an explicit priority after the first functional core. C is deferred, not rejected. Preserve target context/actual conditioning and distinguish conditioning, compatibility and independent recognition. No engine, initial family subset, chemistry, API, deployment or implementation is approved. Review applicable resource terms, particularly PepMLM's additional access commitments; Work-shell checks are not laboratory audits. |
| D34 | Adopt AMP compatibility as the desired function and hemolysis as the adverse property for the first bounded V0.1 coverage; qualify Macrel first and HydrAMP second. | Explicit investigator approval on 2026-10-27. Preserve predictive/native meanings; neither score is measured antimicrobial activity, percent hemolysis or safety. Core responsibilities stay independent of these functions/resources. Qualification order does not select a version/checkpoint or establish execution, applicability or permission. The initial HydrAMP de novo candidate uses filter_out=False, n_attempts=1 and bounded proposal count, retaining conditioning, internal scoring/order, external Macrel evaluation and PeptideMT selection distinctly. Do not require Python 3.8 in the main host; assess isolation if needed. No implementation/installation/issues authorized. Chemistry/lengths, preprocessing policy, exact selectors, fixtures, concrete interfaces and qualification acceptance remain to approve. |
| D35 | Approve increment 1's scientific Macrel contract and M1–M8, including strict sequence preservation, both exact reference selectors and provisional single-peptide canonical-symbol/<100-residue operational scope. Close its scientific design within those limits, subject to actual provider qualification and indispensable operational decisions. | Explicit investigator approval on 2026-10-27. Leading-M originals remain valid proposals but incompatible with a native route that clips them. Derived-clipped and unchanged-sequence feature routes are deferred and need separate qualification; AMP training also uses native normalization. Preserve per-occurrence correspondence, negatives, both scores, labels/categories, precision, evidence/provenance, original chemistry/unknowns and explicit empty/unavailable/failed/anomalous outcomes. AMP-descending/Hemo-ascending or Hemo-ascending/AMP-descending ordering uses original occurrence as final tie; neither is biological acceptance, safety, selectivity or synthesis approval. No universal fitness/cutoffs or empirical validation of every <100 length. H0–H4 remains a suitable proposal, not execution permission or definitive HydrAMP adoption; retain the stated native candidate/isolated legacy-runtime boundary. No implementation, installation or issues authorized. Prepare the bounded commissioning/admission brief; actual bundles, terms, environment/budget and execution evidence remain pending. |
| D36 | Authorize W0–W4 within D35 and M1–M8, starting formal admission. Propose primary scientific-component/incubating/active/python-package classification, subject to central acceptance. W1 starts only after W0 completes correctly. | Explicit investigator authorization on 2026-10-27. Allow the necessary central admission issue if none exists, as a specific exception to the no-issues rule; no general development-issue authority. Name the responsible owner and preserve ecosystem boundaries. Use accepted published central registration, immutable policy and genuine admission SHA when required, official starter in an empty temporary target and reviewed preservation of existing content/history. Core works without Macrel; one real Macrel 1.6.1 qualification candidate on Linux CPU/Python 3.14 must resolve and execute both ONNX models, with assets/terms/fixtures/effective limits identified first. Native integration cannot pass on mocks/skips or reduced criteria. Codex owns routine internal implementation; scientific changes return to review. No HydrAMP, increments 2/3, target-conditioned generation, new scientific models, package publication or new architecture. Delivery requires identifiable commit, admission and package/model evidence, and executed M1–M8 with engine-free/live distinctions; partial work remains partial. |

The [four worked examples](design_examples.md) are conceptual stress tests and
conceptual analysis, not selected demonstrators or executed campaigns. Their
individual targets, chemistry envelopes and plans are not approved architecture;
the semantic responsibilities adopted through P07 are recorded under D15–D16.

## Pending proposals

| ID | Proposal | Decision still needed |
| --- | --- | --- |
| P02 | Refine context, qualified label/resource mappings and evaluator bindings within D10/D17–D20. | Macrel increment-1 scientific meanings/bindings are accepted under D35; concrete encodings/interfaces and other resources remain open. |
| P03 | Keep a small sequence/design core with optional molecular and model adapters. | Compare dependency cost against uniform molecular integration. |
| P05 | Compare and compose filtering, external optimization, sampling-time guidance, functional distributions and learned conditioning through explicit capabilities. | Current [strategy analysis](generative_strategies.md); no definitive generator, common API, capability schema or first comparison experiment selected. |
| P06 | Formal suite admission and official Python starter generation. | W0 authorized under D36; accepted registration published at 8a94e16f. Official starter integrated; component qualification and central receiving remain pending in uibcdf/molsyssuite#146 and uibcdf/peptidemt#1. |
| P10 | Distinguish collective/distributional library proposals from individual molecular proposals, including incomplete individuals. | Pending bounded recommendation from [V0.2 case A](future_horizons.md#9-bounded-extensibility-review-after-p09-approval). No library support, generic population hierarchy or MVP requirement adopted; concrete semantics can wait until such a capability is prioritized. |

The [V0.1 direction is accepted under D33](v0_1_scope.md), D34 fixes first coverage/
qualification order, and D35 closes increment 1's scientific contract including
M1–M8. The [work order](increment_1_work_order.md) is authorized under D36, with W0
started and W1–W4 gated on its completion. Exact bundles/permissions, operational
limits, central acceptance/publication and actual qualification remain pending;
do not repeat the scientific/architectural approval. Later feedback is outside scope.
P02/P03/P05/P06 need only the selected capability-specific portions; P10 and future
horizons add no requirement. Earlier unapproved A/B/C records below are history.

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

The next explicit approval adopted the domain-aware, origin-independent principle
and its eight qualifications as D23–D24. It preserves optional direct/internal
and composed-workflow use without requiring both implementations. At that stage
P09 remained partially open: the investigators requested minimum capability meaning,
not adoption of the proposed information list as a mandatory schema. Small
optional capabilities with explicit compositions were the preferred pending
organization; no general planner or duplicate MOLI orchestration was requested.

P09 is now **resolved conceptually as D25–D26**, adopting alternative B and all
seven principles within the previous limits. Fundamental/contextual/optional
information distinctions and sufficient evidence for actual required operations
are accepted without approving every illustrative table entry as a mandatory
field. P09 is not left open merely because concrete software contracts remain
unwritten. Those contracts, representations, identifiers, schema/registry details,
deployment and capability-specific checks belong to later specifications under
the accepted organization; P07's chemistry/identity deferrals also remain open.

The bounded library/state/transformation review is design analysis, not a new
accepted architecture. Only the collective-versus-individual distinction is
proposed as P10. No new top-level architecture is recommended for state panels
or precursor/product relationships. None of these horizons becomes an MVP gate.

P04 is **closed conceptually under D27–D32**. Alternative 2 and all seven minimum
principles are accepted with purpose-relative selection, independent strictness/
checkability, preserved evidence and bounded interpretation.
The X/Y requirement/check/evidence alternative 2 is now explicitly accepted under
D29, with its seven qualifications and no software representation selected.
D30 accepts preserving objectives/evaluations and separating search, results/
tradeoffs and action-specific selection; no mandatory Pareto archive follows.
D31 accepts the operational case's scoped-restriction reasoning and all seven
investigator qualifications. It does not adopt every illustrative policy or the
whole proposed contract table. The [bounded synthesis](uncertainty_diversity_budget.md)
proposed five additional principles and closure; both are now explicitly accepted
under D32. C1–C5 retain their labels as subordinate principles, not five new decision
IDs. P04 is not left open because concrete interfaces or algorithms remain unwritten.
Those choices belong to capability specifications, now narrowed to the V0.1
direction accepted under D33. No optimizer, numerical policy, interface or
implementation is adopted.
No later policy can retroactively convert a missing assessment into established
compliance or selection into validated activity.

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

## Domain-aware approval and minimum-semantics discussion — 2026-10-26

Recorded explicit approval as D23–D24, including configuration-qualified support,
non-inherited internal operations, optional Chaperone and conceptually available
direct integration. Preserved the earlier review's dated pending status as history.
Updated the engine review's current disposition, guide index, README, alternatives,
strategy discussion and open questions consistently.

Expanded capabilities_and_composition.md with pending fundamental/contextual/
optional information distinctions; RFD4/external-evaluator, opaque Chaperone and
short-peptide extrapolation cases; alternatives for expressing/matching support;
and investigator versus future implementation decisions. Distinguish native
delegated reward search from PeptideMT-controlled branching: only the latter
necessarily needs externally exposed state-control operations. A record's syntax
and schema remain open, as do P07's explicit chemistry/identity deferrals.

Reused the immutable engine/ecosystem evidence and rechecked selected metric,
search, block and result-schema sources. No model installation/execution,
scientific implementation, benchmark reproduction, issue or selected demonstrator.
The semantic recommendation itself awaits approval.

## Future scientific horizons — exploratory addition, 2026-10-26

At the investigators' request, added [future_horizons.md](future_horizons.md)
as an opportunity inventory and a set of conceptual stress tests: advanced peptide
chemistry, conformational/state-selective design, negative targets, mechanism,
delivery, synthesis/developability, active learning, activatable/multifunctional
constructs, functional atlases, natural-peptide mining and multifidelity evaluation.
This material is **not an accepted decision, fixed roadmap, implementation scope,
new selected demonstrator or additional precondition to a useful MVP**. Current
P09 discussion continues; any core distinction uncovered by stress tests requires
independent scientific discussion and explicit approval. No code or issues created.

## P09 conceptual closure and bounded horizon review — 2026-10-26

Recorded explicit approval of alternative B, all seven principles and the
context-sensitive information obligation as D25–D26. Removed P09 from pending
conceptual proposals and separated concrete contracts/interfaces from that
resolved choice. Retained earlier partial-approval records as dated history.

Before editing, fetched and fast-forwarded through the investigators' GitHub
changes to `e28fbd3`; read future_horizons.md V0.2 and S1–S12. Preserved that
inventory and added a bounded review of implicit combinatorial libraries,
multi-state/antitarget design and precursors/transformation products. Proposed
P10 only for collective-design meaning; no class hierarchy or library feature
was adopted. State panels fit the existing separation; transformation relations
need explicit meaning without becoming a universal reaction engine.

Proposed a progressive P04 discussion beginning with evaluation meaning and
feasibility/evidence, then tradeoffs, uncertainty, diversity and budgeted selection.
No P04 choice is approved by that proposed order. Updated related current-status
documents consistently, without changing the ecosystem/engine audit snapshots,
selecting a demonstrator, implementing scientific code or opening issues.

## P04 evaluation and purpose-specific selection discussion — 2026-10-26

The investigators concur with P09's closure and the horizon review, explicitly
retaining P10 as pending without a library-design MVP requirement. They request
conceptual P04 analysis and further approval before adopting its recommendations;
no D27 or new accepted evaluation/selection bundle is recorded.

Added [evaluation_and_selection.md](evaluation_and_selection.md), comparing direct
selection-specific checks, four explicit semantic responsibilities and a general
decision framework. Recommended the middle approach without four classes/stages,
a global candidate grade or a general decision engine. Compared strict violations,
operational cutoffs, missing/failed evaluation, conflicting predictions and
out-of-domain signals. The A/B/C cases preserve that more complete evidence need
not be favorable, disagreement need not be comparable, and selection alone
adds no functional evidence.

Proposed seven minimal P04 principles for discussion, not approval, and separated
fixed-evidence policy comparison from end-to-end search comparison. Reused the
pinned ecosystem audit; no new runtime capability or empirical result is claimed.
Updated navigation, current discussion and related family/evaluation guidance.
No scientific code, model execution, development issue or selected experiment.

## Partial P04 approval and X/Y selectivity discussion — 2026-10-26

Recorded explicit adoption of alternative 2 and its seven principles as D27,
with the investigators' global-interpretation/Nextia boundary as D28. P04 remains
open for the requested later choices. Retained the earlier pending analysis as
dated history; no selector, API or threshold follows from the approval.

Extended evaluation_and_selection.md with a hypothetical binder for X avoiding
homolog Y: scientific scope independent of evaluators; exact computational checks
versus biological estimation; affinity/structural/proxy meanings; missing Y,
discordance and noncomparability; three selection purposes; and three alternatives
for representing requirements, checks and compliance evidence. Recommended their
linked semantic separation, still pending, without classes or a constraint engine.

Qualified equilibrium-affinity comparison using IUPAC terminology, checked
Boltz-2's documented output/domain limits at the existing audit pin and used NIST's
measurement distinction only as a general conceptual anchor. No new engine was
selected, installed or executed; no peptide sequence, target structure or experiment
was produced. Updated related current-status documents. No scientific code or issues.

## X/Y semantic approval and multiobjective discussion — 2026-10-26

Recorded the investigators' explicit approval of X/Y alternative 2 and all seven
qualifications as D29. Requirements, operational checks and evidence links have
distinct meanings; no classes, universal status scheme, thresholds, rejection
rule or constraint engine follows. Earlier dated pending recommendations remain
history. P04 stays open for optimization and selection.

Added [multiobjective_optimization.md](multiobjective_optimization.md) for the
X-recognition/Y-avoidance/CPP/hemolysis case: weighted utilities, Pareto archives,
hierarchical and constrained policies, uncertainty without compulsory calibrated
probabilities, diversity and cost. Invented candidates expose different choices,
missing/noncomparable results and a chemical-check violation. Verified their
arithmetic separately; these are not scientific data or executed model outputs.
Distinguished search, evaluation acquisition, survival and final action selection;
proposed fixed-evidence and end-to-end comparisons without choosing a policy.

Consulted primary NSGA-II, MOEA/D, scalarization and Bayesian multiobjective papers;
their generic algorithms do not establish peptide-domain effectiveness. Reused
the pinned ecosystem and engine audits without changing their source snapshots.
Updated navigation and current-status documents consistently. No scientific
software, model execution, benchmark reproduction, experiment or development issue.
All new optimization recommendations remain pending investigator discussion.

## Search/results/selection approval and operational case — 2026-10-26

Recorded explicit conceptual approval as D30: preserve original objectives and
evaluations while permitting different exploration/optimization and purpose-specific
selection policies on one scientific problem. Included the investigators' limits:
no universal fitness/algorithm, no compulsory Pareto archive or absolute candidate
Pareto status, and no invented missing scores. P04 remains open for restriction
handling during exploration, uncertainty, diversity and policies under budget.

Extended [multiobjective_optimization.md](multiobjective_optimization.md) with
scope-dependent search invariants, final-solution requirements, temporarily relaxed
operational criteria and scientifically unresolved requirements. These are roles
for a particular use, not a universal restriction taxonomy. An uncheckable strict
requirement cannot silently become satisfied, violated or deleted; a plan cannot
promise verified enforcement without the needed means.

Reused invented A/F/H and added invented I with aligned but opposing CPP
assessments. Compared continued generation, additional computational evaluation
and synthesis/experimental selection under explicit alternative purposes. Kept
the prior incompatible-Y case G distinct. Illustrated how expanding a comparable
pool changes nondominance without rewriting old evidence. Added pending scientific
obligations for future components and investigator versus implementation choices,
without signatures, storage or classes. Prioritized uncertainty, then diversity,
as subsequent discussions; neither is resolved by this update.

Reused the existing literature and pinned ecosystem/engine evidence; no new model
support, installation, runtime behavior, biological result or benchmark is claimed.
Updated related navigation/status documents and checked documentation consistency
and invented dominance arithmetic. No scientific implementation or issues.

## Scoped-restriction approval and bounded P04 closure proposal — 2026-10-26

Recorded explicit approval as D31 with all seven qualifications, including honest
internal-versus-final guarantee scope and valid empty/failed/unresolved execution
outcomes. Kept earlier pending analyses as dated history; no universal restriction
policy or complete contract table is inferred from this approval.

Added [uncertainty_diversity_budget.md](uncertainty_diversity_budget.md): seven
sources/limits of uncertainty, nonprobabilistic versus probabilistic techniques,
F/I counterexamples, shared bias/reward exploitation, seven diversity meanings
across four uses, decision-relevant acquisition and resource/reuse/observability
accounting. Allocation numbers are invented, not benchmark costs. Consulted
primary Ovadia, COMs, CbAS and PESMO papers; no general algorithm is selected or
peptide integration/runtime qualification claimed.

The document synthesizes D27–D31, recommends five explicitly pending principles
(C1–C5), separates later capability contracts from algorithm alternatives and
checks the current cases for conceptual contradictions. It formally proposes
P04 closure without recording it as approved. P04 remains open awaiting investigator
approval; V0.1 capability selection/contracts/cases/acceptance are the next proposed
milestone, not an implemented or frozen scope. No future-horizon expansion.

Updated current statuses and navigation consistently, retaining pinned ecosystem
audits and the investigators' horizon inventory. No scientific implementation,
model execution, benchmark reproduction, experimental protocol or development issue.

## P04 conceptual closure and PeptideMT V0.1 alternatives — 2026-10-26

Recorded explicit adoption of C1–C5 and conceptual P04 closure as D32. Removed P04
from pending conceptual proposals and updated current dispositions, retaining
earlier pending records as dated history. Concrete contracts/interfaces remain
capability-specific, not grounds for another broad conceptual round. No universal
algorithm, probabilistic model, uncertainty policy or diversity metric follows.

Added [v0_1_alternatives.md](v0_1_alternatives.md): A external-proposal assessment,
B real sequence generation/redesign plus functional knowledge, and C structural
generation; scientific/resource/terms comparisons, minimum contracts, meaningful
acceptance cases and the V0.1 portions of P02/P03/P05/P06. Recommended A as an
internal slice of B, not the whole useful generative product, with a bounded
feedback extension distinguished from postselection. No alternative, mandatory
model, chemistry envelope or first demonstrator is selected. P10 stays deferred.

Reused the pinned structural/ecosystem audits. Targeted source refresh confirmed
PepMLM/HydrAMP/PrMFTP snapshots unchanged; inspected Macrel at 8c1f7321 and the
official HydrAMP starter kit at 7804df86. Recorded native filtering/precision,
sequence versus recognition meaning, code/checkpoint/data terms and legacy
environment limits. Official PepMLM model-card metadata and additional conditions
remain unresolved for adoption; no access terms accepted or weights downloaded.

A read-only local interpreter/dependency/driver inspection establishes only the
reported shell state, not CPU/GPU model qualification or absence of other machines.
No scientific model was installed or run, no benchmark reproduced, no scientific
code implemented and no issue created. Documentation checks do not establish
runtime or biological validation. General conceptual design moves to bounded
V0.1 capability selection and specifications under D14.

## V0.1 B approval and bounded implementation proposal — 2026-10-26

Recorded the investigators' approval as D33, including A as increment 1, real
generation/redesign plus functional assessment as the minimum useful increment 2,
and genuine feedback as a priority conditional increment 3. C is deferred; joint
target/family design remains central with an explicit target-directed milestone
after the first functional core. No engine, chemistry, API or implementation is
adopted. Preserved the earlier alternatives/recommendation as dated reasoning.

Added [v0_1_scope.md](v0_1_scope.md): bounded candidate feasibility, proposed AMP/
hemolysis coverage, increment contracts, failure/acceptance behavior, controls,
shared-data/bias limitations, owner boundaries and the remaining approval sequence.
Macrel and a bounded HydrAMP route are candidates to qualify, not selected models.
Rechecked the existing source pins and official PepMLM model-card conditions;
inspected HydrAMP's native/starter quota loops and finite-batch alternative,
starter training provenance, and Macrel's training/export source. Exact cross-model
training overlap is unknown, not inferred from Macrel's internal overlap comment.
No new field-wide survey or laboratory hardware audit was undertaken.

Updated navigation, current statuses, roadmap and open questions. This is source/
metadata/documentation work only: no provider installation/execution, checkpoint
download, access agreement, scientific implementation, issue or runtime qualification.
The proposed acceptance tests are future work; documentation checks cannot pass them.

## AMP/hemolysis coverage and increment-1 specification — 2026-10-27

Recorded explicit investigator approval of the bounded scientific coverage and
Macrel-then-HydrAMP qualification order as D34. The HydrAMP de novo configuration
is the initial qualification candidate, not a selected checkpoint or runtime.
Added [v0_1_increment_1.md](v0_1_increment_1.md): input/view/chemistry/length
obligations; all native outputs, precision, negatives and per-occurrence mapping;
two exact proposed selectors; M1–M8 acceptance cases; H0–H4 bounded HydrAMP gates;
resource adoption/reconsideration criteria; controls and owner/extension boundaries.
These contracts and test budgets remain proposed, not approved implementation.

Rechecked unchanged source pins, normalization, feature/prediction calls, native
tests and dataset preparation. Newly documented native removal of initial M and
terminal stop, header truncation, the <100 stated scope versus >=110 warning,
unestablished empirical lower-length bound, and token/string attribution limits
in HydrAMP. Recommended sequence-preserving admission to the first Macrel route;
alternatives for leading-M inputs require a scientific choice. Read the primary
HemoPI paper and distinguished Swiss-Prot-sampled negatives from experimentally
demonstrated absence of hemolysis. Cross-resource training overlap remains unknown.

Aligned current coverage/status/navigation without rewriting older dated approvals.
Read central suite/optional-engine guidance; formal admission and route qualification
remain future work. No model was installed/run, no weights downloaded, no issue or
scientific implementation created. Documentation checks do not execute M/H gates.

## Increment-1 scientific closure and commissioning preparation — 2026-10-27

Recorded D35: explicit acceptance of the conservative preprocessing policy,
Macrel scientific contract, both reference selectors and M1–M8, with provisional
single-peptide canonical-symbol/<100 scope and no fabricated chemistry or empirical
length guarantee. Deferred clipped-derivative and unchanged-feature alternatives;
retained H0–H4 as an appropriate proposal without execution permission. Approved
science does not establish installed execution, rights, admission or implementation.

Added [increment_1_work_order.md](increment_1_work_order.md): fixed scope, operational
prerequisites, a draft central classification/admission route, non-destructive
starter integration, W0–W4 deliverables, engine-free versus real-provider tests,
Codex discretion/review boundaries and the evidence required for acceptance.
The work order is ready for explicit authorization, not an executed assignment.

The bounded final review confirmed PeptideMT absent from central suite.toml at
14b2e74c; checked official starter/refusal of nonempty destinations and separate
immutable policy/admission route. Published policy-v1.5.10 resolves to 1c38d503.
Confirmed official Macrel v1.6.1 release/tag (19046260); three key source blobs match
the prior audit, without claiming installer/asset equality or installed execution.
No model survey, central registry edit, issue, package bootstrap, installation or
scientific implementation was performed. Updated current statuses without rewriting
older dated decisions; documentary checks do not execute M/H acceptance gates.

## W0–W4 authorization and formal admission initiated — 2026-10-27

Recorded D36: the investigators authorize W0–W4 within D35/M1–M8, starting W0
and gating W1 on actual completed admission/bootstrap. The permitted issue
exception is limited to necessary central admission, not general development
reporting. Scientific scope changes, other models, HydrAMP/increments 2–3/target
generation, package publication and new architecture remain excluded.

No existing appropriate admission issue was found; opened
[uibcdf/molsyssuite#146](https://github.com/uibcdf/molsyssuite/issues/146), identifying
Diego Prada-Gracia (UIBCDF) as accountable owner and preserving ecosystem boundaries.
Submitted registration and truthful pending review/inventory records in
[PR #147](https://github.com/uibcdf/molsyssuite/pull/147), candidate commit
`b652fc9a24158f0ae46c66e70a9b698ca0c2546e`. Central acceptance and publication
remain pending; this candidate is not an admission SHA and has not been used
to generate a PeptideMT starter.

Central offline governance and administrative publication controls pass; full
governance tests passed (544 tests, one documented opt-in Mamba skip) in isolated
Python 3.14.4. The focused 161-test Conda Python 3.14.7 run passed; a full shared-
environment run exposed unrelated dependency conflicts, preserved rather than
silently repaired. No scientific provider/model was installed or executed, no
M1–M8 qualification is claimed and W1 has not started. Hosted PR evidence is
separate. Updated working instructions and current handoff status for D36.

## Change protocol

For each consequential discussion update, record date, approval or proposal
status, rationale, affected documents and evidence. Preserve superseded reasoning.
Do not manufacture meeting approvals, experiments, issue numbers or consensus.
Git history provides the document revision record; a more elaborate ADR system
is unnecessary at this stage.

## Accepted central registration and component W0 receiving — 2026-10-27

Central maintainers accepted and published registration through PR #147 at
`8a94e16f1ba26122304df264e89c4eca15afaf5a`; checkpoint `784d7cb7` records
partial W0, not scientific implementation. The official starter was generated in
an empty temporary destination from that central checkpoint using immutable
`policy-v1.5.10` (`1c38d50337ffd67e20eb02f5e02b24152073b3b4`) and the real
`--admission-sha`. Its baseline is integrated without replacing scientific history.

The investigators expressly authorized one additional local issue,
[uibcdf/peptidemt#1](https://github.com/uibcdf/peptidemt/issues/1), for W0 evidence
and receiving because the applicable member reviews require member-owned issues.
This is an operational extension of D36's reporting authority, not a new scientific
or architectural decision or authority for other issues. W1 remains gated on W0
receiving. See the [receiving record](pending_proposals/complete_w0.md).
