# Isolated HydrAMP execution adapter and bounded installed qualification plan

Status: **real installed case completed; exact resource accepted for experimental
AMP generation under D41**, 2026-11-03. See the [acceptance and its limits](hydramp_dev3_acceptance.md).
The original failed startup and its correction remain preserved below.
Owner: [PeptideMT #8](https://github.com/uibcdf/peptidemt/issues/8).
The investigator commissions this next step after the
[public data-receiving milestone](hydramp_public_receiving.md). No new scientific
decision or model allowance is inferred from implementation authority.

## Implemented calling boundary

`peptidemt.generate_hydramp` accepts an explicit target count, seed, snapshot,
`HydrAMPBundle`, `HydrAMPLimits`, absolute worker interpreter and optional
qualification reference. The existing `HydrAMPReceipt` remains the result.
The [user guide](../docs/content/user/hydramp_execution.md) and
[API reference](../docs/api/public.rst) document the provisional interface.

One separate Linux CPU process calls the pinned provider's numeric PCA,
checkpoint loader, `HydrAMPGenerator.generate_with_trace` and
`Modlamp433Properties`. The native branch remains AMP, unfiltered,
`properties=True`, one attempt and an explicit seed. A successful call contains
one decoder, both original-token heads and one descriptor bundle. Existing
source observations are delegated unchanged; no chemistry, molecular parser,
descriptor formula, precision choice, score meaning or selector is replaced.
MolSysMT still owns molecular operations.

Before learned operations, the worker verifies its PeptideMT version/source
against the caller, distribution versions, installed import origins, complete
HydrAMP Python-source hashes and checkpoint/PCA digests. Shadowed or editable
scientific packages are rejected on this installed route. Only the requested
worker's `hydramp_torch` import has a DepDigest guard; neither installer route
is advertised for the unpublished experimental provider. The shared optional
engine review replaces the Macrel-only dependency help link.

The caller supplies count, time, virtual-address, sampled tree-RSS, output,
CPU/thread and resource-floor limits. Numerical settings apply only in the
child. A dedicated process group and Linux parent-death handling isolate cleanup
without replacing the host's signal policy. Sampling is not a hard physical-RAM
quota. Kernel address space is not resident RAM. Failure/timeout/interruption
cleanup and parent-death behavior have bounded model-free process tests.

State is saved atomically before and after each permitted operation. No retry,
refill, fallback or environment installation occurs. Incompatible native proposals
remain in the existing receipt. Missing/invalid/mismatched output cannot acquire
another request's identity or become negative scientific scores. Detailed failure
stage/type and retained state accompany catalog-owned SMonitor events.

## Optional attribution and ownership

The existing Macrel capture implementation is reused through one private capture
helper. Confirmed HydrAMP child operations contribute to the application's parent
Ackredit session after execution. Offline bibliography and original versions
survive provider absence/failure. Unfinished descriptor work does not receive
completed-descriptor credit; saved replay creates none. Original HydrAMP is a
reference implementation; legacy TensorFlow is not an executed dependency.
The method, modern implementation, NumPy, Torch and modlAMP retain separate roles.
No component-owned session or automatic network enrichment is introduced.

The investigator reiterates the owning-component issue route for sibling
improvements. The initial test adjustments concern expected Ackredit deduplication
and an incorrect test reference to DepDigest internals, not demonstrated provider
bugs. A separate real reuse need is reported as
[HydrAMP #2](https://github.com/uibcdf/hydramp/issues/2): publish owner-maintained,
data-only generation/descriptor-profile metadata. Its
[verified proposal receipt](evidence/hydramp_profile_owner_proposal.json) retains
the exact disclosure. This is a proposal, not an accepted new profile or candidate.
Until delivery/qualification, exact provider/worker source identity and original
definitions are retained. The adapter adds no second computational implementation.

## Exact local artifact and executed engineering evidence

Local unpublished wheel: `peptidemt-0.1.0+118.g1f8c444.dirty-py3-none-any.whl`,
SHA-256 **`18b1cb18b9662092203aad9c64d45bc0d61a862577297c13a664572dbdbc3e83`**.
This is a different local artifact from the earlier data-only wheel; both original
files remain retained under separate task directories. No immutable public package
coordinate is overwritten, and no commit or package publication is claimed.

**55 installed controlled checks pass**, using published Pytest Receptor 1.1.0
and agreeing native JUnit. They cover the new adapter, old receiving/attribution,
the complete diagnostic catalog and a full foreign-process public call with an
explicit artificial provider. That stand-in loads no neural library or scientific
array and is not a real-provider gate. Process time is 3.58 s, child kernel
RSS high-water about 50.1 MiB. A separate actual installed missing-engine round
trip reports `RequiredDependencyError`, zero native attempts and no attribution.
Two model-free approval/budget controls also pass with published Receptor 1.2.2.

All 26 wheel members except generated RECORD match installed bytes; all package
Python files match the wheel and current source. Parent fixture dependency closure
passes. The original H4 receipt/result files still replay exactly with both
complete rankings. Sphinx HTML builds with warnings fatal and six unchanged
memory-input doctests pass against this exact installed package. The first two
source-test failures and the initial short RST underline warning are retained,
with their causes and passing replacements; they are not concealed skips.

The new generation worker initially inherited the shared Conda base's packages:
Python venv creation from another venv uses its base environment rather than
inheriting that venv's site-packages. `pip check` exposed unrelated base-profile
dependencies. Inspection of `sys.prefix`, `sys.base_prefix` and `sys.path`
identified this cause before any model import or sibling modification.
The new worker now excludes global site-packages and explicitly includes only
the unchanged frozen dev3 site-packages. Exact API-only copies of published
DepDigest 0.15.1/SMonitor 0.22.0 and the new consumer wheel are added in its own
prefix; support console entry points are not claimed. Corrected `pip check`
passes. Neither old scientific worker nor the shared Conda environment is changed.

## Prepared single real case: fresh approval required

Plan: `local_data/hydramp-execution-adapter-vceg9u_2/live-plan.json`;
SHA-256 **`1d4679f27d06d95bd402b1f9239e8dc1fc5120a722da5057be526220985da665`**.
The [qualification runner](../devtools/hydramp_execution_qualification.py) verifies
**345 file pins** without model/PCA loading. Missing or other-plan authorization
blocks both execution entry points. The real authorization/model-attempt files
are absent at preparation closeout. Initial unsealed plans are not run approvals.

Request one public call, **16 proposals / seed 1001**, compared with the retained
native receipt from the approved H4 experiment. Maximum new allowance is:

- one checkpoint load and one numeric PCA load/inverse transform;
- one decoder plus one AMP and one MIC forward: **three neural forwards**;
- one descriptor bundle and no retries;
- **zero Macrel, legacy, training, GPU or other scientific-model calls**.

Verify actual installed public receiving, request identity, native rows/order/
indices, all original trace fields, saved replay and real parent-session
attribution. Preserve any variation; do not change thresholds or force legacy
identity. Existing Macrel/selector and native-comparison evidence is reused.

Use the unchanged dev3 wheel
`81761e0d48d92f0956e0afc28b3b4154f16032de53c666fd2cfbb53606102ed7`,
original source `6590d2f4c2963f25d30669052a4c4a857e0e7279`, starter
`7804df862872ccc6d09fe01c41bafbca194cfa31`, epoch-37 checkpoint and numeric PCA,
under the previously approved local research/use conditions. The parent is the
new installed consumer over frozen W3/Python 3.14.10/Ackredit 0.9.0; the isolated
generation worker uses Python 3.14.7/NumPy 2.4.6/Torch 2.15.0+cpu/modlAMP 4.3.3.
The plan records all resolved runtime versions and exact origins, not a new public
dependency-support range.

Limits: **4 GB task RAM intent**, stop at **2 GiB sampled aggregate process-tree
RSS**, CPU 0/1, one numerical thread, nice 10, worker ≤180 s and whole case ≤210 s.
Worker virtual address space is ≤8 GiB; parent ≤1 GiB. Require ≥8 GiB host available
RAM and ≥1 GiB free disk, output ≤128 MiB. No network/GPU/retry. The 23:22 UTC
snapshot shows about 14.65 GiB available RAM and 2.30 TiB free disk; conditions
are rechecked during execution rather than reserved by the snapshot.

The [preparation receipt](evidence/hydramp_execution_adapter_preparation.json)
retains source, artifact, environments, executed controls and this exact plan.
There are **zero new real model/PCA/descriptor/Macrel calls** in preparation.
The old budgets remain exhausted; root `AGENTS.md` requires fresh approval of this
exact case before executing it. Approval would authorize the bounded adapter
experiment, not scientific dev3/H0–H4 adoption or a release. Earlier numerical
FAILs, unknown chemistry and the joint AMP/hemolysis limitation remain unchanged.
Retain resources through 2026-11-13.

The [existing consumer work update](https://github.com/uibcdf/peptidemt/issues/8#issuecomment-6618254454)
was fetched back and verified exactly; its
[publication receipt](evidence/hydramp_execution_adapter_issue_update.json)
retains the final body and proposal identity. Publishing the plan is not execution
approval.

## First approved attempt and parent-limit correction — 2026-11-03

The investigator approved plan
`1d4679f27d06d95bd402b1f9239e8dc1fc5120a722da5057be526220985da665`.
The [authorization](evidence/hydramp_execution_adapter_authorization.json) and
[failed execution receipt](evidence/hydramp_execution_adapter_failed_execution.json)
preserve the actual attempt. The API returned an incomplete receipt with
`worker_preflight`, `ValueError: not allowed to raise maximum limit`, zero rows,
no confirmed native operation and attribution `not-executed`.

**Cause:** this qualification harness set both soft and hard parent `RLIMIT_AS`
to 1 GiB. The worker inherited that 1 GiB hard ceiling and could not establish
its requested 8 GiB limit. The error occurs before the worker calls the provider,
loads checkpoint/PCA or computes descriptors. It is a qualifier resource-composition
defect; no numerical regression or sibling defect follows. The public adapter
correctly returned explicit failure rather than inventing scientific output.

The original runner exited cleanly after storing that failed receipt. Its process
exit code alone did not establish scientific success; inspection caught the
incomplete result. The corrected runner now propagates incomplete/failed case
status while retaining observations. This changes no scientific tolerance or
acceptance criterion.

The corrected qualifier enforces **parent soft 1 GiB, hard 8 GiB**, permitting its
worker to inherit and set the already proposed 8 GiB ceiling. The parent's active
allocation ceiling remains 1 GiB. These are virtual-address controls, not RAM
allocations; the 4 GB RAM intent and 2 GiB aggregate sampled-RSS stop are unchanged.
No consumer/provider package, numerical method, model, SDK or installed environment
was changed. The exact consumer wheel remains
`18b1cb18b9662092203aad9c64d45bc0d61a862577297c13a664572dbdbc3e83`.

Four model-free qualifier checks pass, including
`devtools/tests/test_hydramp_execution_qualification.py::test_parent_soft_limit_preserves_inherited_worker_hard_ceiling`.
Real tiny stdlib processes verify the parent soft/hard pair and successful child
limit setting without allocating those bytes or importing scientific providers.
The other new guard prevents a failed scientific case from being reported as
success merely because its process exited normally. The actual failed startup
took 1.12 s / 56.1 MiB aggregate sampled RSS; this is **not an inference benchmark**.

The old plan/source/attempt files remain retained, including the exact original
runner under `local_data/hydramp-execution-adapter-vceg9u_2/failed-first-attempt/source/`.
One public API attempt was used; checkpoint/PCA loads, neural forwards, descriptor
bundles, Macrel calls and retries are all **zero**. The original attempt is not
erased or repeated under its no-retry authorization.

The corrected proposal is
`local_data/hydramp-execution-adapter-vceg9u_2/live-plan-corrected.json`, SHA-256
**`31317bd3023165300d9558134e73c584a3bdfa25e2c619a200cff11c65c33608`**.
Its new `corrected-real-run` directory has no authorization or model-attempt file.
The only changed executable inputs are the qualification runner and its tests;
the complete 345-file runtime/artifact manifest and both inventories pass preflight.
It requests **one new API attempt** of the same 16 proposals/seed 1001, three
neural forwards, one checkpoint/PCA load/inverse and one descriptor bundle,
with zero Macrel/legacy/GPU/network/retries. Original active CPU, wall, RSS and
disk/output limits remain as proposed above. Fresh investigator approval is
required before that new attempt. Broader scientific disposition remains pending.

The [fix receipt](evidence/hydramp_execution_parent_limit_fix.json) preserves the
four model-free guards and unchanged candidate identities. The
[existing issue update](https://github.com/uibcdf/peptidemt/issues/8#issuecomment-6618529710)
was fetched back and verified exactly; its
[publication receipt](evidence/hydramp_execution_parent_limit_issue_update.json)
does not authorize a second execution.

## Corrected installed public case completed — 2026-11-03

The investigator explicitly approved corrected plan
`31317bd3023165300d9558134e73c584a3bdfa25e2c619a200cff11c65c33608`.
Its [authorization](evidence/hydramp_execution_adapter_corrected_authorization.json)
and [execution receipt](evidence/hydramp_execution_adapter_corrected_execution.json)
preserve the exact single new attempt. The frozen plan and both installed
packages were unchanged. The earlier failed startup remains a separate record;
this success does not rewrite it.

The real installed `generate_hydramp` call completed with **16 proposals, seed
1001**, no failure or receiving issue. All native rows, original order/indices
and the complete original trace match the retained H4 seed-1001 receipt exactly,
including PCA and decoder-input evidence. Saved JSON replay is exact. This checks
faithful receiving from the same modern provider, not equivalence to every
legacy result. The real parent Ackredit session captured seven bibliography
records; the original implementation is reference-only, not executed TensorFlow.

Actual allowance consumed: one public call, one numeric PCA load/inverse, one
checkpoint load, one decoder plus one AMP and one MIC forward (three neural
forwards), and one descriptor bundle. The worker journal confirms all seven
single operations. **No Macrel, legacy, GPU, network, retry or new candidate.**

The supervised whole case took **8.358 s** and peaked at **453,214,208 bytes
(432.2 MiB)** aggregate sampled process-tree RSS; launcher including preflight
took 9.289 s. Worker kernel high-water RSS was 419,319,808 bytes (399.9 MiB).
Retained output at supervision completion was 205,373 bytes. Actual worker
controls confirm CPU 0/1, nice 10, one Torch/inter-op thread, CPU-only build
and 8 GiB virtual-address ceiling. The 4 GB RAM intent, 2 GiB sampled-RSS stop,
180/210 s limits and host/disk floors were respected. Sampled RSS is not a hard
kernel reservation or a general performance benchmark.

This closes the real execution gap for **this exact local adapter/bundle/case**.
The corrected call budget is exhausted. Broader dev3/H0–H4 scientific acceptance,
package publication, other hosts/seeds and biological effectiveness remain
unqualified. Earlier numerical/ranking findings and the retained H4 pool's lack
of a joint AMP-positive/NonHemo hit are unchanged. No scientific threshold,
chemistry, selector or accepted decision was changed. Retain resources through
2026-11-13.

The [completed consumer issue update](https://github.com/uibcdf/peptidemt/issues/8#issuecomment-6618614382)
was fetched back and verified exactly. Its
[publication receipt](evidence/hydramp_execution_adapter_corrected_issue_update.json)
preserves the bounded outcome without claiming broader acceptance or more calls.
