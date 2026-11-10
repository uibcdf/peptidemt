# First new module: deterministic HydrAMP encoder proposal

Current status: **D42 approves the contract and E1; installed synthetic checks
pass**, 2026-11-04. See the [E1 outcome](hydramp_encoder_E1.md) for the distinct
dev4 candidate and 95 tests. E2 real-weight qualification remains unapproved.
The original E0 proposal below is retained as review history, not current status.

Preparation status, 2026-11-03: concrete work order prepared for review; no implementation.
Provider owner: [HydrAMP #8](https://github.com/uibcdf/hydramp/issues/8).
Parent: [HydrAMP #4](https://github.com/uibcdf/hydramp/issues/4).
Consumer: [PeptideMT #32](https://github.com/uibcdf/peptidemt/issues/32).

The investigator requests preparing the encoder increment following the
[own-use full-modernization direction](hydramp_full_modernization.md).
The provider-owned proposal is `devguide/pytorch_encoder_work_order.md` in
the modern HydrAMP worktree `../hydramp/local_data/pytorch-comparison`.
Its exact bytes and primary source/metadata inventory are in the
[preparation receipt](evidence/hydramp_encoder_preparation.json).
The document is local/uncommitted; no published source commit is invented.

## Proposed scientific boundary

- Nonempty CPU int64 original tokens `[N,25]`, values `0..20`, with order,
  duplicates and every zero position preserved. No strings or molecular parser.
- Mean `[N,64]` and raw native log-variance parameter `[N,64]`, CPU float32,
  without sampling, RNG mutation, PCA, decoder/heads, descriptors or analogues.
- Native `z_sigma` is used as a log-variance parameter: the original obtains
  standard deviation through `exp(z_sigma / 2)`. Return the raw parameter,
  not a mislabeled scale or hidden random sample.
- Original unmasked embedding, two concatenating bidirectional 128-unit GRUs,
  reset-before with actual saved sigmoid/tanh settings, and two linear heads.
  Verify backward time alignment/final-state order against retained Keras source.
- Reuse existing owner cell/weight-validation primitives. No new scientific cell
  equation, native torch GRU substitution or duplicate model in PeptideMT.

Public names are illustrative until agreement; scientific input/output/failure
obligations are the proposal. It does not design a platform record or reopen
M1–M8/selector contracts. Missing/altered metadata/parameters, wrong shape/type/
device and nonfinite output fail explicitly, without fallback or silent repair.

## Readiness and stage map

Original `6590d2f4c2963f25d30669052a4c4a857e0e7279`; starter
`7804df862872ccc6d09fe01c41bafbca194cfa31`. Existing 42-entry header evidence
contains all **17 encoder parameter headers**. Original asset identities cover
17 parameters, five layer JSON and one master JSON: **23 files**.
This preparation checks the six JSON files and source text only; it does not
reopen/re-hash or deserialize any parameter array.

| Stage | Status / required outcome |
| --- | --- |
| E0: source/metadata work order | Prepared now, with zero scientific imports or model calls. |
| E1: synthetic implementation | Proposed for approval: separate candidate, artificial-weight reference checks, strict-loader failures, no RNG mutation, installed-origin/core regressions. Synthetic `atol=2e-6, rtol=2e-5` is proposed, not a new pretrained criterion. |
| E2: real encoder qualification | Future exact candidate/input/runtime/host/call plan and explicit approval before real weights. No forward budget or scientific acceptance is granted now. |

Accepted dev3/D41 remains frozen. Neither E0 nor hypothetical E1 extends its
acceptance. Preserve original/modern references and all existing FAIL evidence.
Reference construction can read/build unrelated components; E2 must count actual
work, avoid a full-generator/PCA shortcut and verify any unused stochastic graph
effects. Its scientific/numerical criteria must be justified prospectively.

Deterministic encoder comes first, analogue/redesign later. Original filter
findings in [HydrAMP #7](https://github.com/uibcdf/hydramp/issues/7) stay separate.
Training, new-family capability, GPU, new learned runs, releases, commits/pushes
and author contact are outside preparation. Preserve the shared-host 4 GB task
intent; future actual execution needs its own bounded reviewed limits.
