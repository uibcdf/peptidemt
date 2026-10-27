# Open questions

Navigation: [index](README.md) · [alternatives](architecture_alternatives.md) · [decisions](decisions.md).
All questions remain open unless an explicit decision is recorded.

Updated: 2026-10-26. Alternative B is accepted under D09–D13 and revised P07
under D15–D16. P08 is accepted under D17–D20. The worked cases remain illustrative,
with no selected demonstrator. P09 is resolved conceptually under D21–D26,
including alternative B and all seven principles; concrete contracts remain
deferred. P04 is the next discussion block. The bounded horizon review adds only
a pending collective-design distinction (P10), not new MVP obligations.

## Q1. Design intent and execution

**Resolved conceptually:** scientific intent, computational plan and execution
evidence are separate; families are independent of their models. No class names,
API, storage or implementation is approved. Remaining questions concern minimal
representations, evidence obligations and plan comparability, not whether to
adopt the separation. See D09–D13 and the worked cases.

## Q2. Family definitions and evidence

**Resolved conceptually (P08, D17–D20):** a small extensible scientific catalog
with explicit source-label/resource associations; scientific relations differ
from co-annotation and learned correlations. Justified indirect/exploratory models
can guide search while leaving the desired function unassessed. Reward improvement
is not independent validation. No common representation, differentiability,
formal ontology or evidence-state scale is required. See the
[accepted record](functional_families.md#p08-conceptual-alternatives-and-generative-use).

**Still open:** minimum concrete metadata and mapping policies. What context and
provenance suffice for a qualified association? How do equivalent, narrower,
partial/proxy and unresolved mappings behave without implying biological truth?
How do we represent direct/indirect/absent evidence and doubtful applicability
without turning these distinctions into a rigid hierarchy?

The 21-label predictor/structural target-generator exercise exposes representation
conversion versus empirical applicability, partial completions under P07, discrete
labels versus scores, and final filtering versus actual sampling intervention.
Which qualification is needed for a resource to guide exploration, and which
additional evidence is needed to assess a selected candidate's requested function?

The [extended literature inventory](functional_families.md) documents more than
CPP/AMP/ACP: MultiPep (20 labels), PrMFTP/ETFC (21) and Xiao et al.'s dataset
(15 major categories, 47 labels including 15 generic labels). These schemes are
not interchangeable ontologies. **Open:** how to map source-specific labels to
shared concepts without requiring a fixed enumeration or treating nested labels
as independent functions? How will label provenance and model availability be tracked?


Which differences require distinct family definitions versus contexts or assays?
How do CPP membership, uptake and cytosolic access relate without being merged?
How should AFP relate to the chosen broad or narrow meaning of AMP?
Can context be unavailable while still permitting a computational task?
How do model-specific label semantics affect multifamily requests?

## Q3. Candidate chemistry and representation

**Resolved conceptually (D15–D16):** P07 alternative III permits incomplete
proposals, explicit realizations and evaluated-view relationships. Supported
direct evaluations and evaluations of explicit hypothetical chemical realizations
are allowed, without rewriting the original proposal. Preserve actual inputs,
chemistry, assumptions, transformations, model and attribution limits. Completion,
conversion and redesign differ; calculation reuse does not guarantee scientific
transfer. Retain convergent provenance and do not impose mandatory stages.

**Explicitly still open:** canonical molecular identity, grouping of chemical
states, identifier schemes, persistence, concrete interfaces and initial chemical
support. What minimum known/unknown information is needed by each evaluator?
When is a chemical realization sufficiently defined? Which species differences
can be grouped under a parent without merging evaluation subjects? See the
[accepted P07 record](architecture_alternatives.md#p07-reconsidered-proposals-chemistry-views-and-evaluation-subjects).

What is the initial supported subset, and how do we preserve unsupported
modifications? How do sequence, chemical identity, conformer and target-bound
pose remain distinguishable? Which MolSysMT experimental boundaries require
pinned adapters? No canonical-only permanent scope is adopted.

Use the [target-free case and broader probes](design_examples.md) to test these
semantics. The inflammatory/immune, ACE/physiology and tumor-homing examples
stress different endpoint meanings without a formal family ontology (P08).

## Q4. Labels, negatives and applicability

For each model, are negatives measured, inferred, sampled or merely unannotated?
Can we obtain training data and cluster-aware/temporal evaluation?
Which PU/one-class approaches help under source selection bias?
When should an evaluator abstain rather than extrapolate?

## Q5. Combining families and recognition

The [five-way strategy comparison](generative_strategies.md) under P05 covers final filtering, external
optimization, sampling-time guidance, distribution composition and learned
conditioning. Available operations belong to providers through adapters,
requirements to strategies and selected use to plans. The
[P09 alternatives](capabilities_and_composition.md) preserve that accepted separation
and now resolve the conceptual organization: small optional, evidence-linked
capabilities plus explicit compositions. The seven principles and context-sensitive
information obligation are accepted; concrete contracts will be specified for
particular capabilities, without approving every possible attribute separately.
A complete-sample interface supports filtering and some
outer search, not automatically continuation, infill, density ratios or gradients.
How should several compatible strategies compete or cooperate within one budget?
Which compatibility checks can be made before execution, which depend on runtime
resources, and what scientific limits remain after a composition is operational?
What alternatives may a plan explicitly authorize without silent strategy changes?

Use independent predictors, a multilabel model, family priors, expert
combinations, Pareto selection, or several together? How will correlated
descriptors and overlapping training sets be detected? What preserves
recognition when a family-driven optimizer edits a binder?

### P04 proposed discussion sequence

Status: **pending discussion agenda**, not adopted evaluation/selection policies.
Return to the individual-peptide operational core; library, ensemble and
transformation cases remain optional counterexamples rather than required features.

1. **Evaluation meaning and decision context.** What is evaluated: which proposal,
   chemical realization/view, target/state/context and property? Keep raw results,
   units/score meaning, applicability, source and dependencies distinct from the
   objective or reward using them. Identify whether a result guides search,
   assesses a candidate or provides genuinely independent evidence.
2. **Constraints and evidence sufficiency.** Separate the desired scientific
   requirement, an exact check and a model-based operational criterion. What
   happens when a required assessment is missing, fails or has doubtful scope?
   Distinguish an observed violation, an unmet operational criterion and absence
   of evidence without adopting a mandatory status enum or universal rejection.
3. **Multiple objectives and tradeoffs.** Which objectives remain separate and
   which comparisons are meaningful? Compare documented scalarization, Pareto,
   lexicographic and other policies without selecting one universal optimizer.
   Missing/uncertain entries and incomparable scales affect what can be ranked.
4. **Uncertainty and robustness.** Distinguish prediction uncertainty where
   available, model disagreement, applicability limits, experimental variation
   and context/state variability. Determine what may influence decisions without
   fabricating a common confidence scale or requiring calibrated probabilities.
5. **Diversity and budgeted selection.** Define relevant sequence/chemical/
   structural/function diversity and novelty, avoiding duplicate molecular
   counting while preserving convergent provenance. Then discuss batch size,
   cost, exploration and active-learning extensions. No universal distance,
   acquisition rule or experimental loop is adopted now.

These are discussion slices, not execution stages. Before choosing selection
algorithms, use a small counterexample: candidate A has stronger predicted target
recognition but lacks a relevant antitarget assessment; candidate B has weaker
predicted recognition with more complete evidence. Neither is automatically the
winner. Can a candidate advance to further evaluation while remaining ineligible
for a claim that all scientific requirements are satisfied? Which requirements
make a particular selection provisional, and what evidence would resolve it?

**Suggested first discussion:** agree what information and scientific meaning
evaluation results must preserve, and how feasibility differs from missing
evidence. Only then discuss a policy for comparing candidates. D11/D18/D19/D26
already rule out treating a proxy as activity, missing evidence as inactivity or
reward improvement as independent validation; P04 must make their consequences
useful for selection without reopening those principles.

## Q6. Guidance access and budgets

The [expanded engine matrix](protein_peptide_design_engines.md) compares general
protein and specialized peptide engines, with separate documented/source/runtime/
benchmark/adaptation/unknown evidence. D23–D24 now adopt architecture/origin
independence with domain/capability/evidence awareness, optional individual/
composite access and non-inheritance of internal capabilities. Concrete adapters
and simultaneous implementation of both routes are not approved.

The [three-case semantic analysis](capabilities_and_composition.md#8-three-tests-of-minimum-capability-meaning)
now supports D25–D26: meaning-preserving, evidence-linked claims and explicit
requirements, with fundamental/contextual/optional information for actual use,
not a universal metadata record. Unknown support is not established support.
Operation-specific contracts/checks remain future specifications, rather than
an unresolved conceptual choice for P09.
Delegated native reward search can work without exported sampler states;
external PeptideMT branching needs additional operations. Which exact intervention
and molecular-view promises suffice for each, without a universal state API?

For RFD4 specifically, what evidence qualifies short/cyclic/modified peptide use
for the current matched checkpoint pair? Can an adapted family metric preserve
chemical projections, source-label meanings and missing-output causes? Which
state/metric operations are genuinely exposed by each deployment? Neither the
Chaperone inverse-direction example nor a service token limit answers these.

Which engines expose partial states, infilling, likelihoods or gradients?
Does a saved trajectory contain a resumable algorithm state, or only molecular
coordinates? Which variable and quantity does a claimed gradient connect?
Can completed rollouts support a black-box family evaluator?
What predictor budget and independent validation suffice to show enrichment
beyond final filtering? Count rollouts, denoising/forward calls, structural work
and training rather than only selected candidates. When independent evidence is
unavailable, report reward improvement without inferring biological gain.
Do improvements survive length/composition controls and retain diverse modes?

## Q7. Ecosystem and publication

When should the documentation workspace seek central admission?
Which minimal optional adapters justify initial dependencies?
How do local design attempts reference future Nextia project Candidates?
How do Praxis Protocols refer to PeptideMT algorithm settings without duplicating
them? Recorda captures operations; what native result provenance stays local?
If Chaperone owns an external workflow's job submission, how do surrounding
Praxis/PeptideMT calls retain one scheduling owner and avoid double-counted work?
Which native artifacts and pinned assets are sufficient for design attribution,
and which hidden operations must remain explicitly unobserved?

## Q8. Demonstrators and experiments — explicitly deferred

Which seed-based and de novo cases best discriminate the competing strategies?
What assays and collaborators are available? What evidence would support
mechanism, specificity or joint activity? No answer is required to approve the
general computational design scope.

## Q9. Future horizon stress tests — exploratory, not a freeze gate

The [future horizons V0.2](future_horizons.md) inventory considers modified/cyclic
chemistry, target ensembles and selectivity, delivery, activation and degradants,
synthesis, PK/ADMET exposure, multifidelity learning, combinatorial/display libraries,
TCR–pMHC design, screening landscapes, molecular proximity, imaging/materials and
other extensions. S9–S12 are additional semantic stress tests, **not** newly
approved design objects or mandatory gates.

The [bounded three-scenario review](future_horizons.md#9-bounded-extensibility-review-after-p09-approval)
finds a pending collective-versus-individual distinction (P10). State panels fit
the accepted separation, with aggregation/claim limits for P04; precursor/products
need distinct subjects and a future transformation relation, not a general reaction
engine. These conclusions do not claim implemented support or adopt new architecture.

When library design is prioritized, what separates an implicit member set, a
sampling distribution, realized screening material and a computational batch?
For future transformation capabilities, which participants/context/evidence are
essential without requiring a kinetics model? Detailed schemas can wait. Immune,
exposure, materials and other horizon-specific capabilities remain strategic
opportunities, not compulsory checks before the first implementation.
