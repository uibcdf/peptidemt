# Generative resources for a nonexclusive PeptideMT catalog

Status: **investigator-requested discovery and source inspection**, 2026-10-29.
Navigation: [design guide](README.md) · [V0.1 scope](v0_1_scope.md) ·
[existing engine review](protein_peptide_design_engines.md) ·
[immutable inspection inventory](evidence/generative_resource_survey.json).

## Purpose and evidence

The investigator clarifies that HydrAMP, a possible modern derivative, PLUM and
other resources can coexist. This reinforces D17–D26's many-to-many resource and
capability principles. An order for engineering qualification is not an exclusive
backend choice or a permanent choice of architecture. A requested function does
not select a particular model automatically.

This search extends the earlier review with primary repositories, native entry
points, dependency inputs, papers and public weight inventories. It deliberately
includes different function domains and algorithmic families. It is a bounded
survey, not an exhaustive census or a cross-paper performance ranking. Model
accuracy, reported assay outcomes and predicted improvements retain their
original study conditions; none qualifies a PeptideMT adapter here.

Eighteen inspected source blobs were matched to the frozen Git trees for ten
repositories in the JSON inventory. Four source snapshots inspected earlier in
this discussion are reused with their original full SHAs. Named weight files
are metadata observations: no new candidate checkpoint was downloaded, loaded or
verified for completeness. No alternative environment, model or GPU job ran for
this survey. The earlier HydrAMP source/checkpoint acquisition and Python 3.8
bootstrap remain a separate partial preparation under [#8](https://github.com/uibcdf/peptidemt/issues/8).

## Sequence generators with complementary AMP routes

HydrAMP and PLUM remain candidates with different identities. Neither is an
experimentally interchangeable implementation of the other.

| Resource and inspected source | Native contribution | Assets and runtime observations | Important receiving limits |
| --- | --- | --- | --- |
| **HydrAMP**, `6590d2f4c2963f25d30669052a4c4a857e0e7279` | AMP/low-MIC-conditioned de novo proposals and a separate analogue route. | Exact original source and official starter checkpoint inventory acquired under D38. Legacy Python 3.8/TensorFlow 2.2/Keras 2.3 stack; original dependency resolution fails on modlAMP's unavailable mysql pin. | Current commission is the bounded native de novo route. A modern fork is under discussion, not created or qualified. Original weights do not gain other functions by modernization. [Work record](pending_proposals/qualify_hydramp_increment_2.md). |
| **PLUM**, [650fdae718f8e761deb2c96ff428766854d050a3](https://github.com/priyamayur/PLUM/tree/650fdae718f8e761deb2c96ff428766854d050a3) | Conditional VAE: AMP/non-AMP function and length, plus separate prototype-guided generation. | README declares Python >=3.12; generator source uses PyTorch and has a CPU route. Two generative checkpoint filenames are visible in the repository. MIT code. | Requirements are unpinned and include classifier frameworks beyond the generator. Native generation excludes unsuitable lengths and training-set matches. Python 3.14 and exact checkpoint receiving are untested; associated [2026 study is a preprint](https://pubmed.ncbi.nlm.nih.gov/42124643/). |
| **OmegAMP**, [20b691b5b6f74ef86bc83f34d5610e30cd456c96](https://github.com/szczurek-lab/OmegAMP/tree/20b691b5b6f74ef86bc83f34d5610e30cd456c96) | Diffusion generation: de novo, analog, fixed motif and analog+motif; property profiles for length, charge and hydrophobicity. From the HydrAMP research group. | Programmatic generator returns sequences and conditioning. MIT code, Python >=3.11 manifest, PyTorch/Lightning; README links a generative checkpoint and embedding data on Google Drive. | Its so-called unconditional strategy still fixes isAMP=1. Targeted properties are not arbitrary protein-target conditioning. Exact scikit-learn 1.7 and other requirements need an actual Python 3.14 route; external weights/embedding files remain unverified. |
| **ARCADIAMP**, [70448c14a176399640a26095782e870b7204c338](https://github.com/IBPA/ARCADIAMP/tree/70448c14a176399640a26095782e870b7204c338) | EvoDiff-D3PM-based AMP generator; a separate two-stage classifier/novelty cascade. | README recommends Python 3.11.9 and documents CPU inference. Generator notebook calls generate_d3pm with explicit count/length/device. Named model tar files are present; Apache-2.0 code. | Qualify the generator independently of the notebook's whole screening pipeline. Verify checkpoint completeness/base dependencies and actual CPU cost. Its [published study](https://www.nature.com/articles/s41467-026-75030-8) does not qualify our generated candidates. |
| **AMP-Designer**, [07d455dd6eb7ef61fe03b85732966caa32bf3dc4](https://github.com/jkwang93/AMP-Designer/tree/07d455dd6eb7ef61fe03b85732966caa32bf3dc4) | GPT-based AMP-enriched sequence generation; separate training/distillation and MIC prediction code. | MIT code, PyTorch/Transformers; weights linked from [Zenodo](https://zenodo.org/records/17018363). README gives Python >=3.8 rather than an exact 3.8 requirement. | SciPy 1.10.0 and the rest of the route still need review for Python 3.14. CLI hardcodes paths and 100 batches; inspect the bounded native function rather than inherit that workload. Model/config/tokenizer files need matching identities. |
| **PepDiffusion**, [6570dddaf1cac6b5210202bb135d876bebcf6d12](https://github.com/Wangyj2023/PepDiffusion/tree/6570dddaf1cac6b5210202bb135d876bebcf6d12) | Transformer VAE plus latent diffusion for AMP proposals. | README specifies Python 3.8.18 and PyTorch 1.13.1, with example GPU generation and checkpoint-path parameters. | A recent publication does not imply a current runtime. Treat as another scientific/control candidate with its own asset and environment qualification, not an automatic solution to legacy dependencies. |

OmegAMP is particularly worth further inspection because its native controls
add more than another AMP score: motifs, analogue initialization and explicit
property conditioning. These observations come from its
[inference guide](https://github.com/szczurek-lab/OmegAMP/blob/20b691b5b6f74ef86bc83f34d5610e30cd456c96/README-Inference.md)
and [actual entry point](https://github.com/szczurek-lab/OmegAMP/blob/20b691b5b6f74ef86bc83f34d5610e30cd456c96/project/scripts/inference/generate_samples.py).
Their scientific and operational effectiveness remains to test.

## CPP, ACP and extensible functional learning

These candidates broaden the inventory beyond AMP. Pathogen specificity, a
cellular endpoint and binding a named protein are distinct conditions/claims.

| Resource and inspected source | Relevant operation | Current evidence and remaining work |
| --- | --- | --- |
| **CPP_Design**, [9e8e5afb66dc66c951af27bf64eef23f2806f6b3](https://github.com/IoriYamahata/CPP_Design/tree/9e8e5afb66dc66c951af27bf64eef23f2806f6b3) | EvoDiff fine-tuning/generation with CPP data and a CPP classifier. Separate optimization project combines other methods. | Sequence-generation recipe uses Python 3.9 and CUDA packages. Fine-tuned state/classifier files are visible; base EvoDiff weights may be downloaded by the native code. Verify complete base/adapter identity, bounded CPU route and source/artifact terms: no license file was found in the inspected tree. [Primary study](https://pubs.acs.org/doi/10.1021/acs.jcim.6c01267). |
| **TACaPe**, [bbb2a74f77046516322f8ab52b265572bcf0180d](https://github.com/omixlab/anticancer-peptide/tree/bbb2a74f77046516322f8ab52b265572bcf0180d) | Transformer-based ACP generation and classification; optional final classifier filtering. | MIT code, TensorFlow-based CLI and explicit training/generation commands. No pretrained weight file was found in the inspected tree. Locate a permitted trained checkpoint or account for a separate training effort before calling it ready inference. |
| **PepGenWL**, [5bf77472c111c51aa1c316c57f8a57fdfcbe5e3c](https://github.com/ZhiweiNiepku/PepGenWL/tree/5bf77472c111c51aa1c316c57f8a57fdfcbe5e3c) | Weakly order-dependent autoregressive model with continual fine-tuning; references AMP/ACP and further tasks. | Apache-2.0 code; README reports MindSpore on Ascend-910 (32 GB) and provides pretraining/fine-tuning/generation instructions. No weight file was found in the inspected tree. Interesting for learning across tasks, with substantial hardware/asset/deployment work unresolved. |
| **MMCD**, [e96d25d580591b9f6679c2786489fe3ebd4df105](https://github.com/wyky481l/MMCD/tree/e96d25d580591b9f6679c2786489fe3ebd4df105) | Multimodal contrastive diffusion using sequence and structure. [Primary paper](https://ojs.aaai.org/index.php/AAAI/article/view/27749) studies therapeutic peptide generation including AMP/ACP evaluations. | Repository demonstrates AMP-data preparation and training, and links external training data. No weight or license file was found in the inspected tree. Porting the method to other functions is not equivalent to obtaining a ready multi-family sampler. |

For ACP, preserve cell line, assay and selectivity context. For CPP, distinguish
uptake, endosomal escape and cytosolic access. A generic class label or docking
score does not substitute for these endpoints. Dataset negatives/missing labels
and overlap between functions follow the [accepted family semantics](functional_families.md).

## Search, richer chemistry and later capabilities

These resources can be useful future options while exceeding D38's current
sequence-only native qualification. A composite resource can expose generation,
scoring and search together; internal operations are not automatically a generic
callback or separate reusable API.

| Resource and inspected source | Added capability | Qualification boundary |
| --- | --- | --- |
| **AMPGAN v3**, [6f8f9294a42c8cb537d7c0a1d9272c889e797858](https://github.com/marszzibros/AMPGANv3/tree/6f8f9294a42c8cb537d7c0a1d9272c889e797858) | Conditional GAN with species/MIC/length controls and noncanonical chemical tokens; separate PepCraft agent workflow. | Three checkpoint files are visible. Manifest restricts Python >=3.11,<3.13 and bundles agent dependencies. The generator does not conceptually require adopting its agent workflow. Source/artifact permission is unresolved: no license file was found. The [2026 study is a preprint](https://arxiv.org/abs/2606.17127). Modified chemistry cannot be stripped into a falsely qualified Macrel sequence view. |
| **AMPainter**, [548017d9a6c5a508c875437b0a5f2530c958021f](https://github.com/ComputBiophys/AMPainter/tree/548017d9a6c5a508c875437b0a5f2530c958021f) | Reinforcement-learning mutation policy, fine-tuned Ankh residue proposals and HyperAMP scoring. | Several policy/scoring weight filenames are present, but complete Ankh/fine-tuned bundle and native scoring need verification. README exposes sequence evolution with its own internal feedback, not a plain de novo API. No license file was found in the inspected tree. |
| **PepINVENT**, [e976dd18d68a6e0496ec0f70d7a4dc78d473ae6c](https://github.com/MolecularAI/PepINVENT/tree/e976dd18d68a6e0496ec0f70d7a4dc78d473ae6c) | Query-position peptide design beyond canonical residues, plus multi-parameter RL objectives. | Apache-2.0 code and a named generative checkpoint; README describes pre-trained models. Supplied environment freezes Python 3.8.13, Torch 1.8.1/CUDA and includes OpenEye tooling. Qualify a supported minimal route and its dependencies/terms rather than inherit the entire environment. |
| **PepTune**, [ce4daf00ade848cca7007b04b70ae9fe54ed2268](https://github.com/sophtang/PepTune/tree/ce4daf00ade848cca7007b04b70ae9fe54ed2268) | Peptide-SMILES masked diffusion with multiobjective Monte Carlo tree search and native scoring resources. | Apache-2.0 code and external checkpoint links. Reuse the [existing source/API review](capabilities_and_composition.md#5-matrix-from-public-implementations): target sequences enter binding scorers in the inspected route, rather than establishing a target-conditioned denoiser. Chemistry, assets, costs and score meanings remain separate gates. |

The existing [target/structural review](protein_peptide_design_engines.md) already
covers PepMLM, DiffPepBuilder, RFpeptides, RFD3/RFD4, BoltzGen and related resources.
Their prior pins, target/chemistry semantics and access limits are retained; this
survey does not repeat those audits or resolve gated weights and permissions.
They remain complementary candidates for the accepted later target milestone.

## Additional leads and resources with other roles

- [KPPepGen](https://github.com/wyky481l/KPPepGen) exposes pathogen-prompt diffusion
  and knowledge-based training. Its README and [primary paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC12591163/)
  were located; exact checkpoint/environment/permissions receiving was not audited
  to the same depth as the frozen rows above. Pathogen prompts do not by themselves
  establish binding a chosen molecular target.
- [AMPGen, Jin et al. 2025](https://www.nature.com/articles/s42003-025-08282-7)
  reports MSA-informed generation and a discriminator/scorer cascade, with code
  and trained models linked through Zenodo. Do not confuse it with other projects
  using the AMPGen name. The archive's exact installed route was not inspected.
- **PeptideCLM-2**, [6b9708d4cb05717307d310daaf1c0f88c71ff084](https://github.com/AaronFeller/PeptideCLM-2/tree/6b9708d4cb05717307d310daaf1c0f88c71ff084),
  is relevant for chemical representations and learned features. Its shown public
  inference example extracts embeddings, not completed peptide proposals. MIT
  code, external Hugging Face models and Python 3.11/3.12 full-training guidance
  are visible. Do not count it as a ready generator from that example alone.
- Multi-function predictors, datasets and attribution tools can complement these
  generators. They retain their distinct roles; a predictor's many labels are
  not evidence of a generator that accepts those labels as conditions.

## Proposed inspection order and integration obligations

The following priorities are recommendations, not newly commissioned integrations:

1. Keep HydrAMP's bounded reference/renewal discussion and PLUM in the inventory;
   inspect OmegAMP, ARCADIAMP and AMP-Designer next for complementary AMP routes.
   They offer different priors, controls and operational costs.
2. Review CPP_Design and TACaPe assets/permissions for concrete CPP/ACP coverage.
   If trained artifacts are unavailable or terms unresolved, record that blocker
   rather than silently train a replacement or assume unrestricted use.
3. Retain AMPGAN v3, PepINVENT, PepTune, AMPainter, PepGenWL and MMCD for explicitly
   scoped chemistry/search/learning/structural work. Their presence in a catalog
   adds no requirement to implement them all before useful peptide design.

For each selected future route, identify the exact source/checkpoint/configuration,
native conditioning, internal selection and observable cost; verify supported
views and per-occurrence output/failure accounting; qualify installed execution
and a bounded direct-native comparison. Record code, asset and data terms
separately. Keep absent engines and saved readers usable according to their
existing contracts. Macrel scores and the two accepted selectors stay unchanged
until a scientific decision explicitly commissions something else.

PeptideMT owns peptide-specific orchestration and interpretation. MolSysMT owns
molecular systems and general format operations; broader chemical engines do not
authorize local copies of those operations. Optional-provider availability,
diagnostics and attribution retain DepDigest/SMonitor/Ackredit ownership. A future
integration may use an isolated worker when justified; the suite's ordinary
development remains Python 3.14. README compatibility and visible files are not
installed qualification or a claim that every resource supports Python 3.14.

No fork, new trained model, dependency addition, broader chemistry, feedback run,
target-conditioned execution, GPU use or publication is authorized by this search.
