# HydrAMP → PeptideMT → Macrel: bounded receiving qualification

Status: **approved bounded execution completed; experimental AMP acceptance under D41**,
2026-11-03. Preparation facts and proposed limits below are retained as history;
the executed result is recorded at the end. The [current acceptance](hydramp_dev3_acceptance.md)
preserves this private experiment's limits and the separate public adapter proof.
Owning work record: [PeptideMT #8](https://github.com/uibcdf/peptidemt/issues/8).
Provider findings: [HydrAMP #1](https://github.com/uibcdf/hydramp/issues/1).

The investigator directs us to preserve independently justified modern results
and explain their differences rather than imitate legacy approximations. The
[activation attribution](hydramp_amp_activation_attribution.md) completes that
finite numerical analysis. It does not establish biological superiority or
approve a new production precision policy. Keep dev3 unchanged and answer the
remaining consumer-receiving question with this small functional experiment.

## Exact candidate and consumer route

The local plan is `local_data/hydramp-h4-qualification-mc6nax6v/plan.json`,
SHA-256 **`f9b8040897079401d75c6ad3afd3b0cfc499350abfc2943a268b37646ba82c2a`**.
The [preparation receipt](evidence/hydramp_h4_preparation.json) retains its exact
bytes, 116 file pins, inventories, preflight and guarded checks. The plan is a
proposal, not an authorization. No actual authorization or scientific-attempt
file exists at preparation closeout.

Reuse `hydramp-torch==0.0.0.dev3`, wheel SHA-256
`81761e0d48d92f0956e0afc28b3b4154f16032de53c666fd2cfbb53606102ed7`,
the original publisher-attributed epoch-37 checkpoint and numeric PCA. Original
HydrAMP source is `6590d2f4c2963f25d30669052a4c4a857e0e7279`; the selected
starter is `7804df862872ccc6d09fe01c41bafbca194cfa31`. Existing local research
use and attribution conditions apply; no new redistribution permission follows.
The original legacy reference, weights, code and descriptors are preserved.

Two sequential workers use the unchanged retained scientific environments:

| Stage | Actual installed profile |
| --- | --- |
| Generation | `hydramp-comparison-qnbdpism/worker`: Python 3.14.7, Torch 2.15.0+cpu, NumPy 2.4.6, modlAMP 4.3.3; 41 distributions |
| Receiving and assessment | `w3-20261028-hNmM4w/qualification-env`: Python 3.14.10, PeptideMT 0.1.0+95.g7a299d1, Macrel 1.6.1, ONNX Runtime 1.25.1 CPU, NumPy 2.5.4, development MolSysMT 0.23.0+286.g3781031d0; 99 Python distributions |

The assessment worker loads only the new private data-receiving module from
source into the frozen installed W3 core. This preserves the accepted Macrel
worker and its scientific dependency closure without changing either environment.
An initial source inspection expected the newer `_molsysmt.py` helper; its absence
was diagnosed as an older core layout. It is not a broken baseline. The relevant
input record definitions match and the result/data/Macrel modules are byte-identical
to the current source. Guarded compatibility checking with an invented trace
and cached W3 results passes in the actual assessment environment.

This is an explicit **source-extension experiment**, not qualification of a new
installed PeptideMT package or public generation API. The task-specific
[driver](../devtools/hydramp_h4_qualification.py) orchestrates owner functions;
it adds no molecular parser, chemical realization, descriptor algorithm or
selection policy. Molecular-system work remains with MolSysMT.

## Scientific questions and finite calls

Generate two batches of 16, seeds **1001 and 1002**, with the existing AMP mode,
`filter_out=False`, `properties=True`, `n_attempts=1`. The owner performs sampling,
numeric PCA inversion, decoding, original-token AMP/MIC scoring and descriptors.
The worker captures returned data and existing intermediates without replacing
their calculations. Compare saved same-provider returns as a reproducibility
observation; do not turn historical legacy identity into a new acceptance gate.

For each batch, receive every occurrence in its native order, retain tokens,
precision, mapping and portable provenance, and require exact same-operation
serialization/replay. Native scores remain native evidence, separate from Macrel.
Unknown molecular termini or stereochemistry remain unknown. Assess unchanged
strings through the accepted Macrel route; retain incompatible proposals and all
failure evidence. The cached fixture predicts two leading-M exclusions, leaving
30 generated strings plus four controls evaluable; actual exclusions must be
reported, not hidden or replaced. No refill or retry is permitted.

The first Macrel call uses the four original W3 computational controls:

1. `FLPVLAGLTPSIVPKLVCLLTKKC`
2. `HGRHVTLKDIVLDLQPPDPVGLHCYEQLVDSSEDEVDEVDGQDSQPLKQHFQIVTC`
3. `AA`
4. `F`

Their native W3 values are frozen in the plan. They check the unchanged assessment
route, including short and negative computational outputs; they are neither a
biological efficacy benchmark nor a competing generator. Stop before later calls
if their native results differ. On each pool apply the unchanged D35 `amp-first`
and `hemolysis-first` selectors at k=4 and verify identical saved-result replay.
Report eligible/excluded counts, rankings and chosen occurrences from the same
pool. Preserve completed results if a later boundary fails.

| Operation | Maximum new allowance requested |
| --- | --- |
| Public generation calls | 2 × 16 requested proposals |
| Decoder / AMP / MIC neural forwards | 2 / 2 / 2, six total |
| Descriptor bundles | 2 through unchanged modlAMP 4.3.3 |
| Numeric PCA | One load, two inverse transforms; no pickle |
| Macrel | Three calls: control 4, batch 16, batch 16 |
| Macrel input / ONNX heads | 36 proposed occurrences maximum / six head executions maximum |
| Retries, legacy calls, training, GPU | Zero |

Reusing retained native smoke, repeatability and numerical-reference evidence
avoids repeating those campaigns. Call ledgers reserve before attempting a call;
an exhausted or failed stage does not authorize another attempt.

## Proposed shared-host limits

The host snapshot at 2026-11-03 20:55 UTC reports an Intel Xeon E5-2630 v4,
10 physical cores / 20 logical CPUs, approximately 30.7 GiB RAM, 15.4 GiB
available and 2.30 TiB free disk. Swap is almost fully occupied. These are
observations, not reservations; resource floors are checked before each stage
and monitored while it runs.

- CPU affinity 0/1, nice 10; Torch/BLAS one numerical thread, Macrel ONNX two.
- Sequential stages: generation ≤180 s, assessment ≤420 s, total ≤600 s.
  Each of the three native Macrel calls retains its ≤120 s timeout within that
  assessment allowance, ≤16 records and ≤8 KiB sequence/identifier input.
- Retain the investigator's **4 GB task RAM intent**. Stop at **2 GiB sampled
  summed RSS of the worker and descendants**, sampled every 0.1 s. Record the
  controller separately. Shared pages may be counted more than once; sampling
  is a protective stop, not a hard kernel resident-memory quota.
- Worker address space ≤8 GiB; each native Macrel child ≤4 GiB address space.
  Virtual-address ceilings are not physical RAM allocations.
- Stop if host available RAM falls below 8 GiB. Require ≥1 GiB free disk;
  stop at 128 MiB task output. No scientific network access or GPU.
- Kill only the task's owned process group on timeout, resource stop, controller
  interruption or worker exit. Stages are exclusive and cannot silently restart.

The almost full swap argues for keeping the conservative RAM stop and available
memory floor, even though current available RAM is sufficient. No environment
installation or other process cleanup is requested.

## Executed preparation and remaining disposition

**34 guarded artificial source tests pass**: 16 receiver and 18 controller/
transport cases, including actual termination of tiny model-free subprocesses.
Published Pytest Receptor 1.2.2 reports 34 passed; native JUnit agrees. The
isolated seven-distribution test worker uses Python 3.14.7, CPU 0/1 and a 1 GiB
address-space ceiling; total startup/test time is 0.87 s, child kernel RSS
high-water about 55.1 MiB. Separate actual-profile compatibility passes in
1.57 s / 39.9 MiB. There are **zero new model, PCA, descriptor or Macrel calls**.
The [earlier saved replay](hydramp_receiving_preparation.md) retains 272 real
saved occurrences and their exact evidence; it is not a live integrated run.

Fresh investigator approval of this exact plan and host/call limits must precede
either scientific stage, as required by the root working agreement. Earlier
model allowances are exhausted. After execution, return the actual ledgers,
resource measurements, received results, exclusions, controls and selections
for H0–H4 disposition. Execution approval does not itself accept dev3 or establish
biological activity/safety, global numerical equivalence or public support.
The private receiving path also does not complete a future packaged optional
backend/API. Retain preparation resources through 2026-11-13; no commit, push,
training, analogue generation, feedback, target/family expansion or release is
part of this proposal.

The [prepared-plan issue update](https://github.com/uibcdf/peptidemt/issues/8#issuecomment-6615276631)
was fetched back and verified exactly; its [publication receipt](evidence/hydramp_h4_preparation_issue_update.json)
retains the published proposal. Publication of the plan is not its approval.

## Approved execution and independent review — 2026-11-03

The investigator approved this exact plan after its complete host/call request.
The [authorization](evidence/hydramp_h4_authorization.json) and
[execution receipt](evidence/hydramp_h4_execution.json) retain the actual
allowance, completed ledgers, outputs, checks and resource measurements. Both
stages pass, with no stop or retry. All 116 scientific/source pins still match
following execution. Original worker environments, model and production code
remain unchanged. The authorized calls are now fully consumed.

| Observation | Control | Seed 1001 | Seed 1002 |
| --- | ---: | ---: | ---: |
| Proposed occurrences | 4 | 16 | 16 |
| Eligible Macrel rows | 4 | 15 | 15 |
| Preserved incompatible leading-M inputs | 0 | 1 | 1 |
| Macrel AMP-positive | 2 | 4 | 5 |
| Macrel Hemo-positive | 1 | 6 | 7 |
| Macrel AMP-positive and NonHemo | 1 | **0** | **0** |

Both new generation batches reproduce the cached dev3 native results exactly.
Independent replay with scientific providers and scientific array imports
blocked verifies all 32 native rows/order/mappings, original latent/PCA/token/
score arrays, FP64 conditioning versus FP32 decoder input, 212 zero-token
positions, per-occurrence provenance and unresolved chemistry. Received inputs
are exactly the inputs retained by the actual Macrel assessments. Neither
excluded sequence is repaired, trimmed, replaced or dropped from the evidence.
The four W3 controls reproduce every native value exactly.

All three Macrel results capture real Ackredit 0.9.0 attribution with five
portable bibliography records each, retaining executed MolSysMT transport,
native features and predictions. Saved reading creates no new execution credit.
Generation provenance retains its source/starter, wheel/checkpoint/PCA digests,
runtime versions, native descriptor parameters and local-use scope. A future
public HydrAMP adapter still needs its own executed optional-attribution boundary;
this private source-extension experiment does not qualify that future API.

Both unchanged k=4 selectors and their complete rankings reproduce exactly after
saved-result reading. The selected occurrence tokens are:

| Pool | AMP first | Hemolysis first |
| --- | --- | --- |
| Seed 1001 | input-0, input-6, input-1, input-9 | input-8, input-14, input-13, input-15 |
| Seed 1002 | input-3, input-2, input-7, input-0 | input-11, input-14, input-6, input-13 |

For **both** batches, all four AMP-first selections are Hemo-positive; all four
hemolysis-first selections are AMP-negative. Across the complete generated pool,
all nine Macrel AMP-positive rows are also Hemo-positive. No generated row meets
the joint pair of native AMP-positive/NonHemo labels in this small fixture.
These are computational predictions using each model's native meanings, not
measured activity or hemolysis. The controls show that the assessment can return
a joint-positive/NonHemo row; their quality is not a generator baseline.

This is a meaningful observed tradeoff, not an execution failure. D35's selectors
are lexicographic preferences, not a guarantee of joint feasibility. Do not
silently impose a new filter, choose a more favorable seed or relabel the native
scores. This small unfiltered sample cannot establish generator efficacy or
biological superiority over original HydrAMP; it also cannot establish a general
failure rate. The modern numerical improvements and the original strict
probability/global-rank FAIL diagnostics remain recorded without threshold changes.

A separate saved-only comparison verifies that these same 32 new sequences, in
native returned order, also match the retained **original HydrAMP** outputs for
seeds 1001/1002. The original output JSON matches its accepted campaign digest
`90c5cff29e21154a9a37d15e8bd481a5098b36ae9ba896f91c2dc12f7a07f7a7`.
Thus the lack of a joint Macrel AMP-positive/NonHemo hit on this fixture is not
evidence of a port-specific sequence regression. This is an inference from equal
sequence inputs and the fixed assessment route, not a new legacy/Macrel run or
a claim of general model quality.

Generation takes **21.80 s** with **400.2 MiB** peak sampled process-tree RSS;
assessment takes **33.96 s** with **553.5 MiB**. Sequential total is **55.76 s**;
controller high-water is at most **26.3 MiB**, measured separately. Retained task
output is about **3.27 MiB**. No resource guard triggers. Actual calls are two
generations, six neural forwards, two descriptor bundles, one numeric PCA load,
two inversions and three Macrel assessments of 34 compatible/36 proposed records
(six fixed ONNX head branches). No scientific call remains in this allowance.

**Disposition for review:** same-operation private receiving, exact replay and
actual Macrel/selector composition pass on this exact bundle and fixture. Final
investigator acceptance of dev3/H0–H4 remains pending. The ordinary public
optional-backend/API and its installed qualification are still future work; this
result is not a package release. Before judging joint AMP/hemolysis utility more
broadly, agree a separate scientific benchmark and acceptance question. No new
benchmark campaign or calls are authorized by this report. Keep resources through
2026-11-13; no commit, push, training, GPU or release occurred.

The [consumer result](https://github.com/uibcdf/peptidemt/issues/8#issuecomment-6616590411)
and [owning-fork follow-up](https://github.com/uibcdf/hydramp/issues/1#issuecomment-6616597432)
were fetched back and verified exactly. The
[publication receipt](evidence/hydramp_h4_execution_issue_updates.json) retains
both bodies and their identifiers; the issues remain open for disposition.

## Subsequent public data API qualification — 2026-11-03

The [next engineering milestone](hydramp_public_receiving.md) promotes the
existing receipt to `peptidemt.HydrAMPReceipt`, rejects ambiguous duplicate JSON
keys and verifies a new local installed wheel using these saved results only.
All original JSON data and both complete rankings survive exact replay.
The historical H4 source bytes are preserved separately; its original execution
is not relabelled as a test of this later candidate. This qualifies the installed
data boundary, not a public generation execution adapter or broad scientific
adoption. Zero new scientific calls follow; the previous allowance stays exhausted.
