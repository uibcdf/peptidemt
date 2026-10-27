# Learned functional spaces and generative search

Status: **targeted literature/implementation review, 2026-10-26**.
Navigation: [index](README.md) · [scope](vision_scope.md) · [alternatives](architecture_alternatives.md).

For a broader inventory of multifunctional peptide labels, datasets and models,
see [functional_families.md](functional_families.md). This document concentrates
on learned search and integration strategies rather than an exhaustive function list.
The [strategy comparison](generative_strategies.md) develops mathematical and
capability implications without selecting a generative architecture.

Primary papers establish reported evidence; official source inspection establishes
bounded implementation observations. No listed model was installed or executed
here. This is a working review, not an exhaustive systematic survey or model
selection decision. Weights, licenses, compute and reproducibility need a later
engine-specific review.

## A. Predictors, distributions and conditions are different assets

A discriminative score s_F(x) estimates compatibility with labels defined by a
particular dataset/model. It does not define a sampler q_F(x). Even a calibrated
training-distribution P(F|x) does not by itself determine P(x|F): a sequence prior,
class prevalence and sampling procedure are also needed.

A family-enriched proposal q_F(x) may represent several disconnected modes,
motifs, lengths, scaffolds or mechanisms. High density may encode collection
bias and close homologs rather than broad functional coverage. A low-dimensional
embedding plot does not prove a biological manifold or a connected feasible set.
One-class learning, density estimation and sampling are distinct capabilities.

A target-conditioned generator q_0(x|T) can be reweighted conceptually as:

    q*(x|T) proportional to q_0(x|T) * 1_C(x) * exp(sum_j w_j s_j(x))

C denotes explicit candidate constraints; scores can include functional-family,
recognition and other objectives. This is an engineered search distribution,
not a claim to recover the true joint biological conditional. Sampling it
exactly, learning its normalizer and guaranteeing experimental activity are not
established by the expression. Reweighting cannot recover modes outside q_0's
support. A different proposal distribution or edits may be necessary.

Combining independent scores is not estimating joint CPP+ACP probability.
Correlated descriptors, overlapping training sets and common annotation practices
can double-count the same signal. A multilabel model can learn dependencies
when suitable joint labels exist, but missing labels require explicit handling
and its correlations may still be dataset-specific. Neither approach proves
that both activities coexist in the chosen biological context.

Products of family distributions can collapse diversity or double-count a shared
sequence prior; mixtures preserve alternatives but do not enforce conjunction.
Compare combinations empirically and retain component scores and family modes.

## B. Compatible intervention levels and constraint controls

| Intervention | Existing family models reusable without full generator retraining? | Required access / limits |
| --- | --- | --- |
| Post-filter | Yes, complete compatible candidates suffice. | Does not alter proposal distribution internally; rare joint acceptance may be costly. |
| External optimization | Yes: evolutionary, Bayesian, mutation or alternating proposal/evaluation loops. | Requires editable candidates or compatible proposal calls; preservation of binding must be reevaluated. |
| Sampling-time guidance | Often: rollout/tree/resampling can consume black-box scores on completed candidates. Gradient guidance requires a compatible differentiable path or surrogate. | Partial sequences/noisy states may be outside a clean-sequence classifier's domain. Decode/complete rollouts instead, at extra cost. |
| Learned conditioning | Reuse a pretrained conditional generator when relevant conditions already exist; otherwise adapter/head/fine-tuning/training may be necessary. | A target-conditioned model does not acquire CPP conditioning merely by accepting a new label string. |
| Hard constraints | Often for native masks, fixed positions, alphabets and supported chemistry. | Global counts/motifs/chemical validity need appropriate feasibility logic and final verification; score thresholds constrain scores, not biological truth. |

These can coexist. For example, an outer optimizer can call a family-conditioned
generator with native fixed positions, score target recognition and apply final
chemical validation. Such combinations are proposals, not current integrations.

A fair comparison fixes proposal/evaluator versions, budgets, target/state,
candidate domain and constraints. Report acceptance, diversity, novelty,
applicability, recognition retention and independent evaluation. Gains against
the same reward model alone are not demonstrated biological improvement.

## C. Public precedents and integration limits

### PepTune — inference-time multiobjective tree guidance

Tang, Zhang and Chatterjee, ICML 2025,
[PMLR 267:59017–59065](https://proceedings.mlr.press/v267/tang25n.html).
The paper reports tree guidance using classifier rewards with masked discrete
diffusion over peptide SMILES. It is a direct precedent for inference-time
guidance without retraining the whole generator for every objective.

Official source inspected at
[ce4daf0](https://github.com/sophtang/PepTune/tree/ce4daf00ade848cca7007b04b70ae9fe54ed2268):
[src/pareto_mcts.py](https://github.com/sophtang/PepTune/blob/ce4daf00ade848cca7007b04b70ae9fe54ed2268/src/pareto_mcts.py)
and [ScoringFunctions](https://github.com/sophtang/PepTune/blob/ce4daf00ade848cca7007b04b70ae9fe54ed2268/src/scoring/scoring_functions.py)
separate tree search and score vectors. Its supplied permeability evaluator is
PAMPA-based, not a CPP/cytosolic-access classifier. Replacing scores needs explicit
representation/domain/direction adapters and qualification; no drop-in
compatibility with arbitrary family models is established.

### NOS / LaMBO-2 — differentiable guided sequence diffusion

Gruver et al., NeurIPS 2023,
[Protein Design with Guided Discrete Diffusion](https://papers.nips.cc/paper_files/paper/2023/file/29591f355702c3f4436991335784b503-Paper-Conference.pdf).

The method guides hidden states using gradients and combines sequence diffusion
with objective optimization. It supports the principle of learned-property-guided
sampling. Its antibody setting is not evidence of CPP+target performance.

Official [source and training instructions](https://github.com/ngruver/NOS/blob/569f1c85adf2ca2ea5e32efdf46276995fcf322c/README.md)
include a discriminative head and guided sampling. This does not provide
gradients for an arbitrary random-forest CPP classifier. Reusing a compatible
head may avoid full retraining; a new surrogate/head may still need training.

### PepMLM — target-sequence-conditioned linear binder proposals

Chen et al., online publication 2025 (journal issue 2026),
[Target sequence-conditioned design of peptide binders using masked language modeling](https://doi.org/10.1038/s41587-025-02761-2).
Official [implementation instructions](https://github.com/programmablebio/pepmlm/blob/3169c4920f8c383948e0a5d3a7c8f87e5e7d2436/README.md)
load a masked language model and tokenizer with a published model identifier.

Target-aware complete proposals can be filtered or used by an external search
without full retraining. Infill/decoding or logit guidance are possible adaptation
questions, not verified native family-guidance interfaces. Reported
intracellular results involving expressed fusions do not establish delivery of
the corresponding free synthetic peptide.

Additional source observation: the inspected
[generation routine](https://github.com/programmablebio/pepmlm/blob/3169c4920f8c383948e0a5d3a7c8f87e5e7d2436/scripts/generation.py)
samples per-position top-k logits for a fully masked binder region, then computes
pseudo-perplexity. It does not expose a native family-feedback or autoregressive
continuation loop. Custom remasking/decoding is an adaptation to qualify;
pseudo-perplexity must not be treated as normalized molecular likelihood or
binding affinity. No execution is claimed.

### DiffPepBuilder — structural target-conditioned co-design

Wang et al., 2024, JCIM,
[DOI 10.1021/acs.jcim.4c00975](https://doi.org/10.1021/acs.jcim.4c00975).
Official [source](https://github.com/YuzheWangPKU/DiffPepBuilder/tree/c19eb4f0cd2419d3bcc116184c0868243b6c4169)
documents target structure/hotspots, inference configuration and sequence/structure
co-design; it also now contains DiffPepDock.

Filtering and outer optimization are plausible without full retraining.
Sequence-family guidance inside joint structural diffusion needs compatible
sequence states/evaluators or completed rollouts. No generic family callback was
verified. Its environment and PyRosetta postprocessing need independent review;
do not force them into the host's Python environment.

### RFpeptides and ProteinMPNN — structural and sequence stages

[Accurate de novo design of high-affinity protein-binding macrocycles using deep learning](https://www.nature.com/articles/s41589-025-01929-w),
Nature Chemical Biology, 2025, reports macrocycle binder design with structural
generation, sequence design and structural evaluation. It supplies evidence for
targeted macrocycle design, not a universal CPP constraint.

The official [ProteinMPNN options](https://github.com/dauparas/ProteinMPNN/blob/8907e6671bfbfc92303b5f79c4b5e6ce47cdef57/README.md)
include fixed positions, omitted amino acids, residue biases and tied positions.
These are concrete native sequence controls. Biases do not guarantee family
activity or exact global composition. In backbone-first pipelines, family
guidance may naturally enter inverse folding or an outer alternating loop;
a backbone denoiser may have no sequence for a CPP classifier to score.

### HydrAMP — a family-enriched proposal model

[Discovering highly potent antimicrobial peptides with deep generative model HydrAMP](https://www.nature.com/articles/s41467-023-36994-z),
Nature Communications, 2023, describes conditional VAE-based AMP design.

Official [HydrAMPGenerator](https://github.com/szczurek-lab/hydramp/blob/6590d2f4c2963f25d30669052a4c4a857e0e7279/README.md)
documents analogue and unconstrained generation. This is a concrete precedent
for both seed-based and de novo family-first proposals.
Adding target recognition externally is a proposed composition, not a native
target-conditioned binder capability. The documented Python 3.8/custom TensorFlow
context illustrates why optional process/environment adapters may be necessary.

## D. Positive, negative and missing labels

### PrMFTP — 21-label source-level integration observations

Additional inspection: **2026-10-26**, no model installation or execution.
[Yan et al. (2022)](https://doi.org/10.1371/journal.pcbi.1010511) reports
sequence-based multi-label prediction, sigmoid outputs and a 0.5 label threshold.
This is not demonstrated calibration or a learned joint activity distribution.

At official source revision
[`42488d2`](https://github.com/xialab-ahu/PrMFTP/tree/42488d2e1a2cc2855375717fa926d21c8887783e),
[`predictor.py`](https://github.com/xialab-ahu/PrMFTP/blob/42488d2e1a2cc2855375717fa926d21c8887783e/predictor.py)
encodes sequence letters, pads to 50 positions, averages ten checkpoints and
thresholds the averages before exporting named labels. Its fixed output-name
order must accompany the checkpoint. An exported `none` means no thresholded
label, not measured absence of all functions. It does not export the continuous
scores as a ready-made reward interface.

[`MLTP/main.py`](https://github.com/xialab-ahu/PrMFTP/blob/42488d2e1a2cc2855375717fa926d21c8887783e/MLTP/main.py)
filters training inputs above 50 residues; the prediction script does not provide
equivalent explicit length rejection. Its `X` encoding does not establish
qualified prediction on masked/ambiguous proposals. The
[requirements](https://github.com/xialab-ahu/PrMFTP/blob/42488d2e1a2cc2855375717fa926d21c8887783e/requirements.txt)
pin legacy Keras/TensorFlow; environment and launch-path qualification remain
pending. These are source observations, not a successful runtime check.

**Proposed adaptation, not implemented:** preserve per-output scores and model
provenance before thresholding when accessible; distinguish the discrete-label
capability from continuous scoring. Validate chemical/input applicability and
label mapping separately. The
[P08 composition exercise](functional_families.md#p08-conceptual-alternatives-and-generative-use)
considers a structural target-conditioned generator. Its concrete counterpart,
[DiffPepBuilder's inspected instructions](https://github.com/YuzheWangPKU/DiffPepBuilder/blob/c19eb4f0cd2419d3bcc116184c0868243b6c4169/README.md),
uses prepared receptor data, sequence/structure generation and optional disulfide
construction/postprocessing. That chemistry cannot be assumed covered by a
sequence-only functional predictor. No native cross-model guidance is established.

| Family/example | Primary evidence about dataset construction | Consequence for PeptideMT |
| --- | --- | --- |
| CPP: CPPred-FL | [DOI 10.1093/bib/bby091](https://doi.org/10.1093/bib/bby091) describes CPP924 positives from CPPsite and random-sequence negatives. | Score may distinguish curated CPPs from that artificial background, not experimentally tested nonpenetrators in our candidate population. |
| AMP: Macrel | [PeerJ e10555](https://peerj.com/articles/10555/) describes non-AMP sequences selected from UniProt by absence of several annotations. | Preserve unannotated/sampled versus measured-negative status and class balance; do not equate annotation absence with inactivity. |
| ACP: AntiCP 2.0 | [DOI 10.1093/bib/bbaa153](https://doi.org/10.1093/bib/bbaa153) uses different negatives in main/alternate sets; peptides with both anticancer and antimicrobial properties were removed when constructing the main comparison. | That classification contrast may oppose the multifunctional region we seek. Keep model/dataset label semantics, not only an ACP name. |
| AFP: Antifp | [Original study](https://pmc.ncbi.nlm.nih.gov/articles/5834480/) uses exclusive AFP positives and other AMPs and/or random SwissProt-derived negatives, depending on dataset. | Family-exclusivity construction and annotation gaps can distort multifunctional search. AFP versus other AMP is not the same task as AFP versus random background. |

These are examples, not claims about every predictor in a family. Public
standalone code/data are available for
[AntiCP 2.0](https://webs.iiitd.edu.in/raghava/anticp2/) and
[Macrel](https://github.com/BigDataBiology/macrel); they were not executed here.
A public model or benchmark does not establish a PeptideMT-ready dependency.

[Benchmarks in antimicrobial peptide prediction are biased due to the selection
of negative data](https://doi.org/10.1093/bib/bbac343) provides a direct methodological
warning. Evaluate models on common, disjoint, context-relevant data; use clustered
and, when possible, temporal/source-separated splits, not just random splits.
Deduplicate across source databases and prevent close homologs/analogues from
leaking into validation. Report precision-recall, calibration and operating
points under the relevant prevalence; balanced accuracy alone is insufficient.

[Learning peptide properties with positive examples only](https://doi.org/10.1039/D3DD00218G),
Digital Discovery, 2024, offers a peptide-property PU-learning precedent.
PU learning can avoid labeling every unknown negative, but requires assumptions
about positive selection and the unlabeled population. Published positives are
often selected nonrandomly; class priors and calibrated posteriors are not
automatically identifiable. One-class models can describe observed support but
may learn collection bias; they neither prove activity nor automatically generate
new sequences. Multilabel learning needs observed/missing-label masks and
assessment of annotation completeness.

## E. Safeguards and proposed comparison

1. Preserve training-set provenance, negative construction, chemistry, lengths,
   contexts, calibration and model/checkpoint identifiers.
2. Treat unsupported chemistry and unknown labels explicitly; never remove
   modifications silently to obtain a classifier input.
3. Limit extrapolation using empirical applicability slices, overlap checks,
   diverse ensembles and independent models. None supplies universal OOD proof.
4. Retain Pareto tradeoffs and multiple proposal modes; avoid rewarding correlated
   charge/hydrophobicity signals several times without checking their effect.
5. Evaluate gains beyond the search reward: held-out models/data, mode coverage,
   novelty, matched-composition controls and experiments when available.
6. Compare target-first filtering, family-first target optimization and compatible
   sampling guidance at matched budgets. Keep failures, infeasible requests and
   candidates unassessed by expensive evaluators in the result record.

The existence of these methods makes learned-family-guided binder search
plausible. Transfer to CPP+ACP/AMP, reliable joint activity and improved
experimental yield remain research hypotheses, not adopted capabilities.

## F. Inference-time steering and distribution composition

### FK steering: non-gradient trajectory allocation

Singhal et al., ICML 2025,
[A General Framework for Inference-time Scaling and Steering of Diffusion Models](https://proceedings.mlr.press/v267/singhal25b.html).
The paper studies intermediate resampling of diffusion trajectories using
reward-related potentials, including gradient-free steering. Its experiments
concern image/text generation, not joint peptide target/family design.

**Proposed relevance:** an external predictor can influence which compatible
trajectories are continued without differentiating through that predictor.
This requires access to intermediate states and continuation plus justified
future-reward estimates; a complete-output-only API does not provide these by
itself. Applying the method to peptide engines or partial chemical views needs
separate qualification. Paper inspected; no code/runtime audit claimed here.

### Feynman-Kac Correctors: a limit of naive model composition

Skreta et al., ICML 2025,
[Feynman-Kac Correctors in Diffusion: Annealing, Guidance, and Product of Experts](https://proceedings.mlr.press/v267/skreta25a.html).
The paper derives weighted simulation/correction methods for annealed and
composed diffusion distributions, with molecular and image examples.
It shows why heuristic score combinations need not track the intended
intermediate distributions.

**Proposed relevance:** combining pretrained models can avoid universal
retraining, but a product of models' scores is not automatically a sampler for
the desired terminal distribution. Shared output domains, normalization/support,
representation multiplicity and the cost of corrections must be examined.
No arbitrary cross-tokenizer peptide composition or drop-in MolSysSuite adapter
is established. This is a methodological precedent, not an adopted engine;
paper inspected, implementation and peptide-family transfer unqualified.

### Interpretation of uncalibrated and extrapolative rewards

Under accepted D18–D19, perfect calibration is not required to try a justified
ranking signal. Model-data/chemistry support, observed discrimination and
independent assessment remain separate questions. Exploration may be justified
beyond a model's validated domain, but the score is then qualified as such;
syntactic acceptance is not scientific applicability. Improvement against the
reward model alone establishes reward optimization. Independent evidence may
be absent; computational completion does not require inventing it or claiming
biological validation. No formal evidence hierarchy is introduced here.
