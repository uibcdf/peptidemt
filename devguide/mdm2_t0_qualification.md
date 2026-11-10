# MDM2 T0 qualification: observed reference and geometry controls

Status: **completed within the D51 T0 scope**, 2026-11-06. Local source/fixture
delivery; no commit, release or predictive/biological acceptance is implied.
Owner: [PeptideMT #33](https://github.com/uibcdf/peptidemt/issues/33).
The [approved order](mdm2_t0_work_order.md), [authorization](evidence/mdm2_t0_authorization.json)
and [final resource correction](evidence/mdm2_t0_resource_correction.json) retain
their separate scientific and operational authority. The earlier
[implementation checkpoint](mdm2_t0_implementation.md) remains historical.

## Actual source and molecular admission

MolSysMT receives the official [1YCR revision 1.5](https://www.rcsb.org/versions/1YCR)
reference through its public conversion APIs. Source entry/revision and a single
source coordinate model are checked through the owner-returned parser object.
The expanded coordinate file remains SHA-256
`03f62994ea1ff55d98c0d9d835b706319e523367fce56d9deb51b850c83e47a8`.
Retain [Kussie et al.](https://pubmed.ncbi.nlm.nih.gov/8875929/) and deposition
attribution. No local molecular parser, sequence normalization, reconstruction,
hydrogen addition, capping or chemical repair is introduced.

The selected observed populations are 705 MDM2 heavy atoms in chain A and
113 p53 heavy atoms in chain B. There are 85 and 13 observed groups, respectively,
with 85 receptor C-alpha fit atoms. All 818 represented atoms are selected;
98 source/native group correspondences and unique source atom IDs are checked.
Author/label/native indices remain distinct. Source model ID is `1`; native
structure ID is unavailable and recorded as null, separately from index 0.
MolSysMT validates non-collinear fit anchors before applying its transformations.

The reader retains primary occupancies and no alternate-location observations
for this file. Its graph contains **739 explicit and 96 inferred bonds**, with
connectivity completeness **partial**. This is bookkeeping, not chemically
complete preparation. The owner conversion report says `equivalent` within
`chemical_state`, is **not exhaustive**, and reports no issues in that audited
scope. It does not certify every source semantic or a simulation-ready chemistry.
Crystallographic/assembly metadata is retained; measurements use the deposited
A/B pair as an isolated nonperiodic complex, without lattice/assembly transforms.

## Fixed geometry outcomes

MolSysMT owns copies, rotation/translation, receptor-only fitting, distances,
contacts and RMSDs. All output distances are explicitly extracted in nm under
a non-default angstrom application policy. The peptide is measured after
receptor fitting, without independent peptide superposition.

| View | Receptor RMSD (nm) | Peptide RMSD (nm) | Atom-pair contacts at 0.40 / 0.45 / 0.50 nm |
| --- | ---: | ---: | --- |
| Reference | 4.02e-16 | 4.21e-16 | 105 / 253 / 461 |
| Whole-complex rigid transform | 1.34e-15 | 1.36e-15 | 105 / 253 / 461 |
| Peptide-only 10 nm displacement | 4.02e-16 | 10.0 | 0 / 0 / 0 |

All **29 recorded checks pass**. The largest rigid-transform distance difference
is `3.9968028886505635e-15 nm`, below the fixed `1e-6 nm` numerical tolerance.
There are no pairs in the predefined boundary bands. The original reference
coordinates remain unchanged after each owner copy/view. Raw arrays are float64
distance/coordinate data and Boolean contact maps with explicit units and axis
mappings; the retained array artifact SHA-256 is
`7c46c1a2d28fe520f1ab93d59ca02034011fb3de93ae81990d5a4979f18a7ae2`.

A fresh reader verifies saved file identity, units and fixed definitions without
importing NumPy, MolSysMT or learned providers. A subsequent, separate NumPy
inspection summarizes the already returned arrays and checks source/group maps;
it performs no new molecular geometry. No successful geometry run is repeated.

## Exact installed profile and diagnosed failures

The separate Linux/Python 3.14.7 Conda fixture is built offline from cached
Conda-forge packages and isolated development checkouts. The standard Conda
name `py-mmcif` supplies Python distribution `mmcif` 1.1.1. Native `pip check`,
actual source/native origins, unchanged source pins and application unit-policy
preservation pass. The profile records 3,258 pinned files plus its full package
inventory; it is not the shared environment or a public distribution claim.

| Provider | Fixed source |
| --- | --- |
| MolSysMT | `ed09f64539a5af6c1dbe9bd352c7ef65dcd4a7a6` |
| SMonitor | `ccdcace55ba5caf431b4a6a6904d8d18173114a3` |
| DepDigest | `0884f0cc1dd60b79ed01930e68d80c87e51744c9` |
| ArgDigest | `7e09e974c36bcf5cace99a7b898d0f5f7a9d3ff2` |
| PyUnitWizard | `9d74f0e1e911d78c1906948e74ce8da93935557d` |
| MolSysViewer | `73a6f388e09146650349dfe83564ae318ba20298` |

Native extension SHA-256:
`9e18e308ef6976d4c12981564f069ce26bc0db906c42a285052891abb87dcb72`.
Actual key third-party versions are NumPy 2.4.6, pandas 3.1.1 and h5py 3.16.0.
No viewer/render process is started. Optional Recorda/Ackredit integration is
not requested/installed in this fixture; host-owned provenance and citations
remain explicit, with no claim of live portable attribution.

Preserved earlier failures and their disposition:

- The original two builds stop on the then-applicable 8 GiB reserve; an
  intermediate build is explicitly interrupted for the investigator's resource
  correction. Their resource records are not relabeled as unused or successful.
- The inherited system-site venv fails `pip check` on unrelated Amber packages.
  Cause and isolation are reported in [MolSysSuite #82](https://github.com/uibcdf/molsyssuite/issues/82#issuecomment-6678822888).
  No shared package or unrelated component is repaired downstream.
- The first offline solve uses the Python name `mmcif` as a Conda package;
  correcting this consumer specification to `py-mmcif` resolves that failure.
- The first geometry dispatch stops before reading the molecular input because
  h5py's cold platform query invokes `uname -p`. This single host-metadata probe
  is explicitly declared/recorded before the strict no-unplanned-child phase.
  Network and all other unplanned commands remain prohibited. The misleading
  argument classification is reported in [MolSysMT #601](https://github.com/uibcdf/molsysmt/issues/601).

The RSS regression in [PeptideMT #38](https://github.com/uibcdf/peptidemt/issues/38)
is corrected locally: process traversal includes every thread's children list.
Its real 32 MiB-child guard fails before and passes after. Earlier compiler
records may omit thread-created children; do not infer a complete process-tree
peak retrospectively. The successful clean installation and geometry use the
corrected supervisor. The issue retains local/unpublished delivery status.

## Verification, resources and scientific limit

Published Pytest Receptor 1.2.2 and native pytest record **15 passed**: 11 T0
artificial interpretation/integrity checks, the real RSS regression, and the
existing timeout, output/host-memory and parent-death process guards. No molecular
or learned provider is imported in that test run. The complete raw outputs,
failed-before evidence, exact code snapshots and selected scope are retained.

All substantial work is serial on CPUs 0/1 with one numerical thread and no GPU.
The current envelope is a 4 GiB available-host-RAM reserve and 2 GiB sampled
aggregate task RSS stop. The geometry run takes 5.37 s and peaks at
309,362,688 bytes (about 295 MiB); the clean-source installation peaks at
546,844,672 bytes. Numerical wall/CPU/virtual-memory/output limits remain intact.
The [execution receipt](evidence/mdm2_t0_execution.json) binds the actual stages,
files, failures, environment and later cleanup disposition.

T0 establishes faithful observed-coordinate handling and these artificial
geometry controls on one known complex. It does not establish binding prediction,
affinity, specificity, anticancer action, cellular entry, design improvement or
biological validation. Missing source chemistry/coverage remains unassessed;
the independently dated validation PDF is not matched to an exact coordinate
hash. T1, docking, generation, model/GPU execution and publication remain outside
this order. HydrAMP resources, M1–M8, selectors and historical acceptance remain
unchanged. No commit/push/tag/release is created.
