# HydrAMP decoder localization: next execution proposal

Status: **authorized and executed; divergence localized to the GRU path**, 2026-10-30.
The [first real-checkpoint experiment](hydramp_pytorch_comparison.md) remains
failed: eighteen decoder probabilities exceed tolerance while all tokens match.
D39 and existing PeptideMT #8 own this continuation. The investigator requested
proceeding with localization; the previous six-call allowance remains exhausted.

## Executed diagnostic outcome

The investigator explicitly approved the pinned two-forward plan
`8f87fe9711767297e4de063bde1e6a6cc6de1103d9b4df55bc895596315d020e`.
Both workers completed once, without a resource stop or retry. Their final
probabilities are **bitwise identical to their own previous saved outputs**:
instrumentation endpoint error is zero in each framework, and all tokens remain
exact. The [execution receipt](evidence/hydramp_decoder_trace_execution.json)
preserves the four captured tensors, authorization, inputs and measurements.
The aggregate outcome and isolated candidate preparation are
[recorded in existing PeptideMT #8](https://github.com/uibcdf/peptidemt/issues/8#issuecomment-6535704181).

| Stage | Maximum absolute difference | Elements outside the unchanged tolerance |
| --- | --- | --- |
| Autoregressive GRU sequence | 1.6391277313232422e-5 | 25 |
| LSTM sequence | 1.6123056411743164e-5 | 93 |
| Dense logits | 1.5163421630859375e-4 | 161 |
| Final probabilities | 4.845857620239258e-5 | 18 |

The earliest observed nonzero difference is already at GRU timestep 0 (maximum
`1.1175870895385742e-6` there), before the LSTM. GRU outputs first cross their
diagnostic threshold at timestep 11; downstream stages can exceed their own
threshold earlier because these are different variables/scales. This localizes
the path without proving which GRU operation/backend is responsible. The original
18/6300 probability failure is unchanged; no tolerance or scientific acceptance
is altered.

Legacy and PyTorch worker wall times were 8.48 s and 2.05 s respectively. The
maximum conservative sampled worker-plus-supervisor RSS was **472.94 MiB**,
inside the authorized 4 GB envelope. No new PCA load, classifier evaluation,
descriptor, Macrel call or GPU computation occurred. The old TensorFlow binary
again logged a failed CUDA driver probe, with execution pinned to CPU/Host.

The source-supported grouping hypothesis now has a separately prepared
[GRU-layout candidate](hydramp_gru_candidate.md): one recurrent update/reset
matrix product as in Keras implementation=2. It is not an accepted correction
and has since failed its separately approved one-forward real validation. The
failed dev0/dev1 artifacts, completed experiments and original worktree remain
intact. An independent numerical-reference proposal follows that negative result;
no automatic additional model execution or tolerance change is permitted.

The proposal below is retained as the historical scope of the completed diagnostic.

## Concrete diagnostic

The provider prepares `ports/pytorch/devtools/decoder_trace.py` in its local
`peptidemt-pytorch` worktree. In each framework capture the autoregressive
sequence, LSTM sequence, dense logits and final probabilities during **one**
decoder forward, using the same twelve saved conditioned inputs. Total request:
**two decoder evaluations of twelve rows**, one legacy and one PyTorch.

The legacy diagnostic exposes existing symbolic tensors through a Keras output
view. Its unchanged original loader also builds encoder/head graphs, without
evaluating those networks. The PyTorch diagnostic wraps existing methods to
copy outputs, then restores them even on failure. Neither replaces equations,
activations, precision, weights, conditions or input chemistry.

No PCA object/load/export/inverse transform, AMP/MIC forward, descriptor,
Macrel, native generation-API call, resampling, corrective evaluation or retry.
Use the existing checkpoint/installations and same original licence/local-use
scope. The installed PyTorch wheel remains
`738377ef8943fa79456d54747fd4f19a00a6194eeb07a9d57adac37e19903e1d`;
upstream source remains `6590d2f4c2963f25d30669052a4c4a857e0e7279`.

The saved reference NPZ is pinned at
`ad584797d832b076e9f6e3d95274635b2e6a0cde3ca251810de93da7555de8c7`;
the saved candidate NPZ at
`7746ecc7b721e8ac153e867c05862bd467f43cb0bfb7bbee30a0d2e29533b33c`.
Read the original conditioned 12x66 float64 array directly, with the same
framework float32 input conversion. No new seed/PCA preprocessing is involved.

## What this can establish

Report the first nonzero and first out-of-tolerance difference in the four
stages and timesteps, keeping `atol=2e-6, rtol=2e-5` and exact token checks.
Also compare each traced endpoint against its own prior saved endpoint.
Requesting graph intermediates can affect TensorFlow optimization; if endpoint
drift appears, report that instrumentation/repeatability question before
attributing the original failure. A localized difference alone does not establish
root cause, justify a correction or approve a broader numerical tolerance.

## Same host limits, fresh finite calls

- **4 GB task physical-RAM budget**, one worker at a time, 2 GiB sampled worker
  RSS stop and a separately measured small supervisor.
- CPU affinity 0,1, one native thread, nice 10; **180 seconds per worker**,
  at most 360 seconds combined.
- 8 GiB virtual ceiling, distinct from physical RAM; retain 8 GiB available host
  RAM floor and 1 GiB free-disk preflight. Stop above 128 MiB task outputs.
- **No GPU computation, network, automatic retry or extra scientific call**.

The prior experiment used approximately 511 MiB maximum conservative worker +
supervisor RSS. No larger resource allowance is proposed. The new plan has its
own task directory and one-attempt records; it cannot overwrite or reuse the
previous stage-attempt files.

## Prepared evidence and source preservation

The [receipt](evidence/hydramp_decoder_trace_preparation.json) pins the exact
plan/tool/source hashes and the provider's detailed runbook. The control helper
only gains hash-pinned diagnostic worker/input routing and blocks a diagnostic
plan from accidentally using the old six-call worker. Its exact original
six-call version is retained in that prior task's `source-snapshot/parity.py`;
old receipts/hashes/results are preserved. Scientific source/licence and the
installed wheel are unchanged. No commit or push is claimed.

Twenty-two synthetic pytest cases pass, including the previous eleven comparison
checks and eleven trace/control checks. A separate guarded Python 3.8 probe
captures four tensors from one artificial-weight two-row native decoder forward,
without opening pretrained artifacts; it verifies graph API/softmax association.
Those checks were preparation; the later real diagnostic is reported above.
Its two-forward allowance is now exhausted. Further real evaluation requires a
new finite budget under the [standing agreement](../AGENTS.md).
