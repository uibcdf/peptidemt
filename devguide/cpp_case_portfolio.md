# Complementary CPP case studies beyond the main guide-project ladder

**Status:** proposed **supplementary scientific case pool**, 2026-10-27; not an approved implementation plan, predictor benchmark, new D decision, or V0.1 change.

**Primary portfolio:** [cpp_guided_projects.md](cpp_guided_projects.md) is the **canonical CPP-01–CPP-12 case-guided ladder**. This document adds **four complementary scientific questions** that fill gaps without reusing CPP identifiers or duplicating the twelve existing briefs. It also links the open-ended [conceptual CPP+ACP/target design case C](design_examples.md#4-case-c--cpp--acp-conditioned-on-a-molecular-target) and the [fully specified ATSP-7041 reference](case_study_cpp_anticancer_mdm2_mdmx.md).

Navigation: [index](README.md) · [canonical CPP guide projects](cpp_guided_projects.md) · [original design cases](design_examples.md) · [scientific trajectory](scientific_trajectory.md) · [future horizons](future_horizons.md).

## 1. Additional coverage, not duplicate identities

| Supplement | Difference relative to CPP-01–CPP-12 | Source precedent | Main later PeptideMT capability tested |
| --- | --- | --- | --- |
| **CPP-S1 Pep-1** | **Noncovalent protein–CPP complex** with protein cargo, unlike the canonical ladder's TAT fusion or oligonucleotide nanocomplex | Morris et al. 2001 | Composition/assembly, cargo identity, productive biological delivery |
| **CPP-S2 GALA** | **Acid-fusogenic endosomal escape helper**, as distinct from dfTAT's dimeric CPP escape and pHLIP's extracellular low-pH insertion | Parente et al. 1988 | Component-level helper role, context, escape versus initial uptake |
| **CPP-S3 mitochondrial peptide** | **Intracellular organelle-specific penetration** after general cell entry, not generic cytosolic delivery | Horton et al. 2008/2012; Kelley et al. 2011 | Cell/organelle boundaries, localization vs membrane injury |
| **CPP-S4 buforin II** | **Penetration into bacteria by an AMP**, not automatically a mammalian CPP and not equivalent to membrane-lytic AMP | Park et al. 1998/2000 | Biological membrane/organism scope, entry vs killing mechanism |

**Overlapping directions already have an owner:** canonical CPP-01/02 cover R8/R9 and penetratin; CPP-03/04 Tat cargo and dfTAT; CPP-05 p28; CPP-06 iRGD; CPP-07 pHLIP; CPP-08 cyclic CPP; CPP-09 ATSP-7041; CPP-10 CPP+AMP; CPP-11 PepFect14; CPP-12 protease-activated CPPs. Do not count overlapping entries as independent validated scientific results. The open-ended CPP+ACP target problem remains **Case C**, not an additional numbered CPP record.

## 2. CPP-S1 — Pep-1 and a noncovalently delivered protein

**Scientific question:** Can a peptide carrier associate noncovalently with a separate protein and produce biologically meaningful **intracellular cargo delivery** without forming a new covalently fused molecule?

- **Published primary reference:** [Morris et al., *Nature Biotechnology* 2001, protein delivery using Pep-1](https://doi.org/10.1038/nbt1201-1173).
- **Scientific input:** Pep-1 as an identified carrier, a concrete protein cargo, the specified noncovalent assembly under reported conditions, and separate source references. Cargo identity and folding matter; an isolated free-peptide string is not the transported assembly.
- **Candidate future exercise:** compare a documented carrier/cargo pair and a justified cargo-alone control, record available composition/association evidence, and distinguish total uptake, intracellular cargo presence and verified protein activity. A chosen generative route could later propose Pep-1 sequence variants while keeping the *same* cargo/assay, when support exists.
- **Main failure:** favorable free-Pep-1 CPP-classifier output cannot certify assembly formation, intact cargo delivery or activity inside cells.
- **Difference from the canonical ladder:** CPP-03 Tat-fusion is covalent; CPP-11 PepFect14 is an oligonucleotide nanocomplex. This case asks a distinct **noncovalent protein-cargo** question.

## 3. CPP-S2 — GALA as an acidic endosomal escape helper

**Scientific question:** Can a fusogenic peptide increase **productive endosomal release after uptake by another route**, rather than merely increasing membrane-associated fluorescence?

- **Primary reference:** [Parente, Nir and Szoka, *JBC* 1988](https://pubmed.ncbi.nlm.nih.gov/2450874/) on pH-dependent vesicle fusion by synthetic amphipathic **GALA**.
- **Scientific input:** GALA with a declared bilayer and acidic condition; a separate uptake/cargo system is required if the question is **endosomal escape in cells**. The liposome study is evidence for vesicle fusion, **not direct evidence of endosomal escape in a living cell**.
- **Candidate future exercise:** assess a justified two-module carrier+escape hypothesis with uptake and escape as separate outcomes, recording actual environmental pH, peptide/cargo molecular assembly and the route that gets the cargo into an endosome.
- **Main failure:** a GALA membrane-fusion or pH-dependent descriptor alone is not evidence of CPP entry, cytosolic cargo or cancer-selective delivery.
- **Difference:** canonical CPP-04 dfTAT shows a tested dimeric CPP endosomal escape route, while CPP-07 pHLIP describes low-pH *plasma-membrane* insertion and cargo translocation. These cannot be assigned the same generic score endpoint.

## 4. CPP-S3 — mitochondria-penetrating peptides and organellar localization

**Scientific question:** Can a cell-permeating carrier accumulate inside mitochondria without becoming primarily a mitochondrial membrane disruptor?

- **Primary references:** [Horton et al., *Chemistry & Biology* 2008](https://pubmed.ncbi.nlm.nih.gov/18420144/); [Kelley, Stewart and Mourtada, 2011](https://pubmed.ncbi.nlm.nih.gov/21833796/); [Horton et al., *ChemBioChem* 2012](https://pubmed.ncbi.nlm.nih.gov/22238158/).
- **Scientific input:** actual mitochondrial peptide molecule (cationic/lipophilic; some experimental variants include noncanonical chemistry), cell type, organellar compartment and membrane context.
- **Candidate future exercise:** compare sourced peptides with distinct reported mitochondrial uptake and disruption tendencies; preserve biological-compartment mapping and chemical differences. When methods support it, relate charge, lipophilicity and chemistry to **separate** total uptake, organellar location and membrane-integrity evidence.
- **Main failure:** cytosolic entry does not establish mitochondrial matrix access; organellar fluorescence alone need not demonstrate fully released cargo or absence of membrane damage.
- **Difference:** unlike the canonical CPP ladder's tissue targeting and generic cytosolic delivery, this explicitly tests the **next compartment barrier** and organelle-associated toxicity.

## 5. CPP-S4 — buforin II: intracellular antibacterial action is not human-cell CPP behavior

**Scientific question:** Can an antimicrobial peptide enter **bacterial cells**, interact with internal biomolecules and kill microorganisms without acting primarily through overt membrane lysis?

- **Primary references:** [Park, Kim and Kim 1998](https://pubmed.ncbi.nlm.nih.gov/9514864/) and [structure–activity/proline-hinge study 2000](https://pmc.ncbi.nlm.nih.gov/articles/PMC26932/).
- **Scientific input:** a specified buforin II peptide/variant, bacterial organism and relevant comparison with a lytic AMP under compatible observations. A human-cell CPP context is **not** implied.
- **Candidate future exercise:** separate antibacterial compatibility, bacterial uptake, nucleic-acid association, membrane damage and organism-specific killing. Compare published buforin/magainin mechanism distinctions with subsequent source-qualified predictions if suitable resources are eventually admitted.
- **Main failure:** positive Macrel AMP classification cannot automatically be interpreted as bacterial penetration, target-specific inhibition, **human-cell CPP**, safety or absence of hemolysis.
- **Difference:** this complements the first **AMP/hemolysis** coverage with a much more demanding *mechanistic* design objective, without expanding D35/M1–M8.

## 6. Cross-case acquisition, guide order and honest claims

The [canonical twelve-case portfolio](cpp_guided_projects.md) supplies the main progression, especially **CPP-05 p28** as a relatively simple intracellular anticancer/target case and **CPP-09 ATSP-7041** as a harder chemistry-dependent comparison. Their progression is **not** a fixed development sequence. The four supplements above should be selected if a future real capability addresses their distinctive evidence questions:

- **Peptide-cargo composition** → CPP-S1.
- **Uptake followed by endosomal-release helper** → CPP-S2.
- **Subcellular organelle targeting** → CPP-S3.
- **Bacterial penetration and target/membrane mechanism** → CPP-S4.

Every case needs a stated molecular subject, actual chemical representation, biological organism/compartment, defined action and relevant evidence. Keep surface adhesion, endocytosis, total uptake, cytosolic availability, cargo delivery, target engagement, phenotype and toxicity distinct; [Richard et al. 2003](https://pubmed.ncbi.nlm.nih.gov/12411431/) documents historical uptake-assay artifacts. A source result on labeled, cleaved, cyclic, conjugated or stapled chemistry is not automatically an outcome for a canonical unmodified peptide.

**No CPP-specific computational execution is currently qualified by these papers.** No speculative reference model, predictor, experimental activity, sequence edit or clinical effect is presented as generated by PeptideMT.

**Current authorization remains unchanged:** proceed through the authorized W1–W4 Macrel AMP/hemolysis work under D35–D36 after the centrally received W0 engineering bootstrap. Neither the twelve core cases nor these four supplements requires a new general architecture, extra issues, scientific code, provider installs, experiments or release commitments.
