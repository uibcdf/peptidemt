# Combining target-conditioned generation and functional knowledge

Status: **comparative scientific analysis and pending recommendations**,
2026-10-26. P08's concept/resource separation and qualified indirect guidance
are accepted under D17–D20; no generative strategy or implementation is selected.
Navigation: [index](README.md) · [families](functional_families.md) ·
[literature](literature.md) · [decisions](decisions.md).

## 1. The question and the invariant scientific problem

Can existing target-conditioned generators explore preferentially toward one or
more requested functions, without retraining a universal generator? **Yes at
several intervention levels**, subject to compatible inputs, actual engine
access and useful predictive signals. Better biological outcomes or lower cost
than filtering remain hypotheses to test, not consequences of connecting models.

Keep target roles, desired functions/context, candidate domain and scientific
constraints in the problem. Put engines, resource bindings, rewards, intervention
points, budgets and selection policies in the plan. Execution records actual
proposals, hypothetical realizations, evaluated views and interventions under
P07. The same problem can support competing or cooperating plans. A target-free
problem omits the recognition requirement; it does not invent a dummy target.

An indirect or uncalibrated predictor can provide useful search rankings. Its
scientific/empirical rationale, supported inputs and extrapolation limits must
remain explicit; usefulness may itself be untested. Better search-reward values
are computational results, not independent evidence of improved function. A
direct applicable prediction also remains a prediction, not an experiment.

## 2. An operational mathematical view, not a biological probability model

For a declared compatible representation and domain, let q0(x | T) be a base
target-conditioned proposal distribution. Let U(x,T) be a plan's utility built
from applicable evaluations or justified proxies, and C its explicit feasibility
conditions. One possible search target is:

    q_beta(x | T) = q0(x | T) * 1_C(x) * exp(beta * U(x,T)) / Z(T).

This requires a finite, nonzero normalizer and is an engineered distribution.
U need not be a calibrated log-probability; its scaling and beta then express
search preferences. Monotonic score transformations can preserve a single-score
ranking while changing sampling weights and multiobjective tradeoffs. A scalar
utility is illustrative: Pareto, constrained and lexicographic policies are other
possibilities (P04). None proves the true joint distribution of target activity
and functional families. Literal reweighting cannot create support absent from
q0; edits, alternative proposal sources or a different model may expand exploration.

During a staged Markov generator with state z_k and terminal output X, an ideal
future-aware weight has the form:

    h_k(z_k) = E_q0[1_C(X) * exp(beta * U(X,T)) | z_k, T].

This conditional expectation explains a central difficulty: a terminal sequence
classifier does not supply the value of a partial/noisy backbone or sequence.
Rollouts estimate future utility at a cost; learned value models need training
and qualification. A reward on a decoded estimate can be a heuristic rather
than an exact h_k. In particular, averaging utility and then exponentiating is
not generally the same as averaging the terminal exponential weight above.
Exact tilted sampling additionally needs appropriate transition
and, where relevant, initial-state weighting. Naively adding a gradient or
resampling with arbitrary intermediate scores does not establish that exact law.
The [FK steering and corrector papers](literature.md#f-inference-time-steering-and-distribution-composition)
provide distinct methodological precedents; their guarantees do not transfer
automatically to a new peptide adapter.

## 3. Comparison of five strategies

Costs below are qualitative. Actual runtime depends on proposal length, batching,
target preparation, structural reevaluation, rollouts and available hardware.

| Strategy | Actual intervention/access | Interoperability and extra training | Cost, applicability and diversity |
| --- | --- | --- | --- |
| Generate then filter/rank | Only completed samples and evaluators are needed. Original proposal law is unchanged. | Broadest reuse across isolated engines; no new training required. | Cheap integration; rare joint acceptance can make generation expensive. Retained diversity depends on base coverage and selection. |
| External optimization/redesign | Feedback changes subsequent edits, seeds, proposals or resampling choices. Needs a compatible edit/proposal operation, not generator gradients. | Evolutionary, Bayesian or alternating search can use black-box predictors. Surrogate-based Bayesian search may need fitted models. | More reevaluations and target checks; neighborhood trapping and reward exploitation are risks. Restarts, source mixtures and diversity-aware selection can help. |
| Guidance during sampling | Changes token/state transitions, trajectory allocation or expansion before completion. Needs continuation/partial-state, logits or compatible gradient access, depending on method. | Rollouts/tree/particle methods can reuse black-box evaluators; differentiable guidance needs a valid path or trained surrogate/head. | Extra denoising/rollout/predictor calls and particle memory; resampling can collapse ancestry. Clean-input predictors must not be applied directly to unsupported noisy states. |
| Combine functional proposal distributions | Mix proposal sources, alternate models, or sample a deliberately composed density. | Mixtures need only samplers; products/density-ratio methods require stronger shared-domain and evaluable-density/score assumptions. No full retraining necessarily. | Mixtures can cover modes without enforcing conjunction; products can collapse coverage. Heterogeneous latent spaces or tokenizations cannot simply be averaged. |
| Learned conditioning | Reuse supported native conditions or adapt a model to target/function combinations. | Existing conditions may require no training. New conditions can require a head, adapter, fine-tuning or a new generator, with increasing data needs. | Potentially cheaper repeated inference after adaptation, but upfront training/qualification and joint-label coverage matter. Unseen combinations and mode collapse remain concerns. |

### Generate then filter: the necessary comparison baseline

For independent proposals and a fixed acceptance policy with rate p > 0, obtaining
m accepted outputs takes m/p proposals in expectation. This is not a biological
success-rate estimate. Rare acceptance can make even inexpensive classifiers
costly through wasted generation or structural computation. Staged cheap/expensive
evaluation can save work, but cheap rejection may eliminate useful modes; retain
coverage/failure counts. Final filtering changes the returned population, not the
generator's internal sampling. Adaptive reallocation of future proposals is
already an additional search intervention and should be reported as such.

### External optimization: useful before touching a denoiser

Generate target-aware seeds, propose supported edits and select using functional
and recognition evaluations. Seeds may be newly generated or supplied references;
redesign is not the sole entry point. A black-box generator that only samples
complete unrelated outputs does not thereby support infill or local editing;
another proposer can supply edits while the target generator supplies restarts.

Sequence edits can invalidate a pose, fold or predicted interaction. Reevaluate
recognition at a declared frequency and track deferred checks; a fixed backbone
or seed's score cannot silently stand for every edited candidate. Native masks
and fixed-position controls help preserve a declared subset of features, not
experimental binding. Cheap sequence proxies can triage expensive structural
work, with the loss of coverage visible. No universal performance ordering versus
sampling-time guidance follows from this simpler integration.

### Sampling-time guidance: several distinct capabilities

- **Rollout/tree guidance:** expand partial proposals, complete supported rollouts,
  evaluate terminal views and use that feedback to allocate further expansion.
  PepTune is a concrete peptide-SMILES precedent. Its reward backpropagation in
  a tree is not differentiation through the generator.
- **Particle/resampling guidance:** maintain several trajectories and preferentially
  continue those with promising future-reward estimates. FK steering supplies a
  general precedent outside this peptide-family task. Particle ancestry, effective
  diversity and all rollout costs matter; fixed population size is not fixed cost.
- **Gradient/hidden-state guidance:** NOS supplies a sequence-diffusion precedent
  using compatible discriminative heads. A differentiable clean-sequence model
  still does not provide a valid derivative through arbitrary token decoding,
  chemical projection or another generator's hidden coordinates. A fitted
  surrogate can help, but adds training and approximation error.

When a structural generator has no sequence state at the intervention point,
family feedback may belong at inverse folding, in completed rollouts or in an
outer alternating search. Forcing a sequence callback into backbone denoising
does not solve the missing future-sequence evaluation. Hard constraints also need
supported partial-feasibility logic and final verification; soft family rewards
cannot guarantee functional activity.

### Combining distributions: mixture is different from conjunction

A mixture q_mix(x) = sum_i alpha_i q_i(x), with nonnegative weights summing to one,
can sample from target- and family-enriched sources without their likelihoods.
It preserves alternative proposal sources, not necessarily CPP+AMP or target+
family intersections. Evaluate all relevant objectives on the proposed outputs.
Model alternation can search toward multiple criteria, but need not converge to
one stated joint density.

A product q_prod(x) proportional to q0(x|T) * product_i q_i(x)^lambda_i favors
common support under suitable normalization. It can have negligible overlap or
be undefined if no nonzero finite normalizer exists. Repeated common sequence
priors can overconcentrate it; classifier posteriors, sampler densities and
likelihood ratios are not interchangeable factors. Correcting a shared prior
requires justified probabilistic assumptions, not a generic recipe.

Products need distributions on the same meaningful output space or justified
pushforwards/mappings. A peptide has many SMILES and coordinate realizations;
token-sequence likelihoods are representation-dependent. Pseudo-perplexity is
not a normalized molecular likelihood. Independent VAE latent coordinates have
no automatic alignment. Even combining continuous diffusion scores need not
produce the intended terminal product without suitable correction; see FKCs.
This makes source mixtures and qualified external scoring more immediately
interoperable than arbitrary products, without adopting them as the best strategy.

### Learned conditioning: reuse first, training only when justified

HydrAMP demonstrates native family-related generation and analogue modes, not
arbitrary protein conditioning. PepMLM demonstrates target-sequence conditioning,
not native conditioning on every functional label. Joint conditions must be
available, learned or implemented through explicit guidance; naming them cannot
create the capability. Retraining only a head/adapter is different from training
a whole generator, and still needs data, compatible representations and testing.
Distillation of a successful search into a conditional sampler is a possible
future route; it can also reproduce reward bias and reduce mode coverage.

## 4. Concrete engine observations versus proposed adaptations

| Published engine / inspected source | Existing bounded observation | PeptideMT composition still to qualify |
| --- | --- | --- |
| [PepMLM generation script](https://github.com/programmablebio/pepmlm/blob/3169c4920f8c383948e0a5d3a7c8f87e5e7d2436/scripts/generation.py) | Uses a fully masked binder region, per-position top-k sampling from model logits and subsequent pseudo-perplexity scoring. | Final family filtering is straightforward conceptually; feedback editing, custom decoding or guidance require adaptation. The inspected routine is not a native autoregressive family-guidance loop, and pseudo-perplexity is not affinity. |
| [DiffPepBuilder](https://github.com/YuzheWangPKU/DiffPepBuilder/tree/c19eb4f0cd2419d3bcc116184c0868243b6c4169) | Structural target input, sequence/structure co-design, optional disulfide/postprocessing stages. | Compatible family views and possible intervention points; no universal family-reward hook has been verified. |
| [ProteinMPNN controls](https://github.com/dauparas/ProteinMPNN/blob/8907e6671bfbfc92303b5f79c4b5e6ce47cdef57/README.md) | Fixed positions, omitted residues, composition/per-position biases and tied positions. | Useful inverse-folding controls; arbitrary global family rewards and joint biology are not guaranteed by those controls. |
| [PepTune tree search](https://github.com/sophtang/PepTune/blob/ce4daf00ade848cca7007b04b70ae9fe54ed2268/src/pareto_mcts.py) | Expands partial diffusion outputs, completes rollouts, scores decoded valid outputs and updates search rewards. | New function evaluators require chemical-view, semantic and applicability adapters; supplied permeability is not cytosolic delivery. |
| [NOS instructions](https://github.com/ngruver/NOS/blob/569f1c85adf2ca2ea5e32efdf46276995fcf322c/README.md) | Describes guided sampling and training discriminative heads. | Reuse of compatible heads versus training a new surrogate; no automatic arbitrary-classifier gradients. |
| [HydrAMP](https://github.com/szczurek-lab/hydramp/blob/6590d2f4c2963f25d30669052a4c4a857e0e7279/README.md) | Analogue and unconstrained family-related generation. | A family-first proposal source plus external target optimization is a proposed combination, not its native target-binding guarantee. |

These are source inspections and primary-report precedents, not executed
PeptideMT integrations. No weights were trained or benchmarked here.

## 5. A common comparison and a cooperative plan

Compare the same problem with matched or explicitly stratified chemical coverage,
targets/states, seeds, stopping rules and independent evaluation panels. Count
base-model forward/denoising calls, completed rollouts, predictor invocations,
unique evaluated views, structural reevaluations, wall time, memory and training
cost. Equal final candidate counts or equal outer iterations do not equal cost.
Report cached reuse separately while retaining scientific attribution under P07.

Keep reward performance separate from independent computational assessment and
experimental evidence. A second model using the same training corpus is not
necessarily independent; record overlap and source bias. If no independent
evaluation exists, report score optimization and its limitations rather than
claiming improved biological function. Experimental validation is not required
to complete the computational campaign.

Assess validity, coverage/applicability, target retention, objective tradeoffs,
unique sequences and chemical realizations, diversity within/across modes,
novelty against known/training data and failures. Sequence and chemical diversity
are different; no single embedding distance establishes functional diversity.
Uncalibrated rank utility can be useful, but cross-model scalar rewards require
declared scales, directions and sensitivity checks. Keep direct/indirect/missing
evidence separate from applicability: a directly targeted output may still be
poorly supported in the explored domain. These are conceptual distinctions, not
a newly adopted evidence-state enum or confidence scale.

One **proposed cooperative plan** could allocate a budget to target-conditioned
and family-enriched proposals, evaluate compatible views, retain several promising
regions, and run outer optimization or supported sampling guidance on different
branches. A common assessment panel then compares the branches. Preserve source
and intervention provenance; do not call branch selection an independent test if
it repeatedly tunes against that same panel. This is an illustrative plan, not
an implementation sequence or selected demonstrator.

## 6. Implication for the next decision

The [capability/composition analysis](capabilities_and_composition.md) now refines
this recommendation under conceptually resolved P09. Available operations belong to providers
through their adapters; strategies have requirements; plans select explicit
compositions; execution records actual use. These owners and the three
compatibility dimensions now have conceptual approval (D21–D22), not an approved
capability contract or four additional stages. The [expanded engine review](protein_peptide_design_engines.md)
adds general protein-design methods, composite procedures, domain-specific
evidence and optional direct/Chaperone routes. D25–D26 now adopt small optional,
evidence-linked capabilities and explicit compositions, including all seven
principles. Concrete contracts remain deferred.

**Recommendation, pending:** discuss capability-based strategy composition (P05),
starting with complete proposals plus external evaluation/search, while preserving
optional infill, continuation, logits/likelihoods and compatible gradient access.
This is a proposed comparison baseline, not an admission requirement: partial-only
or backbone-first generators remain valid under P07 with compatible evaluations
and explicit completions where needed.
This identifies the least access needed for reuse without making all generators
implement universal hooks. Separate capability presence from empirical scientific
qualification; preserve model/environment boundaries and MolSysMT ownership.

The domain-aware provider principle and optional individual/composite access now
have approval under D23–D24. The [minimum-semantics cases](capabilities_and_composition.md#8-three-tests-of-minimum-capability-meaning)
distinguish delegated native reward search from externally controlled branching;
only the latter inherently needs externally exposed state-control operations.
The semantic obligation and conceptual composition choice are now accepted.
Return to [P04 evaluation and selection](open_questions.md#p04-proposed-discussion-sequence);
select concrete engines and experiments later from that evidence. Sampling-time guidance and learned
conditioning should remain alternatives that can outperform or complement a
baseline, not mandatory stages or a definitive generative architecture.

The [multiobjective analysis](multiobjective_optimization.md) now separates search
rewards, evaluation acquisition, population survival and action-specific final
selection on an invented X/Y/CPP/hemolysis case. Scalar guidance can feed a Pareto
archive or a constrained shortlist; a Pareto search need not dictate the final
choice. D29 accepts requirement/check/evidence meanings; D30 now accepts distinct
search/results/selection policies with preservation of original objectives and
evaluations. No particular optimizer, fitness or mandatory Pareto archive follows.
Compare fixed-evidence policy effects separately from end-to-end search effects,
with retained raw objectives, unresolved evaluations and declared costs. No
optimizer or generator capability is selected by this extension.

The [operational case](multiobjective_optimization.md#11-operational-stress-test-four-candidates-three-purposes)
adds restriction scope, absent Y, contradictory CPP, a chemical-check violation
and adverse hemolysis evidence. A candidate's permitted contribution to generation
depends on the branch/action; exploratory use is not acceptance as a satisfactory
solution. An unavailable check cannot provide verified enforcement. These concrete
policy recommendations remain pending, with uncertainty and diversity next.
