---
summary: Prepare and qualify the commissioned native HydrAMP route within H0–H4.
issue: uibcdf/peptidemt#8
status: resolved
opened: 2026-10-29
closed: 2026-11-03
verification: measured
area: [generation, qualification, integration]
guard:
normative: devguide/hydramp_dev3_acceptance.md
blocked_by: []
supersedes: []
---

# Increment 2: bounded HydrAMP qualification

## Resolution through experimental AMP acceptance — D41, 2026-11-03

The investigator accepts HydrAMP modernized with PyTorch as the exact reviewed
experimental AMP resource. The [D41 acceptance record](../hydramp_dev3_acceptance.md)
and [decision receipt](../evidence/hydramp_dev3_acceptance.json) bind the disposition
to the original review and unchanged provider/consumer identities. This resolves
#8 through the explicitly accepted scope, not by declaring universal equivalence,
biological efficacy, every historical H0–H4 plan or a release qualified.

All probability/global-rank FAILs, unfavorable H4 results, original asset/use
limits, separate private/public execution scopes and exhausted budgets remain.
The original proposed review bytes are retained before acceptance. Earlier
pending statements below describe their historical checkpoints.

The investigator also directs preserving future comparison, independent-product,
family-extension/successor and original-author-interest questions. Their new
consumer owner is [PeptideMT #32](https://github.com/uibcdf/peptidemt/issues/32),
with an [active follow-up record](../pending_proposals/hydramp_scientific_followup.md)
and cross-linked HydrAMP #3–#6. The existing numerical/profile provider issues
remain open. No new scientific run, publication or external contact occurs.

## PyTorch port commissioned — 2026-10-30

D39 records the investigator's instruction to move to PyTorch if feasible.
The separate local `peptidemt-pytorch` worktree preserves the dirty packaging
worktree, original `amp/` tree and legacy workers. The provider owns the new
`ports/pytorch/` implementation; no molecular parser or model implementation is
copied into PeptideMT. The [port review](../hydramp_pytorch_review.md) separates
the implemented computational core from the still-unqualified native generator.

The fixed decoder, native AMP/MIC heads, numeric PCA inverse transform and
hash-pinned JSON/NPY loader have synthetic tests. At that initial implementation
milestone no pretrained weights/PCA had been loaded; the later authorized
comparison below supersedes that execution status. H0–H4 remain partial; descriptors,
native ordering/provenance and consumer integration are not accepted by these
tests. The fork has issues disabled; keep #8 as the active consumer tracking
route rather than contacting upstream or changing repository settings.
The [real-checkpoint comparison](../hydramp_pytorch_comparison.md) has now run
under the explicitly approved 4 GB task budget, using all six allowed forward
evaluations and one PCA load, without retries. All tokens/strings are exact and
PCA/heads pass, but 18 of 6,300 decoder probability values exceed the unchanged
tolerance. Overall comparison status is **fail**; cause is localized to the
decoder path but not yet established internally. Observed maximum worker plus
supervisor RSS was approximately 511 MiB. This is not model acceptance or H2
completion; new real-model diagnostics require a separate approved budget.
The [intermediate diagnostic](../hydramp_decoder_trace.md) has now completed two
separately approved forwards: endpoints are bitwise unchanged and divergence is
already observed in the GRU. The original failed comparison is preserved. A
separate [joint-product candidate](../hydramp_gru_candidate.md) is built and passes
twenty-nine artificial-weight checks but has since failed its separately approved
single-forward validation (17/6300 probability violations, no token changes).
It is not adopted as a correction. An [independent float64 reference](../hydramp_numeric_reference.md)
completed its two separately authorized evaluations on 2026-11-02: FP64
formulations agree, native/port FP32 errors have similar magnitude, and all
300 tokens match. The execution receipt and numerical admissibility review are
linked there and the [explicit issue review](https://github.com/uibcdf/peptidemt/issues/8#issuecomment-6593862430)
was subsequently given the limited D40 disposition below. The original diagnostic
failures, deployment precision and criteria are unchanged. #8 remains open for
full H0–H4 qualification and remaining investigator evaluation.

## Limited behavioral acceptance — D40, 2026-11-02

The [behavioral evidence and limited acceptance record](../hydramp_behavioral_acceptance.md)
uses retained outputs only: tokens and saved AMP/MIC score order remain unchanged,
with all pair relations preserved. Four raw normal draw fixtures match bitwise
between retained NumPy 1.18.5/2.4.6 workers; this is not full generator repeatability.
Twelve artificial boundary/diagnostic tests pass. No model or PCA loaded and no
learned forward, descriptor or Macrel call occurred. The investigator explicitly
accepted the measured numerical deviation only on these twelve compared inputs,
allowing continued dev0 qualification. The [decision receipt](../evidence/hydramp_limited_acceptance.json)
pins exact evidence and scope. Complete HydrAMP acceptance, broader numerical
criteria and new model execution remain pending. Prior failed reports and the
unadopted dev1 disposition remain unchanged; this issue stays partial.

## Generation wrapper preparation — 2026-11-02

The [new dev2 candidate](../hydramp_generation_preparation.md) is isolated on
`peptidemt-pytorch-generation`, preserving dev0/dev1 and all exact evidence.
Its numerical core/PCA are byte-identical to dev0; it adds seeded generation,
original-token scoring, AMP-order native views and explicit occurrence trace.
The installed Python 3.14 wheel has clean base dependency closure and 74 passing
artificial checks. The modlAMP descriptor adapter is explicit, not installed or
scientifically qualified in Python 3.14. Reusable descriptor needs are recorded in
[MolSysMT #485](https://github.com/uibcdf/molsysmt/issues/485#issuecomment-6595490991).
No pretrained model/PCA, real descriptor or Macrel call occurred. D40 does not
automatically qualify dev2; exact broader fixture/use and fresh finite execution
limits precede further learned work. Complete H0–H4 remains partial.

## Original evaluation-resource review — 2026-11-02

The investigator requests checking original tests, benchmarks and data. The
[resource inventory](../hydramp_upstream_test_resources.md) finds no conventional
automated test paths in the pinned original master, but identifies original
notebooks, archived data/results and paper supplementary evaluation resources.
They are candidate regression/scientific references, not an accepted benchmark
or a new model/descriptor/training allowance. CAS/NAS source has training loops
and an unresolved helper import; its settings and the large generation notebooks
do not match our selected route. No archive/table or scientific artifact was
loaded and no existing accepted check was repeated.

## Exact full-comparison preparation — 2026-11-02

The [dev3 preparation](../hydramp_full_comparison.md) retains the dev2 numerical
core/generation bytes and adds an explicitly configured modlAMP 4.3.3 route.
The Python 3.14 profile has clean native closure (41 packages), 76 passing
installed-package artificial checks and 13 final controller checks. Two model-free
descriptor bundles on eight fixed original published occurrences match all five
fields exactly across reference, modern route and archived values. Charge pH7 /
amide=True and pI amide=False preserve legacy definitions despite changed modern
defaults. No neural model or PCA loaded in this preparation. The exact proposed
six-generation / 22-network comparison has passed byte-only preflight and awaits
fresh investigator approval of its source/assets/use and finite host/call plan.
D40, all prior failures and the partial H0–H4 status remain unchanged.

## Approved full-comparison execution — 2026-11-03

The investigator authorized the exact prepared plan, SHA-256
`b019e1dfa4e8c61ed667198b73dd7b09dfb5308459225399c84c9eb54beae929`.
The [execution report](../hydramp_full_comparison.md) records six generation calls,
22 network evaluations and six descriptor bundles, with no retry/GPU/training/Macrel.
All 900 tokens, 36 paired sequence/occurrence returns and five descriptors match
on twenty distinct latent inputs, and each worker repeats the same-seed output
bitwise. Head scores pass. The original strict probability diagnostic remains
FAIL (58/18900 values, maximum `4.845857620239258e-5`); no threshold changes.
Workers used 39.07 s total and at most 550.19 MiB conservative combined RSS.
Modern public-call timings are lower, but its whole-worker time is higher; import
and construction were not separately timed, so no general speedup is claimed.
D40 scope and all prior evidence stand; broader acceptance, PeptideMT adapter/
portable provenance and full H0–H4 receiving remain pending. Allowance exhausted.

## Confidence expansion proposal — 2026-11-03

At the investigator's request for stronger confidence, the
[proposed confidence campaign](../hydramp_behavioral_acceptance.md#proposed-confidence-campaign-after-the-dev3-comparison--2026-11-03)
prioritizes broader paired coverage (candidate: 256 distinct latent rows),
decision margins, predeclared batch/occurrence cases and consumer qualification.
At that proposal checkpoint the exact manifest and shared-host budget still needed
preparation and approval. The recommendation was not an
accepted criterion, a D40 extension or new execution authority. It preserved every
prior FAIL and exact receipt without itself allowing model/PCA/descriptor/Macrel calls.

The investigator subsequently instructed proceeding. The
[prepared confidence campaign](../hydramp_confidence_campaign.md) fixes 256 new
latent inputs, one repeat, five core layout controls per worker and an exact
proposed 132-network-forward/34-generation-call budget. Thirty-one artificial
controller checks, both model-free raw-input probes and byte-only preflight pass.
At that preparation checkpoint no new learned model/PCA/descriptor call had run;
exact execution approval and broader candidate acceptance were pending. The
subsequent separately approved execution is recorded below.

## Approved confidence execution — 2026-11-03

The investigator explicitly authorized the prepared 132-forward CPU plan. The
[executed campaign](../hydramp_confidence_campaign.md) completed both workers once:
all 7,700 paired token positions, every public batch's returned order/strings and
five descriptors match; heads stay within band and repeats are bitwise exact.
Distinct-input coverage is 256 latent rows / 6,400 token positions. The probability
diagnostic FAIL now has maximum `2.2727251052856445e-4`; the global AMP pair check
also FAILS (one reversal, two split native ties, seven new port ties across 32,640
pairs). All changed AMP relations are between batches, near score 1; no actual
public-batch order changed. Native batch-size sensitivity is also observed.
Both verdicts, thresholds and D40 scope remain unchanged. Worker time totals
68.39 s; sampled worker RSS is approximately 525/404 MiB, without resource stops.
The allowance is exhausted. Numerical/ranking relevance review, original-Drive
bundle provenance and PeptideMT adapter/H0–H4 receiving remain pending.

## Saved ranking relevance and proposed disposition — 2026-11-03

The investigator authorized a saved-output relevance review. The
[review and concrete limited-disposition proposal](../hydramp_rank_relevance.md)
locate the changed score branch in AMP-head execution on identical original
tokens, without proving an individual arithmetic cause. Replaying all k=1..256
cuts finds one membership replacement at k=2,5,9,10,23,42,50 in both declared pool
orders; thirteen occurrences move rank, at most two places. Small score errors
are therefore not universally selection-irrelevant. PeptideMT's actual selectors
read Macrel AMP/hemolysis, so this AMP-only replay is not H4 or a selector test.
Eighteen guarded artificial checks pass in the explicit isolated published-test
profile; an initial shared-interpreter invocation is preserved and superseded,
with identical corrected analysis output. No new model/PCA/descriptor/Macrel call
ran. Admission of the exact dev3 fixture deviation for continued consumer
qualification is recommended, with both FAILs, raw scores, contracts and D40 kept
unchanged. Investigator acceptance is pending; #8 remains open.

## Causal numerical investigation and owning-fork receiving — 2026-11-03

The investigator requests the cause and authorizes reporting in the owned fork,
retaining established modern numerical improvements. Issues were enabled by the
investigator; [HydrAMP #1](https://github.com/uibcdf/hydramp/issues/1) now owns the
provider investigation. The [causal record](../hydramp_amp_numerics.md) documents
different legacy/modern sigmoid CPU kernels on identical artificial inputs,
independent FP64/80-digit Decimal comparisons and a legacy monotonicity
counterexample. The modern operation is more accurate at 162/272 points, legacy
at 23, with 87 ties; this is not proof of whole-model or biological superiority.
The exact original-token AMP trace was prepared with sixteen guarded artificial
checks and a native zero-weight graph smoke. Earlier instrument setup/metadata
failures and a host-I/O timeout are retained. The investigator then approved its
exact allowance; the [execution receipt](../evidence/hydramp_amp_trace_execution.json)
records 36 learned forwards, 24 sigmoid replay vectors and two FP64 activation
vectors, all now spent. Saved endpoints reproduce bitwise. The final-kernel
switch alone reproduces all ten changed AMP pair relations: modern corrects one
legacy reversal and splits two ties in the conditional FP64 direction, but
introduces seven ties. The first recorded layer difference is the first LSTM;
whole-head precision and biological superiority remain unestablished.
The [full AMP-head FP64 comparison](../hydramp_amp_reference.md) was then
prepared with seventeen artificial checks and separately authorized by the
investigator after its concrete limits were presented. All 24 reference forwards
completed in 3.75 s / 81.3 MiB sampled worker RSS; both layouts agree bitwise.
Modern has lower aggregate maximum/mean/RMS error at every nontrivial recorded
stage on this selected cohort, including the complete AMP output. It is closer
in 91 outputs versus 58 native, with 43 equal errors; seven new modern ties
persist. Both exact allowances are spent. General equivalence, biological
superiority, wider dev3 acceptance and H0–H4 receiving remain unestablished.
The investigator subsequently asks why native is closer in 58 cases. The
[saved-array review](../hydramp_amp_error_attribution.md) identifies 39 native-closer
logits, 12 modern-closer logits and 7 identical logits among those 58 final native
wins. Native/modern full-head FP64-cast matches are 48/47. These are additional
metrics, not new acceptance criteria. Eight guarded artificial tests pass; no
model, weight/PCA load or activation evaluation occurs in this review.
Both existing FAILs, D35/M1–M8, D40, original environments and bundle/use limits
remain unchanged. Broader acceptance and consumer/H0–H4 receiving stay pending.

## Local fork packaging — 2026-10-30

The investigator created [uibcdf/hydramp](https://github.com/uibcdf/hydramp) and
explicitly authorized local packaging preparation on `peptidemt-inference`.
The local build `1.2.0+uibcdf.1` preserves the complete upstream `amp/` tree and
MIT licence at `6590d2f4c2963f25d30669052a4c4a857e0e7279`. It separates base inference,
optional training/data dependencies and PEP 517 build requirements. A wheel build,
exact-wheel installation and guarded class imports pass in an isolated Python
3.8.20 worker. All 57 retained external versions match the earlier reference.

HydrAMP no longer needs a metadata override. Native checking retains three
modlAMP-only discrepancies (`nose`, `lxml`, unavailable MySQL); the explicitly
declared effective profile has zero. No modlAMP version or descriptor changed.
The [consumer handoff](../evidence/hydramp_fork_packaging.json) identifies the
producer-owned local report and receipt hash; the fork changes are uncommitted
and no published adoption is claimed. Original preparation resources remain.

The investigator also highlighted the public Drive linked by the original README.
Anonymous inspection confirms its four original archives. No full archive was
downloaded; byte parity between the starter assets and original archive remains
unverified. This preparation introduces no model/PCA loading, inference, Macrel
calls or GPU use and does not change H0–H4 acceptance gates.

## Locked environment milestone — 2026-10-30

The [H0–H1 review](../hydramp_environment_review.md) records successful isolated
installation and guarded imports using the official starter's exact lockfile and
declared inference-only metadata substitutions. All 61 installed versions match
the lock; 41 installed native Python source files match the pinned upstream bytes.
TensorFlow 2.2.1, Keras 2.3.1 and `HydrAMPGenerator` import without instantiating
the generator or opening scientific artifacts. Preparation used two CPU cores,
single native-library threads, bounded memory/time and no GPU.

Native metadata checking still fails with eight expected discrepancies from
the starter overrides; the effective declared profile has zero discrepancies.
These are separately retained in the [receipt](../evidence/hydramp_h0_h1_review.json),
not presented as clean native closure. The original source, wheel metadata and
lockfile were not patched. The local-use review also records publisher provenance,
original archive licence metadata and the still-unexecuted PCA loading boundary.

H0/H1 remain partial for exact-bundle/use and deployment-profile disposition and
authorized model-load qualification. Model loads, generation and new Macrel calls
remain zero. Adapter preparation is authorized under D38; exact bundle/use review
and fresh host/call budgets still precede scientific execution. The earlier
preparation summary below records its original dated checkpoint.

## Current preparation and renewal discussion — 2026-10-29

The investigator explicitly requests a nonexclusive inventory: HydrAMP, PLUM
and other generators can coexist as optional resources. The
[expanded source survey](../generative_resource_survey.md) records complementary
capabilities and separate readiness, including OmegAMP and non-AMP candidates.
An implementation priority is not an exclusive platform/model choice. D38's
commission remains bounded; listed alternatives are not silently adopted.

The investigator accepts retaining HydrAMP as one optional reference despite its
legacy stack, alongside future alternatives, and is discussing a modern fork
and a later multi-family algorithm. The
[scope discussion](../v0_1_scope.md#hydramp-renewal-and-other-functions--exploratory-discussion-2026-10-29)
keeps modernization, new training and resource adoption distinct. At this
historical checkpoint no fork or replacement had been approved. The later local
fork packaging and D39 port commission above supersede that preparation status;
neither accepts a replacement model. D38's original model-loading/execution
prerequisites still apply.

Exact original source and 65 selected official starter files were acquired and
verified against Git blobs/SHA256, including 60 checkpoint files. Forty-two
numeric weight headers were checked without array/model loading. A task-owned
Python 3.8.20 bootstrap exists; the original dependency dry run fails because
modlAMP 4.2.3 requires unavailable mysql-connector-python==8.0.17. Conda also
lacks the requested old setuptools artifacts and modlAMP 4.2.3 in the inspected
channels. The bootstrap uses setuptools 75.3.0; this is not a qualified HydrAMP
runtime. No dependency metadata was patched, no scientific provider was installed
in that environment, and no TensorFlow/model/PCA was loaded. H0/H1 remain partial;
the original resolution failure is not bypassed or reported as clean closure.
The [preparation receipt](../evidence/hydramp_preparation.json) and
[asset inventory](../evidence/hydramp_reference_assets.json) preserve the exact
bounded observations and hashes; they do not clear H0/H1 or authorize model calls.

## Commissioning accepted — 2026-10-29

D38 records explicit investigator approval to continue after the scope explanation.
The single native de novo route and H0–H4 obligations below are commissioned for
artifact/use preflight, isolated legacy environment and adapter preparation.
Model loading/inference remains gated on the exact bundle, use conditions and a
fresh shared-host envelope, including a separate Macrel budget. There is no GPU
or automatic retry/refill authority and no scientific acceptance of HydrAMP.

This existing #8 record now owns the commissioned qualification through its
actual H0–H4 disposition, instead of opening a duplicate implementation theme.
The original review-only close criterion below is superseded by this dated
commission: preserve partial status until actual evidence and investigator
acceptance or a documented narrowed/declined outcome. The earlier proposal
is retained as the approved scope with its historical status explicit.

## Original proposal — historical review checkpoint

Status: **proposal for investigator review**, 2026-10-29. This record prepares
the next commission; it is not acceptance of HydrAMP or execution permission.
The investigator requested continuing after D37 and completed increment-1
delivery at `b872f32965f50ccec64c46659176ca8c8acf727c`.

## What and why

D33 requires real learned generation/redesign plus assessment/selection for the
minimum useful V0.1. D34 names HydrAMP as the first generator candidate after
Macrel. Propose qualifying **one native de novo route**, using the existing
[H0–H4 plan](../v0_1_increment_1.md#62-qualification-gates-with-a-small-execution-budget).
No general architecture, new family ontology, feedback optimizer or second
generator interface is needed to answer whether that route works.

Increment 1 is completed under D35/D36 and accepted under D37. Its
[acceptance receipt](../evidence/increment_1_acceptance.json), M1–M8, molecular
contracts, exact native evidence and both selectors remain unchanged. Generation
must add actual proposals, not import a fixed pool and call it learned generation.

## Read-only findings

Official branch identities were checked through GitHub on 2026-10-29 and match
the previous inspected pins:

| Source | Immutable identity and inspected inputs |
| --- | --- |
| HydrAMP 1.2.0 source | `szczurek-lab/hydramp@6590d2f4c2963f25d30669052a4c4a857e0e7279`; [native generator](https://github.com/szczurek-lab/hydramp/blob/6590d2f4c2963f25d30669052a4c4a857e0e7279/amp/inference/inference.py), [package requirements](https://github.com/szczurek-lab/hydramp/blob/6590d2f4c2963f25d30669052a4c4a857e0e7279/setup.py) |
| Official starter, asset/environment reference | `szczurek-lab/hydramp-starter-kit@7804df862872ccc6d09fe01c41bafbca194cfa31`; [manifest](https://github.com/szczurek-lab/hydramp-starter-kit/blob/7804df862872ccc6d09fe01c41bafbca194cfa31/pyproject.toml), [provenance](https://github.com/szczurek-lab/hydramp-starter-kit/blob/7804df862872ccc6d09fe01c41bafbca194cfa31/README.md#model--data-provenance), [model configuration](https://github.com/szczurek-lab/hydramp-starter-kit/blob/7804df862872ccc6d09fe01c41bafbca194cfa31/checkpoint/model/model_config.json) |

The starter declares Python >=3.8,<3.9, TensorFlow 2.2.1, Keras 2.3.1 and an
older numerical stack. It overrides HydrAMP's dependency metadata and modlAMP's
database requirement. These are explicit upstream deployment choices, **not a
tested dependency solution for PeptideMT**. A plain install and the starter's
custom resolution route are different candidates; any required override needs
an explained, reproducible dependency contract before qualification.

The starter identifies an epoch-37 model and a PCA decomposer. Git tree metadata
lists 60 checkpoint files totaling 3,718,445 bytes, including layer/configuration
files. That is an inventory size, not a download, SHA256 receipt, complete runtime
size or RAM estimate. Model/data provenance still needs artifact-specific review;
public access and an MIT code license alone do not settle every intended use or
redistribution right. No numerical weights or PCA blob were downloaded or
deserialized here.

## Finite attribution and functional receiving preparation — 2026-11-03

The investigator directs preservation of independently justified modern results
rather than forced legacy identity. The [activation analysis](../hydramp_amp_activation_attribution.md)
finishes the 58-case decomposition: native upstream differences, final-kernel
approximation and beneficial or harmful compensation coexist. Of seven modern
ties, three already tie after rounding the FP64 target to float32 and four do
not. A saved-only precision counterfactual is recorded, unimplemented and
unaccepted. Dev3, original FAIL reports and D40 remain unchanged.

The [private receiver](../hydramp_receiving_preparation.md) preserves 272 retained
occurrences with exact native fields/order/trace replay, including 20 leading-M
incompatibilities. The [exact H3/H4 experiment](../hydramp_h4_qualification.md)
now fixes two live 16-row generation batches and three Macrel calls (one four-row
W3 control plus both generated pools), portable provenance and both D35 selectors.
Thirty-four guarded artificial receiver/controller checks and actual frozen-core
model-free compatibility pass. No new model/PCA/descriptor/Macrel call was made;
fresh approval of the exact host/call plan is pending. Broader scientific
acceptance, final optional-backend/API qualification and H0–H4 disposition remain
pending; this preparation does not create a new scientific decision.

## Approved bounded private receiving result — 2026-11-03

The investigator then approved the exact H3/H4 CPU plan. Its
[executed result](../hydramp_h4_qualification.md#approved-execution-and-independent-review--2026-11-03)
passes two 16-row generations, exact cached dev3 returns and same-operation
receipt/replay, 30 compatible generated Macrel assessments plus four exact W3
controls, portable attribution and both unchanged selectors. Two leading-M
proposals remain explicit incompatibilities. Six neural forwards, two descriptor
bundles and three Macrel calls are fully consumed; no retry or resource stop.
Total time is 55.76 s, maximum sampled process-tree RSS 553.5 MiB.

All nine generated Macrel AMP-positive rows are also Hemo-positive. Thus
functional composition passes without establishing joint AMP/hemolysis utility,
biological superiority or broader scientific acceptance. The public installed
optional-backend/API and its HydrAMP attribution boundary remain future work.
The [execution receipt](../evidence/hydramp_h4_execution.json) preserves this
finite result, all exclusions and original numerical limits. Investigator
H0–H4 disposition remains pending; no new scientific decision is inferred.

## Public data receiving and installed reader — 2026-11-03

The investigator requests continuing after the private H4 report. The
[implemented public data boundary](../hydramp_public_receiving.md) now exposes
`HydrAMPReceipt`, retains v1 semantics and shares ResultSet's existing strict
JSON duplicate-key protection. A local unpublished wheel passes 41 selected
installed reader/controller/W1 checks, exact H4 saved replay, dependency closure
and documentation HTML/doctests. Prior source bytes and failed/corrected source
harness evidence remain retained. This qualifies the installed data boundary,
not a public generation execution adapter, another scientific run or broad dev3
acceptance. The previous allowance is exhausted; final disposition remains pending.

## Isolated public execution adapter prepared — 2026-11-03

The investigator then commissions the actual execution adapter. The
[implemented route and qualification plan](../hydramp_execution_adapter.md)
retains one installed CPU worker, pinned identities, explicit host/call limits,
native operation delegation, structured failures, faithful receipt and parent
Ackredit capture. Fifty-five installed controlled checks, missing-engine
receiving, two approval controls and documentation builds pass. A diagnosed
fixture-inheritance error was corrected without touching sibling packages.
The planned single real-adapter case needs new approval: 16 proposals/seed 1001,
three neural forwards, one descriptor bundle, numeric PCA/checkpoint loading,
no Macrel/legacy calls or retries. No real model has run in this step.

[Our HydrAMP #2](https://github.com/uibcdf/hydramp/issues/2) receives a nonblocking
provider-owned profile-metadata proposal. No new descriptor definition, model
candidate, architecture or scientific adoption follows. Original numerical FAILs,
the joint AMP/hemolysis limitation and investigator disposition remain unchanged.

## First public attempt: qualifier limit fix, no learned operation — 2026-11-03

The investigator approved the exact prepared single public call. It stopped in
worker preflight because the parent qualifier set both soft/hard RLIMIT_AS to
1 GiB, which the child could not raise to its requested 8 GiB. No checkpoint/PCA,
neural or descriptor operation was attempted; the failed receipt and original
source/plan remain retained. The [corrected qualifier and fresh plan](../hydramp_execution_adapter.md#first-approved-attempt-and-parent-limit-correction--2026-11-03)
set parent soft 1 GiB/hard 8 GiB and preserve incomplete-case status. Four model-free
regressions pass. No scientific method, consumer/backend wheel or SDK changed.
A new public-call attempt requires fresh approval under the original no-retry
limit; broader scientific disposition remains pending.

## Corrected installed execution completed — 2026-11-03

The investigator then approved the corrected single installed-adapter case.
It completed with **16 proposals**, exact retained native results/order/indices/
trace, exact saved replay and captured parent attribution (seven records).
The [execution record](../hydramp_execution_adapter.md#corrected-installed-public-case-completed--2026-11-03)
reports 8.358 s / 432.2 MiB sampled aggregate RSS and the consumed three-forward
budget. No Macrel, legacy or retry was run; broader scientific disposition is
still pending. The earlier failed startup remains preserved.

## Consolidated dev3 acceptance review prepared — 2026-11-03

The investigator requests the final bounded-acceptance report after the actual
public adapter case passes. The [consolidated review](../hydramp_dev3_acceptance_review.md)
binds the recommendation to the exact provider/consumer wheels and retained
artifacts. It separates observed sequence/return fidelity, explained numerical
differences, preserved probability/global-rank FAILs, private H4 composition and
the independently executed public generation case. Zero of thirty compatible H4
proposals have joint Macrel AMP-positive/NonHemo labels; no biological quality or
general equivalence is inferred. Broader asset identity/use and deployment
limitations remain explicit.

The recommendation is acceptance only as a bounded experimental AMP resource,
with no new scientific method, run budget, redistribution or release. The user
has authorized preparing this report, not accepting its scientific disposition.
No new D-number is assigned; D40 remains its original dev0 decision. This owning
record stays partial and #8 stays open pending investigator disposition.
The report uses retained evidence only and performs no scientific evaluation.

## Proposed scientific boundary

Use the native softmax constructor and `unconstrained_generation` with
`mode='amp'`, `filter_out=False`, `n_attempts=1`, `properties=True`, an explicit
seed and bounded positive `n_target`. The inspected branch breaks after its
batch rather than refilling a quota. Preserve its native return order, duplicates,
AMP/MIC scores and descriptors. Internal conditioning/scoring and token argmax
remain part of the method; this is not an unconditional or decision-free sampler.

Retain these distinct layers: HydrAMP conditioning and native scores; generated
sequence occurrences and their provenance; separate Macrel assessment of
compatible unchanged strings; and either existing PeptideMT selector. Native
`mic` is not a concentration, and native `amp` is not Macrel's `AMP_probability`.
Agreement is not independent biological validation. The original decoder token
layout may differ from the returned string's re-encoding; preserve that unknown
instead of asserting unobserved token-level equivalence.

Account for every returned occurrence and any requested/returned-count mismatch.
Keep empty/malformed/noncanonical/unexpected-length output and incomplete runs
explicit; do not silently repair, deduplicate, refill or assign a failed view's
score to a different molecule. Macrel's leading-M/chemistry rules remain in force.
No inferred termini, stereochemistry or crosslinks are added to generated strings.

## Proposed commissioning sequence

| Stage | Reviewable result and stopping condition |
| --- | --- |
| H0: artifact/use preflight | Exact source, checkpoint/PCA inventory and byte digests, applicable terms and permitted local use. Unresolved necessary rights stop acquisition/use; redistribution is not requested. |
| H1: isolated deployment | One reproducible Linux CPU legacy worker, installation/import origins and truthful dependency closure. Preserve the Python 3.14 suite host and shared environments. No silent TensorFlow modernization or copying the generator. Source inspection and solver success cannot establish model-load success. |
| H2: bounded native calls | Retain the proposed four calls/52 requested outputs from H0–H4. An allocation is direct smoke n=4, direct n=16/seed A, adapter n=16/seed A, adapter n=16/seed B. The repeated seed supplies parity/repeatability evidence within four total generation calls, not four direct plus four adapter calls. No retry/refill. |
| H3: fidelity/repeatability | Compare actual returned sequences/order/scores/descriptors for the direct/adapter repeated case and preserve any variation. A seed alone is no promise of bitwise repeatability. Usable real output is required; controlled stand-ins cover failures only. |
| H4: end-to-end assessment | Preserve all generated proposals, assess compatible strings with the qualified Macrel route, and apply both unchanged selectors. Compare the same pool before/after selection and a declared small procedural control. Freeze the control and its budget before execution; it is not a replacement generator or an efficacy benchmark. |

Before model loading or generation, inspect the actual shared host and agree the
worker's CPU/thread, wall-time, RAM/address-space, disk and child-process limits.
Use no GPU at this stage. The previous Macrel allowance is exhausted: H4 requires
its **own fresh call/input/resource budget**, including the control and any parity
calls. Do not invent that budget from the 52 requested HydrAMP outputs. Insufficient
resources or an unmaintainable runtime return this candidate for reconsideration.

Reuse MolSysMT for molecular/FASTA operations; keep peptide-specific orchestration
in PeptideMT under the canonical component map. Preserve DepDigest, SMonitor and
Ackredit boundaries. The MolSys-AI umbrella concerns suite understanding/operation;
its presence is not a reason to relocate this peptide generator there. Propose any
missing independently reusable sibling operation to its owner before duplication.

## Scope, exclusions and acceptance of this proposal

This issue closes when investigators accept, narrow or decline the concrete next
commission and the decision is recorded with explicit execution prerequisites.
No new accepted decision is inferred from preparing this record. If approved,
implementation/evidence needs a linked owning work record and actual H0–H4
results before scientific acceptance; unresolved stages remain partial.

Analogue generation, feedback, protein-target conditioning, altered chemistry,
new selection rules, training, package/model redistribution and publication are
outside this proposed commission. Preserve original W3 artifacts while useful;
[retained-resource review #7](https://github.com/uibcdf/peptidemt/issues/7) has its
own owner and disposition. The new documentation-tooling inventory handoff
[MolSysSuite #156](https://github.com/uibcdf/molsyssuite/issues/156) stays separate
from completed #151/#152 receiving.

## What was refuted

- Acceptance of Macrel is not acceptance of a generator, a new inference budget
  or a complete generative V0.1.
- A visible starter checkpoint or historical Python 3.8 recipe is not a qualified
  installed runtime, trusted deserialization receipt or distribution permission.
- The starter's quota-filling challenge workflow is not required by this proposal.
- Native scores, external assessment and downstream filtering do not demonstrate
  functional feedback or measured antimicrobial activity/safety.

Saved-only review also verifies that these same 32 generated sequences and their
returned order match the original HydrAMP campaign for the fixed seeds. The
observed lack of a joint Macrel AMP-positive/NonHemo hit in this fixture is
therefore not evidence of a port-specific sequence regression. No additional
legacy or Macrel execution was required; the exact source digest and comparison
are retained in the [execution receipt](../evidence/hydramp_h4_execution.json).
