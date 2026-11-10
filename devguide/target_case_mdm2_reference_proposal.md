# Proposed first target-reference case: human MDM2 and a p53 peptide

Status: **feasibility analysis delivered; subsequent D51 approves only the
concrete T0 structural-reference work order**, 2026-11-05. Owner: [PeptideMT #33](https://github.com/uibcdf/peptidemt/issues/33).
This is the bounded case-analysis output of
[continuation-plan package 6](continuation_plan_2026_11_04.md#6-select-a-feasible-targetfunction-case).
The investigator commissions preparation of this proposal after the dev9 review.
No target implementation, coordinate preparation, scientific calculation, model
selection/execution or new D decision follows from the analysis.

The subsequent [concrete T0 work order](mdm2_t0_work_order.md) is approved
under D51, including its controls, definitions, admission gates and separate
resource envelope. Its [completed T0 qualification](mdm2_t0_qualification.md)
distinguishes exact profile/source/geometry receiving from predictive evaluation.
The [earlier checkpoint](mdm2_t0_implementation.md) retains the interrupted attempts.
T1 prediction and the broader design case remain unapproved and unexecuted. The latest source inspection and connectivity-policy observation
are recorded there; the earlier source snapshot below retains its review scope.

## Recommendation and scientific question

Propose **recognition of the p53-binding interface of human MDM2** as a narrow
first target/function reference. Use a published native peptide complex to make
identity, target participation and reference geometry inspectable. The later
design question would be whether supported peptide proposals can retain or
improve an independently assessed binding property under a declared chemistry
and assay. This memo does not select a generator or assert that this capability
already exists in PeptideMT.

The structural precedent is [Kussie et al., 1996](https://pubmed.ncbi.nlm.nih.gov/8875929/),
which reports the MDM2–p53 interaction. The reference candidate is
[RCSB entry 1YCR](https://www.rcsb.org/structure/1YCR): human MDM2 chain A,
p53-derived chain B, declared lengths 109 and 15, X-ray resolution 2.60 Å.
The entry currently reports revision 1.5; its
[revision history](https://www.rcsb.org/versions/1YCR) dates that revision to
2024-02-14. The entry lists 98 modeled versus 124 deposited residues overall.
These metadata are inspected; no local coordinate file or per-chain missing-group
map has been qualified. Deposited sequence must not be treated as fully observed
coordinates or a fully determined chemical state.

Molecular binding is the proposed first functional endpoint. An eventual
biochemical comparison could use a matched equilibrium dissociation-constant
assay with molar units and stated conditions. No matched panel is acquired here;
IC50, Ki, docking scores and cell viability must retain their own meanings.
Displacement of p53, cellular entry, pathway response and anticancer activity
would require additional distinct evidence. None is a first-stage success claim.

## Why this narrower case

| Existing direction | Disposition for this first reference exercise |
| --- | --- |
| Full [CPP-05 p28](cpp_guided_projects.md#cpp-05--p28-a-relatively-straightforward-target-associated-anticancer-cpp) | Keep its existing role as the proposed early target+CPP+anticancer reference. This narrower geometry exercise does not replace that portfolio recommendation, equate p28 with a p53 mimetic, or change its direct target |
| Full [ATSP-7041 case](case_study_cpp_anticancer_mdm2_mdmx.md) | Retain the dual-target, modified-chemistry and cellular-evidence goals. They add obligations beyond the intended first structural reference |
| [GABARAP + CPP](design_examples.md#2-case-a--protein-binder-with-cpp-properties) | Retain its existing conceptual domain/chemistry and access questions; no compatible linear seed or qualified CPP/recognition route is assumed |
| Narrow MDM2–p53 reference proposed here | A single deposited complex provides an inspectable structural anchor. It requires fewer simultaneous new chemical/access/phenotype claims; this is the feasibility inference motivating the recommendation |

This is a separately proposed subproblem related to the MDM2/MDMX scientific
compass, using a different reference molecule. The p53-derived fragment is not
ATSP-7041 or p28. No new numbered CPP case, family model or selected therapeutic
is created. The investigators retain the choice of scientific case.

## Stages, outcomes and stopping points

| Stage | Proposed work and evidence | Readiness / meaning of completion |
| --- | --- | --- |
| T0: identity and structural-reference qualification | Pin exact public coordinate/validation bytes and revision; receive through MolSysMT; preserve deposited/observed mappings, construct, chain and atom identities, missing data and chemical unknowns. Inspect defined reference geometry with existing MolSysMT operations | Feasible to prepare with inspected owner APIs, but not executed/qualified here. Completion establishes faithful reference handling, not predictive recognition or target-aware design |
| T1: peptide-recognition evaluation | Select and qualify an actual peptide-capable evaluator with a sourced positive/weak-binding panel, explicit input chemistry, assay scope, controls and prospective criteria | Not implementation-ready: no evaluator or matched panel is selected/qualified. Native-complex geometry alone cannot pass this stage |
| Later design study | Choose a compatible proposal operation and compare its contribution with an appropriate fixed-reference/control policy under declared opportunities | Requires a separate scientific work order. HydrAMP AMP conditioning is not transferred to MDM2 recognition; no target-conditioned route is commissioned |

Only approval of the case and a concrete T0 work order would permit progressing
beyond this feasibility memo. T0 would stop after one reference package/report
and reusable saved inspection. New molecular preparation, engine installation,
search/scoring, sequence changes, feedback and experiments remain separate.
A T0 success cannot be counted as completion of T1 or the library's design goal.

## Chemistry, measurements and controls for the future T0 order

Preserve the actual deposited reference first. Any later canonical-L, linear
proposal domain needs explicit terminal, stereochemical and modification
choices; a one-letter projection cannot supply them. Do not silently rebuild
missing groups/atoms, protonate, cap, remove waters or change constructs. If an
operation requires more chemistry than the reference establishes, report the
limitation or a separately reviewed hypothetical realization.

Propose one isolated receptor–peptide reference complex with explicit
nonperiodic geometry. Preserve crystallographic box/assembly metadata without
silently using lattice-image contacts or inheriting a provider's periodic
default. The exact assembly/observed-atom selection must be fixed with its file.

Select receptor and peptide by verified source mappings, keeping group/atom
indices distinct from database identifiers. A future receptor-aligned peptide
RMSD must distinguish alignment atoms from evaluated peptide atoms and identify
which missing/alternate atoms are excluded. Preserve physical units and use
PyUnitWizard through the owners; no local coordinate parser, RMSD, contact or
unit-conversion implementation belongs in PeptideMT.

A coordinate-identical reference and an owner-transformed whole-complex copy
can check identity/alignment invariance. An explicitly displaced peptide pose
can be an adverse **geometry** control. Such constructed poses are not measured
nonbinders and cannot validate discrimination or biochemical affinity. Distance/
contact definitions, cutoffs and numerical tolerances must be fixed in the T0
order rather than selected after results. No cutoff or acceptance threshold is
adopted by this memo.

The target would determine reference selection and structural evaluation in T0.
It would not condition generation or a sequence selector. In the present work,
no target-dependent execution occurs at all. MDMX selectivity, cytosolic delivery,
hemolysis, cellular phenotype and clinical utility stay unassessed. Macrel's
AMP/hemolysis outputs cannot certify MDM2 binding or p53 mechanism.

## Verified owner map and actual local state

| Owner | Relevant inspected public surface | Scope of this observation |
| --- | --- | --- |
| MolSysMT | `basic.convert`, `basic.get`, `basic.select`, `file:cif` conversion route; `structure.get_distances`, `get_contacts`, `get_rmsd`, `translate` | Source inventory at `71fbe4f46d3c70e4e973c8025f01752a8c9b1084`; no import, parsing or geometry execution. `convert` exposes strict/report options. Contacts operate on selections within one molecular system; their map is resident and atom pairs are distinct from group-index output |
| MolSysViewer | Scientific rendering/inspection owner | Source/instructions at `73a6f388e09146650349dfe83564ae318ba20298`; optional future visualization, no viewer/GPU started |
| DockingMT | Existing `dock`, `score`, preparation and evaluation surfaces | Committed README at `1837eecb32ba87e5e78697ac667f9d5a7de9c3ae` describes its qualified starting profile as a rigid protein and a declared small-molecule state. No peptide-docking qualification is established by this bounded inspection |
| PeptideMT | Scientific question, requirements/evidence coverage, composition, interpretation and selection | Current plan/issue #33; no new representation or generic campaign framework is prescribed |
| Recorda / Ackredit | Existing caller-owned recording/references and attribution | Reuse supported boundaries when a real work order reaches them; this memo creates no runtime session or scientific credit |

[MolSysMT API source](https://github.com/uibcdf/molsysmt/blob/71fbe4f46d3c70e4e973c8025f01752a8c9b1084/molsysmt/structure/get_contacts.py)
and [DockingMT committed scope](https://github.com/uibcdf/dockingmt/blob/1837eecb32ba87e5e78697ac667f9d5a7de9c3ae/README.md)
provide immutable owner links. Source inspection is not a claim of installed
cross-component qualification. MolSysMT and MolSysViewer are respectively 122
and 111 commits behind fetched main in this snapshot; their worktrees are clean.
A later runtime order must deliberately select and qualify actual development
sources, preserving existing evidence. No shared checkout/environment is pulled
or replaced here.

DockingMT has concurrent documentation/example work. The inspected dirty README
and committed version agree on the small-molecule starting profile; its worktree
is preserved, and actual read-file hashes are recorded separately. No future
peptide-engine support is inferred from uncommitted documentation. No provider
bug or missing reusable API is demonstrated for T0, so no speculative provider
issue is opened. An actual selected T1 route would receive its owning proposal
with concrete consumer evidence before implementation.

## Access, evidence and decision requested

The [wwPDB archive policy](https://www.wwpdb.org/about/usage-policies) makes archive
data available under CC0; retain attribution to the deposition and primary study.
This does not establish permissions for a future model, article reproduction or
unselected external assets. Metadata browsing supplies no exact downloaded-file
SHA or coordinate admission. The direct RCSB REST metadata endpoints were not
accessible through the web tool; that is an access limitation, not proof that
data are absent. The official entry/history pages and primary paper abstract
supply the cited feasibility facts.

The [analysis receipt](evidence/target_case_mdm2_reference_review.json) pins local
source observations, owner revisions, dev9-review identities and access limits.
No structures are downloaded/preprocessed, no scientific providers run, and no
learned models, GPU, generation, mutations, docking, training or feedback execute.
The D50 serial resource profile remains scoped to its own synthetic/packaging
checks; it is not transferred to future target execution.

**Recommended investigator decision:** choose or reject this narrow MDM2
reference case; if chosen, commission only a concrete T0 preparation/inspection
work order first. Keep the full target-aware design goal open until T1 and an
actual design comparison have qualified methods and evidence. This is a proposal,
not an accepted case, an execution permission or a new scientific acceptance.
