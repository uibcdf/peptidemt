# Future scientific horizons and design stress tests

Version: **V0.2 scientific horizon review**, 2026-10-26.
Status: **strategic opportunity inventory and pending questions**, not approved architecture.
This document is not an approved roadmap, API specification, implementation commitment, benchmark result, or change to current accepted decisions.

Navigation: [index](README.md) · [vision](vision_scope.md) · [roadmap](roadmap.md) · [open questions](open_questions.md) · [decisions](decisions.md) · [working methodology](design_methodology.md).

## 1. Purpose and scope

PeptideMT aims to generate, redesign, evaluate and optimize peptides under molecular-target, functional-family, chemical and contextual objectives. The accepted problem/plan/execution separation (D09), peptide-proposal and chemical-realization semantics (D15–D16), functional-concept/resource separation (D17–D20), and domain-aware composition (D21–D24) provide a promising foundation.

Our design discussions have so far concentrated on **how** heterogeneous generators and functional predictors work together. This document complements that work by asking **which scientific questions** a powerful peptide-design platform may need to answer over the next several years. A future application is worth keeping visible without implementing it, designing a universal abstraction for it, or making it a prerequisite for the first useful release.

The V0.2 review adds combinatorial/display libraries, peptide immunology, systemic exposure, molecular proximity/degradation, peptide transformation networks, high-throughput experimental landscapes and nontherapeutic probes/materials. These are literature-motivated directions, not new mandatory platform contracts.

For a bounded scientific differentiation and near-term implementation trajectory,
see [scientific_trajectory.md](scientific_trajectory.md). A mechanistically
grounded case of a **cell-permeating, MDM2/MDMX-directed, p53-mimetic stapled
anticancer peptide** is developed in
[case_study_cpp_anticancer_mdm2_mdmx.md](case_study_cpp_anticancer_mdm2_mdmx.md).
The [graded CPP case-guided pool](cpp_guided_projects.md) additionally
distinguishes basic sequence uptake, cargo and compartment delivery, p28
intracellular anticancer target engagement, tissue-homing iRGD, pHLIP
condition-dependent insertion, cyclic endosomal-escape peptides and stapled
binders. Their scientific boundaries are intentionally not unified into one CPP
classifier output.
Neither the pool nor either previously linked document adds a mandatory V0.1
milestone or adopts a new experimental demonstrator.

The opportunity is not primarily to compete with foundational protein generators. It is to combine their proposals with peptide-specific chemistry, rigorous molecular assessment, biological context, multiobjective search and reproducible evidence. Both target-directed and target-free problems remain in scope; experimental verification is not a prerequisite to complete a computational campaign.

**Design rule:** distinguish (a) a long-term opportunity, (b) a semantic implication worth testing before freezing a core contract, (c) a capability-specific specification that can be deferred, and (d) work approved for implementation. Entries here are primarily (a) and (b). No implementation is authorized.

## 2. Future horizons — not a fixed development sequence

The horizons describe **scientific ambition**, not dates, maturity percentages, dependency graphs or guarantees. Some advanced functionality may be prioritized earlier for a concrete project; some seemingly simple functionality may remain unsupported.

### Horizon A — trustworthy peptide discovery foundation

A practical, model-independent system capable of reproducibly expressing and comparing problems, proposals, evaluations and candidate selections.

- **Qualified multi-family search:** target-first, family-first, de novo and seed-based redesign; source-specific functional definitions and predictors; target-free requests.
- **Positive and negative design:** preferred targets, homologs and alternative sites/states to avoid; absence of an antitarget assessment is not evidence of selectivity.
- **Chemical identity and transformations:** sequences, incomplete proposals, terminal choices, stereochemistry, chemical variants and their provenance; no silent conversion from one chemistry to another.
- **Properties beyond bioactivity labels:** length, solubility, charge/pH-dependent properties, aggregation warnings, stability, toxicity, hemolysis and applicability; numerical scores are not automatically experimental measurements.
- **Multiobjective selection:** feasibility, tradeoffs, uncertainty, diversity and cost, without reducing every objective to one opaque score.
- **Reproducibility and benchmarking:** exact model/checkpoint, data/negative-label construction, domain, evaluated representation, settings, budget, failures and independent assessment.
- **Campaign usability:** inspection, comparison, export and re-evaluation of designs; researchers can interrogate *why* a candidate was selected.
- **Library-aware hypotheses:** future support for representing a combinatorial sequence space, degenerate alphabet or constrained position pattern *without materializing every member*. A library specification and a sampled individual peptide have different identities, provenance and feasibility claims.
- **High-throughput evidence:** preserve raw counts, selection rounds, replicate/library context and censoring rather than flattening screening/NGS results prematurely into an unqualified positive/negative label.

**Important boundary:** a useful first implementation need not provide every Horizon A capability. Its contracts should make known gaps explicit and should avoid preventing the other capabilities later.

### Horizon B — molecular and mechanistic peptide engineering

Capabilities that operate beyond sequence classification and single predicted complexes.

1. **Chemistry-aware modality design.** Linear and cyclic peptides, disulfide-constrained structures, stapling, D/noncanonical residues, N-methylation, terminal caps, conjugation and multivalency. Generate or redesign with a specific chemistry in scope rather than assuming one-letter sequences uniquely determine molecules. Optimize chemistry and target recognition together when models support it. Unknown chemistry remains unknown; proposed stereochemistry or ring closure is an explicit realization.

2. **Multi-state and ensemble-aware target design.** Evaluate several conformations, protonation/chemical states, complexes and binding sites. Explore state-selective ligands, allosteric binders and conformational stabilization; never assume one docked pose proves an ensemble preference. A conformational ensemble is a scientific input with provenance and weights/uncertainty, not a file list with automatic thermodynamic meaning.

3. **Selective and negative design.** Explicit positive/negative target panels, related species/homologs, mutations and off-target interfaces. Include the option to *propose* candidate antitargets from biological knowledge while requiring investigator review before treating them as requirements.

4. **Mechanism-aware design.** Distinguish binder, blocker of an interaction, enzyme inhibitor, receptor agonist/antagonist, conformational modulator and complex stabilizer. Represent a mechanism **hypothesis and supporting tests** separately from predicted affinity, structural confidence and cellular phenotype.

5. **Access, transport and spatial delivery.** Separate membrane interaction, uptake, endosomal trafficking/escape, cytosolic or organellar availability, pathogen-envelope passage and target engagement. CPP classification, PAMPA permeability and measured cytosolic delivery are distinct endpoints. Allow target/cargo and transport functions to be on one peptide or separate conjugated components.

6. **Developability and manufacturability.** Synthesizability, solid-phase synthesis difficulty, cyclization/stapling feasibility, monomer availability, yield risk, chemical and proteolytic stability, formulation, solubility, aggregation, environmental degradation and approximate cost. These can be constraints, optimization objectives or triage signals; prediction of feasibility is not laboratory proof.

7. **Multifidelity evaluation.** Sequence-level classifiers and chemical checks; structures/complexes and interaction models; ensemble/dynamics calculations; rigorous binding free-energy or kinetic estimates where validated; experimental assay evidence when available. More expensive computation is not automatically more accurate, and cheap triage can introduce false negatives.

#### Additional Horizon B opportunities highlighted in V0.2

- **Immunological epitope and antigen design.** Explore peptides in the context of antigen processing, HLA/MHC allele presentation and T-cell receptor recognition. In a TCR–pMHC task the functional target is a multi-component recognition system, not necessarily an isolated target protein; presentation, specificity and immunogenicity are separate endpoints. An [EPIC diffusion study (2026)](https://doi.org/10.1093/bioinformatics/btag358) provides a *computational* precedent for decomposing this design into coupled objectives; its predictions are not measured vaccine or T-cell responses.
- **Pharmacokinetics, ADMET and systemic exposure.** Route- and formulation-dependent bioavailability, absorption, tissue distribution, proteolytic and renal clearance, plasma binding, dose/exposure and immunogenicity can affect the utility of a therapeutic peptide. Exposure is not always an intrinsic property of the isolated candidate. A [2026 therapeutic-peptide pharmacokinetics review](https://doi.org/10.1007/s40262-025-01615-z) motivates explicit context/units/model scope, *not* a requirement to build an in-house pharmacokinetic simulator.
- **Molecular proximity and targeted degradation.** Design peptide-mediated recruitment or delivery of payloads to promote productive multi-component complexes, including peptide–degrader conjugates. The [GLP-1-guided BRD4 degrader report (2026)](https://pubmed.ncbi.nlm.nih.gov/42283322/) motivates this modality; it does not demonstrate de novo generation of such constructs or universal intracellular delivery. The desired effect may depend on complex stoichiometry, geometry, compartment and dynamics, not peptide-target affinity alone.
- **Peptide transformations and metabolites.** Represent precursor, proteolysis products, modified derivatives and active/inactive fragments with scoped conditions and (where justified) rate/abundance estimates. [ML cleavage-site work on cyclic/noncanonical peptides (2026)](https://doi.org/10.1038/s41598-026-50335-2) illustrates a possible specialized evaluator; site predictions alone do not determine fragment abundance or biological activity. This intersects with activatable constructs under Horizon C, without requiring a general reaction engine.

**Ownership:** PeptideMT states peptide-design requirements, orchestrates peptide-specific scoring/selection and preserves attribution. MolSysMT owns molecular representations/manipulations, while target geometry, docking, interaction evidence, dynamics and pharmacophores should reuse qualified existing MolSysSuite components or external engines rather than duplicating them. Any proposed free-energy or mechanism engine requires a distinct capability/domain review.

### Horizon C — adaptive and programmable discovery

8. **Closed-loop experimental learning.** Integrate measured affinity, potency, uptake, selectivity, degradation and toxicity with units, assays, cell/organism context, replicates, failed and censored measurements. Use active learning, Bayesian optimization or retraining to select informative experiments under finite budgets. Preserve training/selection leakage and distinction between model uncertainty and experimental variability. Praxis/Recorda/Nextia retain cross-tool protocol, operational and project-evidence responsibilities.

9. **Stimulus-responsive/activatable designs.** Pro-peptides, protease-cleavable masks, pH-sensitive or other triggered switches, linkers and cargo release. A design may be a related **family of chemical species and transformations over conditions/time**, not just a peptide sequence with a static family label. Activation products and their own evaluated chemistry must be explicit; predicted cleavage does not establish selective activation in vivo.

10. **Multifunctional and modular architectures.** Multiple functional sites, cell-access module + target binder, multivalent or multispecific peptides, conjugates and cargo-bearing systems. Compare a single multifunctional sequence with modular linked components; addition of a delivery moiety may change binding, uptake and toxicity.

11. **Robustness and evolutionary design.** Account for strain and patient variants, pathogen escape mutations, conservation, polymorphisms and possible resistance trajectories. Evaluate robustness across a **declared panel**, not claim universal resistance-proof activity.

12. **Functional-space atlas and inverse navigation.** Explore family-conditioned sequence/embedding spaces, learned modes, overlap, diversity, density, uncertainty, generated/known candidates, mutation paths and Pareto fronts. Enable queries such as “sample this underexplored region while preserving recognition”. Embedding plots are *model-dependent projections*, not verified contiguous functional or free-energy landscapes. MolSysViewer can visualize molecular instances; atlas visualization is a separate optional concern.

13. **Natural-peptide mining and knowledge-assisted seeding.** Search proteomes, secretomes, peptidomes, proteolytic fragments, natural-product databases and publications to propose seeds. Preserve source, organism, processing context, measurement status and license. Sequence similarity alone does not establish the same biochemical function.

14. **Mechanism/assay-aware experimental design assistance.** Propose discriminating assays and negative controls; distinguish target engagement, phenotypic response and nonspecific effects. Design decisions can identify which experimental measurements would reduce ambiguity. PeptideMT should not become a general laboratory information management system.

15. **Scientist-facing interactive exploration.** Inspect conflicting models, compare runs, audit provenance and model applicability, export synthesis/evaluation candidate sets and explore design histories. This supports human decisions rather than creating a separate, autonomous scientific agent. Generic AI-agent orchestration belongs to MOLI/MolSys-AI.

#### Additional Horizon C opportunities highlighted in V0.2

- **Computational design of experimental libraries.** Optimize a constrained *population* rather than only an individual: alphabet/position degeneracy, scaffold and motif preservation, member coverage, redundancy, anticipated display/synthesis biases, expected diversity, and sampling/selection budgets. A library might encode 10^6 or >10^12 possible members without explicitly enumerating them; this is a **representation goal**, not a claim of synthesizing or scoring that many molecules. Link the library definition to realized sequences and selection results. [Architectural design of phage-displayed libraries (2026)](https://doi.org/10.1002/bit.70370) and [mRNA/RaPID display with noncanonical residues (2026)](https://doi.org/10.1016/j.copbio.2026.103477) motivate this direction.
- **High-throughput sequence–function landscapes.** Treat deep mutational scanning, selection/enrichment, phage/mRNA display sequencing and combinatorial screening as structured evidence with library design, batch, round, read-depth, controls, replicate and assay context. Enrichment is not automatically calibrated affinity; zero counts are not measured inactivity. This can improve model training and adaptive library redesign. [NGS/phage display methods review (2026)](https://doi.org/10.1007/s00726-025-03492-z) provides a relevant operational precedent.
- **Nontherapeutic probes, imaging, diagnostics and materials.** Targeting/affinity probes, fluorescent and radiolabeled imaging constructs, biosensors, surface/mineral-binding peptides, self-assembling hydrogels and biomineralization demand objectives outside conventional therapeutic bioactivity. A [2026 review of responsive peptide imaging probes](https://doi.org/10.1002/rpm2.70064) and a [2026 self-assembly review](https://doi.org/10.1038/s12276-026-01691-6) illustrate the breadth. Device/material performance must not be relabeled as a therapeutic phenotype.

### Additional possible directions, not presently prioritized

- **Binding kinetics and residence time:** distinguish equilibrium affinity from on/off rates; require suitable methods and assay semantics before optimizing kinetic quantities.
- **Membrane and solvent environments:** lipid composition, salt, pH, serum proteins and crowding can change binding, permeability and AMP activity.
- **Stereochemical and noncanonical search:** chirality-aware mutation, residue substitutions, peptidomimetics and constrained backbones require chemistry-aware representations and qualified tools.
- **Context-selective toxicity and immunogenicity:** healthy-versus-diseased cell selectivity, immune recognition and potential adverse responses; context-specific proxies rather than one universal safety number.
- **Synthesis-aware diversification:** select chemically and structurally diverse candidates that share feasible synthesis families or building blocks, subject to verified costs.
- **Complex/cooperative recognition:** design for oligomer interfaces, transient complexes or molecular glues, with explicit stoichiometry and causal hypotheses.
- **Experimental assay design and batch effects:** compare evidence across labs/methods only with appropriate normalization and provenance; negative/unreported results matter.

These ideas are **not** a mandate to add separate packages, models, APIs or new MolSysSuite repositories.

## 3. Strategic opportunity map

| Opportunity | Scientific value | What could invalidate naive implementation? | Architectural implication to test |
| --- | --- | --- | --- |
| Modified, cyclic and stapled peptides | Expands designable chemical space, can alter preorganization/stability | Unsupported chemistry silently projected to canonical sequence; stereochemistry lost | Proposal → chemical realization → evaluated view, explicit conversions (D15–D16) |
| Multi-state, allosteric and negative-target design | Selectivity and mechanism rather than single-pose binding | Different states/sites score on noncomparable scales; ensemble weights unknown | Multiple qualified targets/states, conditional objectives and evidence |
| Cellular/pathogen delivery and conjugates | Connects predicted binding to access | Uptake confused with cytosolic exposure, conjugate inherits parent score | Target/cargo/delivery chemistry and distinct endpoint meanings |
| Synthesis and developability | Improves feasibility of candidates | Heuristic synthesizability declared measured yield or biological efficacy | Qualifiable evaluator roles, hard constraints versus uncertain predictors |
| Activatable peptides | Context-dependent behavior and selectivity | A static sequence model cannot represent precursor, trigger and products | Conditional transformations/products, temporal/contextual evaluations |
| Active learning and assay feedback | More informative iteration and use of expensive measurements | Leakage, nonrandom missing data and selection bias | Evidence lineage, assay identity, proposal policy, cost accounting |
| Robustness across variants | Better selectivity/coverage under change | A few tested variants misrepresented as universal coverage | Panels and distributions with explicit scope |
| Atlas/navigation | Scientific understanding of learned spaces and diverse discovery | Projection artifacts mistaken for real topological or thermodynamic barriers | Optional analysis/visualization, not mandatory design-core dependency |
| Combinatorial library design | Efficiently sample/design large constrained populations; link to display screens | Implicit library treated as enumerated/individually evaluated; display/NGS bias omitted | Collective design object with constraint semantics and population-level evidence |
| TCR–pMHC epitope design | Immunology and context-dependent multi-component recognition | Single-peptide affinity score interpreted as antigenicity or immunogenicity | Target/context may involve several participants and allele/assay-specific effects |
| Systemic exposure/ADMET | Translational feasibility under route and dose constraints | Sequence-only PK score presented as measured in vivo exposure | Contextual, unit-bearing model and experiment associations |
| Proximity/degradation | Productive ternary complexes, cargo recruitment and degradation | Pairwise binding interpreted as ternary cooperativity or degradation | Compositional mechanism/complex hypothesis and separate endpoints |
| Proteolytic transformation products | Predict stability and possible downstream bioactive species | Predicted cut assumed to imply exact products/rates or phenotype | Explicit precursor-to-product relationships and conditional evaluation |
| High-throughput functional evidence | Learn from mutational scans, selection rounds and large screens | Sequencing enrichment interpreted as direct affinity; negatives inferred from dropout | Population-specific assay/provenance; replicate/censoring/batch data |
| Nontherapeutic peptide engineering | Imaging, sensing, binding materials and assemblies | Therapeutic class ontology imposed on materials endpoints | Open functional concepts and property-specific evaluators (D17–D20) |

## 4. Which questions matter *before* a core architecture is considered stable?

Do **not** demand all future capabilities be specified before implementing an MVP. Instead stress-test whether current accepted semantics can represent these scenarios *without requiring a redesign of core scientific meaning*.

### Core semantic stress tests worth resolving or documenting soon

**S1 — chemical modality:** A sequence-only proposal branches into an L/D peptide, a capped derivative and a macrocycle. Which distinctions create chemical candidates, which views remain lossy, and which family scores can be reused only as limited surrogates? P07 covers the principle; chemistry/state and equivalence policies remain open.

**S2 — target ensemble and negative design:** Optimize against two conformations of one target while avoiding a homolog. How are target states and selectors named, scored and aggregated? Are alternate conformational populations known or merely speculative? Must not silently treat “binds conformer A” as “stabilizes A”.

**S3 — molecular mechanism versus phenotype:** Request both target-binding and anti-inflammatory phenotype, with one model only evaluating sequence-family compatibility. Keep the mechanistic causal hypothesis, independent evidence and unknown links separate.

**S4 — dynamic/activatable construct:** Design a masked peptide and an explicit proteolytic activation product. Does the problem refer to a precursor, products, transformation, environmental trigger and multiple contexts without forcing a static single-candidate interpretation? This may justify a future module, not a universal reaction engine now.

**S5 — multifidelity adaptive campaign:** An inexpensive family model, structural evaluator and expensive molecular simulation disagree under budget limits; later measured data arrive. How are deferred/failed evaluations, cost, selection bias and retraining versions preserved? The same candidate may receive new evidence without rewriting historical results.

**S6 — multimodal conjugate:** Compare free binder, CPP–binder fusion and linker-cleaved delivery. Are these distinct chemical candidates related by a design hypothesis, with assays on labeled variants correctly attributed?

**S7 — evolutionary robustness:** A peptide targets several pathogen variants and avoids a human homolog; what is a panel-scoped claim and what remains untested?

**S8 — target-free peptide and functional atlas:** Sample novel CPP+AMP candidates with no protein target. How can an embedding exploration guide search without being treated as true calibrated functional density?

**S9 — combinatorial library without enumeration:** Define a constrained library (for example, 10^6 theoretical variants with fixed motifs and position degeneracy), sample a few designs, and attach phage/mRNA display or NGS selection data. Is the library a collective proposal with its own provenance and coverage, distinct from realized members? Can a model score sampled members without pretending to have evaluated the whole library?

**S10 — TCR–peptide–MHC recognition:** Design an epitope with a specific HLA allele and receptor context. Does the scientific problem express presentation, TCR engagement and immunogenicity as distinct properties of an interacting multi-component system? Must not reduce the objective to one pairwise affinity or assume immunogenicity from a pMHC pose.

**S11 — transformation and degradant network:** Represent a parent pro-peptide, a cleaved active product and a potentially toxic secondary fragment under protease/pH conditions. Can each species receive distinct evidence and estimated formation propensities without equating a cleavage-site prediction to a measured product distribution?

**S12 — exposure-constrained design:** Select a target-binding candidate under a therapeutic route and exposure requirement (e.g., half-life/clearance in a stated species). Can we keep molecular properties separate from model-specific dose, formulation and physiology assumptions? A missing PK model must not silently become a negative design score.

These are **test cases**, not implementation requirements or selected biological demonstrators. Document failures and counterexamples. Avoid building a full general ontology or workflow planner merely to accommodate hypothetical cases.

### Architectural impact versus development commitment (V0.2 triage)

| Opportunity | New scientific meaning or new evaluation domain? | Early *semantic* stress test? | Implementation can wait? | Current owner/likely extension boundary |
| --- | --- | --- | --- | --- |
| Combinatorial/display library | Collective/distributional design versus chemical individual | **Yes — S9** | **Yes** | PeptideMT library-design meaning; Praxis/experimental systems own protocols |
| TCR–pMHC immunological epitope | Context-dependent multi-component recognition and endpoints | **Yes — S10** | **Yes** | PeptideMT problem/selection; structural tools handle qualified complexes |
| PK/ADMET and exposure | Contextual dose/route/species-dependent properties | Useful — S12 | **Yes** | External PK/ADMET evaluators; avoid a PeptideMT physiologic simulator |
| Molecular proximity / induced degradation | Multi-component mechanism and cargo species | Useful with S3/S6 | **Yes** | Molecular-system evaluation and mechanism-specific optional tools |
| Degradants and activation products | Parent-to-product chemical transformation, multiple effects | **Yes — S11** | **Yes** | MolSysMT handles molecular identity; PeptideMT keeps design relations |
| High-throughput/DMS/display selections | Population- and round-specific evidence | Useful with S5/S9 | **Yes** | Experiment source data and PeptideMT evaluated population/provenance |
| Imaging/sensors/materials | Nontherapeutic function semantics and application-specific endpoints | Can defer | **Yes** | Functional catalog plus optional specialized evaluators |

"Yes" means worth **checking for a conceptual contradiction before finalizing a core contract**, not an implementation gate or a requirement to build its evaluation method. If no new core distinction is needed, leave the capability to its eventual specialist adapter.

### Decisions to settle before a *particular capability* is implemented

- Scientific input/output meaning, evaluated representation and acceptable missing chemistry.
- Engine/evaluator operations actually exposed, their conditional support and scientific applicability (P09).
- Selection policy under missing, contradictory and out-of-domain evidence; hard constraint versus surrogate score (P04).
- Explicit responsibility with MolSysMT, other MolSysSuite components and Praxis/Recorda/Nextia.
- Minimum reproducibility, error/abstention semantics and scientifically meaningful acceptance tests.
- Compatibility, version, license and operational deployment of the specific integrated engine.
- If an advanced modality is in scope for that capability: its chemistry, state and transformation contracts.

### Explicitly deferrable beyond the first useful implementations

- Universal support for all peptide modifications, all reaction-triggered designs or all biochemical assays.
- Universal differentiable guidance or one sampler interface that exposes every model's internals.
- A fully populated family ontology, automatic mechanistic inference or a general planning engine.
- Automated selection of off-targets, fully autonomous experiments, a universal uncertainty measure.
- One implementation of every proposed future-horizon idea.

## 5. Evaluation philosophy that should influence the core

1. **Search quality is not identical to reward optimization.** Compare to independent computational evaluators or experiments where available; report data overlap and model-specific bias.
2. **Better structure/confidence is not binding free energy or function.** Promote physically meaningful claims only with applicable evidence; separate equilibrium affinity, kinetics, conformational populations and functional effects.
3. **Multiobjective before a single universal fitness.** Preserve raw objectives, direction, hard feasibility, applicability, uncertainty, novelty, diversity and evaluation budget. Scalarization is a documented policy, not the scientific truth.
4. **No universal ladder of “higher fidelity = higher accuracy”.** Expensive simulations and complex predictors also have domain limits and uncertainty.
5. **No unsupported chemical inheritance.** A sequence-family score may inform a chemically modified derivative, but attribution is conditional and visible.
6. **Separate execution completion from scientific sufficiency.** Empty or limited evidence is still an honest result.
7. **Make negative knowledge useful.** Preserve failed designs, negative measurements, dead ends and contradictory predictions; their provenance improves both benchmarking and later active learning.
8. **Prefer modular extension over ownership creep.** PeptideMT owns peptide-specific design semantics and composition; MolSysMT owns molecule handling; specialist methods and platform-wide orchestration remain with appropriate tools.

## 6. Selected scientific anchors (not an exhaustive evidence review)

These sources motivate future directions and test cases. None establishes performance of PeptideMT, a selected implementation, or a validated universal predictor:

- **Display and library architecture:** [Ling, Peng & Lim, *Biotechnology and Bioengineering* (2026)](https://doi.org/10.1002/bit.70370), overview of linear-to-multicyclic phage-displayed libraries; [Bakhshinejad & Kjaer, *Amino Acids* (2026)](https://doi.org/10.1007/s00726-025-03492-z), NGS-aware phage-display workflows; [mRNA/RaPID display and chemical diversification (2026)](https://doi.org/10.1016/j.copbio.2026.103477).
- **Immunological peptide design:** [Huang et al., EPIC, *Bioinformatics* (2026)](https://doi.org/10.1093/bioinformatics/btag358), computational TCR–pMHC epitope design with multiple objectives.
- **Systemic pharmacokinetics:** [Nordell et al., *Clinical Pharmacokinetics* (2026)](https://doi.org/10.1007/s40262-025-01615-z), peptide disposition and size-/mechanism-related scaling limitations.
- **Targeted proximity/degradation:** [Multicomponent stapled GLP-1-guided degrader (2026)](https://pubmed.ncbi.nlm.nih.gov/42283322/), experimental receptor-guided conjugate example; not a generic peptide-design model.
- **Proteolysis and chemical modalities:** [Cifuentes et al., *Scientific Reports* (2026)](https://doi.org/10.1038/s41598-026-50335-2), model-based prediction of cleavage sites in cyclic and noncanonical peptides.
- **Nontherapeutic and responsive systems:** [Responsive peptide fluorescent probes (2026)](https://doi.org/10.1002/rpm2.70064); [biomimetic peptide self-assembly (2026)](https://doi.org/10.1038/s12276-026-01691-6).

No claim here that model weights, databases, displayed libraries or commercial use are available under compatible licenses. These require separate qualification.

## 7. Relationship to current work

- [Vision and scope](vision_scope.md) gives the **present** working purpose. This document does not replace it.
- [Roadmap](roadmap.md) proposes **incremental deliverables**, with no implementation authorization. Horizon concepts here do not automatically become roadmap stages.
- [Functional families](functional_families.md) covers label/resource meaning; this document asks what additional functional, mechanistic and chemical objectives could matter.
- [Generative strategies](generative_strategies.md), [capabilities/composition](capabilities_and_composition.md) and [engine survey](protein_peptide_design_engines.md) examine concrete generator access. This document tests their future scientific expressivity.
- [Four worked problems](design_examples.md) establish initial stress tests; this adds **additional hypothetical stress tests**, without selecting a target.
- [Decisions](decisions.md) alone records investigator approval. The inventory does not change accepted decisions or close proposals. Subsequent explicit approval closes P09 conceptually under D25–D26; the bounded analysis below adopts no additional architecture.

## 8. Next suggested design discussion (not an approval request for all horizons)

P09's capability/compatibility organization is now accepted conceptually. The bounded review below addresses the investigators' selected library, multi-state/antitarget and precursor/product cases before returning to P04. S9–S12 do not require running all tests before a useful first release. If one truly requires a new core distinction, propose it with counterexamples; otherwise defer its concrete implementation.

**North star:** robust and extensible peptide molecular engineering, not a monolithic model zoo or a general-purpose replacement for MolSysSuite/MOLI. Keep a small trustworthy core, optional domain-qualified methods, and a path from computational hypotheses to experimental evidence.

## 9. Bounded extensibility review after P09 approval

Date: **2026-10-26**. Basis: investigators' V0.2 at repository revision
[`e28fbd3`](https://github.com/uibcdf/peptidemt/tree/e28fbd3), read before this update.
Status: **conceptual analysis and limited recommendations**, not new accepted
features. P09 is resolved under D25–D26; the observations here do not reopen it.
No models were executed and the horizon literature inventory was not re-audited.

| Selected scenario | Are current decisions enough? | Real boundary / proposed response | What can wait? |
| --- | --- | --- | --- |
| A. Implicit combinatorial libraries (S9) | D09 and P09 support problem/plan/evidence and optional providers, but P07 does not explicitly distinguish a collective design intention from an incomplete individual. | Propose that distinction as P10 before promising library design. Do not redefine a molecular realization as a library member or adopt a universal population hierarchy. | Library syntax, distribution representation, counting, samplers, display models and library-level optimizers; all are outside the present MVP commitment. |
| B. Positive/negative target states (S2) | Yes for conceptual separation and attribution; no implemented target-panel or ensemble API is claimed. | Preserve state/context-specific evaluations and explicit positive/negative requirements; defer aggregation and selection policies to P04. No new top-level architecture is needed. | State naming/grouping, ensemble weights, free-energy methods, exchange kinetics and specialist adapters. |
| C. Precursors and transformation products (S4/S11) | P07 supports distinct molecular subjects, realizations, views and provenance; it is not already a reaction/process model. | Use explicit precursor-to-product relationships with their meaning and evidence when this capability is specified. Transformation is neither chemical completion nor mere conversion. No general reaction graph is justified now. | Reaction representation, product enumeration, kinetics, mixtures, activation models and transformation-specific contracts. |

### A. A library is an intention about a population

An individual incomplete proposal says that some information about an intended
molecular design remains unresolved. A combinatorial library deliberately spans
many members. A finite computational batch is yet another thing: it is a sample
or work allocation, not necessarily the scientific library being designed.
Treating all three as 'a sequence with unknown positions' loses their meanings.

**What can already be expressed conceptually:** the problem requests a library
with variable positions, preserved motifs and global restrictions; the plan
chooses how to represent/sample/evaluate it; execution records samples and the
evidence actually obtained. P09 permits an optional provider with such outputs.
Neither D09 nor P09 requires enumerating all possible molecules.

**Actual gap:** P07's individual proposal/realization semantics do not by
themselves establish library membership or population-level claims. The minimal
pending distinction is a collective/distributional proposal versus an individual
molecular proposal. Membership/sampling relates them; chemical completion still
relates an incomplete individual to its realizations. A sampled member can itself
need chemical realization. These relations must not be collapsed.

A support definition and a sampling distribution also differ: the same allowed
members can be sampled with different probabilities. Position choices alone need
not determine a joint distribution after global constraints or correlations.
The intended library, a computational sampling law and a physically realized
screening population can differ. Evidence from a few evaluated members does not
become evidence about every member. Coverage, counts and aggregate estimates
retain whether they are exact, inferred, sampled or unknown.

**Recommendation, pending P10:** preserve this distinction when a library
capability is designed. Do not now extend every candidate type, require a measure
calculus, define identifiers or install a population engine. A first individual-
peptide implementation can explicitly lack library support without prejudicing
future extensibility. This finding does not block the next P04 discussion.

### B. States and antitargets fit without a new core entity taxonomy

The scientific problem can favor recognition of specified states of a protein
and disfavor another state or another molecule. It must distinguish requiring all
favored states from permitting any one of them. The plan selects representations,
evaluators and an explicit comparison policy; execution retains each candidate,
target/state/site, context, model/input and result, including missing evaluations.
These are uses of D09, P07 and P09, not a new mandatory sequence of stages.

**Semantic guardrails:** a conformation, a chemical/protonation state, a different
target and a sampler state are not interchangeable. Preserve their relationships
without deciding canonical identity/grouping here. Structural instances and their
weights have source/assumption scope; a list of conformers is not automatically an
equilibrium ensemble. Averaging confidence or docking scores is not automatically
a thermodynamic or state-selectivity estimate. Stabilization of a state is a
stronger mechanistic claim than a favorable predicted complex in that state.

The problem's positive/negative intent must survive the plan's aggregation. Do
not compare unrelated predictor scales as if they were common affinity units,
or infer selectivity because no antitarget evaluation exists. Whether to seek
worst-case performance, use justified weights or retain separate objectives is
part of the specific problem/plan and pending P04, not a universal default.

**Conclusion:** no contradiction in the accepted organization. A state-panel or
ensemble capability needs later input/evaluation contracts and domain-qualified
methods; those are extensions, not grounds to build an ensemble engine now.

### C. Transformation products are separate evaluation subjects

A precursor and its activation/degradation products may have different chemistry,
recognition and functional effects. Each can have incomplete proposals, explicit
realizations and evaluated views under P07. The problem can request properties of
the precursor and of particular products in stated contexts; the plan selects
how to propose products and assess them; execution preserves the actual species,
assumptions, transformations, predictions and observations.

**P07 is necessary but does not supply transformation meaning automatically.**
Completing an unresolved terminus, converting a representation, computationally
redesigning a peptide and proposing a biological cleavage have different meanings.
A future specialized relation should identify source/product participants and
the transformation hypothesis/context, preserving whether evidence is predicted,
assumed or observed. It need not be a universal reaction object or a kinetic model.

Products must not be silently grouped as conformations or chemical states of one
unchanged molecular subject. The audited MolSysMT
[ChemicalStates](https://github.com/uibcdf/molsysmt/blob/e395e52646dab2ecb480d3d67aa7254be99b8524/molsysmt/native/chemical_states.py)
uses a stable atom-index domain; changing atom inventories does not automatically
fit that representation. Keep supported molecular operations with MolSysMT and
design-specific transformation attribution with PeptideMT.

A predicted cleavage site does not establish product abundance, formation rate
or functional activity. An assay on a mixture is not automatically attributable
to one fragment. A precursor's score cannot be transferred to its products
without justification, and several precursor paths can reach the same product
without losing provenance. Missing chemical details remain unresolved or enter
explicit hypothetical realizations, rather than being filled retrospectively.

**Conclusion:** distinct subjects and explicit, evidence-qualified relations are
sufficient at this level. Specify the transformation relation when needed; no
new top-level architecture or compulsory reaction/activation engine is warranted.
Time, stoichiometry, product distributions and kinetic equations can wait unless
a particular future claim depends on them.

### Disposition and return to the operational core

Only A exposes a new collective-versus-individual distinction worth proposing
separately. B and C require disciplined use and later extension of existing
semantics, not a redesign of problem/plan/evidence or capability composition.
None of these findings is implementation approval or an MVP prerequisite.
Canonical identity, initial chemistry support and the other P07 deferrals remain
open. P10 remains pending; no additional proposal hierarchy is introduced.

Return now to [P04's proposed discussion sequence](open_questions.md#p04-proposed-discussion-sequence):
evaluation meaning and constraints/evidence first, then objective tradeoffs,
uncertainty, diversity and budgeted selection. The horizons provide counterexamples
when useful; they do not expand the initial evaluation layer into every future
domain or require resolving S1–S12 before proceeding.
