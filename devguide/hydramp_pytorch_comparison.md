# HydrAMP real-checkpoint comparison: executed outcome

Status: **executed; decoder probability fidelity criterion failed**, 2026-10-30.
Owning work: PeptideMT #8, D38/D39. This is a bounded implementation comparison,
not HydrAMP scientific acceptance or completion of H0–H4. The
[execution receipt](evidence/hydramp_pytorch_parity_execution.json) retains exact
inputs, installed artifacts, outputs, logs, measurements and the failed result.
The aggregate outcome is [recorded in the existing issue](https://github.com/uibcdf/peptidemt/issues/8#issuecomment-6535218763);
the full source/report changes remain local and uncommitted.

## Authority, inputs and execution

The investigator explicitly instructed execution after clarifying a **4 GB RAM
budget for the task**, retaining the stricter 2 GiB sampled worker RSS stop.
The [authorization record](evidence/hydramp_pytorch_parity_authorization.json)
preserves the original proposal and the authorized plan. Its SHA-256 is
`275848c194af7a5b49dac9f4e41f8f212e4643f56a56b321b202a41d2d8c9419`.
The unchanged tool SHA-256 is
`686a7d4adbd80058d8689ef185680759f299c2643a6cb4c1dde57ebc1d15cd48`.
The 8 GiB virtual address-space ceiling was distinct from the physical RAM budget.

Source and candidate remain the reviewed upstream
`6590d2f4c2963f25d30669052a4c4a857e0e7279` and starter
`7804df862872ccc6d09fe01c41bafbca194cfa31`. Reused all 65 hash-pinned retained
files, both existing isolated installations and local wheel SHA-256
`738377ef8943fa79456d54747fd4f19a00a6194eeb07a9d57adac37e19903e1d`.
Original source/licence bytes, installed versions and prior receipts remain
unchanged. There is no new commit, push or package publication.

The original PCA was deserialized **once**, only in the Python 3.8 worker.
It reports `whiten=False` and float32 components. Numeric coefficients were
exported once for Python 3.14; that worker did not load the pickle. Both evaluated
the same twelve explicit latent rows with conditions `[1,1]`. Each worker made
one decoder, one AMP-head and one MIC-head forward evaluation: **six total**.
Heads used original reference tokens. No encoder forward evaluation, native
generation-API call, descriptor calculation, Macrel call or retry occurred.

## Numerical results

The original thresholds are unchanged: PCA/conditioned values `atol=rtol=1e-10`;
float32 probabilities/heads `atol=2e-6, rtol=2e-5`; exact tokens and strings.

| Compared output | Maximum absolute difference | Result |
| --- | --- | --- |
| PCA inverse transform | 0 | Pass |
| Conditioned decoder inputs | 0 | Pass |
| Decoder probabilities | 4.845857620239258e-5 | **Fail** |
| All 300 argmax tokens | 0 mismatches | Exact |
| Twelve vocabulary strings, in row order | 0 mismatches | Exact |
| Native AMP scores | 2.980232238769531e-7 | Pass |
| Native MIC scores | 1.1920928955078125e-7 | Pass |

Eighteen of 6,300 probability elements exceed the declared mixed absolute/relative
tolerance, across eight input rows. The first affected position is zero-based
position 4; the largest difference is at row 10, position 7, token 13:
reference `0.41052961349487305`, port `0.41048115491867065`. Mean absolute
probability error is approximately `1.02e-7`, RMS error `1.39e-6`. These aggregate
small errors do **not** override the failed elementwise criterion. The minimum
reference top-two margin is approximately `0.0240` in this fixture; exact decoded
tokens here do not prove equality on other inputs or near ties.

The native head result is qualified only for this fixture and declared numerical
tolerance; it is not bitwise equality, biological activity or score calibration.
The report's overall `pass` remains **false**, and its process exit status is 1.
Both scientific worker processes themselves exited 0.

## Memory and time

Workers ran sequentially with CPU affinity 0,1, one native thread, nice 10,
180-second per-worker limit, 8 GiB address-space ceiling and 2 GiB sampled RSS
stop. No limit triggered. The supervisor separately measured its high-water RSS.

| Worker | Wall time | Sampled worker RSS peak | Conservative worker + supervisor RSS |
| --- | --- | --- | --- |
| Legacy reference | 9.76 s | 488.28 MiB | 511.02 MiB |
| PyTorch CPU | 2.05 s | 284.26 MiB | 307.04 MiB |

Total model-worker wall time was approximately **11.81 seconds**. Adding the
independent supervisor high-water measurement to the sampled worker maximum
gives a conservative estimate, not an instantaneous kernel group measurement.
The observed RAM usage is comfortably inside the authorized 4 GB task budget;
this experiment does not justify moving to another machine for memory reasons.

No GPU computation occurred. The old TensorFlow binary logged opening its CUDA
driver library and a failed `cuInit` probe (`CUDA_ERROR_NO_DEVICE`) despite hidden
GPU visibility; the explicit execution context and available XLA device were CPU/
Host. PyTorch used the reviewed CPU-only binary. Preserve this log observation
rather than claiming the legacy binary never probes a driver.

## Cause analysis and next boundary

Saved-output inspection localizes the observed failure to the decoder probability
path among the compared outputs. PCA/conditioning is exact and both heads pass.
The source review confirms reset-before equations, gate order, condition reminders
and the inspected LSTM equation. It also identifies a concrete operation-layout
difference: Keras 2.3.1 GRU `implementation=2` multiplies the previous state by
the concatenated update/reset recurrent kernels in one matrix operation; the
port performs the two projections separately. The real-number formulas are
equivalent, while float32 kernels, grouping and backend rounding can differ.

This observation is a **candidate explanation, not a demonstrated root cause**.
No saved intermediate hidden states/logits exist from this first experiment, so
the current evidence cannot identify the first differing internal operation or
exclude another reference/port detail. Do not alter the model, switch precision,
change the scientific contract or widen tolerance on that hypothesis alone.

The next informative experiment would capture corresponding autoregressive
states, LSTM outputs, dense logits and softmax values on identical inputs, before
choosing a correction. The current six-evaluation allowance is exhausted; a
separately prepared and investigator-approved diagnostic budget must precede
any new real-model load/evaluation. There is no automatic rerun.
The [two-forward intermediate diagnostic](hydramp_decoder_trace.md) has since
executed under separate approval: endpoints reproduce this experiment bitwise,
and the first observed divergence is already in the GRU. A separate arithmetic-
layout candidate was then separately validated and also failed the original
criterion. Both failures remain preserved; the next proposed diagnostic uses
an independent numerical reference rather than another guessed source change.

The provider's issue board remains disabled; the current consumer finding belongs
in existing PeptideMT #8. Do not contact upstream or modify unrelated components.
Original Drive/starter byte parity, native RNG, descriptors, pandas ordering/ties,
complete provenance, adapter integration and H0–H4 acceptance remain pending.
