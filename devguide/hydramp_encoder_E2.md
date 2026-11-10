# HydrAMP encoder E2: prospective real-weight comparison

Status: **separately approved execution completed; prospective numerical
comparison PASS**,
2026-11-04. Owner: [HydrAMP #8](https://github.com/uibcdf/hydramp/issues/8).
Consumer: [PeptideMT #32](https://github.com/uibcdf/peptidemt/issues/32).
This follows the [D42/E1 artificial implementation](hydramp_encoder_E1.md).
There is no new scientific acceptance or implicit extension of D41.
The maintained owner record is `devguide/pytorch_encoder_E2.md` in
`../hydramp/local_data/pytorch-encoder`.

## Executed outcome — 2026-11-04

The investigator explicitly directs continuing in response to the exact
execution approval question. The [authorization](evidence/hydramp_encoder_E2_authorization.json)
binds that permission to unchanged plan
`eb6d30fc31217dee57c9200fcfcff982ebbee0facb12fdeff3b6f9da3b92692b`.
The [execution evidence](evidence/hydramp_encoder_E2_execution.json) retains
both native worker exits, every saved output, original report exit **0**, exact
hashes and host/resource observations. Earlier proposed sections below retain
their pre-execution scope; frozen copies preserve their original bytes.

Both workers completed all **five evaluations each**, with no retry/resource
stop: 32 distinct token rows, 36 baseline occurrences and 144 submitted
occurrences per implementation after repeats/layout controls. These are not
144 independent inputs. Both raw posterior outputs and intermediate states
pass the prospectively approved `atol=2e-6, rtol=2e-5` across every saved case.

| Field | Maximum absolute original/modern difference across all cases |
| --- | ---: |
| Mean | 1.9073486328125e-6 |
| Raw log-variance | 3.814697265625e-6 |
| First bidirectional sequence | 2.682209014892578e-7 |
| Final second-layer state | 5.587935447692871e-7 |

There are **zero elements outside the combined absolute/relative band**.
The log-variance maximum exceeds the absolute floor alone and passes the
declared combined criterion; it is not bitwise cross-implementation equality.
Within each implementation, repeat values are exactly equal and permutation,
partition and duplicate comparisons have **zero numerical difference** in
these cases. Exact repeat here means equality of the retained numerical values;
the JSON comparison is not a signed-zero bit-pattern diagnostic.

Each worker opens exactly 23 distinct selected model files and deserializes
the seventeen encoder arrays. The legacy log has 24 open audit events because
the master JSON appears twice; Python3.8's `Path.open` uses an additional opener
hook. This is not an extra parameter/model evaluation. No unrelated scientific
artifact/PCA is opened or predictive classifier/decoder/descriptor/Macrel run.
Native construction draws exactly the allowed one unused eager64 epsilon vector;
the actual selected executable and all its function bodies have no random
operations and keep the same identity across calls. Modern calls preserve
NumPy and Torch RNG state. Native initializer work remains disclosed.

| Whole supervised worker | Original | Modern |
| --- | ---: | ---: |
| Wall seconds | 4.6412 | 3.4860 |
| Peak sampled process-tree RSS | 367.45 MiB | 272.75 MiB |

Total supervised time is **8.1271 seconds**, maximum retained run output
**41,347,047 bytes**, under all approved limits. No GPU computation or retry
occurs. These are single shared-host instrumented observations including
startup/output work, not a general speed/memory benchmark.

**The ten-evaluation allowance is exhausted.** This establishes finite
pretrained deterministic encoder fidelity for this exact bundle/fixture; it
does not establish arbitrary-input equivalence, biological superiority,
analogue generation, training or scientific adoption of dev4. Accepted dev3,
consumer artifacts, D35/M1–M8/selectors and all earlier unfavorable numerical
evidence are unchanged. #8/#32 remain open for investigator disposition and
later independently commissioned modules. No new model call, commit/push,
package publication or author contact follows.

## Frozen preparation — before approval and execution

## Exact proposal

Plan SHA-256:
`eb6d30fc31217dee57c9200fcfcff982ebbee0facb12fdeff3b6f9da3b92692b`.
Local plan: `local_data/hydramp-encoder-E2-prep-7y8qhl7j/plan.json`.
The [preparation evidence](evidence/hydramp_encoder_E2_preparation.json) pins the
plan, executable instrument, installed sources/metadata, fixture, audit and
artificial qualification. The plan digest binds inputs, not human permission.
No real-run authorization file or model attempt is created in preparation.

Candidate: unchanged installed `hydramp-torch==0.0.0.dev4`, wheel SHA-256
`01fe4e125eca5decdca89f43e8925e8e969d3453b7a4da701be8e96e5e18dbe0`.
Python 3.14.7, Torch 2.15.0+cpu, NumPy 2.4.6; the E1 borrowed-payload prefix
has 41 distributions. This is not a new clean solver/public installer claim.

Reference: the retained Python 3.8.20 / TF 2.2.1 / Keras 2.3.1 / NumPy 1.18.5
prefix, 61 distributions and 41 original installed source files. Preserve its
eight known native dependency-metadata discrepancies and the separately reviewed
effective inference profile. E2 changes neither stack nor their dependencies.

Use only the selected **23 encoder files: six JSON and seventeen numeric NPY**,
2,032,384 bytes, from official starter
`7804df862872ccc6d09fe01c41bafbca194cfa31`, original code
`6590d2f4c2963f25d30669052a4c4a857e0e7279`. Current byte-only preflight matches
the retained [asset receipt](evidence/hydramp_reference_assets.json). Real
parameter bytes are rehashed here, never deserialized into a numerical array.
Full original Drive-archive byte parity remains unverified. Preserve the
University of Warsaw MIT notices, publisher epoch-37 provenance and method
attribution. The [existing local-use review](hydramp_environment_review.md#exact-inputs-and-local-use-review)
applies: bounded local research, no new acquisition/training data, redistribution,
commercial/output-rights clearance or model publication.

## Ordered fixture and counted work

Fixture SHA-256:
`7dfd8672aeb359958bdbe04d6e2a3bbfc3e18d60ffe90675989ecaad8e024f3c`.
It fixes **32 distinct original-token rows and 36 occurrences**, each 25 int64
positions in 0..20. Twenty homopolymer controls, post-zero length controls
0/1/2/7/19/20/21/24/25, reverse, gapped and asymmetric controls exercise the
selected numerical boundary. Four rows repeat at the end. These are synthetic
structural inputs, including an all-zero out-of-biological-domain control;
they are not a sampled natural-peptide population or efficacy benchmark.
No molecular parser/realization, FASTA codec or chemistry change is introduced.

Each worker constructs its encoder once and performs exactly:

| Evaluation | Rows | Purpose |
| --- | ---: | --- |
| full | 36 | Ordered baseline and four duplicate occurrences |
| repeat | 36 | Identical-input exact repeat |
| permuted | 36 | Complete reverse occurrence order |
| left | 18 | First partition |
| right | 18 | Second partition |

Total: **10 encoder evaluations**, 144 submitted occurrences per implementation
(288 paired-worker submissions), not 288 independent inputs. Mean and raw
log-variance are fetched together; first bidirectional sequence/final second
state are tapped in those same evaluations. The two posterior projections and
intermediate taps are not extra network calls. No decoder, AMP/MIC classifier,
PCA, descriptor, Macrel or analogue evaluation is proposed.

The reference loads only its selected layers with the unmodified original
per-layer loader and `AMPEncoder.output_tensor`. It retains native Keras2.3/TF2
eager variables and symbolic execution, rather than forcing TF1 graph mode or
constructing the full master/generator.

**Construction is not RNG-pure:** Keras's non-symbolic `random_normal((64,))`
uses `init_scope` and immediately draws one unused epsilon vector. Propose
exactly **one 64-value construction noise draw in the legacy worker** and no
sampled latent `z` fetch. Native layer initializer RNG/SVD also occurs before
all seventeen saved arrays replace the initialized weights. Both belong to
the one model construction, not hidden encoder evaluations. The instrument
observes the original normal call without changing its output, then restores
the function. It verifies that selected endpoints do not reach the sampled
branch and that the actual pruned executable, including function bodies,
contains no random operation. That executable identity is checked before each
call. This is executable-graph exclusion, not a separate runtime profiler trace
or a claim that reference construction never consumes RNG. Modern encoder
calls must preserve both NumPy and Torch RNG state.

## Prospective numerical decision rule

Propose `abs(modern - original) <= 2e-6 + 2e-5 * abs(original)` elementwise for
both raw posterior outputs and the retained intermediate states. It is a new
encoder proposal made before observing real outputs: the strict FP32 diagnostic
scale is small in the original coordinates and detects deviations near zero
through an absolute floor. It does not follow automatically from E1's bounded
artificial weights or establish biological equivalence. Recurrent accumulation
and cancellation with trained weights may fail it; report failures without
widening the band or changing the implementation to mimic weaker arithmetic.

Require finite FP32 shapes, exact occurrence mappings, exact identical-batch
repeats, and the same declared band for permutation/partition/duplicate numerical
comparisons within each implementation. Report count over band, maximum absolute
and RMS errors separately by endpoint/stage/case. A failure prevents claiming
parity; retain all outputs and prepare a separately justified diagnostic if
needed. A pass supports only this finite deterministic encoder boundary, not
scientific adoption, posterior sampling, analogue quality or biological activity.

## Shared-host envelope proposed for approval

Two **sequential** scientific workers; CPU 0/1, one numerical/inter-op thread,
nice 10, no GPU computation or subprocess commands. Maximum **120 seconds each,
240 seconds total**, no retry. Retain the **4 GB task RAM intent**, with a
**2 GiB sampled aggregate process-tree RSS stop** and **8 GiB virtual-address
ceiling per worker**. The latter is address space, not physical RAM allocation.
The existing qualified process supervisor handles process-group cleanup and
parent-death protection; the provider gains no PeptideMT runtime dependency.

Before and during each worker, require at least **8 GiB available host RAM**;
require at least **1 GiB free task disk** before startup and cap retained run
output at **128 MiB**. The sampled stop is not a kernel RAM reservation.
Reference failure/resource stop prevents modern startup. Each attempt reserves
an exclusive marker; no automatic replacement/retry follows. CPU/threads/address
bounds apply before scientific imports. Existing code may probe CUDA drivers;
that does not authorize GPU computation.

Current host: Xeon E5-2630 v4, 10 physical cores/20 threads, 30.7 GiB total RAM,
about 15.4 GiB available during preparation and 2.52 TB free on the task volume.
These are observations, not a reservation; floors are checked again at execution.
Temporary scientific output uses the task disk, not the shared `/tmp` tmpfs.

## Instrument qualification and remaining authority

**Eight model-free instrument tests pass** with published Receptor 1.2.2/native
JUnit: strict numerical failures, malformed/nonfinite values, occurrence mapping,
saved-output integrity, no eager framework import, artifact/command/network guards.
The network guard test invokes its audit event, creating no socket.

The final instrument also completes **five artificial encoder evaluations per
worker**, using retained E1 toy arrays with actual configuration text. Both
endpoints/intermediates, repeats and layouts pass. Final original/modern workers
take about 4.03/3.13 seconds and 361.4/268.1 MiB sampled RSS; this does not benchmark
real weights. The observed legacy constructor draws exactly one unused eager
64-vector, while its executable has no random operations.

Preserve initial instrument failures: missing child traceback, an over-strict
command hook interfering with Python3.8's optional `uname` probe, incompatible
forced graph mode, and integer learning-phase override. Fixes affect only this
diagnostic; native providers remain untouched. The successful preliminary
artificial case is retained separately from the final accounting-instrumented
case. An initial model-free test also encountered the host's socket-creation
restriction; its correction tests the actual audit event directly. This is
instrument development, not a sequence of failed pretrained runs.

D42 permits artificial preparation; [root instructions](../AGENTS.md) require
separate exact-bundle and fresh host/call approval before E2. Ask for approval
of this plan's criteria, ten evaluations, one legacy construction epsilon draw
and resource limits. No approval is inferred from preparing or posting it.
Accepted dev3/consumer artifacts, D35/M1–M8 and selectors remain unchanged.
No analogue, training, filter fix, other family, release, commit/push or original
author contact is commissioned. Retain preparation resources through 2026-11-14.
