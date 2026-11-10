# peptidemt contributor instructions

## Mandatory MolSysSuite instructions

Read and follow `MOLSYSSUITE_GUIDE.md` before working in this repository.

Within their stated scope, its common rules take precedence over this file
and any nested `AGENTS.md`. Local instructions may refine them; deviations
require the documented policy exception process.

The synchronized guide is owned by `uibcdf/molsyssuite`. It includes the
[reusable-tool ownership rules](MOLSYSSUITE_GUIDE.md#modular-reusable-tools)
and [working-instruction rules](MOLSYSSUITE_GUIDE.md#durable-working-instructions).
For work under `devguide/`, also read `devguide/AGENTS.md` and its local
reporting protocol. Keep repository-specific instructions below.

## Local working context

Read `devguide/governance.md` for PeptideMT's local scientific scope and W0
receiving. Select the applicable local commands and test scope:

```bash
ruff check .
ruff format --check .
python -m pytest --receptor=llm
python devtools/devguide_index.py --check
```

Before curating PeptideMT Discussions, read `devguide/tools_catalog.md` for
the approved category routing, family/role labels and resource-record lifecycle.

Generated member Conda environments remain CI/bootstrap/clean qualification
fixtures. Routine work uses the authorized named shared profile; the original
W0 engineering baseline does not qualify Macrel or M1–M8.

## Standing execution authority and shared-host resources

The investigator delegates routine tests, measurements, debugging and reasonable
diagnostic retries within the already approved work. Proceed without requesting
permission for each invocation or retry. This standing authorization supersedes
historical per-run resource-confirmation pauses; consuming an earlier call or
process allowance does not by itself require another human confirmation.
Keep earlier receipts and spent allowances unchanged. Record a fresh bounded
run and its authority rather than relabeling old budgets as unused or claiming
that the investigator reviewed a run-specific plan they did not review.

This machine is shared. Inspect available RAM, load and disk before substantial
runs; reserve headroom, run heavy workers sequentially and limit CPU/thread use.
For the current HydrAMP work, retain the conservative envelope: logical CPUs
0/1, one numerical thread, 4 GB task-RAM intent, a sampled 2 GiB aggregate
controller/worker RSS stop, and at least 8 GiB RAM available before each worker.
The 8 GiB address-space ceiling is a virtual-memory limit, not permission to use
8 GiB of physical RAM. Keep bounded wall/CPU/output limits; reduce or defer work
if the shared host is under pressure. Do not saturate all CPUs or exhaust RAM.
GPU use remains unauthorized until explicitly approved.

For D50 synthetic data and packaging checks only, the investigator approves a
serial lightweight profile: one job at a time on CPUs 0/1, one numerical thread,
a sampled 512 MiB aggregate supervisor/worker RSS stop and at least 4 GiB RAM
available before and throughout each job. Keep bounded wall/CPU/output and
8 GiB virtual-address-space limits. This scoped profile supersedes the 8 GiB
host reserve above for these checks; it authorizes no GPU, weights, PCA loading
or neural evaluations. Other work retains its existing resource envelope.

Choose and record suitable per-run resource/call limits autonomously, preserve
input/source/environment identities and failures, and stop on a breached limit.
Retry only for a diagnosed reason; preserve successful evidence and avoid
repeating accepted checks without a new question, source change or unresolved
failure. Use the MolSysSuite components and existing supervision/diagnostics.

Ask when the scientific scope, chemistry, preprocessing, acceptance criteria or
other agreed contracts materially change, or a substantially larger resource
allocation is needed. This delegation does not authorize new scientific models,
families, targets, training, feedback, package publication or third-party contact.
Record the applicable scientific and resource authority before model work;
routine execution consent within that scope is already delegated under D49.

## PeptideMT scientific working agreement

Read `README.md`, `devguide/README.md`, `devguide/decisions.md` and the
canonical [MolSysSuite component guide](https://github.com/uibcdf/molsyssuite/blob/main/MOLSYSSUITE_GUIDE.md)
before making changes. D36 authorizes the W0–W4 increment-1 work order. Central
registration is accepted at `8a94e16f`; official W0 engineering receiving is
recorded in `devguide/archive/complete_w0.md`. Before continuing W1–W4, read that
receipt and the component-owned work order; engineering checks do not establish
scientific execution. Preserve the existing scientific design history.

Use English for maintained documentation and commits. Keep changes focused,
preserve human work and do not publish secrets, private attachments or raw
conversation transcripts.

The user has authorized maintaining `devguide/` as the design source of truth
when important scientific or architectural matters are discussed. Update related
documents consistently and preserve the reasoning and sources behind changes.
Do not convert an assistant recommendation, hypothetical API or research
hypothesis into an accepted decision without explicit investigator approval.
A provisional definition remains provisional.
Follow the investigator-approved responsibilities and implementation-readiness
agreement in `devguide/design_methodology.md`; major design changes return to discussion.

Follow D35, M1–M8 and the authorized W0–W4 work order. W1 begins only after W0
completes through accepted published central registration and the official
staged starter. Report actionable bugs, limitations and improvements in the
owning component, or update an existing issue, under the canonical feedback
policy. Cross-link consumer evidence and any workaround/removal condition. The
earlier W0-only issue restriction no longer limits this reporting duty. Reporting
a need does not authorize its implementation, a scientific scope change or
publication. Preserve confidentiality and existing declined/deferred disclosures.
Publishing issues or comments in repositories outside the investigators' own
projects requires their explicit permission for that external publication.
The owning-issue reporting duty alone does not grant this permission. Keep
findings in authorized local/PeptideMT records while awaiting it; if repository
ownership or prior external-publication authority is unclear, ask first.
Do not treat a proposed registration branch as accepted admission or fabricate
an admission SHA. D38 now commissions the single HydrAMP increment-2
qualification recorded under PeptideMT #8: read its maintained work record
before continuing. D39 additionally authorizes the local native PyTorch inference
port in the investigator-owned HydrAMP fork; read `devguide/hydramp_pytorch_review.md`.
Preserve the legacy reference and distinguish synthetic port tests from pretrained
qualification. D41 accepts the exact modern HydrAMP bundle for experimental AMP
generation; read `devguide/hydramp_dev3_acceptance.md` for its scope and the
separate future-work ownership in PeptideMT #32. D42 approves deterministic
encoder E1 with artificial weights only; read `devguide/hydramp_encoder_E1.md`
before continuing HydrAMP #8. Preserve accepted dev3; read
`devguide/hydramp_encoder_E2.md` for the later separately approved real encoder
comparison and its exhausted allowance. D43 authorizes the first analogue A1
contract and artificial-weight implementation/tests; read
`devguide/hydramp_analogue_work_order.md` and its authorization/pause evidence.
The investigator's implementation instruction after the audit resumes that
unchanged A1 scope and the continuation plan's first cycle. Preserve dev3/dev4;
real analogue A2 and a new consumer redesign API remain separate reviewed work.
The subsequent exact A2 execution authorization is recorded in
`devguide/evidence/hydramp_analogue_A2_authorization.json`; read
`devguide/hydramp_analogue_A2.md` for the executed outcome and exhausted allowance.
D44 subsequently accepts the exact dev5 native-score analogue route for
experimental AMP proposals; read `devguide/hydramp_dev5_acceptance.md` for its
limits. The consumer contract in `devguide/hydramp_redesign_work_order.md`
is approved for R1/R2 under D45, recorded in
`devguide/evidence/hydramp_redesign_authorization.json`. Implement data receiving,
the owner codec and isolated artificial execution within that unchanged contract.
R3 real consumer qualification requires its own review and fresh limits. Resource
acceptance does not supply missing provider APIs or fresh execution authority.
R1/R2 now have local source/installed artificial evidence; read
`devguide/hydramp_redesign_implementation.md` before further consumer work.
The separately authorized R3 case now passes finite technical receiving; read
`devguide/hydramp_redesign_R3_qualification.md` and its execution receipt.
Its 27-evaluation allowance is exhausted. Its sole child scores worse than its
parent under Macrel; do not infer useful optimization or new dev6 scientific
acceptance, repeat models, or transfer its budget to another experiment.
D46 approves the finite historical experimental-entity/unchanged-sequence view
and E. coli ATCC 25922 review scope. Read
`devguide/hydramp_historical_work_order.md` before continuing that comparison.
D46 initially commissioned model-free work-order/fixture design. The subsequent
investigator continuation commissions its data-only receiver/replay cycle; read
`devguide/hydramp_historical_data.md` for delivered behavior and exact authority.
General chemistry admission and all native input/model execution remain separate.
D47 approves the finite reported-MIC endpoint and paired descriptive ROC-AUC
policy, with data-only implementation and artificial score controls. Read
`devguide/hydramp_historical_evaluation.md` before continuing that work. Its
synthetic-score comparator does not receive learned-model evidence or authorize
native inputs, models, equivalence claims or changes to the accepted bundles.
D48 subsequently approves separate historical learned-score receiving,
scalar/method-double tests and two bounded owner-codec children, with zero
weights or network evaluations. Read
`devguide/hydramp_historical_real_implementation.md` for the actual checkpoint:
the initial modern codec passes and the original initially fails during startup.
Both D48 codec allowances are spent; preserve those facts and the successful
artifact. The D49 continuation qualifies original encoding and paired native
inputs, reusing the modern artifact. The fixed historical learned comparison
has now executed; read `devguide/hydramp_historical_real_comparison.md` before
further work. Preserve its complete raw outputs, finite interpretation and
consumed twelve-evaluation declaration; no general equivalence or new bundle
acceptance follows.
D49's standing execution authority above now governs
reasonable continuation/retries and resource-bounded execution in the approved
historical comparison. Qualify paired native inputs and freeze exact code,
bundle/use conditions and host/call limits before scoring; partial input
qualification does not establish model readiness or scientific equivalence.
Further real analogue work, increment 3/feedback,
target-conditioned generation, other scientific models, publication and a new
architecture remain outside this commission.
Material changes to chemistry, preprocessing, attribution, selectors or scientific
acceptance return to the investigators. Routine internal technical choices are
delegated to Codex within these contracts.

D50 commissions the approved first independent HydrAMP generation-result
contract in `devguide/hydramp_result_contract.md`: owner profile, faithful
save/read and optional saved-result Recorda/Ackredit integration, qualified with
synthetic data only. Preserve accepted resources and the dev7 source baseline
in a separate worktree/candidate. No neural evaluation, learned parameter/PCA
loading, live attribution, other portable operation, release or commit/push is
authorized by this data-only commission. D49 governs reasonable bounded checks.

D51 commissions the approved single MDM2–p53 T0 structural-reference case.
Read `devguide/mdm2_t0_work_order.md` and `devguide/mdm2_t0_qualification.md` before
continuing. Exact source/profile admission precedes real geometry; artificial
interpretation checks are separate evidence. T1 prediction remains uncommissioned.
The later investigator-directed T0 resource correction sets a 4 GiB available
host-RAM reserve and a 2 GiB aggregate task RSS stop while retaining the other
limits; read `devguide/evidence/mdm2_t0_resource_correction.json`. This does not
change the HydrAMP/D50 resource profiles.

D52 commissions the longer-horizon target-directed demonstrator preparation.
Read `devguide/target_directed_demonstrator.md` before continuing. Evidence/provider
review and a concrete scientific proposal precede any new T1 model, chemistry,
evaluator or generation implementation; preserve component ownership.

D53 approves and commissions the data-only MDM2 T1a reported-affinity contract.
Read `devguide/mdm2_t1a_work_order.md`, `devguide/mdm2_t1a_qualification.md` and
the approval/execution receipts before continuing. Its finite receiving and
saved replay are now qualified; do not repeat accepted checks without a new question.
The earlier T1a review holds are historical. Preserve the original proposal and
source identities; use owner quantity/measurement tools and keep all missing
chemistry/unquantified outcomes. The scoped serial envelope is 512 MiB aggregate
task RSS and a 4 GiB available-host-RAM reserve, with the order's other bounds.
This authorizes no molecular preparation, predictive method, generation or public
API/release. Routine technical checks remain delegated under D49.

Preserve demonstrated modern numerical improvements. Explain legacy/modern
differences with independent reference and functional evidence; do not modify the
port solely to reproduce legacy approximations. This does not waive faithful
same-provider result receiving, scientific acceptance or execution limits.

Follow the common domain-owner map when selecting providers. PeptideMT owns
its peptide-specific scientific question, design/selection policy, orchestration
and interpretation. Preserve the separate responsibilities of Praxis, Recorda,
Sabueso, Nextia and MolSys-AI and identify cross-component scientific source
links by repository and preferably immutable commit.

For documentation changes, check relative links, navigation, status consistency,
citations and whitespace. Do not claim scientific tests or CI qualification from
a documentation check. The official reporting checker and baseline package tests
are present; they do not qualify Macrel or execute the scientific M1–M8 gates.

Before scientific implementation, complete official W0 receiving. The integrated
starter supplies policy workflows, package metadata, development environments and
guide synchronization; retain its real gates and applicable release controls. Do not fabricate policy pins, admission commits, badges or support
claims. This initial repository publication is not a versioned software release.

For work in `devguide/`, also read `devguide/AGENTS.md`.

Use the published GH Run Receptor for the first inspection of Actions, then
verify required native job/step conclusions. Record both surfaces in the W0
evidence issue. Never infer scientific execution from the baseline CI.

## Registered integration guides

Read the registered consumer guides when working on their respective boundaries:

- `GH_RUN_RECEPTOR_GUIDE.md`
- `PYTEST_RECEPTOR_GUIDE.md`

- `SMONITOR_GUIDE.md`
- `DEPDIGEST_GUIDE.md`
- `ACKREDIT_GUIDE.md` for portable scientific attribution; central consumer
  registration is tracked in `uibcdf/molsyssuite#152`.
