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
