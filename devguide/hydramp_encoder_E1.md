# HydrAMP deterministic encoder E1

Status: **approved contract implemented; installed synthetic checks pass**,
2026-11-04. Owner: [HydrAMP #8](https://github.com/uibcdf/hydramp/issues/8).
Consumer: [PeptideMT #32](https://github.com/uibcdf/peptidemt/issues/32).
D42 authorizes the reviewed deterministic encoder contract and artificial-weight
implementation/tests after the investigator explicitly directs continuing.
The [authorization](evidence/hydramp_encoder_E1_authorization.json) records that
scope. D41/dev3 and the scientific design/selector contracts remain unchanged.

## Outcome

The new local `hydramp-torch==0.0.0.dev4` candidate implements CPU int64 tokens
`[N,25]` → CPU float32 mean/raw log-variance `[N,64]`, preserving rows, duplicates
and unmasked zero positions. It reuses the original owner reset-before GRU cell
and adds bidirectional composition, the posterior container and strict encoder
loader. There is no standard-deviation evaluation, latent sampling/RNG mutation,
training or molecular parser. No model is implemented in PeptideMT.

Wheel SHA-256:
`01fe4e125eca5decdca89f43e8925e8e969d3453b7a4da701be8e96e5e18dbe0`.
Source is in the separate owner worktree `../hydramp/local_data/pytorch-encoder`;
the owner outcome record is `devguide/pytorch_encoder_E1.md`. The source and
candidate are local/uncommitted, not a published package or adopted consumer.
The [E1 evidence receipt](evidence/hydramp_encoder_E1.json) retains identities,
installed probe, old audit failures, successful correction, test logs and JUnit.

**95 installed tests pass**: 41 new encoder, 25 existing inference/core,
24 existing artificial generation and five property-spy regressions. Published
Receptor 1.2.2 agrees with JUnit. These are the selected applicable tests, not
a relabelling/rerun of every historical 76-package/13-controller test campaign.
The new mathematical checks retain the proposed synthetic `atol=2e-6, rtol=2e-5`;
this is not a pretrained acceptance threshold.

Controls distinguish backward alignment/concat/zero-mask mistakes, raw native
log-variance versus scale, occurrence mapping, RNG changes and invalid input/
metadata/artifacts. The synthetic loader reads exactly 23 expected files and
no unrelated layers. All real scientific arrays/providers, the consumer package
and network are blocked during tests. Toy decoder/head/PCA regressions and
descriptor spies remain artificial; no real trained-model/PCA/descriptor/Macrel
call occurs.

## Preservation and resource scope

Original mathematical function/class ASTs and unchanged generator/prior/property
module bytes are verified. A shared file-validation helper preserves the old
reader body, while the old decoder loader only delegates that check. The exact
accepted dev3 source/wheel/environments are not changed. Only the candidate
version differs in the project/lock graph; build/runtime pins are retained.

The new runtime fixture borrows frozen dependency payloads and copies their exact
metadata. Earlier `.pth`/metadata-link audits failed because the native scanner
saw only the candidate despite Python resolving 41 distributions. Correcting
only the task prefix makes native dependency checking pass for all 41; the
original environments/providers remain untouched. This is not a new public
installer or clean solver qualification.

The controlled synthetic test case took 13.462 s with 327.4 MiB aggregate sampled
RSS, under the 4 GB intent/2 GiB RSS stop, CPU 0/1, one numerical thread,
nice 10 and bounded wall/address-space controls. It is not a real encoder
performance benchmark or a hard kernel RSS reservation.

## What remains

E2 has no approval or run budget. Before real parameters, prepare the exact new
candidate/assets/ordered fixture/reference construction, prospective encoder
criteria and finite shared-host call/resource plan. Keep unused stochastic graph
effects and unrelated legacy loads visible. No analogue, training, filter fix,
new family, GPU, release or author contact follows from E1. E1 completes only
the artificial installed boundary; #8/#32 remain open for later disposition.
