# Decisions and discussion history

Navigation: [index](README.md) · [scope](vision_scope.md) · [alternatives](architecture_alternatives.md).
Date of initial record: **2026-10-26**. Approval authority: the investigators.

Current operational handoff, **2026-11-10**: the investigator requests a
[complete migration checkpoint](migration_checkpoint_2026_11_10.md), correcting
the intended host to another machine. Earlier hardware observations belong to
the source machine only. This commissions checkpoint review/preservation and
issue synchronization, not a new scientific decision, engine/chemistry adoption,
model/GPU execution, commit/push or package publication. D49 and the existing
scope-specific resource contracts persist; actual destination admission is pending.

Subsequent explicit instruction commissions a private ZIP with placement
instructions and **reviewed PeptideMT source synchronization to GitHub with a
clean local clone**. See [transfer instructions](migration_transfer.md). This
supplies that source commit/push authority; it does not authorize a package
release, new science or publishing HydrAMP's private branches. Portable bundles
and overlays remove the need to copy raw `.git`; older checkpoint statements
about local-only PeptideMT source are historical. No new scientific D-number follows.

Latest resource disposition: **D44 accepts the exact modern HydrAMP dev5 route
for experimental native-score analogue generation**, 2026-11-04. See its
[acceptance record](hydramp_dev5_acceptance.md). D41's accepted dev3 de novo
bundle and the earlier chronological entries retain their original scopes.

Latest work direction: **D53 approves and commissions the data-only T1a
reported-affinity reference**, under the [approved work order](mdm2_t1a_work_order.md).
D52's full independently evaluated target-directed demonstrator remains the
longer-horizon objective; new molecular/evaluator/generation contracts retain
their review boundary.

Next proposed work, **not an accepted decision**: [T1b molecular admission](mdm2_t1b_proposal.md),
2026-11-10. Its source/chemistry question precedes a qualified peptide-pose
profile and independent affinity/selection assessment. D53 is not extended by
this proposal or by the investigators' instruction to continue preparation.
That earlier T1b/3EQS proposal is an optional source-admission branch, not the
mandatory next step. The latest preparation instead describes a proposed
[1YCR pose comparison](mdm2_comparative_pilot_proposal.md) and its
[input-profile questions](mdm2_input_profile_preparation.md); neither is approved
for scientific execution. Resume in the order specified by the checkpoint.

Subsequent investigator clarification, 2026-11-10: protein–peptide docking has
not begun and its alternatives, including binder design, must be discussed and
explored properly. The [comparative review](peptide_protein_binding_survey_2026_11_10.md)
is delivered under D52 preparation. T1b/3EQS and HADDOCK3 are possible choices,
not accepted requirements or a new implementation commission.

The subsequent investigator instruction commissions **source/method/data review
and comparative-protocol preparation**, delivered in the
[BindCraft–MDM2 audit](bindcraft_mdm2_source_review_2026_11_10.md) and
[pose-pilot proposal](mdm2_comparative_pilot_proposal.md). This is D52 preparation,
not acceptance of the proposed methods, chemical recipe, geometric tolerance or
model-run budget. No new scientific decision ID is assigned by this delivery.

Latest completed finite commission: **D53 T1a reported-affinity receiving**,
with the [actual qualification](mdm2_t1a_qualification.md), 2026-11-09.
All source occurrences, repeated-display links, quantities and unknowns survive
one actual receiving and fresh replay. This does not qualify a predictive method
or complete D52's independently evaluated selection objective.

The earlier **D51 single MDM2–p53 T0 structural
reference** retains the [approved work order](mdm2_t0_work_order.md) and its
[authorization](evidence/mdm2_t0_authorization.json). This commissions finite
identity/geometry work, not a predictive target model. The
[actual T0 qualification](mdm2_t0_qualification.md), 2026-11-06, now completes
its prescribed source/profile/geometry gates; biological acceptance remains
separate. The investigator subsequently sets the scoped host reserve/task RSS
stop to 4/2 GiB in the [resource correction](evidence/mdm2_t0_resource_correction.json).

Latest HydrAMP module commission: **D50 approves the independent HydrAMP generation-result
contract and data-only implementation**, 2026-11-05. See the
[approved contract](hydramp_result_contract.md) and its
[authorization](evidence/hydramp_generation_result_authorization.json).
The investigator also approves a [scoped serial resource profile](evidence/hydramp_generation_result_serial_authorization.json)
for D50 data-only/package checks: 512 MiB sampled aggregate RSS stop, 4 GiB
available-host-RAM reserve, CPU0/1 and one numerical thread. Other work retains
its envelope. The [final qualification](hydramp_generation_result_implementation.md)
passes source and installed synthetic checks. The investigator subsequently
authorizes exactly one local consolidation commit,
`6a3ff905635a4bd744854cd540f8513916aa99f0`, matching the reviewed 21-path tree;
its [authorization](evidence/hydramp_dev8_commit_authorization.json) and
[execution receipt](evidence/hydramp_dev8_local_commit.json) keep this separate
from D50's original no-Git commission. No push, merge, publication or scientific
scope change follows.
The earlier **D45 analogue consumer contract and R1/R2 implementation with
controlled data/artificial parameters** retains its 2026-11-04 scope.
See [the work order](hydramp_redesign_work_order.md) and
[implemented outcome](hydramp_redesign_implementation.md). D43/A1 retains its
original contract and scope.
D42/E1 and the later finite E2 encoder evidence retain their separate scope.

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
its provisional chemistry/length scope. D36 authorized W0–W4; official W0 receiving is complete. **D37 now accepts the
specific executed Macrel 1.6.1 bundle for exploratory assessment/ranking within
D35**, with its recorded chemical, preprocessing, length and biological-applicability
limits. Central optional-client receiving is accepted under MolSysSuite #152.
Macrel is one optional evaluator in the extensible resource catalog. Initial
user documentation follows the suite's Sphinx/MyST/PyData conventions; its
layout remains provisional. No later increment or publication is authorized.
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
| D37 | Accept the exact executed Macrel 1.6.1 bundle for D35 exploratory computational assessment/ranking and document its use, limits and qualification evidence. | Explicit investigator acceptance on 2026-10-29 after the in-conversation report and clarification that Macrel is one optional evaluator among extensible bioactive-family resources. Preserve D35/D36 and M1–M8; predictions are not experimental activity/safety, score calibration or universal family-membership probabilities. Exact numerical package 7a299d1, driver a1b5e3a, model/provider/environment hashes and live/control evidence remain identified in w3_assessment.md and evidence/w3_summary.json. Central #152 is received at b12f7230. The investigator also requests provisional documentation informed by MolSysMT/MolSysViewer; implementation choices are routine and do not add a new scientific architecture. No new model call, host allowance, HydrAMP/later increment or package/site publication is inferred. |
| D38 | Commission preparation and qualification/integration of the single proposed native HydrAMP de novo route for increment 2, using H0–H4 and the existing Macrel assessment/selectors. | Explicit investigator authorization on 2026-10-29 after the scope explanation and proposal at 52c32e1 / PeptideMT #8. Permit artifact/use preflight, an isolated legacy environment and adapter preparation. Preserve native softmax, amp conditioning, filter_out=False, n_attempts=1, properties=True, explicit seeds, occurrence fidelity and distinct native/Macrel scores. The four-generation-call/52-requested-output test design includes direct/adapter repeatability; actual model loading/inference still requires the exact bundle/use conditions and a fresh shared-host resource/call envelope, including separate Macrel calls. No scientific acceptance of HydrAMP, GPU, retries/refill, analogue route, feedback, target conditioning, training, redistribution, publication or general architecture is granted. D35–D37 and M1–M8 remain unchanged. |
| D39 | Authorize a local native PyTorch inference port in the investigator-owned HydrAMP fork, preserving the legacy reference and testing mathematical fidelity before adoption. | Explicit investigator instruction on 2026-10-30 to move to PyTorch if feasible, following the authorized fork/packaging preparation. Implement the selected de novo computational path in a separate worktree; isolated Python 3.14 CPU installation and synthetic-weight tests are preparation evidence. Preserve checkpoint equations, chemistry, conditioning, native token/score meanings and D35–D38. Real checkpoint/PCA loading and legacy-versus-port execution still require exact bundle/use review and a fresh host/call envelope. No pretrained parity, scientific acceptance, full generator replacement, new training, family generalization, GPU, publication or commit/push authority is inferred. |
| D40 | Accept the measured numerical deviation only for the twelve compared HydrAMP inputs and continue qualification of the original dev0 PyTorch port. | Explicit investigator acceptance on 2026-11-02 of the limited behavioral-review proposal. Bind this disposition to the dev0 wheel and retained evidence in hydramp_behavioral_acceptance.md / evidence/hydramp_limited_acceptance.json. Preserve original numerical FAIL reports, exact tokens/strings, source/assets/environments and unchanged diagnostic tolerances. Dev1 is not adopted as a correction. D38/D39 local preparation continues; complete native properties/provenance/adapter and H0–H4 qualification remain partial. No unseen-input equivalence, full HydrAMP acceptance, larger tolerance, new scientific scope, model/PCA execution allowance, GPU, training or publication follows. |
| D41 | Accept HydrAMP modernized with PyTorch, exact dev3 bundle, for experimental AMP generation in PeptideMT. | Explicit investigator acceptance on 2026-11-03 of hydramp_dev3_acceptance_review.md after its full report. Bind the scope to hydramp_dev3_acceptance.md / evidence/hydramp_dev3_acceptance.json, provider wheel 81761e0d…ed7 and consumer wheel 18b1cb18…e83. Preserve the seeded unfiltered native route, exact assets/definitions, D35/M1–M8, both Macrel-based selectors, all probability/global-rank FAILs and unresolved use/provenance limits. D40 retains its original dev0 scope. Accept experimental use, not universal equivalence, biological efficacy, other-family capability or a release. Existing calls are exhausted; no new execution, training, GPU, new method or external contact/publication follows. Record future scientific comparison, standalone-product review, family-extension/successor feasibility and possible original-author handoff in HydrAMP #3–#6 and PeptideMT #32. |
| D42 | Approve the deterministic encoder contract and E1 implementation/testing with artificial weights in the owned HydrAMP fork. | Explicit investigator instruction to continue on 2026-11-04 directly answers the concrete E1 approval question. Bind the reviewed proposal SHA-256 064848b3832d65f462c86cf347f74b534fccb4044e803c156b5a04e2832a926e and evidence/hydramp_encoder_E1_authorization.json. CPU int64 tokens [N,25] yield CPU float32 mean/raw log-variance [N,64], preserving occurrences/zeros, with no posterior sampling/RNG mutation. Separate dev4 candidate; installed synthetic outcome in hydramp_encoder_E1.md. Preserve D41/dev3, D35/M1–M8 and selectors. E2 real weights/reference execution requires its own exact artifacts, prospective criteria and fresh host/call approval. No pretrained encoder acceptance, analogue/training/filter-fix/other-family work, GPU, release or author contact follows. |
| D43 | Approve the first native-score analogue-improvement contract and A1 implementation/testing with artificial parameters in a separate HydrAMP candidate. | Explicit investigator continuation before the audit pause, retained in evidence/hydramp_analogue_A1_authorization.json, contract SHA-256 11c1a85ec9233ba5a09ee18be377d41a577831793b9d7b7a2eef817a3415d360. Preserve attempt/prototype occurrences, local explicit seeded noise, strict native AMP/low-MIC-class score comparison, raw tokens and no-hit/empty diagnostics; no optional filters, discovery, descriptors or PCA. The subsequent instruction to implement the reviewed continuation plan lifts the audit pause for this unchanged artificial scope. Preserve accepted dev3/dev4, D35/M1–M8/selectors and old FAILs. Real analogue A2, new consumer redesign/feedback/target capabilities, training, GPU and publication retain their own review; no new real model allowance. |
| D44 | Accept the exact dev5 HydrAMP route for experimental native-score analogue generation, retaining all A2 diagnostic failures and finite coverage limits. | Investigator agreement to continue on 2026-11-04 follows the A2 report and recommendation to accept this route. Bind to hydramp_dev5_acceptance.md / evidence/hydramp_dev5_acceptance.json, provider wheel f6b9e306…433e and executed receipt def2a831…7cd8. Preserve the token/latent/native-score/bucket semantics, experimental AMP scope, probability FAIL, standalone near-tie batch sensitivity, sparse real candidate/duplicate-pool coverage and unresolved use conditions. D41/dev3, dev4/E2, Macrel, M1–M8 and both selectors remain separate. This accepts a resource, not the new consumer redesign contract/API or biological/general numerical equivalence. All real allowances are exhausted; no new calls, training, GPU, feedback, family/target expansion, release, commit/push or author contact follows. Prepare the concrete consumer work order for review under #32 and report the missing reusable codec to owner #4. |
| D45 | Approve the concrete analogue consumer contract and commission R1/R2: data-only receiving/composition and owner codec/isolated artificial execution. | Investigator explicitly directs continuing in response to the R1/R2 approval question, contract SHA-256 876ef80c5629dc74cf9e541bcf5f1d257ed37f28a0148f5e435a738c8a47fd71, authorization evidence/hydramp_redesign_authorization.json. Preserve operation-specific admission, original chemistry, parent/attempt mapping, all failure/no-hit evidence, separate native/Macrel meanings, existing selectors and accepted dev3/dev4/dev5. Implement the reusable native codec in HydrAMP in a new identified candidate. No real learned weights/Macrel, R3 call allowance, GPU, training, feedback, targets, new families, release, commit/push or author contact. |
| D46 | Approve the finite historical experimental-entity/unchanged-sequence model view and E. coli ATCC 25922 MIC review scope for original–modern comparison preparation. | Investigator explicitly directs proceeding in answer to the finite-view approval question on 2026-11-04. Bind approved proposal SHA-256 30f8b637c4c8dde4949c9080381a002dc98f38f5e2e4f5f1c03273ba02463376 and evidence/hydramp_historical_view_authorization.json. Preserve experimental amidation, original strings, every table observation, unknowns, censoring and provenance; the model-view omission does not assert chemical equivalence. Commission the next model-free work order and controlled-fixture design. No implementation commission, general admission/API change, native payload, model/artificial-network allowance, biological endpoint/class truth, mass/unit conversion, independent cohort, equivalence, GPU, generation, release or external contact. D35/M1–M8, D41/D44/D45 and exhausted budgets remain unchanged; current authority is in hydramp_historical_work_order.md. |
| D47 | Approve the finite historical reported-MIC endpoint and descriptive paired ROC-AUC policy, and commission the data-only endpoint/comparator with artificial score controls. | Explicit investigator approval and continuation on 2026-11-05 after the endpoint proposal and model-free implementation question. Bind proposal SHA-256 e7bf019ec410bb02ef5a01ee12fba625159d7c71e9b76b704787d9005ed223ed and evidence/hydramp_historical_endpoint_authorization.json. Use displayed E. coli ATCC 25922 MIC ≤32 µg/mL: retain all 42 observations/39 literal-string groups, primary 38 stable groups (12 positive/26 negative), and both 39-group ambiguity scenarios with the same class choice in both engines. This is reported activity, not the native pooled molar target or calibrated probability. Preserve source bytes, raw score precision, exact ties and paired sensitivity without adopting a conflicting value or confidence interval. Qualify an existing statistics provider; no learned-score receiving, native input/model call, new budget, mass/unit conversion, 128 µg/mL endpoint, independent cohort/equivalence/quality verdict, public API/admission change, release or third-party contact. Read hydramp_historical_evaluation.md for the controlled implementation outcome; D35/M1–M8, accepted bundles and exhausted allowances remain unchanged. |
| D48 | Approve the finite historical learned-score receiving/native-input contract implementation, scalar/method-double tests and two bounded codec-only children. | Explicit investigator approval on 2026-11-05 in direct response to the implementation/codec question. Bind contract SHA-256 1b08e464261a3190bff886e26fe42dd826903ec89a09a9beb91d0de611fc5972 and proposal 8ecf7787f48bd5eb29ca693ffa0f2c4f439e639635e6c8c461f2bd1c01ecf89a through evidence/hydramp_historical_real_implementation_authorization.json. Reuse owner codecs, preserve all D46/D47 source/endpoint/precision/pairing obligations, separate real and control evidence, use truthful detached attribution and model-free saved replay. Codec children are sequential on CPU0/1, one numerical thread, ≤180 s each/360 s total, 4 GB RAM intent with sampled 2 GiB aggregate RSS stop and 8 GiB virtual ceiling. Zero learned weights, neural/artificial-weight evaluations, Macrel/PCA/descriptors/GPU/training/generation or new model allowance. Preserve accepted bundles, selectors/M1–M8 and exhausted earlier budgets. Read hydramp_historical_real_implementation.md: modern codec passes, original import stops before encoding; the two-child allowance is spent. A further original-codec attempt needs new exact single-use approval. The twelve model evaluations and public API/admission/release/third-party contact remain unapproved. |
| D49 | Delegate reasonable routine execution and diagnostic retries within approved work, with shared-host stewardship instead of per-invocation permission rounds. | Explicit investigator direction on 2026-11-05 that reasonable resource use should not require repeated permission, followed by the request to persist the guideline in AGENTS.md. Record evidence/shared_host_execution_delegation.json and root AGENTS.md standing execution authority. Inspect available RAM/load/disk; keep small bounded batches, one heavy worker, CPU0/1 and one numerical thread for current HydrAMP work, 4 GB RAM intent with sampled 2 GiB aggregate RSS stop and 8 GiB RAM reserve. No GPU. Declare fresh bounded run/call limits and preserve every historical spent ledger and failure; a new record cites standing delegation and must not claim per-plan investigator review. This supersedes resource-confirmation pauses, including the pending original-codec retry and routine bounded continuation of the approved D46-D48 historical comparison once inputs/bundles qualify. Scientific scope/contracts, preprocessing/chemistry, acceptance, new models/families/training/targets/feedback, publication and third-party contact still need their applicable separate authority. |
| D50 | Approve the first independent HydrAMP generation-result/provenance contract and commission its bounded data-only implementation. | Explicit investigator approval on 2026-11-05 after the concrete contract review. Bind original proposal SHA-256 ce32baaa65cdce9a6474f95bac3a65ec5425fd3601bbdeb8f6e8983f4f4ed70b through evidence/hydramp_generation_result_authorization.json. Implement an owner descriptive profile, faithful completed-generation save/read, a light model-free reader and optional caller-owned Recorda references/detached Ackredit metadata. Preserve original tokens, occurrences/order, scores/descriptor values, producer versus exporter identities and explicit unknown provenance; reuse NumPy and supported providers. Qualify synthetic data only with zero neural evaluations or learned weights/PCA; preserve dev7 and accepted bundles separately. No analogue/encoder persistence, live attribution, new science/chemistry/acceptance, models, GPU, training/feedback/families/targets, package publication, commit/push or author contact. D49 delegates ordinary bounded technical checks. |
| D51 | Approve the single MDM2–p53 T0 structural-reference work order and its finite implementation/execution. | Explicit investigator approval after the concrete implementation explanation on 2026-11-05. Bind the reviewed order through evidence/mdm2_t0_authorization.json. Receive 1YCR revision 1.5 and qualify an exact isolated MolSysMT application profile before observed-heavy-atom geometry. Implement the case-specific coordinator and original/rigid-transform/peptide-displacement controls with the fixed criteria and serial CPU/resource limits in mdm2_t0_work_order.md. Preserve provenance, observation/inference distinctions, failures and saved outputs. This checks identity and geometry, not predictive recognition or biological utility. D49 delegates reasonable technical checks/retries. No T1, learned models, docking, generation, GPU, new public API/selector, commit/push/publication or external-author contact. |
| D52 | Pursue one independently evaluated target-directed peptide design/selection demonstrator, starting with evidence/provider review and a concrete prospective T1 proposal. | Explicit investigator direction on 2026-11-06 to attempt the proposed objective and respect negotiated scientific-readiness and component-ownership rules. See evidence/target_directed_demonstrator_authorization.json and target_directed_demonstrator.md. PeptideMT owns the question/policy/orchestration/interpretation; reusable molecular operations remain with MolSysMT and other capabilities with their owners. MDM2–p53 is conditional on suitable evidence/evaluation, not an accepted undefined T1 model/chemistry/assay contract. Preserve D14, D35/M1–M8, accepted AMP scopes and D49. No new models, generation/docking, training, GPU, scientific thresholds or Git/publication authority is inferred for this preparation package. |
| D53 | Approve the source-scoped MDM2 T1a reported-affinity contract and commission its private data-only implementation/qualification. | Explicit investigator approval on 2026-11-09 in direct response to the concrete T1a question. Bind original proposal SHA-256 069247bf4b46e8fafba553ecb5311f67b0bfd6748ea4a06822053c3285c05e56 through evidence/mdm2_t1a_authorization.json and mdm2_t1a_work_order.md. Preserve every original source occurrence, WT alias, Kd/SD unit and precision, unavailable result, chemical unknown, source discrepancy and prior exposure; use supported quantity/measurement records and model-free saved replay. Serial CPU0/1/one thread, 512 MiB aggregate task RSS, 4 GiB host reserve, 180 s wall/120 s CPU/8 GiB address space/64 MiB output per job. D49 delegates routine checks and diagnosed retries. No molecular-state admission, new model/evaluator, docking, sequence generation, GPU, training/feedback, public API or Git/package/dataset publication. |

On 2026-11-05, following the D49 paired-codec checkpoint, the investigator
directs continuing the unchanged fixed historical comparison. A separate
bounded declaration under standing D49 authority is fully consumed in twelve
neural evaluations. The [executed outcome](hydramp_historical_real_comparison.md)
records equal primary descriptive AUC and ordering, small retained native score
differences, repeat/batch diagnostics and guarded saved replay. This is execution
evidence, not a new scientific acceptance decision or a change to D46-D48.
Earlier codec-only and preparation allowances/statuses remain historical.

On 2026-11-05 the investigator's continuation after the D46 work-order report
commissions its first data-only receiver and saved inspection/replay cycle.
[Implementation authority](evidence/hydramp_historical_data_authorization.json)
preserves the exact pre-implementation work order. The
[local outcome](hydramp_historical_data.md) records 38 controlled tests and
actual-source saved replay, with unchanged public admission and zero native
model inputs/calls. D46's finite scientific view is unchanged; neither a new
biological endpoint nor a model execution allowance follows.

On 2026-10-30 the investigator separately authorized the D39 real-checkpoint
comparison after clarifying a 4 GB task RAM budget. Its six evaluations completed
within roughly 0.5 GiB observed worker-plus-supervisor RAM. The
[execution report](hydramp_pytorch_comparison.md) preserves the failed decoder
probability criterion despite exact tokens and passing PCA/heads. No scientific
adoption, tolerance relaxation or further model budget follows.
The separately approved two-forward [intermediate diagnostic](hydramp_decoder_trace.md)
then reproduced both earlier endpoints bitwise and localized the first observed
difference to the autoregressive GRU. An isolated [joint-product candidate](hydramp_gru_candidate.md)
is prepared as a numerical-layout hypothesis, without real candidate evaluation
or adoption at preparation. Its separately approved single forward then also
failed the original probability criterion; it is not adopted. On 2026-11-02 the
investigator separately authorized the prepared two-forward NumPy FP64
[independent numerical reference](hydramp_numeric_reference.md), which completed
within 0.52 s and 65.63 MiB conservative sampled combined RSS. Both formulations
agree, all 300 tokens match, and native/port FP32 probability errors relative to
that reference are similar. This is diagnostic evidence for the pending numerical
admissibility review in #8 at that execution checkpoint, not acceptance, a tolerance
change or further calls. The subsequent explicit D40 decision now accepts only the
measured deviation on those twelve inputs, allowing continued dev0 qualification.
The [limited acceptance record](hydramp_behavioral_acceptance.md) retains the
exact evidence and wider pending qualification; no additional execution is granted.

On 2026-11-03 the investigator separately approved the exact dev3 full-comparison
execution plan, with 22 network evaluations and sequential CPU/4GB task bounds.
The [execution report](hydramp_full_comparison.md) preserves exact tokens, sequence
occurrence order and five descriptors, passing heads and exact repeats on twenty
distinct latent inputs (36 paired returns). The strict probability diagnostic
remains failed. This execution approval is not a new scientific acceptance decision
or a D40 extension; original bands, failures, source/assets and exhausted quotas
remain unchanged. Broader resource/adaptor acceptance returns to the investigators.

Later on 2026-11-03 the investigator instructed proceeding with broader confidence
qualification, aiming for the confidence warranted by the original on the ported
route. The [prepared campaign](hydramp_confidence_campaign.md) freezes 256 new
latent inputs and proposes 132 network forwards including repeat/layout controls.
Preparation and artificial checks are complete; exact new execution-budget
approval and scientific disposition remain pending. This records commissioning
of preparation, not a new acceptance decision or an extension of D40.

The investigator then explicitly authorized the exact 132-forward CPU plan.
The [campaign outcome](hydramp_confidence_campaign.md) records agreement of all
public batch sequence/order/descriptors and 7,700 paired token positions on 256
distinct latent inputs plus reuses. The probability diagnostic and global AMP
pair check FAIL: one reversal, two split native ties and seven new ties, all
between batches near score 1. No public-batch order changed. Both workers complete
within bounds; the allowance is exhausted. This is execution authority/evidence,
not broader acceptance, a threshold/selector change or a new D40 disposition.

The investigator then commissioned a saved-output ranking relevance review.
The [review](hydramp_rank_relevance.md) finds one member replacement at seven
global HydrAMP-AMP-only cutoffs, with at most two rank positions of displacement;
the actual PeptideMT selectors retain their separate Macrel AMP/hemolysis binding.
A concrete dev3 fixture-deviation disposition for continued consumer qualification
is proposed for investigator decision. No new acceptance, model allowance or D40
extension is inferred from the instruction to perform this review.

The investigator next requires a causal explanation and explicitly authorizes
an issue in the owned fork, retaining justified modern numerical improvements.
[HydrAMP #1](https://github.com/uibcdf/hydramp/issues/1) now owns the provider
investigation after the investigator enabled Issues. The
[numerical record](hydramp_amp_numerics.md) demonstrates different standalone
sigmoid kernel behavior, an original-runtime monotonicity artifact and stronger
modern operator accuracy on the fixed artificial sample. The investigator subsequently authorized the exact prepared AMP-stage allowance,
which completed with all saved endpoints bitwise reproduced. Switching only the
final sigmoid reproduces all ten changed relations: one native reversal and two
ties resolve in the conditional FP64 direction, while seven new ties lose strict
relations. The first recorded upstream difference is the first LSTM.
The [execution receipt](evidence/hydramp_amp_trace_execution.json) preserves the
fully spent 36-forward/24-replay/two-FP64-vector budget. This is causal diagnostic
evidence, not whole-head superiority, biological acceptance, a D40 extension, a
tolerance/selector change or further pretrained execution authority.
A [full AMP-head independent FP64 reference](hydramp_amp_reference.md) was
subsequently prepared with seventeen artificial tests, then explicitly authorized
by the investigator's direction to continue after the concrete plan was presented.
All 24 forwards completed in 3.75 s; both FP64 layouts agree bitwise. Modern has
lower aggregate maximum/mean/RMS error at every nontrivial recorded stage on this
cohort, with AMP closer in 91 cases versus 58 native and 43 ties. The seven new
modern rank ties persist. The [execution receipt](evidence/hydramp_amp_reference_execution.json)
preserves this numerical finding and exhausted allowance; it is not D41, general
equivalence, biological superiority, dev3 acceptance or H0–H4 receiving.
A subsequent investigator question about the 58 native-closer results triggers
[saved-data attribution](hydramp_amp_error_attribution.md), with no new model or
activation evaluation. Of those 58 cases, 39 already have closer native logits,
12 have closer modern logits and 7 have identical logits. Native/modern whole-head
FP64-cast matches are 48/47 across 192 outputs; this metric does not favor modern.
This refines the aggregate numerical conclusion without a new decision or
changed scientific acceptance.

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
| P10 | Distinguish collective/distributional library proposals from individual molecular proposals, including incomplete individuals. | Pending bounded recommendation from [V0.2 case A](future_horizons.md#9-bounded-extensibility-review-after-p09-approval). No library support, generic population hierarchy or MVP requirement adopted; concrete semantics can wait until such a capability is prioritized. |

The [V0.1 direction is accepted under D33](v0_1_scope.md), D34 fixes first coverage/
qualification order, and D35 closes increment 1's scientific contract including
M1–M8. The [work order](increment_1_work_order.md) is authorized under D36: W0
receiving and W1–W3 are complete; D37 accepts the executed bundle, and W4 supplies
the requested verified documentation. Central engineering receiving is
accepted in MolSysSuite #152 at b12f7230. Preserve each stage's exact evidence;
do not repeat the scientific/architectural approval. Later feedback is outside scope.
P02/P03/P05 need only the selected capability-specific portions; P10 and future
horizons add no requirement. Earlier unapproved A/B/C records below are history.

### Proposal disposition

P06 is **completed through W0** under D36, with accepted published registration,
the official starter, component qualification and effective central receiving.
The closed [central admission issue](https://github.com/uibcdf/molsyssuite/issues/146)
and [component evidence issue](https://github.com/uibcdf/peptidemt/issues/1)
retain the original admission, source, environment and audit identities.

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

### Historical real-score work order prepared, not approved — 2026-11-05

Following D47 delivery, the investigator continuation commissions preparation
of the [real-score receiving and execution contract](hydramp_historical_real_work_order.md).
It preserves D47's finite endpoint and proposes source-bound native receiving,
primary/repeat 39-row batches and fixed 20+19 context diagnostics. Static source,
opaque-asset and metadata checks identify the exact installed routes; no model
or codec is imported/called and no native input is prepared. The modern public
API computes both heads, so the proposed budget includes four auxiliary AMP
forwards: twelve neural evaluations total, not eight. This is not a new accepted
decision, receiving implementation or model allowance. Implementation and later
exact executed-artifact/host/call approval remain distinct; all prior allowances
stay exhausted. The [receipt](evidence/hydramp_historical_real_preparation.json)
preserves the proposal and static evidence. Reuse #3/#32 and route the reusable
single-head scoring improvement to our HydrAMP #4, without third-party contact.

### W1 implementation under the existing work order — 2026-10-27

After completed central W0 receiving, the investigators commissioned W1 under
the existing D35/D36 contract. [PeptideMT #4](https://github.com/uibcdf/peptidemt/issues/4)
tracks ordered sequence/FASTA proposal ingestion, attributed saved provider rows,
operation-specific validation and both exact replayable selectors. The
[implementation guide](w1_core.md) documents the small provisional public boundary.
Controlled engine-free tests exercise parts of M3–M8; no native Macrel execution,
M1/M2 qualification, HydrAMP or package publication follows. This is implementation
within the existing decisions, not a new architecture or scientific approval.


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
receiving. See the [receiving record](archive/complete_w0.md).

## Strategic trajectory and experimental-reference case — 2026-10-27

At the investigators' request, added
[scientific_trajectory.md](scientific_trajectory.md) to preserve the original
**target-directed plus functional-family-guided peptide design** goal, the
distinction between scientific architecture and executable usefulness, the
principal overengineering/reward-model risks, and a proposed four-milestone
progression: faithful real evaluation, real learned generation, functional
feedback affecting later proposals, and joint target/function design.

Expanded [design_examples.md](design_examples.md) with a fifth, published-
evidence-anchored **case E** and added its detailed
[MDM2/MDMX cell-permeating anticancer peptide study](case_study_cpp_anticancer_mdm2_mdmx.md).
ATSP-7041 and PDB 4N5T provide experimental and chemical reference evidence;
the PDB receptor construct is not assumed to be unmodified human MDMX. The
existing case C remains an independent *conceptual* CPP+ACP problem.
The experimental results belong to the cited sources and have **not** been
reproduced in PeptideMT.

**Disposition:** scientific trajectory and future case are contextual
research/design documentation, not new D decisions, accepted model/target
selection, live scientific evidence or expanded W0–W4/M1–M8 contracts.
D33–D36, the W0 engineering/receiving rules and no-new-issues boundaries
are unchanged; the historical W0 pause has since been resolved. The next authorized work remains finishing W0 before W1.

## CPP guided-case coverage expansion — 2026-10-27

At the investigators' request, added [cpp_guided_projects.md](cpp_guided_projects.md)
to build a representative **CPP-specific** case-guided research pool. Twelve
literature-grounded guides span linear arginine-rich/penetratin peptides,
CPP/cargo, endosomal escape, **azurin-derived p28 with direct p53 interaction
and anticancer context**, iRGD-mediated tumor/tissue penetration, pHLIP pH-driven
membrane insertion, cyclic CPP cytosolic delivery, stapled ATSP-7041 directed
to **MDM2/MDMX**, a multifunctional CPP+AMP search hypothesis, **PepFect14
oligonucleotide nanocomplex cargo delivery**, and **protease-activatable
polyanion-masked CPPs (ACPPs)**. The case
pool explicitly distinguishes cell uptake, endosomal escape, cytosolic access,
cargo/tissue delivery, intracellular molecular recognition and anticancer
phenotype, with different chemical species and biological contexts.

Updated [worked cases](design_examples.md), [vision](vision_scope.md),
[scientific trajectory](scientific_trajectory.md), [roadmap](roadmap.md) and
[future horizons](future_horizons.md) as cross-references. The new cases
are literature-anchored future research/project references, **not** newly
approved scientific capabilities, experimental results, automatic benchmark
fixtures or new release obligations. The current V0.1 AMP/Macrel/HydrAMP
direction, D33–D36, M1–M8, W0 central receiving gate and issue authority
remain unchanged. No model installation, new scientific run or code/issue
was authorized by this documentation addition.

## Supplemental CPP project cases — 2026-10-27

The investigator requested a representative case-guided pool beyond the
advanced stapled peptide. The simultaneously published
[canonical twelve-case CPP progression](cpp_guided_projects.md) is retained
as owner of **CPP-01–CPP-12**. A separate
[four-case complementary extension](cpp_case_portfolio.md), with unique
**CPP-S1–CPP-S4** identifiers, covers Pep-1 noncovalent protein delivery,
GALA membrane fusion as an endosomal-escape *helper*,
mitochondria-specific penetrating peptides, and buforin II's
bacterial intracellular antimicrobial mechanism. The existing abstract
CPP+ACP target case and ATSP-7041 detailed case remain linked rather
than duplicated as distinct implementations.

These are scientific development guides using primary published evidence,
not approved model packages, experimental replications, execution,
additional scientific requirements or D decisions. D33–D36, the already completed W0 engineering receiving,
Macrel M1–M8 and the existing issue boundaries are unchanged.

## Investigator governance clarification — 2026-10-27

After W0 engineering receiving, the investigator explicitly requires PeptideMT
to follow the existing suite contributor rules: both receptors, canonical
release/tag identities, the authorized principal-maintainer direct-push route
versus external full-suite PRs, owning-issue feedback and reuse of domain owners.
This clarifies operational governance; it creates no scientific decision number
or additional scientific implementation/publication authority.

The earlier D36/W0-only issue restriction and its dated extensions describe the
bootstrap authorization then in force. They are superseded **for reporting**:
actionable bugs, limitations and improvements in any component must reach its
owning issue with consumer evidence. PeptideMT owns peptide-specific design,
selection and interpretation; MolSysMT owns general molecular-system operations,
MolSysViewer visualization and TopoMT cavities/topography. Existing APIs are
reviewed before adding functionality; missing general capabilities are proposed
to their owners. The [governance map](governance.md) routes the full applicable
policy set. D35/D36's scientific meaning and M1–M8 remain unchanged.


## Macrel resource acceptance and documentation — 2026-10-29

The investigator accepted Macrel after reviewing the exact bundle, actual outputs,
M1–M8 evidence, selector consequences and stated limitations. D37 records this
disposition; [the acceptance record](increment_1_review.md) names the bundle.
Macrel is one optional evaluator for native AMP and hemolysis evidence. Future
resources keep their own scientific roles and qualification; no universal
probability scale or generic plugin architecture is approved by this acceptance.

The investigator requests documented use, limitations and confidence evidence,
and an initial provisional user-documentation structure informed by MolSysMT and
MolSysViewer. The [documentation build guide](../docs/README.md) records those
source references and the Sphinx/MyST/PyData layout. No scientific model runs
or public deployment accompany this documentation work.


## Nonexclusive generator inventory and renewal research — 2026-10-29

D38 commissions bounded native HydrAMP preparation and qualification after the
investigator-approved explanation. Exact bundle/use conditions and a fresh host
envelope still precede model loading/inference. The
[preparation receipt](evidence/hydramp_preparation.json) records verified source/
asset identities, an isolated bootstrap and the unresolved original dependency
closure; no model was loaded or executed.

The investigator subsequently reiterates that HydrAMP, a possible modern
derivative, PLUM and other resources can coexist. This clarifies implementation
priorities within D17–D26 rather than selecting one exclusive architecture.
The [expanded resource survey](generative_resource_survey.md) records source
observations and complementary capabilities; listed integrations remain proposed.
A modern inference fork and a new multi-family trained model are distinct research
directions. Neither has been created, trained, commissioned or accepted through
this discussion. Preserve the approved Macrel and molecular/selection contracts.

## Preserve justified modern results; complete functional receiving — 2026-11-03

The investigator clarifies the current objective: preserve modern numerical
improvements when independently justified, explain nonidentical results and why
they are sound, and avoid degrading the implementation to imitate legacy
approximations. This is a working direction within D38/D39, not a new scientific
acceptance decision, unconditional superiority claim or extension of D40.

The [finite activation attribution](hydramp_amp_activation_attribution.md)
separates upstream and activation errors and compensation; it records benefits
and limits of the unchanged dev3 candidate. A hypothetical precision change is
unimplemented and unaccepted. The [private receiving bridge](hydramp_receiving_preparation.md)
passes saved-data replay. The [exact functional plan](hydramp_h4_qualification.md)
prepares two generated pools, qualified Macrel and both unchanged selectors.
Fresh host/call approval remains necessary before either live stage. No new
model/descriptor/Macrel call, release, commit or push occurred in preparation.

## Authorized private HydrAMP receiving experiment completed — 2026-11-03

The investigator approves the exact H3/H4 plan
`f9b8040897079401d75c6ad3afd3b0cfc499350abfc2943a268b37646ba82c2a`
after its full resource/call request. This grants that finite execution, not
scientific adoption. The [result](hydramp_h4_qualification.md#approved-execution-and-independent-review--2026-11-03)
passes same-operation receipt of 32 proposals, two exact cached dev3 returns,
30 generated Macrel assessments plus four exact W3 controls, and both unchanged
selectors with exact saved replay. Two leading-M incompatibilities remain visible.
Six neural forwards/two descriptor bundles and three Macrel calls are consumed;
no retry or new implementation candidate follows.

All nine generated Macrel AMP-positive rows are Hemo-positive in this fixture.
Functional composition therefore passes while joint AMP/hemolysis utility and
biological superiority remain unestablished. Preserve that outcome and the
original numerical FAIL diagnostics. D35/M1–M8, D40, scientific-disposition
responsibilities and the future public API boundary remain unchanged; no new
accepted scientific decision number is inferred.

## Public HydrAMP data receiving continuation — 2026-11-03

After the bounded private result, the investigator requests continuing. The
[public data-receiving milestone](hydramp_public_receiving.md) implements the
provisional `HydrAMPReceipt` export, shared strict JSON reading, installed local
wheel checks and user documentation. This is engineering within the existing
receiving responsibilities, not a new scientific decision or broad dev3 adoption.
A public generation execution adapter and final scientific disposition remain
pending. No model/PCA/descriptor/Macrel call or publication is authorized or
performed by this data-only continuation.

## Isolated HydrAMP execution engineering continuation — 2026-11-03

The investigator instructs implementing the isolated public execution step after
installed data receiving. The [adapter record](hydramp_execution_adapter.md)
retains the exact local consumer artifact, controlled/installed transport and
parent-session attribution evidence. One real 16-proposal case is prepared with
three neural forwards and its own exact host/call plan; approval is pending.
This grants implementation and controlled verification, not a new scientific
acceptance decision or model allowance. Existing scientific limits and budgets
remain unchanged.

The investigator also reiterates the existing owning-component issue commitment
for sibling bugs/improvements. The actual descriptive-profile need is reported
in [our HydrAMP #2](https://github.com/uibcdf/hydramp/issues/2), cross-linked to #8.
Expected Ackredit deduplication and a test's wrong DepDigest internal reference
do not establish provider bugs. The initial inherited-environment audit failure
was diagnosed and corrected in the new fixture, without altering other components.
No standing rule is duplicated: root AGENTS.md already carries the common reporting
and external-publication boundaries.

## Approved installed-adapter attempt stopped in qualification preflight — 2026-11-03

The investigator approves the exact single-call plan. Its actual invocation
returns an incomplete receipt before provider/model/PCA loading: the qualifier
lowered the parent's hard virtual-address ceiling to 1 GiB, preventing its child
from setting the already requested 8 GiB. The [failure and correction](hydramp_execution_adapter.md#first-approved-attempt-and-parent-limit-correction--2026-11-03)
retain all original evidence. One API attempt was made; every learned/PCA/
descriptor/Macrel count is zero. There is no scientific numerical outcome.

The qualifier is corrected to parent soft 1 GiB/hard 8 GiB and has a real model-free
inheritance regression, plus nonzero status on incomplete case. The underlying
consumer/provider wheels and scientific source remain unchanged. The original
no-retry attempt is not repeated; a new exact single-attempt proposal awaits
fresh approval. This is routine engineering correction, not a new accepted
scientific decision or wider model/call authority.

## Corrected installed-adapter execution completed — 2026-11-03

The investigator then approved the corrected single installed-adapter case.
It completed with **16 proposals**, exact retained native results/order/indices/
trace, exact saved replay and captured parent attribution (seven records).
The [execution record](hydramp_execution_adapter.md#corrected-installed-public-case-completed--2026-11-03)
reports 8.358 s / 432.2 MiB sampled aggregate RSS and the consumed three-forward
budget. No Macrel, legacy or retry was run; broader scientific disposition is
still pending. The earlier failed startup remains preserved.

This is a separately authorized bounded engineering/scientific execution record,
not a new accepted scientific design decision or broad adoption.

## Consolidated dev3 disposition proposed for review — 2026-11-03

The investigator directs preparation of the [bounded-acceptance report](hydramp_dev3_acceptance_review.md)
after the public adapter case completes. The report recommends exact-bundle
experimental AMP use while preserving probability/global-rank FAILs, numerical
limitations, original use conditions and the lack of a joint Macrel hit in the
small H4 pool. It distinguishes private composition from the separately executed
public adapter. No new scientific evaluation occurs. This is a recommendation,
not acceptance or a D40 extension; #8 remains open for investigator disposition.


## Encoder E2 prepared; approval pending — 2026-11-04

Following completed D42/E1, the investigator directs preparing the next
comparison. The [prospective encoder plan](hydramp_encoder_E2.md) freezes the
same dev4 candidate, selected original23-file encoder,32 distinct token rows
and ten evaluations. Its model-free controls and artificial dual-worker case
pass; real parameter bytes are rehashed only. No new D-number, scientific
acceptance or real execution permission is recorded.

The native reference performs one unused eager64 noise draw during model
construction, in addition to initializer RNG/SVD. This is explicitly counted;
the selected executable excludes random operations. Prospective endpoint bands,
exact bundle/use and finite shared-host limits still need investigator approval.
D41/dev3, D42's artificial-only boundary, D35/M1–M8 and selectors remain unchanged.


## Encoder E2 separately approved and executed — 2026-11-04

The investigator explicitly instructs continuing in response to the exact
execution approval question. The [authorization](evidence/hydramp_encoder_E2_authorization.json)
records plan SHA-256 eb6d30fc31217dee57c9200fcfcff982ebbee0facb12fdeff3b6f9da3b92692b,
prospective criteria, ten evaluations, one unused legacy 64-value construction epsilon
vector/native initializer work and the finite CPU/shared-host envelope.

The [executed outcome](hydramp_encoder_E2.md) passes all original/modern raw
posterior and intermediate comparisons, exact retained repeats and layout/
duplicate controls. Both workers complete once, total 8.127 seconds and peak
sampled process-tree RSS 367.45 MiB. The allowance is exhausted. No new scientific
acceptance/D-number, dev4 adoption, later module or model call is inferred.
D41/dev3, D35/M1–M8/selectors, exact source/artifacts and prior FAILs remain.


## Analogue contract prepared for review — 2026-11-04

After the finite E2 encoder outcome, the investigator directs preparing the next
module. The [analogue work order](hydramp_analogue_work_order.md) recommends a
first native-score-improvement route: explicit local seeded latent noise,
original softmax/conditions, both strict native-score comparisons, occurrence-
preserving results and no optional filters/descriptors. The original sequence-
keyed output loses repeated prototypes; optional filters and source documentation
have separate inconsistencies retained under HydrAMP #4/#7.

This is source review and a proposed contract, not scientific acceptance or A1
implementation approval. No new D-number, array/model load, mathematical test
or call allowance is recorded. Before implementation, the investigators review
input/output meanings, seeded sampling, strict decisions, deliberate occurrence-
interface difference, failure behavior and artificial acceptance criteria.
Discovery/descriptors/filters/transport and any trained comparison stay separate.
D41/dev3, dev4/E2 evidence, D35/M1–M8 and both selectors remain unchanged.


## Post-audit first cycle resumed — 2026-11-04

The investigator directs implementing the reviewed continuation plan. This lifts
the audit implementation pause and resumes existing D43/A1 artificial work.
The original draft hashes and the untested pause state were verified before
editing. The first cycle also includes the receipt diagnostic fix under #34,
a worked AMP evidence report/comparison brief under #33, and preparation of
analogue consumer receiving expectations under #32. Actual later scientific
execution remains governed by its concrete bundle/criteria/host-call review.
This records operational commissioning; it is not a new architecture decision,
a repeat of encoder qualification or a broader biological acceptance.


## Analogue A2 separately approved and executed — 2026-11-04

The investigator explicitly directs continuing in response to the exact A2
approval question. The [authorization](evidence/hydramp_analogue_A2_authorization.json)
binds unchanged plan SHA-256
556c917c1937a564ae047d6b30f3cb91311f50c22d55633eed27be1b808c35d4,
prospective criteria, 42 neural evaluations, the pinned native PCA/constructor
noise and descriptor work, and the finite sequential CPU/shared-host envelope.

The [executed outcome](hydramp_analogue_A2.md) records exact tokens, sequences,
joint strict-score decisions, occurrence buckets/mappings and repeats. The
unchanged probability diagnostic fails, and saved-only analysis exposes separate
AMP near-tie batch sensitivity without a joint/returned-result difference.
Both workers complete once in 25.42 seconds total, peak sampled tree RSS
552.13 MiB. Actual original descriptor bundles are six of the maximum 27.

The allowance is exhausted. No new scientific acceptance/D-number, general
equivalence, consumer redesign API, retry or further model/diagnostic allowance
is inferred. Original/reference/source/wheel identities, D41/dev3, dev4/E2,
D35/M1–M8 and both selectors remain unchanged. Narrow experimental disposition
is recommended for investigator review, preserving the sparse structural
coverage and all numerical failures.


## Analogue consumer R1/R2 delivered under D45 — 2026-11-04

The investigator approves the exact R1/R2 contract in response to its concrete
question. The authorization pins original contract 876ef80c…fd71. The
[implementation record](hydramp_redesign_implementation.md) reports 259 source
tests,101 installed cases and21 artificial network evaluations with exact
direct/adapter/repeat traces and parent/attempt mapping. The missing native
codec is implemented in a separate HydrAMP dev6 candidate; accepted dev5 and
seven numerical/runtime modules remain unchanged. The isolated profile has
clean21-package closure; the shared profile retains its seven known AmberTools
findings under central #82. Initial failed checks and their causes are retained.

R1/R2 are implemented, not a real pretrained consumer qualification. R3 and
Macrel use need their own exact plan/use/criteria/shared-host-call review. D44,
D41, D35/M1–M8, existing selectors, old numerical FAILs and source history remain.
No scientific utility/biological claim, new real allowance, GPU, training,
feedback, other family/target, release, commit/push or external contact follows.

## Separately authorized R3 technical receiving — 2026-11-04

After the exact R3 approval question the investigator authorizes executing plan
7a55b24e8c5d2cc105274e54dec83cf442f80b28211d0f297f55d6c2b1216974.
The [authorization](evidence/hydramp_redesign_R3_authorization.json) records its
unchanged case, bundles/use, criteria and finite shared-host/call limits. The
[R3 outcome](hydramp_redesign_R3_qualification.md) passes direct/adapter/repeat
receiving, Macrel controls and separate parent/child assessment, with actual
Ackredit capture and fresh engine-free replay. All 21 HydrAMP and six ONNX
evaluations complete once; the allowance is exhausted.

The sole returned child improves native AMP/low-MIC-class scores but receives
lower Macrel AMP and higher hemolysis probabilities than its parent. Both
selectors return it under the existing ranking-only policies. Saved A2 outputs
contain the same candidate from original HydrAMP; this is not a newly established
modern-port sequence regression or a biological verdict. Technical workflow
delivery does not establish useful optimization, change D44/D45 scientific
acceptance or authorize another run, feedback, training or publication.
