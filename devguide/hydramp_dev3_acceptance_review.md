# HydrAMP dev3: consolidated bounded-acceptance review

Status: **original proposal accepted for experimental AMP generation under D41**,
2026-11-03. The [acceptance record](hydramp_dev3_acceptance.md) is the current
disposition. The recommendation and prospective conditions below preserve their
pre-acceptance wording; exact original bytes are retained in the decision receipt.
Owner: [PeptideMT #8](https://github.com/uibcdf/peptidemt/issues/8).
Provider numerical findings remain in
[HydrAMP #1](https://github.com/uibcdf/hydramp/issues/1); reusable profile metadata
is proposed separately in [HydrAMP #2](https://github.com/uibcdf/hydramp/issues/2).

## Original recommendation and decision boundary — retained history

**Recommend accepting the exact modern dev3 bundle as an experimental resource
for reproducible, unfiltered AMP proposal generation in PeptideMT, subject to
the bounded conditions below.** This is a recommendation for scientific
disposition, rather than an accepted decision, a release qualification or
permission for another run. The investigator requested this consolidated review
after the real installed-adapter case completed.

The evidence supports a functioning modern computational route with preserved
observed sequence behavior and explicitly investigated numerical differences.
It does not establish that generated peptides are active, safe, generally better
than the original, or equally useful across peptide families. Accepting this
proposal would admit the documented dev3 deviations within this scope; the
original failed diagnostics would remain failed. D40 retains its original
twelve-input dev0 scope until a distinct investigator disposition is recorded.

No model, PCA, descriptor or Macrel evaluation was performed for this review.
The [review receipt](evidence/hydramp_dev3_acceptance_review.json) pins its evidence
and exact proposal. Historical artifacts, environments, calls and verdicts are
reused, without merging their separate qualification scopes.

## Exact candidate and provenance

| Item | Reviewed identity |
| --- | --- |
| Provider | `hydramp-torch==0.0.0.dev3`, local unpublished wheel |
| Provider wheel SHA-256 | `81761e0d48d92f0956e0afc28b3b4154f16032de53c666fd2cfbb53606102ed7` |
| Consumer | `peptidemt-0.1.0+118.g1f8c444.dirty-py3-none-any.whl`, local unpublished artifact |
| Consumer wheel SHA-256 | `18b1cb18b9662092203aad9c64d45bc0d61a862577297c13a664572dbdbc3e83` |
| Original reference source | `6590d2f4c2963f25d30669052a4c4a857e0e7279` |
| Selected official starter | `7804df862872ccc6d09fe01c41bafbca194cfa31` |
| Learned assets | Publisher-attributed epoch-37 checkpoint; exact per-file hashes in the execution plan |
| Numeric PCA SHA-256 | `c3e1a32546ffe3c39f577e1908a72142321b26d51a0184bd647720f14539c99d` |
| Installed-adapter execution plan SHA-256 | `31317bd3023165300d9558134e73c584a3bdfa25e2c619a200cff11c65c33608` |

The installed execution uses parent Python 3.14.10 and generation Python 3.14.7,
NumPy 2.4.6, CPU Torch 2.15.0+cpu and modlAMP 4.3.3. Its complete 345-file manifest,
both runtime inventories, SDK identities and import origins are retained in the
[adapter record](hydramp_execution_adapter.md). This is qualification of those
installed bytes, not a supported range for arbitrary newer dependencies.

The [artifact/use review](hydramp_environment_review.md) retains publisher
attribution, original notices and bounded local research conditions. Byte
identity between the selected starter assets and the original Google Drive
archive remains unverified. Archive metadata and original repository licensing
are not presented as newly verified permissions to redistribute weights or
commercialize outputs. This proposal preserves the existing local-use boundary;
it does not settle those separate questions.

## Evidence by scientific question

| Question | Observed result | What it supports |
| --- | --- | --- |
| Does modernization preserve generated sequences? | In the [confidence campaign](hydramp_confidence_campaign.md), all 256 distinct latent inputs / 6,400 distinct-input token positions agree; all 7,700 paired positions including reused controls agree. All seventeen actual public batches per implementation preserve strings, occurrence order and five descriptors. | Strong finite-fixture sequence/return fidelity; no unseen-input guarantee. |
| Is all internal numerical output equivalent? | Probability diagnostic FAIL: 346/134,400 distinct-input values, or 421/161,700 including reuse, exceed the unchanged band; maximum difference `2.2727251052856445e-4`. | A real retained numerical deviation, despite unchanged observed tokens. |
| Is global native AMP ranking identical? | Of 32,640 pairs, one reversal, two split native ties and seven new modern ties. Saved AMP-only top-k membership differs by one occurrence at k=2,5,9,10,23,42,50. | Global ranking equivalence fails; this can affect a real AMP-only selection boundary. |
| Are the differences understood well enough to retain modern computation? | [Causal and FP64 analyses](hydramp_amp_activation_attribution.md) explain final-activation effects, upstream drift and error compensation. On 192 selected original-context rows, full-head FP64 maximum/mean/RMS error is lower in modern; individual outputs favor modern 91, original 58, equal 43. | Evidence favors retaining the modern implementation; no uniform pointwise superiority or exact-arithmetic proof. |
| Does the public installed adapter receive genuine output faithfully? | The [single corrected case](hydramp_execution_adapter.md#corrected-installed-public-case-completed--2026-11-03) returns 16 proposals at seed 1001, exact retained modern results/order/indices/full trace, exact JSON replay and captured parent attribution with seven records. | Real installed adapter fidelity on this exact case, separate from artificial tests. |
| Does assessment and selection compose correctly? | The [H4 source-extension experiment](hydramp_h4_qualification.md) retains 32 proposals, assesses 30 compatible strings plus four controls with Macrel, and reproduces both k=4 selector rankings after replay. | Procedural composition and preserved meaning/provenance on the tested pools. |
| Has useful joint AMP/hemolysis behavior been demonstrated? | Of 30 assessable generated strings, nine are Macrel AMP-positive; all nine are also Hemo-positive. Zero meet the joint AMP-positive/NonHemo labels. Two leading-M exclusions are retained. | No demonstrated joint hit on this small fixture; neither biological efficacy nor a general generator failure rate follows. |

The FP64 cohort was selected to investigate known discrepancies, not to estimate
unbiased population performance. Its two layouts share NumPy/BLAS; bitwise
agreement between them is a consistency check rather than independent-library
validation. The [58 original advantages](hydramp_amp_activation_attribution.md)
include genuine pointwise advantages as well as compensating errors; they are
not all dismissed as an original implementation bug. Individual upstream LSTM
accumulation primitives remain unlocalized.

The 32 H4 sequences and returned order also match retained original HydrAMP
output for seeds 1001/1002. Thus the lack of a joint Macrel hit is not a
port-specific sequence regression on those inputs. The four controls establish
assessment behavior, including a possible joint hit; they do not constitute a
competing generator or an efficacy benchmark.

## Qualification map and practical limits

| Boundary | Current evidence and remaining limit |
| --- | --- |
| H0: assets/use | Exact selected assets and original attribution retained for the authorized local research use. Drive-versus-starter byte identity and broader use/distribution questions remain open. |
| H1: deployment | Real isolated Linux CPU/Python 3.14 execution, exact import origins and installed dependency closure. No other-platform or public package-acquisition qualification. The historical legacy metadata overrides remain reference-environment facts. |
| H2: bounded calls | Separate approved comparison, confidence, diagnostic, H4 and public-adapter attempts have actual receipts. Each allowance is exhausted; their totals are not silently substituted for the original historical four-call proposal. |
| H3: fidelity/repeatability | Repeated native/modern batches and actual same-provider adapter receiving pass within their measured scope. Internal probability and global AMP-rank criteria remain FAIL. |
| H4: composition | Real private source-extension generation/assessment/selection and saved installed receiving pass. The full live chain was not rerun as one all-public installed workflow; the public adapter's one generation is separately qualified. Broader scientific disposition is still pending. |

The public-adapter case took **8.358 s**, with **453,214,208 bytes (432.2 MiB)**
aggregate sampled process-tree RSS; launcher including preflight took 9.289 s.
The earlier private generation/assessment experiment took 55.76 s sequentially,
with 553.5 MiB maximum sampled tree RSS across its stages. These observations
fit the investigator's 4 GB task intent. They are shared-host observations,
not a stable speedup benchmark or a hard kernel resident-memory guarantee.
The 8 GiB virtual-address ceiling is distinct from physical RAM usage.

The public adapter first failed before all learned operations because the
qualifier imposed an inherited hard 1 GiB parent address-space limit. Its
[failed receipt](evidence/hydramp_execution_adapter_failed_execution.json) remains
preserved. The corrected parent soft 1 GiB/hard 8 GiB composition and failed-case
exit status have four model-free guards; the fresh separately approved attempt
passed. The failure is not hidden or counted as a model-quality failure.

Engineering evidence includes 55 installed controlled checks, four qualifier
guards, exact saved replay, parent attribution, model-free documentation builds
and six doctests. Their original environments and published receptor identities
remain in their receipts; those checks do not multiply the scientific sample.

## Proposed conditions of bounded acceptance

1. Accept only the exact local experimental candidate above and the commissioned
   seeded AMP route: `softmax=True`, `mode='amp'`, `filter_out=False`,
   `properties=True`, `n_attempts=1`, explicit seed. Preserve weights, numeric
   PCA, equations, precision and original token-to-score attribution.
2. Retain native AMP/MIC scores as model outputs, distinct from Macrel scores,
   experimental MIC, activity, safety and calibrated probabilities of success.
   Keep every occurrence, original order, trace, failure and unresolved chemical
   attribute. Preserve the two incompatible H4 proposals without repair/refill.
3. Admit the documented numerical/ranking deviations explicitly within this
   scope, keeping their original values, thresholds and FAIL verdicts. Exact
   global native AMP ranking is unqualified. No silent rounding, widened band,
   legacy imitation or per-peptide implementation switching follows.
4. Preserve D35/M1–M8 and both current selectors. They use Macrel AMP/hemolysis
   fields, not HydrAMP AMP/MIC. There is no new global HydrAMP-score prefilter.
   A change to that selection boundary requires separate scientific review.
5. Retain original artifact/use conditions, exact inventories and provider-owned
   computations. Molecular-system handling remains MolSysMT-owned. Metadata
   reuse proposed in HydrAMP #2 is nonblocking and does not authorize an
   implementation or change the descriptor definition.
6. Treat all existing execution budgets as consumed. Acceptance of this resource
   would not itself authorize new model/PCA/descriptor/Macrel calls, GPU, training,
   analogue/target-conditioned generation, another family, feedback or publication.

## Next work after disposition

If the investigators accept or narrow this proposal, record their exact scope
and reasoning in the decision log and #8 before relabelling any resource as
accepted. Reconcile the active work record through its normal lifecycle; do not
close the separate numerical/profile provider issues merely because consumer
use is accepted. No new accepted D-number is assigned by this report.

Then complete a tutorial for generation, assessment and both selectors using
the retained receipts first. Label cached replay and real execution separately;
the tutorial must not execute models during a documentation build or imply that
its displayed generation example has fresh run authority.

A subsequent scientific benchmark would address utility with declared assays,
chemistry, dataset provenance/training overlap, comparators and prospective
criteria. It needs its own commissioned design and finite call plan. The current
32-proposal pool is neither a general efficacy benchmark nor a reason to search
seeds until a favorable result appears. The unimplemented precision proposal in
HydrAMP #1 remains an independent investigation, rather than a prerequisite for
this bounded decision.

## Review and resource retention

This document consolidates existing measurements. It adds no new scientific
test, tolerance, source change, accepted decision, commit or publication of a
package/model. The exact evidence manifest and documentation checks accompany
the review receipt. Retain the task resources for review through 2026-11-13;
reassess retention before cleanup rather than deleting the underlying arrays.
