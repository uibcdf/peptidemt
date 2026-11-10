# 1YCR input profile: owner-supported preparation specification

Status: **preparation delivered; chemical recipe not yet executable/accepted**,
2026-11-10. Owner: [PeptideMT #33](https://github.com/uibcdf/peptidemt/issues/33).
Read alongside the [pose-pilot proposal](mdm2_comparative_pilot_proposal.md) and
[node feasibility report](mdm2_node_feasibility.md). The investigator commissions
preparation and resource investigation, not automatic selection of unknown
chemical states or execution of a new model.

## Frozen evidence and input split

Use the already admitted deposited A/B pair, 1YCR revision 1.5, source model
`1`, native structure index `0`; its coordinate SHA-256 remains
`03f62994ea1ff55d98c0d9d835b706319e523367fce56d9deb51b850c83e47a8`.
The existing T0 map selects 705 receptor heavy atoms in 85 observed groups and
113 peptide heavy atoms in 13 observed groups. No assembly/lattice transformation
or periodic model is selected. Keep the original full source and custody maps.
Do not equate this observed fragment with a full solution construct.

MolSysMT owns reading, group/sequence projection, extraction, geometry,
correspondence, naming/state provenance and preparation operations. PeptideMT
does not parse a molecular file, reconstruct an omitted residue, assign bonds
or generate backbone torsions. The new read-only coverage evidence uses the
existing qualified MolSysMT source/native composition, not an updated sibling
checkout. It detects no heavy-name gaps in its 98 examined residue templates;
it explicitly leaves terminal context and docking readiness unassessed.

Create separate downstream carriers only after the actual provider contract is
received: receptor coordinates/template and a fixed peptide identity/sequence
for prediction; reference peptide coordinates for evaluation only. The known-site
declaration must contain receptor-only source mappings. Never transfer the native
peptide pose into initialization, templates, restraints or output selection.
Do not compute a new receptor-site recipe from the answer as an implementation
convenience. Its receptor residues and information provenance still need review.

## Chemical recipe fields that require explicit disposition

| Field | Evidence available | Preparation recommendation / unresolved choice |
| --- | --- | --- |
| Molecular view | Fixed observed receptor and peptide group/atom maps | Preserve that view; no full-length reconstruction |
| Standard residue heavy inventory | No missing names under the examined exact templates | Reuse the result; it does not assess terminal OXT or prove chemical completeness |
| Termini | Terminal context is explicitly unassessed | Propose a declared linear-fragment terminal hypothesis for review; free termini and capped fragments are different chemical models, not interchangeable defaults |
| Environmental state | No admitted solution pH/protonation recipe | Specify modelling pH, per-residue states, terminal charges and their provider interpretation before preparing inputs; do not infer experimental state from a sequence |
| H atoms / formal charge | Zero explicit H; formal charge missing | Owner-supported explicit addition/assignment with generated-atom and retained-heavy maps; no fabricated caller values |
| Bond chemistry / stereochemistry | Partial bond orders/connectivity; atom stereo missing | Preserve source/inferred evidence; obtain the declared provider assessment or an explicit unsupported outcome |
| Waters / ions / other material | Existing T0 source admission reports no excluded atoms in its 818-atom view | No blanket stripping or new solvent/cofactor chemistry; record engine-generated material separately |
| Missing atoms / new geometry | No missing-heavy reconstruction admitted by the pilot proposal | If a chosen terminal model needs an additional heavy atom or repair, return that specific change for review before execution |
| Engine force field and preparation | Not selected/received | Record topology/parameter identities, terminal/residue patches, H naming and actual changes; engine defaults are not a frozen recipe |

This is intentionally a **specific list of unresolved scientific/provider
values**, not a YAML file that silently fills them. Choosing a pH, terminal
model and residue state list without their review would alter the scientific
input. No claim of a complete chemical preparation is made from successful
coverage inspection. The residue-template report's `assessed` status means
the comparison ran, not that the molecule is chemically validated.

The existing public pieces must be reused rather than reported as absent:
[`get_peptide_chemical_template`](https://github.com/uibcdf/molsysmt/blob/ed09f64539a5af6c1dbe9bd352c7ef65dcd4a7a6/molsysmt/physchem/get_peptide_chemical_template.py)
already constructs coordinate-free linear-peptide chemistry from explicit
residue-state names and free amine/carboxyl terminal states, including terminal
OXT and stored H counts. It does not infer pH, create coordinates or declare
residue stereochemistry. `assess_chemical_template`, `apply_chemical_template`
and `build.add_missing_hydrogens` are existing separate owner operations.
Their actual composition, exhaustive maps and any required terminal repair
must be received for this case; no source inspection proves every composition
route is unavailable. [MolSysMT #558](https://github.com/uibcdf/molsysmt/issues/558)
already owns terminal-completion maps/history, and
[#685](https://github.com/uibcdf/molsysmt/issues/685) owns capped/stereochemically
declared references. Reuse those issues for their respective needs. The latter
does not authorize selecting a cap or silently declaring every L residue `S`.

## Candidate owner profiles

**Classical route, HADDOCK3:** DockingMT #33 remains the existing owner triage.
The candidate uses an explicitly declared MolSysMT molecular state and mapped
engine input, a non-native peptide conformational ensemble and owner-managed
topology, flexible sampling, original scores/ranks and output maps. The
[upstream peptide guide](https://www.bonvinlab.org/haddock3-user-manual/bpg/peptides.html)
recommends conformational ensembles. The ensemble source, actual conformations,
seed and module-specific sampling are therefore scientific prescription fields,
not a generic local builder task. Proposed local execution has `ncores=1`, one
numerical thread and CPU0/1 affinity. A complete runnable scientific config is
not supplied before these values and CNS/binary terms are received.

**Complex prediction, Boltz-2:** the pinned
[input guide](https://github.com/jwohlwend/boltz/blob/b1ebfc46ecf57f5414e0d1a6f9027bbb122c53bc/docs/prediction.md)
supports protein-chain sequences, receptor templates and protein-binder pocket/
contact conditioning. Owner receiving must demonstrate the actual receptor-only
template split, source-to-prediction group maps and any terminal/state limitations
of that representation. A plain sequence is not proof of the same explicit
chemistry as a force-field input. Receptor/peptide MSAs and external acquisition
remain to be chosen: the guide distinguishes precomputed MSA, server acquisition
and single-sequence mode, which it warns may reduce accuracy. Do not choose
`msa: empty` merely to avoid a resource/provenance question. No MSA service
was contacted and no sequence was submitted.

These are candidate profile requirements, not invented public MolSysSuite APIs
or implementation promises. DockingMT's inspected current source still offers
the Vina engine family, not a received HADDOCK3 or cofolding route. The owner must
resolve the reusable cofolding boundary. If chemistry or information cannot be
made comparable, preserve separate methodological strata rather than silently
normalizing them into a head-to-head comparison. Do not invoke Boltz's
small-molecule affinity head for a peptide-Kd endpoint.

## Reviewable continuation

The work that can start without new GPU hardware is owner-led molecular recipe
resolution, existing-input transport/correspondence, CNS/runtime receiving and
data-only output/refusal checks. Appropriate technical runs fall under standing
execution authority once the unchanged scientific inputs/provider exist; repeated
per-command permission requests are unnecessary. Actual engine/model adoption,
new chemistry, GPU allocation and the pilot criterion need their scientific
disposition. The proposed three-seed/five-output outer caps still do not fix
engine-internal sampling or allocate model calls.

The [readiness receipt](evidence/mdm2_node_feasibility_2026_11_10.json) preserves
the executed read-only question, exact original composition, failed serialization
attempt, diagnosed retry and sampled resources. Original T0 geometric evidence
is reused unchanged; no accepted geometry tests or scientific models were rerun.
