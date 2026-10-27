# Capabilities, strategy requirements and explicit composition

Status: **P09 resolved conceptually (D21–D26), contracts and implementation
deferred**, 2026-10-26. No capability schema, software contract, API
or class hierarchy is approved. Navigation: [index](README.md) · [strategies](generative_strategies.md)
· [families](functional_families.md) · [decisions](decisions.md).

The [expanded engine review](protein_peptide_design_engines.md) adds general
protein-design engines, Chaperone, RFD4, short-peptide benchmarks and revised
composition recommendations. The five-model matrix below is the earlier bounded
subset, not an exclusion of general protein engines. **P09 is conceptually closed.**

D23–D24 accept origin-independent, domain-aware support and optional individual/
composite access without automatic inheritance. D25–D26 now adopt alternative B,
all seven principles and the distinction between fundamental, contextual and
optional information sufficient to justify actual use. The illustrative details
below are not a mandatory field inventory or API. Further attribute-by-attribute
approval is unnecessary; concrete contracts follow capability-specific design.

## 1. Responsibility rather than four execution stages

The investigators accept four distinct responsibilities (D21) within the accepted
scientific-problem / computational-plan / execution-evidence architecture:

| Responsibility | Meaning | Important boundary |
| --- | --- | --- |
| Engine through its adapter | Declares operations actually exposed for a particular implementation, model/checkpoint, configuration and input/output domain. | A plan cannot create a capability by requesting it. An adapter may expose less than the underlying model could theoretically do. |
| Search strategy | Describes how proposal/evaluation capabilities are used; has requirements, optional routes and its own algorithm settings. | A requirement is not evidence that a selected engine satisfies it. |
| Computational plan | Selects resources, compatible strategy instances, transformations/completions, parameters and authorized alternatives for the scientific problem. | Selects and configures capabilities; does not own or redefine the engine's available operations. |
| Execution evidence | Records actual resolved resources, operations, inputs, adaptations, capability use, failures, deviations, costs and outputs. | Attempted, available, selected and successfully used capabilities may differ. |

**Accepted conceptual separation:** it keeps capability truth with its
provider and makes strategy reuse testable without changing the scientific
problem. It is not an additional four-stage workflow or four required objects.
Strategy logic belongs in the computational solution; engine capability evidence
is a reusable resource property; their realized use belongs in execution.

Three refinements avoid misleading abstractions:

1. Availability is conditional: backend code presence, adapter exposure, usable
   weights/environment and supported input conditions are separate facts. A
   declaration needs bounded evidence; static inspection does not prove runtime.
2. A provider may be composite. PepTune combines generation, scoring and tree
   search; HydrAMP includes internal selection. Preserve these roles and internal
   policies without requiring their existing software to be split into new classes.
3. An adapter-supplied conversion, external mutation operator or composite rollout
   can add an effective operation. Name its actual provider and assumptions; do
   not relabel that derived operation as a native property of the base model.

Observability is also bounded. A black-box call may not expose every internal
proposal or scorer invocation. Record the operations actually observed, selected
settings and missing telemetry; do not fabricate traces or equate 'not logged'
with 'not used'. Instrumentation may improve visibility later without becoming
a requirement to reimplement an opaque engine.

## 2. What a capability description needs to mean

Beyond an operation name, consider its input/output representation and information
requirements, preserved versus editable features, supported conditions/parameters,
scientific output meaning, limits and evidence. State dependencies and potentially
significant costs. These are semantic questions, not an approved field inventory.

For example, `complete` could mean filling sequence masks, assigning a sequence
to a backbone, supplying missing chemical termini, or completing a diffusion
trajectory. These are not interchangeable operations. A proposed complete sequence
may still be chemically incomplete under P07. A source accepting an `X` token
does not establish qualified evaluation or generation of arbitrary masked inputs.

Distinguish native, adapter-provided and composed support, and distinguish known
absence from uninspected/unknown support or temporary runtime unavailability.
No fixed capability-name enum or availability-state taxonomy is adopted here.
A single boolean such as 'supports guidance' would conceal too much information.

### Minimum meaning, not a mandatory record

A capability is useful **relative to an intended strategy and use context**.
The strategy's required operations and information must be justified by the
actual provider route. A broad catalog description can remain unresolved while
a particular plan needs more detail. This obligation is accepted under D26;
information can be referenced from versioned documentation,
resource descriptions or evidence rather than duplicated in every declaration.

**Fundamental** means needed to interpret a claim without changing its meaning.
**Contextual** means needed when a selected strategy/domain relies on it, not
less important. **Optional** means useful without being a prerequisite for the
stated use. Unknown information must not masquerade as a guarantee; an explicit
unknown can be an honest description without satisfying a particular requirement.
Absence of known restrictions is not evidence that an operation exists. The table
illustrates the accepted distinctions, rather than prescribing identical fields
or claiming every possible provider detail has been specified.

| Information to examine | Illustrative semantic obligation | When more detail becomes necessary |
| --- | --- | --- |
| Operation and output meaning | Fundamental: what is actually provided, by which effective access route, and what the result asserts. | Distinguish generation, sequence assignment, evaluation, continuation and workflow execution; a job receipt is not a generated candidate or a completed evaluation. |
| Admitted inputs/outputs and evaluation subject | Fundamental: required information, representation and intended subject; permitted incompleteness and output interpretation. | A family evaluator needs the peptide view and label meanings; a state controller needs sampler-state semantics; file-format compatibility alone is insufficient. |
| Molecular information required, changed and preserved | Fundamental for affected information, including what is unresolved or discarded; not an inventory of all possible chemistry. | Sequence versus coordinates, termini, stereochemistry, links, target identity/pose, edits and hypothetical completions become explicit when the operation relies on or can change them. |
| Conditions and restrictions | State conditions defining the claimed support and the actual kind of restriction. Detailed controls are contextual. | A strategy requiring fixed target coordinates, an exact residue mask or ring preservation needs that specific promise; a preference or post-filter cannot silently replace it. |
| Intermediate access/intervention | Contextual; no universal state, gradient or callback obligation. Missing access cannot satisfy a strategy that needs it. | Native reward injection can suffice for delegated search; externally controlled branching additionally requires compatible state/continuation/branch operations. Trajectory export is a different capability. |
| Execution requirements | Fundamental to distinguish declared support from resolved availability; concrete resources/assets are contextual to a plan and environment. | Required weights, dependencies, permissions, GPU/runtime compatibility and significant cost multipliers must be resolved where relevant. Exact peak memory can remain unknown; an executable plan then needs an explicit way to handle that uncertainty. |
| Evidence and applicability | Fundamental: the basis and bounds of the claim, or what is unknown. No minimum benchmark quality or universal confidence number is imposed. | A scientific use needs its task/chemistry/length/context interpretation. Code acceptance, producer execution and functional evidence support different claims; exploratory extrapolation stays explicit. |
| Known limits, failure and unavailable results | Fundamental where they affect meaning or required behavior. Exhaustive failure catalogs are unnecessary. | Missing scores, unsupported chemistry, partial output and failed execution cannot become negative bioactivity or successful completion. A strategy depending on their handling needs an explicit policy. |
| Efficiency and extra observability | Optional unless the strategy depends on them. | Batching, derivatives, uncertainty estimates, caches, state export and detailed timing can become requirements for a particular strategy. No fabricated uncertainty or hidden telemetry is required. |

Identifiability under D23 need not prescribe an identifier scheme. The claim must
be scoped to its engine/version/model assets/adapter/configuration/conditions;
execution records what actually resolved. A deterministic descriptor may have
no checkpoint. A composite can reference its recipe and known constituents while
leaving inaccessible service assets explicitly unknown. Such opacity may limit
reproduction without making every black-box use impossible.

Three extra distinctions are needed. The provider describes the meaning of an
output; the plan chooses a reward/selection policy using it. Neither defines the
scientific family. Provider requirements describe reusable support; current GPU
availability and measured costs are facts of preparation/execution. A prediction
on a view has an attribution scope; computational reuse does not extend it to
every realization under P07. These distinctions do not require separate classes.

### Generative and intervention capabilities

| Capability family | Relevant input/output and conditions | Common or method-specific? / possible provider |
| --- | --- | --- |
| Propose terminal outputs | Target/context/seed where required; returns sequences, graphs, structures or other terminal outputs of that operation. | Broadly useful, but not a mandatory chemically complete output; a partial-design engine remains valid. |
| Native conditioning | Specify which target representation, functional conditions or other controls actually enter the model or sampler. | Method-specific. Target-dependent scoring in an outer strategy is different from target conditioning in a base model. |
| Redesign / mutation | Parent proposal/candidate and allowed edits; outputs derivatives with correspondence and preservation limits. | Native analogue/infill modes, external mutation operators or composite strategies. An analogue generator need not preserve exact residue masks or edit counts. |
| Complete partial designs | Partial sequence/backbone/chemistry plus preserved information and assumptions; outputs explicit completions. | Specific completion engines or adapters; chemical realization, conversion and redesign remain distinct under P07. |
| Continue / branch sampling | A valid algorithm state at an identified step, model/conditioning, schedule and relevant caches/randomness. | Specific to algorithms that expose those operations. A saved structural trajectory does not by itself contain a resumable state. |
| Expose probabilities or internal values | Token logits, conditional probabilities, latent variables, denoising score fields or pseudo-scores, each with its meaning and domain. | Optional and noninterchangeable. Internal tensors need not be accessible in a public adapter; pseudo-perplexity is not normalized molecular likelihood or affinity. |
| Support trajectory evaluation / resampling | State access and continuation/forking sufficient for a strategy to obtain compatible assessments and allocate trajectories. | Usually composed: the engine advances states, evaluators assess supported views, the strategy selects/branches. A model need not implement a particle filter or MCTS. |
| Expose gradients | State explicitly which scalar quantity is differentiated with respect to which variables and through which transformations. | Optional; neural implementation alone is insufficient. Token decoding, external tools or molecular projections can break the required path. Tree reward backpropagation is not a gradient interface. |
| Native sequence/structure restrictions | Declared masks, fixed regions, alphabets, links or geometry rules, including their scope and postconditions. | Method-specific. Preserving a receptor is not arbitrary peptide infill; a bias is not an exact constraint. Preserve final verification and unsupported restrictions. |

A molecular state/conformer/pose is not a sampler state. The latter may include
noisy tokens/rigids, time, conditioning, masks, self-conditioning caches and random
state. MolSysMT should represent supported molecular content; PeptideMT must
retain design references and engine-specific sampling context without pretending
it is another molecular state axis. Saved coordinates alone cannot generally
establish exact continuation, replay or independently randomized branching.

### Evaluator capabilities and strategy-side operations

An evaluator declares the subject/view it accepts, property actually estimated,
context, output shape/order/units or score meaning, and applicability limitations.
Distinguish discrete labels, continuous scores, calibrated estimates where
supported, uncertainty/abstention and gradients when actually available. Batch
evaluation is an optional efficiency property, not proof of interchangeable inputs.

Sequence classifiers, descriptor models, structure/complex evaluators and
partial-state/value models need different views. The existence of a complete-input
predictor does not imply a partial-state evaluator. Rewards transform outputs
into preferences; selection, resampling, allocation and stopping belong to the
strategy/plan. An adapter may expose internal models separately, but a bundled
generator's own classifier is not automatically independent assessment.

| Evaluator family | Input and output meaning to preserve |
| --- | --- |
| Complete-view property evaluation | Supported sequence, descriptors, structure or complex plus context; outputs labels, scores or quantities for explicitly named properties. |
| Partial-state / future-value assessment | A supported algorithm/design state and relevant continuation policy; a direct partial observable or estimated terminal utility, distinguished from scoring a specific completion. |
| Feasibility / preservation checks | The stated chemistry, sequence or structure predicate and required information; distinguish exact checks from predicted surrogates and unresolved checks. |
| Optional uncertainty / derivative / probabilistic outputs | The subject, quantity, variables and interpretation of each additional output; neither a generic confidence number nor an assumed normalized likelihood. |

These families overlap and are not a mandatory evaluator hierarchy. An engine
can expose several, and a composite procedure can provide a qualified estimate
when no direct evaluator exists.

## 3. Compatibility has operational, runtime and scientific dimensions

The three dimensions below are **accepted conceptually under D22**. D25–D26
accept explicit semantic matching; concrete checking mechanisms remain to be
specified. Match requirements against
capabilities under the selected configuration, using an explicit composition when direct
matching fails. Do not demand the union of all possible operations from every
engine. Compatibility can require several operations together, or one of several
documented alternatives; names or input-file extensions alone are insufficient.

- **Operational:** can the selected components perform the required operation
  and pass the required information, with stated preservation and output meaning?
- **Runtime/resource:** can this resolved setup run with available dependencies,
  model assets and resources? Is the proposed computation within the declared
  budget? Some conditions can only be checked during preparation or execution.
- **Scientific:** how well do the evaluation domain, output definition and input
  transformations support the intended use? Under D18, justified exploratory
  extrapolation remains possible; computational compatibility does not establish
  reliable biological evidence, and weak empirical support is not the same as a
  mechanically incompatible input.

Unknown support must remain unknown until checked; no universal confidence value
combines these dimensions. Preliminary compatibility checks can reject an
impossible composition without promising that execution will succeed.

### Worked mismatch: partial diffusion states and a complete-sequence classifier

A rollout-guidance strategy needs an engine that can advance/branch compatible
partial states, a way to obtain supported complete sequence views, and a usable
family evaluator. If those operations are available, the plan can explicitly
compose continuation, sequence/chemical completion as needed, conversion and
evaluation. Each rollout retains its source state, assumptions, exact evaluated
input and cost. A family score applies to the completion; any aggregate used to
choose its parent branch is a strategy's estimate, not a direct measurement of
the partial state's bioactivity.

Multiple continuations, inverse folding and structural checks can make this far
more expensive than final filtering. An adapter that merely extracts an argmax
sequence from a noisy state supplies a different heuristic, requiring its own
scientific rationale. It does not establish equivalence to completed rollouts.

If the generator only emits terminal outputs and has no continuation access,
this particular strategy is unavailable through that adapter. An alternative
engine or an explicitly adapted sampler may satisfy it. Final filtering or outer
search may still address the scientific problem, but substituting either is a
different strategy choice. A plan can pre-authorize a named alternative with
conditions; execution must record its actual use. Otherwise return the mismatch
for an explicit plan revision, not a silent fallback or a false guidance claim.

## 4. Three organizational alternatives

These A–C alternatives organize compatibility; they do not reopen the accepted
alternative B separating scientific problem, plan and execution evidence.

| Alternative | Advantages | Costs / limits |
| --- | --- | --- |
| A. Pairwise strategy/backend integrations with explicit checks | Straightforward for a few engines; keeps method-specific details close to code. | Repeated compatibility logic and conversions; growing pair count makes scientific assumptions hard to compare. Still a viable bounded prototype. |
| B. Small composable capability descriptions plus explicit plan recipes | Reuses matching concepts across engines while keeping optional operations optional; composite adaptations and costs remain reviewable. | Requires careful descriptions and pre/postconditions; too many names can become an ontology or hidden universal interface. |
| C. General typed operation graph with automatic planning/inference | Can discover compositions and validate complicated chains. | Significant semantic/solver infrastructure; may select scientifically questionable conversions and duplicate Praxis or workflow responsibilities. No demonstrated current need. |

**Accepted conceptual choice: B (D25)**, with a small vocabulary grounded
in these cases and manual explicit compositions initially. Retain A for genuinely
specialized integration details. Revisit C only if concrete cases justify it;
no registry schema, type system or general planning engine is proposed for
implementation. A universal interface containing every operation would mostly
encode unsupported methods and is not required by B.

The [expanded assessment](protein_peptide_design_engines.md#8-revised-p09-recommendation-and-next-approvals)
supports B, now **accepted conceptually**, with domain/deployment-specific support
and non-transitive access through optional composite providers. Chaperone is not
made mandatory, and a native model's operations are not automatically exposed by
a workflow/service adapter. Those conceptual support/access principles are now
accepted under D23–D24; concrete contracts remain deferred. No universal
interface follows from composability.

## 5. Matrix from public implementations

Snapshot check on **2026-10-26** confirmed the five repository HEAD revisions
below match the earlier pinned inspection. **All 'observed' entries mean source
inspection, not installed execution or scientific qualification.** Documented
mechanisms and adaptation possibilities are distinguished explicitly.

| Resource, immutable revision and inspected entry points | Inputs/outputs and source-observed capabilities | Additional adaptation / qualification needed |
| --- | --- | --- |
| [PepMLM `3169c49`](https://github.com/programmablebio/pepmlm/blob/3169c4920f8c383948e0a5d3a7c8f87e5e7d2436/scripts/generation.py) | Target sequence plus requested length; fully masked binder region, per-position top-k generation; returns sequence/pseudo-perplexity results. Logits are internal; inference uses `no_grad`. | Public return does not expose logits, gradients, arbitrary partial infill or continuation. A wrapper can expose supported internal values; custom remasking or feedback decoding changes the sampler and needs qualification. |
| [DiffPepBuilder `c19eb4f`](https://github.com/YuzheWangPKU/DiffPepBuilder/blob/c19eb4f0cd2419d3bcc116184c0868243b6c4169/experiments/run_inference.py), [inference internals](https://github.com/YuzheWangPKU/DiffPepBuilder/blob/c19eb4f0cd2419d3bcc116184c0868243b6c4169/experiments/train.py), [configuration](https://github.com/YuzheWangPKU/DiffPepBuilder/blob/c19eb4f0cd2419d3bcc116184c0868243b6c4169/config/inference.yaml) | Prepared receptor features, native receptor fixed masks, structural diffusion and final residue logits/sampling. Saves structures and optionally trajectories; exposes step/noise/length/temperature settings and disulfide processing. | The inspected loop restarts its schedule at 1.0 and runs under `no_grad`; trajectory export is not a resumable/forkable-state API. External family callbacks, arbitrary peptide infill and differentiable guidance were not verified. |
| [PepTune `ce4daf0` search](https://github.com/sophtang/PepTune/blob/ce4daf00ade848cca7007b04b70ae9fe54ed2268/src/pareto_mcts.py), [scorers](https://github.com/sophtang/PepTune/blob/ce4daf00ade848cca7007b04b70ae9fe54ed2268/src/scoring/scoring_functions.py) | Internal masked peptide-SMILES states/timesteps, denoising expansion and completed rollouts; validity checks, objective vectors and tree updates. Protein sequences enter binding scorers in this path, guiding search rather than establishing protein conditioning of the base denoiser. | Search code is tied to its MDLM/tokenizer operations. Reusing it with another generator needs equivalent continuation/branching semantics. New family scorers need chemical/semantic mappings; the current scorer set is not an arbitrary plugin guarantee. |
| [HydrAMP `6590d2f`](https://github.com/szczurek-lab/hydramp/blob/6590d2f4c2963f25d30669052a4c4a857e0e7279/amp/inference/inference.py) | `unconstrained_generation` and seed-based `analogue_generation`; AMP-related conditions, latent perturbation controls and internal classifier/filter selection; native sequence arrays include a 25-position shape. | No native arbitrary protein conditioning or trajectory-continuation interface observed. Analogue generation is not exact masked mutation. Even `filter_out=False` selects among decoded attempts using internal scores in the inspected path; it is not automatically an unselected raw decoder sampler. |
| [PrMFTP `42488d2`](https://github.com/xialab-ahu/PrMFTP/blob/42488d2e1a2cc2855375717fa926d21c8887783e/predictor.py) | A sequence evaluator, not a generator: encoding/padding, ensemble prediction and a named 21-label output after thresholding. | Continuous score export, arbitrary partial-input support and a gradient interface are not provided by this entry point. Adaptation must retain output meanings and applicability; neural layers do not establish those operations. |

The [primary literature and earlier code review](literature.md) provide the
scientific precedents. Specific native controls are not guarantees of activity,
arbitrary chemistry or model portability. None of these observations chooses a
PeptideMT model or claims every absent entry is impossible in the underlying model.

### What can really be reused across generators?

A ranking/Pareto policy can be reused when objective meanings, directions,
constraints and missing-evidence behavior are compatible. A black-box outer
optimizer can share control logic across different compatible proposal/edit
providers, including generators that supply only restarts. Its moves remain
representation-specific; a sequence mutation operator is not automatically a
backbone, graph or cyclic-peptide operator.

Tree selection or particle allocation can be shared only where engines expose
appropriate state/continuation/completion semantics; a common list of methods
does not prove equivalent transition laws. Gradient guidance and density-based
composition demand still stronger variable/derivative or probability semantics.
Reusable policy does not mean identical cost, valid chemistry, neighborhood,
sampling law or scientific evidential strength.

## 6. Seven accepted conceptual principles

**All seven principles are conceptually approved under D25**, within D15–D24's
limits and D26's information obligation. None is a concrete software contract:

1. Providers declare conditional operations and their evidence; strategies state
   requirements; plans select explicit compositions; executions record actual use.
2. Describe representation, information and preservation semantics, not just
   operation names. Capabilities can be native, adapter-supplied or composed.
3. Keep optional operations optional. Partial outputs and non-generative
   evaluators remain first-class participants; no universal gradient/state API.
4. Separate operational compatibility, runtime availability and scientific
   applicability, preserving justified exploratory uses under P08.
5. Identify missing, incompatible or unknown support before use where possible,
   and record runtime failures; do not silently substitute another strategy.
6. Explicit adaptations and authorized alternatives retain inputs, assumptions,
   provenance, additional costs and attribution limits under P07/P08.
7. Reuse ecosystem owners rather than adding a molecular engine, generic workflow
   planner or project database. Strategy reuse must remain bounded by the actual
   operations and scientifically meaningful outputs it requires.

The earlier phrase 'capabilities a plan must declare' is corrected: the plan
declares **selected usage and composition**; available capabilities come from
the providers and requirements from the strategy. The investigators now approve
the organization and all seven principles; concrete interfaces, classes, schemas,
registries and automatic composition mechanisms remain unapproved.

## 7. Ownership and what remains for Codex

Use the [preserved ecosystem audit](integration_audit.md): MolSysMT owns supported
molecular representation/manipulation and correspondence; PeptideMT adds design
relations and local algorithm/evaluation semantics. Praxis owns reusable cross-tool
methodology; this analysis does not require reimplementing its catalog/executor.
Recorda can observe operations while native results retain their meaning. Nextia
owns project-level context/evidence. SMonitor, ArgDigest and DepDigest can support
diagnostics, argument checks and optional dependency availability; none decides
biological applicability or supplies a missing scientific operation. PyUnitWizard
keeps meaningful quantities distinct from uncalibrated scores.

After approval and sufficient capability-specific requirements, leave Codex
freedom to choose internal classes/composition, data structures, dispatch and
discovery, validation mechanics, batching, caching, process/service boundaries,
state handling, tests and performance optimizations. Any technical choice that
changes scientific meaning, supported promises or owner boundaries returns to
discussion. In particular, choosing a lossy chemical projection, changing a
required constraint, inventing a partial-state reward or substituting a strategy
is not an unrestricted internal implementation detail. Representation/interface
choices explicitly deferred in P07 also remain open, rather than being silently
delegated or decided here. No code or development issue is introduced.

The domain-aware provider principle and optional composite access are now
accepted. The following cases support the now-accepted conceptual meaning and
organization. They remain probes, not selected implementations or runs.

## 8. Three tests of minimum capability meaning

### Case A — RFD4 with a CPP or multi-label evaluator

**Invariant intent:** propose peptides recognizing a specified molecular target
with the requested functional property/properties. A predictor's score is an
operational search signal under its own source definitions, not that intent.

There are two different strategies, which must not be assigned the same needs:

| Strategy | What must be effectively accessible | What need not be exposed to PeptideMT |
| --- | --- | --- |
| Delegate RFD4's native reward search | Target/design conditions; a supported way to bind the external evaluator and reward outputs to native search; relevant evaluation checkpoints/policy and actual result/limitation reporting. | Raw sampler tensors, external step/branch control or an exported trajectory, if the native procedure manages them itself. |
| Let PeptideMT control trajectory allocation | Compatible initialization/advance, continuation and branching semantics; supported scoring views/completions; evaluator access and policy/cost control. | A common tensor format across engines, gradients or a new implementation of the denoiser. These are not required merely for black-box reward use. |

**Evidence boundary:** the inspected RFD4
[search configuration logic](https://github.com/RosettaCommons/RFD4-Proteina/blob/aaccdd2ad0720c180468df5f9cf037a713d403e5/src/rfproteina/search/beam_search.py)
checks selected metrics and their groups. Clean-prediction checkpoints admit
design metrics only; refolding metrics require an explicitly selected oracle.
Thus even native 'custom metric support' is conditional on where and how a metric
runs. An external PeptideMT step/branch adapter is not established by that code.
See the [engine review](protein_peptide_design_engines.md#4-rfd4-proteina-unusually-relevant-access-still-domain-limited-evidence)
for pinned native search, metric, reward and deployment evidence.

**Inputs and subjects:** generation uses the supported target/design context,
conditions and sampling state. Evaluation uses a specific completed continuation
or decoded clean estimate, the selected peptide region, correspondence to the
complex and the predictor's actual supported view. Complete-sequence decoding
does not by itself resolve termini, links or stereochemistry. A sequence-only
method may evaluate the available partial proposal directly when it admits it;
if it requires missing chemistry, introduce explicit hypothetical realizations.
Do not silently invent those realizations merely to simplify the data model.

For cyclic/modified candidates, extracting canonical letters is a projection
with attribution limits, not proof of chemical equivalence. Evaluate several
explicit realizations if warranted, preserving which one produced each result.
The reward attached to a continuation is not a direct functional evaluation of
its incomplete parent, nor of every realization sharing its letters.

**Function and intervention:** one multi-label evaluator can expose several
source-qualified outputs. Select relevant outputs; preserve the raw vector and
contradictory evidence. Thresholded-only output and continuous score access are
different operations. Neither all 21 outputs nor perfect calibration is required.
Native search may consume a scalarized reward while PeptideMT retains the
underlying objectives and missing values. A missing metric must remain missing,
even if the backend assigns it an exclusion reward. Evaluation must affect later
allocation to count as search guidance; final-only filtering does not supply it.

**Compatibility conclusion:** delegated reward search can be a valid composition
without externally exposed sampler states. It still needs an actual evaluator
extension, correct molecular views, usable environments and declared scientific
limits. The current CPP/multi-label integration is a proposal, not an implemented
capability. A different service route may fail the operation requirement even
while using related model weights. No gradient compatibility is assumed.

### Case B — Chaperone running a structural workflow

**Intent and plan:** address the same kind of design problem using a selected
complete workflow. PeptideMT selects the recipe, inputs and exposed controls;
Chaperone can own its internal block execution and resource submission.

**Claim that can be made:** execute this configured procedure on these admitted
inputs and return its observed proposals/results/artifact references and limits.
Its internal generation/refold/filter stages can be documented constituents
without becoming individually callable PeptideMT capabilities. The inspected
[block entry](https://github.com/RosettaCommons/chaperone/blob/a86eb8355c6e362590238c381de13dcba9bef0e0/src/chaperone/block_config/base.py)
and [result schema](https://github.com/RosettaCommons/chaperone/blob/a86eb8355c6e362590238c381de13dcba9bef0e0/src/chaperone/data/schema.py)
support block/data-handler execution and molecular/metric/lineage outputs;
neither creates a universal internal-state or family-reward interface.

Fundamental information includes **which entity is designed and which is the
target**, the admitted molecular views, exposed conditions and preservation
semantics, workflow/version/assets where identifiable, result meanings and
scientific evidence/unknowns. The inverse-direction peptide-binder example in the
engine review demonstrates why a recipe title is insufficient. Target sequence
preservation and target-coordinate preservation must remain distinguishable.

Dependencies, containers, weights, site configuration and total resource policy
become contextual requirements for execution. Separate submitted/running/completed
work and produced/filtered/no candidates without imposing an execution-status
enum here. Zero retained candidates can be a completed procedure; a skipped stage
was not executed. Rerun/caching behavior matters when a plan depends on fresh
sampling, but does not require exposing every internal random variable.

**Compatibility conclusion:** this route can satisfy a complete-proposal workflow
strategy while failing a requirement to inject a reward inside its generator.
It could support that stronger requirement only if the actual block/recipe exposes
it. Do not infer support from a constituent model or relabel between-block filters
as within-generator guidance. Unknown internal proposals/costs remain unknown.

Retain native artifacts and known lineage plus P07 attribution; do not promote
workflow IDs to canonical chemical identity. MolSysMT owns supported molecular
operations, Praxis reusable methodology, Chaperone this delegated execution and
Recorda observable recording. Assign scheduling ownership per boundary and avoid
duplicate job submission/counting. No general orchestrator is needed in PeptideMT.

### Case C — a general protein engine used for short peptides

**Hypothetical probe, not a new experimental result:** a resolved target-conditioned
engine accepts a 15-residue design, and a bounded execution in that configuration
has succeeded. Available scientific evidence is mainly for longer globular
proteins; peptide performance remains poorly established.

The operation/input requirements can be met and runtime availability demonstrated
while scientific applicability remains uncertain. Record what was executed,
the target/design chemistry and length, constraints, known training/benchmark
coverage and its gaps. Do not infer unsupported length limits from a default,
turn a larger-protein benchmark into a peptide benchmark, or create a universal
'validated generator' flag. Output chemistry may still be incomplete under P07.

Under D18 an explicitly exploratory plan may use this engine, with a rationale
for how its proposals and evaluations address the problem and with bounded
interpretation. The same evidence may be insufficient for a claim that the
engine reliably designs that peptide class. The purpose of use matters: generating
diverse hypotheses, ranking them and independently assessing them make different
claims. No default numerical applicability score is justified.

This permission does not repair a mechanical incompatibility. If the resolved
model cannot represent the requested ring, accepts only a different alphabet or
the adapter fails to preserve a required condition, call that mismatch explicitly.
A hypothetical projection/completion or altered strategy is a plan change with
its own assumptions, not scientific evidence supplied by the protein engine.

**Compatibility conclusion:** limited empirical evidence need not exclude useful
exploration, but technical success cannot satisfy an unsupported scientific
promise. The evidence gaps, transformations, budget, assessment role and outcome
must remain traceable. No requirement for new experimental validation is imposed
on completing a computational campaign.

## 9. Alternatives for expressing and checking the meaning

These alternatives explain expression/checking within the accepted P09 direction;
they are not new names for the earlier A–C organizational alternatives.

| Expression approach | Benefits | Limits exposed by the three cases |
| --- | --- | --- |
| Narrative resource profiles plus method-specific human checks | Minimal infrastructure; accommodates opaque workflows and unusual chemistry. | Easy to overlook the same input/preservation mismatch repeatedly; difficult to compare changes across versions or automate even basic checks. |
| Small evidence-linked semantic claims plus explicit strategy requirements and contextual checks | Shared meaning where justified, optional method-specific detail, explanations of satisfied/failed/unresolved requirements. Supports native delegated search and opaque procedures without a universal state API. | Needs careful scientific definitions and a policy for unknowns; a structured form must not pretend all empirical judgments are decidable. |
| Formal pre/postcondition/domain calculus and automatic composition | Strong mechanical checks and potential discovery of long compositions. | Premature vocabulary/solver burden, uncertain scientific inference, and overlap with Praxis/execution systems. The cases do not justify a general planner. |

**Accepted conceptual approach (D25–D26):** the middle approach, with narrative evidence and
method-specific checks where formalization adds little. Retain simple manual
composition. No file format, field list, class/interface, logic language, registry
or automatic matching implementation is selected.

A matching explanation should answer: which strategy requirement is addressed,
by which resolved operation, under which assumptions, with which limits, and what
is established or still unresolved across D22's three dimensions. A requirement
can be satisfied by an explicit composition; identical operation names or shared
input types are insufficient. Operational composition must preserve relevant
meaning, not just data flow. Some checks are static, some require preparation/
execution and some remain scientific judgment.

Do not default unknown information to either a guarantee or a global rejection.
An unknown indispensable operation leaves that strategy unresolved until inspected,
adapted or revised; uncertain biological applicability can support a justified
exploratory use. An unavailable GPU is a runtime condition, not loss of the model's
generative operation. An unavailable internal callback cannot be fixed by more
runtime resources. Explicit alternative plans are allowed; silent substitutions
that change the search or scientific claim are not an implementation detail.

## 10. Next decision and implementation freedom

**Resolved conceptually:** preserve the meaning of a claim and justify the
particular strategy's requirements without a universal mandatory metadata record.
The section 2 examples do not require separate approval of each possible attribute.
Concrete operation contracts, interfaces, schemas, registries and checks remain
to be specified when a particular capability is prepared for implementation.

The [bounded horizon review](future_horizons.md#9-bounded-extensibility-review-after-p09-approval)
checks libraries, state panels and transformation products without reopening P09
or adopting future features. The next major discussion is
[P04 evaluation and selection](open_questions.md#p04-proposed-discussion-sequence).

Next scientific/architectural choices include required molecular preservation,
permitted approximations and attribution, exploratory-use rationale, treatment of
missing/conflicting evaluations and acceptable exposure at each execution boundary.
Reward versus independent assessment and scientific intent versus operational
criteria remain distinct. Many functional families and joint target/family
guidance remain central, without requiring PeptideMT-owned foundation models.

After capability-specific obligations and acceptance criteria are mature,
Codex can choose internal structures, dispatch, validation machinery, batching,
cache mechanics and process wrappers within them. API/contracts and P07's explicit
identity/chemistry/storage deferrals still require their own discussion; they are
not automatically delegated. A technical choice that changes preservation,
attribution, strategy or the scientific promise returns to the investigators.
No software or issue creation is authorized by this semantic analysis.
