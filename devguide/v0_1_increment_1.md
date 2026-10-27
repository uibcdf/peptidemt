# Increment 1 specification and bounded HydrAMP qualification

Status: **increment-1 scientific contract, conservative preprocessing, both
selectors and M1–M8 accepted under D35; scientific design closed within its
provisional scope**, 2026-10-27. D36 authorizes W0–W4 with W1 gated on completed
W0. Exact Macrel assets, terms, fixtures, environment and effective limits must
be identified before actual qualification. HydrAMP remains a candidate outside
this scientific assignment, and package publication remains excluded. Normal
owning-issue reporting follows [the governance map](governance.md); it does not
expand the approved scientific work.

Navigation: [index](README.md) · [decisions](decisions.md) · [V0.1 scope](v0_1_scope.md)
· [owner audit](integration_audit.md) · [working agreement](design_methodology.md)
· [commissioning/readiness brief](increment_1_work_order.md).

## 1. Approved scientific task and evidence boundary

The first bounded coverage is **desired AMP compatibility and adverse hemolysis**.
Both retain their model-specific predictive meaning. Neither output measures MIC,
experimental percent hemolysis or safety. This task does not define PeptideMT's
permanent function catalog. The core remains independent of AMP, Macrel and HydrAMP.

Increment 1 evaluates externally supplied proposals and makes reproducible
computational selections. It does not generate peptides, establish target
recognition, predict arbitrary chemical variants or accept candidates as biologically
satisfactory. Increment 2 still requires actual learned generation/redesign.

Source snapshots were rechecked on 2026-10-27; they remain unchanged. Macrel's
source version is **1.6.1** at
[`8c1f7321`](https://github.com/BigDataBiology/macrel/tree/8c1f7321618ccde2a28b960d32525620d2c737e3),
not a selected package release or proof of a usable installation. Key contracts:

- [Feature-input and skip behavior](https://github.com/BigDataBiology/macrel/blob/8c1f7321618ccde2a28b960d32525620d2c737e3/macrel/AMP_features.py).
- [Native normalization and feature calculation](https://github.com/BigDataBiology/macrel/blob/8c1f7321618ccde2a28b960d32525620d2c737e3/macrel/macrel_features.py).
- [Classifier calls, labels and length warning](https://github.com/BigDataBiology/macrel/blob/8c1f7321618ccde2a28b960d32525620d2c737e3/macrel/AMP_predict.py).
- [Peptide-mode call and rounded CLI export](https://github.com/BigDataBiology/macrel/blob/8c1f7321618ccde2a28b960d32525620d2c737e3/macrel/main.py).
- [Upstream feature tests](https://github.com/BigDataBiology/macrel/blob/8c1f7321618ccde2a28b960d32525620d2c737e3/macrel/tests/test_features.py)
  and [prediction tests](https://github.com/BigDataBiology/macrel/blob/8c1f7321618ccde2a28b960d32525620d2c737e3/macrel/tests/test_predict.py).

These sources establish observable behavior, not our runtime or scientific
qualification. Publisher access to the main Macrel article and AmPEP article
failed in this review; no training-length distribution is inferred from that
absence. The implementation evidence below remains directly inspectable.

## 2. Input, chemistry, length and attribution contract

### 2.1 Supplied proposals and evaluated views

**Accepted initial entry representations:** ordered records containing complete
one-letter sequence proposals, and amino-acid FASTA records. Preserve each original
record, full source header, occurrence and any supplied chemical/context metadata.
Multiline FASTA joining is a declared formatting operation; DNA translation,
structure-to-sequence inference, molecular completion and chemical editing are
outside this first route. No fixed Python types or identifier scheme is adopted.

The provider view uses uppercase `ACDEFGHIKLMNPQRSTVWY`. Reject ambiguous symbols,
stops, gaps and inline modification syntax at the affected operation, with an
explicit reason. Do not silently uppercase lowercase text that might encode
stereochemistry, delete characters or substitute residues. Empty records are
accounted for even if not submitted to Macrel. An empty collection is different
from a collection containing an empty sequence.

This is a sequence-view calculation. No all-L/free-terminal chemical realization
is manufactured from an unspecified proposal. Supplied D residues, cyclization,
crosslinks, terminal modifications or other chemistry are preserved; the first
route does not automatically project them away and rank their parent molecules.
A user-authorized projection could later be evaluated explicitly with limited
attribution, but is not part of the accepted default. Standard cysteine symbols
do not specify disulfide connectivity. A sequence-only result is not evidence for
every realization or molecular state.

### 2.2 Critical native preprocessing: initial methionine

Macrel's `normalize_seq` removes one leading `M` and a terminal `*` before feature
calculation. That changes the peptide sequence; its name does not make it a
chemistry-preserving operation. The FASTA parser also keeps only the first header
word by default. Both facts affect attribution.

**Accepted conservative contract under D35:** execute the native feature/predict
route only where preprocessing preserves the supplied residue sequence. For a
leading-M proposal, retain the original and report this route as unable to evaluate
it without a sequence-changing transformation. This is a route limitation, not
a declaration that methionine-containing peptides are scientifically invalid.
Single-M input also exposes an indexing risk in the inspected normalizer after
removal; this is source reasoning, not a reproduced crash.

Deferred alternatives requiring specific future qualification are (a) explicitly create/evaluate the
clipped derived proposal with ancestry and no automatic score attribution to its
parent, or (b) qualify a route using Macrel's existing `compute_all` on the unchanged
sequence. Option (b) changes preprocessing relative to the native FASTA/training
path; it cannot inherit qualification automatically. The AMP
[training preparation](https://github.com/BigDataBiology/macrel/blob/8c1f7321618ccde2a28b960d32525620d2c737e3/train/build-AMP-table.py)
also calls `fasta_features` and its normalizer. Do not copy or patch feature
formulas into PeptideMT. D35 excludes both alternatives from increment 1; this
preprocessing choice is settled, not an obstacle requiring another design round.

### 2.3 Length: no invented supported interval

| Evidence | What follows, and what does not |
| --- | --- |
| Classifier code describes development/testing on peptides **<100 residues**. | This is the inspected declared short-peptide envelope, not a model architecture limit or validation for every shorter sequence. |
| Warning fires only at **>=110 residues**. | Lengths 100–109 can run without the warning while lying outside that stated envelope. Warning absence is not applicability evidence. |
| Feature vectors have fixed dimension from variable-length sequences; upstream tests include one-/two-residue examples. | There is no inspected padded-input cap or evidence-based minimum length here. Computational acceptance of an extremely short input does not establish predictive usefulness. |
| Training scripts identify source datasets but do not establish a qualified per-head length distribution for the selected installed assets. | Minimum/maximum and sparsity of training/test lengths remain to verify if accessible and permitted. No arbitrary 8-, 10- or 25-residue lower cutoff is proposed for Macrel. |

**Accepted provisional operational rule:** record original/evaluated length and the
specific evidence scope for both heads. Rank only sequence-preserving, otherwise
compatible views within the declared <100 envelope under the exploratory policies
below; make the unknown lower empirical coverage explicit. This is a conservative
operational scope, **not a claim that all lengths 1–99 are biologically qualified**.
Lengths >=100 are retained as outside this first ranking scope, without truncation.
Any optional diagnostic execution outside it requires explicit configuration and
attribution and is not required for increment 1. Practical file/count/memory limits
are execution budgets, not scientific length limits.

Before declaring a narrower scientifically supported interval, qualify each head
against the selected assets' documented data and actual boundary fixtures. If
training data cannot be obtained permissibly, record the unresolved coverage and
scope the support claim accordingly; do not invent a numerical boundary.

## 3. Evaluation outputs, mapping and provenance

### 3.1 Meaning and precision of native prediction outputs

The accepted contract uses the native Python prediction result with `keep_negatives=True`;
this preserves precision and native labels rather than relying on rounded CLI
exports. This is one version-qualified access route, not a stable upstream API
promise. Native extraction/scoring must remain Macrel-owned.

| Output | Required preserved meaning |
| --- | --- |
| Row/access index | Provider-side row identity mapped to an input occurrence; not molecular identity. |
| `Sequence` | Actual sequence used for feature/scoring, compared with the submitted view. A mismatch is not silently accepted. |
| `AMP_probability` | Native classifier output for class `AMP`, dimensionless, nominally in [0,1]. Preserve its name and value; calibration for our candidates is unestablished. Not MIC, measured activity or a universal probability of AMP function. |
| `is_AMP` | Native boolean from **score >0.5**, retained for every evaluated input. Exactly 0.5 is false. This is Macrel's decision rule, not a biological cutoff adopted by PeptideMT. |
| `Hemolytic_probability` | Native classifier output for class `Hemo`, dimensionless, nominally in [0,1]; no concentration, percent lysis or universal safety interpretation. |
| `Hemolytic` | Native `Hemo` if score >0.5, otherwise `NonHemo`, with the same boundary qualification. |
| `AMP_family` | Native ADP/ALP/CDP/CLP composition categories, derived from acidic/basic feature comparison and cysteine presence. They do not establish folding, disulfides, mechanism or independent functional families; preserve even when `is_AMP` is false. |

Retain all native columns and diagnostic/artifact references. Unexpected columns
are preserved without silently assigning scientific meanings. The feature path
uses 22 ordered descriptors and converts model inputs to float32; this does not
prove the dtype/precision of every returned value. Record observed output dtype
and preserve native numeric values without decimal rounding. If serialized,
round-trip those values without changing selection. The CLI's three-decimal export
is a distinct quantized view; a displayed 0.500 cannot reconstruct the original
label or higher-precision ordering. Derived displays never overwrite originals.

Feature assumptions (including charge at the provider's fixed pH and its native
hydrophobic-moment configuration) are computational settings, not experimental
assay conditions. Do not expose them as MolSysMT-independent general measurements
or confuse predictor features with measured properties.

### 3.2 Every input occurrence is accounted for

Use an unambiguous **run-local correspondence** for each occurrence, independent
of repeated FASTA headers or identical sequences. Exact identifier syntax is an
implementation choice; global canonical identity remains open. Preserve original
headers separately from provider-safe row tokens. A repeated sequence may reuse
a justified calculation while retaining both origins and one evidence source.

Before scoring, record admissible and incompatible inputs. After scoring,
reconcile every provider row to exactly one submitted view. Never join by a
possibly duplicated header, deduplicate silently or zip mismatched rows by order.
Unexpected, duplicate or missing provider rows are retained as anomalous output;
unreconciled values cannot enter selection. A batch failure does not produce a
negative prediction. A mixed batch may retain individually verified results;
unresolved rows keep their actual failure/incompatibility, without fabricated scores.

Distinguish: unsupported input; unavailable selected provider/assets; transitive
import/load failure; feature/scoring failure; malformed output; timeout; and
completed evaluation. These are required distinctions, not a universal state enum.
Both classifier heads share one native invocation; report its actual cost, not two
independent experiments. No native per-head partial result is invented if the
routine fails before returning it.

An empty pool returns an empty result without loading a model, explicitly recording
that no provider ran. An all-incompatible pool accounts for every record similarly.
Neither can pass the real-provider acceptance gate.

### 3.3 Reproducibility record

For each actual evaluation retain the proposal/view mapping, original chemistry
and unknowns, transformations, assumptions and length/applicability qualifications;
distribution/build/version and import origin; source pin if relevant; both model
asset paths/cryptographic digests and available provenance/terms; access route,
feature/preprocessing identity, native configuration and CPU execution provider;
Python/platform/dependency versions; native outputs/labels, warnings/failures,
timing and observable reuse. This is an obligation, not a storage schema.

Do not infer assay organism, strain, red-cell species, concentration, incubation
or experimental pH from the runtime configuration. Preserve supplied context and
state what the classifier cannot condition on. An updated model produces new
evaluations; it does not rewrite old scores. No uncertainty interval or global
confidence is manufactured when the provider supplies none.

## 4. Two accepted reference selection policies

Both policies operate on a named evaluation snapshot and the **same supplied
proposal occurrences**. Eligibility requires sequence-preserving attribution,
the agreed provisional operational scope, and both finite comparable scores from one
qualified bundle. Exclude unresolved/failed/incompatible rows from ranking while
retaining them with reasons. No score imputation, calibration, averaging across
resources, native-label gate or biological acceptance threshold is implied.

| Policy | Exact ordering |
| --- | --- |
| **AMP-first** | Higher native AMP score; then lower native hemolysis score; then earlier original input occurrence for exact numerical ties. |
| **Hemolysis-first** | Lower native hemolysis score; then higher native AMP score; then the same stable tie rule. |

Return at most the declared nonnegative count k; k=0 is a valid empty selection.
Preserve full rankings, selected/unselected occurrence references, eligibility
reasons, priority order, precision, tie rule and requested count. Identical sequences
can occupy multiple positions because this first policy selects input occurrences;
report that explicitly, with no chemical uniqueness/diversity claim. A later
deduplication/diversity policy requires its own meaning and can coexist.

Lexicographic preferences are intentionally simple: the second objective only
breaks ties, and a very poor secondary score is not automatically disqualifying.
Thus these policies compare computational priorities; **neither is a synthesis,
nonhemolysis or safety approval policy**. They can return no candidates. Changing
policy preserves original evaluations. Changing a biological requirement needs
scientific agreement rather than a hidden change in ordering.

**Invented acceptance fixture, not model output or scientific data:** input order
Q1, Q2, Q3, Q4, Q5; k=2; the first four otherwise meet operational eligibility.

| Occurrence | AMP score | Hemolysis score |
| --- | --- | --- |
| Q1 | 0.90 | 0.80 |
| Q2 | 0.40 | 0.10 |
| Q3 | 0.90 | 0.20 |
| Q4 | 0.90 | 0.20 |
| Q5 | 0.95 | Missing |

Expected AMP-first order: Q3, Q4, Q1, Q2; selection Q3/Q4. Expected hemolysis-first
order: Q2, Q3, Q4, Q1; selection Q2/Q3. Q5 remains unranked without imputation.
Q3 precedes Q4 by the stable occurrence rule. Q2 demonstrates that the accepted
hemolysis-first selector can select a native AMP-negative result; that is an
explicit computational preference, not acceptance of AMP function. If investigators
want an additional eligibility gate for a particular action, it must be specified
separately rather than silently added to these tests.

## 5. Acceptance specification for increment 1

The following tests are **accepted under D35, not run**. Semantic fixtures and real-provider
evidence have different purposes; a mock-only suite cannot qualify this increment.

| Test | Pass criterion |
| --- | --- |
| **M1 — installed native parity, required** | In the designated real Macrel environment, run direct upstream extraction/prediction and the adapter on the same permitted fixtures/assets, with negatives retained. Reconcile sequences, all labels/categories and both scores; use the same unrounded values. Verify distribution/import origin and execute both ONNX heads. Missing/shadowed/skipped provider cannot pass. |
| **M2 — positive and negative outcomes, required live** | A small frozen upstream-derived fixture covers native AMP true/false and Hemo/NonHemo outcomes, without requiring all joint combinations. All rows survive with both outputs. Record each fixture's source, terms, actual native reference output and asset identity. Model-positive/negative is not experimentally active/inactive. Do not invent expected values before the run. |
| **M3 — mapping** | Repeated sequences, repeated/full FASTA headers, reordered provider rows and a mixed compatible/incompatible pool preserve per-occurrence correspondence. Missing/extra/duplicate output rows cannot acquire another subject's score. Controlled malformed-output fixtures complement native cases. |
| **M4 — chemistry and preprocessing** | Leading M, terminal/internal stop, lowercase/ambiguous symbols, empty sequence, partial proposal and explicitly modified chemistry produce the approved attribution/incompatibility behavior. A normalizer-induced sequence change is never an unmarked score on the original. |
| **M5 — length boundary** | Qualification-only direct native probes cover permitted fixtures below/at the reported 100 boundary and the 110 warning boundary, plus very short upstream fixtures. Record operational output/failure versus applicability separately. Controlled boundary strings test behavior only, not new activity support or an ordinary out-of-scope execution route. No truncated sequence is scored as the original. |
| **M6 — output validity and precision** | Detect nonfinite/out-of-range scores, missing fields, row/label mismatches and changed sequence views. Native score-to-label consistency uses unrounded values and strict >0.5. A controlled exact-0.5 case tests the rule; it does not claim a natural model output. Serialization/display preserves native values/ranking. |
| **M7 — two selectors and replay** | On one unchanged pool, both exact ordering rules, k=0, ties, short/empty eligible sets and duplicated occurrences give the specified outputs. A small explicitly invented score fixture demonstrates differing choices. Replaying saved evaluations requires no live Macrel execution or model installation. |
| **M8 — failures and emptiness** | Empty/all-incompatible pools record no provider execution. Missing assets/provider, transitive failure, corrupt output and bounded interruption retain truthful reasons and partial verified results; no fallback or synthetic prediction. Controlled faults are acceptable here, separately labeled from live evidence. |

For M1, first require identical retained values against the direct result in the
same environment. If separate native calls expose numeric variation, record it
and propose a justified tolerance **before** declaring parity; any change affecting
labels, ties or selected candidates needs review. A tolerance must not conceal
changed preprocessing/assets. No fixed cross-platform equivalence is claimed.

Qualification must identify the exact permitted fixtures and coverage for both
heads, not merely run tests named 'prediction'. Provider-reported metrics or an
all-skipped CI run are insufficient. Ordinary lightweight tests can omit large
external resources with explicit reasons; a designated installed-provider gate
must actually run them. Completion means computational integration within the
declared scope, not biological validation. Actual execution of these accepted
gates remains pending; approval is not a pass result.

## 6. Bounded HydrAMP contract and qualification plan

The initial candidate is native de novo `unconstrained_generation`, with
`mode='amp'`, `filter_out=False`, `n_attempts=1`, bounded positive `n_target`,
explicit seed and `properties=True`. Propose qualifying the softmax decoder
configuration explicitly; no checkpoint or constructor setting is adopted by D34.
Source:
[`HydrAMPGenerator` at 6590d2f4](https://github.com/szczurek-lab/hydramp/blob/6590d2f4c2963f25d30669052a4c4a857e0e7279/amp/inference/inference.py).

### 6.1 Four distinct layers of decisions

1. **Generative conditioning:** the inspected AMP mode sets both native AMP/MIC
   conditioning inputs positive, samples latent vectors, applies the saved PCA
   inverse transform and decodes discrete residue tokens. This is learned
   family-directed generation, not an unconditional baseline or protein-target
   conditioning.
2. **Native scores/decisions:** the chosen branch exits the accumulation loop
   after its batch. One attempt makes selection among repeated decodings trivial,
   but token argmax, internal AMP/MIC scoring and, with `properties=True`, descending
   AMP-score ordering remain. Preserve that returned order; do not describe it as
   the original latent-sampling order. No native AMP/MIC threshold/physicochemical
   quota filtering is used by this branch, but it is not devoid of internal decisions.
3. **Macrel assessment:** a new, separately attributed invocation on each compatible
   returned sequence view. HydrAMP's `amp` and Macrel's `AMP_probability` are
   different evaluations; no averaging, interchangeability or independent-validation
   assumption follows.
4. **PeptideMT selection:** the declared downstream policy uses its named evaluation
   snapshot; it neither overwrites native order nor becomes generative feedback.

Native `mic` is an internal learned low-MIC compatibility/classifier score, not
a numerical MIC in micromolar units. Record exact checkpoint label/normalization
meaning during qualification. The decoder's 25 positions and
[`translate_peptide`](https://github.com/szczurek-lab/hydramp/blob/6590d2f4c2963f25d30669052a4c4a857e0e7279/amp/utils/generate_peptides.py)
omit zero-coded positions when forming a string; a native classifier may have seen
the original padded token layout rather than a fresh re-encoding of that string.
Retain this attribution/observability limit unless actual token arrays are exposed;
do not assert representation equivalence automatically. A generated string does
not fix termini, chirality or crosslinks.

Preserve all returned rows, duplicate proposals, native `amp`/`mic`, order and
additional native length/hydrophobicity/moment/charge/pI descriptors with their
provider configuration. They are not substituted for MolSysMT general molecular
properties. Empty/noncanonical/unexpected-length output, inconsistent descriptor
length, nonfinite scores, malformed shape or fewer/more rows than requested must
be recorded and quarantined as appropriate. Never silently repair, discard,
refill or relabel them as valid generated candidates. Distinguish malformed
output from a valid completed empty result and timeout without returned data.
Useful partial outputs can survive with explicit run incompleteness. No claim
about all hidden decoder states or rejected work is made.

### 6.2 Qualification gates, with a small execution budget

No gate below has been executed. Approval of this plan and actual environment/
resource limits is required before future execution.

| Gate | Required evidence and pass/reconsider outcome |
| --- | --- |
| **H0 — permitted artifacts and deployment** | Identify code, decoder/encoder/native classifiers, PCA artifact, provenance, digests and separate applicable terms. The original/starter code is MIT; visible weights/data provenance is not a blanket redistribution determination. Resolve use and planned distribution rights. Reject or narrow the route if permissions are incompatible or unresolvable for intended use. |
| **H1 — isolated environment** | Test one exact source/asset/environment bundle. The official starter requires Python >=3.8,<3.9 and legacy TensorFlow/Keras dependencies. Keep those out of the main PeptideMT host. Assess a bounded isolated worker and artifact-loading trust; no uncontrolled environment modification. Record the actual laboratory/worker platform, not the prior Work-shell probe. Failure to install/load safely within the chosen maintenance constraints returns the resource for reconsideration. |
| **H2 — bounded native generation** | Proposed engineering budget: one smoke call with n=4, then two distinct-seed calls with n=16 and one repeat of a preceding seed: at most four calls and 52 requested outputs, no automatic retries/refilling. These counts are proposals, not scientific length thresholds or guaranteed unique yields. Before running, fill in explicit wall-time and memory/process limits for the actual worker. Unset limits block execution. Record actual time/counts/termination; loading time and hidden work remain distinct. |
| **H3 — output fidelity and repeatability** | Compare direct native results with the adapter's sequences/order/scores/descriptors. Record variation for the repeated seed rather than guarantee bitwise equality from seed alone. Require usable real outputs, honest anomalies, and declared bounds without switching to another branch/checkpoint silently. If the required configuration cannot deliver usable output, increment 2 is not demonstrated. |
| **H4 — join to increment 1 and controls** | Evaluate compatible outputs via the already qualified Macrel route, preserving native scores/order and incompatible leading-M or other views. Apply both selectors without rewriting results. Compare the same generated pool before/after selection and a small procedural control under stated budgets. This demonstrates generation plus assessment/selection, not experimental efficacy or feedback. |

The [official starter](https://github.com/szczurek-lab/hydramp-starter-kit/tree/7804df862872ccc6d09fe01c41bafbca194cfa31)
is an asset/environment reference, not a workflow dependency. Do not inherit its
quota filling, challenge reference exclusions or library rules. If no appropriately
bounded permitted environment works, return a concrete alternative for scientific
review. A random or fictional generator cannot silently fulfill the learned-
generation increment. A maintenance-heavy but working route may still be declined;
operational success, applicability and permission are separate gates.

## 7. Resource terms and small scientific controls

For Macrel as well, separate code license, notices from incorporated code, packaged
ONNX assets, source-data/fixture terms and any redistribution. The inspected project
declares MIT and bundles the model files; confirm the exact selected artifact and
notices instead of treating a paper or metadata as universal permission. Record
private-use qualification separately from any decision to redistribute assets/data.
No retraining or bulk training-data redistribution is required for increment 1.

| Resource disposition | Evidence that justifies it |
| --- | --- |
| **Recommend accepting a specific Macrel bundle for the agreed scope** | M1–M8 pass, actual installed assets/import route are identified, applicable use/fixture terms are acceptable, and investigators accept the stated chemical/preprocessing/applicability limitations for exploratory ranking. This is not generic acceptance of every Macrel version. |
| **Reconsider or decline Macrel** | Unresolvable identity/row/negative-loss behavior, inability to preserve/justify precision, unusable installed route, unacceptable asset terms, or a domain mismatch that makes it unsuitable for the agreed task. The bounded leading-M incompatibility is already accepted under D35; it is not biological invalidity or total resource rejection. |
| **Recommend accepting a specific HydrAMP route** | H0–H4 pass with usable native output, acceptable terms and isolated-environment maintenance, honest representation/observability limits, and a real Macrel integration within approved bounds. |
| **Reconsider or decline HydrAMP** | Required artifacts/permissions unavailable, unmaintainable or unsafe environment, failed native loading/generation, no usable compatible output in the bounded qualification, or irreconcilable output attribution. Report what failed; no surrogate generator or completion claim follows. |

Uncertainty about source training data is not by itself proof that inference is
forbidden. Identify which terms/evidence are applicable to the actual use,
fixtures or distribution; keep unresolved rights separate from empirical domain
limitations and from runtime defects. These dispositions return evidence for
investigator approval, not automatic permanent dependency adoption.

Macrel's [training instructions](https://github.com/BigDataBiology/macrel/blob/8c1f7321618ccde2a28b960d32525620d2c737e3/train/README.md)
and [AMP preprocessing](https://github.com/BigDataBiology/macrel/blob/8c1f7321618ccde2a28b960d32525620d2c737e3/train/build-AMP-table.py)
identify AmPEP training data and separate iAMP benchmark sets; do not equate the
benchmark model with the exported deployed model. Its Hemo route uses HemoPI-1
main/validation data. The [HemoPI source paper](https://doi.org/10.1038/srep22843)
describes positive experimental examples but Swiss-Prot-sampled negatives, not
a complete collection of experimentally established nonhemolytic peptides.
Thus `NonHemo` is particularly unsuitable as a safety certificate. Do not import
HemoPI's historical labeling criteria as PeptideMT biological thresholds.

Compare those origins with the official HydrAMP
[training provenance](https://github.com/szczurek-lab/hydramp-starter-kit/blob/7804df862872ccc6d09fe01c41bafbca194cfa31/data/README.md).
Record shared source pools, sampled-negative assumptions, charge/hydrophobicity
and length preferences. Exact sequence/homology overlap and linkage to selected
asset builds remain unknown. If small permitted reference data become available,
check exact overlap and representative similarity; no exhaustive benchmark or
retraining is requested. Unknown overlap stays unknown. Different algorithms
alone do not supply independent evidence.

Keep three initial controls: (1) fixed external pool, both selectors; (2) learned
generated pool before/after those same selectors; (3) a small declared procedural
proposal/redesign control with matched length/composition where possible, assessed
identically. Such matching can leave many Macrel features unchanged, which is
informative about model sensitivity, not evidence of biological equivalence.
Report native/internal and external evaluation budgets separately. Improved Macrel
scores establish improvement in that signal, not experimental AMP/hemolysis gains.

## 8. Ownership, extension obligations and remaining approval

PeptideMT owns per-occurrence design/evaluation attribution, resource/function
bindings, eligibility/selection meaning, failure accounting, reproducibility and
later feedback decisions. Macrel owns its native features/classifiers and HydrAMP
its native sampling/scoring. Reuse MolSysMT for actual molecular representations/
manipulations; do not build coordinates for this sequence-only route or duplicate
its topology/chemistry tables. SMonitor/DepDigest handle diagnostics/selected optional
dependency boundaries, ArgDigest input contracts, PyUnitWizard actual quantities;
unitless scores remain unitless. Praxis/Recorda reuse stays within the preserved
[audit](integration_audit.md); no general MOLI orchestration prerequisite is added.

The [suite optional-engine contract](https://github.com/uibcdf/molsyssuite/blob/main/devguide/optional_engine_integration.md)
requires selected-route guards, lazy imports, original result/mapping provenance
and actual installed-provider evidence. This specification is its local scientific
review precursor, not completed adoption. Formal admission/starter generation
is now authorized under D36 and started in uibcdf/molsyssuite#146; no other
development issue is authorized. Actual admission/bootstrap remains incomplete.

Minimum extension obligations are concrete: external and generated proposals use
the same attribution/evaluation boundary; one native resource can return multiple
outputs without becoming multiple scientific families; native generation evidence
does not overwrite external evaluations; later selections/parent choices retain
the evidence snapshot used. Saved evaluations remain usable without generators.
No fixed mandatory stages or target input are imposed on these providers. Preserve
target context if supplied and record it **unused by these native operations**;
neither can meet an unassessed recognition requirement. Increment 3 needs actual
subsequent permitted proposal calls; the priority target-directed milestone still
follows the functional core without waiting for a universal framework.

D35 accepts sequence-preserving preprocessing, provisional chemistry/length scope,
native output/mapping/precision behavior, both selectors and M1–M8. The scientific
design of increment 1 is closed within those limits, subject to real qualification
and review of any material applicability limitation. Exact builds/assets/terms,
permitted fixtures, environment/resource bounds, suite admission and commissioning
remain operational prerequisites; they do not reopen the general design. W0–W4
is now authorized under D36, with W1 conditional on completed W0. HydrAMP H0–H4
remains a proposal with no execution authorized or assets selected. The
[commissioning brief](increment_1_work_order.md) records the bounded next tasks.

Within approved contracts, Codex can choose internal types, run-local token syntax,
layout/serialization, batching, safe worker mechanics and routine test mechanics.
It may not silently change sequences, resource roles, native thresholds, eligibility,
precision affecting choices or scientific attribution. Concrete Python interfaces
are a small next implementation-design task, not permission to replace these
contracts with a generic plugin framework. The current task is the authorized
admission/implementation assignment and its indispensable operational conditions,
not reapproval of the settled scientific contract.
