(hydramp-execution)=
# Isolated HydrAMP generation

{func}`peptidemt.generate_hydramp` implements one provisional installed-Python
access route to the modern HydrAMP AMP generator. The scientific calculations
remain in the provider. The adapter and its attribution/transport controls have
installed tests with artificial providers. A separately approved real-checkpoint
case now passes for the exact local Linux CPU bundle: 16 proposals at seed 1001
match retained native results, order, indices and full trace exactly, saved replay
is exact, and parent-session attribution is captured. This finite adapter proof
supports the investigator's D41 acceptance of this exact resource for experimental
AMP generation. Biological validity, general equivalence and other-family
capability remain unestablished. Earlier private qualification and scientific
limitations are recorded separately.

## Before requesting a run

Review the exact implementation, checkpoint/PCA, dependency profile and permitted
use. Agree the host and call limits with its maintainer. Constructing configuration
objects is not approval to execute a model. No package, model or asset is installed
or downloaded automatically. The earlier qualification call allowances are exhausted.

The explicit worker interpreter must contain this same PeptideMT implementation
and version, the pinned installed `hydramp-torch` distribution, NumPy, CPU-only
Torch and the selected modlAMP 4.3.3 profile. A separate interpreter keeps those
dependencies out of the host's ordinary data/selection imports. The caller supplies
an absolute interpreter path; it is not resolved to a base Python or replaced
with another environment.

{class}`peptidemt.HydrAMPBundle` identifies absolute checkpoint/PCA paths,
relative-path SHA-256 manifests, installed provider source hashes, exact runtime
versions, original source/starter commits and a use-condition reference. Its
identifier is independent of the artifact directory. Paths do not grant permission
to use arbitrary artifacts, and a qualification reference does not certify them.
Before provider import/model loading, the worker checks identities and rejects
changed files, shadowed providers or an incompatible runtime.

{class}`peptidemt.HydrAMPLimits` requires the requested count ceiling, wall time,
virtual address-space ceiling, sampled process-tree RSS stop, output byte ceiling
and CPU affinity. Numerical threads, lowered priority, host available-memory and
free-disk floors remain explicit. Defaults do not replace authorization. The
current route is synchronous Linux CPU; requesting it elsewhere returns a
structured unsupported-host failure. Saved-data APIs remain independent.

## One batch, then separate assessment

```python
from peptidemt import HydrAMPBundle, HydrAMPLimits, generate_hydramp

# These fields and host limits must describe the reviewed, authorized operation.
bundle = HydrAMPBundle(**reviewed_bundle_fields)
limits = HydrAMPLimits(
    **{**authorized_limit_fields, "cpu_ids": tuple(authorized_limit_fields["cpu_ids"])}
)
receipt = generate_hydramp(
    n_target=16,
    seed=1001,
    snapshot_id="my-generation-snapshot",
    bundle=bundle,
    limits=limits,
    worker_python=worker_python,
    qualification_reference=None,
)
```

This is a real-generation example when supplied with valid configurations and
run by a caller. Documentation builds display it without execution. Each call
attempts one unfiltered AMP batch with `properties=True`, `n_attempts=1` and the
explicit seed. One successful call reaches one decoder and both native heads,
one descriptor bundle and one numeric PCA inverse transform. Numeric PCA loading
uses `allow_pickle=False`; the adapter delegates checkpoint loading and scientific
operations to the provider. It does not call legacy TensorFlow, refill, deduplicate,
change precision or silently retry.

The returned {class}`peptidemt.HydrAMPReceipt` retains every native occurrence and
original order/mapping, scores/descriptors, tokens including zeros, latent/PCA
evidence, actual FP32 decoder input and distinct FP64 conditioning. Unknown
chemistry remains unknown. Inspect `completed`, `failures`, `issues` and
`provenance.details` before composing `receipt.inputs` with the separately
qualified Macrel route described in {ref}`hydramp-results`.

The original descriptor definitions remain with HydrAMP: Eisenberg scale,
moment window 1000/angle 100/max, charge at pH 7 with amide=True and pI with
amide=False. These method conventions do not establish molecular termini.
The provider-owned metadata capability proposed in
[HydrAMP #2](https://github.com/uibcdf/hydramp/issues/2) would make those definitions
directly consumable. Until then, provenance identifies the exact provider and
worker code defining them; the consumer adds no second computational formula.

## Failures, resources and attribution

The parent supervises the worker tree, time, output size and available host RAM.
The child applies affinity, lowered priority, numerical-thread controls and
`RLIMIT_AS` before provider imports. Address space is virtual memory; sampled
RSS and a RAM-budget intent are not hard kernel resident-memory reservations.
The caller's inherited hard address-space ceiling must permit the requested
worker ceiling. A qualifier using a lower parent limit must lower the parent's
soft limit while retaining a sufficient hard ceiling for the child; the adapter
does not raise a caller's hard limit or bypass the operating-system restriction.
The worker uses an owned process group. Ordinary failure, timeout and caller
interruption clean that group; parent-death handling is registered in the worker
and has model-free process tests. No parent signal handler is replaced. Private
temporary transport/cache files are removed after normal result receiving.

Import/model/PCA/generation/descriptor/output failures remain distinguishable.
Incomplete or failed output is not a negative prediction; the receipt retains
reported failure and confirmed completed operations. Malformed or mismatched
receipts cannot replace the requested snapshot, seed, count or bundle identity.
SMonitor reports operational diagnostics. DepDigest guards only the requested
worker backend; unqualified PyPI/Conda installer routes are disabled. There is
no alternate method or environment fallback.

Confirmed child operations contribute optional Ackredit >=0.9.0 capture in the
**application's parent session**, with detached bibliography and original software
versions retained in the receipt. The original HydrAMP implementation is a
reference; TensorFlow is not an executed dependency of this route. The method
paper, modern implementation, NumPy, Torch and modlAMP are credited only for
branches actually confirmed. Partial failure does not claim a complete generation;
an unfinished descriptor branch does not receive completed-descriptor credit.
Missing or broken optional attribution preserves scientific results and offline
references. Reading the saved receipt creates no new execution credit.
Use distinct `snapshot_id` values for distinct operations; saved replay keeps
the original identifier.

Functional execution and computational classification do not establish biological
activity, safety or broad generator quality. The earlier 32-proposal sample had
no generated Macrel AMP-positive/NonHemo hit, and its sequences/order matched the
original at those seeds. Both existing selectors preserve their approved meanings.
This API adds no feedback, target conditioning, other family/model, training or
publication authority.
