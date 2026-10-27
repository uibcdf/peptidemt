# Future scientific horizons and design stress tests

Status: **strategic opportunity inventory and pending questions**, 2026-10-26.
This document is not an approved roadmap, API specification, implementation commitment, benchmark result, or change to current accepted decisions.

Navigation: [index](README.md) · [vision](vision_scope.md) · [roadmap](roadmap.md) · [open questions](open_questions.md) · [decisions](decisions.md) · [working methodology](design_methodology.md).

## 1. Purpose and scope

PeptideMT aims to generate, redesign, evaluate and optimize peptides under molecular-target, functional-family, chemical and contextual objectives. The accepted problem/plan/execution separation (D09), peptide-proposal and chemical-realization semantics (D15–D16), functional-concept/resource separation (D17–D20), and domain-aware composition (D21–D24) provide a promising foundation.

Our design discussions have so far concentrated on **how** heterogeneous generators and functional predictors work together. This document complements that work by asking **which scientific questions** a powerful peptide-design platform may need to answer over the next several years. A future application is worth keeping visible without implementing it, designing a universal abstraction for it, or making it a prerequisite for the first useful release.

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

These are **test cases**, not implementation requirements or selected biological demonstrators. Document failures and counterexamples. Avoid building a full general ontology or workflow planner merely to accommodate hypothetical cases.

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

## 6. Relationship to current work

- [Vision and scope](vision_scope.md) gives the **present** working purpose. This document does not replace it.
- [Roadmap](roadmap.md) proposes **incremental deliverables**, with no implementation authorization. Horizon concepts here do not automatically become roadmap stages.
- [Functional families](functional_families.md) covers label/resource meaning; this document asks what additional functional, mechanistic and chemical objectives could matter.
- [Generative strategies](generative_strategies.md), [capabilities/composition](capabilities_and_composition.md) and [engine survey](protein_peptide_design_engines.md) examine concrete generator access. This document tests their future scientific expressivity.
- [Four worked problems](design_examples.md) establish initial stress tests; this adds **additional hypothetical stress tests**, without selecting a target.
- [Decisions](decisions.md) alone records investigator approval. No item in this file changes D09–D24 or closes P02–P09.

## 7. Next suggested design discussion (not an approval request for all horizons)

Preserve the current P09 capability/compatibility discussion. In parallel, evaluate **two or three strategically different stress tests**—one chemical modality, one multi-state/negative-target task, and one adaptive/multifidelity campaign—against the accepted semantic principles. If one truly requires a new core distinction, propose it with counterexamples; otherwise defer its concrete implementation.

**North star:** robust and extensible peptide molecular engineering, not a monolithic model zoo or a general-purpose replacement for MolSysSuite/MOLI. Keep a small trustworthy core, optional domain-qualified methods, and a path from computational hypotheses to experimental evidence.
