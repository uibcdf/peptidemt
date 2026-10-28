# W2 native Macrel boundary

Status: **source implementation with engine-free controls; live qualification
pending**. Tracked in [PeptideMT #6](https://github.com/uibcdf/peptidemt/issues/6).
Navigation: [guide](README.md) · [work order](increment_1_work_order.md) ·
[scientific contract](v0_1_increment_1.md) · [work record](pending_proposals/implement_w2_macrel.md).

## Calling boundary

`peptidemt.assess_macrel(inputs, *, snapshot_id, limits,
qualification_reference=None)` consumes the complete ordered `InputRecord` tuple
returned by `prepare_sequences`. Build proposals in memory; this route never
uses `parse_fasta` or `read_fasta`. The [FASTA reader migration](pending_proposals/delegate_fasta_to_molsysmt.md)
remains pending in MolSysMT #513 and PeptideMT #5.

The caller must supply a `MacrelLimits(max_records, max_input_bytes,
wall_seconds, memory_bytes)` instance containing its authorized bounds. There
are no automatic retries or default host-use permission. Submitted count and
UTF-8 sequence/token byte limits are checked before launch. A single isolated
Linux Python child covers imports, transport, feature calculation and both heads;
the parent enforces wall time. Linux `RLIMIT_AS` bounds child virtual address
space, not RSS. ONNX keeps native CPU/session/thread defaults; this is not a
thread-count or aggregate system-memory guarantee. Choose the actual envelope
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
Macrel installer, and identifies MolSysMT's `uibcdf` Conda route. MolSysMT's
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
0.19.0, separately from shared editable provider tests. Macrel was not installed
and neither ONNX model executed. This is no claim of M1/M2 or live M3–M8 parity.

W3 still requires the actual installed Linux CPU/Python 3.14 combination, permitted
terms/fixtures, approved resource envelope, both heads' real execution and direct
native comparisons. Package publication and broader provider/platform support
remain unqualified and outside this delivery.
