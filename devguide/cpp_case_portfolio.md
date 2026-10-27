# CPP case-guided development portfolio: representative biology, delivery and peptide engineering

**Status:** research-grounded **portfolio of proposed future scientific guide projects**, 2026-10-27. It is an **inventory and progression**, not a newly approved demonstration, scientific implementation, experimental protocol, V0.1 extension, accepted function ontology or new D decision. None of the CPP-specific methods discussed here is currently qualified in PeptideMT. The immediate authorization remains **D35–D36 / W0–W4 / Macrel AMP–hemolysis**, and W0 central receiving must finish before W1.

Navigation: [design cases](design_examples.md) · [specific ATSP-7041 study](case_study_cpp_anticancer_mdm2_mdmx.md) · [scientific north star](scientific_trajectory.md) · [families](functional_families.md) · [vision](vision_scope.md) · [horizons](future_horizons.md) · [roadmap](roadmap.md) · [index](README.md).

## 1. Purpose: test a *space of scientific problems*, not one CPP classifier

PeptideMT's original goal combines **molecular-target recognition** and **functional-family knowledge capable of influencing peptide design**. We need a small but **representative pool of guide projects**, ranging from canonical linear CPPs to complex, chemically modified and cancer-directed intracellular ligands. In particular, the successful or failed prediction of one generic CPP label cannot substitute for the relevant biological operation.

CPP-related phenomena to distinguish:

1. **Cell-surface binding / membrane adsorption** versus internalization.
2. **Total uptake** versus productive **cytosolic** or nuclear delivery; endosomal retention is neither.
3. **Transport of the peptide itself** versus delivery of a linked or complexed **cargo** with its own chemistry, release and activity.
4. **Direct membrane transport** versus endocytosis and endosomal escape; mechanisms can vary with context.
5. **Cell-type preference**, tumor-tissue penetration, microenvironment-responsive entry and organelle targeting as different location/selectivity questions.
6. **Membrane penetration and cytotoxicity** versus a specific intracellular target/mechanism.
7. **Sequence-view predictions** versus predictions on fully specified cyclized, stapled, conjugated, D-amino-acid or noncanonical molecules.
8. **Mammalian CPP** versus a peptide entering **bacteria**; entry into one biological membrane does not transfer automatically to another.

A guide case must specify *what crossed which barrier*, *what reached which compartment*, *whether a cargo was involved*, *what molecular target or physiological endpoint was intended*, and *which evidence can actually test that distinction*.

### Evidence and comparison rules for every guide project

- State **scientific question**, reference molecular identity/chemistry, organism/cell/compartment/conditions, desired function, possible counterobjective, and accepted/comparable evidence.
- Keep literature observations attached **only to the studied molecule and assay**, separate from proposed computational sequences and providers.
- Declare each method's native alphabet, chemical domain, model identity, actual available output and applicability; unsupported operations stay unavailable.
- Compare a reference, a negative/control where scientifically justified and a small variation set **only if those materials are actually sourced**. No invented experimental values, false training labels or automatic score transfer.
- Preserve distinct outputs for uptake, cytosolic access, target engagement, cargo function, off-target/membrane damage and phenotype. A peptide may pass one and fail another.
- Meaningful computational completion can be a faithful reproduction/analysis, a ranked but unresolved proposal set or an informative failure. Experimental work is optional and requires its own design and evidence.
- Historical studies contain assay-dependent claims. In particular, [Richard et al., JBC 2003](https://pubmed.ncbi.nlm.nih.gov/12411431/) showed that fixation and surface-adsorbed fluorescence can confound apparent CPP entry. A fluorescence-positive readout alone should not become **cytosolic delivery evidence**.

## 2. Portfolio matrix and scope progression

Priorities are **suggested order for case-guided learning**, not dependencies, release commitments, or a requirement that a future model can solve each entry. "CPP-adjacent" means a delivery step or tissue/organellar penetration question that is not interchangeable with a conventional cell-entry classifier.

| ID | Guide project | Distinguishing problem | Molecular modality | Scientific reference | Tier |
| --- | --- | --- | --- | --- | --- |
| CPP-01 | Tat vs oligoarginine | Minimal **cationic linear** CPP motifs; simple quantitative controls; adsorption vs uptake | Canonical short peptides | Vives 1997; Futaki 2001; Richard 2003 | I |
| CPP-02 | Penetratin | **Amphipathic natural-derived** CPP; composition alone is not the mechanism | Canonical linear peptide | Derossi 1994 | I |
| CPP-03 | Pep-1 + protein cargo | **Noncovalent complex** and cargo function, not just free-peptide penetration | CPP–cargo assembly | Morris 2001 | II |
| CPP-04 | Tat fusion / linked cargo | **Covalent/fusion delivery**; carrier vs complete construct and active cargo | Explicit CPP–protein conjugate/fusion | Fawell 1994; Schwarze 1999 | II |
| CPP-05 | Azurin-derived **p28** | **Intrinsically cell-penetrant anticancer peptide with molecular target p53** | Canonical linear peptide (chemistry/assay exact) | Yamada 2009/2013; human phase-I 2013 | II |
| CPP-06 | **iRGD** | **Tumor homing, proteolysis and NRP1-dependent tissue penetration**, not guaranteed cytosolic delivery | Cyclized targeting peptide, cleaved active fragment, cargo | Sugahara 2009 | III |
| CPP-07 | **pHLIP** | **pH-dependent membrane insertion** and cargo translocation/release | Environmental states, conjugation/linker | Reshetnyak 2006 | III |
| CPP-08 | **GALA** endosomal escape | Acid-dependent membrane-fusogenic **helper**, not automatically an independently cell-penetrating peptide | Environment-responsive membrane-active module | Parente 1988 | III |
| CPP-09 | **cFΦR4** / cyclic CPP | **Noncanonical cyclic** chemistry, uptake vs **endosomal escape** | Macrocycle incl. naphthylalanine | Qian 2013/2014/2016 | III |
| CPP-10 | **ATSP-7041** | **Stapled, intracellular MDM2/MDMX binder** with p53-dependent anticancer precedent | Noncanonical stapled p53 mimetic | Chang 2013; PDB 4N5T; existing full study | IV |
| CPP-11 | Mitochondria-penetrating peptide | **Organelle-specific** localization vs general cellular entry and organelle membrane disruption | Cationic/lipophilic peptides, sometimes noncanonical | Horton 2008/2012; Kelley 2011 | III–IV |
| CPP-12 | Buforin II | **Bacterial intracellular-access AMP**, membrane penetration vs lytic AMP action; **not mammalian CPP equivalent** | Linear antibacterial peptide | Park 1998/2000 | II |
| CPP-13 | Joint **CPP + AMP**, target-free | Multi-function design without dummy target, independent contexts and safety | Canonical sequences first | Existing [case D](design_examples.md#5-case-d--cpp--amp-without-an-explicit-molecular-target) | II–III |
| CPP-14 | Joint **CPP + ACP + target**, abstract | Target/family co-design independent of one historical binder; prioritize genuine model-feedback comparisons | Linear and/or qualified stapled | Existing [case C](design_examples.md#4-case-c--cpp--acp-conditioned-on-a-molecular-target) | IV |

**Tier I:** sequence-level references/semantics, not verified CPP prediction. **Tier II:** functional distinctions and real cargo/target biology with limited chemistry. **Tier III:** states, transformation, delivery, compartment or noncanonical chemistry. **Tier IV:** demanding joint target, functional and chemical design. Tiers are pedagogical, **not** claims of implementation effort, validated model availability or chronological obligation.

**No single current predictor is established as covering all fourteen questions.** In particular, Macrel is AMP/hemolysis and HydrAMP is a learned AMP proposal engine; neither supplies CPP, tumor-specific uptake, p28/p53 recognition, pHLIP condition, nuclear delivery, cytosolic cargo or stapled chemistry out of the box.

## 3. Case cards — initial linear/canonical references

### CPP-01 — Tat and Arg8: what does a simple CPP score actually predict?

**Scientific question:** Can we distinguish the native uptake reported for short arginine-rich CPPs from generic high charge, surface adhesion and true cytosolic entry?

- **Reference:** Tat-derived basic CPP, e.g. **YGRKKRRQRRR** as an 11-residue published variant; an explicit **R8** oligoarginine reference. These are *example sequence views*, not full chemical species with declared terminal/linker/dye conditions.
- **Published precedent:** [Vives et al. 1997](https://pubmed.ncbi.nlm.nih.gov/9188504/) and [Futaki et al. 2001](https://doi.org/10.1074/jbc.M007540200). Interpretation warning: [Richard et al. 2003](https://pubmed.ncbi.nlm.nih.gov/12411431/).
- **Future computational exercise:** load known sequence variants, assess model scope and charge/length/descriptors when actually supported; explore substitutions/length series under a **declared** design problem and retain every candidate, unsupported view and resource meaning. Later, compare qualified CPP evaluators with independently sourced uptake and cytosolic data.
- **Decisive failure test:** an algorithm that scores Arg-rich strings as CPP cannot report cytosolic delivery or a unique direct-translocation mechanism without corresponding evidence.
- **Readiness:** suitable as a **very early data/meaning fixture** once an actually permitted CPP evaluator exists; not already a working CPP classification test.

### CPP-02 — Penetratin: amphipathicity beyond net positive charge

**Scientific question:** Can a design method distinguish sequence arrangement, aromatic residue contributions and amphipathic character from a charge-only proxy?

- **Reference:** Antennapedia third-helix-derived **penetratin**, commonly represented by **RQIKIWFQNRRMKWKK**; pin the exact variant, termini and reporting source when preparing fixtures.
- **Published precedent:** [Derossi et al., JBC 1994](https://pubmed.ncbi.nlm.nih.gov/8144628/) reported the third-helix translocation phenomenon and effects of aromatic substitutions under its experimental conditions. Early mechanism interpretations require the later uptake-artifact caveats.
- **Exercise:** compare a sourced reference with sequence-permuted or explicitly designed variants using qualified representation-dependent models and, if available, empirical uptake readouts. Avoid treating calculated helicity/amphipathicity as an observed delivery event.
- **Failure test:** a descriptor-matched scrambled sequence is not automatically an experimentally valid inactive negative or an equivalent molecule.
- **Readiness:** early conceptual/computational reference; evaluation may be inapplicable until qualified.

### CPP-03 — Pep-1: noncovalent protein-cargo complexes

**Scientific question:** Does a peptide carrier enable uptake and **functional delivery** of a protein cargo through an explicitly represented complex?

- **Published precedent:** [Morris et al., *Nature Biotechnology* 2001](https://doi.org/10.1038/nbt1201-1173) on Pep-1-mediated delivery of biologically active proteins.
- **Design entities:** Pep-1 sequence/chemistry, protein cargo, their **noncovalent association** and specific tested context; no assumption that a sequence-only ligand model measures stability of the complex.
- **Exercise:** compare peptide-alone, cargo-alone and reported carrier–cargo complex evidence, and eventually assess supported variant complexes. Record assembly assumptions, mixing/stoichiometry where known, outcomes and cargo functionality separately.
- **Failure test:** an encouraging prediction for free Pep-1 is not evidence that a particular intact folded protein reaches the cytosol.
- **Readiness:** requires future cargo/assembly/context support; not an increment-1 requirement.

### CPP-04 — Tat-linked/fused protein delivery: covalent topology matters

**Scientific question:** How do carrier fusion or coupling and cargo identity affect the molecular object and the meaning of delivery?

- **Published precedents:** [Fawell et al. 1994](https://pubmed.ncbi.nlm.nih.gov/8290579/) and [Schwarze et al., *Science* 1999](https://pubmed.ncbi.nlm.nih.gov/10477521/). Their experimental constructs and administration conditions are the references, not universal transfer guarantees.
- **Exercise:** record native Tat segment, linker, **cargo protein**, complete fusion/conjugate, cell/tissue context and biological cargo readout as distinct from peptide uptake. Distinguish an engineered fusion from a peptide with an appended tag that has not been chemically specified.
- **Failure test:** a positive carrier classifier does not establish cell entry, tissue distribution, cargo unfolding/refolding or biological activity of the full construct.
- **Readiness:** future complex/cargo engineering.

## 4. Case cards — target-related anticancer and context-dependent delivery

### CPP-05 — p28 from azurin: a **simpler, linear** anticancer CPP–target guide

**Scientific question:** Can one peptide support both **preferential cancer-cell entry** and an independently supported intracellular interaction with **p53**, with a context-qualified antiproliferative effect?

- **Reference:** azurin residues **50–77**, p28, **LSTAADMQGVVTDGMASGLDKDYLKPDD** (28 residues) as reported in [Yamada et al., *British Journal of Cancer* 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3694247/). Preserve terminal/experimental reagent identity before chemical-specific evaluation.
- **Mechanism/evidence:** p28 interacts with the **DNA-binding domain of p53** and has reported associations with reduced COP1-mediated ubiquitination and altered p53 cellular responses. It is **not** an MDM2/MDMX antagonist in the same sense as ATSP-7041. Published cancer-cell and mechanistic responses depend on **p53 mutation/genotype and biological context**.
- **References:** [p28-derived cell-cycle evidence, 2009](https://pubmed.ncbi.nlm.nih.gov/19808975/); [target/mechanism, 2013](https://pubmed.ncbi.nlm.nih.gov/23736031/); [p53 variant context, 2013](https://pubmed.ncbi.nlm.nih.gov/23952735/); [human phase-I feasibility/safety and preliminary observations](https://pubmed.ncbi.nlm.nih.gov/23449360/). A clinical study **does not** establish efficacy of novel designed derivatives.
- **Case exercise:** freeze the reference peptide and p53 sequence/structure domain, compare declared p28 subfragments and supported designed variants, **separately** account for cell entry, actual p53 binding, COP1/pathway mechanism and cancer phenotype. Specific p53 DNA-binding domain structure/mutant must be attributed. Study nonmalignant/TP53 context as qualifiers, not automatic cancer specificity.
- **Critical contrast:** a CPP label may say little about p28's noncanonical *anionic/amphipathic* uptake pattern; an ACP label cannot prove COP1/p53 causality. A favorable docking pose cannot establish cellular entry.
- **Readiness:** **recommended first target-dependent anticancer CPP guide** in future work because the reference is an ordinary linear sequence rather than hydrocarbon-stapled chemistry. This does **not** mean qualified target recognition or CPP/ACP tools are already available.

### CPP-06 — iRGD: tumor localization and proteolytic activation are different from generic CPP uptake

**Scientific question:** Can a conditional tissue-penetrating design preserve its **integrin binding → protease exposure of CendR motif → neuropilin-1 engagement** cascade?

- **Reference:** **iRGD**, a tumor-homing peptide built around an RGD sequence and a proteolytically exposed CendR motif. Its cyclic/precleavage and exposed active-fragment chemistry must remain distinct; identify exact tested variant from the reference.
- **Primary work:** [Sugahara et al., *Cancer Cell* 2009](https://pmc.ncbi.nlm.nih.gov/articles/PMC2791543/) reported tumor-vessel homing and enhanced tissue delivery under stated experimental conditions.
- **Exercise:** distinguish intended **tumor penetration**, cellular uptake and **cytosolic** delivery of any cargo. Express cleavage as a context-dependent transformation with source/product and distinct functional roles, not as an unannotated edit or an independent peptide score.
- **Failure test:** a generic CPP classifier or RGD docking score alone cannot certify CendR activation, tumor penetration or intracellular cargo activity.
- **Readiness:** later transformation/target/cargo case. **CPP-adjacent**, not a clean positive reference for generic CPP sequence classifiers.

### CPP-07 — pHLIP: pH is part of the *scientific problem*

**Scientific question:** Can a peptide insert/translocate cargo at acidic extracellular pH while behaving differently at normal pH?

- **Reference:** **pH(low) insertion peptide (pHLIP)**, including any explicitly declared C-terminal cargo conjugation/linker and protonation/bilayer context; these are different chemical candidates and experimental conditions.
- **Primary work:** [Reshetnyak et al., *PNAS* 2006](https://pmc.ncbi.nlm.nih.gov/articles/PMC1435408/).
- **Exercise:** compare separate pH/chemical contexts; track peptide insertion, cargo movement and cleavage/release where relevant. Do not collapse acidic and neutral outputs into one family label or extrapolate a single pH-independent score.
- **Failure test:** low-pH bilayer insertion is not proof of tumor selectivity, cytosolic delivery of any arbitrary cargo or universal cell penetration.
- **Readiness:** future contextual/state, environment and linker/cargo handling. **CPP-adjacent**.

### CPP-08 — GALA: distinguish an *endosomal escape helper* from entry

**Scientific question:** Can acid-triggered fusogenic or membrane-active peptides change cargo release **after** a separate uptake route?

- **Reference:** synthetic Glu–Ala–Leu–Ala-repeat-derived **GALA**, under acidic membrane conditions.
- **Primary work:** [Parente et al., *JBC* 1988](https://pubmed.ncbi.nlm.nih.gov/2450874/) reports pH-dependent vesicle fusion, not a generic whole-cell CPP/cancer activity claim.
- **Exercise:** treat initial uptake and endosomal release as **different** requirements and evaluations. Compare delivery with and without a compatible escape module, but only if an actually qualified assembly/transport route exists.
- **Failure test:** fusogenicity in liposomes cannot be silently relabeled measured endosomal escape in living cells or cytosolic cargo delivery.
- **Readiness:** future delivery-composition case, **not** a classic stand-alone CPP benchmark.

## 5. Case cards — advanced molecular chemistry, organelles and multifunctionality

### CPP-09 — cFΦR4: cyclic CPP and productive cytosolic delivery

**Scientific question:** Can a system preserve macrocycle connectivity and noncanonical aromatic residues while explaining why uptake and endosomal escape differ?

- **Reference:** **cyclo(FΦRRRRQ)**, where **Φ is L-2-naphthylalanine** (not a standard one-letter residue). Do not silently convert Φ to F or omit cyclization.
- **Published studies:** [Qian et al., *ACS Chemical Biology* 2013](https://pubmed.ncbi.nlm.nih.gov/23130658/); [Qian et al., *Biochemistry* 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC4075989/) on early endosomal escape; [later mechanism work 2016](https://pubmed.ncbi.nlm.nih.gov/27089101/).
- **Exercise:** use a specific, chemically complete macrocycle (where supported) and compare documented family members/chemical variants. Keep membrane binding, total uptake, endosomal escape and cytosolic-cargo delivery evidence distinct.
- **Failure test:** a canonical sequence projection or score for linear FFRRRRQ is **not** evidence on cFΦR4.
- **Readiness:** later chemistry-capable design and qualified evaluator; valuable P07 stress test.

### CPP-10 — ATSP-7041: stapled peptide binding MDM2/MDMX

**Scientific question:** Can PeptideMT pursue **intracellular target engagement + peptide access + anticancer mechanism** without losing chemically essential hydrocarbon stapling and target-construct context?

- **Research precedent:** [ATSP-7041 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC3767549/) and experimental [PDB 4N5T](https://www.rcsb.org/structure/4N5T). Preserve receptor species/construct: the deposited MDMX construct is **not** simply a native unmodified human receptor. The p53-mimetic stapled ligand and a canonical linear projection are different scientific objects.
- **Detailed guide:** **[case_study_cpp_anticancer_mdm2_mdmx.md](case_study_cpp_anticancer_mdm2_mdmx.md)** defines E0–E7, distinct evidence layers, cancer context, control cases and computational plans. Do not duplicate these contracts here.
- **Failure test:** favorable generic CPP/ACP scores or a plausible pose do not prove productive intracellular MDM2/MDMX antagonism, p53 pathway activation or antitumor efficacy.
- **Readiness:** a high-complexity **later** target/function/chemistry guide; preserve p28 as a simpler complementary first case.

### CPP-11 — mitochondria-penetrating peptides: subcellular destination matters

**Scientific question:** How do peptide composition and chemical modifications favor **mitochondrial localization** without causing mitochondrial membrane disruption?

- **Primary research:** [Horton et al., *Chemistry & Biology* 2008](https://pubmed.ncbi.nlm.nih.gov/18420144/), [Kelley et al., 2011](https://pubmed.ncbi.nlm.nih.gov/21833796/), [Horton et al., *ChemBioChem* 2012](https://pubmed.ncbi.nlm.nih.gov/22238158/).
- **Exercise:** express whole-cell entry, organelle localization, matrix accumulation and membrane injury as separate questions. Where a published candidate uses delocalized lipophilic cations or noncanonical residues, keep that chemistry rather than inventing canonical substitutions.
- **Failure test:** mitochondrial fluorescence cannot alone be reinterpreted as matrix delivery of an active cargo, nor does generic CPP activity prove mitochondrial targeting.
- **Readiness:** future organellar/chemical/context capability; no mitochondrial classifier assumed.

### CPP-12 — buforin II: antimicrobial entry is **not** mammalian-cell CPP

**Scientific question:** Can a peptide enter bacterial cells and affect intracellular targets without functioning primarily by lysis?

- **Primary research:** [Park et al., *Biochemical and Biophysical Research Communications* 1998](https://pubmed.ncbi.nlm.nih.gov/9514864/) and [structure–activity study, 2000](https://pmc.ncbi.nlm.nih.gov/articles/PMC26932/).
- **Exercise:** distinguish bacteria-specific penetration, membrane disruption, nucleic-acid association and organism-dependent killing. Compare with an appropriate lytic AMP reference only under compatible conditions. Separate bacterial cell entry from human CPP activity and mammalian host toxicity.
- **Failure test:** labeling buforin II as AMP does not prove a human-cell CPP phenotype, cytosolic mammalian access or nonhemolysis.
- **Readiness:** bridge between initial AMP coverage and later CPP-scientific tasks; Macrel AMP/hemolysis does **not** itself test buforin's bacterial translocation mechanism.

### CPP-13 and CPP-14 — open-ended *design* rather than reproducing a known peptide

- **CPP-13: CPP + AMP, target-free:** retain [original conceptual Case D](design_examples.md#5-case-d--cpp--amp-without-an-explicit-molecular-target). No dummy protein target; human cell entry and organism-specific antibacterial activity have different contexts. Distinguish postselection from functional feedback.
- **CPP-14: CPP + ACP + molecular target:** retain [original conceptual Case C](design_examples.md#4-case-c--cpp--acp-conditioned-on-a-molecular-target). Joint target/family conditions, an actual anticancer mechanism, optional negative/secondary targets and chemical modality distinguish it from a generic double-positive classifier.
- **Difference from p28/ATSP:** CPP-05/10 ask if one can **reproduce and then redesign a known literature system**; CPP-13/14 are *open-ended hypothesis-guided scientific requests*. Treating them as equivalent demonstrations would conceal evidence.

## 6. One cross-case evidence checklist and negative controls

Future tasks should create a small **case card** before choosing a model. The card should preserve:

| Attribute | Examples of values/meaning |
| --- | --- |
| Reference identity | Exact published molecule, sequence and any chemical modification; source version and copyright/usage permissions for data |
| Mode | Free peptide / peptide–cargo conjugate / noncovalent complex / cyclic / stapled / cleaved precursor/product |
| Barrier and endpoint | Mammalian plasma membrane / endosome / tumor interstitium / bacterial envelope / organelle; uptake, delivery or cargo function |
| Conditions | Organism, cell line, compartment, extracellular pH, genotype, assay conditions, cargo identity when supplied |
| Targets | MDM2, MDMX, p53, integrin, neuropilin, other specific molecule; roles **binding target, pathway context and antitarget** kept distinct |
| Search and evidence | Fixed reference/reproduction, de novo proposals, redesign, native vs derived scores, biological evidence, costs, applicability and limitations |
| Key negative/control | Nonpenetrating comparison only when evidenced, cargo alone vs carrier–cargo, nonmalignant or TP53-null, neutral vs acidic pH, uptake vs cytosol, alternate species/construct |
| Outcome | Observed real provider execution, qualified computational inference, unassessed question, unsupported chemistry, failed/incomplete/empty selection |
| Acceptance | A **bounded measurable claim** that the chosen actual capability could demonstrate; no automatic translation from CPP prediction to therapy |

**Assay artifact checkpoint:** total fluorescence in fixed cells or surface-retained peptide may overstate internalization, and endosomal puncta do not prove productive cytosolic delivery. Use [Richard et al. 2003](https://pubmed.ncbi.nlm.nih.gov/12411431/) as the cautionary primary comparison; functional cytosolic cargo or orthogonally localized readouts have different strength and scope.

**Chemistry checkpoint:** labeling, cargo coupling, cleavage, termini, stereochemistry, head–tail cyclization and hydrocarbon stapling can all change the actual evaluated subject. Preserve original and derived entities, observed native result, conditional projections and missingness under accepted P07/P04 semantics.

**Model checkpoint:** overlap of training data and assay labels can make two predictor outputs dependent. A generated peptide with the best CPP model score is not proven to penetrate cells, and optimizing that score does not constitute independent assessment.

## 7. Case use, sequence and explicit noncommitments

Recommended use is **scientific scaffolding for future capability selection**, not immediate implementation of all rows:

1. First CPP-specific follow-up, when authorized: **CPP-01 + CPP-02**, to establish what a qualified linear-sequence CPP evaluation means and where it fails.
2. First **intrinsic, anticancer, target-specific CPP** scientific guide: **CPP-05 p28**, which does not require stapled-peptide chemistry as an entry prerequisite.
3. Next **cargo/biology** branch: CPP-03 and CPP-04; **microenvironment/tissue** branch: CPP-06/07/08; **organelle** branch: CPP-11.
4. Advanced **chemistry and cytosolic-delivery** branch: CPP-09 cFΦR4 and CPP-10 ATSP-7041.
5. Functional overlap and joint optimization: CPP-12/13/14, using published evidence where available, actual prediction-domain checks and explicit controls.

This progression is **not a fixed path**: a real scientific project can promote a more demanding case sooner. The goal is representative coverage, not exhaustive peptide enumeration or a mandatory benchmark suite. When an engine is eventually selected, specify only the **one or two** guide cases it can actually exercise and defer the rest.

**Current hard boundary:** finish PeptideMT **W0** central receiving at `bf79de5`, then the already authorized **W1–W4** Macrel AMP/hemolysis increment. **No new CPP predictors, generators, structural/cargo chemistry, PDB files, experimental assays, scientific packages, issues or W0–W4 gates are authorized by this portfolio.** The first *generative* V0.1 increment and all CPP-specific case executions still require their own bounded approval.

## 8. Primary-source index (non-exhaustive)

- [Vives 1997, Tat](https://pubmed.ncbi.nlm.nih.gov/9188504/) · [Futaki 2001, arginine-rich](https://doi.org/10.1074/jbc.M007540200) · [Derossi 1994, penetratin](https://pubmed.ncbi.nlm.nih.gov/8144628/) · [Richard 2003, uptake artifacts](https://pubmed.ncbi.nlm.nih.gov/12411431/).
- [Morris 2001, Pep-1](https://doi.org/10.1038/nbt1201-1173) · [Fawell 1994, Tat cargo](https://pubmed.ncbi.nlm.nih.gov/8290579/) · [Schwarze 1999, Tat delivery](https://pubmed.ncbi.nlm.nih.gov/10477521/).
- [Yamada 2009, p28](https://pubmed.ncbi.nlm.nih.gov/19808975/) · [Yamada 2013, p28/p53](https://pmc.ncbi.nlm.nih.gov/articles/PMC3694247/) · [p28 phase I](https://pubmed.ncbi.nlm.nih.gov/23449360/).
- [Sugahara 2009, iRGD](https://pmc.ncbi.nlm.nih.gov/articles/PMC2791543/) · [Reshetnyak 2006, pHLIP](https://pmc.ncbi.nlm.nih.gov/articles/PMC1435408/) · [Parente 1988, GALA](https://pubmed.ncbi.nlm.nih.gov/2450874/).
- [Qian 2013, cyclic CPP](https://pubmed.ncbi.nlm.nih.gov/23130658/) · [Qian 2014, cytosolic escape](https://pmc.ncbi.nlm.nih.gov/articles/PMC4075989/) · [Qian 2016](https://pubmed.ncbi.nlm.nih.gov/27089101/).
- [Chang 2013, ATSP-7041](https://pmc.ncbi.nlm.nih.gov/articles/PMC3767549/) · [RCSB 4N5T](https://www.rcsb.org/structure/4N5T).
- [Horton 2008, mitochondria](https://pubmed.ncbi.nlm.nih.gov/18420144/) · [Kelley 2011](https://pubmed.ncbi.nlm.nih.gov/21833796/) · [Horton 2012](https://pubmed.ncbi.nlm.nih.gov/22238158/).
- [Park 1998, buforin II](https://pubmed.ncbi.nlm.nih.gov/9514864/) · [buforin SAR 2000](https://pmc.ncbi.nlm.nih.gov/articles/PMC26932/).

References give published precedent, not downloaded permissioned datasets, approved exact peptide synthesis recipes, a qualified model test set or replicated PeptideMT evidence.
