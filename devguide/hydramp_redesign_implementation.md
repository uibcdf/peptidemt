# Analogue consumer R1/R2: implemented and artificially qualified

Status: **R1/R2 delivered locally under D45; exact real R3 technical case completed**,
2026-11-04. Owner: [PeptideMT #32](https://github.com/uibcdf/peptidemt/issues/32);
provider: [HydrAMP #4](https://github.com/uibcdf/hydramp/issues/4).
The [authorization](evidence/hydramp_redesign_authorization.json) binds the
reviewed [contract](hydramp_redesign_work_order.md), original SHA-256
`876ef80c5629dc74cf9e541bcf5f1d257ed37f28a0148f5e435a738c8a47fd71`.
The exact original bytes remain in the task's authorized_work_order.md.
The [delivery receipt](evidence/hydramp_redesign_R1R2.json) pins code, wheels,
profiles, tests, saved data, development failures and observed resources.

## Delivered behavior and ownership

PeptideMT exports HydrAMPAnalogueReceipt, AnalogueParentOutcome, AnalogueLink and
analogue_input_issues without importing scientific engines. The separate
redesign_hydramp route and HydrAMPAnalogueBundle load lazily. Callers can inspect
all parents, native trace and failures, extract returned proposal occurrences,
then explicitly use the existing assess_macrel and select operations.

HydrAMP owns the new **encode_sequences** public native vocabulary operation,
delivered only in separate `hydramp-torch==0.0.0.dev6`. It returns CPU int64
[N,25], preserves initial M, order and duplicates, pads after the sequence and
rejects unsupported/empty/overlength views before tensor allocation. It neither
interprets FASTA nor realizes chemistry. MolSysMT's existing source-preserving
file transport is unchanged. Seven dev5 numerical/runtime modules are
byte-identical; only the new codec, exports and candidate metadata change.
Accepted dev3/dev4/dev5 and the original `amp/`/licence are preserved.

The consumer keeps operation-specific admission, one compatible batch, explicit
dense-provider/original-parent/attempt/raw-row mappings and all no-hit/failure
states. It checks exact native joint decisions, lexical buckets and the first
accepted attempt before extracting proposals. Equal child strings across parents
remain separate. Generated views inherit no parent chemistry or measured data.
Empty/initial-M views remain explicit exclusions at the unchanged Macrel boundary.

An analogue-specific, content-bound JSON envelope preserves detached data and
rechecks receiving on replay. Digests establish consistency, not authentication.
Qualification-reference labels do not prove execution or upgrade controlled
evidence. The de novo receipt and its JSON contract are unchanged. Extraction
from incomplete or inconsistent evidence fails conservatively; the raw data and
known/unknown execution progress remain inspectable.

The isolated worker calls the provider's supported codec, encoder/core loaders
and analogue composer. It reuses source/artifact/version checks and process
supervision, without requiring PCA or modlAMP. Reservations precede dispatch:
two encoder evaluations, one decoder and four native head evaluations per call.
Partial progress is retained without retries/refill. Sampling completion is
confirmed after the trace returns; interrupted internal sampling can remain
unknown. A paired-head call reserves two evaluations; both are confirmed only
when that call returns. An interrupted pair can therefore contain unobserved
internal progress, and its reserved allowance is not reusable. Parent-side
Ackredit capture credits only observed completed branches,
with offline bibliography retained on absence/failure. No Recorda journal or
Praxis methodology framework is reimplemented or added as a dependency.

## Exact local artifacts and verification

| Artifact | SHA-256 |
| --- | --- |
| HydrAMP dev6 wheel | `1ceb810546c8efe4736d12f67f34d04a0acb1c61440d4a8dcbf961bdd8de0b2a` |
| PeptideMT controlled local wheel | `9104ad927b1cb113e98a72063193fc2d309ceb3a109900d3a6e02ea2882a437b` |

The PeptideMT wheel identifies itself as **0.1.0+unknown**, the declared
versioningit fallback for a build-source copy without Git metadata. It is an
unpublished local qualification artifact, not a port commit or release version.
Its installed Python source matches the current source exactly. The provider
worktree is `../hydramp/local_data/pytorch-redesign`, original Git base
6590d2f4c2963f25d30669052a4c4a857e0e7279; that base does not identify new code.
Host and worker must have matching PeptideMT source **and installed version**.
The controlled unknown-version wheel is qualified with its matching installed
caller, not directly with the unchanged shared editable metadata. R3 must freeze
a matching host/worker pair; do not relax identity checks or rewrite the shared
environment to hide that difference.

- **259 source tests pass** on the shared Python 3.14.7 profile, including a real
  Ackredit capture with controlled completion state. No learned model/Macrel runs.
- **101 installed tests pass** in the isolated prefix: 17 provider codec cases
  and 84 consumer receiving/worker/control cases. Wheel contents/import origins
  and source identity are verified. Published Pytest Receptor 1.2.2 is used.
- Offline installation and **uv pip check pass for all 21 distributions** in the
  minimal profile, Python 3.14.7/NumPy 2.4.6/Torch 2.15.0+cpu,
  DepDigest 0.15.1/SMonitor 0.22.0. modlAMP, scikit-learn, joblib, Macrel and
  Ackredit are absent; no PCA artifact is loaded. Dependency payload reuse with
  faithful metadata is qualification
  preparation, not a newly qualified public installer or console-script route.
- An additional installed codec probe passes with PeptideMT/DepDigest/SMonitor
  imports and all parameter reads blocked, confirming the owner's independent
  operation. This performs zero network/model evaluations.
- One direct provider call, one installed adapter call and its repeat perform
  **21 original-shaped network evaluations on artificial arrays**, not pretrained
  parameters. Complete native traces and ancestry match exactly. Three nonempty
  repeated-parent candidate occurrences survive, with one distinct string and
  explicit distinct noise/attempt relationships. Artificial Macrel-shaped data
  exercise both unchanged selectors and the saved replay example; no Macrel is run.

The fake parameter fixture reuses the explicitly declared A2 artificial arrays,
not the learned checkpoint. Guards block parameter files outside that root,
network, GPU and unrelated scientific providers. CPU 0/1, one numerical/inter-op
thread, nice 10, 2 GiB sampled tree-RSS stop, 8 GiB virtual ceiling and 8 GiB host
headroom floor are used. Both supervised phases remain below **547 MiB** sampled
tree RSS; combined wall time is about **12.93 seconds**, including tests/setup.
These unlike work phases are not a speed benchmark. Source/installed tests and
artificial execution establish engineering/contract behavior, not biology.

## Retained development failures and their causes

1. The first new attribution-failure test expected a nonexistent `failure` key.
   The existing contract uses status/failure_type; correcting the test preserves
   production behavior. Its initial 81-pass/one-failure log is retained.
2. A new regression reproduced rejection of integer temperature=1 after native
   conversion to 1.0. The receipt now uses the native float argument semantics;
   the before/after test and initial wheel are retained. No model math changes.
3. The initial full source suite has 257 passes/one failure: an older Macrel
   test still expected w2_macrel.md although the existing dependency guide had
   moved to optional_engine_review.md. The failure reproduces alone. Only the
   stale test expectation changes; DepDigest and scientific components do not.
4. All 101 installed tests and the direct/first adapter calculations complete,
   but the initial driver then rejects an attribution status. Its qualification-
   only MetaPathFinder erroneously raises when checking an **absent** Ackredit.
   The isolated availability probe identifies the cause. Correcting the guard
   restores normal absence without weakening parameter-file/network controls.
   Completed tests/direct/adapter work are reused; only the pending repeat and
   composition/replay run afterward. All first results and the guard failure
   remain retained; no hidden repetition of those 14 network evaluations occurs.
5. The auxiliary codec-only probe initially monitors the entire retained task,
   including the existing prefix, and stops at the output cap. A dedicated output
   directory corrects that operator mistake; the probe then passes without model
   or parameter work. The stop, source and correction are retained.

The shared source environment's pip check still reports the **seven inherited
AmberTools 26.0 metadata conflicts**, already owned in
[MolSysSuite #82](https://github.com/uibcdf/molsyssuite/issues/82) and the canonical
development-workspace record. Their package owners and causes are unchanged;
the environment is preserved. The isolated 21-package prefix is clean. No
unrelated component or external repository is modified to clear this baseline.

## Use and remaining gate

The [user guide](../docs/content/user/analogue_redesign.md) and
[saved-data example](../examples/replay_analogue_workflow.py) describe actual
development APIs, ancestry and explicit assessment/selection. The example checks
that a saved assessment belongs to this exact proposal pool and rejects mixed
generation ancestry without an engine import or fresh scientific credit.

**The separately authorized [R3 qualification](hydramp_redesign_R3_qualification.md)
now completes once**, with exact direct/adapter/repeat receiving, Macrel controls,
separate parent/child assessment and saved selection. Its 27-evaluation allowance
is exhausted. One returned candidate improves native scores but scores worse
under Macrel than its parent; scientific utility remains unqualified. Reuse A1/A2 math
evidence; this implementation does not justify another fidelity campaign or
biological claim. This single structural case does not establish general yield,
parent-relative predictive benefit or workflow usefulness. D44 dev5 evidence and
its probability/near-tie limitations remain unchanged.

Source and wheels are local/uncommitted, without a public installer, hosted CI,
new platform, package/model publication or full standalone-product claim. No
GPU, training, feedback, target conditioning, other-family work, commit/push or
original-author contact occurs. Active task artifacts are retained under #32/#4
for review by 2026-11-18; shared environments/assets are preserved.
