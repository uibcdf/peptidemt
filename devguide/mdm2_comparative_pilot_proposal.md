# MDM2 fixed-peptide pose pilot: proposal for scientific review

Status: **prepared proposal; no implementation or execution commission**,
2026-11-10. Owner: [PeptideMT #33](https://github.com/uibcdf/peptidemt/issues/33).
The investigator authorizes preparing this protocol after the
[alternatives review](peptide_protein_binding_survey_2026_11_10.md).
The [BindCraft–MDM2 source audit](bindcraft_mdm2_source_review_2026_11_10.md)
explains why structural and experimental-affinity arms must be separate.

Subsequent investigator-directed [input-profile preparation](mdm2_input_profile_preparation.md)
and [node/five-node resource assessment](mdm2_node_feasibility.md) are delivered.
Their new read-only MolSysMT coverage request is separate from scientific pilot
execution. They preserve this proposal's chemistry, method and criterion review
boundaries; the potential CPU route need not wait for new GPU hardware.

## Proposed first question and scope

For one fixed, source-mapped MDM2–p53 identity/view, can an owner-supported
classical docking route and a modern complex-prediction route produce and
select geometrically accurate poses, with declared information and budgets?

Recommend **HADDOCK3 as the first classical candidate and Boltz-2 as the first
modern candidate**, for owner review, not adoption. The former has a documented
peptide/ensemble route; the latter supports receptor templates and protein-chain
binding-site constraints in its inspected contract. FlexPepDock remains an
alternative for a separately declared refinement question. BindCraft/BoltzGen
generation is a later study, not an extra arm using a different task here.

This first case is a finite geometric feasibility demonstration. It cannot rank
methods generally, establish affinity ordering, discriminate biological binding,
demonstrate a novel target/site or complete the original D52 selection objective.
Three seeds are reproducibility samples, not three independent molecular cases.

## Fixed reference and information contract

Reuse the already [qualified T0 1YCR revision 1.5](mdm2_t0_qualification.md):
source SHA-256 `03f62994ea1ff55d98c0d9d835b706319e523367fce56d9deb51b850c83e47a8`,
source model ID `1`, and its retained source/native axes. The observed populations
are 85 receptor and 13 peptide groups. Use that observed view explicitly; it is
not automatically the deposited full sequence or the solution assay construct.
Preserve the qualified source and do not repeat its accepted geometry checks.

The peptide identity is fixed. No sequence generation, substitution, labelled
BindCraft specimen, missing-heavy-atom reconstruction or new target is admitted.
New chemical preparation requires an explicit model recipe, through MolSysMT,
before any engine input is accepted. Protonation, terminal/state treatment,
hydrogens and retained waters/other material must be stated as evidence or
modelling hypotheses. The proposal does not select their unknown values.

Declare this as **known-site, holo-receptor-assisted modelling**. The receptor
coordinates and a frozen receptor-only site declaration are permitted inputs;
the reference peptide coordinates are reserved for evaluation. Do not initialize
the classical arm with the native peptide pose, supply a complex template to
the modern arm, or derive candidate-specific restraints from the answer.

The two arms must receive the same declared biological identity/view and
information content. MolSysMT owns extraction, source sequence projection,
atom/group correspondence, preparation and coordinate operations. Engine-native
sampling is part of the declared scientific method, not a reason to implement
local peptide builders or torsion code.

An input-parity gate must verify what each actual provider accepts. The pinned
[Boltz prediction guide](https://github.com/jwohlwend/boltz/blob/b1ebfc46ecf57f5414e0d1a6f9027bbb122c53bc/docs/prediction.md)
documents protein templates and pocket/contact constraints, including a protein
binder chain. That is inspected support, not tested receiving. Receptor-only
templates must physically exclude the answer peptide; automatic template-chain
matching is not trusted to enforce the exclusion. MSA/template provenance,
site conditioning and any external acquisition are frozen and retained.

If the routes cannot express comparable information, return an explicit
information-stratified demonstration instead of a head-to-head winner. Do not
claim a blind docking comparison. Training/site familiarity, including this
widely known historical complex, remains an exposure limitation.

## Outputs and observables proposed for review

Retain every launch, failure, original score and native pose rank, submitted and
returned molecular axes, software/parameter/source identities, timing and memory.
Predicted structures are hypotheses. Input/output chemical changes or incomplete
maps stop quantitative receiving rather than being normalized silently.

Primary geometric observable: **peptide backbone positional RMSD after receptor
alignment**, in explicit nm, using a frozen common observed N/CA/C/O atom domain.
MolSysMT returns the selections, correspondence and fit. Never fit the peptide
independently, compute a local matcher or silently reduce the evaluation domain
for missing output atoms. Check actual backbone coverage before setting its
final expected cardinality. Do not call this chemically symmetry-corrected RMSD
unless the separate complete-chemistry correspondence contract actually applies.

Report native-ranked top-1 and best-within-top-5 separately. The latter is an
evaluation oracle, not the method's own selected prediction. Rank direction,
cluster-versus-pose meaning, aggregation and deterministic ties must be frozen
per method. Distinguish the method's complete internal sampling budget from the
five retained evaluation candidates; equal output count is not equal search effort.

Propose a **case-specific geometric feasibility criterion**, for discussion:
native top-1 RMSD at most 0.2 nm in at least two of three predeclared seed runs,
with all custody/mapping/coverage gates satisfied. Report every continuous value
and failure regardless of this criterion. This proposed tolerance is not a
universal peptide-docking definition or a binding/affinity threshold. Its acceptance
and the exact fit/atom domain precede execution; no pass is asserted now.

Use the existing T0 unchanged/displaced reference controls as already accepted
evidence for the coordinate observable. Further output-boundary controls should
refuse mismatched sequences/maps, reference-peptide leakage, missing backbone,
wrong unit or stale producer identity, and preserve source/caller policy.
Artificial displaced poses are geometric adverse controls, not experimental
nonbinders. A failed model call is not a predicted biological negative.

## Owner and execution readiness gates

1. **Scientific agreement:** fix input view, permitted information, explicit
   molecular-model recipe, geometric observable, proposed criterion and failure
   policy. This document records a recommendation, not investigator acceptance.
2. **Provider readiness:** DockingMT identifies/receives the selected reusable
   route, with MolSysMT molecular transport/preparation and exact input/output
   maps. No PeptideMT-local engine adapter, molecular parser, builder or scorer
   substitutes for missing provider functionality. Current Vina/small-molecule
   receiving does not satisfy this gate.
3. **Exact execution prescription:** freeze source/bundle/weights and terms,
   versions, inputs, complete configuration, MSA/template sources, initial
   conformations, seed identities and per-module sampling/call counts. Do not
   fill gaps with current engine defaults or the paper's incomplete settings.
4. **Bounded feasibility receiving:** demonstrate that the actual route respects
   the accepted host envelope and failure controls. Native engine errors remain
   distinct from unavailable dependencies and admission failures. A reduced
   sampling profile needs scientific justification rather than a positive result.
5. **Pilot execution:** at most three sequential seed launches per admitted arm,
   retaining up to five native-ranked final candidates per launch. These are
   proposed outer caps only; actual underlying scientific-call budgets remain
   unassigned until the exact prescription is reviewed. No retries are selected
   to improve the result; diagnosed routine technical retries retain failures.

Current document/data checks use the standing shared-host ceiling: one serial
job on CPU0/1, one numerical thread, at most 2 GiB aggregate task RSS, and at
least 4 GiB available host RAM. The document-inspection jobs actually choose
stricter 512 MiB sampled bounds. These limits are not evidence that either
candidate model fits. Boltz's CPU route has not been qualified here, and no GPU
use or larger allocation is authorized. Select a feasible host and record a
concrete time/RAM/VRAM/call prescription before any new engine/model is loaded.
The preparation cannot honestly supply measured GPU or model-run requirements.

No implementation or model run is ready to start merely because the protocol
is written. Exact candidates and an executable chemical/owner route remain
readiness gates, not unreported passing checks.

## Separate experimental and generation arms

Keep Li 2010's qualified reported-affinity reference and the 2025 BindCraft BLI
source separate. The latter first needs specimen/chemistry/assay correspondence,
reconciled sample IDs, quality/error meaning and the appropriate numerical
endpoint. Predicted complexes are not structural labels for those experiments.
Poor-fit rows and unknowns cannot be promoted to verified nonbinders for ROC-AUC.

A later affinity/selection protocol must fix its cohort, comparisons, parent/
uniform baselines, missing-result policy and uncertainty before prediction.
Structural confidence, energy and Kd remain different observables. Boltz-2's
small-molecule affinity head is outside the peptide endpoint considered here.
Known source exposure precludes a prospective-blind claim.

Only after a useful evaluation route is defined should BindCraft or BoltzGen
new-sequence generation be proposed, retaining its own exact bundle, chemistry,
candidate/selection budgets and independent evaluation. Preparing this pose
pilot does not commission generation, training, feedback, package publication,
author contact or a new architecture.

The [D14 agreement](design_methodology.md#progression-and-review) governs the
next scientific disposition. This delivery completes source review/proposal
preparation; the independently evaluated D52 demonstrator remains incomplete.
