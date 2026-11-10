# Prospective scientific comparison of original and modern HydrAMP

Status: **review proposal v1; preparation commissioned, scientific choices and
execution not approved**, 2026-11-04. Scientific comparison owner:
[HydrAMP #3](https://github.com/uibcdf/hydramp/issues/3); consumer:
[PeptideMT #32](https://github.com/uibcdf/peptidemt/issues/32). Product review stays
in [HydrAMP #4](https://github.com/uibcdf/hydramp/issues/4). PeptideMT's devguide
retains the working design text; an identical copy in the owned HydrAMP worktree
supports joint review. Neither copy is an executable work order.

The investigator directs preparation after R3. This commissions research and a
concrete protocol, not adoption of the proposed cohorts, chemistry projection,
similarity rule, endpoints, margins or sample sizes. No new model loading,
inference, training, GPU, feedback, other-family work, release or author contact.
Every previous scientific allowance remains exhausted. D35/M1–M8, D41, D44 and
D45 retain their existing meanings and exact artifacts.

The first proposed pilots concern fixed-input low-MIC prediction and native
improvement analogues. De novo scientific quality, discovery/optional filters,
training and other families remain separate modules; existing de novo fidelity
evidence is reused without claiming a complete scientific review of HydrAMP.

## 1. Questions, claims and evidence to reuse

The programme asks whether the modern implementation retains the original
method's capabilities, and whether that method gives scientifically useful
proposals. These require separate verdicts:

| Question | What could establish a bounded answer? | Insufficient evidence |
| --- | --- | --- |
| Does the port implement the stated method? | Existing numerical/reference and exact same-provider receiving evidence; investigate new decision changes | Copying original approximations or hiding old FAILs |
| Do fixed-input predictions transfer? | Paired predictions on an audited measured cohort, with defined endpoints and uncertainty | Agreement with another predictor alone |
| Do proposal profiles transfer? | Matched original/modern parent, attempt and random-input comparisons, including yield, failures and adverse outcomes | Only the surviving highest-scoring children |
| Are new proposals biologically better? | Matching experimental observations on those chemical entities under the named assays | Native reward, Macrel scores or equality with original strings |

Reuse the 256-input campaign, selected FP64 reference, encoder E2, analogue A2,
H4 and installed R3 receipts. The 91/58/43 numerical-reference comparison is
about selected arithmetic errors, not measured activity of 192 peptides.
R3 repeats do not add independent efficacy observations. R3's sole candidate
improves native scores but worsens both Macrel outputs relative to its parent;
saved original A2 returns the same string. That observation motivates the
protocol; it does not condemn the port or establish either predictor correct.

Relevant existing evidence in PeptideMT: `hydramp_confidence_campaign.md`,
`hydramp_numeric_reference.md`, `hydramp_analogue_A2.md`,
`hydramp_redesign_R3_qualification.md`; R3 execution receipt SHA-256
`9fa24f007a8feca1cf504d4a8aefa2a542c8ecaab11f3aa880980ca6b1b4db1e`.
Keep their original verdicts, tolerances, identities and exhausted allowances.
Do not repeat them as an extra preliminary qualification campaign.

## 2. C0: qualify data and the scientific endpoint before any model

**Recommended immediate next work:** a model-free data/use/overlap audit. Its
deliverable is an eligibility report and proposed frozen cohort, not a claim
that an independent benchmark already exists. The sources below are candidates;
no experimental table or cohort has been qualified by this preparation.

| Candidate source | Appropriate role | Qualification still needed |
| --- | --- | --- |
| Original release/Drive/Zenodo and starter `data/training/` | Training-exposure inventory and historical regression | Archive/starter identity, exact role of each split, component-specific training/model-selection exposure and source terms |
| Original HydrAMP experimental supplements | Historical measured reference; potential fixed-input replication panel | Exact chemical entities, assays/strains/units, selection history, obtainable tables and exposure; selection by the original pipeline limits generalization |
| Deep_AMP publication and repository | Candidate external experimental material | Its 500-candidate cell-free screen and 30 functional sequences have different evidential roles; audit actual assay tables and eligibility, not only sequence filenames |
| New records from the original data sources | Possible later independent cohort | Immutable release/date, publication and sequence exposure, assay provenance and terms; a newer database date alone is insufficient |
| AMP Challenge reference sets | Named competition novelty/reference checks | They are not automatically activity-labelled tests or HydrAMP training-exposure inventories |

The pinned starter README describes `mic_data.csv` and several positive,
assumed-negative and UniProt splits. **Names such as `test` are not independence
certificates.** The inspected original MIC notebook uses `mic_x_test/mic_y_test`
as validation data during fitting/early stopping. Assumed UniProt non-AMP labels
are not experimentally inactive controls. Do not import those labels into the
measured-cohort ground truth. Source references are below.

Deep_AMP's repository exposes sequence lists and biochemical summaries. The
inspected `biochem_450tested.csv` header contains descriptors and a tag, not a
MIC endpoint column. Its paper describes a cell-free production/growth screen:
failed screening can include production/context effects and cannot silently
become an inactive purified-peptide MIC label. No quantitative concentration,
negative label or absent hemolysis value is invented from these resources.

For every candidate assay record, retain source/row ID, publication, exact
sequence/chemical-entity identity, termini, stereochemistry, modifications,
cyclization, organism/strain, medium, inoculum, duration, assay endpoint, value,
unit, censoring relation, tested range, replicates and uncertainty. Missing
required fields remain missing. Do not pool strains/conditions or choose the
lowest activity value to create a favorable label. Resolve endpoint-compatible
replicates before predictions; conflicting labels remain explicit unresolved
records, with inclusion/exclusion counts.

The inspected original notebook's MIC training label is **`value < 1.5`**. The
starter README identifies `value` as log10(MIC/µM), implying a cutoff near
31.62 µM if that provenance is confirmed. This is a training-class definition,
not a clinical breakpoint or a measured MIC output. Confirm the original
archive/units and endpoint relation before using it as cohort truth. Higher
E. coli MIC does not make a peptide a general AMP-negative example. Accordingly,
the first proposed measured comparison concerns the **low-MIC head**; AMP and
hemolysis validation require separately defined, suitable labelled cohorts.

The inspected data-preparation notebook groups E. coli records by sequence and
averages `value`. A strain-specific measurement is not automatically the same
estimand as that pooled training target. C0 must state whether the comparison
reconstructs the original aggregate or proposes strain-specific transportability,
and justify that scientific interpretation before labels are frozen. Do not
pool heterogeneous measurements after observing predictions to obtain agreement.

Preserve intervals for censored values. A primary binary label is available
only if the entire supported interval lies unambiguously on one side of the
approved strict cutoff. An upper/lower reported limit is not substituted for a
measurement. Unit conversion uses PyUnitWizard; any required molecular mass or
chemical interpretation belongs to MolSysMT and requires sufficient chemistry.
No mass-based conversion is guessed from an incompletely specified peptide.

### Chemistry and view agreement is a real entry gate

Both models consume a sequence representation; experimental activity belongs
to a chemical entity in an assay. Preserve that distinction and all original
annotations. Current PeptideMT analogue/Macrel admission rejects explicit
unassessed chemical annotation. Do not clear `SequenceRecord.chemistry`, move
an annotation elsewhere to evade admission, clip initial M, remove residues,
or silently identify modified and unmodified entities.

C0 must identify a cohort compatible with the current scientific contract, or
return a concrete separate chemistry/view proposal to the investigators before
C2/C3. This protocol does not itself authorize that extension. Unknown chemistry
cannot establish equality to a particular experimental realization. If no
sufficient admissible cohort exists, the measured comparison is deferred with
counts/reasons; a synthetic or training panel is not substituted as independent
biological evidence.

### Exposure, relatedness and cohort separation

Audit exact views against separately inventoried generator, encoder and both
native-head fitting/model-selection corpora. Inventory Macrel exposure when
interpreting its secondary predictions. Unknown or incomplete training exposure
remains **unresolved**, not clean. Archive/starter claims of common provenance
do not prove byte identity. Public availability does not settle data-use terms.

Reuse MolSysMT's public `topology.get_sequence_alignment` and
`topology.get_sequence_identity`. Its identity is query-length normalized and
directional. A guarded development-profile probe gives ACD→ACDEF=100% and
ACDEF→ACD=60%; this is documented behavior, not a defect. No local aligner,
molecular parser or alternative identity implementation is introduced.

**Proposed consumer relation, for review:** evaluate both owner directions with
the same pinned backend/options and let S(a,b)=min(I(a,b),I(b,a)). Group connected
components of edges S≥80% and keep each component in one partition; also report
exact-overlap and 90% sensitivity results without picking the best threshold
after outcomes. Retain alignment/matching indices, lengths, directions and
versions. This proposed short-peptide heuristic is not a biological independence
guarantee, not MolSysMT's default, and not the challenge's Levenshtein definition.
Graph closure can make large components; report excluded components and class
losses rather than splitting them to fill quotas. Validate computational cost
and the owner route before a full-corpus audit; this preparation ran eight
toy identity calls, not an all-versus-all homology search.

Select/split using only sources, chemistry, assay labels, stable IDs and the
approved overlap relation **before either model is loaded**. Record all excluded,
incompatible, conflicting, unresolved and missing records. A clean exact-string
comparison alone supports only exact-string disjointness. Reserve a calibration
partition for any threshold/margin design; a final comparison partition must
remain untouched by model choice, endpoint choice or acceptance tuning.

## 3. Proposed first pilots, conditional on C0 and scientific review

These are resource-conscious **exploratory** samples, not powered equivalence
studies. The sizes below are proposed; no cohort, seed campaign or call allowance
is approved. Failure to meet entry criteria returns to design before predictions.

### C2: fixed-input low-MIC prediction

Propose 128 distinct admissible sequence-relatedness components with measured
endpoint labels. Select at most one representative per component by a frozen
source/ID/content-hash rule, without model scores. Freeze the exact 128 and their
order after C0; insufficient data returns a narrower design for review. Do not
balance a natural sample to 50/50 and then claim deployment calibration. Report
class prevalence and require at least 16 per class for the proposed ranking
summary; otherwise that pilot design needs review, without replacement draws.

Use the same original checkpoint, explicit native padding/token representation,
eight fixed batches of 16 and paired original/modern scoring. Both native heads
execute, even though the measured primary endpoint is the low-MIC head. Retain
all raw scores, exact/near ties, threshold changes and ranking differences.
No rescaling, rounding, recalibration or temperature choice is fitted on these
outputs. AMP-head agreement is transfer evidence; E. coli MIC labels do not
become AMP-head ground truth. New decision deviations receive owned analysis;
do not repair modern arithmetic merely to imitate legacy approximations.

### C3: parent-conditioned proposal profiles

Propose 32 parents drawn **before C2 scoring**, from that same audited cohort:
16 low-MIC and 16 higher-MIC-class cases, distinct components. This stratification
is for behavior coverage, not a population prevalence estimate. Choose by frozen
hash within the measured strata, interleave strata and freeze four batches of
eight. Preserve source IDs/original occurrence and assay context.

For each implementation, use the same four batches and four noise blocks,
temperature 1.0, two attempts, native improvement, no optional filters or modern
descriptors. Proposed seeds 39001–39016 map in noise-block-major/batch-minor order;
the same call pair gets the same seed. Verify actual random-input correspondence
through the qualified original/modern route; a shared seed alone is not proof.
Freeze original constructor effects and observed random-state operations before
the first call. Preserve duplicate occurrences before the original dictionary
collapses them; do not alter its numerical operations.

There are 16 analogue calls per implementation, **256 raw attempted rows per arm**,
512 combined. The 32 parents and four repeated noise blocks are not 512 independent
biological samples. Keep fixed batch context, all no-hit and failure states,
incompatibilities, every raw/returned relationship, self-exclusion and within-parent
native deduplication. Identical returned strings remain separate occurrences.

Retain native generated scores on their original decoded token arrays. Do not
re-encode projected strings and overwrite those scores. Assess unchanged returned
views through the existing Macrel route, with separate parent baselines and one
retained W3 control batch; preserve initial-M/empty incompatibilities and all
negatives. The two existing selectors replay unchanged at k=4. No parent promotion,
new AMP cutoff, refill, feedback or alternative evaluator is added.

### Planning arithmetic, not execution permission

C2's paired heads require 32 network evaluations. C3 requires 32 analogue calls
×7=224 network evaluations. With sixteen-row Macrel batches, two parent batches,
up to 32 returned-child batches and one control batch add at most 35 calls/70 ONNX
evaluations: **326 neural evaluations as a preliminary upper bound**, including
both stages. Empty/incompatible pools invoke no Macrel; unused slots cannot be
reassigned. Maximum assessed occurrences are 32 parents +512 children +4 controls.

This arithmetic assumes the stated routes and sizes. Original constructor/PCA
loads, mandatory original descriptors, all other incidental work and stage-stop
semantics require an observed, exact separate execution ledger. Do not infer a
complete allowance from this estimate. The CPU-only/4 GB task RAM intent remains;
fresh installed artifact/use checks, host headroom, threads, wall/RSS/virtual
ceilings, output/disk limits and explicit investigator approval precede any load.

## 4. Outcomes and analysis fixed before a later campaign

| Layer | Proposed outcomes and units |
| --- | --- |
| Same-provider receiving | Exact input/parent/attempt correspondence, lossless native outputs, rows, provenance and saved replay; hard engineering requirement |
| C2 primary | Paired difference in low-MIC-head Brier loss: mean[(p_modern−y)²−(p_original−y)²], with both predictions on the same measured cases |
| C2 supporting | Per-implementation Brier loss, AUROC, average precision with prevalence, reliability description, fixed-threshold decisions, calibration/error by prespecified strata and missingness; no new fitted threshold |
| C3 proposal coverage | Returned/attempted counts, parent coverage, no-hit/failure categories, identical-to-parent cases, native duplicates and exact-string uniqueness within/across parents |
| C3 secondary computational endpoint | Per-parent/noise-block observed complete Macrel AMP-positive/NonHemo children per two requested attempts; paired modern−original differences, alongside assessment coverage and labels |
| C3 remaining profiles | Both native-score changes, both independent Macrel-score changes, disagreement matrix, complete selector rankings and ties, parent/child similarity and named-corpus novelty under the reviewed owner relation |
| Cost | Actual dispatched/completed calls, constructor/descriptor work, wall time and sampled/kernel memory on matched hosts; keep unlike workloads separate |

Failures/unassessed rows are not inactivity. For C2, preserve all 128 frozen cases;
if either score is absent, withhold an unqualified complete-cohort primary verdict
and show coverage/paired-complete descriptive results with missingness. For C3,
observed positive count per requested opportunity is an operational criterion;
show assessed-only rates and bounds for unresolved outcomes as well. Do not
declare those bounds measured biological probabilities. Stop on a failed
scientific stage, preserving partial results; no retry, replacement or favorable
subset selection is implicit.

For the exploratory pilot, summarize differences and prespecified stratification,
with cluster-aware uncertainty. Keep all records from one peptide-relatedness
component together; account for study/assay grouping and retain repeated draws
within their parent. A single-source panel supports only conditional inference,
not between-laboratory replication. Specify and verify the statistical backend
and resampling design in the eventual analysis plan before predictions; do not
treat individual attempts or near-duplicate peptides as independent n.

Average precision is cohort/prevalence-dependent, and a case-selected panel does
not establish population calibration. If a class or outcome is absent, mark the
corresponding metric non-estimable; do not switch the primary endpoint to a
favorable one. If C3 has no informative joint positives, retain that result and
the prespecified secondary profiles. Agreement between two poor predictors or
two poor generators is not an absolute quality qualification.

## 5. Confirmatory decisions require an additional scientific agreement

No numerical equivalence/non-inferiority margin or absolute quality floor is
adopted here. Choosing one merely because it admits the observed result would
invalidate the comparison. Investigators must justify a meaningful endpoint-
scale loss, calibration/decision consequences and acceptable missingness before
the confirmatory cohort is opened. Use a separate calibration/design source for
effect/variance planning, and derive sample size/power or target precision with
the actual cluster design. The pilot's 128/32 is not that calculation.

For a later reviewed paired-loss non-inferiority question, negative Δ favors
modern; the appropriate upper confidence bound must be below the approved
positive loss margin. Two-sided equivalence additionally needs the entire valid
interval within approved lower/upper bounds. At α=0.05, a valid paired 90% interval
corresponds to two one-sided 5% tests; do not substitute a naive row-wise interval
when grouping invalidates its coverage. A nonsignificant difference is not
equivalence. Secondary superiority searches require their own multiplicity and
confirmation plan. These are proposed statistical principles, not a new pass rule.

The final disposition has separate rows: method/receiving fidelity, fixed-input
predictive comparability, absolute predictive adequacy, proposal-profile
comparability and empirical generation benefit. A row may be supported, failed,
inconclusive or not tested; never collapse them into a general “better” badge.
No new activity/safety benefit can be concluded for unmeasured generated entities.
That question needs appropriately matched independent experimental observations
or a later separately commissioned assay study; none is authorized here.

## 6. Readiness, responsibility and relation to other proposals

The next deliverable is **C0**: source/use manifest, full exposure map, chemistry/
view review, normalized assay/interval metadata, overlap report, exclusion
waterfall and proposed labelled cohort with explicit unresolved cases. Keep the
last comparison partition sealed to model/threshold selection. If unavailable,
return the precise data/chemistry limitation rather than a counterfeit benchmark.

Only then review the endpoint/chemistry agreement, pilot sizes and similarity
policy; approve a concrete installed artifact/input/call/host work order. Later
formal equivalence requires separately justified margins, absolute-quality
criteria and confirmatory design. Current execution readiness is **false**:
there is no frozen qualified cohort, approved scientific choices or new call
budget. Preparation authorizes none of those by implication.

HydrAMP owns native inference, mathematical definitions and comparison fidelity;
PeptideMT owns the peptide question, cohort/endpoint policy, orchestration and
interpretation. MolSysMT owns molecular/sequence representation, format handling,
alignment and identity; PyUnitWizard owns unit conversion. Ackredit retains actual
scientific attribution. Reuse provider-supported tools and report an actionable
missing reusable capability to its owner. No provider defect was found in this
preparation: directional identity is explicit and the existing public API suffices
for the finite probe. Full-corpus feasibility is still unqualified.

Do not introduce generic journal/workflow/statistics infrastructure into
PeptideMT: Recorda, Praxis and other platform owners keep their existing scope.
The separate sequence-order control under PeptideMT #33 remains its own proposal;
it is not an original/modern comparator or an experimentally inactive control.
No molecular permutation helper, external scientific model or new dependency
has been added. AMP/low-MIC is the present question; CPP/general family transfer,
training and feedback remain separate scientific work.

## Sources inspected and limits

1. [HydrAMP paper](https://www.nature.com/articles/s41467-023-36994-z) and
   [public full-text record](https://pmc.ncbi.nlm.nih.gov/articles/PMC10017685/).
   Primary research reference for the original method/experimental context;
   publisher/full-text fetching was restricted during this review. No inaccessible
   supplement's assay rows are claimed verified.
2. [Original MIC training notebook at 6590d2f](https://github.com/szczurek-lab/hydramp/blob/6590d2f4c2963f25d30669052a4c4a857e0e7279/scripts/mic_classifier_training_prodecure.ipynb)
   and [data preparation notebook](https://github.com/szczurek-lab/hydramp/blob/6590d2f4c2963f25d30669052a4c4a857e0e7279/scripts/dataset_preparation.ipynb).
   Inspected as JSON/source only, never executed; local bytes/commit are recorded.
3. [Starter data README at 7804df8](https://github.com/szczurek-lab/hydramp-starter-kit/blob/7804df862872ccc6d09fe01c41bafbca194cfa31/data/README.md).
   Publisher-described corpus roles and units, not a local enumeration or
   independent-test qualification.
4. [Cell-free AMP study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10632401/) and
   [Deep_AMP README at a44465f](https://github.com/amirpandi/Deep_AMP/blob/a44465f704f3224120fd3b1c0bc2d5823a1181c8/README.md),
   with [inspected biochemical-table header](https://github.com/amirpandi/Deep_AMP/blob/a44465f704f3224120fd3b1c0bc2d5823a1181c8/data/biochem/biochem_450tested.csv).
   Read-only source/header inspection; no model, training archive or experimental
   cohort imported/qualified. Paper/source visibility does not settle data terms.
5. [Lakens, equivalence-testing primer](https://pmc.ncbi.nlm.nih.gov/articles/PMC5502906/).
   Rationale for prespecified meaningful margins and why absence of a significant
   difference does not establish equivalence; clustered implementation still needs
   an appropriate analysis design.
6. MolSysMT's [alignment](https://github.com/uibcdf/molsysmt/blob/71fbe4f46d3c70e4e973c8025f01752a8c9b1084/molsysmt/topology/get_sequence_alignment.py)
   and [identity](https://github.com/uibcdf/molsysmt/blob/71fbe4f46d3c70e4e973c8025f01752a8c9b1084/molsysmt/topology/get_sequence_identity.py)
   contracts and eight guarded toy calls. Their Biopython sequence projection
   reports Tier 2 support; this finite probe is not full provider/platform or
   full-corpus performance qualification.

The preparation receipt records source fingerprints, the guarded MolSysMT probe,
read-only workspace state and zero new neural/Macrel/PCA/descriptor calls. Old
models, profile inventories, numerical evidence and source history are preserved.
