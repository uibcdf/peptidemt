# MDM2 T0 work order: source identity and structural reference

Status: **investigator-approved T0 implementation and finite execution scope**,
2026-11-05 (D51). The [authorization](evidence/mdm2_t0_authorization.json)
binds the reviewed proposal bytes; implementation/profile/geometry outcomes
remain separate evidence. The [qualified outcome](mdm2_t0_qualification.md)
now completes this exact T0 scope on 2026-11-06.
Owner: [PeptideMT #33](https://github.com/uibcdf/peptidemt/issues/33).
Parent: [MDM2 reference feasibility proposal](target_case_mdm2_reference_proposal.md).
The investigator approves this concrete next step after the implementation explanation. Existing D35–D50,
M1–M8, source/model acceptance and spent execution/Git permissions remain intact.
This order does not commission T1 prediction, generation or a new public API.

## 1. Scientific meaning and approved scope

Qualify faithful handling of one published human MDM2–p53 coordinate reference,
then demonstrate receptor-frame structural measurements on that reference and
two artificial geometry controls. A passing T0 establishes source/identity and
geometry bookkeeping for the specified observed atoms. It does not establish
predictive recognition, binding affinity, inhibition, cellular access, anticancer
effectiveness, selectivity or successful target-aware peptide design.

The approved authorization covers a case-specific local coordinator/
example, bounded source/asset receiving, finite geometry qualification and saved
inspection. Keep molecular-system implementation in MolSysMT. Do not create a
generic campaign framework, result schema, molecular parser, public target API,
new selector or modification of existing PeptideMT receipts. No Git commit/push
or package publication is included.

## 2. Frozen source intent and admission before measurements

Reference: [1YCR](https://www.rcsb.org/structure/1YCR), version **1.5** from the
[official revision history](https://www.rcsb.org/versions/1YCR). Retain
[Kussie et al.](https://pubmed.ncbi.nlm.nih.gov/8875929/) and deposition attribution.
The [archive usage policy](https://www.wwpdb.org/about/usage-policies) covers PDB
archive data under CC0. It does not supply terms for unrelated models/articles.

After scope approval, acquire only the versioned mmCIF reference, its provenance/
revision metadata and at most one official validation artifact. Resolve the real
versioned download through the archive; do not fabricate a URL or substitute a
newer/current file silently. Record actual URLs, timestamps, sizes, raw/expanded
SHA-256 and internal entry/revision identifiers before any measurement.

Acquisition bounds: 2 MiB per compressed coordinate/validation file,
8 MiB expanded per file, 1 MiB per metadata response and 32 MiB total retained
source material. Limits are operational guards, not scientific admission rules.
No unbounded crawl, structure search, model/weight download or retry loop. Report
an unavailable validation artifact separately; do not infer that it validates
the exact coordinate revision unless its provenance establishes that relation.

Receive the entire reference through MolSysMT before selecting one coordinate
view. Require one represented structure for this T0; if several are present,
stop before measurements rather than silently selecting a favorable model.
Record native `structure_index=0` and the source model identifier only when
actually available. Validate the intended MDM2 and p53 chain/entity correspondence
from owner-provided IDs/names; author labels, label IDs and native indices remain
distinct. Do not treat declared polymer length as observed coordinate coverage.

The working reference is the deposited receptor–peptide pair, analyzed as an
isolated nonperiodic complex. Preserve crystallographic box/assembly metadata;
no symmetry-image construction or periodic contacts. If the selected source pair
cannot be identified unambiguously or needs an unreviewed assembly transform,
stop and return that source-admission question.

## 3. Chemistry, observations and source profile

Preserve all original source bytes. Select existing observed receptor and peptide
heavy atoms for measurements; exclude hydrogens/isotopes and waters/other entities
from these two endpoint populations through MolSysMT selections, not string
parsing or deletion of the retained source. Record excluded populations/reasons.
Require unique atom/group/chain mappings, finite coordinates and at most **2,048
selected atoms total**. Missing groups/atoms, termini, stereochemistry, protonation,
formal charges and chemical completeness remain source-declared or unassessed.
No reconstruction, hydrogen addition, capping, minimization or chemical repair.

Use MolSysMT's selected primary alternate-site policy, retaining its original
occupancy/alternate-location observations and unknowns. Do not choose alternates
by a favorable contact outcome. Report any metadata absent from the supported
reader. If observed-atom mapping or required observation evidence cannot be
retained, stop before geometry; a complete missing-polymer-position map must
not be fabricated from observed group IDs.

A native reader may derive connectivity as bookkeeping. Record supported
`bond_evidence` and `connectivity_completeness`; distinguish source chemistry
from inferred graph information. No force-field, energy or atom typing is used.
The inspected mmCIF topology wrapper declares but does not read a
`get_missing_bonds` option. Do not pass that option and claim inference was
thereby disabled. This is a **static source observation**, related to existing
[uibcdf/molsysmt#304](https://github.com/uibcdf/molsysmt/issues/304), not a newly
executed public-route failure. An explicit-only reader contract remains owner
work; no downstream parser or inference workaround is introduced.

The inspected development source is MolSysMT
`ed09f64539a5af6c1dbe9bd352c7ef65dcd4a7a6`; the checkout previously used by the
shared profile remains older. Before actual T0 work, choose and qualify an exact
application profile at the inspected source (or explicitly review a replacement),
including interpreter, installed origin/native extension and dependency versions.
Use a separate checkout/profile if necessary; do not silently switch a shared
editable installation, reuse an unrelated wheel as qualification, or rebuild
beyond the resource envelope. The closed occupancy issue
[uibcdf/molsysmt#556](https://github.com/uibcdf/molsysmt/issues/556) and source
inspection support selecting a current reader; they do not qualify this future
installed composition. This gate was pending at preparation; it now passes in the
[exact isolated profile](mdm2_t0_qualification.md). Another composition still
needs its own receiving before use.

## 4. Approved geometry definitions and controls

These values are **approved T0 diagnostic definitions**, not biological thresholds
or global PeptideMT selection policy. They are fixed before observing T0 results.

| Item | Fixed definition |
| --- | --- |
| Endpoints | The verified observed heavy-atom populations of MDM2 and the p53 peptide; atom indices and source identities are retained on both axes |
| Boundary / units | Isolated complex, `pbc=False`, CPU/double precision; report distances and RMSD in nm via owner quantity APIs |
| Contact maps | Owner `get_contacts`, inclusive distance threshold 0.45 nm; diagnostic sensitivity at 0.40 and 0.50 nm. No predicted binding label is assigned |
| Raw distances | Owner `get_distances` for the same ordered endpoints; retain the unthresholded matrix and axis mappings |
| Alignment | Owner `least_rmsd_fit`: fit verified receptor C-alpha correspondences, transform the whole selected complex, then owner `get_rmsd` on peptide heavy atoms **without another peptide fit** |
| Numerical tolerance | 0.000001 nm for identity/rigid-transform distance and fitted-RMSD comparisons; this is numerical bookkeeping, not experimental precision |
| Boundary pairs | Record any pair within that tolerance of a contact threshold; require map invariance outside this predeclared band rather than silently reclassifying borderline pairs |

Three views only, with identical molecular identities:

1. **Reference:** an independent owner copy of the received observed reference.
2. **Whole-complex rigid transform:** owner `rotate` using +90 degrees about z, with matrix
   `[[0,-1,0],[1,0,0],[0,0,1]]`, then owner `translate` by (1, 2, 3) nm, on both endpoint populations.
   Fit only receptor anchors to the reference and assess peptide geometry there.
3. **Adverse geometry control:** owner `translate` of peptide atoms only by
   (10, 0, 0) nm; receptor stays fixed. Fit the receptor in the same manner.
   This is a displaced pose, not an experimental nonbinder or a new sequence.

A proper rotation preserves handedness. Require at least three unique
non-collinear receptor fit atoms; ambiguous correspondence or a degenerate fit
fails admission. Do not use independent peptide superposition that would erase
the displacement. Do not normalize, mutate or regenerate peptide sequences.

## 5. Prespecified outcomes and retained evidence

| Gate | Passing outcome / required limitation |
| --- | --- |
| Source receiving | Exact file/revision identity, owner-provided observed mappings and one coordinate view are recorded. Unknown chemistry and source/validation mismatches remain explicit |
| Reference | Receptor-fitted peptide RMSD is within tolerance; finite nonempty endpoint distance matrix and at least one primary cross-chain contact are returned |
| Whole-complex transform | Receptor-fit and peptide RMSD are within tolerance; raw interchain distances agree within tolerance and contacts agree outside the declared boundary band |
| Displaced peptide | Receptor fit remains within tolerance; peptide RMSD is 10 nm within tolerance; no cross-chain contacts at any of the three thresholds |
| Preservation | Source bytes/native reference are unchanged; each view is a distinct owner copy. Source/derived/inferred information, axis maps, units, settings and actual failures remain recoverable |
| Saved inspection | Inspect saved outputs and verify declared file references without recalculating geometry or crediting a new scientific computation |

A failed gate remains failed; do not change the displacement, cutoff, tolerance,
source, selection or alternate-site choice to obtain a passing result. Diagnose
technical defects before any bounded retry. A material scientific definition or
source-domain change returns to investigator review. Failure of source/profile
admission is not completion of the geometry phase.

Retain one case report, raw owner-returned distances/contact maps and RMSDs,
source/atom/chain maps, conversion reports/warnings, exact code/environment
manifest and operation statuses. Native molecular snapshots, if needed, use
MolSysMT's supported storage/conversion with explicit fidelity reporting; NumPy
may retain already returned arrays. Recorda owns optional caller-managed file
references/checking; Ackredit owns any actually reached attribution. No generic
serializer, resolver or automatic library session is copied into PeptideMT.
Missing recording providers must remain visible; they do not fabricate science.

## 6. Approved implementation and execution envelope

After scientific approval, use a small case-specific development coordinator /
example, with all molecular parsing, selections, copies, transformations,
alignment and geometry delegated to supported MolSysMT APIs. PeptideMT owns the
question, output interpretation and prespecified gate comparison. Do not put
new scientific operations in its public package merely for this case.

After source acquisition and manifest freezing, run numerical workers offline.
No implicit CCD, model, dependency or other asset downloads, package installation
or unplanned child dispatch. If the owner route needs another asset, stop at
source-profile admission and report it before measurements. Profile receiving
must have its own bounded engineering evidence; it cannot hide a build/install
inside the scientific worker or its output budget.

Current envelope: serial workers, CPUs 0/1, one numerical thread, **2 GiB sampled
aggregate supervisor/descendant RSS stop**, **4 GiB available host-RAM reserve**,
8 GiB virtual-address-space ceiling, 180 s wall /120 s CPU per numerical worker,
and 64 MiB task output ceiling. Recheck headroom before/throughout each worker;
stop only owned work on breach. Download timeouts/bytes are bounded separately.
No GPU, model assets, learned evaluation, descriptor calculation, docking/search,
sequence proposal, training or feedback. Do not start a local molecular viewer.

This is the approved T0 envelope within the standing conservative shared-host
approach. The D50-specific 4 GiB reserve exception is **not** transferred here.
Once T0 scope is accepted, D49 delegates routine technical checks and diagnosed
retries within its envelope; another permission round is not required per API
call or run. Changes to scientific criteria or substantially larger allocation
retain their existing review boundary. Count actual acquisition/conversion/
geometry/inspection work, not fictitious learned-model calls.

## 7. Recorded decision and stop boundary

The investigator approves **this T0 work order** after the concrete scope
explanation. D51 authorizes the described case-specific receiving, coordinator
and finite geometry qualification; it does not approve a
new predictive model, T1, target-conditioned generation, clinical conclusion,
M1–M8 changes, source/Git consolidation or publication. The shared-profile entry
gate must still pass before any geometry. Stop after the single reference package
and honest gate report, including an adverse or incomplete outcome.

The [preparation receipt](evidence/mdm2_t0_work_order_preparation.json) binds this
proposal to inspected source/API evidence and actual preparation activity. At
that preparation checkpoint there was no received coordinate file, implemented
T0 helper, geometry result, new model, new commit or accepted scientific decision.
D51 subsequently approves the scope, not an unexecuted result.

Implementation receiving is tracked in the [checkpoint](mdm2_t0_implementation.md);
source download, artificial checks and interrupted profile preparation are distinct
from actual source/geometry qualification.

## Scoped host-reserve adjustment

The investigator subsequently explicitly selects a **2 GiB available-host-RAM
reserve** for this T0 work. The [adjustment record](evidence/mdm2_t0_resource_adjustment.json)
retains the original 8 GiB authorization and interrupted evidence unchanged.
The task aggregate RSS stop remains 1 GiB; CPU/thread, virtual-memory, timing,
output, source and scientific criteria remain unchanged. This is not the D50
exception and does not change another workstream or authorize GPU/model/Git work.

The investigator then explicitly **corrects** that intermediate adjustment to
**4 GiB host reserve and a 2 GiB aggregate task RSS stop**. The
[current correction](evidence/mdm2_t0_resource_correction.json) supersedes the
2 GiB-reserve/1 GiB-stop record without rewriting it. The intermediate build
was interrupted only in its owned process group; this is not a provider failure.
All scientific criteria and remaining limits are unchanged.

## Completed T0 receiving — 2026-11-06

The [qualification](mdm2_t0_qualification.md) and
[execution evidence](evidence/mdm2_t0_execution.json) complete this scope. A single
recorded `platform.processor`/`uname -p` metadata prelude resolves h5py cold-start
requirements before the strict no-unplanned-child phase; no parser, digestion,
chemistry or criterion is bypassed. The reference/rigid/displaced views pass
without repeating successful geometry. Remaining workspace/reporting/source
publication tasks are separate from the completed finite T0 qualification.
