# Scientific vision and scope

Status: **provisional definition supplied by the investigators**, 2026-10-26.
Navigation: [index](README.md) · [decisions](decisions.md) · [questions](open_questions.md).

## Purpose

PeptideMT is a computational peptide-design platform that generates, redesigns,
evaluates and optimizes peptide sequences, exploring regions of sequence space
conditioned on molecular targets, bioactive functional families and configurable
constraints.

Practical research utility takes priority over inventing a new algorithm.
Target-directed design is central, but optional for tasks where a protein-binding
mechanism is inappropriate or unknown. The scope includes CPPs, AMPs, ACPs, AFPs,
other families, and combinations such as CPP+ACP or CPP+AMP.

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

## Scientific distinctions retained

Describe separately physicochemical properties, access/exposure, molecular
recognition, mechanism and phenotype. These distinctions help interpret outputs;
they do not restrict the platform to campaigns demonstrating the entire chain.

Targets may include positive and negative targets, selected sites, conformational
or chemical states, and unavailable/uncertain structural information. Desired
binding is not necessarily inhibition or activation.

Sequence strings are convenient views, not complete chemical identity.
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

The platform should represent all three without making the mechanism of one
case mandatory for the others.

## Outside the present phase

No scientific implementation, fixed API, mandatory generator, frozen molecular
alphabet, first experimental demonstrator or new model-training program is
approved. Full workflow scheduling, scientific-project history and generic
recording belong to their ecosystem owners. Universal prediction of biological
efficacy, inferred mechanisms from classification alone and guaranteed joint
activity are not product claims.
