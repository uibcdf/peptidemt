# Historical HydrAMP comparison: real-score receiving and execution proposal

Status: **proposal v1 prepared for investigator review**, 2026-11-05.
The continuation commissions this source/contract/resource preparation only.
It does not approve this new receiving contract, native inputs or model calls.
Owners: [PeptideMT #32](https://github.com/uibcdf/peptidemt/issues/32) and our
[HydrAMP #3](https://github.com/uibcdf/hydramp/issues/3); reusable provider work
belongs to our [HydrAMP #4](https://github.com/uibcdf/hydramp/issues/4).

## Question and preserved authority

Compare the two implementations' MIC-head discrimination of the historical
reported ATCC 25922 activity, using the endpoint already approved under D47.
This is a finite descriptive comparison, not a test of general equivalence,
native molar calibration, generation quality, safety or prospective efficacy.
It changes no model, threshold, source label, chemistry admission or selector.

The [D47 outcome](hydramp_historical_evaluation.md) has a qualified source
endpoint and synthetic-score comparator. Its 33 selected tests and guarded
statistical controls are reused, not another model campaign. The unchanged
[D46 data receiver](hydramp_historical_data.md) remains authoritative for the
source. D35/M1–M8 and D41/D44/D45/D46/D47 persist. Every earlier model allowance
is exhausted; none is transferable to this proposal.

Retain all **42 observations / 39 literal-string groups**, including chemical
annotations, unknowns, repeated measurements and censoring. Use **38 stable
groups (12 active / 26 inactive)** for the primary ROC-AUC and both shared-class
39-group ambiguity scenarios. The same Hydraganan-2 class choice applies to
both implementations in each scenario. No 128 µg/mL endpoint is added.
The source groups have declared lengths 11–25; none exceeds the owner's width.
That is a source/codec-compatibility observation, not biological applicability.

## Exact candidate and inspected provider routes

The [preparation receipt](evidence/hydramp_historical_real_preparation.json)
identifies the non-dispatchable local plan, complete artifact/source manifests,
metadata-only environment inventories and observed host. No model package was
imported; model files were hashed as opaque bytes, never deserialized.

| Item | Proposed fixed identity / route |
| --- | --- |
| Original source | `6590d2f4c2963f25d30669052a4c4a857e0e7279`; installed `amp/` files match the retained source manifest |
| Original profile | Retained isolated Python 3.8.20 / TensorFlow 2.2.1 / Keras 2.3.1 / NumPy 1.18.5; 61 distribution metadata records match the earlier qualification |
| Modern candidate | `hydramp-torch==0.0.0.dev6`, wheel SHA-256 `1ceb810546c8efe4736d12f67f34d04a0acb1c61440d4a8dcbf961bdd8de0b2a` |
| Modern profile | Retained isolated R3 generation prefix: Python 3.14.7 / Torch 2.15.0+cpu / NumPy 2.4.6; 21 distribution metadata records match R3 after standard project-name normalization |
| Learned assets | Same retained publisher-attributed epoch-37/starter model, starter `7804df862872ccc6d09fe01c41bafbca194cfa31`; all 59 files / 3,699,734 bytes match the A2 manifest |
| Endpoint | Exact D46 saved snapshot and D47 endpoint, authority and metric-provider pins retained in the local plan |

The dev6 codec is needed for owner-controlled sequence encoding. Its inference,
generation, encoder, prior, analogue and property source modules are byte-equal
to the accepted dev5 wheel; this is source identity, not new dev6 scientific
acceptance. Installed dev6 Python sources also match its exact wheel. The
original commit identifies the reference, not the uncommitted modern port.
Keep the D41 dev3 and D44 dev5 accepted resources distinct from this candidate.

For the original, reuse `amp.data_utils.sequence.to_one_hot` and `pad`, followed
by `load_master_model_components(model_path, softmax=False)[3].predict`.
Index 3 is the original `VeltriAMPClassifier` MIC head. Fix `batch_size` to the
actual request size and `verbose=0`; preserve its native float32 output and
native integer input dtype. The loader reads the full master checkpoint and
builds encoder/decoder/classifier graphs. Encoder/decoder and AMP prediction
calls are prohibited, even though graph/weight construction occurs.

For the modern candidate, reuse public `encode_sequences`, `load_checkpoint`
and `HydrAMPInference.score_tokens`. The codec returns CPU int64 tokens. The
public scoring operation evaluates **both AMP and MIC**, returning AMP first,
MIC second. Retain the AMP values as auxiliary provenance and count their
evaluations; they supply no additional endpoint or AMP-membership claim.
The loader constructs the selected decoder and both heads; the decoder is not
executed. No copied vocabulary, private-layer scoring implementation or new
MIC-only backend is introduced in PeptideMT.

A reusable single-head scoring operation would avoid the extra AMP work; its
need is reported in owner #4. It is a product improvement, not a blocking bug or
permission to implement it here. Adopting a different provider API/bundle later
requires a revised plan and its own qualification; it cannot silently reduce
or repurpose the present budget.

PeptideMT owns only the finite study/receiving policy and orchestration. Reuse
its existing `_hydramp_process` primitives and qualification supervision rather
than copying a new process manager. Verify the aggregate RSS scope explicitly:
monitoring a child tree alone does not account for its controller. Use the
registered DepDigest/SMonitor boundaries for actual optional availability and
diagnostics; do not turn a provider failure into absence or a fallback method.
Preserve offline scientific/software attribution and use public optional
Ackredit capture for completed operations, retaining detached original/modern
producer identities. Saved replay must not claim a new calculation or replace
the application's attribution session. The implementation applicability review
must verify actual support hooks; this static preparation proves no adoption.
No generic persistence, methodology or bibliography framework is introduced.

## Inputs, fixed requests and exact accounting

The reviewed descriptor lists the 39 group IDs in D47 first-source-occurrence
order and maps each to every source occurrence ID. No native array exists yet.
After commissioning, each worker obtains that same approved D46 sequence view
and invokes its owner's codec, preserving the initial M, case and every residue.
No truncation, repair, file parser, unit/mass operation or new chemical identity
is allowed. General molecular/FASTA operations remain MolSysMT's responsibility.

Both native inputs must have shape [39,25], equal integer token values and
canonical post-padding, while retaining their original dtypes separately.
Record the complete native arrays, dtype, shape and value correspondence.
Reject the comparison on a codec/value mismatch. String equality alone cannot
authorize prediction reuse: earlier generated rows can contain internal zeros.
No previous generated score substitutes for these newly specified requests.

Run one original worker followed by one modern worker, each loading its model
once and issuing exactly these requests in the same process:

| Request | Group indices, zero-based | Purpose |
| --- | --- | --- |
| `primary_full` | 0–38, one batch of 39 | Prespecified primary scores, before seeing any outcomes |
| `repeat_full` | 0–38, one batch of 39 | Same-process repeat diagnostic, same order and configuration |
| `split_first` | 0–19, one batch of 20 | Fixed alternate batch context |
| `split_last` | 20–38, one batch of 19 | Complete alternate context, without dropping a group |

Reassemble the two split results in the original group order. Full, repeat and
split contexts each contain one score per group. The 117 scored rows per head
are repeated evaluations of 39 source groups, not additional biological cases.
There are **8 scoring API calls**, **4 original MIC forwards + 4 modern MIC
forwards + 4 unavoidable modern AMP forwards = 12 neural evaluations**.
The total is 351 row/head outputs. Weight loading, graph construction and
statistics are recorded separately; there are no uncounted warm-up predictions.
No extra repeated process, per-sequence probing, alternate ordering, fallback,
retry, refill, generation, encoder/decoder inference or Macrel call is included.

Use inference mode and native FP32 computations. Fix initialization seeds to
431 for reproducible setup; this grants no sampling or latent generation.
The seed is a technical setup choice, not a new scientific parameter. No head
temperature, threshold, coefficient, equation or precision change is proposed.

## Proposed finite learned-score receiving contract

This is a separate developer record, provisionally
`peptidemt.hydramp_historical_learned_comparison@1`. It is not a public package
API, general methodology framework or an accepted schema yet. Do not relabel
learned results as synthetic or weaken the existing artificial-only entry point.

The record must contain:

- Exact D46 source snapshot, D47 endpoint/authority and approved future work
  order/execution authorization, with bytes/digests and every observation link.
- Fixed provider slots, interpreter/distribution/source/wheel/asset identities,
  owner method/head identities and the actual input dtype/shape/token arrays.
- Unmodified raw per-request output records, native dtype/shape, all scores,
  source-order IDs and explicit original/modern/MIC/auxiliary-AMP mapping.
  JSON scalars must round-trip the native float32 values without decimal
  rounding; retain native-output byte identities as well as numeric values.
- Observed parent/worker provenance: actual command/source identities, exit
  status, opened-asset audit, attempted/completed forwards, resources, failures
  and explicit timeouts. A declared model/kind or hash alone is not independent
  authentication of where arbitrary numbers came from. The controlled launcher
  and captured execution evidence are part of the trust boundary.
- All three score contexts and cached descriptive results, excluded-group
  reasons, repeat/batch diagnostics and incomplete/failed-stage records.

Validate complete one-to-one correspondence before metrics. Reject wrong
authority/source/provider/head, foreign/duplicate/reordered/missing groups,
wrong dtype/shape/tokens, nonfinite/out-of-range scores, booleans/coercions or
unexplained forward counts. Never fill missing values or silently reduce the
panel. An incomplete paired context has no AUC; retain its failure and available
raw outputs rather than inventing a successful comparison.

On valid complete primary results, delegate descriptive ROC-AUC to the same
qualified public sklearn provider as D47. Reuse endpoint/scenario validation
and private common metric machinery without a local generic AUC routine.
The synthetic interface and evidence kinds must remain distinct and truthful.
No real output is passed through `evaluate_synthetic`.

`primary_full` always supplies the headline result, even if another context
looks more favorable. Show both ambiguity scenarios and their paired ranges.
Compare repeat outputs bitwise at native precision; a mismatch is a retained
repeat diagnostic failure, not a reason to rerun or choose a different primary.
Finish only the already scheduled calls unless structural/resource guards stop
the worker. Compare primary versus split raw values, exact ties, changed pair
relations, AUC and paired differences for each provider. Batch sensitivity is a
reported property; it does not change the primary context or acceptance bands.

Report original–modern raw score differences and changed rank relations, while
keeping numerical differences separate from historical assay discrimination.
No probability-equality tolerance, hypothesis test, equivalence margin, confidence
interval, model-calibration claim or automatic biological pass/fail is added.
Preserve all previous numerical diagnostic FAILs and independent evidence for
modern improvements; do not modify either implementation to obtain agreement.

Save exclusively to new paths. Embed sufficient source/input/raw-output and
authority/provenance material for autonomous model-free replay, revalidate its
bindings and recompute cached statistics with the qualified provider. Replay
must not import either model, read weights/PCA, reopen former source paths or
invoke processes/network. It is not a new neural experiment or renewed allowance.

## Proposed host and stopping envelope

This is a **budget proposal**, not execution approval. Refresh the shared-host
checks immediately before any model run. The static audit observes a Xeon
E5-2630 v4, 10 physical cores / 20 logical CPUs, 30.68 GiB RAM and 12.79 GiB
available, with 2.29 TiB free on the workspace filesystem. Free swap is below
1 MiB; the budget must not rely on swap. These are dated observations, not a
promise about availability later or an instruction to alter other processes.

- Two model worker processes in total, sequential; at most one child at once.
  Pin each to logical CPUs 0/1; all BLAS/OpenMP/TF/Torch numerical pools and
  intra/inter-op execution are limited to one thread. No GPU is visible or used.
- At most 180 s wall / 120 s CPU per child, 360 s combined model-worker wall
  allowance; no retry. Four original and eight modern neural forwards are hard
  operation caps. No decoder/encoder/PCA/descriptors/training/generation/ONNX.
- Preserve the investigator's **4 GB task RAM intent**. Stop on sampled aggregate
  parent+child RSS above 2 GiB, sampled every 100 ms. Sampling is not an
  instantaneous hard RSS guarantee. The margin includes controller/runtime
  overhead. Per-child address space is capped at 8 GiB; virtual address space
  is not the physical-RAM budget. Stop rather than silently relaxing a cap.
- Require at least 8 GiB available RAM and 2 GiB free workspace space before
  each child. Reserve at most 64 MiB for new outputs/logs and bounded 2 MiB
  JSON input/output records. No asset download, installation or duplicate model
  bundle is needed. Preserve other processes and retained evidence.
- Deny network, arbitrary subprocesses, pickle/PCA/unlisted parameter reads and
  all out-of-plan model operations. Allow only the exact numeric model files
  needed by the pinned loaders. Already installed source/libraries and metadata
  remain distinguished from scientific parameter reads. Preserve guard failures.

The 59-file checkpoint and previous local-research conditions are reused;
original-Drive identity, redistribution/output-use and broader provenance
limitations retain their earlier dispositions. This does not authorize asset,
sequence or package publication, external contact or a new platform claim.

## Review, implementation gates and deliverable

1. Review/approve this finite receiving and native-input contract and commission
   its developer implementation. Current continuation only prepared it.
2. Implement the receiver, guarded owner-codec/worker composition and operator
   using artificial scalar records and instrumented method doubles within that
   commission. No artificial-weight network experiment is requested: reuse the
   qualified unchanged provider source/tests. Retain truthful evidence kinds and
   do not load the real bundle. Add meaningful
   controls for wrong model/head/source/authority, swapped pairing, differing
   native tokens behind an equal string, incomplete contexts, dtype/precision,
   replay/cache tampering, exact ties and favorable-context selection.
3. After those controls, qualify each owner's actual codec once on the 39 source
   views, with every parameter read and neural method blocked. This proposed
   preparation substage permits two sequential codec-only children, zero model
   loads/forwards, with the same per-child/thread/host/RSS limits above and at
   most 360 s total. No extra model allowance is hidden in codec qualification.
   Freeze the **actual implemented** operator/worker/tests and native input
   artifacts, qualify guards/accounting/installed origins without inference,
   and present their exact hashes with this resource/call plan for fresh model
   execution approval. Those implementation/input hashes do not exist yet;
   this proposal cannot be approved or invoked as a ready execution artifact.
4. Only after that exact authorization, run once and retain every outcome.
   Deliver original/modern MIC scores, primary/ambiguity/batch diagnostics,
   source-linked saved replay, resource evidence and a bounded interpretation.

The primary panel is selected and partly overlaps published source pools;
checkpoint-specific fitting/selection exposure remains unresolved. It is not an
independent benchmark. Twelve positives do not meet the broader unapproved C2
minimum, and 312 primary positive–negative pairs are not 312 independent cases.
Keep #3/#32 open for those scientific questions. No training, new family/target,
feedback, scientific acceptance, installation, commit/push/release or third-party
contact is commissioned by this preparation. Retained task evidence belongs to
#3/#32; review by 2026-11-19.
