# AMP tools and models: initial resource cards

Status: **maintained discovery records**, 2026-10-29.
Navigation: [catalogue](tools_catalog.md) · [AMP conversation](https://github.com/uibcdf/peptidemt/discussions/10)
· [dated survey and source inventory](generative_resource_survey.md).

These seven initial cards reuse the accepted Macrel evidence and the exact
source snapshots in the survey. They introduce no new model calls or scientific
acceptance. Each resource has one conversation, linked from family indexes.
Additional surveyed AMP/search resources remain in the survey; this first set
is neither an exhaustive inventory nor a performance ranking.

## Macrel

- **Role:** optional AMP and adverse-hemolysis evaluator, not a generator.
- **Source:** [1.6.1 source](https://github.com/BigDataBiology/macrel/tree/190462605913844dca74b184869755609fbb20b2).
- **Readiness:** the exact Linux CPU bundle is accepted under D37. The original
  PeptideMT numerical producer is `7a299d1a9e1b264c2f872e94d35b76d67c548a0a`;
  preserve its environment, artifact hashes and direct-native evidence.
- **Limits:** only unchanged admitted sequence views; no assay-level AMP potency,
  universal calibrated probability, CPP activity or cytosolic-delivery claim.
  Chemistry, leading-M handling and the two selectors retain D35/M1–M8.
- **Maintained evidence/question:** [acceptance](increment_1_review.md) and
  [qualification](w3_assessment.md). How should later independent evaluators
  complement this bounded resource without erasing conflicting observations?

## HydrAMP

- **Role:** AMP/low-MIC-conditioned de novo generation; analogue generation is
  a separate native operation.
- **Source:** [frozen source](https://github.com/szczurek-lab/hydramp/tree/6590d2f4c2963f25d30669052a4c4a857e0e7279).
- **Readiness:** D38 commissions bounded preparation/qualification, not scientific
  acceptance. Source and starter assets were acquired earlier; runtime closure
  remains partial under [#8](https://github.com/uibcdf/peptidemt/issues/8).
- **Limits:** original Python 3.8/TensorFlow 2.2/Keras 2.3 dependencies; unresolved
  original modlAMP/mysql acquisition. A modern fork and new multi-family training
  are distinct, uncommissioned research directions.
- **Maintained evidence/question:** [work record](pending_proposals/qualify_hydramp_increment_2.md).
  Can the native bounded reference be qualified, preserving its weights and
  scientific meaning, before considering a separately tested modernization?

## PLUM

- **Role:** AMP/non-AMP and length-conditioned VAE, with separate prototype guidance.
- **Source:** [frozen source](https://github.com/priyamayur/PLUM/tree/650fdae718f8e761deb2c96ff428766854d050a3).
- **Readiness:** source inspected; MIT code; named generative checkpoint files and
  a CPU route observed. No PeptideMT installed or scientific qualification.
- **Limits:** README declares Python >=3.12, but unpinned dependencies include
  frameworks outside generation. Exact Python 3.14 closure, artifact identity and
  native length/training-match rejection behavior remain to qualify.
- **Maintained evidence/question:** [survey](generative_resource_survey.md).
  Does its conditional/prototype route supply useful complementary proposals
  under an independently qualified minimal environment?

## OmegAMP

- **Role:** diffusion generation with de novo/analogue/motif routes and explicit
  length, charge and hydrophobicity controls.
- **Source:** [frozen source](https://github.com/szczurek-lab/OmegAMP/tree/20b691b5b6f74ef86bc83f34d5610e30cd456c96).
- **Readiness:** source inspected; MIT code; Python >=3.11 manifest and externally
  linked generator/embedding assets. Assets and execution remain unqualified.
- **Limits:** its unconditional strategy still fixes the AMP condition; property
  controls do not constitute arbitrary protein-target conditioning. Exact
  scikit-learn and remaining dependencies need a tested Python 3.14 route.
- **Maintained evidence/question:** [survey](generative_resource_survey.md).
  Are native motif/property controls scientifically useful and operationally
  bounded for a future sequence-design commission?

## ARCADIAMP

- **Role:** EvoDiff-D3PM-based AMP generation, separate from classifier/novelty screening.
- **Source:** [frozen source](https://github.com/IBPA/ARCADIAMP/tree/70448c14a176399640a26095782e870b7204c338).
- **Readiness:** source inspected; Apache-2.0 code; named model archives, documented
  CPU inference and Python 3.11.9 guidance. No installed PeptideMT qualification.
- **Limits:** qualify generator assets/base dependencies and CPU cost separately
  from the notebook's screening cascade. Reported study outcomes do not transfer
  to newly generated PeptideMT candidates.
- **Maintained evidence/question:** [survey](generative_resource_survey.md).
  Can a bounded native generator call be received independently of the complete
  screening pipeline and its internal selection policy?

## AMP-Designer

- **Role:** GPT-based AMP-enriched generation; separate distillation and MIC predictors.
- **Source:** [frozen source](https://github.com/jkwang93/AMP-Designer/tree/07d455dd6eb7ef61fe03b85732966caa32bf3dc4).
- **Readiness:** source inspected; MIT code and externally linked weights. Its
  Python >=3.8 statement is not an exact Python 3.8 requirement.
- **Limits:** older SciPy pins and the rest of the stack need a real Python 3.14
  route; config/tokenizer/model identities remain to receive. The example CLI
  hardcodes paths and 100 batches, unsuitable as an inherited execution budget.
- **Maintained evidence/question:** [survey](generative_resource_survey.md).
  Which native callable permits bounded generation with explicit sampling and
  complete artifact provenance?

## PepDiffusion

- **Role:** transformer VAE and latent diffusion for AMP sequence proposals.
- **Source:** [frozen source](https://github.com/Wangyj2023/PepDiffusion/tree/6570dddaf1cac6b5210202bb135d876bebcf6d12).
- **Readiness:** source inspected; no installed PeptideMT qualification.
- **Limits:** README specifies Python 3.8.18/PyTorch 1.13.1, GPU-oriented examples
  and explicit checkpoint paths. Publication recency does not establish a current
  runtime, usable CPU route, artifact completeness or permission to redistribute.
- **Maintained evidence/question:** [survey](generative_resource_survey.md).
  What distinct scientific contribution would justify its own environment,
  asset/terms review and execution qualification?

## Stewardship

Repository maintainers own triage under [the catalogue rules](tools_catalog.md).
New integration, runtime changes and scientific execution require their own
bounded work and authorization. Discovery threads remain open independently of
those issues. General molecular-system operations remain in MolSysMT; optional
availability, diagnostics and attribution retain their registered suite owners.
