# Protein–peptide docking and binder design: comparative exploration

Status: **investigator-requested scientific exploration and recommendations**,
2026-11-10. Owner: [PeptideMT #33](https://github.com/uibcdf/peptidemt/issues/33).
The investigator explicitly requests discussion of alternatives before starting
protein–peptide docking. No method, new chemistry, execution or integration is
accepted by this review. [D53 T1a](mdm2_t1a_qualification.md) remains completed;
[T1b](mdm2_t1b_proposal.md) remains an unaccepted candidate subproblem.
Source identities and observation limits are in the
[review receipt](evidence/peptide_protein_binding_survey_2026_11_10.json).

## Main finding and change to the earlier recommendation

**Binder-design tools deserve serious consideration alongside docking.** Some
now directly address short peptides and have experimental binding evidence.
They can supply candidate sequences and complex models to PeptideMT. They do
not automatically supply an independent assessment of their own designs,
calibrated affinity or the chemical representation needed by every candidate.

The earlier [method review](target_directed_method_review.md) made HADDOCK3 a
reasonable first technical candidate. The present, broader evidence does not
justify treating that choice as settled. A directly relevant 2025 experimental
BindCraft study changes the priority of further investigation. Likewise, 3EQS
admission is a useful possible source task, not a mandatory next implementation
chosen by this review. Reuse T0's qualified 1YCR evidence where applicable.

## Different capabilities that a single pipeline may combine

| Question | Inputs and output | What it does not establish |
| --- | --- | --- |
| Pose docking | Fixed peptide/receptor identities and structures or an ensemble → candidate complex poses | Correct sequence, strong binding or affinity order |
| Complex prediction / cofolding | Usually fixed molecular identities, sequences and optional structures/MSAs → joint complex model and confidence | Binding of a proposed pair or calibrated experimental Kd |
| Binder generation | Target information and design constraints → new peptide sequence, often with a proposed pose | Independent validation of the generated proposal |
| Affinity / selection evaluation | A declared molecular/assay domain and qualified estimator → a stated observable or selection decision | Cellular action, uptake, safety or generalization outside that domain |

Tool names can obscure orientation: designing a protein that binds a peptide is
a different task from designing a short peptide that binds a protein. Each
candidate below must be assessed for the latter task when used as a generator.

## Candidate map and evidence

| Alternative | Actual role for this discussion | Evidence and assessment |
| --- | --- | --- |
| **HADDOCK3** | Information-driven flexible docking, including peptide ensembles | A useful classical comparator when site information is declared. Official peptide workflow exists; the old MDM2 tutorial is not our human-case qualification. CNS and complete-bundle terms need their own receiving. |
| **Rosetta FlexPepDock / PIPER-FlexPepDock** | Local refinement or fragment/ensemble-based global docking | Valuable reference methods for flexible peptide poses. Local refinement needs a suitable starting neighborhood; global protocols and sampling are distinct. Historical pose benchmarks do not establish present affinity accuracy. |
| **AutoDock CrankPep (ADCP)** | Specialized peptide conformational search/docking | Remains a candidate, with the source/distribution, representation and terms correspondence questions retained from the prior review. Do not substitute ordinary rigid-small-molecule Vina qualification. |
| **Boltz-2, Chai-1, AlphaFold3** | Joint complex prediction for fixed identities | A distinct structural comparison route. Training overlap, binding-site familiarity, MSA, chemistry and confidence interpretation need explicit evaluation. Boltz-2's affinity interface is not a qualified peptide-affinity route. |
| **BindCraft / BindCraft2** | Target-conditioned binder generation with structure-based design/selection | Highest immediate relevance to investigate for the MDM2 case because a study tests short BindCraft peptides experimentally. BC2 adds explicit peptide modalities, but the original study does not validate BC2 or its defaults. |
| **BoltzGen** | General all-atom binder generation with peptide protocols | Strong open-source candidate for an extensible catalog. Linear/cyclic peptide evidence, pipeline version, sampling cost and chemical coverage must be assessed separately from miniprotein/nanobody results. |
| **EvoBind2** | Joint sequence/structure design from target sequence, linear or cyclic peptides | Specifically addresses short peptides and reports experimental evidence. Attractive when target structure/site information is absent; initial validation breadth and computational cost limit generalization claims. |
| **PepMLM** | Target-sequence-conditioned generation of linear peptide sequences | Complementary sequence-only generator. Its experimental binding/functional results merit review, while cellular/fusion outcomes and free-peptide Kd remain distinct endpoints. It is not a standalone docking engine. |
| **PepFlow / PepGLAD** | Receptor/site-conditioned full-atom sequence–structure design; some fixed-sequence conformation tasks | Relevant specialist research baselines with public code. Computational interface energies and benchmark “success” must not be described as measured affinity or wet-lab hit rates. |
| **RFpeptides** | Target-conditioned macrocyclic peptide design | Strong experimental/structural evidence for macrocycles. This is a different chemical domain from the current linear-peptide case. |
| **RFdiffusion3 / Foundry** | General all-atom protein/binder design infrastructure | Important current direction and a possible future provider. Its broader protein-design results alone do not establish short-linear-peptide suitability. |
| **PepFGLD** | Claimed 2026 flexibility-aware peptide latent diffusion | Watchlist: the inspected author README advertises ICML 2026 but still promises future code/model/data links. Conference acceptance and ready reproducible artifacts are separate questions; no runnable bundle is received. |

Sources for the classical rows remain the pinned [earlier review](target_directed_method_review.md),
the [HADDOCK peptide guide](https://www.bonvinlab.org/haddock3-user-manual/bpg/peptides.html),
[Rosetta documentation](https://docs.rosettacommons.org/docs/latest/application_documentation/docking/flex-pep-dock)
and the [primary PIPER-FlexPepDock paper](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005905).
No performance percentage is transferred between their differently defined benchmarks.

## Particularly relevant experimental evidence

**BindCraft and MDM2.** [Filius et al., ACS Chemical Biology, online 18 November
2025](https://pubs.acs.org/doi/10.1021/acschembio.5c00774) report peptides of
10–20 residues: 70 candidates generated, 15 synthesized and seven showing specific
nanomolar binding. The same study reports failures on PD-1/PD-L1. This supports
MDM2-focused investigation, not universal peptide-design success; 7/15 is the
tested selection's outcome, not a measured rate over all generated candidates.
The article's textual site description and figure caption differ, so exact input
configuration needs verification before reproduction. The data have now been
exposed and are not a blinded reference. No supplemental chemical state or
complete dataset is admitted by this literature inspection.

The [original BindCraft paper](https://www.nature.com/articles/s41586-025-09429-6)
provides broader protein-binder evidence. That evidence must stay separate from
the short-peptide study and the newer
[BindCraft2 source](https://github.com/PacesaLab/BindCraft2/tree/8c1a858fdc1bfc94c60846ff11a0d01c9aa44136),
whose README explicitly includes linear peptides below 25 residues and cyclic
peptides. We have inspected these declarations, not executed them.

**EvoBind2.** The [2025 primary study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12280060/)
reports experimentally tested linear/cyclic peptides of 8–20 residues for its
initial target. Its separation of design and subsequent model-based assessment
is useful, but two AlphaFold-derived evaluations are not independent experimental
confirmation or proof of broad target generalization.

**RFpeptides.** The [2025 Nature Chemical Biology study](https://www.nature.com/articles/s41589-025-01929-w)
reports tested macrocyclic binders across four targets, with crystallographic
agreement for selected complexes. This is substantive evidence for future
cyclic-peptide scope, without transferring its results to linear peptides or MDM2.

**BoltzGen.** The [inspected preprint v1](https://pmc.ncbi.nlm.nih.gov/articles/PMC12697729/)
contains linear and disulfide-cyclized peptide experiments, including micromolar
binding. Its broader successes span different binder modalities. The paper's
version and the current code must remain distinct; do not summarize every
modality as nanomolar peptide binding. A later preprint version was found but
its full text was inaccessible here, so its revised quantitative results are
not substituted into the v1 observations.

## Current trends, with their limits

1. **Joint sequence–structure generation.** Binder design increasingly proposes
   both the sequence and interaction geometry. [PepFlow](https://arxiv.org/abs/2406.00735)
   and [PepGLAD](https://papers.nips.cc/paper_files/paper/2024/hash/88ad9774ffcb7a272457e9396f793a07-Abstract-Conference.html)
   make this explicit for peptide-specific flow/diffusion models. Their numerical
   proxy evaluations still need endpoint-specific interpretation.
2. **Complex prediction joins classical docking.** New cofolding models offer a
   different hypothesis for a fixed pair. The [Guan and Keating 2025 benchmark](https://onlinelibrary.wiley.com/doi/10.1002/pro.70331)
   finds important training/binding-site and MSA effects. A familiar MDM2 interface
   is useful for a pilot but cannot demonstrate de novo generalization. No single
   cross-paper percentage establishes a universal winner.
3. **Atom-level and chemical constraints.** [BoltzGen](https://github.com/HannesStark/boltzgen/tree/6472b44e8072187e6eaa51271ae6838245206013)
   and [RFdiffusion3](https://pmc.ncbi.nlm.nih.gov/articles/PMC12458353/)
   broaden atom-level conditioning. “All-atom” does not guarantee arbitrary caps,
   D residues, noncanonical monomers, protonation or covalent topology. Molecular
   interpretation and interoperation still require MolSysMT-owned support.
4. **Control over modality and multiple states.** BC2's named modalities and
   multistate capabilities illustrate movement toward more explicit design
   specifications. Specificity, off-target and developability claims each need
   their own question and evidence; more constraints do not validate themselves.
5. **Experimental and adversarial evaluation matter more.** Negatives, different
   binder formats, assay artifacts, target exposure and independent verification
   distinguish useful evidence from an attractive model. Selecting and “validating”
   with correlated models can exploit their shared error rather than improve binding.

## Structural confidence, affinity and implementation feasibility

Boltz-2's [public prediction contract](https://github.com/jwohlwend/boltz/blob/b1ebfc46ecf57f5414e0d1a6f9027bbb122c53bc/docs/prediction.md)
restricts its affinity request to one small-molecule ligand chain. A peptide
encoded as a protein chain does not acquire that endpoint; encoding it another
way does not establish scientific applicability. We would initially assess
Boltz-2 for complex structure, not treat it as a peptide-Kd estimator.

Likewise, ipTM, PAE, pLDDT, generator likelihood and docking energies have
different meanings. A high-confidence pose is not an affinity measurement.
Ranking against experimental Kd and improving selected candidates remain
separate PeptideMT studies with predeclared baselines and honest unknowns.

Operational declarations are not our measurements:

- The [BindCraft README](https://github.com/martinpacesa/BindCraft/blob/7713aa0d0d351e4117a8befeb8541f3a8ebd3368/README.md)
  requires an NVIDIA CUDA GPU and recommends substantial GPU memory. The
  MDM2 experimental paper also reports stopping generation on a memory limit.
- [BC2 installation documentation](https://github.com/PacesaLab/BindCraft2/blob/8c1a858fdc1bfc94c60846ff11a0d01c9aa44136/docs/source/installation.md)
  requires a GPU and does not offer CPU installation. Its automatic worker
  planning is not an appropriate unreviewed shared-host configuration.
- [BoltzGen's current README](https://github.com/HannesStark/boltzgen/blob/6472b44e8072187e6eaa51271ae6838245206013/README.md)
  describes a GPU pipeline and multi-gigabyte model/runtime downloads; its
  current dependencies differ from the original paper's pipeline.
- [Chai-1's README](https://github.com/chaidiscovery/chai-lab/blob/c691da74d6f348b19bc9f931abe95d66d0b88e78/README.md)
  requires a CUDA/bfloat16 GPU. Boltz documents a much slower CPU route, but
  that does not qualify it under our 2 GiB task-RAM ceiling.

No model installation, parameter download, target upload, GPU job or native
scientific execution was made. The current shared-host allowance is adequate
for this source review, not evidence that these pipelines fit it. An isolated
provider environment may be appropriate; Python 3.14 in PeptideMT does not
require rewriting every scientific engine into its own interpreter.

Code, parameter and subcomponent terms stay separate. Boltz/BoltzGen advertise
MIT code/weights. Current BoltzGen documentation names SolubleMPNN and ESMFold2
in its default pipeline; their actual artifacts, conditions and compatibility
need separate review rather than inheriting the project's MIT statement.
The inspected [BC2 license](https://github.com/PacesaLab/BindCraft2/blob/8c1a858fdc1bfc94c60846ff11a0d01c9aa44136/LICENSE)
is explicitly source-available and hosting-restricted, with separately governed
dependencies; it must not be called MIT/open-source by analogy with BindCraft.
[EvoBind's README](https://github.com/patrickbryant1/EvoBind/blob/e8f77170d65dd079f29c35cc74e5d98a453f88a2/README.md)
states CC BY-NC for its design protocol. A future bundle/use review must inspect
all actually used terms, including CNS, PyRosetta or model parameters where present.

## Recommendation for discussion and ownership

Study a small **nonexclusive** comparison rather than adopt every candidate:

- **Classical structural reference:** HADDOCK3 and/or FlexPepDock, selected for
  the actual site knowledge and sampling task.
- **Modern fixed-pair prediction:** Boltz-2 as an open candidate, with Chai-1/AF3
  as possible comparisons subject to their actual routes and terms.
- **Targeted peptide generation:** prioritize the original short-peptide
  BindCraft evidence, assess BC2 separately, and compare BoltzGen's peptide route.
  EvoBind2 and PepMLM provide useful alternatives when sequence-only input is
  scientifically relevant; RFpeptides is a future macrocycle branch.

For MDM2, review the BindCraft experimental study and its actual inputs/data
before privileging another tool merely because it is newer. Define what the
first comparison must answer: recovering fixed known poses, discriminating
binding/nonbinding peptides, ordering affinities, or selecting improved candidates.
Those objectives require different references and controls. Retain all negative
and failed outcomes, consistent source chemistry and prior exposure.

DockingMT owns reusable docking workflows and their public execution/result
contracts; a cofolding route used for pose prediction needs an agreed provider
boundary. MolSysMT owns molecular systems and transformations.
Peptide-specific generators, selection policy and scientific interpretation
remain PeptideMT responsibilities. Generic modeling infrastructure, if needed,
follows the registered owner map rather than a new local framework. A model
combining several functions does not erase these boundaries.

The existing DockingMT #33 handoff is a capability discussion, not permission
to implement HADDOCK3 or an indication that protein–peptide docking has started.
Keep T1b as a possible source/chemistry subproblem and revisit its sequence after
this alternatives discussion. Accepted T0/T1a/AMP evidence, existing source hashes
and spent runs remain unchanged. No new scientific acceptance follows.
