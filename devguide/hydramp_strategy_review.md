# HydrAMP direction: compatibility, independent fork or scientific successor

Status: **own-use/full-modernization direction recorded; staged scope proposed**,
2026-11-03.
Owner: [PeptideMT #32](https://github.com/uibcdf/peptidemt/issues/32), with existing
provider questions in [HydrAMP #4](https://github.com/uibcdf/hydramp/issues/4),
[#5](https://github.com/uibcdf/hydramp/issues/5) and
[#6](https://github.com/uibcdf/hydramp/issues/6).

## Subsequent investigator steering — own use and full modernization

The investigator now prioritizes modernizing HydrAMP's complete original
functional scope for our own use, with possible collaboration/contact only at
the end. The [proposed staged programme](hydramp_full_modernization.md) records
the objective, source inventory and module boundaries. This steers the earlier
collaboration-first recommendation below; it does not approve every missing
module, training or a new scientific method. D41 remains unchanged. The generic
standalone-contract work has not resumed; first decide the actual module scope.
No authors are contacted. Earlier option comparisons below are retained as
discussion history rather than the latest execution plan.

## Investigator pause and unchanged acceptance

The investigator explicitly pauses the proposed independent result/workflow
contract to consider strategic direction first. Do not begin that design or its
implementation while this discussion is unresolved. The pause does not revoke
[D41 experimental AMP resource acceptance](hydramp_dev3_acceptance.md), authorize
new model calls or select a new architecture. No strategic recommendation below
is an accepted decision. No authors have been contacted.

The [product review](hydramp_product_review.md) identifies missing independent
product capabilities. Its proposed implementation order is a backlog, not a
commission to turn the fork into a separate platform before this decision.

## Primary-source context inspected

- The [original project](https://github.com/szczurek-lab/hydramp) documents both
  analogue and unconstrained generation plus training material. The accepted
  modern port implements a selected unfiltered de novo inference route, not
  every original feature or modern training.
- The [original paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC10017685/)
  describes a conditional VAE with AMP and low-MIC conditions. Its pretrained
  conditions do not constitute a demonstrated other-family predictor.
- The lab's [HydrAMP starter](https://github.com/szczurek-lab/hydramp-starter-kit)
  presents HydrAMP as an AMP Challenge 2027 baseline. Its classifier-filtered
  challenge workflow differs from our deliberately unfiltered accepted route.
  That source shows continuing reference utility, not author interest in a port.
- The same lab publishes [OmegAMP](https://github.com/szczurek-lab/OmegAMP),
  describing a diffusion-based AMP approach. This makes alternative-method
  comparison relevant; it proves neither that HydrAMP is abandoned nor that a
  diffusion model is preferable for our future question.

These were read-only sources. No challenge submission, new evaluation,
dataset/model acquisition or external publication/contact occurred.

## Comparison of directions — recommendation, not disposition

| Direction | Value | Cost/risk | Current recommendation |
| --- | --- | --- | --- |
| Compatible modernization suitable for collaboration | Preserve original method identity, assets, meaningful API behavior and a traceable numerical comparison; offer a useful modern inference backend. | PyTorch is already a substantial implementation rewrite; compatibility must be defined and evidenced. A full-feature migration is not yet delivered. | Preferred immediate direction: a small, clearly scoped scientific port with reviewable engineering and honest differences. |
| Independently maintained fork | Permit improvements on our timetable and retain a usable backend if upstream integration is unavailable. | We own maintenance, acquisition, documentation, compatibility, scientific validation and eventual distribution decisions. Custom infrastructure can increase integration cost. | Keep this option available; expand when a concrete user need and sustainable ownership justify the divergence. |
| Family-extensible scientific successor | Potentially address new functional questions and reuse the engineering/validation experience. | Needs its own scientific hypothesis, data/labels, training strategy, comparators and prospective evaluation; inheritance is not evidence that this architecture is the best starting point. | Investigate feasibility under #5, but do not transform the accepted reference resource by default. |

Scientific closeness and textual diff size are different. Retaining weights,
equations, inputs, score meanings and traceability can preserve scientific
continuity across a large backend rewrite. Conversely, a small new filter or
changed condition can alter scientific behavior. Keep justified modern numerical
improvements and explicit failure reports; closeness does not mean reproducing
known legacy approximations merely for identical FP32 bytes.

PeptideMT can progress as an orchestrator of multiple resources without owning
a new learned method or expanding HydrAMP into the platform. Its existing
adapters/contracts are the place for consumer-specific integration. Do not impose
MolI-specific dependencies on the core before deciding their benefit and the
collaboration boundary. Existing modular ownership and reuse obligations remain.

## Other families: generation and prediction are distinct questions

Separate a classifier that predicts functional labels from a generator that
proposes sequences conditioned on a function. They need not use the same model
or live inside a transformed HydrAMP. Existing AMP/MIC heads do not become CPP
or multifunctional predictors by changing a label or adding an output field.

A family-extensible hypothesis could reuse our numerical validation, conversion
experience, occurrence tracing and modular engineering. Whether to reuse this
latent architecture or pretrained representation is a separate empirical choice.
The current modern port does not provide a qualified encoder/training pipeline;
moving beyond its inference route would be substantial new scientific work.

Before choosing that route, define whether the task is prediction, generation,
or both; select a concrete new function and experimental endpoint; assess data,
labels/negatives, multi-function overlap, chemistry and train/test leakage; and
compare a faithful baseline against alternatives on prospectively agreed goals.
Keep new scientific identity/claims distinct from reproducing the original method.
No training, family expansion, novel method or benchmark is commissioned here.

## Proposed practical posture

1. Retain the exact accepted modern HydrAMP as a reproducible reference resource.
2. Keep a collaboration-oriented port boundary: no silent scientific changes or
   unnecessary platform coupling; preserve original attribution and legacy reference.
3. Prepare a factual, scoped contribution summary for internal review, including
   missing original features and numerical differences. Author interest is unknown;
   later contact requires explicit permission for recipient/channel/content.
4. Keep independent product maintenance and successor research as separate
   decisions. Decide a scientific reason to diverge rather than accumulating
   a new project accidentally through packaging work.

This revises the earlier priority of proceeding directly to a portable standalone
contract: first agree what we want to contribute, maintain and scientifically
claim. A portable record or CLI may still be useful, but its ownership and
scope should follow that direction. Collaboration and a future distinct method
can coexist; neither should be treated as a guaranteed outcome or prerequisite
for the other.
