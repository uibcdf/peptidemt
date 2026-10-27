# PeptideMT V0.1: bounded scope and implementation proposal

Status: **B accepted under D33; AMP/hemolysis coverage and Macrel-then-HydrAMP
qualification order accepted under D34; increment-1 scientific design closed
under D35**, updated 2026-10-27. The [increment-1 specification](v0_1_increment_1.md)
now carries accepted contracts/selectors/M1–M8 and provisional chemistry/length
scope. D36 authorizes W0–W4; exact resources, operational qualification and
completed admission remain pending. See the [work order](increment_1_work_order.md):
W0 has started in uibcdf/molsyssuite#146; W1 follows completed W0. H0–H4,
other development issues and package publication are not authorized.
P04/P09 remain conceptually closed. This document narrows their application rather
than designing a universal optimizer or reopening the general architecture.

Navigation: [index](README.md) · [decision D33](decisions.md)
· [A/B/C comparison and resource snapshots](v0_1_alternatives.md)
· [ownership audit](integration_audit.md) · [working agreement](design_methodology.md).

## 1. Accepted direction and its limits

The investigators adopt **B: real sequence generation/redesign with functional
evaluation and reproducible selection**, using A (assessment of external proposals)
as its first internal increment. A alone, or a pipeline demonstrated only with
simulated generators/evaluators, does not satisfy the minimum useful V0.1.

The requested progression is:

1. **Increment 1 — assessment and selection:** supplied proposals, at least one
   real functional evaluator, retained evaluations, incompatible/failed-input
   handling and explicit selection policies.
2. **Increment 2 — real functional generation:** one concrete generation or
   redesign route, a qualified functional resource and the preceding assessment
   layer. This is the **minimum useful V0.1**.
3. **Increment 3 — functional feedback:** evaluations affect subsequent proposals,
   parents, modifications or resource allocation. This is a priority extension;
   its precise inclusion in V0.1 depends on the chosen generator's viability.
   Generating once and filtering afterwards cannot count as this increment.

Joint target/family-directed design remains central. The first functional core
may be target-free; recognition assessment and advanced structural generation
are not mandatory V0.1 capabilities. **Target-directed capability is the next
priority milestone after that core**, not an indefinite optional horizon and
not contingent on completing every feedback extension. C remains a later option.
Exact engine bundles, API and deployment remain unadopted. D34 settles first
coverage/order; D35 accepts increment 1's provisional chemistry/length envelope
and scientific contract without qualifying every chemical realization or length.

## 2. Bounded resource review

Source and metadata were inspected on 2026-10-26. These are feasibility judgments,
not measured performance or successful PeptideMT integrations. No weights were
downloaded, terms accepted, packages installed or scientific models run here.
The earlier [resource review](v0_1_alternatives.md#3-bounded-resource-evidence-and-feasibility)
and immutable ecosystem/structural audits remain part of the evidence.

| Candidate | Actually exposed operation / input and output | Assets, terms and runtime | Proposed disposition and remaining blocker |
| --- | --- | --- | --- |
| **Macrel**, [`8c1f7321`](https://github.com/BigDataBiology/macrel/tree/8c1f7321618ccde2a28b960d32525620d2c737e3) | Sequence feature extraction and CPU ONNX AMP/hemolysis classifiers; continuous scores and native labels. No target recognition, CPP or ACP operation. | MIT project, packaged ONNX assets; Python >=3.10, ONNX Runtime and other declared dependencies. | First evaluator candidate for increment 1. Qualify an actual version/environment, input scope, asset rights, retained negatives, precision and per-input accounting. Installation success alone is insufficient. |
| **HydrAMP**, [`6590d2f4`](https://github.com/szczurek-lab/hydramp/tree/6590d2f4c2963f25d30669052a4c4a857e0e7279) | Learned AMP/MIC-conditioned sequence sampling and seed-based analogue generation; native classifier scores/filters. No protein-target conditioning or arbitrary external reward callback established. | MIT code; archived models and official starter checkpoint/PCA files are visible. Original TensorFlow 2.2/Keras 2.3 stack is legacy. Model/data use and redistribution need artifact-specific review. | Preferred generator **to qualify**, not a selected backend. Isolate its runtime if adopted. Test a bounded native route, loading assets and outputs before committing to it or promising feedback. |
| **Official HydrAMP starter**, [`7804df86`](https://github.com/szczurek-lab/hydramp-starter-kit/tree/7804df862872ccc6d09fe01c41bafbca194cfa31) | Complete-output challenge workflow, native sampling, deduplication, reference exclusions and final filters/ranking. | MIT code; bundled checkpoint/PCA; manifest requires Python >=3.8,<3.9 and legacy dependencies. Provenance documents call for checking upstream data terms. | Useful asset/environment reference, **not a modernized host stack** or a workflow to import wholesale. Its quota loop and challenge rules are unsuitable as implicit PeptideMT defaults. |
| **PepMLM**, [`3169c492`](https://github.com/programmablebio/pepmlm/tree/3169c4920f8c383948e0a5d3a7c8f87e5e7d2436) | Target-sequence-conditioned masked peptide sampling and pseudo-perplexity, from model/tokenizer-based routines. No qualified native family-feedback or analogue interface. | Public model card has MIT metadata **and** additional gated commitments on noncommercial use, authorship, data sharing and patents. No top-level repository license found at this pin. Transformer/weight/context and execution requirements remain to qualify. | Do **not** select as an unrestricted mandatory dependency. Terms prevent that conclusion from MIT metadata alone. Revisit an appropriate authorized access route or another previously audited target-capable engine at the next target milestone. |
| **PrMFTP**, [`42488d2e`](https://github.com/xialab-ahu/PrMFTP/tree/42488d2e1a2cc2855375717fa926d21c8887783e) | 21-label sequence inference with ten checkpoints and thresholded outputs in the inspected interface. | Legacy TensorFlow/Keras; continuous-score extraction and permissions unresolved in the previous review. | Broader coverage does not currently improve initial feasibility over Macrel. Keep optional; no requirement to integrate 21 functions first. |

Relevant primary research: [HydrAMP, Szymczak et al., 2023](https://doi.org/10.1038/s41467-023-36994-z),
[Macrel, Santos-Júnior et al., 2020](https://doi.org/10.7717/peerj.10555),
and [PepMLM](https://doi.org/10.1038/s41587-025-02761-2). Published experiments
qualify the authors' tested domains; they do not validate our proposed workflow.
PepMLM's [official raw model card](https://huggingface.co/ChatterjeeLab/PepMLM-650M/raw/main/README.md)
was checked directly; no access agreement was entered. Root code licenses do not
automatically settle every checkpoint, source database or future redistribution.

### Operational details that change the integration plan

**Macrel:** [`AMP_predict.py`](https://github.com/BigDataBiology/macrel/blob/8c1f7321618ccde2a28b960d32525620d2c737e3/macrel/AMP_predict.py)
uses CPUExecutionProvider and drops predicted non-AMP rows by default. The proposed
route must retain negatives (`keep_negatives=True` in that inspected routine)
and original scores/labels. The [CLI](https://github.com/BigDataBiology/macrel/blob/8c1f7321618ccde2a28b960d32525620d2c737e3/macrel/main.py)
rounds exports to three decimals: choose a qualified native-precision route or
record quantization and its consequences for ties. Do not silently reconstruct
precision. [Feature extraction](https://github.com/BigDataBiology/macrel/blob/8c1f7321618ccde2a28b960d32525620d2c737e3/macrel/AMP_features.py)
skips empty/noncanonical inputs; every requested subject must still be accounted
for by PeptideMT. `AMP_family` denotes composition categories, not a new set of
scientific functional families. The two classifier outputs are not a joint
probability of useful and safe antimicrobial activity.

**HydrAMP:** [`HydrAMPGenerator`](https://github.com/szczurek-lab/hydramp/blob/6590d2f4c2963f25d30669052a4c4a857e0e7279/amp/inference/inference.py)
exposes `unconstrained_generation` and `analogue_generation`. The former's
`filter_out=True` route repeats sampling until a quota is reached; no maximum
round count is visible there. The starter's
[`generate_library`](https://github.com/szczurek-lab/hydramp-starter-kit/blob/7804df862872ccc6d09fe01c41bafbca194cfa31/src/hydramp_starter_kit/generate.py)
adds another accumulation loop without an inspected no-progress cap. These are
source observations, not reproduced runtime failures.

**Proposed first route:** qualify the native softmax path with `filter_out=False`
and one decoding attempt. The inspected branch leaves its accumulation loop
after that batch; it still uses native AMP/MIC conditioning/scoring, and with
multiple attempts it would select internally by AMP score. This route avoids
adopting the quota-filling workflow. It is not yet an executed, validated or
approved configuration. Bound calls and elapsed time externally; disclose any
unobserved internal work. If only a filtered route works, record that fact and
its selection bias rather than claim raw proposal access. Native analogue
generation uses a finite declared attempt count and its own improvement/discovery
filters; neither their exact behavior nor useful yield has been qualified here.

The proposed integration burden is a small host-side scientific coordinator,
one Macrel access route and, if feasible, one isolated legacy HydrAMP worker.
Do not downgrade the future suite host to Python 3.8 or build a general service
platform to support one generator. Legacy packaging, safe artifact loading and
reproducible environment maintenance are real costs; no time/GPU estimate is
established. If qualification fails, report the blocker and propose a concrete
replacement for review. Do not silently replace learned generation with a mock
or declare increment 1 sufficient for B.

The previous Work check concerns **one selected shell environment** only
(Python 3.12.8; several model packages not discoverable; NVIDIA driver query
unsuccessful). It is not an audit of laboratory hardware, other environments,
GPU absence or the feasibility of CPU/external execution. Deployment must be
qualified against the actual intended host/worker environment.

## 3. Accepted first coverage and proposed comparison

**Coverage accepted under D34:** desired AMP compatibility plus adverse hemolysis,
with Macrel then HydrAMP as qualification candidates. A target-free first native
route is consistent with D33. D35 accepts increment 1's contract, provisional
operation envelope and two selectors; exact bundles/execution remain pending.
It exercises more than one objective without promising
CPP/ACP or target recognition. Define the intended antimicrobial context and the
classifier's narrower operational label separately: generic AMP classification
does not establish activity against a chosen organism/protein. Low hemolysis
score does not demonstrate absence of hemolysis, general cytotoxicity or safety.

**Increment-1 provisional envelope accepted under D35:** complete single-peptide
sequences using the 20 canonical symbols, with strict sequence preservation and
<100-residue operational scope as qualified in the accepted specification. This
is not empirical support for every size. HydrAMP uses a 25-position representation
and its starter documents training sequences of at most 25 residues; its actual
generative domain still requires qualification. Neither fact validates every
sequence/model projection. Broader chemistry remains open: a symbol string is a proposal/view,
not automatically a fully specified all-L, free-terminal chemical species.
Retain supplied termini, stereochemistry and modifications even when an operation
cannot use them. No silent stripping or score transfer to all realizations.

For the first selectors, D35 accepts the **ordered-preference comparison**:
one configuration prioritizes higher AMP model score, breaking ties by lower
hemolysis score; another reverses that priority. Retain both scores and the exact
evaluation snapshot, declared precision, candidate pool, requested count and
stable tie rule. These are operational preferences, not biological acceptance
rules; lexicographic ordering permits no tradeoff on its first objective. Require
both comparable evaluations for these specific rankings, retain other subjects
as unranked with reasons, and permit fewer than the requested count. This small
contract avoids a universal scalar fitness, calibrated-probability assumption
or compulsory Pareto archive. Other approved selectors can follow later.

### Controls that make the contributions interpretable

| Arm | Purpose and qualification |
| --- | --- |
| Supplied sequence pool + assessment/selection | Fixed increment-1 reference; evaluates selection effects without generation. |
| Simple procedural proposal/redesign + the same assessment | Shuffles/composition-matched sampling or declared permitted edits are possible controls. They are real simple algorithms, not simulated learned models or known biological negatives. Confirm which changes are meaningful within the agreed task. |
| Native learned generation + external assessment/selection | Increment-2 baseline: one qualified HydrAMP route if selected, with its own internal conditioning/filters made explicit. Compare raw observable outputs and selected subsets. |
| Native analogue generation without external feedback, if supported | Tests seed-based proposal effects under the same assessment, without mislabeling native AMP/MIC filtering as Macrel guidance. |
| External functional feedback + subsequent native calls | Increment-3 extension: Macrel-based policy changes chosen parents or allocation, then actually invokes a permitted proposal operation again. Compare with fixed/uninformed parent choice under the same declared opportunity budget. |

Use declared seeds, starting pools, length/composition scope and resource versions.
Compare selectors on the **same pool** to isolate selection; compare generators
before and after the same selector to expose its contribution. For feedback,
compare an equal-opportunity nonfeedback control and record the actual sequence
of evaluations, parent choices and later calls. No score improvement for every
seed is required; no biological superiority follows from better reward scores.

Bound both proposal and evaluation calls, attempt parameters where exposed, and
elapsed-time limits. Retain actual observed counts, time, failures and reuse;
equal final output counts do not mean equal sampling cost. Hidden provider
rejections prevent claims about all decoded candidates or exact matched internal
work. Report this limitation rather than invent denominators. A small declared
replicate set checks variability; fixed seeds alone do not guarantee bitwise
reproducibility across runtimes/hardware.

### Dependencies between learned components

The starter's [training provenance](https://github.com/szczurek-lab/hydramp-starter-kit/blob/7804df862872ccc6d09fe01c41bafbca194cfa31/data/README.md)
distinguishes AMP-source databases, AMP Scanner classifier data, MIC data and
UniProt-derived sequences/assumed negatives from its challenge reference filter.
Macrel's [training script](https://github.com/BigDataBiology/macrel/blob/8c1f7321618ccde2a28b960d32525620d2c737e3/train/train-models.py)
exports AMP and hemolysis classifiers from separate training sets and explicitly
handles overlap within its own AMP training/test evaluation. That comment is
**not evidence of a measured HydrAMP–Macrel intersection**. Exact cross-resource
sequence/homology overlap and the correspondence to deployed asset versions have
not been calculated here.

Shared public AMP source pools, UniProt-background assumptions and charge/
hydrophobicity preferences are plausible dependencies worth examining. Different
architectures (generative neural model versus feature-based random forest) do
not establish independence. Inventory data origins/versions first; if usable
sequence data are later approved, quantify overlap and clustered similarity
without relabeling assumed negatives as measured inactivity. Report overlap
unknown when it is unknown. Inspect length/composition shifts and compare matched
controls. An additional predictor is not compulsory, and agreement between
dependent predictors is not independent validation. Experimental or independently
qualified evidence, if later available, retains its separate role under C5.

## 4. Proposed implementation sequence and minimum acceptance

The increment-1 contract is accepted under D35; the later increments' rows remain
proposed **scientific acceptance contracts**, not Python signatures or permission
to implement the later increments. D36 grants commissioning for W0–W4; the real
central admission route still precedes W1. Actual qualification requires execution
in a chosen environment; source inspection does not satisfy these gates.

| Increment | Obligatory result if that increment is commissioned | Acceptance evidence before claiming it works |
| --- | --- | --- |
| 1. Assessment/selection | Import supplied proposals with original chemistry/context; run one real functional resource; retain original outputs and failures; apply explicit selectors reproducibly. | A permitted native input fixture actually runs. Every input has an attributable outcome; negative predictions survive; two policies can select differently from unchanged evaluations. Missing/incompatible/failed cases follow approved behavior. |
| 2. Minimum useful V0.1 | A real generator or redesign operation produces proposals and the same layer evaluates/selects them; no mock substitute. Generation and evaluation provenance remain separate. | One bounded end-to-end native case produces usable output and attributable evaluation/selection; a redesign case demonstrates an actual change if redesign is the claimed operation. A simple proposal control and generate-plus-select reference run with declared budgets. Empty/failure cases are also exercised. |
| 3. Priority feedback extension | An approved external evaluation policy affects later permitted generator calls, parent choice, edits or allocation. | A controlled intervention demonstrates a change in the later inputs/actions; replay verifies the decision trail. A final-only filter cannot pass. Run actual later generation and compare an uninformed/fixed policy without requiring reward improvement. Include only after the proposal operation/environment qualifies. |

The first coding sequence would therefore be: central suite admission/bootstrap;
resource/version/asset/environment qualification; increment 1; one increment-2
native route plus controls; then a decision on the qualified feedback extension.
Do not implement many interchangeable providers before one real route works.
Qualification can reveal that the proposed resources or envelope must return to
review; no general conceptual redesign is required for an explicit substitution.

### Minimum behavior under failure or uncertainty

- **Unsupported/malformed/partial input:** retain the original subject, explain
  which operation cannot run and why. Do not coerce an ambiguous residue, drop a
  modification or force molecular completion. A partial proposal may still be a
  valid stored result; this first evaluator need not support it.
- **Unavailable runtime, assets or permission:** report unavailable/failed execution;
  no invented score, silent model replacement or simulated-success fallback.
- **Empty output or exhausted budget:** preserve partial observable work, stop
  within the qualified operational bounds and record the reason. Distinguish an
  interrupted provider with unreturned work from a completed empty generation.
- **Missing or incompatible assessments:** no invented favorable/unfavorable value
  for ranking. Preserve the subject and reason; use only comparable subsets for
  the selected policy. An unmet count does not authorize relaxing requirements.
- **Opposing evaluations:** retain each original subject/view/model/context and
  score. State which qualified binding the policy uses and expose the conflict;
  no silent averaging, global confidence or post hoc winner selection.
- **Duplicate proposals and convergent paths:** keep every origin and parent path.
  Justified reuse can save computation without adding independent evidence or
  establishing full chemical equivalence. Operational sequence equality for a
  sequence-only model is not a canonical molecular-identity decision.
- **Native internal selection/limited observability:** preserve configuration and
  all exposed outputs; disclose unavailable intermediates and costs. Never claim
  all internal states satisfied a restriction from checks on returned sequences.

Use small deterministic fixtures for semantics, alongside **real-provider** checks
for implemented claims. Cases include retained predicted negatives; noncanonical
and unsupported-length inputs; partial chemistry; score rounding/ties; missing Y;
contradictory CPP outputs; two origins; missing assets; timeout and no candidate
passing a policy. Y/CPP conflicts can be controlled fixtures even if AMP/hemolysis
is selected first; they do not claim actual CPP or recognition support. Do not
require large model downloads in ordinary CI or call a mocked test scientific
qualification. Preserve provider environment, asset/configuration identity,
evaluated view, assumptions, seeds, all observable results and selection replay
inputs. Predictive uncertainty may be unavailable; report that rather than invent
calibrated intervals. No safety/affinity/experimental efficacy claim is a software
acceptance criterion for this proposed task.

## 5. Ownership and a small implementation boundary

PeptideMT owns the design problem/plan/evidence relationships, qualified function/
resource bindings, proposal ancestry, operation-specific evaluated views and
assumptions, original/derived results, explicit selections and campaign accounting.
Keep these small and tied to the chosen operations; no universal registry,
planner, ontology, constraint engine or probabilistic model is needed.

MolSysMT owns molecular representation/manipulation. Its audited
[`get/select/convert/extract` interfaces and build/physchem paths](integration_audit.md#molsysmt)
should be reused when a molecular view is actually needed, not reimplemented in
PeptideMT. In particular,
[`build_peptide`](https://github.com/uibcdf/molsysmt/blob/e395e52646dab2ecb480d3d67aa7254be99b8524/molsysmt/build/build_peptide.py),
[`mutate`](https://github.com/uibcdf/molsysmt/blob/e395e52646dab2ecb480d3d67aa7254be99b8524/molsysmt/build/mutate.py)
and [`get_peptide_chemical_template`](https://github.com/uibcdf/molsysmt/blob/e395e52646dab2ecb480d3d67aa7254be99b8524/molsysmt/physchem/get_peptide_chemical_template.py)
need operation-specific qualification; the inspected template leaves
stereochemistry unspecified. Neither coordinate construction nor a fully defined
chemical realization is obligatory for a native sequence predictor.

Use the [pinned support-library audit](integration_audit.md) for SMonitor
`signal/emit/diagnostic_scope`, ArgDigest `FunctionContract/Domain`, DepDigest
`dep_digest/DeclaredRegistry` and PyUnitWizard quantities. These provide diagnostics,
argument/dependency handling and physical units; they do not establish scientific
applicability or calibrate scores. Select actual paths during the qualified
bootstrap rather than copying their responsibilities into a new framework.

TopoMT keeps topology work; DockingMT, PharmacophoreMT and ElastNetMT keep their
respective specialized molecular analyses. Their partial/experimental audited
paths are not ready recognition/affinity oracles. MolSysViewer remains optional
visualization. MolSys-AI keeps shared AI access where qualified; a PeptideMT
adapter must not depend on an unimplemented provider facade. Praxis and Recorda
can supply audited methodology/observable execution records; PeptideMT preserves
the scientific meaning of its outputs. Sabueso/Nextia/MolI/agent runtimes are not
required to execute the first design route. No duplicate global orchestration
or project-interpretation service belongs in V0.1.

## 6. Target-directed milestone and remaining decisions

After increment 2, prioritize **one permitted, executable target-capable route**
before expanding to many interchangeable families/providers. It may condition on
a target sequence or structure; structural C is not the only possible route.
Evaluate PepMLM terms and the previously audited alternatives only against that
specific operation/domain. Do not impose target tensors on HydrAMP/Macrel.

Retain the scientific target context when present and record whether it actually
influenced a native operation, a later selection or neither. Distinguish:
target-conditioned proposal generation; a model-specific compatibility signal;
and independent recognition evidence. If recognition is a requirement that the
available resources cannot assess, report it unresolved. Adding a target name
to a campaign or pseudo-perplexity to its results does not satisfy that requirement.
The target milestone can proceed alongside increment 3; neither requires all
future-horizon capabilities or a universal optimizer first.

Before commissioning development, the remaining items are:

1. **Approved increment-1 contract, now fixed:** D35 settles the scientific
   [specification](v0_1_increment_1.md), conservative preprocessing, provisional
   chemistry/lengths, selectors and M1–M8. Operational qualification may expose a
   material limitation to review; full canonical identity, state grouping and
   broad chemistry remain deferred rather than prerequisites.
2. **Exact qualification bundle:** Macrel first and HydrAMP second is accepted
   under D34; qualify exact assets/terms, intended host/worker environment
   and what would justify returning with an alternative. These are candidates,
   not mandatory dependencies approved by B.
3. **Operational execution conditions:** select permitted fixtures, actual
   environment/budgets and real-provider evidence for the accepted M1–M8.
   Policies/precision/ties are already agreed; there is no new universal
   biological cutoff or promised runtime. See the bounded commissioning brief.
4. **Feedback and target milestone commissioning:** choose the first actual
   feedback operation after qualification, its inclusion in V0.1 or the next
   increment, and the bounded target-route evaluation following the functional
   core. Neither the exact feedback algorithm nor a target engine is selected.
5. **Authorized admission/implementation:** settle the selected P02/P03/
   P05/P06 portions, the suite starter route and small concrete interfaces after
   these scientific contracts. D36 permits W0–W4 and only the central admission
   issue exception; W1 is gated on actual completed W0.

Codex can then resolve internal data structures, batching, process management,
serialization details, deterministic tie implementation and routine tests within
the approved meanings, ownership and observable guarantees. Changing scientific
attribution, permitted chemistry, a resource's role, terms-dependent deployment,
selection meaning or claims requires review. The immediate next discussion should
execute **W0 of the authorized increment-1 assignment**, then W1–W4 after its
actual completion and operational prerequisites. D35 closes the scientific contract;
exact bundles, terms, environment, fixtures/budget and central admission remain.
The [work order](increment_1_work_order.md) makes those tasks reviewable without
another general architecture or model study.
