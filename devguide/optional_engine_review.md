# Optional engine integration review

This review distinguishes historical W0/W1 non-applicability from the current
[W2 source boundary](w2_macrel.md), tracked in uibcdf/peptidemt#6. Live Macrel
qualification and complete runtime adoption remain pending.

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
| Macrel 1.6.1 | Installed native Python, `assess_macrel` | Lazy `macrel`; selected `molsysmt` serialization and its Biopython route; both packaged ONNX heads | Verified PyPI `macrel==1.6.1`; Macrel Conda hint disabled; MolSysMT `uibcdf` route; no automatic installation | uibcdf/peptidemt#6, source/controlled evidence only; W3 pending |

Distinguish original Python libraries, executables, services, saved files and local
implementations. Document extras' actual contents. An unavailable selected route
must not silently switch methods. An intentional automatic selection exposes the
actual choice and its rule.

## Evidence per route

Current W2 controls and remaining gates are recorded in the
[work record](pending_proposals/implement_w2_macrel.md). The 84-test engine-free
suite includes requested absence, transitive failure, timeout, owner transport,
native call arguments, exact worker serialization and original dtype retention.
The declared support floors pass using operator copies of published packages.
No actual Macrel models executed and no live native parity is claimed.
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
