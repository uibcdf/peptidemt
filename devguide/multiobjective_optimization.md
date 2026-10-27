# Multiobjective optimization: recognition, avoidance, CPP and hemolysis

Status: **conceptual analysis and pending alternatives**, 2026-10-26. D27–D29
establish evaluation/selection and requirement/check/evidence meanings. They do
not select an optimizer, scalar reward, Pareto policy, threshold, uncertainty
model, missing-data rule or diversity metric. P04 remains open. No scientific
software or public API is specified here.

Navigation: [index](README.md) · [accepted semantics](evaluation_and_selection.md)
· [decisions](decisions.md) · [open questions](open_questions.md#p04-proposed-discussion-sequence)
· [generative strategies](generative_strategies.md) · [engine evidence](protein_peptide_design_engines.md).

## 1. Same scientific problem, different computational strategies

The intent is to recognize protein X, avoid homolog Y, have the desired CPP
function in a stated context and minimize hemolysis. X/Y constructs, molecular
states, peptide species and the relevant functional conditions qualify that
intent. CPP classification is not automatically cytosolic delivery; low predicted
hemolysis is neither demonstrated absence of hemolysis nor general safety.
The example does not choose targets, chemistry, assay conditions or a demonstrator.

The scientific problem can specify noncompensable requirements as well as
preferences. What may trade off against what needs investigator agreement for
that problem. A plan's proxy reward must not quietly make every requirement
compensable. Failure to establish a requirement leaves it unresolved; favorable
values on the other objectives do not establish it.

Two kinds of comparison must be separated:

- **Within an objective:** is the ordering across these candidates meaningful
  given endpoint, chemical subject/view, method, conditions and applicability?
- **Across objectives:** what preference makes an improvement on one worth a
  deterioration on another? A utility transformation expresses a decision policy,
  not physical calibration or a conversion of structural confidence into affinity.

When comparable affinity estimates exist, retain their units and definitions;
conversion to a utility requires a separate justified preference. Structural
plausibility, physicochemical descriptors and functional classifiers can supply
additional evidence or guidance without each becoming an independent objective.
X recognition, Y avoidance and a derived selectivity measure can otherwise count
the same preference repeatedly. A structural evaluation may also be an applicability
or plausibility check rather than a quantity to maximize.

An objective vector also needs compatible attribution across its entries: X
binding for one chemical realization and CPP for another do not automatically
establish a jointly favorable candidate. Different supported views can inform
the same proposal with explicit attribution limits under P07; selecting the best
completion separately for each objective must not invent a multifunctional molecule.

The separation under D09 supports the following distinct choices without adding
mandatory execution stages:

| Choice | What it controls | What it does not establish |
| --- | --- | --- |
| Proposal/generation strategy | Which compatible proposals, edits or trajectories are explored. | Functional activity or feasibility of the outputs. |
| Search reward, acquisition or survival policy | Which branches continue, which evaluations are requested, or which population members survive. | A universal ranking or independent validation. |
| Evidence archive and assessments | Original results and qualified derived comparisons, with their subjects and provenance. | Automatic sufficiency for each requirement. |
| Action-specific selection policy | Which candidates are chosen for another computation, an exploratory panel or another declared action. | That the search reward must be the final selection criterion. |

A scalar-guided generator can populate a Pareto archive; a Pareto-based optimizer
can feed a constrained final shortlist. A complete-output-only engine can be used
in either comparison without acquiring internal trajectory controls it lacks.

## 2. Invented candidates and reproducible arithmetic

**Every value, candidate and cluster below is invented for reasoning. None is a
sequence, model prediction, experimental datum, calibrated probability or adopted
threshold.** A–E have comparable outputs within each column for this illustration.
Scores for different columns estimate different properties; no common physical
unit is implied. Higher X and CPP are favorable; lower Y and H are favorable.
H is a hemolysis-related proxy, not a measured percentage of hemolysis.

| Candidate | X score, 0–100 | Y score, 0–100 | CPP score, 0–1 | H score, 0–10 | Required chemical check | Invented cluster |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| A | 95 | 80 | 0.95 | 8 | Pass | alpha |
| B | 80 | 20 | 0.70 | 2 | Pass | beta |
| C | 65 | 5 | 0.90 | 1 | Pass | gamma |
| D | 85 | 30 | 0.80 | 3 | Pass | alpha |
| E | 70 | 25 | 0.60 | 4 | Pass | beta |
| F | 92 | Missing | 0.90 | 1 | Pass | delta |
| G | 88 | 12* | 0.85 | 1.5 | Pass | alpha |
| H | 90 | 10 | 0.95 | 1 | Fail | alpha |

H denotes a hypothetical known violation of a required bond-preservation check
on a sufficiently defined molecule, not an implemented chemical capability.
G's Y score (*) comes from a different uncalibrated evaluator and is **not
comparable** with the other Y values. Its apparently favorable number cannot
enter their comparison. F and G remain valid records needing a compatible Y
assessment for a policy requiring it; neither is assigned a favorable/adverse
replacement. H is outside the illustrated chemically admissible set; another
explicitly permitted repair/control action could still use its record.

For A–E define illustrative utilities, all maximized:

`z = (X/100, 1 - Y/100, CPP, 1 - H/10)`.

These fixed anchors express toy preferences, not biological calibration. They
are not recomputed from each batch's minimum and maximum. For `R = sum(w_j z_j)`:

| Candidate | X-prioritized R, weights (0.85, 0.05, 0.05, 0.05) | Balanced R, weights (0.25, 0.25, 0.25, 0.25) |
| --- | ---: | ---: |
| A | 0.8750 | 0.5750 |
| B | 0.7950 | 0.7750 |
| C | 0.6900 | 0.8500 |
| D | 0.8325 | 0.7625 |
| E | 0.6925 | 0.6625 |

The first policy chooses **A**; the second chooses **C**. This describes an
exploratory allocation choice, not acceptance as satisfying all scientific
requirements. A's poor Y/H values illustrate what a compensatory utility permits.

Other policies on exactly the same A–E evidence produce different decisions:

| Illustrative policy | Result | Interpretation |
| --- | --- | --- |
| Pareto nondominance on the four original objectives | A, B, C, D | B dominates E; none of A–D dominates another. The observed front is not one winner. |
| Operational gates Y <= 20, CPP >= 0.70, H <= 2, then maximize X | B and C pass the gates; choose B | Exact arithmetic on invented proxies; not verified biological compliance. |
| Lexicographic ordering: minimize Y first, then other objectives | C | The first objective decides here. |
| Lexicographic ordering: maximize X first, then other objectives | A | A different priority changes the choice. |
| X-prioritized utility, select two | A and D | Both belong to invented cluster alpha. |
| Same utility, but at most one per invented cluster | A and B | An illustrative diversity quota changes the batch. |

No policy here is adopted. F/G do not pass or fail unavailable comparable Y gates;
their eligibility depends on the intended action. Pareto claims above explicitly
refer to the complete comparable subset A–E, not the full search space. H's
chemical-check failure must not be outweighed in an action requiring that check.

## 3. Scalar objectives: useful, explicit compromises

A weighted sum is simple, inexpensive after evaluation and compatible with many
black-box optimizers and native reward hooks. Its weights only have meaning
together with objective directions and utility transformations. Equal weights
after scaling do not mean equal scientific importance. Nonlinear transformations,
saturation or desirability functions change marginal tradeoffs; rank transforms
discard magnitudes and can depend on the comparison pool. Batch min–max scaling
can change a candidate's utility when unrelated candidates arrive.

Strictly increasing per-objective transformations preserve exact Pareto dominance
on complete comparable data, but generally change weighted sums and distances.
Hypervolume values and crowding-based choices also depend on the coordinate
transformation. Keep raw values alongside transformations, anchors and versions.
Positive weights preserve dominance for those data; zero weights ignore an
objective. Sensitivity across scientifically defensible weights is more informative
than presenting one arbitrary weight vector as a uniquely correct answer.

Weighted sums express compensation. A large X reward can offset an adverse H
score. A finite penalty for an operational violation is another tradeoff and
does not guarantee feasibility. A geometric mean or product of desirabilities
can emphasize bottlenecks, but depends on transformations and zero handling;
multiplying classifier outputs does not create a joint activity probability.

For a minimization vector `f`, a Tchebycheff alternative minimizes
`max_j w_j (f_j - r_j)` relative to a declared lower reference `r` with
`r_j <= f_j` over the domain being considered, optionally augmented
by a small weighted sum to resolve weak tradeoffs. This avoids relying solely on
linear supporting directions for nonconvex fronts. Reference choice, scales and
solver assumptions still matter; no guarantee of finding a peptide optimum follows.
[Lin et al. (2024)](https://proceedings.mlr.press/v235/lin24y.html) study a smooth,
gradient-based form. That method's differentiability requirements are not supplied
by arbitrary external classifiers or discrete peptide edits.

Correlated predictors are not independent confirmations. Several CPP models,
charge descriptors and a learned CPP output may repeatedly reward related
signals. Keep their endpoints, training overlaps and roles visible. Options
include using several models as an assessment panel for one property, selecting
a justified search signal, or testing alternative ensembles. None is a default
averaging rule. Correlation alone does not make two biological objectives identical;
automatic decorrelation/PCA would also change their interpretable meaning.

An absent objective must not simply receive zero penalty, a favorable value or
weights renormalized over available columns. Those rules can reward non-evaluation.
A partial utility may guide a declared limited-purpose action, but cannot be
compared as if it were the complete utility. With only the declared toy Y range,
F's balanced utility lies in **[0.68, 0.93]**. This is a logical bound, not a
confidence interval or estimated distribution; it does not settle F versus C.
G's incompatible score cannot be inserted merely because it shares a numeric range.

## 4. Pareto approaches and incomplete comparisons

For maximization, candidate a dominates b when `z_j(a) >= z_j(b)` for every
declared objective and the inequality is strict for at least one. No common unit
across objectives is required, but valid within-objective comparisons are.
Nondominance preserves tradeoffs without choosing compensatory weights. It
does not establish feasibility, calibration, biological activity or one final
choice. A finite observed front is not a certified global Pareto frontier.

[NSGA-II, Deb et al. (2002)](https://doi.org/10.1109/4235.996017) combines
nondominated sorting, elitist population survival and objective-space crowding.
It is a search algorithm when coupled to variation/evaluation, not merely a
post hoc Pareto filter. Crowding supports spread in objective space; it does not
guarantee sequence or chemical diversity. More objectives can leave many candidates
mutually nondominated, making archive truncation and preferences consequential.

For missing or noncomparable evaluations, possible policies include:

| Alternative | Benefit | Limit |
| --- | --- | --- |
| Sort a complete, comparable subset; keep unresolved candidates available for further assessment | Transparent, no imputation. | Completeness can reflect cost or input bias; report excluded coverage and do not call exclusions dominated. |
| Separate comparisons by endpoint/model/context or supported representation | Preserves meaningful local orderings. | Separate fronts cannot automatically be merged into one global ranking. |
| Use justified bounds or scenarios for conservative dominance | Can establish some relations without point estimates. | Broad bounds leave many unresolved; assumptions must be justified. |
| Use a qualified surrogate/acquisition model to choose missing evaluations | Can spend costly evaluations strategically. | Adds statistical assumptions and training cost; surrogate estimates remain separate from observed evidence. |

Dropping missing coordinates separately for each pair is unsafe as a general
ordering. An invented all-maximize example is u=(3,?,1), v=(2,3,?), w=(?,2,2):
on shared coordinates u beats v, v beats w, and w beats u. That cycle is not
ordinary Pareto dominance. Choosing a common projected objective set is possible
for a stated limited question, but it is not dominance on the full problem.

With justified intervals `[L_j, U_j]`, `L_j(a) >= U_j(b)` for all objectives,
strict for at least one, is a conservative sufficient dominance condition across
the declared intervals. It is not a probability statement or a mandate to invent
bounds. Unresolved comparison, contradiction and established domination remain
different meanings. An evaluated-but-inapplicable value is not repaired by a mask.

## 5. Hierarchical and constrained optimization

An epsilon-constraint policy optimizes one objective while requiring declared
bounds on the others. In the toy example it chooses B after Y/CPP/H gates. A
Pareto search inside that operationally admissible subset is another possibility.
Strict lexicographic optimization instead permits no compensation against the
first objective, however small its improvement. Tolerances or priority bands can
avoid making numerically tiny, unreliable differences decisive; these choices
need interpretation in each score's scale.

These policies are useful when certain requirements are noncompensable, or when
a next action needs prerequisites. They require a distinction between:

- **Checkable chemical/representation conditions:** a supported check on known
  chemistry can determine a specified predicate. Missing information cannot pass
  it by default. Generator masks, allowed edits, rejection or repair can enforce
  it only if the required operations and chemistry support actually exist.
- **Biological requirements:** a predictor cutoff is an operational proxy with
  applicability and uncertainty. Hard enforcement of its arithmetic does not make
  the underlying requirement exactly known. Missing Y remains unresolved.

No compulsory chemistry-first pipeline follows. Cheap checks may save expensive
calls, but only when their scope warrants that use; partial proposals can be
evaluated or explicitly completed under P07. Repaired chemistry creates a distinct
design operation and may require reevaluation. A candidate excluded from one
action need not disappear from the evidence archive or an authorized exploration.

If no candidate meets an operational policy, report that outcome. Revising a
cutoff or allocating an exploratory budget is a new visible plan choice; it does
not relax the scientific problem silently. Several exact/uncertain restrictions
can coexist without a universal penalty magnitude or rejection rule.

## 6. Uncertainty, disagreement and applicability

Available uncertainty may describe observation noise, predictive uncertainty,
model disagreement, hypothetical chemical realizations or target/context variation.
These are not interchangeable standard deviations. Preserve their source and
meaning; an ensemble's spread alone is not a calibrated error bar, and agreement
among related models does not exclude shared bias.

Possible policies need different evidence:

| Policy | What it can use | Limitation |
| --- | --- | --- |
| Separate model/context scenarios; inspect stable choices | Several meaningful alternative evaluations, no probabilities required. | Worst-case behavior covers those scenarios, not every possible failure. Contradictory endpoints must first be aligned. |
| Conservative interval or robust utility/constraint checks | Justified bounds or declared sensitivity sets. | Can be very conservative and exclude novelty; heuristic ranges must be named as such. |
| Optimistic exploration or explicit novelty/applicability budgets | A declared heuristic or meaningful uncertainty estimate. | Exploration preference is not evidence that an uncertain candidate is better or safe. |
| Chance constraints, expected utility or Bayesian acquisition | Qualified probabilistic models for the particular objectives and context. | Cannot interpret uncalibrated classifier scores as probabilities of satisfying biology. |
| Further evaluation aimed at a decision-relevant uncertainty | Accessible evaluator, cost and a reason the result might change a decision. | Disagreement or missingness alone does not establish high information value. |

For a second **invented** sensitivity example, let CPP for B range over [0.60,
0.80] and for C over [0.85,0.95], with the other toy values held fixed. These are
declared scenario sets, not confidence intervals. The point gate CPP >= 0.70
admits both, then chooses B on X. Requiring that gate throughout the scenario
set admits C but cannot establish B's robust operational eligibility. It does
not demonstrate that B lacks CPP activity. Unknown Y is not resolved by this test.

[NEHVI/qNEHVI, Daulton et al. (2021)](https://arxiv.org/abs/2105.08195) provide a
Bayesian acquisition approach to noisy multiobjective optimization and parallel
batches using expected hypervolume improvement. Use requires appropriate
surrogates and their uncertainty assumptions, not necessarily probabilistic
outputs from every original evaluator. A surrogate fitted to deterministic
predictor scores models those scores; it does not calibrate their biological truth.

[PESMO, Hernández-Lobato et al. (2016)](https://proceedings.mlr.press/v48/hernandez-lobatoa16.html)
uses information about a Pareto set and permits objective-specific, decoupled
evaluations, potentially with different costs. It is a useful precedent for
asking which missing evaluation to buy next, not a ready PeptideMT adapter or
proof that another model call resolves uncertainty. Both Bayesian options remain
conditional future integrations; no probability model is required of the core.

## 7. Diversity and exploration

Objective-space spread, sequence diversity, chemical diversity, structural
diversity and diversity of provenance are different. Many distinct sequences can
occupy one physical/functional region; similar sequences can differ chemically.
Embedding distance depends on its model/domain. Canonical identity and state
grouping remain deferred under P07: deduplicate only under justified equivalence,
retain convergent generation paths and do not identify molecules by sequence alone.

Possible policies include diversity-aware batch selection after quality checks,
max–min distances, justified clustering/quotas, novelty archives, multiple proposal
sources, restarts and reserved exploration budgets. Their scope differs: a final
diverse shortlist does not repair a search that never explored other modes.
Conversely, diversity as a reward can consume budget without improving the
desired functions. The A/D versus A/B toy batch illustrates a policy effect;
its cluster labels are invented, not a chosen metric or computed classification.

CPP and hemolysis predictors can favor or penalize related physicochemical
features. Examine descriptor distributions, length/composition controls, source
coverage and independent assessments where feasible. Adding several correlated
descriptors as separate Pareto axes can manufacture tradeoffs or dilute selection;
more objectives are not automatically more scientifically informative. Retain
counterexamples and failures rather than optimizing only reported successes.

## 8. Algorithms, costs and ecosystem boundaries

These are reusable mathematical options, not implemented PeptideMT capacities:

Weighted, constrained and evolutionary methods are established general approaches;
they need objective evaluations but not necessarily new training data or calibrated
probabilities. Bayesian variants add a learned surrogate and its data/assumptions.
All still depend on evaluator quality and compatible candidate operations. Generic
algorithmic maturity is not peptide-domain qualification or a cost advantage on
this problem; no performance benchmark has been run here.

| Approach | Practical requirements / cost | Main tradeoff |
| --- | --- | --- |
| Sampling plus scalar, Pareto or constrained postselection | Complete or otherwise evaluable proposals; total evaluator cost often exceeds ranking cost. | Simple computational reference; does not guide the generator's explored distribution. |
| Scalar evolutionary/local search | Supported molecular edits/proposals, evaluator calls, declared utilities; gradients unnecessary. | Easy black-box use, but reward exploitation and chosen tradeoffs can restrict coverage. |
| NSGA-II-style population search | Valid variation, comparable vectors, population evaluation and archive/survival policy. | Multiple tradeoffs in one run; population cost and diversity/truncation choices remain. |
| MOEA/D-style decomposition | Several scalar subproblems, references/scales and neighboring-search coordination. | Shares information across preferences; finite directions and normalization affect coverage. |
| Hierarchical or constrained search | Qualified checks, explicit priorities/bounds and handling of unresolved assessments. | Useful noncompensation; uncertain gates can shrink or bias search and produce an empty set. |
| Multiobjective Bayesian optimization | Initial data, suitable representation/surrogates, acquisition optimization and valid proposal decoding/search. | Can allocate expensive calls; fitting/acquisition overhead, discrete chemistry and model misspecification matter. |
| Native generative guidance | Actual supported reward/state/gradient access, compatible inputs and internal-call accounting. | Can change search during generation; cannot be assumed for an opaque output-only provider. |

[MOEA/D, Zhang and Li (2007)](https://doi.org/10.1109/TEVC.2007.892759) specifically
decomposes a multiobjective problem into simultaneously optimized scalar subproblems
sharing information among neighbors. This is distinct from choosing one fixed
weighted sum or repeatedly running independent optimizers. Its generic results
do not establish performance for peptide chemical spaces.

The [pinned engine review](protein_peptide_design_engines.md#4-rfd4-proteina-unusually-relevant-access-still-domain-limited-evidence)
documents RFD4 native metric/reward and beam-search seams. A scalar reward hook
does not promise a native Pareto optimizer; qualified raw outputs could feed a
separate archive/selector. External classifiers require compatible adapters;
black-box scoring is not differentiable guidance. Optional Chaperone compositions
expose only their actual operations. Provider/version/checkpoint/adapter/configuration
support remains qualified under D21–D26; no new runtime integration is claimed.

The [ecosystem audit](integration_audit.md) continues to govern ownership:
MolSysMT handles molecular representations/manipulations; PeptideMT owns the
design objective interpretation, qualified evaluation links and optimization/
selection rationale. PyUnitWizard can convert compatible physical units, not
calibrate scores. Praxis can supply reusable method/execution conventions and
Recorda observable recording seams within their audited scope; native scientific
results must preserve meaning. No universal planner, project-claim engine,
mandatory Nextia runtime or duplicated molecular/evaluation backend is proposed.

## 9. Reproducible comparisons and a bounded next decision

**Fixed-evidence comparison:** hold the problem, candidate pool, actual evaluated
views and evidence snapshot fixed. Change the scalar/Pareto/constrained or batch
selection policy. Report eligibility, unresolved comparisons, chosen candidates
and reasons. This isolates policy effects, as in the toy tables; it is not a
comparison of search efficiency.

**End-to-end comparison:** hold scientific intent fixed while allowing optimizers
to generate different candidates. Declare evaluators, proposal access, starting
material, allowed edits, budgets, stopping rules and final assessment policy.
If these differ, report the comparison as such rather than attributing every
effect to the optimizer. Replicate stochastic searches; equal integer seeds across
algorithms do not imply equal random paths. Record environment/checkpoint/configuration
and any nondeterminism rather than promising bitwise reproducibility universally.

Budget accounting includes proposals, all evaluator requests, failures, internal
rollouts, molecular preparation, surrogate training, reused/cached evaluations,
hardware time and parallelism where relevant. Count unique qualified evidence
separately from calls or representations. Optimizing a proxy more efficiently
is a computational outcome, not by itself improved real bioactivity.

Compare tradeoffs, operational-check results, evaluation coverage/applicability,
uncertainty, diversity and cost. Hypervolume requires a declared reference point,
directions, transformations and eligible comparable objective set; use the same
conventions when comparing runs. A larger number need not establish superior
biology, and omitting unresolved candidates can bias the apparent result.
Independent assessments are valuable where available; changing the access route
to the same model does not make it independent.

Preserve original evaluations and their chemical subjects/views/assumptions;
record derived objective vectors, utility transformations, policy/configuration,
evidence used, action purpose and selection rationale. If a reward or evidence
snapshot changes, retain which decisions used which version. Native search may
not expose every internal decision; record that limit rather than inventing a
trace. Several selection reports can coexist without overwriting evidence or
discarding convergent provenance. No identifier or persistence scheme is selected.

**Pending recommendation:** support multiple optimization policies over qualified
evidence, while retaining original objective vectors whenever they are available.
A useful first conceptual comparison uses a scalar policy, a nondominated archive
and an epsilon-constraint policy on fixed evidence, before testing search effects.
This is not approval to implement three engines or a mandatory implementation order.

The next concrete discussion should settle the **exploratory versus action-specific
tradeoff policy for this X/Y/CPP/hemolysis problem**: which requirements cannot be
compensated for a declared action, which proxy tradeoffs may guide exploration,
and how unresolved candidates remain available for informative evaluation.
Then agree a small reproducible comparison protocol and only afterwards specify
the first authorized optimizer capability. Scientific thresholds need real context;
toy values must not migrate into defaults. The choice among weighted utilities,
Pareto, constrained/hierarchical and uncertainty/diversity variants remains open.

The cited primary papers establish mathematical/algorithmic precedents. This
review did not install or execute their implementations, reproduce benchmarks,
generate peptides, validate predictors, select a demonstrator or create issues.
