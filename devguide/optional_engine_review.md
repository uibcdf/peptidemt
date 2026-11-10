# Optional engine integration review

This review distinguishes historical W0/W1 non-applicability from the current
[W2 source boundary](w2_macrel.md), tracked in uibcdf/peptidemt#6. The exact Macrel bundle has executed qualification and investigator acceptance
under D37; public delivery and external provider-audit limitations retain their
own scope.

The commissioned HydrAMP work in [#8](https://github.com/uibcdf/peptidemt/issues/8)
has progressed from its [isolated H0–H1 review](hydramp_environment_review.md)
to a native PyTorch port and an [executed bounded private composition](hydramp_h4_qualification.md).
The [public data receiver](hydramp_public_receiving.md) now has an exact local
installed-wheel proof. The [isolated execution adapter](hydramp_execution_adapter.md) now has installed
controlled proof and a separately approved real-checkpoint case with 16 proposals,
exact native results/trace and captured parent attribution. D41 accepts this exact
resource for experimental AMP generation; broader
claims remain unqualified. See the [acceptance record](hydramp_dev3_acceptance.md);
the data route did not certify this execution.

When a concrete change is needed, open the owning issue first and create its report
using the local [reporting protocol](reporting_protocol.md). Link that issue here.
Do not add unused runtime dependencies to fill this worksheet.

## Shared references

- [MolSysSuite optional engine contract](https://github.com/uibcdf/molsyssuite/blob/main/devguide/optional_engine_integration.md)
- [DepDigest provider recipe](https://github.com/uibcdf/depdigest/blob/main/docs/content/user/optional-engines.md)
- [MolSysSuite ecosystem policy](https://github.com/uibcdf/molsyssuite/blob/main/devguide/python_ecosystem_policy.md)
- [MolSysSuite CI policy](https://github.com/uibcdf/molsyssuite/blob/main/devguide/python_ci_policy.md)

Use synchronized provider guides when registered for this member. Verify published
provider versions before claiming clean public installation. DepDigest's executable
and explicit disabled-installer extension is tracked in uibcdf/depdigest#22;
source availability alone is not release evidence.

## W0 applicability — 2026-10-27

No optional-engine boundary exists in the generated empty package. This worksheet
is non-applicable to executed W0 source only, as recorded in
[the W0 receiving record](archive/complete_w0.md) and
[uibcdf/peptidemt#1](https://github.com/uibcdf/peptidemt/issues/1).
Macrel remains a qualification candidate for W2–W3, not an installed or implemented
route. Reassess this worksheet before exposing that route. No model was downloaded
or executed to establish this non-applicability.

## W1 applicability — 2026-10-27

The [W1 core](w1_core.md), tracked in uibcdf/peptidemt#4, receives saved data
without selecting, importing or invoking an engine. Result-schema, mapping,
precision and engine-absent replay checks are implemented; no provider-availability
or execution boundary exists yet. Reassess DepDigest/SMonitor and the route
inventory at W2. No Macrel installation, native comparison or live qualification
is established by controlled W1 fixtures. The archived W0 record remains history.

## Route inventory

Add one row for each implemented route. Names and directory layout remain local.

| Method/provider | Access route and public selector | Requirement/import/command/service | Actual pip/Conda routes or disabled routes | Owner issue and status |
| --- | --- | --- | --- | --- |
| Macrel 1.6.1 | Installed native Python, `assess_macrel` | Lazy `macrel`; selected `molsysmt` serialization and its Biopython route; both packaged ONNX heads | Verified Macrel PyPI file; unqualified installers disabled; exact installed MolSysMT owner-source wheel under #359 | uibcdf/peptidemt#6; actual bounded W3 evidence, investigator acceptance separate |
| Ackredit >=0.9.0 | Optional portable post-operation capture | Lazy `ackredit`; host bibliography retained without it | Public `uibcdf` Conda route; no pip/required runtime extra invented | uibcdf/peptidemt#6; real controlled receiving plus actual native-call capture |
| MolSysMT source-preserving FASTA | `parse_fasta` / `read_fasta` delegate to public `file_fasta.parse_records/read_records` | Lazy `molsysmt`; optional for memory inputs/replay; no Bio or model required for ingestion | Shared editable development source; full-SHA source installation and Conda closure in CI, no unverified public installer | uibcdf/peptidemt#5; owner-backed tests, separate from original W3 model bundle |
| Modern HydrAMP retained data | `HydrAMPReceipt.from_trace/from_json`, `to_json`, `inputs` | Existing native trace values or v1 JSON; no engine/NumPy/Torch import or new scientific execution | No engine dependency, extra or installer is added by receiving data | uibcdf/peptidemt#8; 41 installed data/controller/W1 checks, exact H4 saved replay; separate public execution case completed; D41 experimental AMP acceptance |
| Modern HydrAMP CPU execution | `generate_hydramp`, explicit `worker_python`, `HydrAMPBundle` and `HydrAMPLimits` | Child-only guarded `hydramp_torch`; pinned installed runtime/checkpoint/numeric PCA; no host heavy import | Unpublished exact dev3 runtime; both installer routes disabled; no package extra or automatic acquisition | uibcdf/peptidemt#8; 55 installed controlled checks and one real installed-adapter case completed; exact native receiving/replay and captured parent attribution; D41 experimental AMP acceptance; broader claims unqualified |
| Modern HydrAMP analogue CPU execution | `redesign_hydramp`, explicit `worker_python`, `HydrAMPAnalogueBundle`, existing `HydrAMPLimits`; data-only `HydrAMPAnalogueReceipt` | Child-only guarded dev6 codec/encoder/core/composer; no PCA/modlAMP; pinned installed runtime/source/checkpoint; no host model import | Unpublished exact local dev6/consumer wheels; no public installer/extra or automatic acquisition | uibcdf/peptidemt#32 / uibcdf/hydramp#4; D45 R1/R2 with101 installed controls and21 artificial network evaluations; separately authorized R3 completes21 learned-network/6 ONNX evaluations with exact receiving/replay and captured credit; one child scores worse than its parent under Macrel; allowance exhausted, scientific utility unqualified |

Distinguish original Python libraries, executables, services, saved files and local
implementations. Document extras' actual contents. An unavailable selected route
must not silently switch methods. An intentional automatic selection exposes the
actual choice and its rule.

## Evidence per route

Current W2 controls and remaining gates are recorded in the
[work record](archive/implement_w2_macrel.md). The 84-test engine-free
suite includes requested absence, transitive failure, timeout, owner transport,
native call arguments, exact worker serialization and original dtype retention.
The declared support floors pass using operator copies of published packages.
No actual Macrel models executed and no live native parity is claimed.
That sentence belongs to the original W2 checkpoint. The later
[W3 assessment](w3_assessment.md) retains actual four-call execution, exact native
parity and portable attribution for one installed CPU bundle. Its qualified
MolSysMT source artifact is distinct from the broken public 0.23.0 file.
Central dependency/guide receiving is recorded under uibcdf/molsyssuite#151
and issue #6. The two registered provider guides are delivered via the official
synchronizer. Selected MolSysMT serialization is a guarded integration, not a
declared package extra; no metadata requirement is invented. Scientific-attribution
applicability and remaining host receiving are explicit in [the local governance
map](governance.md#scientific-attribution-before-live-w3-acceptance). These
controls and guide copies do not establish live scientific adoption.

Record commands/selectors, source commit, environment, result and limits for:

- package import/test collection and unrelated routes with the engine absent;
- the requested-route error, truthful installation hint and exception compatibility;
- internal import/execution failures distinct from absence;
- installed distribution or binary identity, including custom command paths;
- direct upstream comparison on the same submitted input, with component-owned
  fields/tolerances and an installed gate that fails on missing/shadowed engines;
- deterministic file/transport tests separately from actual live service execution;
- receiving-component interface evidence, when another member consumes the result.

Identify the CI route/schedule that supplies installed-engine evidence. Ordinary
absence skips cannot establish adoption; present-but-broken engines need an owning
defect. Preserve the component's full/routine lanes and environment constraints.

## Result boundary and compatibility

Document the schema/API version, actual provider/backend, input selection/frame and
source-index mapping, artifact retention, quantities/definitions, transformations
and receiving members. Distinguish unavailable values from zero or empty results.
Record any compatibility adjustments and their removal conditions.

## Exceptions and next gates

For each exception, name the affected rule/route, reason, owner and provider issues,
interim behavior/evidence, responsible maintainer, removal condition and dated
review deadline. Keep guide distribution, source integration, public release and
consumer runtime adoption as separate states. Review this worksheet when an
optional route or result contract changes.
