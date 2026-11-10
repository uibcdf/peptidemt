# AMP activation error, compensation and rounded ties

Status: **bounded parameter-free attribution completed; production unchanged**,
2026-11-03. Owner: [HydrAMP #1](https://github.com/uibcdf/hydramp/issues/1);
consumer: [PeptideMT #8](https://github.com/uibcdf/peptidemt/issues/8).

The investigator directs continuing the bounded explanation of the 58 original
advantages before integrated receiving. The [preceding saved-data review](hydramp_amp_error_attribution.md)
could not quantify activation and upstream errors separately. Its old scalar
report retained aggregate activation metrics but omitted the per-input reference
vectors. This continuation reconstructs exactly **two parameter-free FP64 formula
vectors**, each on the same 384 saved original/modern logits, and now saves both
arrays. No weights/PCA/model is loaded, no framework or neural network executes,
and no previous model allowance is renewed. The [receipt](evidence/hydramp_amp_activation_attribution.json)
binds the agent-selected finite arithmetic limits under the current continuation.

## Component attribution

For each engine, decompose the final-score error against the saved whole-head
FP64 result into:

- **Upstream:** FP64 sigmoid of that engine's saved FP32 logit, minus the saved
  full-head FP64 score.
- **Final activation:** saved engine score, minus FP64 sigmoid of its saved logit.

The components sum to the measured total with zero residual. The stable
exponential and tanh formulations agree within `1.11e-16`, cast to identical
float32 values, and give the same attribution counts below. Earlier accepted
aggregate activation maxima and 88/117 own-logit float32-match counts reproduce
exactly. FP64 remains an approximate diagnostic, not exact arithmetic.

Among the **58 original-closer final outputs**:

| Observation | Count |
| --- | ---: |
| Original upstream component is smaller | 39 |
| Modern upstream component is smaller | 12 |
| Equal upstream components | 7 |
| Original has smaller activation error at each engine's own logit | 36 |
| Modern has smaller activation error at each engine's own logit | 22 |
| At identical native logits: original activation is closer | 28 |
| At identical native logits: modern activation is closer | 16 |
| At identical native logits: equal activation error | 14 |

The first two activation rows compare different arguments; the matched-native
rows compare the same argument. These are overlapping diagnostics, not additive
cause categories. Across all 192 rows, the matched-native-logit activation counts
are 37 original / 83 modern / 72 equal, preserving the stronger aggregate modern
operator result without claiming universal pointwise accuracy.

Original upstream/activation components oppose each other in **31/58** cases;
the activation actually reduces upstream absolute error in **17/58**. Modern's
corresponding counts are 26/58 and 14/58. Opposing signs can overshoot and worsen
the total. The preceding review's 20 cases measured final-score versus logit
error sign, a different predicate; it was not a count of all beneficial
compensations. In eight cases, a more accurate modern activation at identical
native logits produces a worse full-head result, directly illustrating error
compensation. Genuine original pointwise advantages remain alongside this effect.

## What happens to the seven modern ties

Three remain tied after the saved full-head FP64 score is rounded to float32.
Four remain distinct in that rounded reference. Thus float32 representation
explains the first three in this fixture; the other four are not required by the
rounded target. No change to scientific ranking/tie rules is inferred.

## Saved-only precision counterfactual, not an implementation

Casting the newly retained FP64 activation of modern logits to float32 simulates
a more precise final activation without changing any learned computation. This
postprocessing evaluates no additional activation/model. Compared with actual dev3:

- Whole-head FP64-cast matches increase **47 → 89**.
- Absolute output error improves in **59**, worsens in **16**, and is unchanged
  in **117** of the 192 cases.
- Mean absolute error decreases `7.2463286623e-8 → 6.5322367329e-8`; RMS decreases
  `1.3615489328e-7 → 1.3487767108e-7`. Maximum stays `1.0792440363e-6`.
- The four avoidable ties resolve; the other three remain. The former reversed
  pair also becomes tied, matching the float32-rounded target while strict FP64
  still distinguishes its direction.
- Returned stable AMP-sort order changes for **one original batch, seed 1012**.

This is an actionable future precision proposal in the existing owning issue,
not a new accepted candidate. An installed Torch implementation and whole-generator
effects are untested; the observed batch-order change requires an explicit
fidelity/disposition review. Preserve dev3 and its failed diagnostics. Do not
choose implementations per peptide or silently patch its deployment precision.

## Verification and next boundary

Seven guarded artificial tests pass. The parameter-free worker completes in
0.36 s, with 52.3 MiB sampled/HWM RSS; saved-only rounding analysis takes 0.22 s.
Limits are CPU 0/1, one numerical thread, nice 10, 30 s per analysis stage,
512 MiB sampled RSS stop, 1 GiB address space and the existing 4 GB task intent.
Model/framework imports, network and unreviewed scientific artifacts are blocked;
matrix arithmetic is blocked, and saved-only stages also block activation calls.
No retry or GPU occurs. The two formula vectors are fully consumed and retained.

This completes the proposed bounded component-error explanation. Individual
LSTM accumulation primitives remain unlocalized; they need not become an
unbounded search for identical FP32 values. Continue preparation of per-occurrence
receiving and H4 composition with retained/artificial data. Actual model/Macrel
execution and scientific acceptance retain their own exact approval boundaries.
No source/weight/chemistry/selector/tolerance change, scientific acceptance,
training, package publication, commit or push follows from this diagnostic.

The [owning-fork report](https://github.com/uibcdf/hydramp/issues/1#issuecomment-6614434110)
was fetched back and verified exactly. The
[publication receipt](evidence/hydramp_activation_receiving_issue_updates.json)
retains its final body and the consumer receiving update.
