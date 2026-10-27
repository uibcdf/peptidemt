# Evaluation, feasibility, selection and scientific claims

Status: **P04 alternative 2 and seven principles accepted (D27–D28); X/Y
requirement/check/evidence alternative 2 accepted (D29); optimization policies pending**,
2026-10-26. No selector,
feasibility taxonomy, API or implementation is approved. **P04 is closed
conceptually under D32**, including C1–C5; concrete capability policies/contracts
remain unselected. P09
stays conceptually closed and P10 stays pending without an MVP obligation.

D30 subsequently accepts distinct exploration, preserved results/tradeoffs and
purpose-specific selection over the same problem, with original objectives and
evaluations retained. It selects no algorithm or mandatory Pareto archive. The
[operational case](multiobjective_optimization.md#11-operational-stress-test-four-candidates-three-purposes)
compares three actions; concrete restriction, uncertainty, diversity and budget
policies remain capability-specific.

D31 now accepts the scoped-restriction treatment with seven qualifications,
including honest internal-versus-final guarantee scope and legitimate empty,
failed or unresolved outcomes. The [bounded P04 synthesis](uncertainty_diversity_budget.md)
records C1–C5 and conceptual closure accepted under D32. The current
[V0.1 comparison](v0_1_alternatives.md) turns those principles into proposed minimum
contracts and acceptance cases without selecting models, interfaces or a demonstrator.

Navigation: [index](README.md) · [decisions](decisions.md) · [P04 agenda](open_questions.md#p04-proposed-discussion-sequence)
· [families](functional_families.md#selection-contradictions-and-assessment)
· [multiobjective discussion](multiobjective_optimization.md)
· [capabilities](capabilities_and_composition.md) · [ecosystem audit](integration_audit.md).

## 1. Alternatives and accepted conceptual separation

PeptideMT needs to support scientifically justified choices, not just emit ranked
sequences. It need not become a general decision system. Three alternatives are
plausible before choosing a concrete representation:

| Alternative | Strengths | Limits / cost |
| --- | --- | --- |
| Evaluation outputs with selection-specific checks; scientific conclusions remain external annotations | Small initial surface; useful for a bounded filtering/ranking tool. | Feasibility assumptions and the basis for conclusions can become scattered across policies and notebooks. Comparing the same evidence under different purposes is harder. |
| Four explicit semantic responsibilities, connected by evidence and context | Separates what was evaluated, constraint knowledge, the purpose/policy of a choice and the supported conclusion. Allows different policies without rewriting original results. | Needs careful attribution and purpose-specific interpretation, but does not require four objects or automatic claim verification. |
| General decision-theoretic engine with beliefs, utilities, actions and experiment planning | Can formalize sophisticated information/cost tradeoffs when those models exist. | Requires assumptions and infrastructure not justified by the current cases; risks duplicating MOLI methodology/project orchestration. Optional specialist optimizers can come later. |

**Accepted conceptual choice (D27):** the second alternative. Preserve the meanings below
without requiring separate classes, services or a fixed order of execution.
A scalar score may remain useful for a particular policy; it must not replace
the available evaluations or become a candidate's mandatory global quality label.

| Responsibility | Question answered | Important qualification |
| --- | --- | --- |
| Evaluation | What property was measured/estimated, on which subject/view, by which method and under what conditions? | Preserve raw output, meaning/units, applicable context, provenance, available uncertainty and failures. A prediction is not a measurement of activity. |
| Feasibility assessment | What evidence supports satisfaction or violation of the applicable restrictions, and what remains unresolved? | Relative to a specified requirement set, subject and context, not an intrinsic universal candidate status. Computed pass/fail can be about a surrogate rather than the scientific requirement itself. |
| Selection decision | Which candidates are chosen, for what next purpose, using which policy, evidence and budget? | Eligibility for an action is different from scientific feasibility; eligible candidates may remain unselected for cost or redundancy. Selection itself adds no activity evidence. |
| Scientific claim | Which specific conclusion is supported, by what evidence and with which limits? | Can be a bounded computational conclusion. No automatic certification, universal evidence ladder or requirement for experiments before computational completion. |

These responsibilities are not four new pillars added to D09. The **problem**
states desired properties and restrictions; the **plan** binds estimators,
operational criteria and purpose-specific policies; **execution evidence** records
actual inputs/results and the assessments/decisions based on them. Scoped claims
reference that evidence and its assumptions. Researchers may annotate them;
PeptideMT must not infer all scientific conclusions or adjudicate them generally.
D28 explicitly limits its conclusions to the native computational evidence and
selection rationale. Global research interpretation and project-level claim/
decision management remain with investigators and, eventually, appropriate MOLI
components, especially Nextia. This does not prevent interpretable local results.

A candidate can have strong evidence for one property, weak evidence for another
and no evaluation of a third. Its feasibility assessment can change when the
requirements, context or evidence change, while original evaluations remain intact.
Keep the evidence snapshot/references used for a past decision; later results
can motivate a new decision without retroactively justifying the old one.
Changing a scientific requirement revises the problem; changing a reward or
operational selection rule revises the computational plan. Neither should silently
redefine the other or change the scientific meaning of a functional family.

## 2. Strict requirements, operational criteria and unresolved knowledge

**Strictness and checkability are independent.** A scientific requirement can
be strict and meaningful even when no available evaluator establishes it. For
example, a declared maximum sequence length may admit an exact check on a known
sequence, whereas selectivity over a biological panel may remain incompletely
assessed. Do not weaken the latter into a score threshold just because a model
is available, or silently remove it because no suitable model exists.

State what the restriction applies to: an admissible final design, a particular
evaluation subject, an allowed edit or an action under consideration. This does
not prescribe mandatory stages. A known violation can forbid accepting a design
as satisfying the problem while still allowing a plan to use it for repair or as
a comparison/control, if that use is permitted. It does not waive the restriction
or make the original candidate feasible; redesign produces its own attributed
proposal/realization. Some restrictions may forbid the proposed use itself.

The following are meanings, not a proposed enum or global state machine:

| Situation | What follows scientifically? | Possible effect on eligibility, depending on purpose/policy |
| --- | --- | --- |
| Established violation of an applicable strict scientific restriction | The candidate does not satisfy that restriction under the established scope. The basis must support this claim, rather than merely be an adverse predictor score. | Ineligible for a decision requiring satisfaction of that restriction. A permitted repair/control use can have a different eligibility criterion. |
| Failure of a model-specific operational cutoff | The output fails that stated computational criterion. It does not by itself establish biological inactivity or violation of the underlying scientific requirement. | A policy may exclude it from one screening route, retain it for another purpose or send it for further assessment. Record the rule and its meaning. |
| Missing required evaluation or an evaluation failure | The relevant requirement is unresolved; a failed computation is not evidence of a negative biological result. | Cannot count the missing check as passed. May be a priority for evaluation; an action requiring that evidence can remain unavailable. Exploratory selection needs its own stated basis. |
| Apparently contradictory evaluations | First establish comparable property definitions, chemistry/views, conditions and methods. If genuinely discordant, preserve both results and the unresolved interpretation. | Can motivate discriminating evaluation, conditional selection or a policy-specific exclusion. No automatic average, majority verdict or universal penalty. |
| Mechanically valid but empirically out-of-domain evaluation | The result is an extrapolative signal with limited support, not automatically a calibrated probability, absence of an evaluation or measured failure. | D18 permits justified exploratory guidance. A decision requiring stronger applicability evidence cannot treat extrapolation as if that evidence existed. |

Input incompatibility is different from empirical extrapolation: a method that
cannot accept the required molecular information does not gain that capability
through an exploratory-use label. An explicit projection/realization may permit
another evaluation, with its attribution limits under P07/P09.

Disagreement may arise from different contexts or chemical realizations rather
than conflicting estimates of the same property. Correlated models do not count
as independent confirmations merely because they have different names. Nor is
disagreement alone a calibrated uncertainty estimate. These distinctions qualify
use without requiring that every resource provide probabilities or error bars.

**Accepted conceptual implication (D27):** feasibility retains restriction-by-restriction
knowledge where relevant, without requiring one global verdict. Eligibility
should be explained for the proposed action. A later policy may define an
aggregate or evidence gate, but must identify its scope and assumptions.

## 3. A, B and a third candidate with conflicting predictions

These are illustrative profiles, not generated molecules or empirical results.
Assume A's more favorable target prediction and B's less favorable one are
meaningfully comparable within a declared method/context. Without that assumption,
even their target ranking would need qualification.

| Candidate | Available information | What is not supplied by the example |
| --- | --- | --- |
| A | More favorable predicted target recognition; no relevant antitarget assessment. | Selectivity, actual binding and overall quality are not established. A missing assessment is not an observed selectivity violation. |
| B | Less favorable target prediction; more complete computational assessment. | Completeness says neither that the additional results are favorable nor that the methods are more reliable or independent. B is not automatically selective or preferable. |
| C | Two predictors give conflicting assessments of an intended property. | Confirm comparable subjects/endpoints first. The profile alone gives no trustworthy consensus, exact uncertainty or value of resolving the disagreement. |

### Different purposes can support different choices

Every cell below is a conditional rationale, not a default recommendation to
choose that candidate. Budget, applicability, action requirements and actual
results can change the choice.

| Selection purpose | Possible role of A | Possible role of B | Possible role of C |
| --- | --- | --- | --- |
| Continue optimization | Promising target signal can justify exploration while selectivity remains unresolved. | Additional results can help monitor tradeoffs or constraints, if informative. | Can preserve an alternative hypothesis/region or test whether disagreement persists during redesign. |
| More expensive molecular evaluation | A relevant antitarget evaluation may address a decision-changing gap. | Further work is useful only if it could affect the decision; completeness alone does not justify more computation. | A discriminating method may clarify the conflict; expense alone does not confer accuracy or independence. |
| Reduce important uncertainty | Investigate the missing assessment if that knowledge matters to the next decision. | Refine a consequential uncertainty that remains despite broader coverage. | Resolve genuinely comparable disagreement if the possible outcomes would affect action. |
| Explore another region | Requires actual novelty/diversity information, absent from this profile. | Same: evidence completeness does not imply redundancy or novelty. | Disagreement alone does not prove a distinct molecular or functional region. |
| Include in an experimental library/panel | Could test a promising but incomplete hypothesis under explicit panel criteria. | Could supply a comparison with broader computational evidence, depending on its content. | Could test a discriminating hypothesis. Library-level design remains pending P10; selecting individuals does not implement it. |
| Propose synthesis and later assessment | Possible for a declared exploratory purpose if its prerequisites permit the missing evidence. No selectivity claim follows. | Possible if actual results and relevant requirements support that purpose, not merely because the profile is more complete. | Possible as a deliberate test of disagreement, with unresolved interpretation visible. |

A lower-reward candidate can therefore be valuable for information or coverage.
But missing information and disagreement do **not** automatically imply high
information value. An evaluation's usefulness depends on what it could change,
its cost, possible outcomes and relevance. Quantitative expected-value policies
need additional probabilistic/utility assumptions; no such model is selected.
Qualitative, documented prioritization can be useful before those models exist.

### Examples of supportable claims

- **A:** 'Under model M and the specified view/context, A scored more favorably
  for target recognition than B; the relevant antitarget property is unassessed.'
  This does not assert affinity, selectivity or biological function.
- **B:** 'B has evaluations covering additional specified endpoints.' If those
  results favor the requested behavior, a further statement can name that
  computational support and scope. The supplied example alone does not establish it.
- **C:** 'The two named evaluators disagree for this aligned endpoint/view/context.'
  Preserve both outputs and limitations. Selection to investigate the discrepancy
  does not resolve it or prove either biological interpretation.

These are scientific statements about bounded computational evidence; they are
not universal confidence levels. Selecting A, B or C for synthesis, optimization
or information gathering adds a decision rationale, not independent evidence of
activity. Experimental observations, if later obtained, form new attributed evidence.

## 4. Coherence with the accepted architecture and ecosystem

| Accepted basis | Consequence for this proposal |
| --- | --- |
| D09–D13 | Keep scientific intent separate from estimator criteria and selection policy. Family meaning is not a cutoff; different optimizers can address the same problem. |
| D15–D16 | Attribute each evaluation to its actual proposal/realization/view and assumptions. No automatic transfer across chemical completions; retain convergent paths. |
| D17–D20 | Preserve qualified functional mappings, indirect/exploratory signals and search-versus-assessment roles. A resource may serve several roles without becoming independent validation. |
| D21–D26 | Strategies require actual compatible operations; plans choose explicit policies/compositions; execution records what happened. A purpose does not create a missing evaluator, and unknown support remains unknown. |
| D27–D28 | Alternative 2 and all seven principles are accepted; local computational conclusions remain interpretable without a general scientific/project-claim engine. Concrete constraint and selection policies are still open. |
| D29 | Requirements, operational checks and many-to-many evidence links are distinct; links alone do not establish sufficiency. Preserve original evaluations and qualified comparisons, with action-relative eligibility and no default treatment of missing Y as selectivity. |
| D30 | Preserve original objectives/evaluations while permitting different exploration and selection policies. Explored sets, comparable derived fronts and action-specific choices have distinct meanings; no mandatory Pareto archive or absolute candidate Pareto status. |
| D31 | Restriction scope is problem/procedure/action-relative; required conditions cannot be compensated by reward. Authorized relaxation cannot change science silently; actual operations/evaluators bound guarantees. Final checks do not prove every internal state's compliance; empty/failed/unresolved outcomes and contextual fronts retain their actual meaning/provenance. |
| D32 | C1–C5 and conceptual P04 closure are accepted; concrete uncertainty, diversity, budget and selection policies belong to the selected capabilities, not a universal decision engine. |

The [preserved audit](integration_audit.md) remains the source-level basis for
owner boundaries; this discussion does not claim new ecosystem implementations:

- **PeptideMT:** peptide-specific objective/constraint interpretation, evaluation
  associations, feasibility/eligibility rationale and selection results; bounded
  conclusions referencing native evidence. No general scientific-claim adjudicator.
- **MolSysMT and specialist MolSysSuite tools:** supported molecular subjects,
  transformations and qualified domain computations. PyUnitWizard owns shared
  physical quantities/units; it cannot make unrelated model scores comparable.
- **Praxis:** reusable methods/protocols and cross-tool execution within its
  audited experimental maturity; PeptideMT retains native search/selection meaning. No duplicate
  workflow planner is proposed.
- **Recorda:** observable operation recording, with native result identity and
  application-owned sessions; recording is not endorsement or scientific validity.
  See the inspected [activation tests](https://github.com/uibcdf/recorda/blob/ff52fa5d8628d796f413b833c8abe73907990cf9/tests/test_activation.py).
- **Nextia / Sabueso / MOLI agent:** future project-level decisions/evidence,
  qualified source assertions and optional reasoning. PeptideMT may retain its
  own scoped selection rationale without implementing a project-wide decision
  engine or requiring those proposed platform capabilities to exist.

SMonitor, ArgDigest and DepDigest can support diagnostics, arguments and optional
availability. Their checks do not determine scientific feasibility or justify a
claim. Scope/independence judgments are not disguised as generic argument validation.

## 5. Seven accepted principles before multiobjective policies

**All seven principles below are conceptually accepted under D27**, qualified by
D28's MOLI boundary. They do not adopt a selector, field inventory or class model.

1. Distinguish evaluation, feasibility knowledge, purpose-specific selection and
   scientific claims as meanings, without four mandatory classes, stages or one
   global candidate grade.
2. Preserve actual evaluation subjects/views, methods, context, output meaning,
   provenance and available uncertainty. Derived scores and assessments reference
   original results; a new policy or later evidence does not rewrite them.
3. Interpret feasibility relative to the restriction set and its scope, retaining
   supported satisfaction/violation and unresolved knowledge. Scientific strictness
   does not guarantee an exact evaluator or permit replacing a requirement by a proxy.
4. Make selection purpose, policy, action prerequisites, evidence used and relevant
   cost/diversity reasons explicit. Eligibility, selection and scientific success
   are different; a nonselected candidate is not thereby infeasible or inactive.
5. Preserve strict violations, cutoff failures, missing/failed assessments,
   conflicting results and doubtful applicability as distinct situations. No
   universal penalty, missing-as-zero rule, average or rejection policy is adopted.
6. Scope claims to what evidence supports, with unresolved properties visible.
   Improving reward or choosing a candidate does not add independent functional
   evidence. Computational completion and exploratory selection need not await assays.
7. Allow different search/selection methods for the same scientific problem.
   Retain objective meanings and transformations, policy versions, actual budgets
   and selection reasons so their outcomes can be compared without one universal
   optimization strategy.

For **policy-only comparisons**, hold the candidate pool and evidence snapshot
fixed where possible to isolate policy effects. For **end-to-end search comparisons**,
different candidates/evaluators may occur: preserve problem scope, explicit budgets,
coverage, reused versus new evaluations and actual costs. Do not call those two
comparison designs equivalent or count cached evidence as newly obtained evidence.
Use independent assessment where available without claiming independence merely
because a model is called through another route.

## 6. Next discussion and what remains deferred

**Resolved conceptually:** the four semantic responsibilities and purpose-relative
eligibility/feasibility distinction. The X/Y case below now tests a specific
scientific requirement, its operational checks and evidence for different actions.
Its requirement/check/evidence organization is now accepted under D29; no universal
threshold or minimum evidence bar follows from that approval.

The [multiobjective analysis](multiobjective_optimization.md) now compares scalar,
Pareto and hierarchical/constrained policies, uncertainty, diversity and budgets
on an invented X/Y/CPP/hemolysis example. D30 accepts search/results/selection
separation; its concrete policies and proposed contract obligations remain pending.
P10 stays pending; no library
engine or general decision/planning system is needed for the present analysis.

Investigators should settle scientific meaning, constraint scope, allowed proxy
use, evidence prerequisites and the purpose of policies. Later Codex may choose
internal data structures, batching, dispatch, caches and reporting within approved
contracts. Changing a molecular projection, a restriction, missing-data behavior
or the scientific interpretation is not merely an internal implementation choice.
Concrete APIs, identifiers, persistence and acceptance tests remain to be specified
for capabilities authorized later. No code or development issues are introduced.

## 7. Selectivity case: bind X while avoiding homolog Y

Status: **hypothetical scientific case; alternative 2 accepted conceptually (D29)**.
X and Y are placeholders, not selected targets; no candidate, evaluation or assay
is produced. D27–D29 apply; numerical policies and concrete representations remain open.

### Scientific requirement independent of evaluators

The intent is a peptide with the required recognition of protein X and sufficiently
limited recognition of homolog Y **under the intended context**. Identify which
X/Y constructs, molecular states/sites and peptide chemical species the claim
concerns. Y is the declared antitarget; avoiding Y does not establish selectivity
against every other protein. Homology motivates the comparison, not its outcome.

Recognition of X and avoidance of Y are distinct requirements. A relative advantage
over Y can coexist with recognition of X too weak for the intended use; similarly,
strong X binding does not establish acceptable Y binding. Whether the scientific
requirement is relative discrimination, an absolute bound on Y recognition, or both
must be clarified for the problem, without adopting a universal threshold here.
Binding selectivity is also distinct from functional/cellular selectivity or a
claim about downstream mechanism.

The problem may initially express a qualitative requirement; an implementable
decision later needs sufficiently clear meaning and action prerequisites. A
scientifically chosen numerical requirement can belong to the problem. Model
cutoffs, score transformations and evidence gates belong to its computational
plan and cannot silently redefine that requirement. If no adequate Y evaluator
exists, preserve the requirement as unresolved rather than replacing or deleting it.

### Exact checks and biological estimates

| Check or assessment | What may be established exactly? | What remains conditional or estimated? |
| --- | --- | --- |
| Known sequence length or a declared chemical feature | A supported deterministic check can establish the stated predicate on the supplied information. | Unknown chemistry cannot be checked as known; no universal initial chemistry support is assumed. |
| Correct X/Y input identity, chosen chain and evaluated view | Consistency with the specified references and mappings, where the information is available. | Correct bookkeeping does not prove the target's physiological state or a bound pose. |
| A predictor output passes a cutoff, or an arithmetic comparison is computed | The mathematical condition on those reported numbers can be checked. | Biological truth and scientific applicability of those numbers are not thereby exact. |
| Binding/avoidance in the intended context | Qualified measurements or predictions can support a scoped assessment. | Method limitations, uncertainty, construct/state differences and unassessed contexts remain; strictness does not create an exact oracle. |

Thus a hard *operational* cutoff can be checked exactly while the scientific
requirement it approximates remains incompletely supported. Conversely, a hard
scientific requirement remains meaningful even if no reliable check is available.

### Affinity, structural confidence and indirect indicators

If comparable equilibrium dissociation constants are available for the **same
peptide species** against X and Y, an optional descriptive quantity is
**S = Kd(Y) / Kd(X)**; larger values describe relative preference for X under
those assumptions. This uses the equilibrium binding meaning of Kd, as distinguished
from association constants in the [IUPAC terminology](https://goldbook.iupac.org/terms/view/14131).
It is an illustration, not a selected objective or universal selectivity rule.

Both quantities need compatible definitions, units, binding models and relevant
conditions. Retain estimates, uncertainty/bounds and measurement versus prediction
provenance. An undetected Y signal is not automatically zero binding or an infinite
Kd; a censored/bounded result must remain such. Predicted ratios remain predictions,
and the ratio alone does not establish sufficient X recognition.

Complex confidence, predicted geometry, contacts and docking scores can inform
plausibility or guide exploration. Favorable X scores and unfavorable Y scores
do not automatically provide an affinity ratio. Poor confidence for a Y complex
can reflect prediction failure rather than absence of binding. Using the same
engine for both proteins does not establish cross-target calibration. Arbitrary
normalization or subtraction cannot supply a missing scientific correspondence.

Even an output named 'affinity' needs its actual definition and domain. At the
inspected [Boltz-2 interface](https://github.com/jwohlwend/boltz/blob/b1ebfc46ecf57f5414e0d1a6f9027bbb122c53bc/docs/prediction.md),
the affinity head is for small-molecule ligands with protein targets and its value
output is IC50-derived; it is not an established peptide-chain Kd estimator.
This is a bounded capability observation, not selection of an evaluator.
PyUnitWizard can preserve/convert compatible units, not calibrate unrelated scores.

### Missing, conflicting and noncomparable evidence

- **Y not evaluated:** X evidence remains usable within scope; selectivity against
  Y is unresolved. Do not insert a zero penalty, an assumed weak Y affinity or a
  satisfied selectivity check. A strategy requiring a usable Y evaluator cannot
  execute that comparison merely by declaring exploratory intent.
- **Evaluation failed:** preserve the failure and its cause separately from an
  unattempted assessment. Neither is a negative binding observation.
- **Predictors disagree:** align molecular species/views, endpoints, states and
  context before treating outputs as contradictory. Preserve genuine disagreement;
  no mandatory averaging, voting, favorable-result selection or confidence winner.
- **X and Y results are not directly comparable:** retain both assessments and
  their limitations. Seek an applicable common evaluation or justify an indirect
  comparison; until then no quantitative selectivity claim follows. Matching
  numeric ranges is not calibration.
- **Applicability is weak:** D18 permits justified exploration using compatible
  inputs, with the estimated property and extrapolation visible. That use does not
  turn weak support into validated selectivity or fix missing molecular information.

A new expensive method is not automatically more accurate or independent. As a
general measurement precedent, [NIST](https://www.nist.gov/programs-projects/orthogonal-measurements)
distinguishes measuring the same property/sample by different physical principles
from broader complementary support for a decision. This does not prescribe a
peptide-specific assay or prove independence of any pair of predictors.

### Eligibility for three actions

These are conditional policy alternatives, not adopted evidence thresholds:

| Action | Potential eligibility and useful evidence | What selection must not imply |
| --- | --- | --- |
| Continue computational optimization | An informative X signal may justify exploration while Y remains unresolved, if permitted by the declared search policy. If the chosen optimizer requires both X/Y evaluations, that operation must actually be available; another strategy is an explicit plan choice. | Scientific selectivity has not become satisfied because the search proceeds; unknown Y cannot be relabeled as avoidance. |
| Request another evaluation | Choose a missing Y assessment, a comparable X/Y pair or a discriminating assessment of disagreement according to what could change the decision, available methods and cost. | Missing data/disagreement alone do not guarantee high information value; another model invocation is not necessarily independent evidence. |
| Select for synthesis and later assessment | An exploratory comparison panel can admit incomplete computational evidence with a stated purpose. A shortlist whose declared prerequisite is supported X/Y discrimination needs that evidence under its actual rule. Chemical/action-specific prerequisites remain explicit. | Synthesis selection is neither experimental validation nor a selective-binder certification. No universal pre-synthesis evidence minimum is adopted. |

The same candidate may be eligible for one action and not another. Preserve the
scientific requirement and its unresolved status across policies; changing the
purpose affects the selection basis, not the meaning of selectivity. Known
scientific violations, adverse operational checks and absent evidence retain
their distinct meanings under D27.

### Three alternatives for requirements, checks and compliance evidence

| Alternative | Advantages | Limits |
| --- | --- | --- |
| Requirement-centered summaries containing their checks, evidence references and local assessment | Compact for a few requirements, especially exact checks; can preserve scientific meaning without new public entity types. | Shared evaluations/comparisons may be duplicated across requirements; method changes can obscure what was checked unless carefully referenced. |
| Distinct scientific requirements, operational checks and evidence/assessment links | A requirement can exist without an evaluator; several checks may inform it and one evaluation may inform several requirements. Exact checks, proxies and unresolved applicability remain explicit. | Needs disciplined links and attribution, but not three classes, fixed schemas or a general inference engine. |
| General formal constraint/evidence calculus with automatic aggregation | Could help a future specialized optimizer reason about complex predicates and uncertainty. | Premature logic/solver and confidence assumptions; the present case does not justify a universal constraint or decision engine. |

**Accepted conceptual choice (D29): the second alternative.** Distinguish (a) scientific
requirement, (b) the actual predicate/procedure used to check something and (c)
which evaluations, assumptions and applicability justify an assessment. A model
cutoff checks its own operational criterion; its relationship to the scientific
requirement must remain qualified. The first alternative can still be an internal
representation if it preserves these meanings. No API or compulsory field set
is selected, and absence of a check does not delete the requirement.

The approval includes all seven investigator qualifications: requirements remain
independent of methods; checks retain their specific operational meaning; original
evaluations retain subjects, representations, conditions, models, uncertainty and
provenance; many-to-many evidence links do not imply sufficiency; favorable,
adverse, contradictory, insufficient and absent evidence remain distinguishable
without a universal status scheme; eligibility depends on the action's requirements
and selection policy, with missing Y never demonstrated selectivity; comparisons
respect meaning, units, conditions and applicability. A structural score cannot be
arbitrarily recast as an affinity or selectivity ratio. No universal thresholds,
rejection rules, Python classes or formal constraint engine are adopted.

### Traceability, comparison and next discussion

Keep original X/Y evaluations with their exact subjects/views, targets/contexts,
method/checkpoint and available uncertainty. Record derived comparisons,
transformations, criterion/policy versions, evidence references and action-specific
selection grounds. Re-evaluation or a new policy creates new attributed results;
it cannot rewrite the earlier evaluations or justify past selections retroactively.

For a fixed pool/evidence snapshot, one policy may seek well-supported X/Y
comparisons and another may prioritize an unresolved promising candidate for
information. They can make different selections without changing the scientific
problem. A policy requiring only an X score can report an X-based exploratory
choice, not claim that Y avoidance was established. B's broader evidence from
section 3 still needs its actual content; completeness is not favorable evidence.
End-to-end optimizers can additionally generate different candidates; compare
their problem scope, budgets, coverage and actual evaluations explicitly.

**Current next discussion:** compare optimization and selection policies in
[multiobjective_optimization.md](multiobjective_optimization.md). Its operational
extension examines restriction scope and prerequisites for three actions; D31
now accepts that conceptual reasoning, without the concrete policies. D30 accepts
alternative optimizers on the same problem without rewriting evidence. The
[integrated uncertainty/diversity/budget analysis](uncertainty_diversity_budget.md)
records conceptual P04 closure approved under D32. Concrete
contracts and algorithm choices can be qualified with the capabilities selected
for V0.1 after that decision, rather than extending general conceptual analysis.
Numerical requirements and operational rules need a stated scientific use.
P04 is conceptually closed; no universal fitness, selector, formal constraint
solver, code or issue is introduced. The [V0.1 alternatives](v0_1_alternatives.md)
are the current bounded scope decision, not another general architecture review.
