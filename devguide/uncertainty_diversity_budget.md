# Uncertainty, diversity and budget: bounded P04 synthesis

Status: **C1–C5 accepted and P04 closed conceptually under D32**, 2026-10-26,
on the basis of D27–D31 and their agreed limits. This does not adopt an
implementation, universal selector, confidence scale, probability model or
extension to future horizons. Concrete contracts/interfaces belong to the
capabilities selected next. The [V0.1 alternatives](v0_1_alternatives.md) are
pending scope recommendations, not an already selected release specification.

Navigation: [index](README.md) · [decisions](decisions.md)
· [evaluation meanings](evaluation_and_selection.md)
· [multiobjective and operational cases](multiobjective_optimization.md)
· [next decisions](open_questions.md#p04-proposed-discussion-sequence).

## 1. Distinct uncertainty and evidence limitations

The X/Y/CPP/hemolysis problem retains its scientific meaning. F lacks a Y
evaluation; I has opposing CPP assessments after subject/endpoint/context alignment.
Those cases cannot be reduced to two numbers on one uncertainty scale. The
following distinctions describe actual evidence, not mandatory statuses or classes.

| Situation | What to preserve | Consequence for a particular decision |
| --- | --- | --- |
| Evaluation absent or failed | Not requested, unavailable, unsupported input or failed attempt, with actual cause and resource use where known. | No invented score or adverse biological observation. A failed invocation is a valid execution outcome, not a successful scientific prediction. |
| Predictors disagree | Native outputs, definitions, subjects, conditions and applicability; establish alignment before calling them contradictory. | Retain opposing scenarios or use a qualified aggregation policy. A vote or average does not establish resolution. |
| Model reports uncertainty | What the estimate describes, its scale, construction, validation and limitations when available. | Predictive variance, ensemble spread, classification score and structural confidence are not interchangeable error bars. |
| Applicability is doubtful or outside validated support | Relevant chemistry/data/context mismatch and basis for claiming known, doubtful or unknown support. | D18 permits justified exploratory use, not automatic rejection or a guarantee of calibrated uncertainty. |
| Biological context varies | Target constructs/states, endpoint and relevant conditions associated with each result. | Context variation may change the scientific quantity itself; it is not always noise around one universal value. |
| Chemical information is incomplete | Actual proposal/view, unresolved chemistry, hypothetical completions and attribution limits under P07. | A sequence predictor may operate on available information; a chemistry-dependent method may require explicit realizations. Neither establishes all completions. |
| Models share dependencies or bias | Shared training/evaluation sources, architecture or descriptors where known; preserve unknown dependence. | Agreement is not automatically independent confirmation. Missing dependency information cannot justify multiplying probabilities. |

Unknown chemistry, unknown model error and disagreement about a known molecule
are different. Enumerating hypothetical realizations does not make them equally
probable; several model outputs do not form independent samples of biological
truth. Repeating a deterministic call does not add another independent observation.
Stochastic repetitions may characterize a model's variability; they are not
automatically independent biological observations or calibrated biological uncertainty.

## 2. Decision techniques and their assumptions

| Technique | Usable without calibrated probabilities? | What it establishes and what it needs |
| --- | --- | --- |
| Explicit model/context/chemical scenarios | Yes. | Report choices under identified alternatives and where they agree. Robustness covers those alternatives, not all possible errors. No scenario frequency is implied. |
| Justified intervals or bounds | Yes, if deterministic/logical bounds or explicitly declared sensitivity ranges suffice. | Preserve the origin and meaning of each bound. A model's observed range is not a confidence interval or a bound on biological truth. Statistical coverage needs its own assumptions. |
| Sensitivity analysis | Yes. | Vary defensible weights, transforms, gates or assumptions and examine decision stability. Chosen perturbations are not an estimated error distribution. |
| Robust or worst-case decision over a stated set | Yes. | Useful when an action should withstand the stated alternatives. Can be conservative; an incomplete uncertainty set gives no universal guarantee. Minimax regret additionally needs a common declared decision utility across scenarios. |
| Qualified score/model aggregation | Sometimes; a declared heuristic can operate without probabilities. | Needs compatible endpoints and a justified interpretation/transformation. Preserve components and dependence; aggregation does not turn an uncalibrated score into activity probability. |
| Expected utility, chance constraints, Bayesian information/acquisition | Requires a relevant probabilistic model and additional assumptions. | Declare distributions, likelihood/noise assumptions, dependence, action utility and applicable evidence. Numerical expectation under a model is not a guarantee that model describes biology correctly. |

Perfect calibration is not required to try a justified exploratory ranking under
D18. It is nevertheless incorrect to call a heuristic a calibrated probability,
an information-theoretic expectation or a probability of satisfying the scientific
requirements. Joint claims need joint assumptions: multiplying CPP and binding
classifier outputs does not establish a joint success probability.

**F:** preserve Y as absent. A declared search can use other signals or logical
score bounds, but cannot compute an observed full-objective Pareto comparison by
filling Y. An applicable new Y assessment can change eligibility; if none exists,
the requirement remains unresolved and only permitted actions can continue.

**I:** preserve the two CPP assessments. Compare choices under each qualified
scenario; if they produce different action eligibility, name that instability.
If both support the same action under the declared rule, that decision can be
stable despite unresolved disagreement. A min–max envelope is a scenario range,
not a biological confidence interval. Selecting the favorable source or averaging
incompatible scores would conceal the question rather than resolve it.

For either candidate, different hypothetical chemical realizations must not be
mixed into a fictitious jointly favorable individual. If a policy considers several
realizations, state which and how its decision depends on them, without assigning
unstated population weights. Uncertainty does not supply a missing operation or
waive a scoped invariant under D31.

### Search can exploit its own reward model

Optimizing a predictor can concentrate proposals where its errors are favorable.
This concern is directly addressed in offline model-based optimization by
[Trabucco et al., COMs (2021)](https://proceedings.mlr.press/v139/trabucco21a.html).
The paper's conservative learning approach is an algorithmic precedent, not a
universal bound or an implemented peptide evaluator. [Brookes et al., CbAS (2019)](https://proceedings.mlr.press/v97/brookes19a.html)
also distinguish design from simply maximizing an oracle and assume predictive
property distributions. Neither method is a drop-in solution for arbitrary
uncalibrated resources in PeptideMT.

Candidate protections to qualify per capability include separate search and
assessment roles, held-out assessment where feasible, checking training/source
overlap, inspecting descriptor/domain drift, testing sensitivity, limiting a
particular search region or reserving exploratory/assessment budget. None is a
mandatory global policy. Repeatedly tuning against a held-out model turns it into
part of selection; changing its access route does not restore independence.
High agreement among related predictors does not rule out shared exploitation.
Search-reward improvement remains a computational result rather than independent
evidence of activity. No experimental data are required to finish a computational run.

[Ovadia et al. (2019)](https://papers.neurips.cc/paper_files/paper/2019/hash/8558cb408c1d76621371888657d2eb1d-Abstract.html)
evaluate predictive uncertainty under dataset shift and document limitations of
post hoc calibration on their classification benchmarks. This supports checking
applicability separately; it is not peptide-specific validation or proof that any
particular ensemble detects all out-of-domain cases. No papers' code was executed.

## 3. Diversity relative to the scientific purpose and available view

Diversity is optional and purpose-specific. Its measure, comparison set and
representation matter; a large distance does not establish useful novelty.

| Diversity sought | Possible operational approximation | Limits, especially for partial representations |
| --- | --- | --- |
| Sequence | Hamming distance for aligned equal-length compatible alphabets; edit/alignment distances, sequence clusters or qualified embeddings. | Length, tokenization and modifications affect meaning. A comparison on known positions needs coverage; unknown residues are not automatic differences or matches. |
| Chemical and stereochemical | Molecular-graph/feature comparisons including relevant bonds, modifications and stereochemistry; declared chemical groups. | A feature scheme ignoring chirality can collapse stereoisomers. Unspecified stereo/termini are unknown, not assumed equal or different. Canonical identity and state grouping remain deferred. |
| Structural and conformational | Atom-mapped aligned coordinate distances, contact patterns or comparison of conformational ensembles. | Atom correspondence, alignment, target frame and states matter. One predicted conformation or best matching pair does not measure an entire ensemble. A backbone supports only the declared structural comparison. |
| Functional | Qualified activity/annotation profiles or model-output patterns under aligned family definitions. | Predicted-profile diversity is not demonstrated biological diversity. Missing labels are not negatives; source thresholds and dependence matter. |
| Mechanism or recognition site | Qualified site labels, mapped target contacts or interface patterns; mechanism annotations when supported. | Different poses do not prove different mechanisms. An unassigned site/mechanism is not a new mechanistic class. Cross-target comparison needs justified correspondence. |
| Objective profile | Distances, clusters or coverage in the declared comparable objective vector. | Scales, transformations and uncertainty affect distance. Nondominance alone does not imply broad spread or chemical diversity. |
| Generative provenance | Source/strategy/checkpoint/lineage coverage, where actually observable. | Multiple paths can reach the same molecule. Preserve both paths without counting that molecule twice as chemically diverse. Different source labels need not mean different chemistry. |

A sequence-only proposal can be compared in sequence space within its stated
scope; it cannot silently receive fully specified chemical/structural distances.
Different hypothetical realizations can support conditional comparisons, not a
default best-of-completions diversity bonus. Technical inability to compute one
metric permits another justified limited-purpose metric or an unresolved result,
not invented distances. No universal metric or complete chemistry ontology is needed.

| Where diversity is used | Potential role | Important distinction |
| --- | --- | --- |
| Generation/exploration | Multiple sources, restarts, novelty pressure or alternative search regions. | Can change what is explored, but needs actual provider operations. |
| Population maintenance | Niches, clustering, quotas or diversity-aware survival. | Affects subsequent search; not equivalent to a final diverse shortlist. |
| Result conservation | Retain modes/tradeoffs and convergent provenance; optionally summarize/truncate an active archive. | Original evaluations remain attributable; an active archive is not a compulsory Pareto structure. |
| Final batch selection | Cluster representatives, max–min distance or another qualified set policy among candidates eligible for that action. | Can avoid redundancy but cannot recover modes never generated or override noncompensable prerequisites. |

For F and I, missing Y and CPP disagreement do not automatically make them diverse
or informative. Two different sequences may prompt nearly redundant evaluations;
one candidate may support several complementary assessments. Correlated
physicochemical signals can drive both reward and apparent diversity. Report what
the selected approximation actually distinguishes rather than claiming all seven
forms of diversity at once.

## 4. Candidate selection, evaluation actions and budget

A computational action is a particular evaluation or supported operation on an
identified subject/view, not merely a candidate name. Different actions on F or I
can have different cost, applicability and implications. Distinguish four purposes:

| Purpose | Possible policy without calibrated probabilities | What it must not imply |
| --- | --- | --- |
| Choose highest-scoring candidates | Rank compatible values under a declared scalar, Pareto or hierarchical rule. | High reward is not low uncertainty, broad diversity or best next information. |
| Choose a diverse batch | Apply a qualified distance/group/set policy within the action's prerequisites. | Different candidates do not necessarily provide independent information. |
| Probe uncertainty or disagreement | Choose relevant unresolved/scenario-sensitive cases with a stated rationale. | Largest ensemble spread or absent evaluation is not automatically greatest information value. |
| Request an evaluation that could change a decision | Identify which requirement, ordering or action eligibility its possible outcomes could affect, check applicability and compare cost. | A qualitative decision-impact judgment is not expected value of information. |

For F, Y assessment is relevant if its possible outcomes would affect continuation
or selection. For I, another CPP assessment is useful only if it can address the
conflict or alter the contemplated decision. Repeating the same deterministic
prediction or buying an unrelated expensive structure result may not do so.
If every plausible outcome would leave the action unchanged, another candidate
or evaluation may better serve that purpose; novelty alone does not decide.

Thousands of proposals can be screened or grouped cheaply where actual compatible
operations exist, then receive selected costly structural evaluations or simulations.
This is an optional plan, not a mandatory cheap-to-expensive pipeline. A cheap
proxy can wrongly eliminate relevant modes; a molecular simulation is not a
universal ground-truth affinity, CPP or hemolysis assay. Each evaluation retains its
endpoint and uncertainty. Some plans will need expensive evidence early.

**Invented allocation example, not a timing or performance estimate:** suppose a
budget of 20 task-specific cost units, Y assessment of F costing 6, a relevant CPP
assessment of I costing 8, structural assessment of another high-X candidate J
costing 12, a cheap functional assessment of K costing 2, and a simulation costing
40. J/K are placeholders, not new selected scientific cases. A declared ranking
policy might spend 20 on J/F/K; a policy focused on F/I might spend 14 and reserve
6. Neither is established as optimal. The simulation cannot fit this budget.
Leaving budget unused is valid; no evidence warrants a universal allocation ratio
or claiming an expected information gain from these invented costs alone.

[PESMO](https://proceedings.mlr.press/v48/hernandez-lobatoa16.html) is a primary
precedent for probabilistic multiobjective information acquisition with separately
evaluated objectives and potentially different costs. Its information criterion
needs its statistical model; the qualitative policies above need not estimate it.
Expected value of information additionally requires possible-outcome probabilities
and a decision utility/model. Without them, describe anticipated decision relevance
or a declared heuristic rather than reporting a fabricated expectation.

### Accounting, reuse, failures and observability

Preserve estimated versus observed costs, their scope and meaningful units. A
budget can constrain calls, hardware time, money or several resources separately;
no universal scalar cost is required. Wall-clock time of parallel calls is not
their summed device time. Batch/shared preparation cost is not automatically a
sum of per-output costs; one multi-label invocation is not 21 independent calls.

Record requests and outcomes, preparation/transformation work, internal operations
when observable, failures, retries and cancellations. Failed work consumes resources
without becoming a successful prediction. Partial outputs need their actual
qualification. If an engine exposes only aggregate use or incomplete internal
traces, record those limits, not fabricated per-trajectory accounting. A strict
internal-call budget cannot be promised through a route unable to enforce or observe it.
Stopping, failed evaluation, exhausted budget and an empty selection can all be
legitimate reported outcomes without implying scientific satisfaction.

Reusing an evaluation avoids recomputation only under justified equivalence of
the actual subject/view, model/configuration and relevant context. Preserve its
original source and the new use; a cache hit is not new independent evidence.
Chemical completion, state change or model update may invalidate that reuse.
Keep computational reuse distinct from scientific transfer under P07. Preserve
convergent provenance even when equivalent computations share one result.

A plan can use rolling budgets, reserve allocations or adaptive stopping if their
policy is approved. Estimates may change; report actual use and any excess rather
than retrospectively redefining the budget. The implementation may schedule within
agreed rules; it cannot silently substitute methods, weaken prerequisites or
invent outcomes to fill a final batch.

## 5. P04 synthesis: accepted principles and closure recommendation

| Accepted basis | What is already settled conceptually |
| --- | --- |
| D27 | Evaluation, knowledge of feasibility, action-specific selection and bounded computational claims have different meanings; no mandatory global candidate grade. |
| D28 | PeptideMT preserves native scientific results and local rationale, not a general research/project claim adjudicator. |
| D29 | Scientific requirements, operational checks and many-to-many evidence links are distinct; score predicates are not exact biological tests. |
| D30 | Preserve original objectives/evaluations; permit different exploration/optimization and selection policies on one problem, with contextual optional Pareto comparisons. |
| D31 | Restriction scope is problem/procedure/action-relative; required conditions cannot be bought off by rewards. Relaxation must be authorized; guarantees require actual means; valid empty/failed/unresolved outcomes and contextual fronts retain provenance. |
| D32 | All C1–C5 principles and conceptual P04 closure are accepted; capability-specific contracts/interfaces and algorithms remain to select. |

D09, P07, P08 and P09 remain supporting agreements, not new decisions reopened
here. Incomplete proposals, qualified exploratory predictors and optional provider
capabilities remain compatible with the P04 meanings above.

### Five additional principles accepted under D32

**All C1–C5 below are conceptually accepted under D32.** Their local labels are
retained from the closure proposal; they are not five separate decision IDs.

1. **C1 — Qualified uncertainty:** preserve the different sources, scope and
   dependence of uncertainty/evidence limitations. Permit scenarios, sensitivity,
   justified bounds and qualified probabilistic methods without a mandatory
   confidence scale, automatic aggregation or unsupported probability interpretation.
2. **C2 — Purpose-specific optional diversity:** a diversity policy declares what
   differences, representation and comparison set matter for its use. Partial
   representations do not authorize invented chemistry, distances or mechanism;
   diversity need not be an objective or component of every procedure.
3. **C3 — Distinct acquisition purposes:** high score, diversity, uncertainty
   probing and potential effect on a decision are different selection grounds.
   Allow heuristic or probabilistic acquisition with explicit assumptions;
   no expected information-value claim without the necessary models.
4. **C4 — Honest resource and reuse evidence:** preserve estimated/actual cost,
   observable operations, failures and trace limits; qualify reuse and keep it
   distinct from new independent evidence. Budget policies and stopping must not
   silently change the scientific problem or declared action prerequisites.
5. **C5 — Reward exploitation remains an assessment concern:** retain the roles
   and dependencies of reward and assessment models, applicability limits and
   available checks against shared bias. Optimizing a reward is not independent
   confirmation; no particular safeguard or independent evaluator is universally required.

These accepted principles specify meanings/obligations, not a universal policy
engine. Some restate consequences of previous agreements to make closure explicit.
Approval does not adopt every example, measure or algorithm in this document.

## 6. Deferred contracts, algorithm alternatives and coherence

**Capability-specific contracts can wait:** supported chemistry/representations,
actual model inputs/outputs and uncertainty meaning, applicability evidence,
chosen comparisons and numerical tolerances, candidate-edit/invariant support,
selected diversity approximation, acquisition/budget enforcement and observable
trace guarantees. Qualify failures, reuse equivalence and scientific acceptance
criteria for the small capabilities chosen for V0.1. Canonical identity, state
grouping, public interfaces, persistence and P02/P03/P05/P06/P10 retain their
separate disposition. This is not approval to implement unsupported behavior.

**Algorithms are alternatives, not architecture:** weighted/desirability or
Tchebycheff utilities; nondominated sorting; epsilon constraints or lexicographic
ordering; evolutionary/local search or native guidance; scenario/interval robust
selection; qualified Bayesian acquisition; clustering, farthest-point/max–min or
other set selection; staged or adaptive evaluation allocation. Their actual
capability requirements differ. No single algorithm or implementation of all of
them is needed to close P04. Some may never be prioritized.

**Bounded coherence check:** no unresolved conceptual contradiction was found in
the current cases. The following distinctions resolve apparent tensions:

| Apparent tension | Resolution within the accepted architecture |
| --- | --- |
| Strict scientific requirement versus incomplete evidence | Preserve strictness and unresolved fulfillment; only actions whose prerequisites allow it may proceed. |
| Search invariant versus opaque generator internals | Qualify the scope actually enforced/observed. A final-output check does not establish every internal state's compliance. |
| Exploratory OOD reward versus reliable assessment | Justified search utility and scientific applicability remain distinct; neither creates missing evidence. |
| Conservative decisions versus novelty/diversity | Let action-specific policies declare the tradeoff; neither conservative rejection nor diversity pressure is universal. |
| Pareto/score improvement versus biological quality | Derived comparisons retain evaluators, context and pool; independent scientific support is not inferred from optimization alone. |
| Reproducibility versus adaptive policies/budget | Preserve the rule, actual decisions, evidence snapshot and costs; reproducibility does not universally promise deterministic outputs. |

This is a conceptual case analysis, not a proof that every future algorithm is
scientifically valid. A later capability exposing a real semantic conflict must
return it to discussion, but speculative future features are not a closure gate.

## 7. Formal closure proposal and PeptideMT V0.1 handoff

**Accepted resolution (D32):** close P04 conceptually
on the basis of D27–D31 plus C1–C5. Treat uncertainty, diversity, resource allocation
and selection as qualified, interchangeable plan policies acting on preserved
evidence, within scoped restrictions and declared scientific purposes. Do not
adopt interfaces, algorithms, universal thresholds or a general decision engine.
Capability-specific contracts and choices move to subsequent bounded specifications.

**Current disposition: P04 is closed conceptually.** The investigators explicitly
approved C1–C5 and closure after the preceding revision's proposal. This does not
authorize implementation or issues, choose algorithms or freeze interfaces.

The next milestone is **define PeptideMT V0.1**, with a small useful set of
scientific capabilities, not every alternative reviewed. The specific
[V0.1 comparison](v0_1_alternatives.md) now supports that decision. Choose its
intended use/chemical envelope and capability shortlist, then
record each capability's minimum scientific contract, concrete positive/negative/
incomplete/conflicting cases, failure behavior and acceptance evidence. Only then
authorize implementation under D14 and the existing MolSysSuite admission/starter
route. No definitive generator, first demonstrator, chemistry envelope or API is
selected here; P10 and future horizons add no V0.1 requirement.

This update reviewed primary papers and prior pinned ecosystem evidence. No model
was installed, invoked or benchmarked; no molecule, experimental protocol, software
capability or scientific validation was produced. The allocation numbers are invented.
