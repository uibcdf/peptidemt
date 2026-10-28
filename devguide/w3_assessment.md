# W3 assessment: installed Macrel 1.6.1 on the bounded CPU profile

Status: **computational qualification evidence complete; investigator acceptance
of the bundle and stated scientific limits remains separate**. Owner:
[PeptideMT #6](https://github.com/uibcdf/peptidemt/issues/6).
Navigation: [preparation and authorization](w3_qualification.md) ·
[accepted M1–M8](v0_1_increment_1.md#5-acceptance-specification-for-increment-1) ·
[native evidence](evidence/w3_native/manifest.json).

## Exact executed boundary

The installed PeptideMT wheel was built from
`7a299d1a9e1b264c2f872e94d35b76d67c548a0a`, with the qualification driver input
correction at `a1b5e3a178679eb71f47bf6a693a43955879b97d`.
Macrel is the official PyPI 1.6.1 wheel, SHA-256
`7c0bf4c5d2fc98d02dd797522d92c2345c7c011ca818fe3e017fe2fd3aa22ef1`.
Both installed assets and the four native source files match that inspected
artifact. [Preflight](evidence/w3_preflight.json) retains asset digests and terms;
[installed inputs](evidence/w3_native/installed-inputs.json) records actual
software versions, source identity and candidate wheel hashes.

The actual environment is isolated Linux x86_64/CPython 3.14.10, CPU ONNX Runtime
1.25.1, NumPy 2.5.4, pandas 3.1.0, Biopython 1.88, Pyrodigal 3.7.1 and optional
Ackredit 0.9.0. It passes `pip check`; the shared development profile and its
known unrelated dependency findings are preserved. No GPU was used.

MolSysMT's public 0.23.0 artifact failed the non-model serializer preflight because
its SeqRecord recognizer compares against the wrong Python fullname. This is
the already-fixed [MolSysMT #359](https://github.com/uibcdf/molsysmt/issues/359).
Its accepted fix is present at published source
`3781031d0c1d08f34b2aa966ad0b82bf3b64a31d`. An unchanged source checkout produced
an installed local ABI3 wheel, SHA-256
`36fc0ffc34447727ee65cca6ce5313e45b7abd48a63dfa0ff02cc8abc8ced9a7`.
That exact candidate is the qualified molecular serialization provider, not the
broken public file. It is unpublished; neither the provider primary worktree nor
its frozen artifacts were changed. Rust/Cargo 1.98.1 from the named development
profile built it with two CPU affinity and low priority; this is not a public
rebuild or whole-provider/platform qualification.

## Measured live execution and gates

The four authorized calls completed in **21.38 seconds** combined. Individual
times were 5.330, 5.542, 5.279 and 5.229 seconds. Maximum observed child RSS was
539,123,712 bytes (about **514 MiB**), below the 4 GiB virtual-address ceiling.
Each child used CPU affinity `{0, 1}`, nice 10, ONNX intra-op 2/inter-op 1,
sequential graph execution, no spinning and numerical-library thread settings 1.
Host available RAM was 16.52–16.79 GiB before the calls; owned storage was about
1.89 GiB. One child ran at a time; no automatic model retry occurred.

The direct-reference observer records both real CPU ONNX sessions and their
`float32` input tensors for each direct call. The installed adapter invokes the
same verified native source and returns both scores exactly equal to reference.
Raw feature and prediction tables, original dtypes, float values, warnings,
request records and actual controls are retained under `evidence/w3_native/`.

| Gate | Executed evidence and limitation |
| --- | --- |
| M1 | All native feature/prediction columns match the adapter exactly; both actual classifiers execute. No tolerance or rounding was introduced. |
| M2 | The mixed pool has six evaluated occurrences: three AMP true/three false and three Hemo/three NonHemo. These are model outcomes, not measured activity or safety. |
| M3 | Seventeen input occurrences remain accounted for; six compatible rows, duplicate sequences and repeated full proposal headers preserve identity. Reordered/missing/extra/duplicate-row controls remain separately engine-free. |
| M4 | The native comparison clips leading M; the ordinary adapter excludes that original view. Stops, lowercase, ambiguity, empty/missing views and explicit unassessed chemistry remain unscored. |
| M5 | Upstream F/AA execute. Qualification-only direct probes preserve lengths 99, 100, 109 and 110 and record the native warning. Ordinary admission remains unchanged at <100. Operational execution does not establish empirical applicability at those lengths. |
| M6 | Native score/label/category checks pass, including all direct length outputs. Exact values and original dtypes survive serialization. Malformed outputs and the exact-0.5 rule retain their controlled guards. |
| M7 | Both policies replay unchanged evaluations with identical rankings, ties and k=0 behavior. A fresh reader imports neither Macrel nor Ackredit. The invented contrasting fixture remains distinct. |
| M8 | Actual empty/all-incompatible pools launch no provider. The existing controlled absence, broken import, missing asset, malformed output and timeout cases complement live evidence; they are not relabeled as live faults. |

The initial driver attempt failed during input preparation because it supplied
plain `None` rather than `SequenceRecord(None)`. Its
[zero-call failure](evidence/w3_native/preparation-zero-call-failure.json) is
retained. The corrected fixture has a durable engine-free guard. Neither that
attempt nor the earlier provider serializer failure invoked a model or consumed
the four-call inference allowance.

## Replay and interpretation

The real [saved snapshot](evidence/w3_native/qualified-computational.json) retains
all seventeen proposals, the six unrounded native rows, original software
versions and portable Ackredit bibliography. Its original qualification reference
names the actual local run; the exact run manifest is also retained here. A
reference remains a producer assertion, not automatic scientific certification.

Run the installed-package example from this checkout:

```bash
python -I examples/replay_macrel_qualification.py
```

With k=3, `amp-first` selects `input-0`, `input-4`, `input-2`;
`hemolysis-first` selects `input-1`, `input-3`, `input-2`. The first two AMP-first
occurrences are duplicates with native Hemo labels. The hemolysis-first ranking
includes native AMP negatives. This follows the approved reference policies,
which impose no biological acceptance threshold, label filter or deduplication.

AA receives native AMP probability 0.5148515701293945. This illustrates why
operational success on a very short sequence does not establish biological
applicability. Training-length distributions, chemistry beyond the accepted view,
actual termini/stereochemistry and experimental efficacy remain unqualified.
No synthesis/safety, target recognition, generation or optimization claim follows.

## Delivery and remaining work

The engine-free source/installed suite passed 101 tests for the original package
candidate; the corrected qualification fixture adds one new guard. Original
routine/policy and Linux Python 3.11–3.14 CI at `7a299d1` pass with 101 tests in
each test lane, independently checked through published GH Run Receptor 1.3.0
and native exact-source jobs/steps. The new replay example is an installed CI
receiving gate. Later receipt-head checks retain their own identities.

Portable attribution actually captures through public Ackredit 0.9.0 on the
completed live adapter call. Its host bibliography survives absence/failure,
reused references and fresh saved readers in the real-provider controls. Central
guide/inventory receiving for this new client remains separate from the completed
W0/W2 receiving and component-owned scientific acceptance.

FASTA migration remains [PeptideMT #5](https://github.com/uibcdf/peptidemt/issues/5).
MolSysMT #513 has delivered the provider capability, but this qualification
intentionally uses in-memory proposals and never the local parser. SMonitor #54
retains its external src-layout audit limitation; direct installed catalog checks
pass. Published Pytest Receptor 1.1.0 emits a nonblocking late discard-stream
ResourceWarning already tracked in its owning #4; original passing counts and
test exit status remain unchanged.

The scientific qualification environment, exact candidate wheels and original
run artifacts remain task-owned local resources for investigator/receiving
review. Source build scratch was removed after the wheel was installed and
verified. No model binaries, training corpus, release or published package are
part of this repository delivery. HydrAMP and later increments remain outside
the authorization. No more model calls are authorized by this receipt.
