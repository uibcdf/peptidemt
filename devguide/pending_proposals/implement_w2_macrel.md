---
summary: Implement the bounded native Macrel route from in-memory proposal occurrences.
issue: uibcdf/peptidemt#6
status: partial
opened: 2026-10-28
closed:
verification: measured
area: [assessment, integration, provenance]
guard: tests/test_w2_macrel.py
normative:
blocked_by: []
supersedes: []
---

# W2 native Macrel route

## What

Advance the [authorized W2 work](../increment_1_work_order.md) using prepared
in-memory occurrences, following the investigator's explicit operational choice.
The source-preserving FASTA reader remains separately tracked in PeptideMT #5
and MolSysMT #513. W2 does not call or extend the local reader.

## How and why

The [implemented boundary](../w2_macrel.md) uses lazy DepDigest guards,
MolSysMT conversion/serialization, the native Macrel feature function and
prediction function with both packaged heads and `keep_negatives=True`.
Original inputs, returned columns, dtypes, exact scalar values and execution
evidence remain attributed. SMonitor owns operational diagnostics.

One isolated Linux child has explicit record/byte/wall-time/address-space limits
and no retry. Incompatible/empty input pools never launch it. Failure to execute
does not manufacture scores or change the method. Caller-provided qualification
references remain assertions, not automatic bundle certification.

## Measured controls and limits

The 2026-10-28 engine-free source suite passes **84 tests**, including 31 W2
controls. It also passes with operator copies of published DepDigest 0.12.0
and SMonitor 0.19.0, the declared capability floors. Copies do not replace the
shared environment's editable providers or establish clean dependency closure.
Ruff lint/format pass. Installed/hosted evidence will be linked from issue #6.

A direct public MolSysMT conversion/serialization probe in the named shared
Python 3.14.7 profile preserved ACD and the opaque `input-0` token. Executed
provider source: `uibcdf/molsysmt@3781031d0c1d08f34b2aa966ad0b82bf3b64a31d`.
Its SeqRecord form emits its existing Tier 2 best-effort support warning; this
probe does not establish native Macrel parity or all-input transport qualification.
The primary MolSysMT clone was neither edited nor advanced.

The external SMonitor audit stopped at its flat-layout assumption before
inspecting this `src/` package; reported as
[SMonitor #54](https://github.com/uibcdf/smonitor/issues/54). Direct catalog,
reconstruction and installed configuration checks supply bounded interim evidence.
No provider code was changed to bypass that limitation.

The shared profile still reports the 12 previously observed dependency conflicts.
They are not repaired or reclassified by this work. Actual clean installed
dependency resolution remains a hosted/isolated boundary.

## What was refuted

- Macrel's `fasta_features` consumes a filename, not an in-memory sequence API.
  Bypassing it with `compute_all` would change the approved native contract.
- A temporary FASTA transport does not require local FASTA parsing. MolSysMT's
  public converters serialize each occurrence; PeptideMT concatenates their bytes
  and owns only its opaque occurrence IDs. No topology/coordinates are built.
- Controlled native-call stand-ins test orchestration and fidelity, not either
  ONNX classifier. No Macrel package/model was installed or executed here.

## Scope and remaining acceptance

D35/D36, M1–M8, selectors and chemistry remain unchanged. No HydrAMP, later
increment, provider-source change, package publication or model redistribution.

1. Preserve engine-free and installed consumer checks, dependency acquisition,
   diagnostic catalogs and exact-head CI evidence for the implemented source.
2. Register actual DepDigest/SMonitor runtime and optional MolSysMT relationships
   centrally with immutable source evidence; distinguish guide delivery from use.
3. W3 must identify the permitted exact installed bundle/assets, terms, fixtures,
   import origins and investigator-authorized host resource envelope before live
   execution, then supply native parity and the real portions of M1–M8.
4. Keep this record partial until the actual integration has that evidence. A
   passing engine-free suite cannot close the live scientific obligations.
