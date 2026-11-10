# HydrAMP numerical acceptance: behavioral evidence and review proposal

Status: **fixture-specific deviation accepted under D40**, 2026-11-02.
Owner: investigator-owned `uibcdf/hydramp`; consumer: PeptideMT #8 / D39.
The investigator accepted the limited disposition: continue dev0 qualification
with the observed deviation admitted only for the twelve compared inputs.
No new tolerance or full-generator acceptance is recorded. The
[decision receipt](evidence/hydramp_limited_acceptance.json) binds the approval to
the original proposal, exact dev0 wheel and unchanged measured evidence.
The [published D40 decision](https://github.com/uibcdf/peptidemt/issues/8#issuecomment-6595109769)
is verified in its [publication receipt](evidence/hydramp_limited_acceptance_issue_update.json).
The [published issue update](https://github.com/uibcdf/peptidemt/issues/8#issuecomment-6594967117)
retains the review; its [publication receipt](evidence/hydramp_behavioral_review_issue_update.json)
verifies the public record.
The [FP64 report](hydramp_numeric_reference.md) retains the original failed
FP32 comparisons and explains why the legacy binary is not an exact oracle.

## Additional evidence without another model evaluation

The [receipt](evidence/hydramp_behavioral_review.json) pins the provider's new
`ports/pytorch/devtools/behavioral_review.py`, synthetic tests, exact saved input
hashes and local output/log files. It opens only retained, hash-verified output
archives. It imports no engine and loads no weights or PCA. PeptideMT receives
analysis and documentation, not a duplicated model or molecular-system operation.
The port's inference source, installed wheels, environments and thresholds are
unchanged; the new helper is developer analysis outside the wheel's `src/` tree.

| Observation | Result on retained data | Limit |
| --- | --- | --- |
| Tokens versus native, dev0 and dev1 | 300/300 unchanged; all 300 native margins exceed twice their observed local probability error | Conditional on these arrays; no unseen-input error bound |
| Tokens versus independent FP64 reference | All three FP32 implementations match 300/300 | Approximate reference; no biological validation |
| Native AMP versus dev0 scores | Same descending occurrence order; 66/66 pair relations preserved; no tie split/new tie/reversal | Twelve original token rows, no native pandas/descriptor execution |
| Native MIC versus dev0 scores | Same order and all 66 pair relations preserved | Diagnostic only; MIC does not order the commissioned unfiltered route |
| Raw NumPy normal draws | Bitwise equal across NumPy 1.18.5 and 2.4.6 for seeds 101/202 and batches 4/16, width 64 | Raw draws only; not PCA, TensorFlow RNG or end-to-end generator repeatability |

The minimum positive AMP score gap is `1.3828277587890625e-5`, versus
maximum observed AMP error `2.980232238769531e-7`. MIC minimum positive gap is
`3.584555997804273e-6`, versus maximum error `1.1920928955078125e-7`.
Each of the 66 pairwise gaps exceeds the sum of the two observed per-occurrence
errors. There are no exact score ties in this fixture, so it does not test native
tie handling. Half-L1 probability differences are reported as such; float32
normalization is approximate and no calibrated statistical uncertainty is inferred.

Twelve new artificial-data checks pass in the retained NumPy-only Python 3.14
worker. They detect a tiny probability perturbation that flips a near-tie token,
a rank reversal, a split tie even when occurrence order happens to stay unchanged,
new ties, invalid inputs and the difference between local and global perturbation
bounds. All scientific artifact opens, engine imports and network are blocked in
those tests. These checks validate the diagnostic, not near-tie behavior of the
pretrained model. Both old/new raw RNG probes also block artifact/engine/network
access. Processes are sequential, single-threaded, CPU 0/1, nice 10, with a 1 GiB
address-space ceiling and 30 s timeout. No learned-parameter call was made.

## Investigator disposition — D40, 2026-11-02

**Accepted limited disposition:** accept the observed numerical discrepancy only as a documented,
fixture-specific deviation for continued development of the original **dev0**
port. Preserve all prior diagnostic FAIL results. Do not adopt dev1 as a correction
or call the resource scientifically qualified. The FP64 and behavioral evidence
support continuing the port; they do not justify unrestricted acceptance.

The investigator explicitly accepted this limited disposition after reviewing the
measurements and proposed scope. D39 local implementation and artificial-data
preparation can continue. This decision grants no new model execution allowance,
scientific method or architecture. No larger probability tolerance is chosen
retrospectively from the observed maximum error; existing FAIL results stand.

For the prospective qualification, the preparation plan keeps separate verdicts;
acceptance on broader inputs and any new numerical criterion remain unapproved:

1. **Implementation fidelity:** exact source/asset identities, equations, conditions,
   input quantization, token mappings and numerical diagnostics. Keep the original
   `atol=2e-6, rtol=2e-5` report visible; a failed report is neither silently removed
   nor treated as proof of biological failure. Wider numerical criteria require
   an explicit reason and approval before applying them to new results.
2. **Observable result fidelity:** require unchanged occurrence identity, tokens,
   strings, score meaning, duplicates and native ordering for fixed inputs. Keep
   the already used head-score band; detect tie splitting/creation separately.
   Any changed token, ordering or native view returns to investigation, even if
   its absolute numerical error is small. Preserve original per-occurrence values.
3. **Complete route qualification:** native `properties=True`, descriptor provenance,
   original zero-token scoring, count/empty/failure handling, seed behavior,
   result/provenance construction and the actual PeptideMT integration. Passing
   the core calculations does not substitute for these checks or H0–H4 acceptance.

The inspected reference [unfiltered generation path](https://github.com/szczurek-lab/hydramp/blob/6590d2f4c2963f25d30669052a4c4a857e0e7279/amp/inference/inference.py#L159)
uses AMP-descending `nlargest` when `properties=True`, followed by original
physicochemical descriptors. Its heads receive the original decoded token arrays rather than a re-encoding
of the rendered strings. Do not use MIC as an alternative sort key, introduce a 0.8 activity filter,
or re-encode strings for scoring in the commissioned `filter_out=False` route.
The raw-draw evidence corresponds to the NumPy draw used there, not all effects
of its [seed utility](https://github.com/szczurek-lab/hydramp/blob/6590d2f4c2963f25d30669052a4c4a857e0e7279/amp/utils/seed.py).

## Remaining fixtures and execution boundary

### Proposed confidence campaign after the dev3 comparison — 2026-11-03

The investigator subsequently instructed proceeding with this confidence goal.
The [prepared campaign](hydramp_confidence_campaign.md) now fixes the candidate,
256-input fixture, layout controls and proposed finite resource/call allowance.
The exact 132-forward CPU plan was subsequently approved and executed. All 256
distinct-input sequence/token views agree; global AMP near-tie pair relations
change, so the numerical and observable diagnostics remain FAIL. Its execution
record keeps the exact scope and exhausted budget. Broader scientific acceptance
remains pending. The original recommendation below is retained as design history.

The investigator asks how to increase confidence in the modernized generator.
The [completed dev3 comparison](hydramp_full_comparison.md) provides favorable
observable results on twenty distinct latent inputs, with the unchanged internal
probability diagnostic still failing. The recommendations below are **proposed**,
not a D40 extension, accepted new criteria or permission for more model calls.
For confidence in the port itself, prioritize broader paired coverage before
claiming that an integration milestone establishes generator equivalence.

1. **Broader paired inputs.** Prepare a candidate fixture of 256 distinct latent
   rows: sixteen predeclared seeds, 1001 through 1016, with sixteen rows per seed.
   This is a practical first expansion, not a power calculation or a guarantee
   about rare errors. Freeze actual inputs, hashes, versions, use conditions and
   execution order before running either implementation. Keep the commissioned
   `softmax=True, mode='amp', filter_out=False, properties=True` route and existing
   weights, equations, float32 computation and descriptor definitions. Compare
   native and modern results on identical latent bytes; separately verify that
   each public seeded call produces those bytes. Reuse the old twenty-input
   results as retained regressions rather than repeating accepted runs.
2. **Decision sensitivity.** Save per-position token margins, probability
   differences, AMP/MIC scores and pairwise ordering relations for the complete
   fixed fixture. Report the smallest margins and worst discrepancies, not just
   averages. Identify sensitive cases within this declared pool; do not search
   additional seeds until a reassuring result appears. If no near ties occur,
   report that missing coverage. Investigation of a changed token/order or a
   separate targeted search requires a reviewed follow-up plan, not an automatic
   retry or a larger tolerance.
3. **Batch and occurrence behavior.** Predeclare a small subset of those same
   latent rows for reordered/partitioned and repeated evaluations. Compare each
   occurrence across batch layouts and each layout against the native reference;
   track any batch-dependent numerical or decision changes instead of assuming
   bitwise batch invariance. Freeze exact layouts and count every repeated
   decoder/head evaluation in the later execution plan. In separate artificial
   contract cases, exercise duplicate occurrences, exact score ties, internal and
   trailing zero tokens, empty projections and malformed/incomplete results.
   Preserve original token-to-score attribution and native tie behavior; no
   repair, re-encoding, deduplication or refill is introduced.
4. **Prospective verdicts.** Keep numerical diagnostics and observable-result
   fidelity separate, as above. Retain unchanged probability/head bands and all
   existing FAIL reports. Proposed observable checks cover tokens, projected
   strings, occurrence identity/count/order, descriptor definitions/values and
   within-worker repeatability. Any deviation must be reported and investigated;
   a small average error cannot overrule a changed scientific result. Broader
   acceptance remains an investigator decision after reviewing the full report,
   including missing cases; no zero-error-rate claim follows from 256 cases.
5. **Consumer qualification.** Prepare the PeptideMT adapter using retained
   results and artificial cases, with portable result/provenance and attribution.
   Then qualify actual direct/adapter behavior and the HydrAMP–Macrel–selector
   route through the existing H0–H4 commission. The expanded port comparison does
   not spend or replace the separate H2/H4 design, waive bundle/use review or
   accept the adapter. Macrel requires its own explicitly counted allowance.

This is a scoped validation proposal. No exact new forward count or executable
allowance is asserted until the input/layout manifest and controller are prepared.
The current allowance is exhausted. Before learned execution, present the exact
candidate, asset/input hashes, all model/descriptor/PCA calls and stopping rules
for approval; inspect the actual shared host and preserve the investigator's
4 GB task RAM intent, CPU-only sequential operation and no automatic retries.
GPU, training, model replacement, another peptide family and package publication
remain outside this work. Preparation may continue with artificial data and
retained arrays without loading scientific artifacts or evaluating models.

Original published peptides and evaluation data can later support a separately
designed scientific benchmark, with training overlap and assay endpoints checked.
Agreement with the original and agreement with Macrel are computational evidence,
not independent proof of antimicrobial efficacy, safety or biological superiority.
Such a benchmark and experimental validation are separate proposals, not additions
to this execution budget or the present commissioning scope.

### Earlier D40 fixture plan and retained boundaries

| Missing coverage | Concrete preparation | Required evidence before acceptance |
| --- | --- | --- |
| Sensitive decisions | Artificial exact/near ties, per-row perturbations and unchanged-token counterexamples; diagnostic checks now pass | A prospectively chosen broader fixed-input fixture; report the minimum margins actually found, including absence of near ties |
| Recurrence/input coverage | Preserve current twelve rows; predeclare additional seeds/latent rows and batch partitions | Paired exact-input native/port arrays; no cherry-picking or seed search outside a finite approved allowance |
| Occurrences and tokens | Duplicate occurrences, internal/trailing zeros, empty projection, count/shape failures | Actual native token/score/string mapping and result handling; no molecular repair/deduplication |
| Native ordering and properties | Exact ties and near-tie AMP scores, same original descriptor provider/profile | Original pandas behavior and descriptor/result comparison; a stable NumPy sort alone is insufficient |
| Reproducibility | Retain the four raw-draw hashes; preserve explicit host seeds and batch sizes | Repeated complete native/adapter case and provenance, distinguishing fixed latent bytes from seed-only agreement |

This is a fixture/readiness plan, **not an executable model allowance**. It does
not search for difficult latent cases, transform new inputs with the real PCA,
load any model or spend D38's four-generation-call/52-output design on extra
comparisons. Prepare the exact candidate, immutable inputs/use review and a fresh
finite CPU/RAM/time/call plan before requesting further learned execution.
No new Macrel, GPU, training, target conditioning, feedback or publication follows.

Reuse the [active qualification record](archive/qualify_hydramp_increment_2.md)
and #8. The fork issue board remains disabled; retain the explicit provider handoff
limitation rather than contacting upstream or changing settings. Source/reports
are local and uncommitted. Retain task resources for review by 2026-11-13.
