# HydrAMP real-checkpoint comparison proposal

Status: **authorized and executed; decoder probability comparison failed**, 2026-10-30.
Existing commission: D38/D39, PeptideMT #8. The
[preparation receipt](evidence/hydramp_pytorch_parity_preparation.json) pins the
exact local plan, tool, installations, artifact identities and checks.
This is a diagnostic implementation comparison, not HydrAMP acceptance or H2
completion. The historical preparation below loaded no real model/PCA; the later
[execution report](hydramp_pytorch_comparison.md) records the authorized six
evaluations, one PCA load and actual resources. Tokens/strings match exactly,
but decoder probabilities exceed the unchanged tolerance. No retry occurred.

The investigator approved proceeding with a **4 GB physical-RAM task budget**
after the resource clarification. The tighter 2 GiB sampled worker RSS stop and
sequential execution remain. The [authorization](evidence/hydramp_pytorch_parity_authorization.json)
pins the approved plan separately; the original pending proposal is preserved.

## Bundle and use presented for approval

Reuse the 65 retained official-starter files at
`7804df862872ccc6d09fe01c41bafbca194cfa31`, already acquired under the
[asset manifest](evidence/hydramp_reference_assets.json). The byte-only preflight
matches that manifest. Reference source is unchanged upstream
`6590d2f4c2963f25d30669052a4c4a857e0e7279`. The PCA hash is
`a3a5dcea04e91421be363c047249b93fa46e99e128aec929e1f6b0f0e488a26d`.

The publisher attributes this starter checkpoint/PCA to HydrAMP epoch 37.
Original Drive archive byte parity remains unverified; compare these exact
starter bytes without claiming broader archive equivalence. Retain original
University of Warsaw MIT notices and method/software attribution. Proposed use
is bounded local research comparison, with no training data, redistribution,
commercial/output-rights clearance or scientific adoption. The
[existing local-use review](hydramp_environment_review.md#exact-inputs-and-local-use-review)
retains licence texts, archive metadata and partial PCA inspection separately.
That inspection is not a safe-deserialization certification.

Reference: the existing isolated Python 3.8.20/TF 2.2.1/Keras 2.3.1 worker,
61 distributions and 41 unchanged installed source files. The proposal retains
its eight known native metadata discrepancies and zero discrepancies under the
official inference profile. Candidate: the previously tested installed wheel
`hydramp-torch==0.0.0.dev0`, Python 3.14.7/PyTorch 2.15.0+cpu/NumPy 2.4.6,
18 distributions, wheel SHA-256
`738377ef8943fa79456d54747fd4f19a00a6194eeb07a9d57adac37e19903e1d`.
Both installed inventories and source hashes are pinned; no dependency changes
or shared-environment installation are needed.

## Requested execution

Use one fixed 12x64 float64 latent fixture in both workers, with native AMP
conditions `[1,1]`. Fixture bytes are pinned; their construction does not qualify
legacy RNG equivalence.

| Operation | Legacy worker | PyTorch worker |
| --- | --- | --- |
| Original PCA pickle load | 1 | 0 |
| PCA inverse transform | 1 | 1, from exported numeric coefficients |
| Model construction | 1 original loader, including its unused encoder graph | 1 selected inference core |
| Decoder forward evaluation | 1 x 12 rows | 1 x the same 12 rows |
| AMP head evaluation | 1 x 12 original decoded token rows | 1 x the reference's original token rows |
| MIC head evaluation | 1 x 12 original decoded token rows | 1 x the reference's original token rows |

Total: **six network evaluations**, twelve rows each, producing twelve paired
decoder outputs. There are zero encoder forward evaluations, native
`unconstrained_generation` API calls, descriptor calculations or Macrel calls.
This is a fresh additional comparison budget, not a hidden use of the H2
four-call/52-output design.

Proposed diagnostic tolerances: PCA/conditioned coordinates `atol=rtol=1e-10`;
float32 probabilities and scores `atol=2e-6, rtol=2e-5`. Tokens and strings must
match exactly in occurrence order. Invalid/nonfinite outputs fail; a changed
argmax fails even with small probability errors. No tolerance relaxation,
deduplication, re-encoding, repair, refill, retry or automatic acceptance follows.

## Shared-host limits presented for approval

An additional [memory preflight](evidence/hydramp_memory_preflight.json) measures
guarded imports in the two isolated workers: approximately **348 MiB resident
RAM for the legacy stack** and **250 MiB for the CPU PyTorch core**, sequentially.
All native numeric weight files together occupy approximately 3.52 MiB. No model
was constructed and no real checkpoint/PCA opened for deserialization, so actual
inference peak RSS is still unmeasured. An 8 GiB task RAM allocation is expected
to be ample for this fixed comparison; retain the more conservative 2 GiB sampled
RSS stop and measure the real peak during the authorized attempt. The 8 GiB
virtual address-space ceiling is not a reservation of 8 GiB physical RAM. This
finding does not change the pinned plan or grant model-execution approval.

Preparation observes 20 logical CPUs, approximately 30.7 GiB RAM with 15.6 GiB
available, and 2.3 TiB free disk. Swap is almost full; current memory-pressure
averages are zero. These are observations, not reserved resources.

- Two workers **sequentially**, affinity CPUs 0,1, one native thread, nice 10.
- **180 seconds per worker**, at most 360 seconds across both.
- **8 GiB virtual address space** per worker; stop above **2 GiB sampled RSS**.
  The watchdog polls every 0.1 seconds; RSS is a sampled stop, not an instantaneous
  kernel cap.
- Require **8 GiB available RAM** before and during a worker, and 1 GiB disk
  free before starting. Stop above 128 MiB task outputs.
- **No GPU, network, concurrent scientific worker or automatic retry**.

The provider owns the tool at `ports/pytorch/devtools/parity.py` and detailed
runbook `devguide/pytorch_parity_qualification.md` in the local
`peptidemt-pytorch` worktree. Each stage records a single attempt; a failure
stops progression and requires review before any new budget. The supplied plan
digest binds command inputs, not human approval. The original preparation ran
no model command; the later authorized execution is recorded separately above.

## Preparation checks and remaining limits

Eleven new synthetic tests pass for meaningful numerical differences, changed
argmax, invalid output and refusal of a wrong plan hash. Python 3.8 syntax and
byte-only preflight pass. The earlier 25 installed-core tests are preserved
without rerunning unrelated qualification. Preliminary syntax/interpreter
selection mistakes were caught before any model load, corrected and recorded
in the receipt; the initial failed command log is retained.

The approved stages have now run once; their allowance is exhausted. Before any
new model execution, prepare and obtain a separate diagnostic budget. Even a
passing comparison would still leave native
RNG, original `properties=True` descriptors, pandas sorting/ties, full provenance,
PeptideMT adapter and H0–H4 acceptance pending. D35–D37 and M1–M8 remain unchanged.
