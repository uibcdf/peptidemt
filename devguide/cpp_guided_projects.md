# CPP-guided scientific projects: a representative progression from simple entry to targeted functional peptides

Date: **2026-10-27**. Status: **literature-anchored reference cases and a proposed future case-guided development ladder**, not selected V0.1 demonstrators, accepted scientific models or implementation authorization. The pool complements the four original conceptual design cases and the detailed [ATSP-7041 MDM2/MDMX case](case_study_cpp_anticancer_mdm2_mdmx.md). It deliberately covers distinct **biological endpoints, chemical representations, sources of cell selectivity and delivery mechanisms**, rather than treating every cell-penetrating peptide as a target-binding anticancer agent.

Navigation: [index](README.md) · [worked cases](design_examples.md) · [original scientific goal and trajectory](scientific_trajectory.md) · [functional semantics](functional_families.md) · [future horizons](future_horizons.md) · [V0.1 scope](v0_1_scope.md).

## 1. How to use this pool

These are **projects that can guide future scientific capability increments**. They are not executable PeptideMT benchmarks yet. Before commissioning one, select a scientifically permitted concrete molecule, cell/assay context, target/cargo (where relevant), resource/checkpoint and actual chemistry. Specify what constitutes a computational result versus literature reproduction and what remains unassessed. A candidate can retain a favorable score, contradictory models or missing CPP evidence without being assigned experimental uptake.

**Definitions that must not collapse:**

1. Peptide association with a membrane; cellular uptake; endosomal internalization; endosomal escape; effective cytosolic/nuclear delivery; penetration through tumor tissue; delivery of an attached or coadministered **cargo**; and a biologically effective intracellular target engagement are **distinct endpoints**.
2. Intrinsic CPP-like permeability, cargo-carrier CPP function, cancer-cell preference, receptor-mediated homing, pH-responsive membrane insertion and peptide-intrinsic anticancer action are **distinct scientific design intentions**. A broader delivery peptide need not be positive on a generic CPP dataset.
3. A peptide, a fluorescently labeled analogue, a dimer, a conjugate, a drug-loaded particle, a proteolytic product and a hydrocarbon-stapled peptide are potentially **different chemical subjects**. Never transfer assay evidence or model predictions silently between them.
4. Affinity to a cell-surface receptor can provide **localization/uptake**, not automatically binding to the desired **intracellular therapeutic target**. A p53 pathway phenotype requires more evidence than docking or a classifier output.
5. CPP predictors based on canonical linear sequences do **not** inherit qualification for cyclic, stapled, D-residue, protected-terminal or conjugated chemistry. An allowed canonical sequence projection is an explicitly limited surrogate; it is not an observation on the full species.
6. Published uptake and anticancer findings apply to the specific experimental systems described in the primary papers; they are **not** new PeptideMT outcomes or clinical efficacy guarantees.

**Priority/complexity levels:** L1 = simple sequence and endpoint distinctions; L2 = peptide/cargo, membrane trafficking and context; L3 = cell selectivity, molecular target and multifaceted phenotype; L4 = cyclic/stapled/conditional chemistry. These represent **scientific teaching and qualification difficulty**, not release phases, dates or mandatory execution order. The true implementation difficulty can differ substantially with the available engines.

## 2. Coverage matrix: twelve complementary project-guide cases

| ID | Case and research question | Predominant CPP/delivery mode | Conceptual difficulty | Scientific capability it would exercise |
| --- | --- | --- | --- | --- |
| **CPP-01** | Polyarginine R8/R9: what does a simple composition/length change establish? | Linear cationic, no target or cargo obligatory | L1 | Reference sequences, variants, source-specific CPP prediction, sequence selection without false assay claims |
| **CPP-02** | Penetratin versus arginine-rich peptides: can composition/helix/context differences be assessed? | Linear amphipathic homeodomain-derived CPP | L1 | Family heterogeneity, structural/biophysical descriptors with appropriate input scope |
| **CPP-03** | TAT-mediated delivery: distinguish free carrier from a **cargo conjugate/fusion** | CPP used for protein cargo delivery | L2 | Explicit peptide–cargo and experimental subject identity, method/endpoint binding |
| **CPP-04** | dfTAT: why is **endosomal escape** different from total uptake? | Tagged/dimeric CPP, endosomolytic cargo delivery | L2 | Separate uptake/escape/cytosolic-delivery evidence and chemistry/label attribution |
| **CPP-05** | p28 (azurin-derived): can cancer-cell preference and **p53 engagement** be considered jointly? | Intrinsically cell-penetrating, nonclassically cationic, anticancer peptide | L3 | Cancer/normal cell context, explicit intracellular target, p53 pathway and ACP phenotype |
| **CPP-06** | iRGD: can receptor binding, proteolysis and **tumor tissue penetration** be composed without conflation? | Tumor-homing RGD → CendR/NRP1 process | L3 | Multi-target/state and proteolytic-product roles; cargo/tissue delivery separate from generic CPP |
| **CPP-07** | pHLIP: how does **extracellular pH** regulate membrane insertion and delivery? | pH-activated transmembrane insertion, conditional delivery | L3–L4 | State/context-dependent design and protonation/chemical-context limitations |
| **CPP-08** | cFΦR4 and CPP12: can a constrained peptide deliver cargo to the **cytosol**? | Cyclic CPP with noncanonical/stereochemical features | L4 | Explicit cyclic chemistry, cargo topology, endosomal escape and stability; no sequence-only shortcuts |
| **CPP-09** | ATSP-7041: combine **intracellular target engagement** and anticancer effect | Cell-permeating hydrocarbon-stapled p53 mimetic | L4 | MDM2/MDMX target recognition, modified chemistry, TP53 context and evidence/claim separation |
| **CPP-10** | CPP + AMP multifunctional design: does joint guided search differ from **generate then filter**? | Target-free, joint bioactivity prediction/generative design | L2→L3 | True multi-label guidance, rewards versus evaluation, matched-budget controls and negative-function evidence |
| **CPP-11** | PepFect14: can CPPs deliver functional **oligonucleotides** in nanocomplexes? | Amphipathic/lipidated CPP and noncovalent SCO cargo | L3–L4 | Formulation identity and gene-function readout, not peptide score alone |
| **CPP-12** | Activatable CPPs: can local proteolysis **unmask** uptake? | Polycation–cleavable linker–polyanion peptide | L3–L4 | Separate cleavage precursor/product, trigger context and conditional access |

**Boundary cases matter:** CPP-06 is largely **tumor-homing and tissue/cellular penetration**, not a generic proof of cytosolic access. CPP-07 is **pH-driven membrane insertion** rather than a classic cationic CPP. CPP-09 may be cell-permeable without belonging to the supported domain of a standard CPP sequence classifier. Their inclusion deliberately prevents PeptideMT from equating all delivery phenomena to one class label.

## 3. Project briefs with literature anchors and minimum credible outcomes

### CPP-01 — Polyarginine R8/R9: a first sequence-level reference

**Problem:** investigate canonical arginine-rich short-peptide proposals with defined lengths and comparator sequences, without demanding any molecular protein target or anticancer effect.

**Published anchor:** [Futaki et al. (2001), arginine-rich membrane-permeable peptide carriers](https://pubmed.ncbi.nlm.nih.gov/11084031/). [Suzuki et al. (2002), internalization mechanisms](https://pubmed.ncbi.nlm.nih.gov/11711547/) is a related primary reference.

**Future PeptideMT exercise:** enter R8/R9 reference strings and composition/length-controlled variants; preserve source, any terminal chemistry that is actually known, model's input alphabet and original label. Compare an initial CPP predictor with a sequence-only selection policy **only after a real qualified CPP evaluator exists**. A procedural Arg-count score is a descriptor or heuristic, never ground truth CPP probability.

**Evidence/controls:** native outputs, model domain (including training length), length/composition controls, missing data, reuse and unassessed uptake. **Does not establish:** endosomal escape, concentration-dependent viability, cargo delivery, cytosolic entry or cancer selectivity.

### CPP-02 — Penetratin: structurally/compositionally different canonical CPP

**Problem:** compare a homeodomain-derived amphipathic CPP (penetratin) with highly basic references, specifying biological context. The scientific goal is not to decree which peptide is universally better.

**Published anchor:** [Derossi et al. (1994), Antennapedia third helix translocation](https://pubmed.ncbi.nlm.nih.gov/8144628/); [Derossi et al. (1996), cell internalization analysis](https://www.jbc.org/article/S0021-9258%2819%2987040-0/fulltext).

**Future PeptideMT exercise:** retain the source sequence/fragment and any experimental tag/cargo identity; compare justified sequence descriptions, optional helix-compatible views and differently trained CPP resources. Do **not** infer entry mechanism merely from an amphipathic helix or charge. Treat predictions across different cell types and assays as context-sensitive.

**Control:** direct R8 comparison under identical computational input/support conditions; no invented cellular uptake measurements.

### CPP-03 — TAT: carrying another active molecule is a different design object

**Problem:** design or assess a CPP-carrier/cargo construct, not just the isolated carrier, and explicitly distinguish peptide alone from protein/peptide cargo fusion or conjugate.

**Published anchor:** [Schwarze et al. (1999), intracellular delivery of biologically active protein via TAT](https://pubmed.ncbi.nlm.nih.gov/10477521/). This is a primary precedent for cargo delivery; its full methodology and target context must be pinned before reproducing any quantitative finding.

**Future PeptideMT exercise:** compare the reference carrier as a **sequence view**, then a declared conjugate/fusion or other applicable carrier–cargo arrangement as an **independent molecular proposal**. Retain linker/attachment/cargo identity and any observable transport evaluation. The availability of a CPP score on TAT alone does not establish intracellular cargo release or preserved cargo biological function.

**Boundary:** protein-cargo preparation and modified chemistry may require MolSysMT or a future specialized relation; no unconditional fusion generator or delivery predictor is required for V0.1.

### CPP-04 — dfTAT: uptake ≠ escape from endosomes

**Problem:** distinguish internalization from productive cytosolic cargo delivery in a model where endosomal escape is experimentally reported.

**Published anchor:** [Erazo-Oliveras et al. (2014), dfTAT-assisted cytosolic protein delivery](https://pubmed.ncbi.nlm.nih.gov/24930129/). The tested agent includes a dye-labeled TAT-derived **dimer** and is not identical to unmodified monomeric TAT.

**Future PeptideMT exercise:** retain native dimer/label/cargo chemistry; track cell uptake, endosomal sequestration, endosomal escape and cytosolic functional readout as distinct evidence endpoints. Compare with CPP-03 to expose why a sequence classifier cannot tell an endosomolytic reagent from any other positive CPP.

**Interpretation gate:** membrane disruption, viability and cargo function require their own evidence; more uptake is not necessarily better functional delivery.

### CPP-05 — p28: a relatively straightforward target-associated anticancer CPP

**Problem:** design/redesign a relatively small azurin-derived peptide with preferential uptake in tested cancer cells and a **p53-related intracellular mechanism**. This is the recommended early **target + function scientific reference** because it does not *intrinsically* require a hydrocarbon staple like CPP-09.

**Primary evidence:** [Yamada et al. (2009), p28 preferential entry and p53-mediated cell-cycle arrest in breast cancer lines](https://pubmed.ncbi.nlm.nih.gov/19808975/); [p18/p28 comparison and preferential cancer-cell entry (2009)](https://pubmed.ncbi.nlm.nih.gov/19147567/). A [phase-I clinical report (2013)](https://pubmed.ncbi.nlm.nih.gov/23449360/) concerns the historical p28 molecule, not our prospective designed analogues.

**Future PeptideMT exercise:** start from the documented azurin residues **50–77** as p28 and **50–67** as the smaller uptake-oriented p18 fragment; obtain exact sequences and termini from an explicitly pinned original source (no automatic sequence guess here). Build a declared redesign problem focused on **p53 interaction**, cancer/normal cell uptake preference and antiproliferative context. Compare possible mutations or supported generative proposals to pinned reference hypotheses, separately assessing p53 binding, cell access and anticancer phenotype.

**Essential distinction:** evidence in those studies supports p28–p53 interaction; **do not substitute MDM2 as the direct peptide target or treat p28 as equivalent to the MDM2/MDMX stapled inhibitor ATSP-7041**. Cancer preference is contextual, not demonstrated universal selectivity. A generic ACP score is not evidence of the p53 mechanism.

### CPP-06 — iRGD: receptor-guided tumor localization and proteolytic activation

**Problem:** design a tissue-penetrating peptide whose operation involves sequential biological contexts: integrin-mediated tumor homing, proteolytic exposure of a CendR motif, and NRP1-dependent tissue transport.

**Primary evidence:** [Sugahara et al. (2009), iRGD tumor tissue penetration and cargo delivery](https://doi.org/10.1016/j.ccr.2009.10.013); [de novo tumor-penetrating peptide mechanistic/design follow-up (2013)](https://pubmed.ncbi.nlm.nih.gov/23151901/).

**Future PeptideMT exercise:** represent an intact iRGD chemical subject; explicit target roles for αv integrins and neuropilin-1; separate proteolytically processed product, exposed terminus and CendR recognition condition; record attached versus coadministered cargo. A plan may assess each event separately before claiming their conditional sequence.

**Failure mode:** a predicted RGD–integrin contact does not guarantee cleavage, NRP1 interaction, tissue penetration, intracellular delivery or anticancer drug efficacy. This is not an ordinary canonical-linear CPP design problem; ring closure, chemical presentation and cleavage context matter.

### CPP-07 — pHLIP: pH-responsive insertion as a neighboring delivery paradigm

**Problem:** condition membrane insertion/delivery on acidic versus near-neutral extracellular pH, with distinct protonation and membrane environments.

**Primary evidence:** [Reshetnyak et al. (2006), pH-dependent membrane insertion and cargo translocation](https://pubmed.ncbi.nlm.nih.gov/16608910/); [Reshetnyak et al. (2007), membrane-associated states](https://pubmed.ncbi.nlm.nih.gov/17557792/).

**Future PeptideMT exercise:** compare supported peptide variants and state-specific membrane/protonation hypotheses. Retain peptide, cargo, linkage and activation conditions separately; report which physical quantities are from qualified estimators versus unsupported guesses. Where methods are absent, record explicit pending context evaluations.

**Boundary:** pHLIP is not a generic positively charged CPP, nor does a pH-dependent bilayer insertion automatically establish cytosolic delivery of an arbitrary cargo. No membrane simulation is required in current V0.1.

### CPP-08 — cFΦR4 / CPP12: cyclic, noncanonical and effective cytosolic delivery

**Problem:** investigate cell entry and efficient endosomal escape for cyclic CPPs and their cargo, explicitly including chirality and noncanonical residues.

**Primary evidence:** [Qian et al. (2014), cFΦR4, endosomal escape and delivery](https://pubmed.ncbi.nlm.nih.gov/24896852/); [CPP12/CPP12-2 chemistry and lower-concentration/serum effects (2022)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9175492/).

**Future PeptideMT exercise:** record actual macrocyclic topology and noncanonical hydrophobic building blocks, including the CPP12 series' stereochemistry. Compare published chemical candidates and carefully qualified chemical modifications under a fixed delivery endpoint and serum/concentration context. The CPP12-2 published advantage is measured only for its stated systems.

**Failure mode:** converting `cyclo(FΦRRRRQ)` or CPP12 into a flat 20-residue-alphabet string loses real chemical meaning. A label inferred for that projection does not establish permeability of the original macrocycle. Distinguish cytosolic function from general uptake, and distinguish CPP12 from cFΦR4 as chemically separate reference peptides.

### CPP-09 — ATSP-7041: stapled peptide that binds an intracellular anticancer target

**Problem:** design a chemically stapled, cell-permeating p53-mimetic peptide recognizing MDM2/MDMX, with TP53-contextual anticancer phenotype.

**Full case, sources and future verification exercise:** [dedicated MDM2/MDMX project](case_study_cpp_anticancer_mdm2_mdmx.md), including ATSP-7041 published studies and [PDB 4N5T](https://www.rcsb.org/structure/4N5T). Unlike p28, this mimetic **binds p53 regulators (MDM2/MDMX), not p53 as its presumed primary molecular binding target**. 4N5T's receptor is a modified *Danio rerio* MDMX construct and needs explicit mapping before claims about human MDMX.

**Future PeptideMT exercise:** E0–E7 reference, chemistry, target/access/phenotype attribution, then qualified redesign/generation and comparison of search paths. The hydrocarbon staple and noncanonical stereochemistry must be chemically modeled, not stripped.

**Gate:** relatively advanced and **deliberately not** the first target/CPP project; it must not become an obstacle to implementing a simpler p28 or sequence-based CPP study.

### CPP-10 — CPP + AMP multi-function search without a protein target

**Problem:** study whether learned functional guidance can improve proposals jointly oriented to CPP-compatible access and AMP-compatibility, with hemolysis treated as a separate potentially adverse property. The same peptide may have multiple objectives; no protein target is needed.

**Conceptual reference:** [the existing target-free Case D](design_examples.md#5-case-d--cpp--amp-without-an-explicit-molecular-target) and [PrMFTP multi-label precedent](https://doi.org/10.1371/journal.pcbi.1010511); generation may require a separately qualified route. This is a **hypothesis-testing design case**, not a published proof of a specific jointly functional peptide.

**Future PeptideMT exercise:** evaluate a supplied pool with qualified CPP/AMP resources; introduce a real proposal/redesign operation; compare generate–then–filter with feedback that actually affects later proposals under declared budgets. Retain all native labels, negatives, shared biases and uncertainty. **Macrel alone provides AMP/hemolysis, not CPP.** HydrAMP alone does not supply externally controllable arbitrary CPP conditioning.

**Gate:** reward improvement and high multi-label scores are not independent biological validation. A CPP-like classifier trained on unrelated cell types need not be meaningful for the selected context.

### CPP-11 — PepFect14: oligonucleotide delivery through a nanocomplex

**Problem:** distinguish a CPP acting as an intrinsic bioactive molecule from a **carrier formulation** that delivers a splice-correcting oligonucleotide (SCO). Biological success is **splice correction**, not simply peptide uptake.

**Primary evidence:** [Ezzat et al. (2011), PepFect14 (PF14) and SCO delivery](https://pubmed.ncbi.nlm.nih.gov/21345932/); [Ezzat et al. (2012), scavenger-receptor uptake of CPP–oligonucleotide complexes](https://pubmed.ncbi.nlm.nih.gov/22138034/).

**Future PeptideMT exercise:** preserve the lipidated/amphipathic CPP, its nucleic-acid cargo and the **noncovalent nanocomplex** as distinct participants. Consider declared formulation, ratio and serum context; separate internalization, endosomal escape and functional splice-correction evidence. A peptide predictor alone cannot qualify a nanocomplex or restore an oligonucleotide's biological function. A specialized molecular/material representation may be needed later.

**Limits:** cargo complexation, size and charge depend on formulation, not only on the CPP sequence. This complements TAT protein cargo with **nucleic-acid cargo** and does not expand V0.1.

### CPP-12 — Activatable CPPs (ACPPs): proteolytic unmasking near tumors

**Problem:** conditionally enable polyarginine-associated uptake by removing a negatively charged inhibitory segment through cleavage of a linker in a specific protease context.

**Primary evidence:** [Jiang et al. (2004), tumor imaging by proteolytic CPP activation](https://pubmed.ncbi.nlm.nih.gov/15601762/).

**Future PeptideMT exercise:** preserve the masked precursor, its cleavage hypothesis, the released CPP and other products as **distinct molecular subjects**. Specify applicable protease context, any cargo, cell association/uptake and imaging readout. Compare intact and processed species without transferring scores or asserting tumor selectivity from a cleavage predictor alone.

**Limits:** ACPP activation differs from iRGD: iRGD cleavage exposes a CendR motif for neuropilin-mediated penetration, whereas ACPP cleavage removes an inhibitory polyanion. Neither mechanism automatically proves cytosolic delivery or anticancer drug activity.

## 4. A minimal common case-study contract before implementation

A selected CPP guided project should be described with **scientific meaning first**, not an arbitrary shared Python interface:

| Element | Questions to settle |
| --- | --- |
| Biological endpoint | Uptake, cytosolic access, tissue penetration, protein/cargo delivery, tumor selectivity or phenotype? State precisely. |
| Molecular entity | What is the peptide versus cargo, tag, conjugate, modified derivative, cyclic species or cleavage product? |
| Target and context | No target, uptake receptor(s), intracellular target(s), antitargets, species, cell line/TP53 background, pH, serum, dose where relevant? |
| Starting references | Actual pinned primary paper/data/structure, chemical source, sequences only if verified, and reuse permissions. |
| Candidate space | Complete/partial canonical sequence, caps, cyclic/stapled chemistry, permitted edits, protected residues and unsupported views. |
| Design plans | At least one feasible baseline, possible generation and a genuinely different guidance/feedback proposal when operations exist. |
| Evidence | Predictors and their native output semantics, source/applicability, known assays, unavailable evaluations, model dependencies and disagreements. |
| Acceptance | Executable evaluation/proposal tests or scientific reference reproduction with explicit expected behavior; no fabricated quantitative biological success. |
| Resource/budget | Provider identity/versions, allowed asset terms, actual generation/evaluation calls, observable cost, failures and reproducibility. |

An **optional later experimental record** can track uptake, compartment access, target engagement and cellular effects; completion of a **computational** case does not require new laboratory data. A literature reference is not a PeptideMT-generated assay result.

## 5. Suggested adoption order and scientific value

- **First CPP-focused case after qualified CPP evaluation exists:** CPP-01 R8/R9, with CPP-02 penetratin for counterexamples. These are simpler than target-directed oncology and expose label/assay ambiguity with minimal chemistry.
- **First delivery-function extension:** CPP-03 TAT carrier/cargo and CPP-04 dfTAT endosomal escape. CPP-11 then adds **noncovalent oligonucleotide cargo/formulation**, which a peptide-only classifier cannot characterize.
- **First *target + CPP-like + anticancer* case:** **CPP-05 p28**, because its historical molecule is a short azurin-derived fragment and its p53 binding/anticancer context is experimentally described without requiring a staple.
- **More demanding conditional delivery cases:** CPP-06 iRGD, CPP-07 pHLIP and CPP-12 protease-activated ACPPs, each with a different conditional biological mechanism.
- **Advanced chemistry and dual target/function cases:** CPP-08 cyclic CPPs and CPP-09 stapled ATSP-7041.
- **Parallel computational hypothesis test:** CPP-10 CPP+AMP joint guidance versus filtering, whenever a qualified CPP resource is available.

The ordering is illustrative, **not** a claim that literature reproducibility, software readiness or scientific difficulty can be reduced to one universal rank. Different studies may become practical sooner when their data/engines are available.

## 6. Current boundary: do not change W0–W4, V0.1 or the scientific contract

D33–D36 approved **AMP/hemolysis with Macrel first**, then a separately considered HydrAMP generative increment. W0 engineering receiving is now centrally completed according to the current repository record; W1–W4 and M1–M8 remain separate scientific implementation/qualification gates, not results of this CPP inventory. This new CPP project pool **does not** authorize new models, datasets, installations, issues, development changes, target-directed work, experimental protocols or a broader V0.1 acceptance gate.

Use the pool as a **scientific compass** and a candidate backlog of future **case-guided contracts**, not as automatic planned releases. An investigator must explicitly select a case and its supported operations before Codex implements it.

**Original ambition remains testable:** PeptideMT should ultimately be able to join target recognition with learned functional guidance, while preserving what a particular CPP-like signal can and cannot establish.
