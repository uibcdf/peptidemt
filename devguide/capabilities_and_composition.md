# Capabilities, strategy requirements and explicit composition

Status: **partial conceptual approval (D21–D22), remaining P09 proposals and
source-level analysis**, 2026-10-26. No capability schema, software contract, API
or class hierarchy is approved. Navigation: [index](README.md) · [strategies](generative_strategies.md)
· [families](functional_families.md) · [decisions](decisions.md).

The [expanded engine review](protein_peptide_design_engines.md) adds general
protein-design engines, Chaperone, RFD4, short-peptide benchmarks and revised
composition recommendations. The five-model matrix below is the earlier bounded
subset, not an exclusion of general protein engines. **P09 remains open.**

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

The three dimensions below are **accepted conceptually under D22**. The detailed
matching/policy organization remains a recommendation: match requirements against
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

**Recommendation: B as conceptual direction**, with a small vocabulary grounded
in these cases and manual explicit compositions initially. Retain A for genuinely
specialized integration details. Revisit C only if concrete cases justify it;
no registry schema, type system or general planning engine is proposed for
implementation. A universal interface containing every operation would mostly
encode unsupported methods and is not required by B.

The [expanded assessment](protein_peptide_design_engines.md#8-revised-p09-recommendation-and-next-approvals)
retains B as a **pending** recommendation, with domain/deployment-specific support
and non-transitive access through optional composite providers. Chaperone is not
made mandatory, and a native model's operations are not automatically exposed by
a workflow/service adapter. No universal interface follows from composability.

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

## 6. Minimal principles proposed for approval

Principles 1 and 4 have **conceptual approval under D21–D22**; the other
refinements and the detailed organization remain pending under P09. None is an
accepted software contract:

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
the responsibility separation and compatibility dimensions, without approving
the organizational alternative, all refinements or a software contract.

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

**Next discussion proposed:** agree or revise the domain-aware provider principle
in the [expanded review](protein_peptide_design_engines.md#8-revised-p09-recommendation-and-next-approvals),
then discuss minimal operation/domain semantics and optional composite access.
The responsibility owners are settled conceptually; all seven refinements and a
universal interface do not follow from that agreement.
