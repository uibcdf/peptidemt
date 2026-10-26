# Open questions

Navigation: [index](README.md) · [alternatives](architecture_alternatives.md) · [decisions](decisions.md).
All questions remain open unless an explicit decision is recorded.

Updated: 2026-10-26. Alternative B is accepted under D09–D13; the
[worked cases](design_examples.md) are analysis, not additional approvals.

## Q1. Design intent and execution

**Resolved conceptually:** scientific intent, computational plan and execution
evidence are separate; families are independent of their models. No class names,
API, storage or implementation is approved. Remaining questions concern minimal
representations, evidence obligations and plan comparability, not whether to
adopt the separation. See D09–D13 and the worked cases.

## Q2. Family definitions and evidence

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

**Proposed next decision (P07), awaiting approval:** distinguish one chemical
candidate from its sequence/graph/file representations and from molecular states,
conformers, bound poses and generated derivatives. Decide which differences
create a different chemical candidate before choosing identifier formats.

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
