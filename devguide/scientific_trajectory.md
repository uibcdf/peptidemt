# Scientific north star, differentiation and incremental trajectory

Status: **investigator-requested strategic assessment and proposed scientific success trajectory**, 2026-10-27. This is guidance for maintaining the original intent, **not** a newly approved release requirement, revised W0–W4 assignment, selected engine, or evidence that scientific capability already exists.

Navigation: [index](README.md) · [vision](vision_scope.md) · [V0.1 scope](v0_1_scope.md) · [worked cases](design_examples.md) · [case-guided intracellular anticancer binder](case_study_cpp_anticancer_mdm2_mdmx.md) · [roadmap](roadmap.md) · [horizons](future_horizons.md) · [decisions](decisions.md).

## 1. Original hypothesis: preserved, not replaced

The motivating scientific ambition is to **propose peptides that engage molecular targets while favoring specified bioactive functions**, potentially using learned functional knowledge to *change generation*, not only to filter completed proposals. CPP, AMP, ACP and other overlapping functions are examples, not a permanent or exhaustive vocabulary. Target-free design is also scientifically legitimate.

The general architecture did not supersede that idea; it supplied the missing scientific prerequisites:

- Independent scientific intent, computational plan, and actual execution evidence (D09).
- Incomplete peptide proposals, explicit chemical realizations and input-view attribution (D15–D16).
- Functional concepts distinct from dataset labels, predictor outputs, learned proposal distributions and search guidance (D17–D20).
- Actual, access-route-specific generative/evaluator capabilities and explicit composition, including optional protein-design engines (D21–D26).
- Assessment, scientific requirements, action-specific selection, noncompensable constraints, missing evidence, diversity, uncertainty and honest budgets (D27–D32).

**Central success question:** Can an investigator define a meaningful peptide-design problem, obtain reproducible candidate proposals from real tools, understand the evidence for each desired function and target interaction, and compare search procedures without silently changing the chemistry, scientific question or meaning of model outputs?

This is a scientific product question, not merely a Python interoperability test.

## 2. Current strengths, unknowns and the main strategic risk

| Topic | What is established | What still requires executable/scientific evidence |
| --- | --- | --- |
| Scientific architecture | Conceptual decisions D09–D32 and bounded V0.1 contracts are documented. | Real implementations may reveal semantic/API gaps requiring targeted review. |
| Family knowledge | Extensible, context-aware function/model relations are conceptually accepted. | Practical usefulness/calibration/shift limitations of particular checkpoints. |
| Engine independence | Optional capabilities and direct/composite pathways are accepted. | Installed, permitted, maintainable engines with faithful input/output mapping. |
| Chemistry | No silent inference of full chemistry from sequence; explicit realizations and views. | Operation-specific support for staples, macrocycles, termini, stereochemistry, chemical transformations. |
| Evaluation/selection | Claims, scores, constraints and purposes are distinct. | Fidelity and scientific value of actual evaluated and selected peptides. |
| Existing engineering | Central admission and starter baseline were published with reproducible CI receipts. | W0 engineering receiving completed centrally; scientific W1–W4 and M1–M8 are distinct gates and have no completed scientific evidence in this design inventory. |

**Principal strategic risk:** building excellent provenance/integration infrastructure without reaching **useful generative peptide design**. A collection of model wrappers is a useful but limited product; a scientifically grounded discovery tool must support repeatable problems, bounded proposals, qualified evaluations and interpretable improvement.

Other risks: reward-model exploitation, shared model training/negative-label bias, chemical-view information loss, invalid claims from structural confidence or classification labels, license/runtime constraints and hidden internal generator work. None is resolved merely by supporting more models.

## 3. Proposed trajectory: four scientifically meaningful milestones

These are **a strategic sequence for scientific demonstrations**, not automatic release dates, new authorizations or mandatory operations in each version. Existing approved incremental scope and governance remain authoritative.

### Milestone 1 — Real, faithful functional evaluation and selection

**Current authorized increment 1:** W0 central receiving, then W1–W4, Macrel AMP/hemolysis and exact M1–M8 under D35–D36. Preserve negative outputs, original sequence/chemistry, per-occurrence mapping, score precision, model provenance, legitimate empty and failed results, and replayable selection. Do not confuse bootstrap/CI with executed biological prediction.

**Scientific claim permitted by completion:** the implemented, qualified computational resource evaluates its supported sequence views, and PeptideMT preserves/interprets/selects from those predictions faithfully. **Not** AMP efficacy, nonhemolytic safety or generative performance.

### Milestone 2 — Real learned proposals and end-to-end generative assessment

**Accepted V0.1 direction under D33:** combine the evaluation/selection layer with **an actually executed generator or redesign engine**; HydrAMP is the first candidate to qualify after Macrel under D34, not an accepted dependency. Declare native AMP/MIC conditions, filters, biases and chemical domain. Keep source-based model feasibility distinct from installed execution.

Test a bounded generate–evaluate–select task with a simple procedural and/or fixed supplied-pool control. Count effective proposal calls, observed internal selection, quality/coverage and costs. A mock or imported candidate set alone cannot satisfy generative V0.1.

**Claim permitted:** practical generation-plus-evaluation capability and observed computational tradeoffs, not biological superiority.

### Milestone 3 — Functional evidence changes subsequent exploration

A **separately approved** feedback/search capability uses qualified evaluations to change later permitted proposals, parent selection or resource allocation. Demonstrate a genuine intervention and compare it with generate-then-filter or an uninformed control at comparable declared opportunity/cost budgets, preserving visible limits.

A higher reward score is an operational improvement, not automatically a more active molecule. Hold out assessment where justified and possible; record predictor overlap, generated-distribution drift, failure modes, novelty/diversity and uncertainty without requiring a universal independent oracle.

**Claim permitted:** a documented search procedure changed exploration and its qualified computational outcomes. Experimental claims require separate evidence.

### Milestone 4 — Joint molecular-target and functional design

This is the **original scientific north star**, not a vague distant possibility. Qualify a target-capable generator and, where possible, a separately meaningful recognition evaluator. Compare target-first, family-first and feedback/guidance strategies without equating target-conditioned generation, pseudo-perplexity, predicted complex confidence, affinity or mechanism.

A particularly instructive **later case-guided scientific reference** is intracellular MDM2/MDMX inhibition by p53-mimetic, cell-permeating stapled peptides, anchored in published ATSP-7041 and the PDB 4N5T structure. See [dedicated case](case_study_cpp_anticancer_mdm2_mdmx.md). It tests target engagement, cellular access, anticancer phenotype, TP53 context and noncanonical chemistry together.

**Critical limitation:** the selected AMP/Macrel/HydrAMP first increment does **not** implement CPP, ACP, MDM2/MDMX recognition or stapled-peptide physics. The target/CPP/anticancer example must not become an implicit W0 gate or a spurious V0.1 end-to-end claim.

The [CPP-guided project pool](cpp_guided_projects.md) adds a **graded scientific
ladder**: R8/R9 and penetratin for minimal sequence evaluation, TAT/dfTAT for
cargo and endosomal escape, **p28–p53 as a lower-chemistry first anticancer
target+CPP-like reference**, iRGD/pHLIP for conditional localization/delivery,
and cyclic CPPs and ATSP-7041 for advanced chemistry, plus
PepFect14 oligonucleotide nanocomplexes and protease-unmasked ACPPs. Different projects test
different mechanisms, rather than treating one stapled anticancer peptide as
representative of all CPPs. p28 targets **p53**, whereas ATSP-7041 targets
**MDM2/MDMX**; neither a generic CPP score nor an ACP label validates either
intracellular mechanism. All remain future case-study references.

The target milestone may proceed in parallel with a future feedback increment when a route is qualified; it need not wait for every optimizer, chemical family or structural engine to be supported.

The [canonical twelve CPP guide projects](cpp_guided_projects.md)
preserve a graded trajectory from Tat/arginine and penetratin to
**p28 as a simpler intrinsic anticancer CPP–p53 binder** and advanced
ATSP-7041 chemistry. Four [complementary cases](cpp_case_portfolio.md)
add noncovalent protein carriage (Pep-1), a fusogenic helper (GALA),
mitochondrial delivery and bacterial antimicrobial penetration.
They guide future *bounded* tests; none adds a V0.1 implementation gate.

## 4. What would differentiate a strong PeptideMT product?

1. **Scientific intent survives method substitution.** Same requested functions/targets/chemistry can be compared across plans with honest coverage gaps.
2. **Chemistry and claim fidelity.** A canonical-sequence proxy cannot masquerade as a chemically stapled or otherwise modified peptide.
3. **Search–assessment distinction.** Learned family rewards can drive exploration while their bias, training overlap and validation limits remain exposed.
4. **Comparable computational campaigns.** Native results, objectives, candidate pools, failed or reused calls, resources, and selection rationales survive policy/model changes.
5. **Usefulness to researchers.** Actual candidate generation, reproducible selection and explicit next-evaluation questions; not only abstract entity/adapter registries.
6. **Evolution without ownership creep.** Reuse MolSysMT and specialized suite/MOLI components rather than create a general molecule engine, workflow orchestrator or project claim adjudicator.

## 5. Decision gates and useful evidence

| Question at a milestone | Useful evidence | What is *not* sufficient |
| --- | --- | --- |
| Does the installed provider work? | Actual package/asset identity, direct-native comparison, live runs, observed outputs/failures. | Source inspection, import success, fake fixtures or all-skipped CI. |
| Does the computation preserve scientific meaning? | Per-subject attribution, actual chemistry/view, unrounded outputs, constraints, missing/conflicting cases. | A favorable score or a successful return code. |
| Does generation add value? | Qualified native proposals, baseline controls, yield/coverage/diversity, declared costs and repeatability. | A few cherry-picked sequences. |
| Does functional guidance change search? | Recorded later proposals/actions causally affected by prior evaluations and comparable no-feedback control. | Filtering a fixed final batch. |
| Is target-directed/anticancer behavior demonstrated? | Appropriate target, cellular-access, pathway/genotype and phenotype evidence with qualified chemical species and conditions. | CPP/ACP model labels, docking poses or optimizing a shared predictor alone. |

A completed **computational** study may truthfully report negative or inconclusive outcomes without biological assay data. A future experimental reference can make a case scientifically compelling, but a new run does not inherit its experimental results merely by resembling a known peptide.

## 6. Process and boundaries

- The **engineering W0** bootstrap has since been centrally received; its durable [archived evidence](archive/complete_w0.md) documents the previous pause and its eventual completion. W1–W4 are now delivered, and D37 accepts their exact Macrel bundle with separately recorded M1–M8 evidence. D38 now commissions preparation of the [bounded HydrAMP qualification](pending_proposals/qualify_hydramp_increment_2.md); exact bundle/use conditions and fresh host/call limits precede model execution.
- D33–D36 and M1–M8 govern V0.1's commissioned increment. Nothing in this strategic note authorizes extra issues, engines, installations, scientific code, model training or package publication.
- Future horizons include macrocycles, delivery, multi-state/allosteric recognition, chemistry-aware transformation, active learning, library design and more; see [future horizons](future_horizons.md). These need capability-specific scientific review when prioritized, **not** a new up-front general architecture round.
- Codex will implement approved operations and return measured evidence. Investigators retain authority over claims, scientific meanings, permitted transformations and meaningful policy changes.

**Recommended guardrail:** evaluate progress not only by repository conformance, number of adapters or number of generated candidates, but by the next *real scientific operation* that the project can execute and interpret reproducibly. Preserve the joint target/function goal as an explicit near-term scientific trajectory even when the first engineering increment is deliberately target-free.
