# PeptideMT V0.1: useful capabilities and verifiable contracts

Status: **comparison preserved; B is now accepted conceptually under D33**,
2026-10-26, with A as its first internal increment and C deferred. The
[bounded scope proposal](v0_1_scope.md) carries the subsequent feasibility review,
minimum useful increment 2, priority feedback extension and target milestone.
P04 is conceptually closed under D32, including C1–C5. D35 subsequently accepts
increment 1's scientific contract, provisional scope and M1–M8; see the
[commissioning brief](increment_1_work_order.md). Later capability contracts,
exact engines, broader chemistry and interfaces remain pending. D36 now authorizes
only the bounded W0–W4 assignment, starting with central admission #146; the
original comparison below is retained as reasoning, not broader work authority.

Navigation: [index](README.md) · [decisions](decisions.md)
· [accepted P04 synthesis](uncertainty_diversity_budget.md)
· [engine audit](protein_peptide_design_engines.md) · [ecosystem audit](integration_audit.md)
· [working agreement](design_methodology.md).

## 1. What the first useful version should demonstrate

The requested product is a small scientific tool that actually generates or
redesigns peptides, uses some learned functional-family knowledge and produces
attributable evaluations and reproducible selections. Imported proposals remain
useful, but a generic framework demonstrated only with fake evaluators is insufficient.

Joint target/family-directed design remains the central scientific objective.
V0.1 need not solve every part: target-conditioned proposals, evaluated target
recognition and family-guided exploration must have distinct, truthful claims.
Predicted compatibility is not measured activity; target conditioning does not
by itself evaluate binding. No clinical/experimental success is a software acceptance
criterion unless investigators explicitly choose a corresponding validated task.

## 2. Alternatives compared against the requested criteria

These are qualitative engineering/scientific judgments, not measured development
times, GPU benchmarks or probability estimates.

| Criterion | A: external proposals + evaluation/selection | B: real sequence generation/redesign + functional evaluation | C: structural peptide/binder generator + functional evaluation |
| --- | --- | --- | --- |
| Scientific utility | Reproducible screening and comparison of supplied peptide sets. | New sequence proposals or analogues evaluated against stated functions; a small complete design workflow. | Target-associated sequence/structure proposals with molecular evaluation and family assessment. |
| Original generative hypothesis | Establishes the assessment baseline, not generation or guided exploration. | Directly tests generation plus family knowledge. Postselection is weaker than feedback that changes later proposals. | Strong target/structure route; adding a family filter still does not demonstrate in-sampler guidance. |
| Molecular target | Accept externally obtained target evidence with its meaning; do not invent recognition. | Possible target-sequence-conditioned generation. A separate qualified evaluator is needed to assess recognition quantitatively. | Native target geometry/site conditioning where supported; complex confidence is not automatically affinity or selectivity. |
| Existing tools/maturity | Real compatible predictors exist; scientific domain and output semantics still need qualification. | Published sequence generators and pretrained assets exist, with important environment/access limitations below. | Existing pinned audit establishes real generation paths and reported experiments; local execution remains unqualified. |
| Installation/resources | Smallest route; optional CPU predictor may suffice for a chosen task. | One generator environment plus evaluator environment; cost depends on model, target length and scoring calls. | Larger GPU/runtime/preparation burden; multiple structural oracles and optional licensed tools can dominate. |
| Code/weights/data terms | Need an actual permitted predictor and permitted fixtures; publication is not permission. | Review each generator/checkpoint/evaluator separately; several attractive resources have unresolved terms or legacy stacks. | Code, weights, structural auxiliaries and optional services each need their own terms. |
| MolSysSuite integration | Reuse support libraries and qualified molecular views without constructing every sequence. | Same foundation plus an optional generator adapter and actual proposal provenance. | Additional chain/residue/atom/state correspondences and molecular conversions; experimental APIs need bounded contracts. |
| Tests and acceptance | Most controllable fixed-evidence fixtures, failures and policy comparisons; still requires a real evaluator run. | Adds real generation and stochastic/reproducibility checks, with an informative end-to-end case. | Adds complex/native artifact consistency, coordinate mapping, target identity and structural-environment checks. |
| Interpretation risks | Calling a score biological compliance; losing rejected/missing results. | Calling target-conditioned output a verified binder or reward improvement independent validation. | Treating plausible poses as binding, family scores as full-chemistry activity, or terminal checks as internal guarantees. |
| Implementation/maintenance | Lowest relative scope; insufficient as the whole requested generative version. | Moderate if bounded to one route and small family subset; legacy dependencies can change that assessment. | Highest relative scope and external-runtime coupling for a first version. |
| Growth | Reusable foundation for B/C if it preserves molecular/evaluation attribution. | Can add structural generators through the accepted capability boundaries; avoid sequence-only assumptions in all providers. | Reusable if molecular and design ownership stay separate; starting here risks making one engine's workflow the core. |

## 3. Bounded resource evidence and feasibility

Published evidence, inspected code, expected compatibility and our own execution
are separate. Reuse the existing immutable audit rather than surveying every
model again. The targeted additions below identify candidates, not selected dependencies.

### Sequence generators

**PepMLM** — source remains at
[`3169c492`](https://github.com/programmablebio/pepmlm/tree/3169c4920f8c383948e0a5d3a7c8f87e5e7d2436).
The inspected [generation routine](https://github.com/programmablebio/pepmlm/blob/3169c4920f8c383948e0a5d3a7c8f87e5e7d2436/scripts/generation.py)
uses a target sequence, a masked peptide region and sampling; it also reports
pseudo-perplexity. It relies on model/tokenizer globals rather than a complete
installed provider contract. No native arbitrary family-reward loop or seed-based
analogue interface is established. Token vocabulary/output validation needs qualification.

The [2025 paper, 2026 journal issue](https://www.nature.com/articles/s41587-025-02761-2)
reports binding and degradation experiments on its tested examples. These are
authors' results, not validation for our targets or free-peptide CPP delivery.
Pseudo-perplexity is not affinity, selectivity or a calibrated binding probability.
The published training envelope and actual tokenizer/context limits must be checked
separately before choosing V0.1 target/peptide length limits.

**Access/terms remain consequential:** no top-level license file was found in the
inspected Git tree. The [official raw model card](https://huggingface.co/ChatterjeeLab/PepMLM-650M/raw/main/README.md),
read on 2026-10-26, declares MIT metadata but also contains additional access fields
asking for noncommercial use, authorship, data-sharing and patent commitments.
The legacy model identifier redirects to ChatterjeeLab. No access agreement was
accepted and no weights downloaded; public metadata does not settle the applicable
permission. Clarify the exact artifact/use terms before adopting it, rather than
treating this as an unrestricted mandatory backend.

**HydrAMP** — original source
[`6590d2f4`](https://github.com/szczurek-lab/hydramp/tree/6590d2f4c2963f25d30669052a4c4a857e0e7279)
is unchanged from the audit. The inspected
[HydrAMPGenerator](https://github.com/szczurek-lab/hydramp/blob/6590d2f4c2963f25d30669052a4c4a857e0e7279/amp/inference/inference.py)
has unconstrained and analogue generation with native AMP/MIC scoring/filtering.
This is real learned family-conditioned generation, not protein-target conditioning
or arbitrary CPP/ACP control. Defaults embed selection choices that must remain visible.
The [paper](https://www.nature.com/articles/s41467-023-36994-z) reports activity
experiments in its tested domain; they do not validate every generated sequence.

The original [setup](https://github.com/szczurek-lab/hydramp/blob/6590d2f4c2963f25d30669052a4c4a857e0e7279/setup.py)
pins TensorFlow 2.2/Keras 2.3 and related legacy packages. The official
[starter-kit snapshot `7804df86`](https://github.com/szczurek-lab/hydramp-starter-kit/tree/7804df862872ccc6d09fe01c41bafbca194cfa31)
contains checkpoint/PCA files and exposes a complete-output generation entry point,
but its [manifest](https://github.com/szczurek-lab/hydramp-starter-kit/blob/7804df862872ccc6d09fe01c41bafbca194cfa31/pyproject.toml)
still requires Python 3.8. Its fixed-seed reproducibility is provider-reported,
not independently reproduced. The workflow includes task-specific filters/ranking;
do not import its library, novelty or synthesizability rules as PeptideMT defaults.

Original and starter code declare MIT; the starter explicitly bundles weights and
their provenance. Its [README](https://github.com/szczurek-lab/hydramp-starter-kit/blob/7804df862872ccc6d09fe01c41bafbca194cfa31/README.md)
also calls for checking source-data terms. This improves asset traceability but
does not establish a locally qualified environment or every redistribution right.
The [archival data release](https://zenodo.org/records/7420278) lists model archives;
no archive or binary checkpoint was downloaded here.

### Functional evaluators

**Macrel** — newly inspected at
[`8c1f7321`](https://github.com/BigDataBiology/macrel/tree/8c1f7321618ccde2a28b960d32525620d2c737e3).
Its [prediction path](https://github.com/BigDataBiology/macrel/blob/8c1f7321618ccde2a28b960d32525620d2c737e3/macrel/AMP_predict.py)
loads bundled AMP/hemolysis ONNX assets on CPU. It returns continuous model scores
and labels, but removes predicted non-AMP rows by default; preserve all outcomes.
Its [CLI export](https://github.com/BigDataBiology/macrel/blob/8c1f7321618ccde2a28b960d32525620d2c737e3/macrel/main.py)
rounds numeric output to three decimals, so comparisons must use retained precision
or explicitly qualified rounded values. These are adapter obligations, not executed fixes.

[Feature extraction](https://github.com/BigDataBiology/macrel/blob/8c1f7321618ccde2a28b960d32525620d2c737e3/macrel/AMP_features.py)
skips empty/noncanonical inputs; an adapter must account for them rather than
silently lose subjects. Upstream [tests](https://github.com/BigDataBiology/macrel/blob/8c1f7321618ccde2a28b960d32525620d2c737e3/macrel/tests/test_predict.py)
cover retained negatives and very short inputs, not our successful execution or
scientific applicability at every length. The code warns about longer sequences;
operational acceptance and validated length scope remain distinct.

[Metadata](https://github.com/BigDataBiology/macrel/blob/8c1f7321618ccde2a28b960d32525620d2c737e3/pyproject.toml)
requires Python >=3.10 and declares MIT with packaged model files. Dependencies
include ONNX Runtime, pandas and pyrodigal; the full genome-mining stack is not
needed for the proposed peptide-only scientific task, but packaging still needs
qualification. The [paper](https://doi.org/10.7717/peerj.10555) supports AMP/hemolysis
classification in its evaluated domain. It is not CPP/ACP or target recognition;
scores are not MICs, hemolysis percentages or proven safety. Composition categories
in its AMP_family output must not become new bioactivity families automatically.

**PrMFTP** — reused at
[`42488d2e`](https://github.com/xialab-ahu/PrMFTP/tree/42488d2e1a2cc2855375717fa926d21c8887783e),
unchanged in the targeted refresh. The [earlier inspected interface](literature.md#prmftp--21-label-source-level-integration-observations)
has 21 outputs, legacy TensorFlow/Keras, ten checkpoints and thresholded labels.
Continuous-score access needs explicit adaptation; model/code/data permission
is not established by the inspected tree. Attractive broader coverage does not
make it the mandatory first evaluator or turn its labels into our family ontology.

### Structural alternatives and local execution status

Reuse [the pinned structural audit](protein_peptide_design_engines.md), not a new
claim about latest revisions: RFD4-Proteina `aaccdd2a` (native search, specialized
Python 3.12/Torch/CUDA stack, BSD-3-Clause bundle); DiffPepBuilder `c19eb4f0`
(target structure/sequence co-design, MIT project with separate OpenFold/PyRosetta/
asset concerns); BoltzGen `a07fea11` (peptide protocols, MIT code/documented released
weights, GPU and optional structural components). None supplies qualified joint
CPP/ACP/target design merely by adding a family label. Each needs an actual
access-route, checkpoint, environment and chemical-domain contract. Optional
assets retain their own terms. No Chaperone dependency or dual adapter route is required.

**Execution checked in the preceding alternatives review:** a read-only check of the selected
shell interpreter found Python 3.12.8 on Linux x86_64; torch, TensorFlow,
Transformers, MolSysMT and Macrel were not discoverable there. The NVIDIA inventory
command failed to communicate with the driver. This does not prove absence of
physical GPUs or packages in other environments. This is not a laboratory hardware
or environment audit. It does not qualify CPU or GPU model execution.
No generator/evaluator was installed, invoked or benchmarked;
no weights were downloaded. Local driver availability and an external/isolated
worker are alternative deployment questions, not settled infrastructure choices.

## 4. Common minimum scientific contract, whichever alternative is chosen

These are proposed obligations to approve with the selected capabilities, not
Python signatures or a universal schema:

- Accept an identified scientific problem with desired functions and optional
  target context, separate from evaluator bindings, thresholds and search policy.
  Start with a small qualified function/resource mapping, not a 21-family obligation.
- Retain input/output subjects, source identifiers, actual evaluated views,
  transformations, model/checkpoint/settings and relevant context. Preserve
  convergent proposal paths and comparisons to the original evidence snapshot.
- Choose a bounded supported input alphabet, lengths and chemistry for each route.
  A sensible sequence-first proposal is complete canonical-residue strings, with
  explicit unresolved chemistry. Letters alone do not establish termini, stereo,
  protonation, links or a fully specified molecule. No implicit stripping of D
  residues, modifications or cyclization to obtain a favorable model input.
- Define scope-specific checks and action policies. Unsupported/incomplete inputs,
  absent/failed evaluations and disagreement retain their meanings. No fabricated
  score, automatic favorable-model choice or hidden provider substitution.
- Preserve raw outputs and qualified derived objectives. Keep eligibility,
  selection and solution-acceptance meanings distinct. An empty batch is valid;
  passing a score threshold does not establish the biological requirement.
- Record actual calls, failures, reuse and available cost/trace information. A seed
  and configuration support reproducibility; bit-identical stochastic output needs
  qualified execution evidence, not a universal promise.

For the initial sequence route, incomplete or modified proposals may remain
attributable records while a selected evaluator declines them. P07 does not require
every V0.1 method to evaluate all partial proposals, nor all generators to emit
complete sequences. Exact limits must be selected from the chosen routes' supported
intersection; this comparison does not invent a global peptide length bound.

## 5. Alternative-specific minimum capabilities and acceptance

### A. External proposals, real evaluation and purpose-specific selection

| Contract question | Proposed minimum |
| --- | --- |
| Scientific inputs | Supplied sequence/proposal set, desired small function subset, explicit evaluator binding and selection purpose; optional attributed external target evidence. |
| Output proposals/chemistry | Preserve supplied proposals and actual sequence views. No new molecules or automatic chemical completion is claimed. Unsupported chemistry is reported, not normalized away. |
| Evaluations | At least one real permitted functional evaluator, native outputs and applicability; optional separately qualified descriptors. No pretend target affinity if only family scores exist. |
| Checks/policies | Declared alphabet/length/input checks; one simple documented ranking or gate policy. A second fixed-evidence policy can test independence of evidence and selection without a general policy engine. |
| Missing/conflicting results | Preserve missingness/failure/input mismatch and every opposing assessment. The action's chosen rule can defer, select exploratorily or return empty; no default universal rule. |
| Satisfactory implementation | On an approved small fixture, a real evaluator reproduces its native outputs within declared precision; every input is accounted for. Policy changes leave native evidence unchanged. Unsupported, missing and contradictory cases yield the agreed outcomes. |

A is useful screening functionality and a natural first implementation slice,
but **A alone does not satisfy the requested generative V0.1 demonstration**.

### B. One real sequence proposal route plus functional knowledge

| Contract question | Proposed minimum |
| --- | --- |
| Scientific inputs | De novo request and/or seeds according to one chosen generator, small function subset, length/allowed-edit scope and budget; target sequence only if that route supports it. Do not require both de novo and redesign initially. |
| Output proposals/chemistry | Actual model-produced sequence proposals with source/seed/target relationships; bounded canonical input/output subset and explicit chemistry limits. Invalid outputs are recorded, not silently repaired. |
| Evaluations | One compatible real functional evaluator or qualified native functional outputs; generator-internal scores remain distinct from assessment. A separate resource can be useful without assumed data independence. |
| Constraints/selection | Input/output checks, declared native filters and one bounded selection policy. Optional small feedback loop only with actual regeneration/analogue/edit operations. No arbitrary external-gradient capability is assumed. |
| Target meaning | PepMLM-like target conditioning can produce target-associated proposals. Without another qualified recognition evaluator, binding remains unassessed. Pseudo-perplexity is not a surrogate Kd by renaming; X/Y selectivity cannot be fabricated. |
| Missing/conflicting results | Account for all observable generation/evaluation outcomes; retain source-specific conflicts. A required unavailable scorer blocks that operation rather than triggering a silent replacement or random score. |
| Satisfactory implementation | A pinned real generator and functional resource execute a small approved end-to-end task, yielding supported proposals, attributable scores and a reproducible selection report. Controlled failure/unsupported/empty cases work. A framework demonstrated solely with mocks does not qualify. |

Two bounded B scopes should not be conflated:

- **B minimum:** actual generation plus family-based assessment/selection. Scientifically
  useful and an honest reference for the original hypothesis; postselection alone
  does not show restriction of exploration during generation.
- **B feedback extension:** functional evidence changes later proposal allocation,
  analogue parents or supported edits, with an explicit budget. HydrAMP's analogue
  path is a relevant operation; PepMLM's inspected complete-output path does not
  establish it. Compare against generate-then-select at matched declared cost.
  Reward gains alone do not prove improved real activity, and no positive gain
  is guaranteed for every random seed.

For a target-free family-first route, target recognition can remain explicitly
outside the first capability rather than be silently declared satisfied. For a
target-sequence route, retain that joint target-generation/family-selection value
without claiming jointly learned conditioning or measured binding. If initial
recognition scoring is required, choose and qualify another actual evaluator;
that is additional scope, not a free consequence of B.

An optional narrower route can reuse a PepMLM-like pair pseudo-perplexity routine
as an explicitly hypothesized sequence-compatibility search signal under D18.
It must retain its actual language-model meaning and target inputs. Comparing
such outputs for X and Y does not supply a calibrated selectivity measure; that
scientific requirement remains unestablished without suitable additional evidence.

### C. One structural generator with molecularly attributed assessment

| Contract question | Proposed minimum |
| --- | --- |
| Scientific inputs | Actual supported target construct/structure/chains and design regions/sites, or another native conditioning route; functional request, explicit chemical scope and compute budget. |
| Output proposals/chemistry | Native sequence/structure or backbone-first artifacts with target and residue/atom correspondence, unresolved regions and actual engine chemistry. Do not assume every supported token has full downstream support. |
| Evaluations | Native structural outputs with actual meaning plus qualified sequence-family projections/evaluations. Backbone-only output needs supported explicit completion before a complete-sequence classifier. |
| Constraints/selection | Chosen native preserved regions/chemical checks and postselection policy; internal guarantees only where established. Family-guided native search is a separate capability, not implied by structural generation. |
| Missing/conflicting results | Preserve failed generation/refolding, incomplete chemistry, unsupported projections and conflicts. A good complex confidence cannot replace an absent Y or family assessment. |
| Provenance | Target/state/coordinate frame, generated parts, completion/redesign/conversion history, all native assets and visible internal filters/costs. Editing a sequence does not preserve its previous pose/recognition score automatically. |
| Satisfactory implementation | A small approved native task actually runs in the qualified environment; artifacts map correctly through MolSysMT, functional views retain attribution and selection is traceable. Fixed expected-artifact and controlled failure cases pass. This is computational qualification, not biological validation. |

C need not support all RFD4/DiffPepBuilder/BoltzGen modes, exotic chemistry,
refolding stacks or all structural evaluations. Its difficulty is a larger
minimum executable integration, not a flaw in the conceptual architecture.

## 6. Meaningful tests and what must be decided before coding

For the selected capability set, approve the small scientific domain, actual
provider/checkpoint and usable terms, resource/label mappings, required inputs/
outputs, permissible operations, missing/conflict behavior and bounded acceptance
case. Name what is outside scope. These are concrete V0.1 decisions, not another
general architecture round. Investigators approve meanings and behavior; Codex
can choose internal structures, batching and scheduling under those contracts.

| Case to specify | Scientific behavior it protects |
| --- | --- |
| Approved native positive fixture | Real provider execution and agreement with its own expected outputs, not a mock integration claim. Reference results must be obtained in the selected environment; none exist here yet. |
| Same supplied pool, two selection policies | Raw evaluations/attribution unchanged while choices and rationale can differ. |
| Ambiguous/noncanonical/modified input or unsupported length | No silent loss of subjects or conversion into an apparently supported different molecule; explicit unsupported outcome at the affected operation. |
| Provider drops predicted negatives or exports rounded scores | Every requested subject is accounted for; precision and selection consequences are explicit. Macrel is a concrete source case. |
| Absent Y, opposing CPP outputs and failed scorer | No invented affinity, favorable missing value or silent average; purpose-specific agreed behavior and actual failure/cost reporting. Deterministic fixtures can test these semantics without claiming real model disagreement. |
| Two source paths reach the same proposal/view | Preserve both origins and justify any compute reuse; do not count the reused prediction as new independent evidence. |
| Budget exhausted, unavailable dependency or empty selection | Bounded stop/failure/empty result with the actual reason; no forced batch filling. |
| B feedback, if selected | Show that functional results actually affect subsequent permitted proposals; a final filter alone cannot pass this intervention test. Compare cost/coverage rather than demand improvement for every seed. |
| C mappings, if selected | Target identity, chain/atom correspondences and sequence/structure consistency survive supported conversions; prior scores are not transferred to edited structures automatically. |

Small deterministic semantic tests and optional real-provider integration checks
have different roles. Lightweight CI need not download restricted weights or
pretend to execute GPU jobs. Before claiming a capability implemented, record
successful real-provider execution in its supported deployment and the stated
failure behavior. Scientific utility is demonstrated by actual proposal/evaluation/
selection work; calibration and experimental efficacy require their own evidence.

## 7. Resolve only the V0.1 portions of P02, P03, P05 and P06

| Pending item | What a selected V0.1 scope needs | What can wait |
| --- | --- | --- |
| P02: function/resource bindings | Definitions for the chosen small function subset; native label/order/score meaning, input domain, checkpoint and actual role. One multi-label call stays one resource. | Universal catalog, all 21/47 functions, formal ontology and comprehensive cross-dataset mappings. |
| P03: dependency boundary | Decide the selected host/optional molecular integration and one actual ML access route. Recommend lightweight scientific coordination with isolated legacy/heavy model environments where needed; not yet approved. | Uniform deployment of all engines, generic service platform and support for every chemistry/runtime. |
| P05: strategy | Choose one real proposal path and a stated assessment/selection baseline; decide whether the bounded B feedback capability is in the initial scope or a subsequent increment. | Universal optimizer, all five generative strategy families, custom gradients, retraining and advanced conditioned generation. |
| P06: suite admission/bootstrap | Before Python implementation, agree central registration/admission and official starter, host support, applicable support-library/policy adoption and dependency licensing. This documentation repository is not already admitted. | Public release packaging details and broad model distributions not needed for the selected first implementation; admission itself is not waived. No issues/bootstrap changes now. |

The P06 row preserves the earlier design-stage admission restriction. Completed
W0 and normal owning-issue reporting now follow
[the governance map](governance.md); no new scientific scope follows.

P04's semantic organization is **closed**, not reopened to choose each scalar
weight or metric. P10 and future horizons add no V0.1 requirements. Initial
scientific/chemical limits and concrete interfaces remain to approve for the
selected capabilities; specifying those is ordinary progression to implementation.

The [preserved integration audit](integration_audit.md) supplies the concrete reuse
basis: SMonitor signal/emit/diagnostic_scope for diagnostics; ArgDigest FunctionContract/
Domain for argument contracts; DepDigest dep_digest and DeclaredRegistry for
optional availability; PyUnitWizard for actual physical quantities, never score
calibration. Selective integration does not prove a backend runnable.

MolSysMT get/select/convert/extract and qualified build/mutate/physchem operations
own molecular work. In particular its inspected chemical-template path leaves
stereochemistry unspecified; do not call it a fully defined L-peptide builder.
A/B should not force coordinate construction for every sequence prediction.
C requires qualified molecular correspondences, not a second topology engine.
Molecular viewing is optional. DockingMT, PharmacophoreMT and other partially
implemented components cannot be treated as ready affinity oracles. Praxis/Recorda
integration can preserve methodology/observable calls within their audited scope;
no Nextia/agent runtime or general orchestration layer is a V0.1 prerequisite.

## 8. Original recommendation and subsequent disposition

**Original recommendation, subsequently accepted in direction under D33:** choose B as the target useful V0.1 scope, using A
as its first internal implementation slice rather than its only scientific product.
Qualify one learned sequence generator and one functional resource, a small supported
domain, one reproducible selection route and an actual end-to-end case. Consider
the small feedback extension if its real proposal operations fit the resource
budget; otherwise retain generation-plus-selection as the honest first baseline.
Keep C as a subsequent selectable capability rather than a mandatory foundation.

Do not make PepMLM mandatory while its applicable terms remain unresolved. HydrAMP
has a direct family/analogue rationale and inspectable assets, but its legacy
runtime still needs qualification. Macrel is a concrete narrower CPU evaluator
candidate; it cannot stand in for CPP or ACP. PrMFTP's 21 labels are not required
to demonstrate useful family knowledge. No combination here is selected or locally
qualified; if a candidate fails qualification, return a concrete alternative rather
than silently substitute it or announce that A alone fulfilled B.

**Disposition:** the investigators approved B with A as the first internal
increment, increment 2 as the minimum useful product, genuine feedback as a
priority conditional extension and target-directed capability as a priority after
the functional core. Initial target-free work is allowed; recognition and advanced
structural generation are not initial requirements. No model or chemistry was
selected. The [concrete scope proposal](v0_1_scope.md) now defines the bounded
resource/domain/contract decisions still needed before development. Native runtime
qualification remains unperformed; no new broad conceptual review is required.
