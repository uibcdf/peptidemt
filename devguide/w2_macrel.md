# W2 native Macrel boundary

Status: **implemented; one exact installed CPU bundle has native qualification
evidence, with investigator acceptance separate**. Tracked in
[PeptideMT #6](https://github.com/uibcdf/peptidemt/issues/6).
The [W3 assessment](w3_assessment.md) records actual execution; older source-only
receipts below retain their original scope.
See [W3 preparation](w3_qualification.md) for exact candidate assets and proposed host limits.
Navigation: [guide](README.md) · [work order](increment_1_work_order.md) ·
[scientific contract](v0_1_increment_1.md) · [work record](pending_proposals/implement_w2_macrel.md).

## Calling boundary

`peptidemt.assess_macrel(inputs, *, snapshot_id, limits,
qualification_reference=None)` consumes the complete ordered `InputRecord` tuple
returned by `prepare_sequences`. Build proposals in memory; this route never
uses `parse_fasta` or `read_fasta`. The [FASTA reader migration](archive/delegate_fasta_to_molsysmt.md)
now delegates to the public API delivered in MolSysMT #513 and adopted under
PeptideMT #5. The shared editable development source supplies that capability,
as recorded in the migration report. This changes ingestion, not the original
in-memory W3 scientific fixture or its qualification evidence.

The caller must supply a `MacrelLimits(max_records, max_input_bytes,
wall_seconds, memory_bytes)` instance containing its authorized bounds. There
are no automatic retries or default host-use permission. Submitted count and
UTF-8 sequence/token byte limits are checked before launch. A single isolated
Linux Python child covers imports, transport, feature calculation and both heads;
the parent enforces wall time. Linux `RLIMIT_AS` bounds child virtual address
space, not RSS. Without optional controls, ONNX keeps native CPU/session/thread defaults; this is not a
thread-count or aggregate system-memory guarantee. Optional `intra_op_threads`,
`blas_threads`, `cpu_ids`, `nice`, `min_available_memory_bytes` and `temporary_root`
make selected child controls explicit. Setting ONNX threads uses its public
SessionOptions, sequential graph execution, one inter-op thread and no spinning;
the original factory is restored even on failure. Numerical environment changes
apply only to the child. Requested CPU affinity cannot exceed inherited allowed
CPUs; priority is only lowered. The [authorized W3 profile](w3_qualification.md)
sets these controls and records actual resource use. Choose the actual envelope
with the host maintainer before scientific execution.

Only compatible unchanged views are submitted, retaining each occurrence.
Leading-M, unsupported/empty/incomplete, explicit unassessed chemistry and
out-of-provisional-scope proposals remain in the result with W1's existing
reasons. An empty/all-incompatible pool never loads or starts the engine.

The result is the existing `ResultSet`, saved/replayed using its v1 exact-float
schema and selected with either unchanged W1 policy. Without a caller-supplied
qualification reference, native data remain marked `unqualified_bundle` and
cannot enter ranking. A reference is an assertion requiring external evidence;
the API does not certify arbitrary bundles or scientific applicability.

Completed child operations now attach `scientific_attribution` to provenance.
This host-owned `peptidemt.scientific_attribution@1` record retains offline
bibliography, original producer/software versions and completed operation names.
Optional Ackredit >=0.9.0 capture uses the application's current session after
execution; it never creates a component-owned session or infers references by
subtracting session IDs. Reused references remain in each detached result.
The Macrel paper describes the method, native Macrel/MolSysMT/PeptideMT software
is credited only for completed branches, and adapted modlAMP code is a reference
implementation rather than an executed dependency. Partial child completion is
distinct from successful overall prediction. Missing/failing Ackredit preserves
completed results and bibliography with an explicit status and catalog diagnostic
on failure, including under strict warning filters. Empty unexecuted pools load
no attribution provider. Saved-result reading creates no new scientific credit.

Ackredit is optional runtime use with no new package extra or required dependency.
CI explicitly supplies public Ackredit 0.9.0 as a test dependency so the portable
capability floor and real-provider receiving can be verified across the package
Python matrix. Source tests use controlled completion evidence, not Macrel output;
installed-Macrel attribution remains a W3 gate.

## Ownership and native operations

MolSysMT publicly converts each canonical view to `biopython.SeqRecord` and
serializes it to FASTA. PeptideMT assigns only its opaque occurrence token and
concatenates owner-serialized bytes for this run's transport. It checks that
conversion retained the sequence. No local parser, feature formula, topology,
coordinate construction or chemistry inference is used.

The route targets installed **Macrel 1.6.1**, rejects a mismatching version or
a source checkout shadowing its installed package, and calls:

- `macrel.AMP_features.fasta_features(transport_filename)`;
- `macrel.AMP_predict.predict(AMP_asset, Hemo_asset, features,
  keep_negatives=True)`.

Both asset paths are taken from that installed package. No CLI output,
`compute_all` bypass, alternative model, download, installer or fallback is used.
Source inspection refers to [Macrel v1.6.1 at 19046260](https://github.com/BigDataBiology/macrel/tree/190462605913844dca74b184869755609fbb20b2).
That source observation does not identify an installed artifact's bytes.

The native row index reconciles opaque tokens; returned order and repeated
sequences never replace occurrence identity. All returned prediction columns,
feature/prediction tables and original dtypes are retained in provenance. NumPy
scalars become exact Python scalars through `.item()` and the existing tagged
float codec, without decimal formatting. W1 derives missing/extra/duplicate rows,
changed views, malformed scores/labels and eligibility from retained data.

## Availability, diagnostics and provenance

DepDigest >=0.12.0 guards only the selected native imports. The declaration
advertises the verified PyPI Macrel 1.6.1 route, disables an unqualified Conda
Macrel installer, and disables MolSysMT installers at this selected boundary while
its public 0.23.0 artifact lacks the already-fixed #359 recognition behavior. The
[W3 assessment](w3_assessment.md) identifies the exact installed owner-source
wheel; restore a public installer only after an actual published artifact passes
the conversion/serialization gate. This installer-hint restriction does not
block development against the owner's editable source in the shared Conda
environment, or require a new public release before FASTA migration. MolSysMT's
selected SeqRecord conversion also requires its optional Biopython capability.
Macrel/MolSysMT/Biopython and ONNX dependencies are not installed by PeptideMT
and are absent from core requirements and engine-free CI environments.

DepDigest and SMonitor >=0.19.0 are required support libraries acquired by the
committed Conda CI route. The optional adapter itself is lazy: importing the core
or replaying saved results does not initialize it or import molecular providers.
Selecting it registers SMonitor declarations while preserving application policy.
Its orchestration entry point carries a signal; operational failures emit catalog
warnings with stage/type, separate from scientific data. Existing simple type,
count and positive-limit checks require no nontrivial ArgDigest normalization;
unitless classifier scores introduce no PyUnitWizard quantity operation.

Unavailable dependencies, present-but-broken imports, asset/transport/feature/
prediction/output failures, timeout and child termination remain distinct.
Every submitted occurrence receives the reported failure; incompatible original
proposals retain their own reasons. No score is invented. The result retains
the cause type/message when the child can report it, without interpolating the
native message into diagnostic events. Forced termination can retain only its
return code. Parent-side transport errors retain their type. Child stdout/stderr
are discarded; returned scientific tables and structured failure evidence are
the supported evidence boundary.

Provenance includes submitted mappings, limits/retries/time, package versions and
import origins, native source and both compressed-asset SHA-256 digests, transport
digest, native tables/dtypes, Python executable/version and CPU configuration.
Installer-artifact digest, applicable code/model/data terms and fixture origins
belong in the referenced W3 qualification manifest; runtime identity alone does
not supply those conclusions or full transitive dependency closure.

## Evidence and remaining gate

The source suite has 84 engine-free tests, including native-call stand-ins,
owner conversion/transport controls, exact-float worker round trips, failures,
absence/transitive-import distinctions, limits, diagnostics and core independence.
It passes against operator copies of published DepDigest 0.12.0 and SMonitor
0.19.0 in the parent process, separately from shared editable provider tests;
isolated children retain their installed environment's providers. Macrel was not installed
and neither ONNX model executed. This is no claim of M1/M2 or live M3–M8 parity.

W3 still requires the actual installed Linux CPU/Python 3.14 combination, permitted
terms/fixtures, approved resource envelope, both heads' real execution and direct
native comparisons. Package publication and broader provider/platform support
remain unqualified and outside this delivery.

The preceding paragraph describes the original W2 checkpoint. The later
[W3 assessment](w3_assessment.md) supplies actual Linux CPU/Python 3.14.10
execution for the recorded Macrel 1.6.1/MolSysMT source-wheel combination.
It does not extend that evidence to other provider versions/platforms or silently
qualify the broken public MolSysMT 0.23.0 artifact.

The [exact-source receipt](evidence/w2_boundary.json) records commit `6b86d72`,
the unpublished installed wheel, 84 passing installed tests, complete passing
Linux Python 3.11–3.14 CI, and receptor/native job verification. Central
relations/guide receiving and optional scientific-attribution review are tracked
in [MolSysSuite #151](https://github.com/uibcdf/molsyssuite/issues/151).
The external flat-layout audit limitation is reported in
[SMonitor #54](https://github.com/uibcdf/smonitor/issues/54); direct installed
catalog/configuration/rendering/reconstruction/export controls pass.
