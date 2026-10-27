# Protein and peptide design engines: evidence and composition

Status: **source/literature review and conceptually resolved P09**, 2026-10-26.
D21–D24 accept responsibility owners, compatibility
dimensions and origin-independent, domain-aware optional individual/composite
access. D25–D26 adopt alternative B, all seven principles and context-sensitive
semantic obligations. Concrete contracts remain deferred. No engine is selected
or executed.

Navigation: [index](README.md) · [capabilities](capabilities_and_composition.md)
· [strategies](generative_strategies.md) · [families](functional_families.md)
· [ecosystem audit](integration_audit.md) · [decisions](decisions.md).

## 1. What this review establishes

A model's original description as a protein or peptide generator is a poor
admission boundary. Actual operation, chemistry, conditioning, exposed access
and evidence matter. Accepting a 15-residue input is different from designing
useful 15-residue binders. Conversely, general protein engines already provide
relevant short-peptide results. This motivates the domain-aware principle now
accepted under D23, not a blanket endorsement of every engine.

The matrix uses six separate evidence questions, not an ordinal confidence scale:

- **D — documented:** the provider describes the operation or accepted input.
- **C — code inspected:** an identified implementation path supports the bounded
  observation. Presence alone does not prove successful execution.
- **R — execution/reproduction:** identify who ran which revision, environment and
  task. Author-reported execution is different from independent reproduction.
- **B — benchmark/experiment:** record task, chemistry, endpoint and version.
  Structural confidence and experimental function are different endpoints.
- **A — adaptation:** an integration possibility requiring work/qualification.
- **U — unknown/unsupported:** distinguish uninspected support from an observed
  missing public operation. Neither means universal impossibility.

**Our R status is absent for every engine:** no installation, model execution or
benchmark reproduction was performed. Source retrieval and paper inspection are
the only work performed here. Reported experiments below belong to their authors;
the GPCR study is an external computational assessment with modified protocols.
No PeptideMT adapter exists. This is a targeted survey, not an exhaustive census.

### Immutable implementation snapshots

These references identify inspected source, not necessarily the code used in each
paper. Model weights and service versions need their own identity.

| Resource | Inspected revision / source entry |
| --- | --- |
| Chaperone | [`a86eb8355c6e362590238c381de13dcba9bef0e0`](https://github.com/RosettaCommons/chaperone/tree/a86eb8355c6e362590238c381de13dcba9bef0e0) |
| RFD4-Proteina | [`aaccdd2ad0720c180468df5f9cf037a713d403e5`](https://github.com/RosettaCommons/RFD4-Proteina/tree/aaccdd2ad0720c180468df5f9cf037a713d403e5) |
| RFD3 and RoseTTAFold3 (RF3), in Foundry | [`d078b24d6d0e6f8607e9a0311128f4a897f83953`](https://github.com/RosettaCommons/foundry/tree/d078b24d6d0e6f8607e9a0311128f4a897f83953) |
| BoltzGen | [`a07fea1153111ef453aaea7a15697ee05de9291f`](https://github.com/HannesStark/boltzgen/tree/a07fea1153111ef453aaea7a15697ee05de9291f) |
| BindCraft | [`7713aa0d0d351e4117a8befeb8541f3a8ebd3368`](https://github.com/martinpacesa/BindCraft/tree/7713aa0d0d351e4117a8befeb8541f3a8ebd3368) |
| RFpeptides, in RFdiffusion | [`86507b6538f51fce57b5a72477165f03999ed7ae`](https://github.com/RosettaCommons/RFdiffusion/tree/86507b6538f51fce57b5a72477165f03999ed7ae) |
| PepMLM / DiffPepBuilder / PepTune / HydrAMP | Respective pinned revisions and entry points in the [earlier source matrix](capabilities_and_composition.md#5-matrix-from-public-implementations); reused rather than re-audited. |
| ProteinMPNN | [`8907e6671bfbfc92303b5f79c4b5e6ce47cdef57`](https://github.com/dauparas/ProteinMPNN/tree/8907e6671bfbfc92303b5f79c4b5e6ce47cdef57) |
| LigandMPNN / related MPNN variants | [`26ec57ac976ade5379920dbd43c7f97a91cf82de`](https://github.com/dauparas/LigandMPNN/tree/26ec57ac976ade5379920dbd43c7f97a91cf82de) |
| AlphaFold3 | [`5e23d45bff3a4c1993516ead2ec848cb42d64c1a`](https://github.com/google-deepmind/alphafold3/tree/5e23d45bff3a4c1993516ead2ec848cb42d64c1a) |
| Boltz-2 | [`b1ebfc46ecf57f5414e0d1a6f9027bbb122c53bc`](https://github.com/jwohlwend/boltz/tree/b1ebfc46ecf57f5414e0d1a6f9027bbb122c53bc) |

## 2. Generative-engine matrix

Length examples/defaults are not universal limits. Designed-chain length and
total target-plus-design tokens are different quantities. A chemistry accepted
by a parser is not necessarily generated, preserved by later sequence design,
or empirically qualified. Every row retains the R limitation above.
The combined D/C column identifies source observations with **C**; broader
provider-described scope remains **D**, not a claim of complete code-path testing.

| Engine and role | D / C: length, chemistry and conditioning | B / reported execution evidence | A / U: access and remaining limits |
| --- | --- | --- | --- |
| **RFD4-Proteina:** joint sequence/all-atom generation and native search | Configurable design regions; target/motif/atom/sequence conditioning, partial diffusion and inverse folding. Expanded residue vocabulary and cyclic test fixtures; no inspected universal short-peptide minimum. | New preprint reports multiple protein-design experiments; no dedicated short-peptide binder/family benchmark established in this review. | C: native branch/continue, rollout scoring, checkpoint rewards; optional differentiable guidance is narrower. A: family metrics and domain qualification. U: current checkpoint's short/cyclic/modified-peptide reliability. NIM's 1024-token limit is service-specific. |
| **RFdiffusion3:** all-atom design, with sequence readout | C: [input parser](https://github.com/RosettaCommons/foundry/blob/d078b24d6d0e6f8607e9a0311128f4a897f83953/models/rfd3/src/rfd3/inference/input_parsing.py) accepts contigs/lengths, fixed atom/sequence information, partial diffusion and cyclic-chain controls. Target context/hotspots; not necessarily backbone-only. | Short-peptide computational assessment in the GPCR study below. | A: external family selection/editing or sampler-specific changes. U: generic external reward callback or reusable resumable-state adapter was not verified. Native classifier-free guidance is not arbitrary classifier guidance. |
| **BoltzGen:** joint design model plus configurable pipeline | C: [CLI/protocols](https://github.com/HannesStark/boltzgen/blob/a07fea1153111ef453aaea7a15697ee05de9291f/src/boltzgen/cli/boltzgen.py), design-language lengths, target/site/structural conditions, covalent links and peptide protocol. Linear/disulfide peptide examples; other bond inputs require task-specific checks. | Authors report peptide binding and GyrA-related functional experiments; see section 6. External GPCR assessment uses the design stage. | C: complete pipeline or selected stages; inverse-fold/refold/filter policies vary by protocol. A: external family feedback. U: universal in-denoiser reward/state interface not verified; accepted bonds do not certify every modified peptide. |
| **BindCraft:** composite AF2-based sequence optimization, redesign and filtering | C: [binder optimization](https://github.com/martinpacesa/BindCraft/blob/7713aa0d0d351e4117a8befeb8541f3a8ebd3368/functions/colabdesign_utils.py), target structure, length settings, loss terms and peptide presets. Mainly standard protein sequence chemistry. | Protein-binder experiments in its paper; short-peptide computational evidence from modified GPCR protocols. | Native optimization gradients are with respect to its AF2-design variables/losses. A: family-loss or outer-search integration. U: no arbitrary external predictor gradient, cyclic chemistry or checkpoint-independent state contract follows from this. |
| **RFpeptides:** cyclic backbone generation followed by sequence design | C: [cyclic residue handling](https://github.com/RosettaCommons/RFdiffusion/blob/86507b6538f51fce57b5a72477165f03999ed7ae/rfdiffusion/inference/model_runners.py) and documented RFpeptides workflow; target-conditioned macrocycles, with separate ProteinMPNN/relax/refold tools. | [Published macrocyclic-binder experiments](https://www.nature.com/articles/s41589-025-01929-w), including short rings around 12–18 residues, within tested tasks. | A: family-guided sequence selection/redesign; observe ring and interface preservation. U: no universal D-residue/PTM library or external trajectory-reward interface established. Not joint sequence/backbone generation merely because a full workflow outputs both. |
| **PepMLM:** target-sequence-conditioned sequence generator | C: requested length, masked binder segment and sampled canonical sequence; example/default length 15 is not a qualified global range. | Target-dependent binder evidence summarized in the [literature review](literature.md#pepmlm--target-sequence-conditioned-linear-binder-proposals). | Public entry returns sequence/pseudo-perplexity, not states/gradients; A: external evaluation or adapted decoding. U: structural, cyclic and arbitrary modified-chemistry support. |
| **DiffPepBuilder:** target-structure-conditioned co-design | C: receptor-fixed masks, generated sequence/structure, disulfide processing; inference defaults 8–30 are settings, not all-domain bounds. | Linear/disulfide peptide results in the [primary review](literature.md#diffpepbuilder--structural-target-conditioned-co-design). | Exported trajectories are not a continuation contract. A: external family evaluation or sampler changes. U: general chemical alphabet, arbitrary peptide infill and native family-reward callbacks. |
| **PepTune:** peptide-SMILES diffusion plus multiobjective tree search | C: chemically expressive tokenization and completed rollouts; binding scorers can receive protein sequence. Token count does not translate into one residue limit. | Published computational multiobjective results; [reviewed interpretation](literature.md#peptune--inference-time-multiobjective-tree-guidance). | C: rewards already influence tree allocation. A: new family scorers and qualified projections. U: model-supported chemistry beyond training/tokenization. Scorer-conditioned search is different from a target-conditioned denoiser. |
| **HydrAMP:** family-conditioned sequence/analogue generator with selection | C: AMP/activity conditions, seed analogues and latent perturbations; 25-position native sequence arrays. No arbitrary protein target condition observed. | AMP-focused evidence in its [paper and code review](literature.md#hydramp--a-family-enriched-proposal-model). | A: external target assessment, composite optimization. U: native target binding, exact edit masks, cyclic/modification semantics or continuation. Disabling one filter does not remove internal per-latent selection. |

### Auxiliary models: prediction is not generation

The BindCraft experimental reference above is
[Pačesa et al., Nature (2025)](https://www.nature.com/articles/s41586-025-09429-6);
its protein-binder results do not qualify every short-peptide preset.

| Resource | D / C: useful operation and domain | B / R scope and A / U limitations |
| --- | --- | --- |
| **ProteinMPNN** | Sequence design conditioned on a supplied backbone; fixed/tied residues, exclusions/biases, sampling probabilities. Canonical protein alphabet. | Used in published peptide workflows; no execution here. Does not generate a backbone or assess bioactivity. A: family-aware outer sequence search; bias is not a functional guarantee. |
| **LigandMPNN, soluble/membrane variants** | [Run interface](https://github.com/dauparas/LigandMPNN/blob/26ec57ac976ade5379920dbd43c7f97a91cf82de/run.py): environment-aware sequence design and optional side-chain packing; variants have different context/training. | Structural and sequence-design evidence is task-specific. No arbitrary modified-residue generation or peptide-family condition inferred; exact ring/bond preservation needs checking across the chosen workflow. |
| **AlphaFold3** | Complex structure prediction from sequence/chemical input; [input format](https://github.com/google-deepmind/alphafold3/blob/5e23d45bff3a4c1993516ead2ec848cb42d64c1a/docs/input.md) permits modifications, CCD content and explicit bonds. | Broad structural evidence does not certify every short peptide or an affinity/activity estimator. A: supported candidate-complex assessment. U: de novo peptide generation or reliable functional probability from confidence metrics. |
| **Boltz-2** | [Prediction interface](https://github.com/jwohlwend/boltz/blob/b1ebfc46ecf57f5414e0d1a6f9027bbb122c53bc/docs/prediction.md): complex structures including cyclic/modified inputs; a separate affinity head. | GPCR study below probes structure predictions. **Affinity estimation is documented for small-molecule ligands with protein targets, not protein-chain peptide affinity.** A peptide complex's predicted structure does not qualify that head for peptides. |
| **RoseTTAFold3 / RF3** | All-atom structure prediction in [Foundry](https://github.com/RosettaCommons/foundry/tree/d078b24d6d0e6f8607e9a0311128f4a897f83953); molecular/CIF inputs, explicit bond/cyclic and template contexts. | Computational peptide-complex assessment in the GPCR study. Not RFdiffusion3, and not a peptide generator by itself. Input chemistry and confidence do not establish binding/activity. |
| **PrMFTP (21 functions)** | One sequence evaluator with 21 outputs and source-specific labels; [inspected interface](capabilities_and_composition.md#5-matrix-from-public-implementations) thresholds outputs and pads to length 50. | Publication and source observations are distinct. A: expose continuous outputs if appropriate, preserve label definitions, input scope and checkpoint identity. U: gradient, partial-state and arbitrary chemical-view support from the public predictor entry. |

OpenFold3 is additionally relevant as an optional RFD4 refolding oracle. It is a
separate dependency/weight choice, not evidence that original AlphaFold3 assets
are freely interchangeable or that a second wrapper is independent validation.

For the auxiliary rows, **D** includes accepted formats and provider-described
scope; bounded **C** observations additionally include AF3's
[input validation/parser](https://github.com/google-deepmind/alphafold3/blob/5e23d45bff3a4c1993516ead2ec848cb42d64c1a/src/alphafold3/common/folding_input.py),
Boltz's [YAML-to-schema path](https://github.com/jwohlwend/boltz/blob/b1ebfc46ecf57f5414e0d1a6f9027bbb122c53bc/src/boltz/data/parse/yaml.py),
and RF3's [inference engine](https://github.com/RosettaCommons/foundry/blob/d078b24d6d0e6f8607e9a0311128f4a897f83953/models/rf3/src/rf3/inference_engines/rf3.py),
which exposes molecular input handling and a cyclic-chain option. These code
observations do not verify every downstream chemistry calculation; documented
support and parser acceptance remain narrower than successful prediction.

### Cost, dependency and licensing boundaries

These are observed planning constraints, not installation qualification or legal
advice. Check the exact code, weight and service terms for the chosen deployment.
No common GPU minimum or dollar cost is established by this review. Short design
length does not make a large receptor complex cheap; repeated oracles, branching,
database preparation and compilation can dominate.

| Resource | Observed runtime/dependency profile | Source/model terms and caveats |
| --- | --- | --- |
| RFD4 native | Python 3.12 only in current metadata, Torch >=2.11,<3; CUDA 12/13 profiles, default setup 13; AtomWorks/cuEquivariance/TMol and optional oracle environments. | BSD-3-Clause code/model bundle; optional assets separate. Detailed route distinctions below. |
| RFD3 / RF3 | Foundry/AtomWorks/Torch GPU environments and separate weights; refolding adds cost. | Foundry's [BSD-3-Clause license](https://github.com/RosettaCommons/foundry/blob/d078b24d6d0e6f8607e9a0311128f4a897f83953/LICENSE.md); third-party tool terms remain separate. |
| BoltzGen | Python >=3.11, Torch >=2.4, CUDA operators and optional sequence/refold components; GPU timing depends on protocol. Optional ESMFold2 is a substantial additional model/runtime. | MIT code and released model weights in the provider documentation; bundled/optional tools need their own terms. |
| BindCraft | CUDA/AF2/ColabDesign, optional MPNN and PyRosetta; repeated optimization/refolding. Larger-complex GPU recommendations are not a small-peptide minimum. | MIT project; PyRosetta and model/data terms separate, including access restrictions. |
| RFpeptides | RFdiffusion GPU generation plus separately installed MPNN, relaxation and cyclic refolding workflow. | RFdiffusion source/weights license plus separate downstream Rosetta/AF assets. |
| PepMLM | PLM weights and Torch; substantially different cost from repeated structural oracles, but not measured here. | No clear top-level license established in inspected tree; checkpoint terms require separate verification. Public availability is not permission. |
| DiffPepBuilder | Torch/OpenFold/PyRosetta-related GPU environment; structural preparation and sampling. | MIT project; dependencies/weights retain their own terms. |
| PepTune | Diffusion/tokenizer, several scoring models and rollout/tree costs. | Apache-2.0 project; each scoring asset and dataset requires its own review. |
| HydrAMP | Older Python 3.8/custom TensorFlow stack; isolate rather than force into the host environment. | MIT project; model/data provenance and applicability still matter. |
| ProteinMPNN / LigandMPNN | Torch, structural preparation; GPU helpful for repeated sampling, exact cost not measured. | MIT source/weights per provider; this does not cover every downstream workflow. |
| AlphaFold3 | GPU inference plus potentially expensive CPU/database preparation and model access. | Current upstream code is Apache-2.0; [weight terms](https://github.com/google-deepmind/alphafold3/blob/5e23d45bff3a4c1993516ead2ec848cb42d64c1a/WEIGHTS_TERMS_OF_USE.md) are separate and restrictive. A bundled older runner can have different code terms. |
| Boltz-2 | Torch/CUDA inference and optional MSA/data preparation; affinity head has its own input scope. | MIT code/weights; no implication of peptide-affinity qualification. |
| PrMFTP | TensorFlow ensemble and encoding/padding; batching/environment adaptation needed. | No clear top-level license established in inspected tree; model/dataset redistribution remains unverified. |
| Chaperone | Host Python >=3.12 with Torch, Polars, Pydantic, AtomWorks and Submitit, plus per-tool containers/weights. | Own code MIT; project metadata/third-party notices also include BSD and CC-BY-NC-SA components. Not every block/runner/weight is MIT. |

**Implication, proposed:** optional external environments/services are preferable
to importing every ML stack into PeptideMT's eventual host. In particular,
RFD4's Python 3.12 metadata does not match the suite's current host-development
interpreter. Process/container separation can address runtime conflict, not
scientific mismatch. No dependency profile or deployment mechanism is adopted.

## 3. Chaperone is an execution framework, not a generator

The [official 19 October announcement](https://rosettacommons.org/2026/10/19/introducing-chaperone-a-unified-framework-for-protein-design-workflows/)
and [documentation](https://rosettacommons.github.io/chaperone/) describe reusable
protein-design workflows. The following observations are source-bounded.

### Blocks and composition

[BlockFunction](https://github.com/RosettaCommons/chaperone/blob/a86eb8355c6e362590238c381de13dcba9bef0e0/src/chaperone/block_config/base.py)
uses Pydantic configuration and preparation/command/output-compilation hooks.
The [lazy block registry](https://github.com/RosettaCommons/chaperone/blob/a86eb8355c6e362590238c381de13dcba9bef0e0/src/blocks/__init__.py)
discovers named block classes. Compiled external-tool blocks coexist with inline
transformations/metrics. The [engine](https://github.com/RosettaCommons/chaperone/blob/a86eb8355c6e362590238c381de13dcba9bef0e0/src/chaperone/engine/base.py)
submits and gathers work, chunks data, returns data handlers and supports
branching/parallel compositions and repeated rounds. Fingerprints/cache reuse
are computational mechanisms, not proofs of scientific equivalence under P07.

The inspected [block tree](https://github.com/RosettaCommons/chaperone/tree/a86eb8355c6e362590238c381de13dcba9bef0e0/src/blocks/networks)
includes RFD3, earlier RFdiffusion routes, MPNN variants, AF3, Boltz-2, RF3,
BoltzGen and BindCraft. Additional named modules include OpenFold3, Chai1,
Protenix, ESMFold2, BindCraft2, RFoptimization and Proteina-Complexa. Registration
does not mean every image/weight is installed or scientifically qualified.
Parameter tiers are not validation grades.

**No named RFD4-Proteina integration was observed** in the inspected block registry
and repository path inventory. The Proteina-Complexa block is a different resource;
its name is not evidence of RFD4 support. A later custom wrapper could add support.

### Inputs, outputs and provenance

The [data schema](https://github.com/RosettaCommons/chaperone/blob/a86eb8355c6e362590238c381de13dcba9bef0e0/src/chaperone/data/schema.py)
has structure references/metadata, JSON metrics, design and parent-design IDs,
and structure/sequence artifact kinds with chain-to-sequence mappings. It is not
exclusively structure-based. The [pipeline manifest](https://github.com/RosettaCommons/chaperone/blob/a86eb8355c6e362590238c381de13dcba9bef0e0/src/chaperone/manifest.py)
records completed steps, named input relationships, Parquet paths and execution
summaries in `pipeline.json`; step data live in output tables. Execution tracking
accounts for attempted/completed jobs and timing/resource summaries where available.

Useful execution lineage is already present. It does **not** establish canonical
chemical identity, P07 realization/assumption semantics, functional-family meaning,
or independent assessment. Nor does a manifest alone guarantee immutable capture
of every model weight, container, script and scientific assumption. An adapter
should reference native artifacts and add only the missing design attribution;
unknown internal telemetry remains unknown. Preserve convergent design paths.

### Runtime and intervention boundary

[JobArgs / RuntimeArgs](https://github.com/RosettaCommons/chaperone/blob/a86eb8355c6e362590238c381de13dcba9bef0e0/src/chaperone/orchestration/job_args.py)
represent resources, site settings and explicit overrides. Local GPU execution
and SLURM/Submitit submission are implemented, with container command construction
in [containers.py](https://github.com/RosettaCommons/chaperone/blob/a86eb8355c6e362590238c381de13dcba9bef0e0/src/chaperone/containers.py).
Docker/Apptainer and optional cloud routes require their own configuration/assets.
Chaperone itself has substantial host dependencies; containers do not remove them.

The workflow can score/filter between blocks and feed another complete operation.
This is real feedback but **not necessarily intervention during a denoising
trajectory**. Internal access is limited to controls exposed by the selected
block and tool. Adding an inline family metric does not automatically turn it
into a generator callback. A composite may honestly expose only final proposals.

### The peptide-binder example has the opposite design direction

The [example and reported GPU check](https://github.com/RosettaCommons/chaperone/blob/a86eb8355c6e362590238c381de13dcba9bef0e0/examples/peptide-binder/README.md)
fix a 15-residue peptide's sequence, allow its conformation to change, and design
a **60–140-residue protein recognizing that peptide**. The pipeline repeats
RFD3/packed LigandMPNN/AF3 assessment. It is not evidence that Chaperone has
qualified short-peptide binders against a protein.

The authors report a bounded H200 execution exercising both rounds after
bypassing quality selection. It retained the fixed sequence and finite outputs
but failed the original quality gates; the normal pipeline would stop earlier.
That is provider-reported execution evidence, not our reproduction or a successful
binder. Its supplied-coordinate policy also differs from a fixed receptor pose.

## 4. RFD4-Proteina: unusually relevant access, still domain-limited evidence

The [public bundle/card](https://huggingface.co/nvidia/RFD4-Proteina),
[NVIDIA introduction](https://developer.nvidia.com/blog/design-proteins-with-rfd4-proteina-using-reward-guided-inference-time-search)
and [preprint](https://rfd4-proteina.org/assets/paper/RFD4-Proteina.pdf)
accompany the public code. The preprint is not yet peer reviewed. Its experiments
on binders recognizing peptides must not be relabeled experiments on generated
short peptides. Supplementary Table S1 includes cyclic-peptide data in flow-model
training and modified-peptide data in autoencoder training: stronger evidence
than a parser alone, still not a dedicated short-peptide performance benchmark.

### Released model versus represented chemistry

The [checkpoint reference](https://github.com/RosettaCommons/RFD4-Proteina/blob/aaccdd2ad0720c180468df5f9cf037a713d403e5/docs/reference/checkpoints.md)
identifies the matched **2026-10-19 flow/autoencoder pair**. Documented released
tasks include unconditional generation, motif/enzyme scaffolding, small-molecule,
protein and DNA binders, folding and inverse folding. The paired autoencoder's
expanded vocabulary is not evidence that the flow model generates all represented
chemistries equally well. Training presets and cyclic/head-tail/disulfide/isopeptide
fixtures demonstrate implemented concerns, not universal chemical qualification.

The inspected [inference configuration](https://github.com/RosettaCommons/RFD4-Proteina/blob/aaccdd2ad0720c180468df5f9cf037a713d403e5/configs/inference.yaml)
pins the native Hub bundle to
[`a06e2509c7033b010fc43614e9fd840303588502`](https://huggingface.co/nvidia/RFD4-Proteina/tree/a06e2509c7033b010fc43614e9fd840303588502).
This is observed configuration, not our downloaded or executed model.

The [conditioning description](https://github.com/RosettaCommons/RFD4-Proteina/blob/aaccdd2ad0720c180468df5f9cf037a713d403e5/docs/concepts/conditioning.md)
distinguishes sequence/probability, coordinate/internal-coordinate, grouped and
interaction conditions. Partial diffusion offers refinement routes. Fixed receptor
information, desired contacts and generalized sequence conditions have native
semantics; neither a hotspot nor a soft sequence preference guarantees an affinity
or functional family. Unsupported chemistry needs explicit rejection, exploratory
qualification or a preserved hypothetical/projection relationship under P07.

The [model card's efficiency table](https://huggingface.co/nvidia/RFD4-Proteina#measured-design-efficiency)
is explicitly for an earlier frozen release, not a remeasurement of the current
pair. It does not establish current peptide-specific speed, success or memory.
Pin the selected model assets separately from the code revision.

### Rewards during search are real, but not every kind of guidance

The inspected [beam search](https://github.com/RosettaCommons/RFD4-Proteina/blob/aaccdd2ad0720c180468df5f9cf037a713d403e5/src/rfproteina/search/beam_search.py)
branches and selects at search checkpoints. It can score completed rollouts;
selected non-final checkpoints can instead use a decoded clean prediction.
These have different meanings/costs. Optional saved states/rollouts and continuation
exist here; a generic PDB trajectory is still not equivalent to sampler state.
The term search checkpoint is unrelated to a model-weight checkpoint.

[RewardModel](https://github.com/RosettaCommons/RFD4-Proteina/blob/aaccdd2ad0720c180468df5f9cf037a713d403e5/src/rfproteina/rewards/reward_model.py)
aggregates named metric outputs using configured weights, normalization/clipping.
Continuation criteria and raw metrics are distinct from the aggregated reward.
A missing weighted output returns negative infinity in this implementation:
**an algorithmic exclusion policy, not evidence of inactivity**. Preserve the
missing/failure cause when translating results. Weighted sums do not supply
PeptideMT's proposed general Pareto/diversity policy automatically.

The [metric interface](https://github.com/RosettaCommons/RFD4-Proteina/blob/aaccdd2ad0720c180468df5f9cf037a713d403e5/src/rfproteina/metrics/metric.py)
and [custom-metric documentation](https://github.com/RosettaCommons/RFD4-Proteina/blob/aaccdd2ad0720c180468df5f9cf037a713d403e5/docs/how-to/advanced/custom-metrics.md)
provide a genuine extension seam. Generated-structure metrics receive atom arrays
and metadata; refolding metrics receive design/refold views. Configurable routing
and metric-output names allow external computations to contribute scalar outputs.
This requires an actual implementation, usable predictor environment and controlled
costs/errors; it is not proof that an arbitrary model can be plugged in unchanged.

Separately, [GuidanceModel](https://github.com/RosettaCommons/RFD4-Proteina/blob/aaccdd2ad0720c180468df5f9cf037a713d403e5/src/rfproteina/guidance/guidance_model.py)
requires differentiable metrics on compatible clean-state variables. The shipped
[ContractCAMetric](https://github.com/RosettaCommons/RFD4-Proteina/blob/aaccdd2ad0720c180468df5f9cf037a713d403e5/src/rfproteina/metrics/contract_ca_metric.py)
is a geometric test/example. This does not supply gradients through categorical
sequence decoding, chemical projection and a TensorFlow sequence classifier.
Black-box rollout reward is the more direct conceptual connection to such a model.

### A 21-function sequence predictor: proposed integration, not implemented

1. Keep the scientific target and requested functional concepts unchanged. Bind
   selected predictor outputs to their source-label meanings under P08; do not
   maximize all 21 labels or treat them as independent biological probabilities.
2. Use the generated peptide chain/region as the evaluation subject, preserving
   correspondence to the full complex. A classifier for peptides must not
   accidentally score the receptor-plus-binder concatenation.
3. Derive the exact supported sequence view. Record termini, links, modifications,
   unknown information and discarded features. A cyclic/modified structure projected
   onto canonical letters is a lossy view, not the same qualified chemical subject.
4. An adapted metric can obtain the predictor's supported outputs, retain the raw
   vector and expose selected operational rewards. PrMFTP's inspected public
   predictor returns thresholded outputs; continuous access needs adaptation and
   checking before any smooth-score claim. No generator retraining is intrinsically
   required for black-box rollout scoring.
5. Preserve target/designability assessments as distinct objectives or checks.
   Favoring a family proxy can damage binding, diversity or chemistry. Reward
   scaling, missing outputs and contradictory predictors are explicit plan choices,
   not changes to the scientific definition of a family.
6. Record which completed rollout or clean estimate was scored, model/version,
   actual input, transformations, calls, cost and selected descendants. A reward
   on a completion does not become a direct evaluation of all partial ancestors.
   Reusing that predictor for final assessment is not independent validation.

This is mechanically plausible through the native metric seam; scientific utility
for simultaneous target/family design remains a research hypothesis. It applies
to qualified outputs from many functional families, not a built-in CPP/AMP/ACP list.

### Native execution versus hosted/self-hosted NIM

[Installation](https://github.com/RosettaCommons/RFD4-Proteina/blob/aaccdd2ad0720c180468df5f9cf037a713d403e5/docs/installation.rst)
documents Linux x86_64, Python 3.12, NVIDIA hardware and CUDA 12/13 profiles.
Reported tested devices include A100 40/80 GB, Hopper and newer architectures;
this is not a universal minimum or measured short-peptide requirement. Optional
BioIR requires CUDA 13. Oracle environments add their own weights, licenses,
memory and preparation. Weight-file size is not peak GPU memory. Branch width,
total complex size, recycles, batching and oracles must enter a later cost profile.

The [output reference](https://github.com/RosettaCommons/RFD4-Proteina/blob/aaccdd2ad0720c180468df5f9cf037a713d403e5/docs/reference/output-format.md)
documents annotated CIF, metric tables and resolved configuration/provenance;
it explicitly does not promise a separate run manifest. Keep native artifacts
and add PeptideMT references rather than inventing an already implemented ledger.

The [NIM API reference](https://docs.api.nvidia.com/nim/reference/ipd-rfd4-proteina)
describes hosted requests, attached input contents, seven task modes and a
1024-token deployment limit. Configurable search metrics are not arbitrary uploaded
Python metrics. Refolding oracles need operator-provided assets. Hosted access
can avoid local inference hardware but introduces service identity, authentication,
quotas and terms; self-hosting retains container/GPU/asset requirements.

Native and NIM metadata are not identical: current public cards report differing
parameter/recycle details. The [Build page](https://build.nvidia.com/ipd/rfd4-proteina)
and API reference also present different license labels. Resolve the actual
deployment/version and applicable terms before claiming parity or permission;
native code/weights are labeled BSD-3-Clause, while service use has additional
terms. Arbitrary custom family rewards and exact state export through hosted NIM
were not verified. A native adapter and a service adapter need separate effective
capability descriptions. The Diffusers packaging route likewise needs its own
exposure check; shared weights do not prove identical search interfaces.

## 5. Direct adapters, Chaperone or both?

These are integration alternatives, not selected implementations. D24 now accepts
conceptual availability of individual/composite routes without requiring both.

| Route | Advantages | Costs and limits |
| --- | --- | --- |
| Direct engine adapters | Closest access to native operations, custom metrics and continuation; explicit per-engine boundaries. | More environment/output adapters and maintenance; avoid duplicating each engine's own pipeline. |
| Optional Chaperone adapter | Reuse existing block composition, containers, submission and result tables; import complete pipelines without rebuilding them. | Adapter sees only exposed block/workflow controls; host dependencies and schema translation; no inherited internal access or scientific qualification. |
| Hybrid | Complete workflows and specialized direct interventions can coexist; choose by required access and environment. | Prevent duplicate scheduling, hidden defaults and double counting; identify actual models across both routes. |

**Accepted conceptual optionality (D24), implementation still open:** direct and
composite routes may coexist without implementing both or making Chaperone
mandatory. It remains reasonable for an initial
bounded adapter to use only one route. Preserve native workflow settings/results;
do not decompose BindCraft, PepTune or a Chaperone pipeline merely to fit a common
set of classes. Conversely, a composite may expose optional internal operations
when actually supported. These are additional promises, not implied by its parts.

The [preserved audit](integration_audit.md) establishes ownership, including
implemented versus experimental boundaries. Proposed integration consequences:

- **PeptideMT:** scientific function/resource associations, proposal/realization
  attribution, search objectives and algorithm policies, scientific comparison
  and native design results. It may invoke an external composed procedure.
- **MolSysMT:** supported selection/conversion/extraction/building and molecular
  correspondence. Its experimental chemical-template factory is not a universal
  cyclic/modified-peptide converter. Preserve native annotated CIF/bonds when
  round-trip fidelity is unqualified; any generic molecular extension belongs
  with that owner rather than a hidden PeptideMT chemistry engine.
- **Praxis:** reusable methodology/catalog/applicability and cross-tool procedure
  execution, within its audited experimental scope. A future Praxis method may
  invoke a PeptideMT campaign or a Chaperone procedure. Avoid another automatic
  scientific planner, competing protocol catalog or mandatory nested executor.
- **Chaperone:** selected external workflow execution/container/submission. Assign
  one scheduling owner at each job boundary; preserve external job/step references.
  A surrounding campaign call must not resubmit the same internal SLURM work.
- **Recorda:** recording observable operations through explicit seams, not a
  replacement for native result semantics or unobserved internal telemetry.
  Reference native manifests/tables; distinguish nested events from extra work.
- **Nextia / Sabueso / MolI agent:** future project context, qualified source
  knowledge and optional reasoning, respectively; none is a required new runtime.

DockingMT, TopoMT, PharmacophoreMT, ElastNetMT and MolSysViewer retain the audited
evaluation/presentation domains; MolSys-AI remains an umbrella rather than a
universal model runner. SMonitor, ArgDigest, DepDigest and PyUnitWizard can serve
diagnostics, arguments, optional dependencies and meaningful physical quantities.
None can infer scientific applicability from a successful import or file parse.
No suite repository was modified or re-audited for this expansion.

## 6. Two particularly relevant empirical checks

**BoltzGen:** the [paper, sections 2.6–2.8](https://hannes-stark.com/assets/boltzgen.pdf)
reports short-peptide binding and target-directed GyrA growth-inhibition work.
The latter uses intracellular peptide expression and specificity-oriented controls.
It is a close precedent for target-linked function, but does not demonstrate
uptake after external dosing, a CPP mechanism or generation guided by an AMP
classifier. Its biological endpoint and delivery context must accompany the claim.
It strengthens the case for admitting general design engines without validating
our proposed functional-guidance architecture.

**GPCR assessment:** [Junker and Schoeder, 2026](https://doi.org/10.1371/journal.pone.0355549)
compares BindCraft, BoltzGen and RFD3 at 8/14/22 residues, alongside complex
prediction assessments. The protocols differ from full/default pipelines. It
reports misplaced peptides with excessive confidence, memorization-like behavior
and weaknesses in generated sequences, with some recovery through MPNN. There
is no prospective experimental validation of new peptides in that benchmark.
Treat its scope as computational and task-specific; reported memorization does
not establish universal leakage or failure. Preserve the predictor, protocol,
target preparation and seed policy when comparing methods.

**Architectural inference:** a model name, a confidence cutoff or even a successful
short-peptide example cannot replace a qualified task/domain description. Avoid
calling reuse of a generation-time oracle independent validation merely because
it is accessed through a different wrapper. Retain contradictory structural and
functional evidence rather than collapsing it into one success flag.

## 7. Consequences for the central hypothesis

The invariant scientific problem can request target recognition plus one or more
functional properties. Plans can exploit very different access without rewriting
those properties as model scores:

| Available operation | Feasible use of learned functional knowledge | Limit on the claim |
| --- | --- | --- |
| Sequence-only complete proposals | Final evaluation, family-enriched sources, outer optimization using compatible edits/restarts. | Filtering does not change the base generator's sampled distribution; feedback changes the outer search only when it affects future proposals/allocation. |
| Backbone first, sequence later | Family-aware sequence sampling/selection or redesign on a retained backbone, with target reassessment. | A sequence classifier cannot directly evaluate an unsequenced backbone; explicit completions/rollouts are needed. Folding/contacts may change. |
| Joint sequence/structure generation | Score finished samples or decoded clean/completed estimates; use native feedback if exposed. | Joint output does not automatically expose states, gradients or functional conditioning. |
| Editing/redesign | Optimize a candidate under declared preserved features, then recheck target and chemistry. | An edit is not a representation conversion; a motif mask is not universal chemical preservation. |
| Intermediate state plus continuation/branching | Allocate compatible trajectories using completion-based rewards or qualified state/value models. | A noisy/partial state's future value is different from measured activity of a molecule. Exported coordinates alone may be insufficient. |
| Native reward-guided search | Adapt valid family outputs to the engine's reward seam; RFD4 and PepTune offer different native mechanisms. | Reward shaping, sampling law and cost differ. No promise of calibrated conditional sampling, Pareto optimality or biological gain. |
| Opaque external complete procedure | Use its final proposals, metadata and declared controls; external selection or authorized reruns. | Internal search is not controlled by PeptideMT merely because the procedure is nested in its plan. |

Training a joint target/function-conditioned model remains an option, not a
prerequisite. Black-box rewards can exploit existing knowledge without gradient
compatibility, but still need useful ranking, appropriate views and adequate
exploration. Requested properties may be mutually difficult, labels correlated
or missing, and optimizers may exploit predictor artifacts. Improving an operational
reward is a result; improving function is a separate hypothesis/evidence question.
Comparisons should preserve the original problem, chemistry envelope and budgets,
including rejected samples, rollouts, oracles and unavailable telemetry.

## 8. Revised P09 recommendation and next approvals

**Alternative B is accepted conceptually (D25):** small capability
descriptions plus explicit compositions, with specialized integrations where
needed. The following domain/access qualifications now have conceptual approval
under D23–D24; D26 accepts sufficient contextual information without adopting
universal fields. Concrete contracts remain open:

1. Describe effective support for a resolved **engine + adapter + model assets +
   deployment/configuration + domain**. These are semantic dependencies, not a
   proposed tuple type or required schema. Native, Chaperone and hosted NIM access
   can expose different capabilities even when model weights are related.
2. Distinguish an individual operation provider, a composite procedure, PeptideMT's
   own search strategy and an external execution/orchestration system. One tool
   can play multiple roles; do not force a mutually exclusive taxonomy.
3. Capability exposure is not transitive: constituents' internal operations are
   not automatically operations of a composite's adapter. Optional internal access
   can coexist with a terminal-output contract; no universal interface is needed.
4. Record evidence **for the task/chemistry/access route**, not an engine-wide
   validated badge. Runtime feasibility, scientific support and technical data
   compatibility remain separate under D22. Exploratory use remains possible.

This avoids the growth of pairwise compatibility logic in alternative A without
the premature solver, ontology and cross-tool planner of alternative C. It does
not justify selecting an engine, class hierarchy or operation-name enumeration.

**Now accepted conceptually (D23–D24):** architecture/origin independence with
domain/capability/evidence awareness; configuration-qualified support; optional
individual/composite providers; and non-transitive internal access. Chaperone is
optional and direct generative intervention remains possible. This does not
approve a dependency, two mandatory adapter implementations, declaration schema,
contracts. Subsequent D25–D26 resolve P09's conceptual organization with explicit
small compositions and sufficient information for actual use; no general planner
is requested.

**Needs more evidence before a concrete commitment:** useful short-peptide domain
for the current RFD4 pair; exact chemistry-preserving conversions; hosted custom-
metric/state access and resolved terms; reproducible environments and cost
profiles; qualification of a specific multi-label predictor; and an informative
comparison design. These do not block a conceptual decision about optionality.

**Conceptual discussion resolved:** capability/domain claims must retain meaning
and justify actual use, including when a service exposes less than its base model.
The [three-case semantic analysis](capabilities_and_composition.md#8-three-tests-of-minimum-capability-meaning)
compares delegated RFD4 guidance, complete Chaperone procedures and exploratory
short-peptide use, distinguishing fundamental/contextual/optional information.
The [bounded horizon review](future_horizons.md#9-bounded-extensibility-review-after-p09-approval)
introduces no engine-selection or implementation requirement. Return next to
[P04](open_questions.md#p04-proposed-discussion-sequence). Keep chemistry
identity, initial support, storage, IDs, concrete interfaces, model selection and
the first demonstrator open. No implementation or issue creation follows from
this review.
