# Bioactive peptide functions and multifunctional learning

Status: **literature observations and P08 alternative 2 accepted conceptually**,
2026-10-26 (D17–D20). Family/model independence and P07 attribution remain in
force. The alternative comparison preserves reasoning; detailed field sketches
are not approved schemas, APIs, a formal ontology or implementation claims.

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

## Simple extensible function catalog: accepted concept, illustrative metadata

Treat each *function concept* as independent of the models that implement it. At the conceptual level, consider retaining:

- Human-readable name, optional stable local identifier, aliases and source-specific label mappings.
- Definition and category of meaning (activity/phenotype, access, targeting, mechanism, signaling, indication, safety or molecular/material property); multiple facets may apply.
- Context and measurement semantics when known: target organism, cell line, compartment, assay, concentration, endpoint, etc.; explicit unknowns when absent.
- References and evidence, plus typed relations such as broader/narrower, overlaps/related-to or potentially opposite. Relations must be justified, not inferred from similar names.
- Available **separate** assets: discriminative predictors, learned family-enriched proposal distributions, inference-time guidance/conditional generators and datasets, each with versions, chemistry support, annotation/negative-label assumptions, domain of applicability and output meaning.

P08 adopts this conceptual separation and extensibility, not the individual
fields or relation names listed above. This is **not** a requirement for a complete
ontology, fixed 47-type enum, one predictor per label, single calibrated model or
mandatory target. One predictor may cover several functions, one function may
have many resources, and some functions may have no qualified model. Model names,
API and registry implementation remain open.

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

**Original research-note disposition:** the inventory did not itself approve
architecture, a first demonstration, implementation, issues or classes/APIs.

The preceding inventory was initially a research note. Subsequent investigator
approval adopts P08's semantic alternative below (D17–D20), not the literature's
taxonomy, a selected demonstrator or a concrete implementation.

## P08: conceptual alternatives and generative use

Status: **alternative 2 accepted conceptually with qualifications (D17–D20)**.
The function inventory
above is evidence for breadth, not a reason to adopt its label sets wholesale.
This section develops P08 without selecting models or prescribing an API.

### Three alternatives

| Alternative | Benefit | Limitation |
| --- | --- | --- |
| 1. Catalog of model/database labels | Small initial effort; faithfully exposes each resource's vocabulary. | The same scientific request changes when a model changes. Synonyms, broader labels and incompatible source meanings become hard to distinguish. A useful import inventory, insufficient as the scientific problem's vocabulary. |
| 2. Small scientific concept catalog with qualified source/resource associations | Keeps intent stable across models, supports unknown functions and many-to-many resources, and can record overlap without a complete ontology. | Requires curation of definitions and mappings; unresolved mappings must remain visible. Excessive mandatory metadata would recreate an ontology indirectly. |
| 3. Formal ontology with inference rules and comprehensive relations | Can support rich queries and consistent hierarchical reasoning once definitions and evidence justify them. | Premature consensus, migration burden and false deductions from heterogeneous labels; unnecessary for the current design cases. |

**Accepted conceptual choice: alternative 2.** Start with short scientific definitions and
source-qualified associations only where needed by a problem or resource.
Do not require a complete catalog before a campaign or adopt a 21/47-function
enumeration. Alternative 1 remains useful for raw imports. Revisit richer
reasoning only when concrete scientific use cases require it.

### Separate scientific meaning, source meaning and computational use

The minimal scientific concept can be a name, short definition, reference or
definition provenance, and relevant context/explicit unknowns. It denotes a
function under a definition, not necessarily a homologous group or a single
compact region of sequence/feature space. Meaning facets
(phenotype, access, mechanism, signaling, etc.) can be descriptive rather than
mandatory categories. No universal assay, protein target or numeric activity
threshold is required to name a function. A concept can exist with no qualified
computational model, and a campaign can introduce a provisional definition.

A problem requests a function with its relevant context and intended direction
(promote, avoid or characterize); a generic catalog definition need not contain
every campaign's cell line or endpoint. A source label retains its own dataset
definition, curation/negative rules and conditions. An association states what
part of the requested function a resource can address, with evidence and limits.
The plan selects actual resources, operational score criteria, rewards and
aggregation. Execution records their versions, actual inputs and results under
P07. These are responsibilities, not four required software objects.

In particular, a predictor that calls a sequence CPP-compatible may provide a
limited proxy for a campaign requesting cytosolic delivery. Calling it a proxy
does not establish the desired access. A classifier's antihypertensive label
does not make it an ACE-inhibition evaluator. A source's generic antimicrobial
label can mean a residual category, as in Xiao et al., rather than the broad
umbrella concept used elsewhere. Similar wording cannot establish equivalence.

Keep source-to-concept associations qualified as equivalent within stated scope,
narrower, broader, partial/proxy or unresolved when useful; these are proposed
descriptions, not a fixed relation enum. Mapping direction matters. A source
label can cover several possible interpretations, and several labels can refer
to overlapping parts of one concept. Unknown mappings should not be guessed to
make a model appear to cover the scientific request. A changed interpretation
must remain traceable rather than retroactively changing prior outputs.

### Relations and overlap without an ontology engine

Distinguish three different claims:

- **Scientific relations:** a justified broader/narrower meaning, mechanistic
  connection, overlap or context-dependent opposition. Preserve source, direction,
  scope and uncertainty. ACE inhibition may support an antihypertensive hypothesis;
  that is not equivalence or a universal parent/child relation. Tumor homing and
  CPP concern different access/localization properties.
- **Dataset relations:** co-annotation, apparent exclusivity or missing labels
  under particular curation. Counts depend on sampling and annotation. Parent/
  child labels are not automatically two independent functional achievements.
- **Model relations:** shared features, correlated outputs, common training data
  or a learned dependency. These do not establish biological implication or
  independent corroboration. Multi-label prediction need not supply a calibrated
  joint distribution over activities.

Initially retain a small number of explanatory assertions when they affect a
decision. Do not infer activity transitively, populate a complete relationship
graph or assert mutually exclusive families from absence of co-annotations.
Conflicting source assertions can coexist with their provenance. A new relation
must not silently change a campaign's objective or double its reward.

### Six resource roles, associated rather than owned by a family

| Resource | Contribution | Qualification needed |
| --- | --- | --- |
| Individual or multi-label discriminative predictor | Scores/labels for one or several source-defined functions. | Per-output semantics/order, score versus probability, threshold, calibration evidence, input chemistry, empirical support, negatives/missing labels and provenance. |
| Learned family-enriched distribution | Proposals or a prior favoring patterns learned from family data. | Conditioning/training definition, sampling support, bias and diversity; an implicit sampler need not expose likelihoods. Sampling is not proof of membership. |
| Conditional generator | Proposals responding to supported target/function/context conditions. | Actual accepted conditions and representation, editable states/native constraints and tested combinations; no arbitrary function can be enabled by naming it. |
| Reward function | Transforms evaluations or other justified signals into a search preference. | Preserve component scores, direction/scaling, assumptions and missing-input policy; a reward is not the desired scientific function. |
| Search or guidance procedure | Uses rewards/evaluations to change proposals, trajectory allocation or sampling. | Actual intervention/access and cost must be explicit; an optimizer is not a predictor, and tree reward backpropagation need not mean gradients. |
| Dataset or evidence collection | Observations, annotations, definitions, examples or training/evaluation material. | Chemical identity/partiality, assays, sources, measured versus unannotated negatives, splits, coverage, permissions and contradictions; data availability is not an inference capability. |

Associations are many-to-many: one multi-label model is one versioned resource
with several output bindings, not 21 independent scientific resources. The same
model can be used for final evaluation or search feedback; that role is plan
specific. Several resources may address one function and disagree. A condition's
availability does not imply an independently qualified evaluator exists, nor the
reverse. Preserve scientific requirements that have no applicable resource as
unassessed; model availability must not define the scope of PeptideMT.

### Integration exercise: 21-function predictor plus a protein-conditioned generator

**Scientific problem:** retain the existing target-directed CPP/binder intent
(case A), without specifying a predictor. Other requested functions could be
added with their own meanings; unrequested outputs are not automatically desired
or forbidden. The 21 output slots do not become the platform's function list.

**Concrete precedents:** PrMFTP is sequence based; a structural target-conditioned
engine such as DiffPepBuilder operates on a target and peptide sequence/structure
proposals. Their inspected interfaces are documented in
[the integration observations](literature.md#prmftp--21-label-source-level-integration-observations).
This is a proposed composition, not a tested adapter or model choice.

First compare the generator's output and empirical domain with the predictor's
input and training/evaluation scope. Keep the scientific allowed domain separate
from the subset a plan can assess. The overlap may be narrow or empty. Length/
alphabet acceptance alone is insufficient: a modified binder, constrained fold,
unusual sequence distribution or assay context may lack supporting predictor
evidence even when its sequence can be encoded.

| Situation | Conceptual plan response | Evidence boundary |
| --- | --- | --- |
| Target generator supplies a supported complete residue sequence plus a complex | Retain the complex for recognition; derive a sequence view with recorded correspondence and evaluate the mapped function outputs. | The sequence predictor does not evaluate the complex, target specificity or the requested site mechanism. |
| Generator supplies only a backbone or partial sequence | Defer the sequence evaluation or score supported explicit completions/rollouts. | A completion's family score is attributed to that hypothesis, not automatically to its unfinished source. Geometry can be evaluated separately. |
| Realization contains a link, cap or stereochemistry absent from the predictor's input | Use a qualified projection only with explicit scientific limits, obtain another compatible evaluator, or abstain for that requirement. | Removing chemistry to encode a sequence cannot establish full-molecule function. Hypothetical completion under P07 does not fix model-domain mismatch. |
| No applicable mapping/output or no supported joint domain | Record missing coverage; use another plan or report the limitation without rewriting the intent. | Unsupported is not inactive, zero score, or permission to substitute another functional meaning. |

Input acceptance and empirically validated applicability are different. A model
outside its validated empirical domain may still be used exploratorily with a
scientific/empirical rationale and explicit uncertainty about utility. That does
not repair unsupported input encodings or establish reliable full-molecule
evidence. Preserve the difference between executable, useful-for-search and
scientifically supported assessment rather than imposing one universal gate.

The recognition result and family outputs remain separate. Family prediction is
not made target-specific merely because the sequence came from a target-conditioned
generator. A shared peptide input couples the searches operationally, not as proof
of a joint mechanistic probability. Use MolSysMT for supported molecular extraction/
conversion and maps; PeptideMT retains the design association and evaluation
attribution. No shared embedding, tokenizer, framework or differentiability is
required for a first external composition. Legacy engines may require separate
environments; launch/serialization behavior still needs qualification.

The same problem permits several intervention levels:

1. **Generate then filter/rank:** evaluate completed proposals using mapped
   outputs and recognition evidence. This is the simplest baseline and does not
   change the generator's original sampling.
2. **External multiobjective optimization:** use compatible edits/resampling and
   predictor feedback to change subsequent proposals. Reevaluate target recognition
   after sequence changes; the original pose/score is not preserved by default.
3. **Sampling-time guidance:** only if the engine exposes usable sampling access.
   Complete supported rollouts before applying a clean-sequence classifier when
   partial/noisy inputs are unsupported. The existing reviews of PepTune and NOS
   provide different precedents, not a native PrMFTP/DiffPepBuilder callback.
4. **Learned joint conditioning:** reuse qualified native conditions or consider
   adaptation/training later if evidence and cost justify it. A discriminative
   family predictor alone does not supply a target/function conditional sampler.

For backbone-first methods, the useful intervention may be inverse folding or an
outer alternating search. Nothing in a classifier adapter establishes gradients
through discrete sequence extraction or the generator's hidden states. If only
thresholded labels are available, they can support a coarse policy; continuous
rewards require access to the underlying scores and their interpretation, not
fabricated numerical precision.

### Selection, contradictions and assessment

**Accepted role distinction (D18–D19):** a resource can guide, reward, select,
evaluate candidates, or serve several of these roles. Distinguish desired
function, actual predicted property, operational search signal and available
candidate evidence. Reusing a reward model to report its own score improvements
is allowed but is not independent validation. Independent computational assessors
are useful when available; shared data can compromise that independence.

Perfect probability calibration is not a prerequisite for useful ranking or
evolutionary rewards. Empirical discrimination in the explored domain and gains
on independent criteria are relevant tests of usefulness. A justified heuristic
can be tried before such utility is established, with its status as a hypothesis
retained. Do not interpret its score as a true activity probability or compare it
numerically with arbitrary outputs from other models.

Preserve conceptual distinctions among directly evaluated properties (still
predictions when model based), indirect/partial support and unavailable evaluation.
Applicability can be doubtful for a direct or indirect output; it is an additional
question, not necessarily a higher/lower rung of one evidence ladder. No rigid
evidence-state classification or universal confidence scale is adopted.

Choose the requested subset of outputs with justified mappings; preserve the
other outputs when available without optimizing all 21 toward high activity.
Avoid rewarding broad/narrower synonyms twice or treating unrequested function
labels as negative requirements. Keep raw values and label-specific policies;
do not sum arbitrary scales or multiply marginals into a joint probability.
Objective vectors, constraints and diversity remain preferable subjects for
discussion (P04), not an adopted universal selector. Missing evidence may lead
to abstention/deferment; the plan must state how it affects search and selection.

The [current P04 analysis](evaluation_and_selection.md) tests evaluation,
feasibility, purpose-specific selection and scientific claims with A/B/C cases.
Alternative 2 and seven principles are now accepted under D27–D28. A scientific
requirement can be strict without an exact available evaluator; cutoff failure,
missing evidence, disagreement and extrapolation have different meanings. The
[X/Y selectivity case](evaluation_and_selection.md#7-selectivity-case-bind-x-while-avoiding-homolog-y)
records the accepted organization of requirements, checks and compliance
evidence under D29. The [multiobjective discussion](multiobjective_optimization.md)
compares alternative uses of family signals without adopting a scalar or Pareto
selector. Family labels or structural confidence do not by themselves establish
target selectivity, and global project interpretation stays outside PeptideMT.

Compare only sufficiently aligned subjects, chemical views, contexts and claims
before calling outputs contradictory. Keep disagreement and calibration evidence
separate from selection policy. Shared training data weaken claims of independent
confirmation. A score used repeatedly as a reward can be exploited; compare
strategies using matched budgets, coverage/diversity, independent evaluations
where feasible, and actual changes in sampling. Without assays, conclusions are
computational rather than demonstrated multifunctional activity.

For target-free tasks, omit the target/recognition requirement rather than
inventing one; the same family mappings, resources and attribution still apply.
Family priors and mixtures can seed either kind of task, but neither co-annotation
nor combining sampler densities guarantees conjunction, mode coverage or access
to candidates outside their support.

### Next discussion: how functional resources intervene in generation

P08's concept/source/resource separation and the qualifications above are accepted.
Detailed metadata, relation vocabularies, reward/selection policies, model choices,
API and registry mechanics remain open; P02/P04 are not silently closed.

The next [comparative analysis](generative_strategies.md) examines filtering,
external optimization, sampling-time guidance, combinations of distributions and
learned conditioning. It separates actual engine access, applicability, cost,
diversity and training needs. Several strategies may compete or cooperate; none
is selected as a definitive generative architecture.
