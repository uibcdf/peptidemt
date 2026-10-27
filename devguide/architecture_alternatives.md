# Alternatives for representing design problems

Status: **alternative B accepted conceptually on 2026-10-26** (D09–D13).
Alternatives A/C are retained as discussion history, not competing adopted
architectures. No API, class names or storage schema is approved.
Navigation: [index](README.md) · [literature](literature.md) · [open questions](open_questions.md).

## Shared requirements

A representation should accommodate positive/negative molecular targets,
candidate space and chemistry, desired functional families, interaction and
physicochemical objectives, optional biological context, evidence expectations,
hard constraints, diversity and selection requirements.

Available predictors/generators, search strategy and budgets must also be
representable, but need not be part of the immutable scientific question.
The same intent should be comparable across different methods, with exact
configuration and evidence retained. Redesign adds seeds and preservation/edit
requirements; de novo omits seeds without requiring another evaluation system.

Functional families should identify the intended concept, context and definition
independently of the evaluator. A model binding adds training-data provenance,
output semantics/calibration, applicability and versions. A family-conditioned
generator and a family predictor provide different capabilities; neither is
inferred merely from the other's presence.

These are semantic requirements, not a decision to create a large class hierarchy.
Families remain initially simple and extensible. Joint target/family design is
central; target-free tasks remain possible. See the
[worked examples](design_examples.md) for the first conceptual stress test.

## A. One declarative design specification

One small serializable document contains scientific intent, model choices,
search configuration and outputs/references.

**Benefits:** simple to inspect, easy to save, low initial implementation cost.
**Costs:** changing a generator changes the whole specification; scientific
intent and method choice can become entangled. Cross-method comparisons need
explicitly marked invariant sections. A schema can grow into an opaque bag of
options if generic dictionaries replace semantics.

This remains viable if the problem/execution distinction is visible as sections,
even before separate objects exist.

## B. Scientific problem, computational plan and execution evidence

**Accepted conceptual separation (D09).** The problem describes candidate domain, targets, families, objectives,
constraints, optional context and evidence/selection requirements. A separate
plan binds evaluators, proposal mechanisms, optimizers, budgets, seeds and
policies. A run records actual choices, attempts and results.

**Benefits:** one scientific question can be addressed by different algorithms;
family identity remains independent of a model; reproducible comparisons have
a clear unit.
**Costs:** more reference/version relationships and explicit compatibility checks.
Some requirements depend on method support, so preparation must detect an
unexecutable request without silently weakening it.

Approval covers the separation, not how it is encoded. A future small document
could contain distinct sections; separate files or objects are also possible.
Execution evidence must distinguish the intended plan from what actually ran,
including partial coverage, failures and deviations. Do not invent a platform
Run, scheduler or project database: local computational evidence is distinct
from Nextia's project-scientific Evidence and Praxis method records.

Replacing a generator or predictor can preserve the scientific problem while
changing the evidential strength of the answer. A plan may explore only a
declared subset of the allowed domain. Changing the target, required chemistry,
functional meaning or scientifically required preservation changes the problem
or creates an explicitly related variant; it is not a silent plan substitution.

## C. Typed objective/constraint graph

Represent requirements and transformations as a graph of typed nodes: family
evaluation, target-state evaluation, proposal generation, constraint enforcement,
aggregation and selection.

**Benefits:** handles multiple targets/states and staged evaluations; dependencies
and conditional work can be explicit.
**Costs:** graph validation, execution semantics, persistence and authoring are
substantial. It risks duplicating Praxis and Nextia and obscuring a simple task.
Start with this only if concrete cases exceed the expressive power of A/B.
A future compiler may derive a local evaluation graph without making it the
scientist-facing specification.

## Constraints, objectives and evidence

A hard sequence/chemistry constraint has an exact declared predicate over the
candidate representation. A predictor threshold can be enforced exactly on a
score but cannot guarantee the underlying biological activity.
Desired access to a compartment belongs to scientific intent; a threshold on
model X's CPP score belongs to a plan's operational policy. Conversely, a
scientific requirement such as a binding-affinity bound with explicit units and
conditions can belong to the problem. Its surrogate must not replace its meaning.
If the actual requested quantity is unmeasured/unassessed, retain that status.
Masking residues does not enforce a global compositional rule automatically;
partial-state feasibility and final validation are separate obligations.

Family compatibility may be a score objective, likelihood/prior, applicability
region or a generation condition. Positive and negative molecular targets require
named evaluations; lack of a negative-target score is not proof of specificity.
Retain noncomparable scores separately and record every scalarization.

Uncertainty may be calibrated probability, ensemble variation, interval or an
unavailable value. Applicability may combine training overlap, chemical support
and empirical performance slices. Do not represent these different objects by
a single invented confidence percentage.

## Interchangeable capabilities without universal hooks

A generator can propose complete sequences, structures, SMILES or partial states.
An evaluator may require a complete canonical sequence or a molecular complex.
An optimizer can use only compatible representations and access levels.

Capability descriptions should state whether the adapter supports batch proposals,
seed edits, partial-state evaluation, resampling, log probabilities, gradients,
infill, native conditions and hard constraints. Unsupported requests must remain
visible. No single gradient callback should be mandatory.

Complete-sequence black-box predictors can guide an outer optimizer or score
rollouts from partial states. Gradient guidance requires a differentiable path
or a trained surrogate; a random forest does not become differentiable by being
wrapped. Backbone diffusion may not expose sequence states: family scoring may
belong at inverse folding or an outer alternating search.

No generator/predictor contract or concrete method name is adopted here.

## P07 reconsidered: proposals, chemistry, views and evaluation subjects

Status: **alternative III accepted conceptually as D15–D16**, 2026-10-26,
including explicit hypothetical realizations and qualified evaluations. The
comparison below preserves the reasoning; no class hierarchy or storage design
is approved. Canonical identity, state grouping, identifiers, persistence,
concrete interfaces and initial chemistry support remain open.
See the [four cases and additional probes](design_examples.md).

The earlier candidate-versus-representation proposal omitted a stage: a useful
design output may not yet specify a chemical molecule. A sequence may leave
termini, chirality or modifications unresolved. A backbone-first proposal may
lack residue identities and side chains. Missing coordinates alone, however,
do not make chemical identity incomplete. A representation missing information
also does not imply that its referenced candidate lacks that information.

### Alternatives within the accepted three-way architecture

These alternatives concern P07; they do not reopen architectural alternatives A/B/C.

| Alternative | Advantages | Costs and scientific failure modes |
| --- | --- | --- |
| I. Require a chemically defined candidate at entry | Uniform molecular references and fewer downstream completion checks. | Forces invented defaults or excludes sequence/backbone outputs and early evaluators. Admissible as a particular plan's gate, but unsuitable as the platform entry requirement. |
| II. Keep one generic design item with optional fields that are filled in over time | Low initial ceremony; supports any generator output. | Evaluations can appear to apply to chemistry determined later. Mutation in place obscures assumptions, branching and provenance unless historical views and relations are made explicit. With those safeguards it approaches III in meaning. |
| III. Permit incomplete proposals and explicitly relate their chemical realizations, views and evaluations | Supports early predictions, chemical branching and convergent derivations without inventing chemistry; matches heterogeneous engines. | Requires explicit unknowns, transformations and attribution. Can become overengineered if each distinction becomes a mandatory object or workflow stage. |

**Accepted conceptual choice: III, with semantic distinctions rather than mandatory
layers.** A fully specified chemical proposal can already serve as a candidate;
there need not be an artificial completion operation. The same conceptual record
format could express several roles if it preserves their meaning and history.
No universal molecular representation, five-class inheritance tree or workflow
engine follows from this approval. A generic record as in II remains an encoding
possibility if it preserves the adopted distinctions, attribution and branching.
The choice concerns scientific semantics before software structure.

### Accepted responsibilities and illustrative detail, not an API

The seven approved P07 principles are recorded in [decisions](decisions.md).
The following elaborates their meaning; individual field inventories and the
compatibility table are illustrative rather than approved schemas.

- A **peptide proposal** preserves what was actually generated, its origin,
  determined information, unresolved choices and declared assumptions. It may
  be a sequence, partial backbone, masked sequence or other useful partial design.
  Some evaluations can apply immediately; others must wait or abstain.
- A **chemical candidate** specifies enough molecular identity to distinguish
  the chemical alternatives under discussion: building blocks, connectivity,
  applicable stereochemistry, termini and covalent modifications. This does not
  require coordinates, a preferred conformer or a bound pose. What counts as
  sufficient identity, and how protonation/tautomer states are grouped under a
  parent, remain unresolved; preserve the actual species used in an evaluation.
- **Representations and feature views** need not preserve the same information.
  A sequence, molecular graph, coordinate file and descriptor vector are not
  automatically mutually convertible. Descriptors are lossy derived inputs;
  they are not a new chemical identity. Preserve what a view omits, and whether
  missing information was unknown in the proposal or discarded from a known
  candidate. A file hash can identify an input artifact, not prove molecular
  equivalence across formats.
- **States, conformers and poses** qualify the molecular situation evaluated.
  A pose additionally depends on the target/state and preparation. No assumption
  that all such changes either preserve or change candidate identity is adopted.
- An **evaluation subject** identifies the proposal/candidate or partial design,
  the exact input view and relevant state/complex. Preserve determined chemistry,
  transformations/defaults, evaluator/model version, actual predicted property,
  context and attribution limits. A sequence-only score is a valid result on
  that input when supported; it is not automatically evidence for every later
  cap, stereoisomer or crosslinked realization.

| Evaluator input | Information it actually needs | Boundary of attribution |
| --- | --- | --- |
| Amino-acid sequence | A supported, sufficiently resolved residue sequence and the model's input conventions. | Does not resolve omitted termini, links or delivery context. |
| Physicochemical descriptors | The declared descriptor definitions, computation inputs and assumptions (including chemistry/pH where relevant). | Sequence-derived charge and species-specific molecular charge are different inputs/claims. |
| Molecular structure | Supported chemistry plus the coordinates/state or ensemble required by the method. | One conformer is not automatically an ensemble result or a bound state. |
| Target complex | Specified peptide and target preparations, states, pose/interface and any relevant environment. | Interaction evidence is not automatically inhibition, organism activity or cell access. |

This is a conceptual compatibility table, not four mandatory adapter types. An
evaluator may consume several inputs; a sequence model may also require a target
sequence. Unsupported input can lead to deferral or abstention while other
evaluations proceed. Scientific hard-constraint satisfaction may itself remain
unknown until the required information is determined.

The scientific problem declares the allowed domain and desired functions. The
plan decides when to complete chemistry, prepare views, evaluate or defer, and
how to select under missing evidence. The execution records the actual branches,
assumptions and outputs. An unfinished proposal can be a legitimate campaign
result, explicitly distinguished from a chemically specified final shortlist.
Neither condition alone proves functional activity.

When information is missing, the plan may introduce one or more **explicit
hypothetical chemical realizations** to meet an evaluator's requirements. Keep
the original proposal unchanged in meaning, the introduced assumptions and each
evaluation's actual subject. A realization need not be experimental or known to
exist in the sampled biological environment. A directly generated complete
molecule, partial sequence or backbone need not traverse artificial stages.

### Relations and counterexamples that matter

One sequence proposal can branch into free-terminal and amidated candidates.
That completion adds chemical information; it is not merely a file conversion.
An explicit all-L convention comes from recorded problem/plan assumptions, not
from the appearance of uppercase letters alone. Two independent generators can
arrive at the same chemically specified molecule: chemical deduplication must
preserve both derivations. Redesign instead changes specified features; retain
the parent and edit assumptions. One proposal may also be rejected as outside
the scientific domain without losing its generation record.

A backbone proposal can lead to several sequence designs and chemical candidates.
A backbone geometry evaluation applies to that backbone; a sequence predictor
requires a supported sequence completion or rollout. The rollout is an evaluated
hypothesis, not the unique identity of the parent partial design. Its score may
guide search under a recorded policy but must not be presented as a direct
measurement of an unfinished backbone's bioactivity.

Completing a proposal later does not retroactively complete the chemistry seen
by an earlier evaluation. Reusing a cached result requires an explicit
input/model/context equivalence policy and justified attribution; sharing a
one-letter sequence is insufficient. Conflicting evaluations remain separate.
Distinguish genuine disagreement on comparable claims from different organisms,
endpoints, chemical realizations, input projections or applicability failures.

### MolSysMT reuse and additional PeptideMT meaning

Use the [source-pinned audit](integration_audit.md#molsysmt): public molecular
`get/select/convert/extract`, `build.build_peptide`, `build.mutate`, preparation
reports and available correspondence maps belong to MolSysMT. Its experimental
`physchem.get_peptide_chemical_template` is coordinate-free but does not supply
arbitrary capped/cyclic/modified chemistry or declared stereochemistry.
`native.ChemicalStates` uses a stable atom-index domain; it does not establish
our parent/species identity policy or represent every atom-inventory change.
Missing-heavy-atom mutation outputs are not proof of universal partial-design
support. These are inspected code boundaries, not new execution qualifications.

PeptideMT should retain design-specific meaning **around**, rather than duplicate,
those molecular artifacts: proposal-to-realization and parent/redesign relations;
known/unknown/assumed chemistry; evaluation-to-view associations; transformation
purpose and losses; and which design requirements remain assessable. Atom/residue
correspondences should reference MolSysMT maps where actually available, not
invent an independent topology engine. Generic missing molecular capabilities
belong with MolSysMT; negotiation of extensions is future work.

A partial proposal need not be forced into a supposedly complete MolSysMT system.
Keep the native partial output and its interpretation until a supported conversion
is possible. Record unavailable mappings explicitly. Nothing here establishes a
new partial-molecule backend, identifier syntax, persistence service or adapter.

### Evidence and remaining uncertainty

The existing sequence, structural and multi-label model precedents justify
heterogeneous inputs; the cases expose why chemical branching and output
attribution matter. They do not prove an implementation of III is preferable
in cost or usability. Review whether these minimal distinctions suffice for
mixed-chemistry inputs, ambiguous mixtures and source annotations later; do not
add a comprehensive entity ontology now. P07's semantic alternative is accepted;
the explicitly deferred identity/interface/storage questions remain open. The
broader family-catalog proposal P08 is the next discussion; see its
[alternatives and model-composition exercise](functional_families.md#p08-conceptual-alternatives-and-generative-use).
