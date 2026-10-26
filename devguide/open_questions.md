# Open questions

Navigation: [index](README.md) · [alternatives](architecture_alternatives.md) · [decisions](decisions.md).
All questions remain open unless an explicit decision is recorded.

## Q1. Design intent and execution

Should scientific intent remain invariant when generators, evaluators and search
policies change? Alternative B recommends separating intent from realization;
A can encode that boundary as two sections initially. What are the minimum
semantics of a functional-family requirement independent of its predictor?

Resolve this before choosing the first model or experimental demonstrator.

## Q2. Family definitions and evidence

Which differences require distinct family definitions versus contexts or assays?
How do CPP membership, uptake and cytosolic access relate without being merged?
How should AFP relate to the chosen broad or narrow meaning of AMP?
Can context be unavailable while still permitting a computational task?
How do model-specific label semantics affect multifamily requests?

## Q3. Candidate chemistry and representation

What is the initial supported subset, and how do we preserve unsupported
modifications? How do sequence, chemical identity, conformer and target-bound
pose remain distinguishable? Which MolSysMT experimental boundaries require
pinned adapters? No canonical-only permanent scope is adopted.

## Q4. Labels, negatives and applicability

For each model, are negatives measured, inferred, sampled or merely unannotated?
Can we obtain training data and cluster-aware/temporal evaluation?
Which PU/one-class approaches help under source selection bias?
When should an evaluator abstain rather than extrapolate?

## Q5. Combining families and recognition

Use independent predictors, a multilabel model, family priors, expert
combinations, Pareto selection, or several together? How will correlated
descriptors and overlapping training sets be detected? What preserves
recognition when a family-driven optimizer edits a binder?

## Q6. Guidance access and budgets

Which engines expose partial states, infilling, likelihoods or gradients?
Can completed rollouts support a black-box family evaluator?
What predictor budget and independent validation suffice to show enrichment
beyond final filtering? Do improvements survive length/composition controls?

## Q7. Ecosystem and publication

When should the documentation workspace seek central admission?
Which minimal optional adapters justify initial dependencies?
How do local design attempts reference future Nextia project Candidates?
How do Praxis Protocols refer to PeptideMT algorithm settings without duplicating
them? Recorda captures operations; what native result provenance stays local?

## Q8. Demonstrators and experiments — explicitly deferred

Which seed-based and de novo cases best discriminate the competing strategies?
What assays and collaborators are available? What evidence would support
mechanism, specificity or joint activity? No answer is required to approve the
general computational design scope.
