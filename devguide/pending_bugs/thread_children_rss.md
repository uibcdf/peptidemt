---
summary: Include thread-created subprocesses in aggregate RSS supervision.
issue: uibcdf/peptidemt#38
status: partial
opened: 2026-11-06
closed:
severity: medium
verification: reproduced
area: [execution, resources]
guard: devtools/tests/test_process_supervision.py::test_rss_includes_child_created_by_secondary_thread
normative:
blocked_by: []
supersedes: []
---

# Thread-created children are missing from process-tree RSS

## What

The private Linux supervisor reads only the main task's `/proc` children file.
A subprocess created from a secondary thread is recorded under that creating
task, so its memory is omitted from the declared aggregate RSS scope. This is
confirmed during [D51 T0 receiving](../mdm2_t0_qualification.md).

## Evidence and correction

A real secondary thread starts one Python child retaining a 32 MiB bytearray.
Before correction, parent/child direct RSS is 93,974,528 bytes but `tree_rss`
returns 49,606,656. The guard fails with native pytest exit 1 and published
Pytest Receptor 1.2.2. All work is artificial process/resource checking, with no
molecular or learned provider.

The local correction reads every task's children list, tolerates a task vanishing
during traversal, and retains process deduplication and a single RSS contribution
per process. No dependency or public API changes are introduced. The real guard now passes after the correction. A separate selected run passes
15 tests: that guard, the existing timeout/output/host-memory/parent-death
process guards and the T0 artificial checks. The
[execution evidence](../evidence/mdm2_t0_execution.json) retains both outcomes.
The issue stays partial until the reviewed source/guard is delivered; no commit
or publication is authorized by this local correction.

Earlier receipts retain their exact sampled facts. Their native-build traversal
may have missed thread-created compiler children; a complete aggregate peak
must not be claimed retrospectively. The independently measured host-available
RAM guard still ran. This finding changes no scientific numerical result and
does not authorize rerunning an accepted scientific campaign.
