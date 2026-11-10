# HydrAMP dev3: ranking relevance and proposed limited disposition

Status: **saved-output review complete; investigator disposition proposed**, 2026-11-03.
Owner: investigator-owned HydrAMP fork; consumer: PeptideMT #8 / D39–D40.
The investigator authorized reviewing the retained near-tie cases and preparing
a recommendation. No new scientific acceptance or learned execution is inferred.
The [published review](https://github.com/uibcdf/peptidemt/issues/8#issuecomment-6611090848)
is verified in its [publication receipt](evidence/hydramp_rank_relevance_issue_update.json).

## Evidence and immediate origin

This review uses the frozen [256-input campaign](hydramp_confidence_campaign.md),
candidate **hydramp-torch 0.0.0.dev3**, wheel SHA-256
`81761e0d48d92f0956e0afc28b3b4154f16032de53c666fd2cfbb53606102ed7`.
Its [receipt](evidence/hydramp_rank_relevance_review.json) pins the new provider
analysis/tests, original outputs, consumer source inspection and guarded runtime.
All twenty-four campaign artifact hashes remain unchanged. No weights/PCA are
loaded, no learned arithmetic, descriptors or Macrel calls run, and no scientific
source, threshold, score, selector or earlier FAIL report is modified.

The AMP and MIC heads receive **identical original token arrays across engines**
for all 256 distinct inputs. Consequently the immediate AMP score discrepancy
is in head numerical execution/context, not changed generated tokens or a different
string encoding. Applying the same stable ranking to those two saved score vectors
explains the observed diagnostic rank changes. This localizes the affected branch;
the individual responsible primitive remains unproven. The earlier FP64 work
studied the decoder, not an independent FP64 reference for these AMP-head scores.

All ten changed AMP pair relations involve scores between approximately
`0.99997258` and `0.99999970`. Float32 spacing there is
`5.960464477539063e-8`; native pair gaps are zero, one or two such steps. That
describes numerical scale, not a calibrated biological uncertainty or a justified
new tolerance. Eighteen occurrences participate in changed relations; thirteen
change global rank position. The maximum observed displacement is two places.

## Exhaustive saved-score selection replay

The helper examines every global AMP-only top-k cut, **k = 1 through 256**, with
exact saved values and earlier-occurrence tie breaking. It considers both original
latent order and concatenation of the actual public batch returns. Both pool-order
scenarios give the same affected cutoffs: **2, 5, 9, 10, 23, 42 and 50**. At each,
one selected occurrence is replaced; no cutoff replaces more than one.

| k | Present only in native top-k | Present only in modern top-k |
| --- | --- | --- |
| 2 | seed 1008, latent row 9 | seed 1002, latent row 12 |
| 5 | seed 1008, latent row 3 | seed 1014, latent row 0 |
| 9 | seed 1007, latent row 14 | seed 1003, latent row 8 |
| 10 | seed 1010, latent row 7 | seed 1003, latent row 8 |
| 23 | seed 1013, latent row 6 | seed 1012, latent row 13 |
| 42 | seed 1004, latent row 15 | seed 1002, latent row 2 |
| 50 | seed 1013, latent row 12 | seed 1009, latent row 7 |

Rows are zero-based original latent occurrences, not molecular identities. All
other cuts retain the same selected membership, although internal ordering can
differ. The ten pair changes and seven changed cutoffs are different quantities;
neither is a statistical failure-rate estimate. Of 32,640 pairs, 32,614 have native
separation exceeding the sum of their observed endpoint discrepancies. This is
conditional evidence on saved arrays, not a future error bound.

The small absolute differences **can change an actual global top-k member** in
this diagnostic scenario. They cannot be dismissed as universally irrelevant.
Every public generation batch still has identical returned strings, occurrence
order and five descriptors. Its observed native/modern batch-order agreement does
not establish global AMP-only selection equivalence. Both original diagnostic
FAIL verdicts remain visible and unchanged.

## Boundary with PeptideMT's actual selectors

Source inspection at PeptideMT `1f8c444e4619` verifies the unchanged
[selector](../src/peptidemt/selection.py) and [result](../src/peptidemt/results.py)
contracts. The source hashes/full commit are in the review receipt:

- `amp-first` reads Macrel `AMP_probability`, then `Hemolytic_probability`, then
  original occurrence; `hemolysis-first` swaps the first two keys.
- HydrAMP's `amp` and `mic` fields are **not** those Macrel measurements. MIC must
  not become hemolysis, and HydrAMP AMP must not silently replace Macrel AMP.
- The approved H4 composition retains every generated proposal for assessment,
  including incompatible/failed views, and then applies both unchanged selectors.
  It does not add global HydrAMP-AMP pruning before Macrel.

The replay above **does not execute either PeptideMT selector**, fabricate missing
hemolysis scores or supply H4 evidence. On the observed identical sequence/order
pools, this discrepancy has no direct input-field path into those selectors under
the current composition. Actual identical Macrel results/selections still require
the separately qualified and authorized end-to-end run. No such run is claimed.
Changing pool order or adding HydrAMP-based preselection would create another
selection boundary and needs its own scientific review.

## Proposed investigator disposition

The investigator subsequently prioritized explaining the differences and
authorized an owning-fork issue, with validated modern numerical improvements
retained where justified. The [causal investigation](hydramp_amp_numerics.md)
demonstrates a standalone legacy sigmoid artifact and prepares a real AMP trace;
it does not silently accept the whole model or reclassify the saved FAILs.

**Recommendation:** admit the documented deviations for the exact reviewed dev3
candidate/256-input fixture **to continue consumer qualification** of the already
commissioned deterministic unfiltered AMP proposal route. This is a bounded
development disposition, not general scientific adoption or identical-rank proof.

The concrete proposed conditions are:

1. Preserve the numerical and global AMP-pair FAIL reports, all native/modern
   values, original thresholds, input/output bytes and earlier D40/dev0 history.
   No rounding, widened bands, replaced equations or repaired rankings follow.
2. Keep the same source/starter/assets, local-use terms, descriptor profile and
   selected Linux CPU/Python 3.14 candidate. No other HydrAMP route, training,
   target conditioning, chemistry/family expansion or package/model publication.
3. Keep every generated occurrence and provenance. Native AMP/MIC scores remain
   identifiable native evidence; exact global AMP-only ranking is unqualified.
   Preserve D35/M1–M8 and the Macrel/selector bindings with no new prefilter.
4. Continue adapter preparation using retained/artificial data under existing
   D38/D39 authority. New model/PCA/descriptor/Macrel evaluations need their own
   exact finite approval; every old neural allowance remains exhausted.
5. Retain the original Drive-versus-starter asset identity gap and pending
   portable provenance, direct/adapter/H0–H4 receiving. No biological superiority,
   safety, universal equivalence or every-feature replacement claim follows.

The investigator's instruction to **review** these cases does not approve this
disposition. D40 remains its original twelve-input dev0 decision. Accepting,
narrowing or declining this proposal is the next scientific decision in #8.

## Verification and limitations

The provider's new `ports/pytorch/devtools/rank_relevance.py` independently replays
pair signs, exact ties and all cutoffs; it imports NumPy only. **18 artificial
checks pass**, including changed membership versus order-only changes, ties whose
split leaves selection unchanged, declared occurrence tie rules, displacement,
strict observed separation and corrupt input rejection. Engines/providers,
scientific-artifact access and network are blocked in those tests. Analysis permits
only the two hash-verified saved output archives to be deserialized.

The initial invocation dereferenced the worker interpreter symlink into the shared
runtime. Its outputs, test logs and unpublished receptor identity are retained as
a superseded runtime attempt. The corrected invocation uses the explicit isolated
entrypoint and asserts `sys.prefix`, NumPy 2.4.6 and published Pytest Receptor 1.2.2
(pytest 9.2.0). All eighteen checks pass there; the corrected analysis output is
**byte-identical** to the initial output. No model evaluation occurred in either
attempt. Count eighteen distinct qualified checks, not thirty-six.

This review studies the observed fixture and two declared ordering scenarios. It
does not establish how often near ties occur, near-boundary generalization, exact
reference accuracy, a scientifically justified score precision or real Macrel/
selector parity. Code/reports remain local and uncommitted. Retain task resources
and original evidence for review by 2026-11-13.

## Subsequent whole-head numerical evidence — 2026-11-03

The [causal trace](hydramp_amp_numerics.md) reproduces all ten changed relations
by switching only the final sigmoid at fixed native logits. The separately
approved [complete AMP-head FP64 reference](hydramp_amp_reference.md) now shows
modern lower maximum/mean/RMS error at all nontrivial recorded stages on 192
selected original-context rows. AMP is closer in 91 modern cases, 58 native, with
43 equal errors. The full-head reference confirms the same ten strict pair
directions; modern corrects one native reversal and splits two native ties, but
seven new modern ties remain. These diagnostic allowances are fully consumed.

This strengthens the evidence for retaining the unchanged modern candidate and
reviewing the existing proposed limited dev3 disposition. It does not accept that
proposal, rewrite the original FAILs, infer biological superiority or change
Macrel-bound selectors, global ranking/tie semantics, D40 or H0–H4 receiving.
