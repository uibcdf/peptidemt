# Bioactive peptide functions and multifunctional learning

Status: **verified literature observations and proposed design implications**, 2026-10-26. This is a research catalog, **not** an approved peptide-function ontology, an implementation inventory or a frozen scope.

Navigation: [index](README.md) · [learned functional spaces](literature.md) · [scope](vision_scope.md) · [open questions](open_questions.md).

## Why this document exists

PeptideMT must not be architected around just CPP, AMP and ACP. Published **multi-label** peptide predictors routinely learn many functional annotations at once. Functions may be used as (1) discriminative prediction targets, (2) sources of family-enriched proposals/distributions, or (3) conditions/rewards guiding target-directed or target-free generation. These are distinct model capabilities, not interchangeable API guarantees. A function does not require a known protein-binding mechanism; a requested molecular target is nevertheless central to many PeptideMT use cases.

A function label is not necessarily a homologous/evolutionary peptide family. Labels in published databases mix phenotypes, therapeutic indications, host/pathogen contexts, molecular mechanisms, access/delivery, signaling, safety outcomes and physicochemical/material behavior. They may overlap, nest, and depend on assay conditions. Model labels should not silently become universal biological truths.

## Published multifunctional predictors: distinguish coverage from validation

| Work | Year | Reported functional coverage | Evidence and caveat |
| --- | --- | --- | --- |
| [MultiPep](https://doi.org/10.1093/biomethods/bpab021) | 2021 | **20** bioactivity classes | Hierarchical multi-label classifier. Do not confuse its 20-class scheme with the PrMFTP benchmark. |
| [PrMFTP](https://doi.org/10.1371/journal.pcbi.1010511) | 2022 | **21** therapeutic function labels | Initial 22 types included chemotactic peptide (CP), discarded because of insufficient data; the remaining 21 form the benchmark. |
| [ETFC](https://doi.org/10.1093/bioinformatics/btad334) | 2023 | **21** labels | Multi-label predictor; uses the same broad benchmark lineage rather than demonstrating 21 new independent activity data sources. |
| [MFTP_MFFP](https://doi.org/10.1371/journal.pcbi.1013622) | 2025 | **21** labels | Multi-feature, imbalance-aware classifier; reports using PrMFTP benchmark data. Some label wording in its exposition differs; map semantics against original records, not acronyms alone. |
| [SeekTP](https://doi.org/10.1093/bib/bbaf569) | 2025 | Starts with **21** annotations from PrMFTP | Class imbalance/limited data necessitate a narrower main evaluation; never imply uniformly reliable prediction of all 21. |
| [SA-MTP](https://doi.org/10.1093/bib/bbag361) | 2026 | **15** therapeutic function categories in its benchmark | Structure-aware multi-label predictor. Its classes are not automatically identical to Xiao et al.'s 15 *major* dataset categories. |
| [Xiao et al., Scientific Data](https://doi.org/10.1038/s41597-025-05528-1) | 2025 | **15** major categories and **47** labels/subcategories | *Dataset*, not a trained 47-output predictor; includes 32 named specific subcategories and 15 generic/unspecified labels. |

The models' apparent number of outputs does not establish calibrated probabilities, broad chemical support, applicability to generated sequences, validated multimodal function or independent confirmation. Publications that reuse PrMFTP data are not independent dataset replications. Licensing, model weights, availability, software environment, training splits and practical reuse remain to be audited before choosing adapters.

### The 21 retained PrMFTP labels

These are **published label names**, not a proposed canonical PeptideMT vocabulary. Abbreviations are dataset-local and can collide with other biological acronyms.

| Label | Code | Label | Code |
| --- | --- | --- | --- |
| Antiangiogenic | AAP | Antibacterial | ABP |
| Anticancer | ACP | Anticoronavirus | ACVP |
| Antidiabetic | ADP | Antiendotoxin | AEP |
| Antifungal | AFP | Anti-HIV | AHIVP |
| Antihypertensive | AHP | Antiinflammatory | AIP |
| Anti-MRSA | AMRSAP | Antiparasitic | APP |
| Antitubercular | ATP | Antiviral | AVP |
| Blood-brain-barrier-penetrating | BBP | Biofilm-inhibitory | BIP |
| Cell-penetrating | CPP | Dipeptidyl peptidase IV inhibitory | DPPIP |
| Quorum sensing | QSP | Surface binding | SBP |
| Tumor homing | THP | | |

Source: [Yan et al., PrMFTP, dataset methods and Table 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC9499272/). The initial 22nd class, chemotactic peptides (CP), was removed on dataset-size criteria; it is a legitimate candidate function for future coverage, not an evaluated output of that model.

## The 2025 expanded dataset: 15 broad categories, 32 specific subcategories

[Xiao et al. (2025)](https://www.nature.com/articles/s41597-025-05528-1) report **58,583** compiled therapeutic peptide records, **21,130** classified as multifunctional under their non-subordinate-label criterion, and **54,722** with structural annotations (the latter include predicted structures). They compiled from UniProt and 32 other public databases/datasets. Dataset [Figshare DOI 10.6084/m9.figshare.28691885](https://doi.org/10.6084/m9.figshare.28691885), version 4 (2025-06-07), is listed as CC BY 4.0. Check original source licenses and record-level reuse conditions separately if redistributing derivatives.

The published **47** labels consist of **32 specified functions + 15 major-category generic/unspecified labels**; they are *not* 47 mutually exclusive functional families. Unlike a conventional multilabel benchmark, the paper's 'multifunctional' count excludes mere ancestor/descendant label pairs.

| Major category (15) | Named specific subcategories in this resource |
| --- | --- |
| Antibacterial | Anti-Gram-positive; anti-Gram-negative; antitubercular |
| Antifungal | None specified as an additional named subcategory |
| Antiparasitic | Antimalarial; antitrypanosomal; antileishmanial; antiplasmodial |
| Antiviral | Anti-HIV; anti-HCV; anti-SARS; anti-HSV; anti-MERS-CoV |
| Antimicrobial (generic) | No additional named specific subtype; other pathogen-related major categories are separated by this resource's convention |
| Immunoactive | Antiinflammatory |
| Anticancer | Anti-breast-, anti-cervical-, anti-colon-, anti-lung-, anti-prostate-, anti-skin-, anti-liver-cancer; antiangiogenic |
| Antihypertensive | No additional named specific subtype |
| Thrombolytic | No additional named specific subtype |
| Neuropeptide | Analgesic; opioid |
| Antioxidant | No additional named specific subtype |
| Metabolic regulatory | Lipid metabolism; glucose metabolism |
| Growth/regeneration | Growth regulatory; angiogenic; osteogenic |
| Cell communication | Quorum sensing |
| Drug delivery | Cell penetrating; blood-brain-barrier penetrating; tumor homing |

Some major categories above receive only their generic label in the published 47-category scheme. The dataset limits sequence length to 2–50 residues and includes modifications/HELM metadata, but not every chemical species or activity assay is equally well supported. The authors performed **sequence** deduplication; that is insufficient to establish chemical identity for peptides with different caps, chirality or links, and it does not guarantee homology-, source- or temporal-leakage-free benchmarks. Their aggregate “experimentally validated therapeutic peptides” descriptor must not be read as direct evidence of **every** assigned function for every peptide under the same conditions.

## Additional functional concepts beyond those benchmarks

The following are **scope candidates for future evidence mapping**, *not* classes already supported by a single published 21- or 47-label model: peptide hormones and receptor agonists/antagonists; enzyme inhibitors such as ACE, renin, DPP-IV, alpha-amylase, alpha-glucosidase; anticoagulant/antithrombotic and thrombin-inhibiting peptides; immunomodulators; chemotactic and signaling peptides; surface/mineral binders; self-assembling peptides; antifreeze peptides; sensory peptides (e.g. bitter/umami); and toxicity/hemolysis as frequently *undesired* rather than desired outputs. Specific sources, datasets, activity definitions and model availability require individual verification before catalog inclusion as qualified computable objectives. Mechanistic and indication labels should not automatically be placed at the same semantic level.

## Proposal: simple, extensible function catalog (not yet adopted as a schema)

Treat each *function concept* as independent of the models that implement it. At the conceptual level, consider retaining:

- Human-readable name, optional stable local identifier, aliases and source-specific label mappings.
- Definition and category of meaning (activity/phenotype, access, targeting, mechanism, signaling, indication, safety or molecular/material property); multiple facets may apply.
- Context and measurement semantics when known: target organism, cell line, compartment, assay, concentration, endpoint, etc.; explicit unknowns when absent.
- References and evidence, plus typed relations such as broader/narrower, overlaps/related-to or potentially opposite. Relations must be justified, not inferred from similar names.
- Available **separate** assets: discriminative predictors, learned family-enriched proposal distributions, inference-time guidance/conditional generators and datasets, each with versions, chemistry support, annotation/negative-label assumptions, domain of applicability and output meaning.

This is **not** a requirement to create a complete ontology, a fixed 47-type enum, one predictor per label, a single calibrated multi-label model or a mandatory target for every task. One predictor may cover several functions, one function may have many predictors, and some functions may have no qualified model. No model names/API/registry implementation are approved here.

## Scientific and computational safeguards

1. Separate **observed positive**, **measured negative**, **synthetic/sampled negative**, **unannotated** and **unknown/not-assayed** data. Absence from a source database is not an activity-negative observation.
2. Distinguish **hierarchical overlap** (antiviral/anti-HIV), **co-annotation**, and **independent multifunctionality**. PrMFTP and Xiao datasets use different curation and counting conventions.
3. Preserve organism, assay and chemical scope; a generic ACP label is not evidence of target- and genotype-specific response. CPP classifier score is not cytosolic delivery.
4. Distinguish classifier output s_F(x), learned proposal q(x|F), and conditioned generation q(x|target,F); these are not mathematically or methodologically interchangeable.
5. Beware class imbalance, training-set contamination among reused benchmarks, sequence-family leakage, dataset selection bias and reward-model exploitation. Never multiply marginal model outputs and call the result a joint calibrated probability without a justified probabilistic model.
6. For generation + prediction workflows, log what representation/chemistry an evaluator **actually saw** (including projections from modified peptides) and never transfer a sequence-only prediction to all chemically distinct candidates without qualification.
7. Review each model's license, reproducibility, compute and performance **per label** before treating its output as an actionable search objective. A model may abstain when outside its applicability domain.

See [literature.md](literature.md) for the existing negative-data examples and proposed search comparisons.

## Architecture stress tests and research questions

The [worked cases](design_examples.md) now include three target-directed examples
and a developed target-free CPP + AMP case, followed by brief probes prioritized
for distinct semantic failure modes. They remain **insufficient** to exhaust
this breadth. Conceptual stress tests (none selected for experiments):

- **CPP + AMP without a defined molecular target**, to ensure target-free, multi-family generation is genuine.
- Antiparasitic + target recognition (e.g. a trypanosomatid protein), testing organism context and a chosen mechanism.
- Antiviral + inhibition of a specific viral protein, testing activity-versus-recognition semantics.
- Antiinflammatory + immunomodulatory, testing overlapping or non-independent label definitions.
- Tumor homing + CPP + ACP + target recognition, testing multiple functional modalities and context.
- ACE inhibition + antihypertensive potential, testing a mechanistic label nested within a physiological claim.
- Protein binder + low hemolysis, testing a desired function plus avoidance of an undesirable phenotype.

Questions to resolve in discussion: What minimal label/family semantics must be fixed before a first adapter? How do source-specific labels map to shared concepts? What hierarchy is useful without overengineering? What counts as a real joint-function observation? How do we compare independent predictors with multi-label models when source datasets overlap? How can family distributions seed target-conditioned generation without collapsing diversity?

**No new architecture approval, first demonstration, library implementation, development issue or class/API decision is implied by this research note.**
