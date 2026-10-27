# Evaluation, feasibility, selection and scientific claims

Status: **P04 conceptual alternatives and pending recommendations**, 2026-10-26.
No new conceptual decision, selector, feasibility taxonomy, API or implementation
is approved by this analysis. D09–D26 remain the accepted foundation; P09 stays
closed conceptually and P10 stays pending without an MVP obligation.

Navigation: [index](README.md) · [decisions](decisions.md) · [P04 agenda](open_questions.md#p04-proposed-discussion-sequence)
· [families](functional_families.md#selection-contradictions-and-assessment)
· [capabilities](capabilities_and_composition.md) · [ecosystem audit](integration_audit.md).

## 1. Alternatives and recommended conceptual separation

PeptideMT needs to support scientifically justified choices, not just emit ranked
sequences. It need not become a general decision system. Three alternatives are
plausible before choosing a concrete representation:

| Alternative | Strengths | Limits / cost |
| --- | --- | --- |
| Evaluation outputs with selection-specific checks; scientific conclusions remain external annotations | Small initial surface; useful for a bounded filtering/ranking tool. | Feasibility assumptions and the basis for conclusions can become scattered across policies and notebooks. Comparing the same evidence under different purposes is harder. |
| Four explicit semantic responsibilities, connected by evidence and context | Separates what was evaluated, constraint knowledge, the purpose/policy of a choice and the supported conclusion. Allows different policies without rewriting original results. | Needs careful attribution and purpose-specific interpretation, but does not require four objects or automatic claim verification. |
| General decision-theoretic engine with beliefs, utilities, actions and experiment planning | Can formalize sophisticated information/cost tradeoffs when those models exist. | Requires assumptions and infrastructure not justified by the current cases; risks duplicating MOLI methodology/project orchestration. Optional specialist optimizers can come later. |

**Pending recommendation:** the second alternative. Preserve the meanings below
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
PeptideMT need not infer all scientific conclusions or adjudicate them generally.

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

**Pending implication:** feasibility should retain restriction-by-restriction
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

## 5. Minimal principles proposed before multiobjective policies

**All recommendations below remain pending under P04.** Some consequences follow
from D09–D26, but this analysis does not create D27 or approve the proposed bundle.

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

**Suggested next agreement:** accept or revise the four semantic responsibilities
and purpose-relative eligibility/feasibility distinction before choosing how to
rank candidates. Then discuss how a particular strict requirement and its
operational checks affect a particular selection action. The A/B/C example can
test that agreement without requiring a universal threshold or minimum evidence bar.

Afterwards compare hard/soft objectives, Pareto and hierarchical/lexicographic
policies, reward scaling, uncertainty, diversity, budgets and value of evaluation
progressively. This document selects none of them. P10 stays pending; no library
engine or general decision/planning system is needed for the present analysis.

Investigators should settle scientific meaning, constraint scope, allowed proxy
use, evidence prerequisites and the purpose of policies. Later Codex may choose
internal data structures, batching, dispatch, caches and reporting within approved
contracts. Changing a molecular projection, a restriction, missing-data behavior
or the scientific interpretation is not merely an internal implementation choice.
Concrete APIs, identifiers, persistence and acceptance tests remain to be specified
for capabilities authorized later. No code or development issues are introduced.
