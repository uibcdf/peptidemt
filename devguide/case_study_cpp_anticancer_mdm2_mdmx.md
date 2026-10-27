# Case-guided scientific development: cell-permeating anticancer peptide targeting MDM2/MDMX

Status: **published-evidence-anchored design and verification case; proposed future development guide**, 2026-10-27. Not a V0.1 implementation requirement, selected demonstrator, chemical support claim, experimental plan or new accepted D decision. The original [conceptual CPP + ACP case C](design_examples.md#4-case-c--cpp--acp-conditioned-on-a-molecular-target) remains in place; this companion supplies a **specific experimentally studied molecular reference**.

Navigation: [index](README.md) · [five worked cases](design_examples.md) · [scientific trajectory](scientific_trajectory.md) · [families](functional_families.md) · [capabilities](capabilities_and_composition.md) · [horizons](future_horizons.md) · [roadmap](roadmap.md).

## 1. Why this case, and what the literature actually establishes

**Design question:** Can we use computational peptide design to propose an intracellularly active peptide that antagonizes the **MDM2/MDMX–p53 interactions** in a **TP53-wild-type** cancer context, while separately reasoning about **cellular entry**, **target engagement** and **anticancer phenotype**?

The scientific precedent is **ATSP-7041**, a hydrocarbon-*stapled* p53-mimetic α-helical peptide, not a generic canonical linear peptide:

- [Chang et al., *PNAS* (2013), doi:10.1073/pnas.1303002110](https://pmc.ncbi.nlm.nih.gov/articles/PMC3767549/) reported dual MDM2/MDMX binding, target-related p53 pathway activation, cellular activity and tumor-growth suppression in the stated experimental models. The source paper reports nanomolar affinities in its tests; do not export those values as blanket predictions for new designs.
- [Mechanistic validation study (2016), PMID 27721413](https://pubmed.ncbi.nlm.nih.gov/27721413/) examined uptake, intracellular p53–MDM2/MDMX interference and p53-dependent cellular effects, including assessment under serum-containing conditions.
- [RCSB PDB 4N5T](https://www.rcsb.org/structure/4N5T), [doi:10.2210/pdb4N5T/pdb](https://doi.org/10.2210/pdb4N5T/pdb), contains an experimental **1.7 Å MDMX–ATSP-7041 complex**. The deposited receptor construct is associated with *Danio rerio* and includes structural modifications. **Do not assume it is directly an unmodified human MDMX reference**, or conflate its chain numbering/species with the intended human therapeutic context without explicit mapping.
- [ALRN-6924 discovery, *Journal of Medicinal Chemistry* (2023)](https://pubmed.ncbi.nlm.nih.gov/37439511/) documents a **related but chemically distinct** cell-permeating stapled p53 mimetic optimized for MDM2/MDMX inhibition. Its active metabolite emphasizes the need to distinguish chemical species and transformations.
- [ALRN-6924 Phase 1 results, *Clinical Cancer Research* (2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9401461/) provide clinical context for the modality. These are observations on that drug and enrolled patients, **not** clinical efficacy or safety evidence for a future PeptideMT candidate.

**Terminology nuance:** ATSP-7041 is an **experimentally cell-permeating intracellular inhibitor**, an excellent CPP-like *delivery/function design* reference. It need not belong to the positive class of a generic **sequence-based CPP classifier**, particularly one trained only on canonical linear peptides. For this case, prefer the scientific objective **effective intracellular access** over defining success by a binary CPP label. Cellular uptake, cytosolic access, target engagement and anticancer activity remain separate endpoints.

The reason to use a known published system is **to make claims testable**. Reproducing aspects of prior structural or computational evidence is a useful validation exercise. It does not require discovering a new anticancer therapeutic.

## 2. Scientific problem definition, independent of methods

| Aspect | Intended scientific meaning | Limits |
| --- | --- | --- |
| Designed molecular entity | A peptide capable of intracellular target engagement; linear p53-derived precursors and chemically stapled derivatives are distinct candidate modalities. | One-letter sequence does not encode staples, noncanonical chirality, caps or complete chemistry. |
| Primary target | Human **MDM2** in the relevant p53-interaction region. | Predicted association is not verified competition with p53. |
| Secondary desired target or design branch | Human **MDMX/MDM4** for dual antagonism; another explicit branch may study MDM2 selectivity. | MDMX is not silently a negative target in the dual-inhibitor branch. |
| Desired interaction | Disrupt p53 binding to its inhibitors, enabling **p53 pathway reactivation** in an appropriate **TP53-WT** context. | Binding to MDM2/MDMX, disruption of those PPIs and pathway activation are progressively stronger, distinct claims. |
| Desired access | Efficient entry and availability where intracellular MDM2/MDMX can be engaged. | Membrane adsorption, total uptake, endosomal accumulation and productive cytosolic/nuclear access differ. |
| Desired phenotype | Reduced growth/viability of selected TP53-WT cancer models via the stated mechanism, subject to assay context. | A generic ACP prediction or nonspecific cytotoxicity cannot establish this mechanism. |
| Selectivity/control contexts | TP53-mutant/null comparison where experimentally applicable, unrelated PPIs/targets, and relevant nonmalignant-cell context. | These are proposed discriminating comparisons, not claims of universal cancer selectivity or absence of host toxicity. |
| Constraints and tradeoffs | Relevant chemical feasibility, structure and binding-site preservation, proteolytic stability, solubility, cell access, membrane damage and exposure when applicable. | No universal numerical thresholds or biological guarantee is selected. |

**Alternative problem formulations should be kept separate.** Designing a *dual* MDM2/MDMX antagonist, an *MDM2-only* antagonist, or a *CPP–binder fusion/conjugate* changes molecular modalities and/or intent. A fusion with a separate CPP tag is not chemically identical to intrinsic permeability gained through hydrocarbon stapling.

### Important biochemical and structural attribution

- The mechanism targets **MDM2 and/or MDMX**, which are p53 regulators; the design does **not** require binding directly to p53 as the peptide's target.
- Keep target **species**, construct, numbering, region, mutation, state and experimentally resolved structure separate. Map PDB 4N5T's receptor to the chosen human MDMX context before making human-target claims.
- The hydrocarbon staple is part of the designed ligand, not a removable visualization style. The PDB ligand has modified residues and a nontrivial covalent topology. A canonical letter projection cannot claim full-peptide binding, access or anticancer function.
- TP53-WT is a context for the proposed on-mechanism phenotype, **not** proof that every TP53-WT cancer responds. Effect depends on actual tumor biology and experimental conditions.
- ATSP-7041 and ALRN-6924 are **different chemical molecules** and should not be treated as alternative names for one structure or transferred assay record.

## 3. Four different levels of evidence to keep separate

1. **Published prior evidence:** direct experimental binding, structural and cellular/model effects for the named historical molecules, with their exact species, constructs, conditions and assays.
2. **Provider- or representation-specific computational checks:** for example reading PDB 4N5T, mapping residues and covalent link topology, reproducing a published structural contact pattern under a qualified method. Does not establish uptake.
3. **Predictions about new candidates:** qualified binding-geometry, sequence-family, permeability, stability or contextual phenotype signals. A score is not automatically a biochemical measurement. Reuse of the same or overlapping training data weakens independence.
4. **New experiments (future and optional):** actual intracellular uptake/access, cellular target engagement, pathway and phenotype assays, with species/genotype, dose, viability and method attribution. Computational completion does not require experiments.

A candidate could have favorable structural recognition and no applicable CPP or ACP predictor. That means **functional evidence is absent**, not that it has no access or anticancer effect. Conversely, a high CPP/ACP score cannot replace target-binding or pathway evidence.

## 4. Case-guided progression: exercises that lead to qualified capability contracts

This is a **future case-driven development sequence**, not a newly authorized W0–W4 deliverable. All stages can produce truthful partial or negative results.

| Case stage | Scientific question and candidate operation | Minimum meaningful evidence | What success must **not** be called |
| --- | --- | --- | --- |
| E0. Reference identity | Identify publications, PDB 4N5T receptor/ligand chemistry and the corresponding human targets. | Pinned source/structure revision, chain/residue/atom and species/construct mapping; modified residue/staple inventory. | A native human complex or complete peptide chemical representation inferred from a one-letter string. |
| E1. Molecular-view attribution | Express a sequence-only p53-derived hypothesis and one or more **explicitly defined** stapled realizations; identify supported operations for each. | Proposal→realization→evaluated-view links; unsupported/noncanonical chemistry and projection losses retained. | Treating a linear proxy as the original ATSP-7041 molecule. |
| E2. Target recognition | With suitable target structures and qualified tools, evaluate peptide interfaces, alternative poses or protein–peptide competition evidence. | MDM2 vs MDMX role, species and construct, pose/score semantics and applicability; where possible reproduction against literature references. | Predicted pose equals measured Kd, p53 displacement or pathway activation. |
| E3. Intracellular access | Assess sequence-level CPP *only when its chemical domain applies*; else use separate applicable permeability/uptake evidence or mark absent. | Exact method, chemistry, biological compartment and meaning of its endpoint. | Total uptake or a binary label automatically proves cytosolic/nuclear engagement. |
| E4. Anticancer mechanism | Tie target evidence, TP53-WT pathway hypothesis and the selected cellular phenotype to distinct tests and known reference experiments. | Separate target, pathway and cancer-cell evidence; identify mutant/null/nonmalignant comparators where available. | A generic ACP score automatically proves TP53-dependent cancer suppression. |
| E5. Generate/redesign | Under an actually capable generator, propose supported new sequences/chemical realizations with explicit edit-preservation and constraints. | Which generator emits sequence, backbone or full chemistry; lineage and constraints; no auto-attributed parental evaluations. | A modified sequence automatically preserves its staple, binding pose or uptake. |
| E6. Search guidance and controls | Compare target-first, function-first, generate-and-filter and genuinely feedback-guided search when supported. | Actual intervention; comparable search opportunity/compute budgets; candidate coverage/diversity; native and independent assessment limits. | Favorable reward proves biological activity or improvement over a budget-mismatched control. |
| E7. Purpose-specific selection | Produce a small reproducible computational shortlist or decide to ask for another evaluation. | Raw evaluations, unresolved requirements, noncomparable inputs, selection reasons and legitimate empty outcomes. | Shortlist equals validated anticancer medicine. |

E2–E6 may be reordered or partially omitted by a justified plan; the architecture **does not require a mandatory linear process**. An intentionally modest first exercise might only reproduce structure **identity and chemistry distinctions**, with all cell-entry and phenotype objectives explicitly unassessed.

### Plans that address the same biological intent differently

- **Reference-driven redesign:** start with chemically identified ATSP-7041 or a published precursor; vary only operations and chemical features actually supported, with separate target/function reassessments.
- **Target-first generation:** design candidate binders of MDM2 or MDMX using a target-capable engine, then evaluate intracellular-access and phenotype proxies if their domain is valid.
- **Function/access-first generation:** use a qualified accessible-peptide/CPP-related proposal distribution, then seek MDM2/MDMX recognition; this may be poor at either objective and is an explicit hypothesis.
- **Guided joint search:** introduce appropriately attributable reward signals during later proposal decisions or inside an engine's supported search operation; do not assume a classifier can score intermediate diffusion states or provide gradients.

There is no guarantee that a common *unmodified canonical-sequence* proposal model can generate ATSP-7041-like chemistry. It can legitimately search a **different declared chemical subdomain**, but cannot claim to have reproduced the chemically stapled reference.

## 5. Scientific controls and failure examples

| Test case | Correct scientific interpretation |
| --- | --- |
| The exact ligand from 4N5T is projected to 20-letter sequence for a classifier. | If the projection is allowed at all, report the lost noncanonical/staple chemistry and an explicitly **surrogate** result; do not attribute full stapled-peptide permeability to that score. |
| The complex is built using a different MDMX species or construct. | Preserve species/sequence mapping and mutations; cannot silently claim it reproduces the human context. |
| A new peptide scores well for MDM2 but MDMX is unassessed. | Dual-inhibitor status unresolved; no fabricated favorable MDMX. |
| Target binding looks favorable but CPP classifier is absent/inapplicable. | The access objective remains unassessed; do not call it a CPP-negative. |
| CPP model looks favorable but target interaction is absent. | Access proxy alone does not satisfy molecularly targeted anticancer design. |
| An ACP classifier predicts activity but TP53 context and mechanism are unassessed. | Keep prediction within its dataset-label scope; no p53-pathway antitumor inference. |
| The peptide alters p53-related cell phenotype and also disrupts membranes. | Preserve both observations; nonspecific cytotoxicity is a competing mechanism, not confirmation of targeted action. |
| Two chemical derivatives share a parent sequence but differ in staple/stereo/caps. | They are chemically distinct realizations and need appropriately attributed evaluations. |
| A linearly generated sequence resembles a known stapled reference. | Similarity is a design clue, not a complete molecule or evidence of reproducing intracellular activity. |
| A runtime lacks noncanonical-staple representation or a needed recognition oracle. | Report unsupported/limited capacity and keep the scientific request or next evaluation pending; do not manufacture success. |

## 6. Relationship to current approved PeptideMT engineering

**This case is not the commissioned increment-1 acceptance scenario.**

The immediate W0–W4 work is a **target-free** Macrel AMP/hemolysis assessment/selection increment, with D35/M1–M8 as the normative contract. HydrAMP qualification, first real learned generation, feedback and target-aware design follow as separately reviewed increments; none is implemented by adding this reference case.

The proposed MDM2/MDMX case is a **scientific compass for later target+function work**, and a rigorous test of whether extensions can preserve chemistry, multi-target roles, qualified access and cancer-context meaning. It should be referred to when selecting future engines or chemical support. Do **not** make its full noncanonical chemistry, clinical context or assays mandatory for a small sequence-only V0.1.

No new code, experiments, model weights, PDB preprocessing, structure calculations, issue, selected demonstrator or implementation authorization follows from this document.

## 7. Recommended reading and immutable scientific anchors

1. [Chang et al. (2013), ATSP-7041: dual MDM2/MDMX and p53-dependent tumor models, *PNAS*](https://pmc.ncbi.nlm.nih.gov/articles/PMC3767549/).
2. [RCSB PDB 4N5T: crystallographic MDMX–ATSP-7041 complex](https://www.rcsb.org/structure/4N5T); [entry version history](https://www.rcsb.org/versions/4N5T). Pin the **actual structure revision and downloaded coordinates** in any future implementation; this document does not freeze a local file.
3. [Mechanistic validation of cellular entry and target specificity (2016)](https://pubmed.ncbi.nlm.nih.gov/27721413/).
4. [Discovery and medicinal-chemistry optimization of ALRN-6924 (2023)](https://pubmed.ncbi.nlm.nih.gov/37439511/).
5. [ALRN-6924 phase-1 clinical evidence and its limitations (2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9401461/).

**Scientific interpretation:** this is an experimentally anchored and unusually stringent future case of a cell-permeating, target-engaging peptide with anticancer mechanism in a specific biological context. Its existence motivates a PeptideMT design capability; it does **not** establish that any current generator or generic CPP/ACP score is qualified for the actual stapled chemistry or that PeptideMT has reproduced the reported results.
