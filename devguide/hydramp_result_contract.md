# Independent HydrAMP results: approved first contract

Status: **contract approved under D50; data-only implementation commissioned**,
2026-11-05. Provider owner: [HydrAMP #4](https://github.com/uibcdf/hydramp/issues/4);
method-profile dependency: [HydrAMP #2](https://github.com/uibcdf/hydramp/issues/2);
consumer: [PeptideMT #32](https://github.com/uibcdf/peptidemt/issues/32).
This follows the [source baseline](hydramp_product_baseline.md) and
[public dependency qualification](hydramp_public_installation.md).

The investigator explicitly approves the reviewed first block under D50, recorded
in the [authorization](evidence/hydramp_generation_result_authorization.json).
The original proposal SHA-256
`ce32baaa65cdce9a6474f95bac3a65ec5425fd3601bbdeb8f6e8983f4f4ed70b`
is preserved in the authorization's exact local snapshot. Scientific meaning,
ownership, I/O, failures and acceptance below now define the bounded commission
under [D14](design_methodology.md#progression-and-review). API/helper naming and
routine internal technical choices remain delegated. The separate
[implementation and exact installed qualification](hydramp_generation_result_implementation.md)
now complete the first data-only block. The [final source review](hydramp_dev8_source_review.md)
prepares consolidation; no scientific acceptance or Git authorization follows
from this contract.

## Recommendation and first useful case

Add an optional HydrAMP-owned save/read capability for an **already completed
GenerationTrace**, with exact native arrays and detached provenance. A researcher
can retain a result, move it, inspect all occurrences/scores later and check its
identity without loading models or installing PeptideMT. Existing generation
functions keep their signatures and native return values. Saving or reading a
retained result must not rerun generation or credit it as a new calculation.

Start with the existing unfiltered AMP, one-attempt generation route, supporting
both existing native views with and without descriptors. Preserve descriptor
values already present; never calculate them while saving/reading. Analogue and
encoder archives require their own later payload contracts: their parent/attempt
and posterior/underflow semantics do not fit a generation permutation. First-slice
exclusion from persistence does not remove those existing inference capabilities.

A failed/interrupted generation has no completed GenerationTrace to save. Do not
turn it into an empty successful result. A caller's Recorda journal can retain
the actual failure/incomplete operation separately; a future partial-trace
format needs its own contract.

This is a product I/O contract, not an optimization policy, biological acceptance,
new model, family extension or PeptideMT result refactor. M1–M8, Macrel outputs,
both selectors and the exact accepted dev3/dev5 resources remain unchanged.

## Responsibilities and verified source boundaries

| Owner | Responsibility here |
| --- | --- |
| HydrAMP | Native result fields, model vocabulary/projection, occurrence/order correspondence, scientific meanings and validation of its saved result |
| NumPy | Existing NPY/NPZ array representation and loading; no new binary-array codec |
| Recorda | Optional caller-owned operation journal, declared references and local reference checks; no copying its session, resolver or journal implementation |
| Ackredit | Optional detached bibliography/contextual-use payload, validation and rendering through its supported API |
| PeptideMT | Scientific design question, composition, assessment and selection; existing receipts stay consumer-owned |
| MolSysMT | Molecular entities, chemistry, FASTA/general molecular formats and manipulation; native model codes are not molecular systems |
| Praxis / Nextia / MOLI | Their existing execution, Discovery and platform context responsibilities; this file creates no replacement workflow/session/project layer |

Recorda 0.3.3 at
[`ff52fa5d8628d796f413b833c8abe73907990cf9`](https://github.com/uibcdf/recorda/commit/ff52fa5d8628d796f413b833c8abe73907990cf9)
provides `session`/explicit operations, `Reference`, `inspect`,
`LocalFileResolver`, `check_reference` and `check_references`. Its
[reference contract](https://github.com/uibcdf/recorda/blob/ff52fa5d8628d796f413b833c8abe73907990cf9/devguide/REFERENCE_CHECKS.md)
checks declared file bytes, not native manifest semantics, biological validity,
authenticity or replay. An operation can remain succeeded when a later file
check reports missing/mismatched bytes; preserve both observations.

Ackredit's inspected editable source is
[`74f865d7eca1f5386235885d4ea001e53b5b822d`](https://github.com/uibcdf/ackredit/commit/74f865d7eca1f5386235885d4ea001e53b5b822d),
installed metadata `0.12.0+11.g74f865d`. It is fifteen commits behind fetched
main; the current guide recommends public 0.12.1. Do not relabel this checkout
as that release or update the shared environment for a design probe. The
[portable contract](https://github.com/uibcdf/ackredit/blob/74f865d7eca1f5386235885d4ea001e53b5b822d/docs/content/user_guide/portable_attribution.md)
uses `capture`, `Attribution.from_dict`/`to_dict` and `report`, with feature floor
0.9.0. Application-owned sessions and detached saved attribution remain distinct
from actual scientific execution and client adoption.

HydrAMP source is the local, unpublished commit
`a77baff9de97e8ab4ae101b9b0c79122dea22ce3`. Its `GenerationTrace` has five
NumPy arrays plus seed, projected sequences, native results and returned indices.
`AnalogueTrace` additionally preserves all attempted rows and several exclusion
flags; `EncoderPosterior` uses mean/raw log-variance tensors. Their existing
docstrings explicitly decline a portable-schema claim.

The [review receipt](evidence/hydramp_result_contract_review.json) pins the exact
provider source files. No missing Recorda or Ackredit API is established by this
review. A later demonstrated reusable gap goes to its owner before a workaround.

## Proposed scientific payload

| Content | First-contract obligation |
| --- | --- |
| Schema and kind | An explicit versioned HydrAMP generation-result identity; unknown versions/kinds are refused rather than guessed |
| Native row identity | All N input occurrences, including duplicates; stable row indices local to this result, never string-based deduplication |
| `returned_input_indices` | Preserve the native permutation; returned position k refers to input row at that index |
| `tokens` | Original integer array `[N,25]`, values 0..20, preserving every zero position |
| `sequences` | Exact projected strings in input order, including empty strings; not evidence of realized molecular chemistry |
| `amp`, `mic` | Exact original FP32 arrays `[N]`, finite native dimensionless scores in 0..1; no new calibration claim; MIC-head output is a class score, not a measured MIC or a concentration |
| Latent trace | Original sampled latent `[N,64]` and conditioned `[N,66]` arrays, preserving their actual dtype/values |
| Native return view | Exact strings or descriptor-bearing rows in native returned order; preserve existing Python numeric values and descriptor omissions |
| Configuration | Original seed and supported route settings, distinguishing values derived from the trace from caller declarations and unknowns |
| Implementation/profile | Original producer version/source and provider-owned descriptive profile; actual selected descriptor backend/settings when present |
| Export/inspection software | Record current writer/reader identity separately; never replace the original scientific producer with the software that later saved or read its result |
| Resources | Available model/PCA/input/environment identities or explicit unknowns; a caller declaration is not an observed execution attestation |
| Attribution | Detached existing Ackredit payload when available, plus an explicit recorded/not-recorded/unavailable/failed state; no invented credits |

Native projection omits **all** zeros, including internal zeros. It cannot
recover token locations from a string. Head scores were computed on the original
tokens, so padding/projected-string reconstruction must never replace them.
Cross-field checks reuse the provider's own vocabulary operation. No FASTA
parser, molecular admission rule or terminal-state inference is introduced.

Descriptor assumptions remain method settings, not assigned peptide chemistry.
The pure-data profile need already belongs to #2. It must describe actual
selected settings or explicitly unknown/custom settings rather than importing a
second consumer-authored defaults table. Definitions and profile expectations
must be checked against the delegated calls without evaluating descriptors.

A manually constructed trace and a valid file cannot prove that a neural call
occurred, that resources were permitted or that a reported source produced it.
Missing history must remain missing. This first commission can qualify artificial
save/read behavior; it cannot retroactively manufacture live provenance.

## Proposed storage and independent reading

Recommend **one uncompressed NPZ file**, containing the five native numeric
arrays and a UTF-8 JSON manifest stored as a uint8 array. The manifest carries
the remaining domain fields and optional detached metadata. Use NumPy's
[supported array loader](https://numpy.org/doc/2.4/reference/generated/numpy.load.html)
with pickle disabled. This is a proposed HydrAMP format, not a new generic
serializer or a renamed PeptideMT receipt.

JSON-only storage is possible, but would need explicit dtype/shape/byte-order
conventions for arrays. NPZ reuses the current NumPy dependency and preserves
those properties directly. A directory of sidecars creates multiple artifact
identities to retain/check; a single file gives Recorda one exact reference.
HDF5 or a general artifact service adds dependencies without a demonstrated
need for these five finite arrays.

Recommended first transport bounds: 64 MiB total file and expanded payload,
1 MiB manifest, the six known archive members only, uncompressed entries and
bounded NPY headers. The reader rejects duplicate member/JSON keys, unknown
schema structure, object/structured arrays, inconsistent dtype/shape/row maps,
nonfinite scientific fields and malformed native projections. These are format
bounds, not a new generator batch/chemistry policy. Use supported NumPy, zipfile
and JSON operations; never extract paths, unpickle, evaluate code, fetch assets
or reconstruct a neural object.

The saved archive preserves array element bytes, shapes and dtypes, including
signed zeros. It need not have identical ZIP timestamps/whole-file bytes after
a new export. A retained artifact has its own exact digest. Snapshot caller data
without mutation; do not promise safety against concurrent caller mutation.
Destination collisions and I/O errors propagate; incomplete writes are never
returned as completed results. Do not overwrite an existing result by default.

Read/inspect returns detached data and explicit validation/provenance states.
It uses no model backend, descriptor calculation or scientific recomputation.
NumPy remains required; Torch import must not be needed by the data reader.
The current eager `hydramp_torch.__init__` and `inference.translate_tokens`
prevent that today. A future implementation needs a controlled lazy-import/light
vocabulary refactor with the existing exports and projection behavior preserved,
not a copied alphabet/decoder or a false Torch-free installation claim.

Recorda checks external declared identity through its supported reference API;
HydrAMP checks its own native structure. An absent trusted reference leaves
origin unverified. Byte matching is not authenticity or biological validation.
No new generic resolver, journal format, replay engine or integrity service is
part of this proposal.

Restoring saved values is data recovery, not computational replay. A seed alone
does not promise the same generation under another implementation, dependency
profile or set of model/PCA assets.

## Optional recording and attribution

The core save/read path works without Recorda or Ackredit imports. An explicit
caller integration can record saving as saving, and inspection as inspection,
using Recorda references to the result file. It must not log a replayed result as
a new generation. Sessions, activation, retention and host resource authority
stay with the caller; libraries create no isolated session automatically.

Recorda's source deliberately omits fields whose names contain `token` before
reference adaptation. Use a result-file reference at the declared boundary,
not raw arrays in a field named `tokens`. This is a reviewed policy observation,
not a provider bug or a reason to weaken credential protection.

Preserve an existing attribution through Ackredit's public detached reader when
explicitly requested. Core inspection may retain the opaque saved JSON block
without Ackredit, but must label it unvalidated; it must not render or claim to
validate another component's schema. Unknown/invalid attribution is diagnosed
by Ackredit at that boundary and does not turn otherwise recoverable scientific
data into a successful citation claim. Provider absence/failure is explicit.
No new credit is recorded by reading, writing or rendering retained science.

Adding attribution to future live HydrAMP execution is separate from this
data-only slice. That later boundary must credit only reached branches and
qualify genuine absence, provider failure, reused references and enclosing
caller sessions. Do not silently copy PeptideMT's attribution implementation.

## Proposed implementation order and acceptance

1. **Owner method profile and light data boundary (#2/#4).** Define the selected
   descriptive profile without changing defaults/chemistry; preserve current
   public inference APIs while enabling a reader that does not import Torch.
2. **Generation save/read (#4).** Add the exact domain payload, bounded native
   NPZ/JSON storage and independent inspector. Existing native results remain
   unchanged. Retain the accepted bundles and dev7 source/artifacts separately.
3. **Optional saved-result integrations (#4/#32).** Demonstrate Recorda file
   references and existing detached Ackredit metadata with caller activation,
   synthetic fixtures and fresh reader processes. No live science runs follow.

Completion requires exact round trips for all five arrays and native views;
input/return order, duplicates, empty projected strings and descriptor values;
rejection of malformed/unknown/oversized files and destination collisions;
no mutation of caller data or global RNG; fresh reading with Torch/model imports,
network and learned-asset access blocked; explicit unknown provenance; and real
optional-provider tests for absence/failure, reference changes and no new credit.
Reuse relevant owner tests; do not rerun trained campaigns for serialization.
Source/import refactors produce a new separately identified candidate and require
focused regressions; numerical acceptance is not silently inherited by a new wheel.

Concrete Python API names/classes, small helper layout and diagnostic wording
remain implementation choices after this contract is agreed. No generic framework,
CLI, old-receipt migration, training, feedback, target/family change, release,
Git commit/push or author contact is commissioned by this proposal.

## Evidence and current limits of this review

This subsection retains the original pre-approval review checkpoint. The later
[D50 implementation record](hydramp_generation_result_implementation.md)
separates historical precursor checks from the completed final qualification.

Static owner/provider review establishes supported responsibilities and the eager
import/vocabulary issue. A small NumPy 2.4.6 probe in the already qualified public
dependency environment preserves six synthetic arrays' dtypes/shapes/element
bytes, signed zeros, nearby FP32/FP64 values and endianness, with pickle disabled.
It completes in 1.69 s /61,755,392 bytes aggregate RSS (about 59 MiB), without
Torch, HydrAMP, models or an implemented HydrAMP schema. It qualifies the storage
primitive only, not this proposed result contract.

The initial Recorda/Ackredit mechanism probe does not start because the shared
host resource guard refuses it. A later reading below the conservative 9 GiB
retry-start threshold defers the retry; no combined provider execution/pass is
claimed. The supported APIs above are source/contract observations. Actual
consumer integration tests remain required before adoption. Earlier successful
codec/scientific evidence is retained, not rerun or repurposed.

The [review receipt](evidence/hydramp_result_contract_review.json),
[closeout](evidence/hydramp_result_contract_review_closeout.json) and
[owning issue updates](evidence/hydramp_result_contract_issue_updates.json)
preserve source identities, guarded attempts, the primitive experiment and
proposal status. Raw evidence is in
`local_data/hydramp-result-contract-yfjr66jh`, owned by #4/#2/#32, with retention
review on 2026-11-19. No provider runtime/lock/environment changes, learned reads,
neural evaluations, GPU, public package release or external contact occur.
