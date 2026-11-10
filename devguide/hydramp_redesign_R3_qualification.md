# HydrAMP redesign R3: installed consumer qualification

Status: **authorized exact case executed once; finite technical receiving PASS**,
2026-11-04. Consumer: [PeptideMT #32](https://github.com/uibcdf/peptidemt/issues/32).
Provider: [HydrAMP #4](https://github.com/uibcdf/hydramp/issues/4).
The [D45 contract](hydramp_redesign_work_order.md) commissions the delivered
[R1/R2 implementation](hydramp_redesign_implementation.md). It explicitly keeps
real R3 separate. Preparation was followed by explicit investigator execution
authorization; the outcome below consumes that separate allowance and does not
establish new scientific acceptance.

## Exact reviewable experiment

Retained task: `local_data/hydramp-redesign-R3-yq620q_v`.
Its `plan.json` is 97,791 bytes, SHA-256
**`7a55b24e8c5d2cc105274e54dec83cf442f80b28211d0f297f55d6c2b1216974`**.
The [preparation receipt](evidence/hydramp_redesign_R3_preparation.json) records
the exact files, source/prefix checks, preserved preparation failures and host.
The task-specific [operator](../devtools/hydramp_redesign_r3.py) has eight
[engine-free authority/budget guards](../tests/test_redesign_r3_operator.py).
At preparation closeout neither an authorization record nor a scientific run
directory existed. The later [execution authorization](evidence/hydramp_redesign_R3_authorization.json)
binds the unchanged plan; the [execution receipt](evidence/hydramp_redesign_R3_execution.json)
records the single completed run and exhausted allowance.

Use the eight structural prototype occurrences from the accepted
[A2 fixture](hydramp_analogue_A2.md), in exactly their existing provider order:
`A`, `ACDEF`, `KKKKKKKKKK`, `ACDEFGHIKLMNPQRSTVWY`, 25 leucines,
`RKRKRKRKRKRKRKRKRKRKRKRK`, and repeated occurrences of the third/fourth strings.
There are six distinct strings, without measured activity labels. Add an
incomplete parent at original occurrence 1 and an explicitly annotated `ACD`
parent at occurrence 5. Both remain incompatible. Compatible original indices
are `[0,2,3,4,6,7,8,9]`; duplicate headers/source/context remain distinct.

Fix **seed 431, temperature 1.0, two attempts**, B=8 and N=16, with the unchanged
native improvement rule, `properties=False`, no additional filters. This repeats
one request through a new consumer boundary to check receiving; it does not
repeat the legacy/modern A2 numerical campaign or broaden its population claim.
The cached A2 case has one distinct returned candidate and empty duplicate-parent
buckets. Its sparse coverage remains a limitation, irrespective of R3 outcome.
Do not change seeds or refill an empty pool to obtain a more favorable result.

## Frozen artifacts and two installed profiles

Both new prefixes install the unchanged R1/R2 consumer wheel
`peptidemt==0.1.0+unknown`, SHA-256
`9104ad927b1cb113e98a72063193fc2d309ceb3a109900d3a6e02ea2882a437b`.
The version is the declared versioningit fallback, not a new commit/release.
Complete installed Python sources match each other and the maintained source.
Do not substitute the shared editable metadata or relax the worker identity gate.

| Profile | Exact reused boundary |
| --- | --- |
| `generation/bin/python` | Python 3.14.7, 21 distributions, NumPy 2.4.6, CPU Torch 2.15.0+cpu, HydrAMP 0.0.0.dev6 |
| `assessment/bin/python` | Python 3.14.10, 99 distributions, Macrel 1.6.1, CPU ONNX Runtime 1.25.1, NumPy 2.5.4, source-built MolSysMT 0.23.0+286.g3781031d0, Ackredit 0.9.0 |

The provider wheel is unchanged, SHA-256
`1ceb810546c8efe4736d12f67f34d04a0acb1c61440d4a8dcbf961bdd8de0b2a`.
R1/R2 already prove its seven numerical/runtime modules unchanged from dev5;
the owner codec and receiving integration are the new qualification boundary.
Reuse the original publisher-attributed epoch-37 checkpoint, complete 59-file
manifest/42 arrays, original source `6590d2f4c2963f25d30669052a4c4a857e0e7279`
and starter `7804df862872ccc6d09fe01c41bafbca194cfa31`. No PCA or descriptors.

Dependency payloads reuse the retained R1/R2 and W3 installations by symlink with
faithful metadata. New wheels install offline with no dependency solving. These
are controlled local profiles, not public installation qualification. Both
dependency checks pass. All 30 consumer files in each prefix, 13 provider files
and 3,346 MolSysMT files match their wheels, excluding generated RECORD entries.
Macrel's four scientific source files and two compressed models match accepted
W3 evidence. The plan pins 252 files, including metadata, installed RECORDs,
guards, interpreters, source/operator tests and the resolved `uname` executable.
Every stage rechecks complete inventories, source and checkpoint identity.

The original W3 and R1/R2 prefixes, shared profile, legacy reference, checkpoint
and primary sister worktrees remain intact. Shared development continues on its
named profile. The frozen source-built MolSysMT qualification route is separate
from ordinary editable MolSysMT at `71fbe4f46d3c70e4e973c8025f01752a8c9b1084`.
The suite-status snapshot preserves PeptideMT's concurrent dirty work and the
behind-main MolSysMT/Ackredit checkouts. This task does not update their APIs or
requalify their complete products. The seven known shared AmberTools dependency
findings remain owned by [MolSysSuite #82](https://github.com/uibcdf/molsyssuite/issues/82).

## Prospective receiving and scientific limits

Run six sequential stages, stopping at the first failure:

1. Direct owner codec/loaders/generator: seven neural evaluations, observed before
   dispatch and confirmed on return.
2. Installed `redesign_hydramp`: the identical request, seven evaluations.
3. Installed repeat: another seven evaluations. Require exact detached trace,
   original parent/submission order, outcomes and child links across all three.
4. One Macrel batch with the four accepted W3 controls; both native output scores,
   labels and categories must match the retained values exactly.
5. Separate Macrel parent baseline: eight compatible occurrences, preserving all
   ten parents and their incompatible diagnoses. Parents never enter selection.
6. Macrel assessment of adapter-returned proposals only, at most 16 compatible
   occurrences. Require unchanged correspondence and complete native rows/scores.
   Replay both existing selectors at k=4 with identical ranking, selected,
   unselected and excluded occurrences after exact saved-result deserialization.

Maximum: **three HydrAMP calls / 21 network evaluations plus three Macrel calls /
six ONNX evaluations = 27 evaluations**. Each analogue call contains two encoder
forwards, one decoder forward and two evaluations of each classifier. On an
empty/all-incompatible child pool, `assess_macrel` launches no worker, consuming
zero child ONNX evaluations. Successful preceding stages then total 25. Keep
no-hit/incompatible evidence and report incomplete real candidate-composition
coverage; unused budget is not a new sampling or diagnostic allowance.

Retain native AMP/MIC values and Macrel AMP/hemolysis values as different model
outputs. Compare parents/children by original occurrence and ancestry, without a
Macrel-improvement requirement, combined reward or biological success threshold.
Exact direct/adapter identity is a consumer criterion; old TensorFlow probability
FAIL and near-tie observations remain unchanged. No numerical tolerance is
relaxed, old approximation copied or general legacy equivalence asserted.

The completed adapter should retain actual optional Ackredit capture in this
host. Absence/failure remains explicit and never destroys completed scientific
results. The model-free probe verifies Ackredit 0.9 capture from a **declared
controlled completion state**, not new executed network operations. Saved
receiving/selection continue without scientific engines. Digests and declared
roles do not authenticate a producer.

This small structural case cannot establish population quality, empirical AMP
activity, safety, useful optimization, superiority or another family's validity.
Existing R1/R2 artificial evidence remains necessary for nonempty duplicate-parent
buckets and failures not covered by this finite real case.

## Fresh shared-host proposal

The recorded machine has one Intel Xeon E5-2630 v4, **10 physical cores/20 logical
CPUs**, 30.68 GiB total RAM, about **13.3 GiB available** at final preparation and
about 2.29 TiB free disk. Swap availability fluctuates with concurrent work; this
plan relies on MemAvailable and its stop guard, not on reclaiming other users'
swap. Recheck immediately before execution and continuously while supervised.

- CPU only, affinity `{0,1}`, nice 10, one numerical/ONNX/Torch thread and one
  Torch inter-op thread; ONNX uses CPUExecutionProvider and sequential execution.
- One scientific worker at a time. Count its supervising host and sole child
  together: stop on sampled tree RSS above **2 GiB**, within the investigator's
  **4 GB task RAM intent**. This is sampled enforcement, not a hard RSS ceiling.
- Per-process virtual-address ceiling **8 GiB**; Macrel child ceiling **4 GiB**.
  Virtual address space is not resident RAM.
- Six stages, **120 s each / 720 s maximum total**; nested adapter/Macrel child
  timeout 90 s. No automatic retries, refill or extra diagnostic forwards.
- At least **8 GiB host MemAvailable** and **1 GiB free disk** before each stage;
  stop if available RAM drops below the floor. Output maximum 128 MiB per stage,
  768 MiB across stages, excluding unchanged prefixes/assets.
- Network/shell blocked. The guard permits the two fixed Python interpreters and
  one pinned read-only `uname -p` query per Python process, used by Python/h5py
  platform discovery: up to 11 Python hosts/workers and 11 additional read-only
  query children across the scientific stages. These are not
  neural evaluations. Learned-asset access is refused until an exact separate
  investigator authorization exists. Exclusive run/log markers prevent reentry.

These bounds are suitable for this finite CPU receiving case given the recorded
available resources and previous A2/W3 peaks. They do not reserve resources on
the shared host or qualify larger workloads. No GPU query or GPU use occurred.

## Preparation outcomes and preserved failures, before authorization

**Zero new pretrained/model/Macrel calls**, zero PCA/descriptors, no scientific
authorization or real run created. Eight new operator tests pass. Model-free
probes establish the owner codec, MolSysMT serialization of eight occurrences,
cached-A2 parent mapping, declared artificial assessment/selection replay,
empty/incompatible receiving, incomplete-trace rejection, absent-approval refusal
and actual Ackredit capture for a controlled completion state.

All preparation failures remain retained locally. They do not implicate providers:

- The profile collector initially assumed wheel METADATA for two old egg-info
  distributions. It now faithfully reads their existing PKG-INFO; no dependency
  metadata or provider code was rewritten.
- The first log wrapper lost an exception after closing its redirected stream.
  The operator now retains the traceback before restoring streams.
- An overrestrictive local guard blocked Python/h5py's `uname -p`, which surfaced
  through lazy form registration as `KeyError('file:h5msm')`/ArgumentError for
  `A`. Read-only diagnosis traced the cause to the guard. A further guard check
  incorrectly compared a resolved executable with an unresolved `/usr/bin/uname`
  symlink. Correcting that guard restored unchanged MolSysMT conversion.
- The report tried `dataclasses.asdict` on immutable provenance containing a
  mappingproxy. Reporting now reads the scalar/tuple Selection fields; the core
  evidence codec, selector policies and immutable data remain unchanged.

The successful eight-record transport is reused for the final remaining checks;
accepted source/installed suites and the A1/A2/W3 campaigns were not rerun.
No provider issue is warranted for errors introduced solely by this local
preparation harness. Existing #32/#4 carry the outcome. Source remains local and
uncommitted; there is no package release, new model adoption or author contact.

Retain all new local data under those owning issues; review by **2026-11-18**.
Existing local research/use conditions and attribution apply. Original Drive
byte-identity, redistribution/commercial/output-rights and empirical-use limits
are not resolved by successful execution. No training, feedback, targets, new
family, model/package redistribution or public release is included.

## Executed outcome and interpretation

The investigator authorizes proceeding in direct response to the exact R3
question. Authorization SHA-256:
`4febd7eb91da789465809870f13ca8ef45102e840bb4da3d893c1bebaaa0e3c0`.
All frozen files, complete source/inventories and checkpoint bytes match again
before and after execution. The original plan remains unchanged, including its
prospective criteria. **All 27 evaluations are consumed; none remain.**

| Prespecified receiving criterion | Actual outcome |
| --- | --- |
| Native / installed adapter / installed repeat | Full detached traces, parents, submitted order, outcomes and child links exactly equal; 7+7+7 evaluations complete |
| Original parent correspondence | All ten parents retained: eight compatible, two incompatible, seven compatible no-hit buckets and one nonempty bucket |
| Existing W3 controls | All four complete Macrel rows exactly match retained values, with both CPU ONNX heads |
| Parent and returned-child assessment | Eight parent rows and one child row; incompatible parents remain explicit; complete native features/predictions retained |
| Existing selectors | Both k=4 rankings/selectors return the sole child, `input-0`; no parent promotion, threshold, deduplication or refill |
| Attribution | Actual completed adapter, repeat and all three Macrel calls capture through Ackredit 0.9; detached bibliography survives fresh readers |
| Saved receiving | Fresh process with scientific/Ackredit imports, parameter reads, network and children blocked exactly replays the receipts, assessment and selectors |

The six supervised stages take **33.3768 seconds total**, with maximum sampled
host-plus-child tree RSS **569,028,608 bytes (542.67 MiB)**. Stage times are
3.3068 / 4.0952 / 3.8331 / 7.4784 / 7.3666 / 7.2966 seconds. No guard stop,
failed stage, retry or additional diagnostic inference occurs. The original
reference is not executed; no PCA, descriptors, training or GPU is used. These
different workloads are not a speed comparison against original HydrAMP.

There is one returned occurrence/one distinct string, from original parent 6,
provider index 4, attempt 0, raw trace row 4: 25 leucines become
`LLLLLLLLLLLLLLLLLLLLLLLKL`, a substitution L→K at one-based position 24.
The paired saved observation is:

| Model output | Parent | Child | Interpretation within that model |
| --- | ---: | ---: | --- |
| HydrAMP AMP score | 0.9999840259552002 | 0.9999926090240479 | Native strict improvement |
| HydrAMP low-MIC-class score | 0.99953293800354 | 0.9996746778488159 | Native strict improvement; not a measured MIC |
| Macrel AMP probability | 0.574257493019104 | 0.29702985286712646 | Lower, changing native AMP label true→false |
| Macrel hemolysis probability | 0.3168318271636963 | 0.4851486086845398 | Higher; both labels remain NonHemo |

Thus the integration passes its technical receiving criteria while this case
provides **no evidence of useful redirection under Macrel's two outputs**.
The selectors still return the child because the agreed policies rank eligible
rows without requiring an AMP-positive label. Selection is not a biological
recommendation. Neither model establishes the child's actual activity or safety.

Guarded saved-only analysis also finds the complete R3 detached trace exactly
equal to the retained modern A2 trace, and all eight ordered returned-string
buckets equal to the saved original A2 outputs. The unfavorable Macrel
observation therefore concerns the same sole string already produced by the
original. It does not identify a new modernization-specific sequence regression
or establish which predictor is biologically correct. No original forward or
descriptor is repeated, and its unequal raw scores/probability FAIL remain.

The single homopolymer-derived candidate, six distinct structural prototypes,
empty duplicate-parent buckets and saturated native scores leave scientific
utility, diversity, general equivalence, efficacy and safety unqualified.
The prospective comparison in [HydrAMP #3](https://github.com/uibcdf/hydramp/issues/3)
should include separate paired native/external predictions and independent
evidence/endpoints, preserving unsuccessful outcomes. Its design and any later
execution remain separate work; this result supplies no additional call budget.

No provider/core policy change follows from this disagreement. D44/dev5
acceptance, D45/R1/R2, the original numerical limitations and every installed
artifact remain unchanged. This is a bounded installed-consumer result, not
automatic scientific adoption of dev6, a public installer/release, general
platform qualification or completed independent HydrAMP product review.
