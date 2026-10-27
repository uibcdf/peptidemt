# Scientific vision and scope

Status: **provisional definition supplied by the investigators**, 2026-10-26.
Navigation: [index](README.md) · [decisions](decisions.md) · [questions](open_questions.md).

## Purpose

PeptideMT is a computational peptide-design platform that generates, redesigns,
evaluates and optimizes peptide sequences, exploring regions of sequence space
conditioned on molecular targets, bioactive functional families and configurable
constraints.

Conceptual architecture D09 separates this scientific intent, a computational
plan and execution evidence. D10–D13 keep families independent of their models,
initially simple/extensible, and preserve joint target/family conditioning as a
central objective. See [worked examples](design_examples.md).

The [scientific north star](scientific_trajectory.md) records why combining
function-guided proposal search and molecular-target engagement remains central
as implementation progresses. The [published-evidence-anchored MDM2/MDMX-p53
cell-permeating anticancer peptide case](case_study_cpp_anticancer_mdm2_mdmx.md)
offers a stringent future reference without changing V0.1 chemistry or targets.
The [CPP development-case portfolio](cpp_case_portfolio.md) broadens this
reference with simpler linear and cargo examples, an intrinsically cell-permeant
**p28–p53** anticancer peptide, and scientifically distinct conditional and
chemically modified delivery cases. "CPP" remains a qualified, context-dependent
concept; tumor tissue penetration and endosomal escape are not automatically
cytosolic-delivery labels.

The [representative CPP project pool](cpp_guided_projects.md) deliberately distinguishes
sequence-level uptake, cargo delivery, endosomal escape, cytosolic access,
tumor-homing/tissue penetration, pH-dependent membrane insertion and
intracellular targeted anticancer function. They are different evidence endpoints
and chemical modalities, not interchangeable labels or V0.1 requirements.

Practical research utility takes priority over inventing a new algorithm.
Target-directed design is central, but optional for tasks where a protein-binding
mechanism is inappropriate or unknown. The scope includes CPPs, AMPs, ACPs, AFPs,
other families, and combinations such as CPP+ACP or CPP+AMP. The
[literature-based functional-family survey](functional_families.md) identifies
many additional antimicrobial, antiviral, antiparasitic, physiological, delivery,
signaling and mechanistic categories; none is automatically a qualified model
or a supported implementation.

A completed computational campaign produces a reproducible set of proposals,
evaluations, selection decisions and explicit limitations. Experimental evidence
can strengthen or challenge those outputs; it is not a prerequisite for declaring
the computation finished. Predicted family compatibility is not demonstrated
activity, and a binding score is not experimental affinity.

## Three complementary uses of functional-family knowledge

A family is a scientific/computational concept independent of a concrete model.

1. **Discriminative evaluation:** a predictor supplies a family-compatibility
   score, sometimes written conceptually as P(family | sequence). Record whether
   the output is calibrated, the negative-data construction and applicability.
2. **Learned proposal distribution:** a model represents or samples sequences
   enriched in the family, conceptually P(sequence | family). This is a different
   capability from discriminative classification.
3. **Generation condition or guidance:** a procedure favors family-compatible
   proposals while also accounting for targets and constraints, conceptually
   P(sequence | target, families, context). No claim is made that a selected
   model already learns the true biological conditional distribution.

The same family may have several definitions, assays, model implementations and
learned modes. A CPP sequence model, PAMPA predictor and cytosolic-access assay
must not be silently treated as interchangeable.

A desired family property is distinct from an operational proxy. For example,
cytosolic access is a scientific objective; selecting candidates above a model
score threshold is a plan policy and establishes only the stated score result.
No full family ontology is needed to preserve a short definition, context,
references and explicit unknowns. P08 alternative 2 accepts a small extensible
scientific concept catalog linked to source definitions and resources (D17–D20);
the exact fields and encoding remain proposals. Scientific relations, co-annotation
and model correlations remain distinct. Multiple roles and outputs do not turn
one multi-label model into independent confirmations.

Justified indirect or exploratory signals may guide proposals without directly
assessing the desired function. Perfect calibration is not required for useful
search ranking; applicability, utility hypotheses and independent assessment
must remain explicit. Improvement of the reward used in search is not independent
evidence of improved biology. Direct/indirect/unavailable evidence and doubtful
applicability are conceptual distinctions, not a formal state hierarchy.

## Scientific distinctions retained

Describe separately physicochemical properties, access/exposure, molecular
recognition, mechanism and phenotype. These distinctions help interpret outputs;
they do not restrict the platform to campaigns demonstrating the entire chain.

Targets may include positive and negative targets, selected sites, conformational
or chemical states, and unavailable/uncertain structural information. Desired
binding is not necessarily inhibition or activation.

Sequence strings are convenient views, not complete chemical identity.
Useful proposals can be sequence-only, backbone-first or otherwise incomplete;
chemical completion is not a universal prerequisite to generation or supported
early evaluation. Missing chemistry and omitted information in a view of a known
molecule must remain distinguishable. P07 alternative III is accepted under
D15–D16: explicit relations and evaluation attribution, including hypothetical
realizations, without mandatory stages or a fixed hierarchy. Canonical identity,
chemical-state grouping, identifiers, storage, interfaces and initial chemistry
support remain open.
Termini, chirality, modifications, cyclization and links can distinguish candidates
with the same one-letter sequence. Unsupported chemistry must be rejected or
explicitly marked unassessed, not simplified silently.

Unknown family labels remain unknown. Absence of an annotation or measurement
does not establish a negative label. One candidate may have several activities,
and family membership may depend on context.

## Common architecture, specialized science

| Case | Shared computational elements | Specialized interpretation |
| --- | --- | --- |
| Intracellular binder + CPP | Targets, family objectives, proposal/evaluation/search, diversity and provenance | Distinguish sequence compatibility, uptake and compartment access; preserve delivery context. |
| Antibacterial or antifungal peptide against a protein | Same candidate/evaluator/constraint machinery, positive and negative targets | Binding, inhibition, organism activity and access remain separate; membrane-active families need no protein target. |
| CPP + ACP against a target | Multi-family objectives, biological context and target-specific evaluations | Cell/genotype context, off-target effects and nonspecific toxicity; joint predictions do not demonstrate joint activity. |
| CPP + AMP without a molecular target | Optional target requirement, family proposals/evaluators, multiobjective search and guidance | CPP and antibacterial contexts differ; no protein mechanism or docking is mandatory. |

The platform should represent all four without making the mechanism of one
case mandatory for the others. The [additional probes](design_examples.md#9-additional-probes-from-the-broader-functional-catalog)
test overlapping labels, mechanism versus physiological effect and localization
at different biological scales. They are not selected experimental projects.

For possible longer-term scientific directions and what should be stress-tested
before freezing core contracts, see the [future horizons review](future_horizons.md).
It is an opportunity inventory, not an expansion of currently approved scope or
a commitment to implement the listed features.

## Outside the present phase

No scientific implementation, fixed API, mandatory generator, frozen molecular
alphabet, first experimental demonstrator or new model-training program is
approved. Full workflow scheduling, scientific-project history and generic
recording belong to their ecosystem owners. Universal prediction of biological
efficacy, inferred mechanisms from classification alone and guaranteed joint
activity are not product claims.
