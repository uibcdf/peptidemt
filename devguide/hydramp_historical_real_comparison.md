# Historical HydrAMP MIC-head comparison: executed outcome

Status: **fixed finite comparison complete; guarded saved replay passes**,
2026-11-05. Owners: [PeptideMT #32](https://github.com/uibcdf/peptidemt/issues/32)
and our [HydrAMP #3](https://github.com/uibcdf/hydramp/issues/3).
This is local developer scientific evidence, not a new public API, independent
benchmark, general equivalence decision or acceptance of another bundle.

## Authority, exact inputs and providers

The investigator's continuation after the paired-codec checkpoint resumes the
unchanged historical comparison. D49 supplies standing authority for reasonable
routine execution within approved work, with shared-host stewardship. A fresh
bounded execution declaration records its own plan and resource/call limits;
it explicitly claims **no run-specific investigator review**. Earlier failed
attempts and spent allowances remain unchanged. The preparation work order and
old codec-only statuses remain historical, not current blockers or model receipts.

The [execution receipt](evidence/hydramp_historical_real_execution.json) binds:

| Item | Exact identity |
| --- | --- |
| Scientific contract | [Fixed work order](hydramp_historical_real_work_order.md), SHA-256 `1b08e464261a3190bff886e26fe42dd826903ec89a09a9beb91d0de611fc5972` |
| Qualified inputs and code | [D48/D49 codec checkpoint](hydramp_historical_real_implementation.md); frozen plan canonical SHA-256 `3aa4c156e05a26edf84da393c8d411ad04120194658e7e1006d87f52b4f33621` |
| Execution declaration | SHA-256 `73000e443ea1473a02a6f63ff3590e4a1097c20eea82ee874145ccc77415f542` |
| Original reference | Commit `6590d2f4c2963f25d30669052a4c4a857e0e7279`; retained Python3.8.20 / TF2.2.1 / Keras2.3.1 / NumPy1.18.5 profile |
| Modern candidate | `hydramp-torch==0.0.0.dev6`, wheel SHA-256 `1ceb810546c8efe4736d12f67f34d04a0acb1c61440d4a8dcbf961bdd8de0b2a`; retained Python3.14.7 / Torch2.15.0+cpu / NumPy2.4.6 profile |
| Learned assets | Same epoch-37/starter checkpoint: 59 files /3,699,734 bytes, all opaque hashes verified before execution |
| Saved learned comparison | 463,992 bytes, SHA-256 `3c3f6f97e41b0e0b697dcf5cd287f0a9e2ea2733763c671504b08e9ecddb458c` |

All D46 observations and D47 endpoint definitions remain unchanged: **42 source
observations /39 literal-string groups**, with primary **38 groups: 12 active,
26 inactive**. The endpoint is reported E. coli ATCC 25922 MIC ≤32 µg/mL.
Hydraganan-2 retains conflicting observations and the same two shared-class
ambiguity scenarios. Original int32 and modern int64 owner-produced [39,25]
inputs retain identical token values and their separate native bytes.

The same retained local-research use conditions apply. Original-Drive byte
identity, broader checkpoint provenance and redistribution/output-use questions
remain unresolved. No new download, installation, asset/sequence publication,
commit/push, release or external contact occurred. The installed model source
and interpreter inventories match their frozen identities; no sibling worktree
was changed. Official status inspection found a dirty PeptideMT worktree and a
clean but behind MolSysMT clone; both were preserved. No molecular operation
requiring a new MolSysMT route is introduced.

## Executed requests and results

One original worker then one modern worker each loaded its model once. Each
completed `primary_full` (39), `repeat_full` (39), `split_first` (20) and
`split_last` (19), in the prescribed order. There were **eight API calls**:
four original MIC forwards, four modern MIC forwards and four unavoidable
modern auxiliary AMP forwards, **twelve charged neural evaluations**. Modern
AMP scores are retained as provenance; no AMP endpoint or result is inferred.
No retries, warm-up predictions, generation, encoder/decoder inference, Macrel,
PCA, training or GPU computation occurred.

The prespecified full primary batch supplies the headline; repeats and split
contexts are diagnostics, never replacements selected after seeing results.
Public `sklearn.metrics.roc_auc_score` uses the unchanged D47 metric profile and
single-thread limit, not a new local AUC implementation.

| Reported-MIC scenario | Groups | Original ROC-AUC | Modern ROC-AUC | Modern minus original |
| --- | ---: | ---: | ---: | ---: |
| Primary stable groups | 38 | 0.6538461538461539 | 0.6538461538461539 | 0 |
| Shared ambiguous group inactive | 39 | 0.6635802469135803 | 0.6635802469135803 | 0 |
| Shared ambiguous group active | 39 | 0.6331360946745562 | 0.6331360946745562 | 0 |

All three contexts yield those same descriptive AUCs. No primary positive–
negative pair changes order or tie status between implementations. A further
data-only check finds **all 741 pair relations across all 39 rows unchanged**,
with no exact score ties in either implementation. These are correlated pair
comparisons, not 741 independent biological cases.

## Numerical differences and repeat/batch diagnostics

Primary scores are not byte-identical: **17 of 39** values differ. Maximum
absolute original–modern difference is **2.384185791015625e-7**, and mean
absolute difference is **3.069608166510872e-8**. Repeat differences are the same;
in the reassembled split context 15 values differ, with the same maximum.
No rounding, tolerance-based equality or rank repair was applied. These are
small FP32-scale differences; this campaign does not causally localize them
to a particular layer or numerical operation.

Each implementation reproduces its full-batch scores bitwise in the scheduled
same-process repeat. Original batch splitting changes four scores, by at most
**1.1920928955078125e-7**, without affecting any primary binary rank or AUC.
Modern splitting preserves every score bitwise. This is a bounded technical
advantage in batch stability for these inputs, not evidence of better biological
prediction. Preserve previous probability/ranking diagnostic failures in their
own panels; this MIC-head result does not reverse them or validate generation.

## Shared-host and receiving evidence

The run used CPU0/1, one numerical thread and one model worker at a time, with
180 s wall /120 s CPU per child, an 8 GiB virtual-address ceiling and a sampled
2 GiB aggregate controller/worker RSS stop. At preflight about 14.9 GiB RAM was
available, with ample workspace disk. Physical RAM intent remains 4 GB; the
address-space limit is not a physical-RAM allowance. Sampling is not a hard
instantaneous RSS guarantee.

| Worker | Wall time | Peak sampled controller+worker RSS | Native exit |
| --- | ---: | ---: | ---: |
| Original | 18.38 s | 444,678,144 bytes (about 424 MiB) | 0 |
| Modern | 3.79 s | 315,277,312 bytes (about 301 MiB) | 0 |

These are operational measurements including startup/loading, not a controlled
speed benchmark. No resource guard fired. The original audit records only
denied `uname -p` metadata dispatch; it executed no extra child. Parameter reads
stay within the exact asset allowlist: 59 original and 37 modern paths.

Paired receiving verifies actual commands, source/runtime/head identities,
native input/output bytes, row correspondence and complete request accounting.
Ackredit captures completed original/modern MIC scoring with detached software
and HydrAMP-paper credit, retaining the already recorded input-encoding credit
inside the plan. The supported existing host bridge is reused; no generic
attribution/persistence framework or MolSysSuite provider reimplementation is
added.

Fresh saved replay recomputes the result while denying model imports, old
provider/weight paths, network and child processes. It matches every cache and
rejects a deliberately modified headline AUC with `comparison_cache`. It creates
no new neural evaluation or attribution credit. Current implementation and test
hashes match the previously qualified **50 passing engineering controls**;
those results are reused, not reported as a newly executed test campaign.
Model receiving/replay is actual new scientific execution evidence, separate
from those engineering controls.

The maintained reader can reproduce the numerical result in the frozen metric
profile without either model runtime:

```bash
python -I -B devtools/hydramp_historical_real.py \
  local_data/hydramp-historical-scoring-m6v0gs0e/scoring/comparison.json
```

Evidence stays in `local_data/hydramp-historical-scoring-m6v0gs0e`, owned by
#3/#32, with retention review by 2026-11-19. Raw source-linked score records,
execution sources, declarations, native logs/exits and all earlier codec
failures remain retained. No successful earlier campaign was rerun.

## Scientific interpretation and remaining work

The modern MIC route preserves the original's observed discrimination and
complete ordering on this finite historical panel, with reproducible outputs
and stable split-batch behavior. It gives additional functional confidence
without changing the modern implementation to imitate legacy approximations.
**The observed discrimination itself is moderate (primary AUC about 0.654).**
Agreement between implementations is different from strong predictive utility.

The panel is selected; some source-pool overlap is known and checkpoint-specific
training/selection exposure remains unresolved. It is not an independent test
set. Twelve positives do not pass the broader unapproved C2 minimum. Assay
conditions, censoring and the source's chemical annotations/unknowns remain
material, while the accepted finite native view does not encode all chemistry.
The reported mass-concentration endpoint differs from the native pooled molar
training target. No experimental efficacy, safety, probability calibration,
general noninferiority or other-family claim follows.

The finite comparison is complete and needs no repeat merely to obtain more
agreement. Broader confidence requires an independently justified data/assay/
chemistry panel, checkpoint-exposure review and prespecified evaluation policy,
not more predictions on these same 39 rows. Independent HydrAMP product review
and modernizing the rest of its approved surface remain separate work under
owner [HydrAMP #4](https://github.com/uibcdf/hydramp/issues/4). Keep #3/#32 open;
accepted dev3/dev5, selectors, D35/M1–M8 and all earlier limitations persist.
