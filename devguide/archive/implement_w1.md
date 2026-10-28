---
summary: Implement the engine-independent D35/D36 W1 input, result and selection core.
issue: uibcdf/peptidemt#4
status: resolved
opened: 2026-10-27
closed: 2026-10-27
verification: measured
area: [core, input, results, selection]
guard: tests/test_w1_core.py
normative:
blocked_by: []
supersedes: []
---

# W1: engine-independent input, results and selection

## What and scope

Implement only W1 of the [accepted work order](../increment_1_work_order.md)
after [completed W0 receiving](../archive/complete_w0.md). D35/D36 and M1–M8
retain their scientific meaning. No Macrel installation or execution, new
scientific model, HydrAMP, package publication or later increment is included.

## How and why

Keep original ordered proposals, full FASTA headers/text, chemical/context
annotations and distinct occurrences. Derive operation-specific admission without
editing sequences or manufacturing chemistry. Receive original token-associated
provider rows and failure reasons, preserving duplicates/missing/extra rows and
all native columns. Recompute eligibility from retained data and apply both exact
lexicographic policies. Saved snapshots replay without the original engine.

The reusable tools live in PeptideMT's input, result and selection modules. No
molecular construction, general FASTA interoperability, feature calculation,
classifier or topology implementation is introduced. This parser is a bounded
peptide-proposal ingestion operation preserving source evidence, not a molecular
system importer.

## Boundary review

Public Python type/count/policy errors use ordinary TypeError/ValueError; there is
no alias normalization, cross-argument digestion or configurable contract engine.
Scientific admission/attribution and native output validation remain PeptideMT
data semantics. ArgDigest's published exports and existing FunctionContract/Domain
operations were inspected; no generic digestion tool is copied or required here.
Reassess when richer public argument digestion appears. No optional provider is
loaded, so availability/diagnostic execution guards remain W2. Incompatibilities,
reported failures and anomalies are retained result data. Scores have no physical
units and this core makes no quantity conversions. No unused runtime dependency
is added.

## Acceptance and evidence limits

Protect per-occurrence mapping, faithful native outputs, strict >0.5 labels,
finite scores, full rankings/ties/k/empty outcomes and exact serialized replay.
Explicit controlled fixtures exercise engine-independent M3–M8 portions. They
cannot qualify either live ONNX head, M1/M2, live M3–M6/M8 or the whole increment.
The caller-supplied bundle qualification reference remains an evidence assertion,
not certification performed by this library.

## Verification

Daily work uses molsyssuite@uibcdf_3.14 (Python 3.14.7), with the local clone
installed `--no-deps --no-build-isolation --editable`. All 53 source tests pass
with published Pytest Receptor 1.1.0, supplied from a temporary copy of its
official UIBCDF noarch `py_1` artifact (SHA-256
`4b56e6fc7c24e3f01d771c989bd7ed4bac9cf40c05e22f831a0ffff8defcd7dc`).
Earlier local runs used editable receptor 1.2.2+2.gb9676f8; those are distinct
tool inputs and are not called published use. The shared install is untouched.
Hosted CI retains published 1.1.0. Ruff 0.16.10 lint/format and report-index checks
pass. The example reproduces both approved invented-fixture selections.

Twelve pre-existing shared-environment dependency findings remain unchanged from
W0; no shared dependency is repaired. Current central repository conformance
passes. Installed snapshot replay and applicable hosted checks remain to record.

Coverage reporting remains unmaintained; controlled contract coverage is not
scientific provider coverage, a percentage badge or native M1–M8 qualification.

## Resolution — 2026-10-27

W1 is delivered at cbdcfe0557adbc2ff50267b39a46945e03ec3bf5, including
the implementation commit 914cb56. All 53 source and installed-wheel tests pass
with no skips. The neutral isolated installed example replays both D35 policies.
Routine CI 40615166187, frozen policy/admission 40615166719 and the complete
Linux/Python 3.11–3.14 matrix 40615211722 pass at that exact source. Published
GH Run Receptor 1.3.0 inspected each first; independent native run/job/step
assertions verify every required job and install/closure/replay/test step.
Event-inapplicable skipped jobs are explicitly excluded, not counted as passes.

The [durable receipt](../evidence/w1_core.json) retains exact input hashes,
local tool artifact digests, source/installed scope and native job/step facts.
The development wheel SHA-256 is
0afe130a1425ec51a2ba83cda793ec4c4c0a48bf49338a998eaf59a2738aa3ee;
it was never published. The final reporting/archive-only change has its own
applicable routine/policy evidence; the full matrix and wheel stay bound to
the original candidate. The guard protects the actual occurrence mapping,
input/output validation, precision, policy ordering and engine-absent replay
mechanisms, not just package import.

W1 is complete within its documented scope. No Macrel distribution/model was
installed or executed by this task, and W2 has not started. Live M1/M2 and the
native portions of M3–M6/M8 remain W2–W3 obligations. The twelve existing shared
dependency findings, future coverage reporting and caller qualification assertions
retain their stated limitations. No scientific contract is changed.
