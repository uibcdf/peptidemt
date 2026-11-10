---
summary: Diagnose oversized numeric receipt values without OverflowError during anomaly inspection.
issue: uibcdf/peptidemt#34
status: partial
opened: 2026-11-04
closed:
severity: low
verification: reproduced
area: [results, diagnostics]
guard: tests/test_hydramp_receiving.py::test_oversized_numeric_values_remain_inspectable_after_replay
normative:
blocked_by: []
supersedes: []
---

# HydrAMP receipt numeric overflow during anomaly inspection

## Local correction delivered — 2026-11-04

The diagnostic now handles numeric-conversion overflow as an invalid native
value while retaining the exact original payload. Fourteen regressions cover
both signs across all seven numeric native fields, inspecting the direct and
JSON-replayed receipt and its proposal context. Before the fix all 14 fail
with the original OverflowError; after it, all 35 receiving checks plus the
reporting guard pass (36 total). Ruff/format checks pass. This is a local source
fix, not a new installed consumer release. Keep the issue partial/open until
the normal source delivery boundary is resolved; no commit/push is inferred.
The final affected receiving, controlled execution/transport and reporting
selection passes 58 tests (1.40 seconds), with no real model execution.

## What

`HydrAMPReceipt.issues` raises `OverflowError` for a stored integer `10**400`
in `hydrophobicity`, instead of returning inspectable anomaly information.
The same failure occurs after its supported JSON roundtrip. Observed during
the [2026-11-04 audit revision 2](../peptidemt_scientific_audit_2026_11_04.md).

## How

Construct one artificial receipt row with sequence `ACD`, ordinary finite native
scores/descriptors, and `hydrophobicity=10**400`; request `.issues`, both directly
and after `HydrAMPReceipt.from_json(receipt.to_json())`. The issue includes the
minimal public-API reproduction. `math.isfinite(value)` in
[`_hydramp_receiving.py`](../../src/peptidemt/_hydramp_receiving.py) converts the
integer to float and overflows. The type check admits integers before that call.

The [observations](../evidence/peptidemt_scientific_audit_2026_11_04_observations.json)
and [instrument receipt](../evidence/peptidemt_scientific_audit_2026_11_04_review2.json)
retain source hashes and both exceptions. No model was loaded or executed.

## Why

The data receiver promises preservation and inspection of anomalous native
payloads. A malformed imported value should not prevent that inspection or
silently become a finite score. The effect on `.issues` is reproduced; broader
malformed-field coverage is pending. Valid qualified native outputs are not
shown to be affected.

## What was refuted

This is not a model precision failure, invalidation of D41, or evidence that a
native provider produced such a value. Serialization alone does not remove it.

## Scope and exclusions

Data-boundary diagnostic robustness only. No model call, scientific-threshold
change, score repair, new chemistry or general schema redesign is requested.
The audit records the bug without implementing its fix.

## Acceptance criteria

1. Preserve the malformed original payload and return a deliberate diagnosed
   outcome for unsupported numeric values without numeric-conversion overflow.
2. Cover in-memory and serialized inspection, plus applicable other native
   numeric fields, with focused regressions when fixing.
3. Preserve current valid numeric semantics and existing qualified receipts;
   do not introduce arbitrary physical cutoffs or new scientific acceptance.
