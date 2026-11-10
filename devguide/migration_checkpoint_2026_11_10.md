# Development migration checkpoint — 2026-11-10

**Subsequent transfer instruction:** read [migration transfer](migration_transfer.md).
The investigator now requests a clean/synchronized PeptideMT repository and a
private ZIP of non-GitHub material, without copying raw `.git`. That instruction
authorizes the reviewed PeptideMT source commit/push and supersedes this earlier
checkpoint's no-new-Git operational state, not its scientific limits. Historical
source coordinates and TAR facts below remain dated evidence. HydrAMP local
branches/commits are privately preserved rather than newly published.

Status: **investigator-directed handoff preparation; destination receiving pending**.
Owners: [PeptideMT #33](https://github.com/uibcdf/peptidemt/issues/33) for the
current scientific capability work, [#32](https://github.com/uibcdf/peptidemt/issues/32)
for HydrAMP consumer/scientific follow-up, and
[HydrAMP #4](https://github.com/uibcdf/hydramp/issues/4) for its independent product.
This is the current resumption entry, not a new scientific decision or release.

## Read this first

The investigator corrects the intended development host: **we are moving to
another machine now**. CPU/RAM/storage/PCI/driver measurements in
[the feasibility report](mdm2_node_feasibility.md) belong exclusively to the old
source machine. They cannot qualify the destination, establish its GPU state or
justify a destination resource allocation. The reported plan for five nodes,
two RTX 5070 Ti, three RTX 5070 and older 2080-series/1080 cards is planning
context; actual placement, card variants and destination specifications remain
unverified. Do not repair the source machine's driver as a supposed migration
prerequisite. The completed MolSysMT inspection retains its original host scope.

**A fresh clone of GitHub is insufficient.** PeptideMT contains extensive local
uncommitted/untracked implementation and evidence; HydrAMP has multiple dirty
experimental worktrees and local-only dev7/dev8 commits. Do not discard that
work by pulling/resetting main or reinstalling over the old compositions.
Preserve local files, history, worktree relationships and private evidence first.

Read in order: root [AGENTS.md](../AGENTS.md) and
[MOLSYSSUITE_GUIDE.md](../MOLSYSSUITE_GUIDE.md), local
[instructions](AGENTS.md)/[reporting protocol](reporting_protocol.md), this
checkpoint, [decisions](decisions.md), [scientific audit](peptidemt_scientific_audit_2026_11_04.md),
[continuation plan](continuation_plan_2026_11_04.md), then the topical records
for the work being resumed. Read current owning-issue replies before acting.
The dated design/proposal documents retain history; later approval and outcome
records determine current status. Do not read an old pause as a new blocker.

## What we are trying to build

PeptideMT's provisional purpose is reproducible peptide generation/redesign,
evaluation and purpose-specific selection, including target-directed and
target-free functional questions. Functional families are independent of
particular models; generators/evaluators are optional, nonexclusive resources.
Target recognition, function, chemistry, predicted scores and experimental
activity are different scientific claims. The architecture keeps scientific
intent, computational plan and actual evidence distinct.

The central remaining product question is **useful peptide design**, beyond
faithful wrappers or provenance infrastructure. The current longer-horizon
commission, D52, seeks one independently evaluated target-directed design/
selection demonstrator. MDM2–p53 is a conditional first case. It has not yet
produced a qualified predictive/docking or generative route. Preserve the
accepted general design and D35/M1–M8; no architecture reopening is requested.

## Completed work and its practical limits

| Work | Current result / acceptance | Authoritative continuation record |
| --- | --- | --- |
| W0 and central admission | Complete; official starter and engineering receiving. Central admission `8a94e16f1ba26122304df264e89c4eca15afaf5a` | [W0 receipt](archive/complete_w0.md), closed PeptideMT #1 / MolSysSuite #146 |
| W1 | Ordered in-memory/FASTA inputs, attributed saved results and two reproducible selectors. General FASTA interpretation delegates to MolSysMT | [W1](w1_core.md), closed #4/#5; no local molecular parser |
| W2–W4 / Macrel | D37 accepts the exact Macrel 1.6.1 CPU bundle for exploratory AMP/hemolysis assessment/ranking | [Acceptance](increment_1_review.md), [W3 evidence](w3_assessment.md), closed #6; scores do not establish activity or safety |
| HydrAMP de novo | D41 accepts exact modern PyTorch dev3 experimental AMP route | [dev3 acceptance](hydramp_dev3_acceptance.md), closed PeptideMT #8; original probability/rank diagnostic FAILs remain visible |
| HydrAMP analogue/provider | D44 accepts exact dev5 native-score analogue route | [dev5 acceptance](hydramp_dev5_acceptance.md), [A2](hydramp_analogue_A2.md); numerical agreement is finite, not general equivalence |
| PeptideMT analogue consumer | R1/R2 artificial implementation and separately authorized real R3 receiving/replay pass | [Implementation](hydramp_redesign_implementation.md), [R3](hydramp_redesign_R3_qualification.md); the sole child scores worse than its parent under Macrel, so useful optimization is unqualified |
| Historical MIC comparison | Fixed D46–D49 panel complete: 42 observations /39 literal groups; primary 38 groups, both routes ROC-AUC 0.653846, same ordering | [Comparison](hydramp_historical_real_comparison.md); selected/exposed panel, moderate discrimination, not an independent benchmark or proof of generation quality |
| Independent HydrAMP product | dev7 package baseline and dev8 generation-result contract locally committed; synthetic installed/source/SDK receiving complete | [Baseline](hydramp_product_baseline.md), [dev8](hydramp_generation_result_implementation.md); no public release or new learned-model acceptance |
| HydrAMP dev9 | Constructor/replace invariant correction qualified in an isolated dirty branch; 73 source, 73 installed and five SDK controls retained | [Invariants](hydramp_result_invariants.md), [source review](hydramp_dev9_source_review.md); local commit proposed, not authorized/executed |
| D51 MDM2 T0 | Single 1YCR rev1.5 identity/geometry reference and unchanged/rigid/displaced controls complete | [T0 qualification](mdm2_t0_qualification.md); structural reference, not target prediction/binding validation |
| D53 MDM2 T1a | Data-only Li 2010 receiving/replay complete: 72 source occurrences, 70 reported evidence records, 66 quantified/four unquantified | [T1a qualification](mdm2_t1a_qualification.md); chemistry, construct correspondence and independence remain unqualified |
| Docking/binder alternatives | Classical docking, fixed-pair cofolding and generators reviewed; actual 2025 BindCraft supplement/text received | [Survey](peptide_protein_binding_survey_2026_11_10.md), [source audit](bindcraft_mdm2_source_review_2026_11_10.md); predicted structures are not experimental poses, specimen/ID/assay gaps remain |
| Current 1YCR preparation | One read-only MolSysMT coverage question completed: 98 groups/818 atoms, no examined template heavy-name gaps, about 201 MiB RSS | [Input profile](mdm2_input_profile_preparation.md), [source-host feasibility](mdm2_node_feasibility.md); zero explicit H and unassessed terminal/protonation/docking readiness remain |

Earlier HydrAMP modern-vs-original investigations support specific numerical
improvements while retaining genuine original pointwise advantages and failed
diagnostics. Do not change the modern port solely to copy legacy approximations,
claim it is uniformly better, or erase earlier failures. See
[numerical evidence](hydramp_amp_numerics.md) and the finite comparison above.

The original E2/A2/R3/historical execution declarations remain consumed. D49
delegates reasonable routine diagnostics/retries within approved questions;
migration does not refill declarations or authorize a new scientific experiment.
No successful scientific campaign should be repeated merely to restart work.

## What is proposed, and what should happen next

The immediate scientific preparation is the
[fixed-peptide 1YCR pose-pilot proposal](mdm2_comparative_pilot_proposal.md):
compare candidate **HADDOCK3 classical docking** and **Boltz-2 complex prediction**
for a fixed identity/view, before considering sequence generation. This is a
recommendation for review, not adopted engines or permission to run models.
The earlier [T1b/3EQS proposal](mdm2_t1b_proposal.md) is an optional source-
admission branch, not a mandatory dependency of this pilot.

The pilot is **known-site, holo-receptor-assisted**. A receptor-only template/
site may be admitted; reference peptide coordinates stay evaluation-only.
The proposal separates native-ranked top-1 from oracle best-within-five, requires
receptor-aligned peptide-backbone RMSD in explicit nm and preserves all failures.
Its **0.2 nm in at least two of three seeds** criterion and three-seed/five-output
outer caps are **proposed, not approved**. Actual internal sampling/call budgets,
maps/atom coverage, permitted information, initial ensembles and chemical recipe
remain unresolved. Equal final output counts are not matched search budgets.
Boltz's small-molecule affinity head is not a qualified peptide-Kd observable.

Resume in this order:

1. **Destination receiving:** locate the transferred workspace, verify source/
   archive identities and worktrees, inspect actual CPU/RAM/disk/GPU/driver state,
   and establish the actual named development profile/import origins. No models
   are needed to establish the continuation context. Do not upgrade sibling
   sources silently or treat the old machine's results as destination benchmarks.
2. **Molecular recipe through MolSysMT:** resolve observed fragment/construct,
   termini, explicit residue protonation/stereo, H/terminal additions and maps.
   Existing `get_peptide_chemical_template`, template assessment/application and
   H tools are reusable pieces, not missing APIs. Free terminal models can need
   OXT; the no-heavy-name-gap result does not establish terminal completeness.
   Review any required chemical/geometry change before execution.
3. **Provider disposition through DockingMT:** receive a supported peptide
   profile or an explicit unsupported outcome, including a CPU HADDOCK3 route
   and the cofolding boundary. The current Vina/small-ligand qualification does
   not transfer. No PeptideMT-local parser, builder, docking adapter or scorer.
   CNS/use terms, exact binaries, configuration, original score semantics,
   mappings and refusals need their actual receiving.
4. **Concrete scientific review:** present the resolved chemistry/information,
   observables, baselines/controls, criterion, complete sampling and destination
   resource prescription. Ordinary technical checks within approved scope are
   delegated; missing scientific definitions are not supplied by that delegation.
5. **Only then qualify/execute the admitted route.** CPU preparation/classical
   qualification need not conceptually wait for new GPUs; actual fit/runtime is
   still unmeasured. A later small Boltz-2 qualification may prioritize one
   5070 Ti after GPU authority and compatibility receiving. Per-card 12/16 GB
   does not become one 68 GB device across the planned fleet. Other generators,
   broader assays/families, training and feedback remain separate proposals.

Parallel in priority, not concurrent heavy execution: HydrAMP independent-product
modernization remains valuable under #4/#32. Its exact dev9 commit proposal is
pending; preserve its twelve changed paths and clean dev8. Broader prospective
scientific comparison, other-family research and possible author collaboration
remain separate owner issues. The investigator wants modernization before any
author contact; do not contact upstream or open external issues without permission.

## Current issues, ownership and deferred ideas

Issue states were read from GitHub on 2026-11-10; check for later replies.

| Owner / issue | Meaning at this checkpoint |
| --- | --- |
| [PeptideMT #33](https://github.com/uibcdf/peptidemt/issues/33) | Open/partial: scientific audit, D52 demonstrator preparation and this migration handoff; the overall useful-design objective is incomplete |
| [PeptideMT #32](https://github.com/uibcdf/peptidemt/issues/32) | Open/partial: accepted HydrAMP consumer, finite evidence and future scientific/product directions |
| [PeptideMT #34](https://github.com/uibcdf/peptidemt/issues/34) and [#38](https://github.com/uibcdf/peptidemt/issues/38) | Local numeric-overflow and thread-created-child RSS fixes/guards delivered; remain partial pending source delivery. Preserve current fixes and earlier failed evidence; not unresolved runtime blockers to redo |
| [DockingMT #33](https://github.com/uibcdf/dockingmt/issues/33#issuecomment-6772377034) | Existing reusable peptide-profile/cofolding boundary request; owner acceptance or delivery is not implied |
| [MolSysMT #558](https://github.com/uibcdf/molsysmt/issues/558#issuecomment-6772379174) | Conditional terminal-completion maps/history need; no completion was executed in the current 1YCR inspection |
| [MolSysMT #685](https://github.com/uibcdf/molsysmt/issues/685) | Capped/stereochemically declared peptide references accepted as design/backlog, not an implementation promise; [#447](https://github.com/uibcdf/molsysmt/issues/447) retains identity/leakage annotations |
| [HydrAMP #4](https://github.com/uibcdf/hydramp/issues/4), [#3](https://github.com/uibcdf/hydramp/issues/3), [#1](https://github.com/uibcdf/hydramp/issues/1) | Independent product; prospective comparison; numerical diagnosis. All open; finite completed results do not close broader questions |
| [HydrAMP #2](https://github.com/uibcdf/hydramp/issues/2), [#8](https://github.com/uibcdf/hydramp/issues/8), [#7](https://github.com/uibcdf/hydramp/issues/7) | Provider provenance/descriptor profile; encoder continuation; legacy filter-dispatch audit. Read exact delivered scopes before choosing another module |
| [HydrAMP #5](https://github.com/uibcdf/hydramp/issues/5), [#6](https://github.com/uibcdf/hydramp/issues/6) | Family-extensible-method research and possible future author handoff; no training/family expansion/contact commission |
| [PeptideMT #7](https://github.com/uibcdf/peptidemt/issues/7), [#28](https://github.com/uibcdf/peptidemt/issues/28), [#29](https://github.com/uibcdf/peptidemt/issues/29), [#30](https://github.com/uibcdf/peptidemt/issues/30) | Open engineering/resource/dependency/distribution/coverage follow-up; not new scientific acceptance or a package-release instruction |
| [PeptideMT #35](https://github.com/uibcdf/peptidemt/issues/35), [#36](https://github.com/uibcdf/peptidemt/issues/36), [#37](https://github.com/uibcdf/peptidemt/issues/37) | Deferred RFD4/provider/data and later target/CPP campaign proposals, not permission to start those scientific branches |

Reusable molecular-system operations belong to MolSysMT, docking workflows to
DockingMT, topography to TopoMT and molecular topology to MolSysMT. PeptideMT
owns peptide questions, design/selection policy, orchestration and interpretation.
Use Recorda/Ackredit and other suite owners at their real boundaries. Report
actionable improvements in the investigators' owning repositories, reusing issues;
do not implement missing reusable capabilities locally or contact third parties.

The resource discovery area is already organized, not a new migration task:
`Scientific Resources` contains `Models and Tools`, `Datasets and Benchmarks`,
and `Literature and Resources`; families/roles are controlled labels. One
discussion per resource, with indexes for navigation. Read
[catalogue governance](tools_catalog.md) before curation. OmegAMP/challenge
discovery and future CPP collection are preserved there; catalogue membership
does not commission a model. Optional pinning is not a scientific blocker.

## Exact source coordinates and worktree custody

These are observed local heads, not assumed public release coordinates:

| Repository / worktree | HEAD / state |
| --- | --- |
| PeptideMT main | `1f8c444e4619499cae8ad9970122c5f40adf6127`; many tracked edits/untracked files. Copy the complete working tree, not only this commit |
| HydrAMP primary `peptidemt-inference` | `6590d2f4c2963f25d30669052a4c4a857e0e7279`; dirty modern-port support |
| HydrAMP `peptidemt-product-baseline` | `a77baff9de97e8ab4ae101b9b0c79122dea22ce3`; clean locally committed dev7 |
| HydrAMP `peptidemt-generation-results` | `6a3ff905635a4bd744854cd540f8513916aa99f0`; clean locally committed dev8 |
| HydrAMP `peptidemt-result-invariants` | Same dev8 parent; twelve dirty/untracked dev9 paths, proposed tree `b8a334085bac8bf6c0d31c2cc9586ad1f311eb40`; not a dev9 commit |
| Primary MolSysMT | `71fbe4f46d3c70e4e973c8025f01752a8c9b1084`; clean, behind fetched main; not the T0-qualified composition |
| T0-qualified MolSysMT worktree | `ed09f64539a5af6c1dbe9bd352c7ef65dcd4a7a6`; under the retained T0 task, with its exact native extension/profile |
| Primary DockingMT | `2fda6238e6b1cb3742f5d30b8ed3af699f9ed748`; clean. Previously inspected fetched source `4e30da511afa4181bbdbb63a3f53c31a19b4e5fa` is a different coordinate |
| MolSysSuite / PyUnitWizard | `b9852d973e96613a68cab7278491ff647bfd0b7d` / `9d74f0e1e911d78c1906948e74ce8da93935557d` |
| Ackredit / Recorda | `74f865d7eca1f5386235885d4ea001e53b5b822d` / `ff52fa5d8628d796f413b833c8abe73907990cf9` |

HydrAMP also has separate `pytorch-port`, `pytorch-comparison`, `pytorch-generation`,
`pytorch-gru-layout`, `pytorch-encoder`, `pytorch-analogue` and `pytorch-redesign`
worktrees below its `local_data`. Do not collapse them into one latest branch.
The full eleven-worktree inventory and source snapshots are retained with this
checkpoint. Clone/bundle history alone does not preserve dirty worktree bytes;
copy their overlays as well. Copied `.git` worktree pointers can contain absolute
old paths; repair/reconstruct them in the destination using Git's worktree tools,
never by deleting the old common repository or treating a new directory as a
new unqualified provider revision.

## Evidence and private material to carry

The [machine-readable checkpoint receipt](evidence/migration_checkpoint_2026_11_10.json)
identifies the source inventories, issue snapshots, correction and verification.
The task directory is
`local_data/peptidemt-migration-checkpoint-9wc2d747` (also recorded by
`local_data/peptidemt-migration-checkpoint-current-path.txt`). It contains local
source/history recovery files and a non-Git reference inventory. Those are
**private transfer artifacts**, not a public package or dataset.

Carry the complete private workspace where possible, including `.git`, ignored
`local_data`, retained source snapshots, native logs/failures, raw records,
source PDFs and build/dependency manifests. Preserve any owner worktrees used
from sibling repositories. The finite recovery archive provides code and
explicitly inventoried evidence files; it is **not** the complete closure of all
environments, directory-valued inputs, implicit model assets or external caches.
Keep the old workspace until destination receiving succeeds. Do not publish
article attachments, raw sequences/assays, weights, internal snapshots or host
paths to solve the handoff.

| Particularly important retained location | Why it matters |
| --- | --- |
| `local_data/peptidemt-mdm2-t0-d1u79kql` | Original 1YCR, saved geometry/maps, executed source, qualified provider source/native/profile and failures |
| `local_data/peptidemt-mdm2-t1a-b03dl94b` | Source-scoped reported-affinity artifact and fresh saved replay; reference SHA-256 `b9af350ef8a39febcb807c18c7d56d8a11391c2c6284ab689ac9d3293007cea6` |
| `local_data/peptidemt-bindcraft-mdm2-review-kte1roqw` | Exact ACS supplement/NLM text, extraction and inspected-page evidence; preserves specimen/source discrepancies |
| `local_data/peptidemt-mdm2-node-feasibility-l7zcuxad` | Original source-host hardware evidence and read-only MolSysMT inspection, including failed serialization and diagnosed retry |
| `local_data/hydramp-historical-scoring-m6v0gs0e` | Paired learned comparison, declarations and raw outputs; saved comparison SHA-256 `3c3f6f97e41b0e0b697dcf5cd287f0a9e2ea2733763c671504b08e9ecddb458c` |
| `local_data/hydramp-result-invariants-qjs8u3_7` | dev9 qualification/artifacts and exact twelve-path source identity; receipt remains SHA-256 `15c5814cfec53531e51f5424d46ea54f028e0e345fd9b30f2bd0537cf77c81d3` |
| HydrAMP worktrees and all earlier task locations in maintained receipts | Accepted dev3/dev5 resources, legacy reference, modern candidates, public dependency archives, PCA/asset manifests and numerical diagnosis history |

The initial non-Git scan finds 1,746 identity-path references: 1,745 exist and
one old `/tmp/peptidemt-current-discussions.json` cache is absent. That missing
cache belongs to the 2026-11-03 resource-intake evidence; its recorded hash is
retained and no identical reconstruction is claimed. Current catalogue/issue
records support continuation without pretending this historical cache survived.
This metadata scan is not a complete recursive asset audit or a new scientific
qualification. The archive manifest records the bytes actually copied.

Old receipts contain absolute paths and producer versions. Keep them unchanged.
Create a destination relocation record from old roots to new roots; do not edit
old receipts to make historical paths look newly executed. Hash matching establishes
file identity, not new-host compatibility. Local permission/use limits for the
accepted research assets persist; unresolved original-Drive identity, checkpoint
exposure and redistribution/output-use questions remain unresolved.

## Destination startup and stopping conditions

1. Verify the transferred recovery archive against its sidecar SHA-256 and its
   per-file manifest **before restoration**. Restore only into a fresh staging
   directory; never overwrite concurrent destination work. Restore Git histories
   and each worktree at its recorded base, then its source overlay and recorded
   deletions. A plain extraction into a clone does not apply deletions.
2. Transfer remaining private workspace assets and record unavailable paths.
   Verify the critical T0/T1a/dev9/reference identities before consuming them;
   do not claim the finite archive replaces every Conda prefix/model bundle.
3. Read the checkpoint/owning issues and inventory the actual destination.
   Map authorized CPU0/1 only if available within destination affinity. Use one
   serial heavy worker and one numerical thread; no GPU compute follows merely
   from finding a card. Inspect RAM, load and disk before substantial work.
4. Establish the canonical `molsyssuite@uibcdf_3.14` development profile, current
   source/import identities and recorded source requirements. Existing copied
   Conda prefixes/native libraries are historical artifacts, not relocation-safe
   installed qualification. Rebuild/receive required native code through its
   owner when needed; do not use an arbitrary public wheel in place of a selected
   development API. Preserve the frozen T0 profile for evidence rather than
   silently replacing it with current main.
5. Diagnose environment failures before changing providers. The source shared
   environment has known Amber-extra `pip check` findings under
   [MolSysSuite #82](https://github.com/uibcdf/molsyssuite/issues/82); the successful
   isolated scientific profiles do not make that global check green. The
   destination's current outcome must be measured independently.
6. Run the documentation index/link checks and only the appropriate focused
   source/data checks for the new destination question, with published Pytest
   Receptor when applicable. Retained model-free replay is preferable to
   repeating learned runs just to show that work resumed. No full scientific
   suite or Actions inspection is required merely to read the handoff.
7. Continue the input/provider preparation above and report a concrete outcome
   to existing #33/#32/owner issues. If a mandatory asset/provider/scientific
   definition is absent, state its exact owner and next resolution; do not
   substitute local molecular code, mark it passed or invent a new contract.

Resource scopes remain distinct: HydrAMP historical model work uses its standing
2 GiB RSS stop/8 GiB host reserve; D50 data/package checks use 512 MiB/4 GiB;
D51/current 1YCR preparation uses 2 GiB/4 GiB; D53 T1a data checks use 512 MiB/
4 GiB. Virtual-address limits are not RAM allowances. D49 avoids per-invocation
permission prompts for routine approved work, but does not select new chemistry,
models, scientific acceptance, training/feedback, GPU use or substantially larger
allocations. Source preservation here does not authorize commit/push/release.

The destination is **not yet received**, no transfer destination was supplied
and no remote copy occurred. Completion of this checkpoint means a reader can
recover the decision context and local source/evidence custody; actual host/
environment/assets receiving must be recorded on arrival. Leave the source
workspace intact until then.
