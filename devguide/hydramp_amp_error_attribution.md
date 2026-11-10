# Why the original AMP result is closer in 58 retained cases

Status: **saved-data attribution completed; exact primitive-level attribution partial**,
2026-11-03. Provider owner: [HydrAMP #1](https://github.com/uibcdf/hydramp/issues/1);
consumer: [PeptideMT #8](https://github.com/uibcdf/peptidemt/issues/8), D39.

The investigator asks why the original implementation is closer in 58 of the
192 [full AMP-head FP64 comparisons](hydramp_amp_reference.md). Lower aggregate
modern error does not imply a smaller error on every input. This review reuses
the saved original/modern stage traces, whole-head FP64 reference and existing
modern-sigmoid replay on native logits. It evaluates **no model or activation**,
loads no weights/PCA and changes no runtime code or scientific acceptance band.
The [receipt](evidence/hydramp_amp_error_attribution.json) freezes the exact sources,
saved inputs, guarded analysis, artificial tests and aggregate report.

## Where the 58 final-score advantages appear

| Pre-sigmoid logits compared with whole-head FP64 | Cases among the 58 |
| --- | ---: |
| Original logits have smaller absolute error | **39** |
| Modern logits have smaller absolute error | **12** |
| Both logits are identical | **7** |

The 39 cases already favor native before the final sigmoid, though this does not
locate an individual recurrent primitive, timestep or dense accumulation. In the
seven identical-logit cases, the different final sigmoid implementation accounts
for the entire observed native-versus-modern output difference. The other twelve
show why a more accurate intermediate value need not yield the closer final
float32 output when activation approximations and rounding also change.

Across all rows, the score-winner/logit-winner table is:

| Final AMP error winner | Native logit closer | Modern logit closer | Equal logit errors |
| --- | ---: | ---: | ---: |
| Native (58) | 39 | 12 | 7 |
| Modern (91) | 13 | 57 | 21 |
| Equal AMP errors (43) | 7 | 25 | 11 |

## Existing fixed-logit counterfactual

Holding native logits fixed, switching only to the modern sigmoid makes error
against the **full-head** reference worse in **33/58** cases, better in **11/58**,
and unchanged in **14/58**. The eleven improvements subsequently become worse
than native after the upstream modern logit change. In **25/58**, this fixed-logit
kernel switch already reproduces the final modern score exactly, including the
seven identical-logit cases. These are overlapping observations, not additional
disjoint cause counts.

This comparison does **not** show that the modern sigmoid is less accurate at
those same mathematical inputs: the target is the full-head result and the
native logits already contain upstream error. A less accurate activation can
partly cancel an earlier error. In **20/58**, native final-score error has the
opposite sign to native logit error relative to FP64, consistent with such
compensation. The exact size of activation error at each engine's own logits
cannot be reconstructed from the current aggregate activation report; it would
need additional separately bounded activation-reference arithmetic. No such new
reference is evaluated here, and no remaining allowance is implied.

## Size and limits of the advantage

Among these 58 cases, the median native advantage in absolute error is
`5.5670e-8`, maximum `4.4942e-7`. Mean absolute error within this selected subgroup
is `4.7306e-8` native versus `1.1304e-7` modern. Their FP64 score ranges are
30 below 0.9, eleven in [0.9,0.99), three in [0.99,0.999), and fourteen at least
0.999. Thus the 58-case phenomenon is **not confined to near-one saturation**.
These bins are descriptive, not scientific acceptance thresholds.

Another metric must also remain visible: across all 192 outputs, native matches
the saved FP64 result cast to float32 in **48** cases and modern in **47**.
This is a comparison with an approximate FP64 target, not a formal correctly
rounded mathematical solution. Modern still has the lower maximum/mean/RMS
error and wins more pointwise comparisons (91 versus 58). No single metric
supports a universal numerical-superiority claim.

Eight guarded artificial tests pass for error comparisons, counterfactual
direction, ULP distance, ties, compensation signs and invalid data. They use the
existing isolated seven-distribution NumPy/Python 3.14 worker and published
Pytest Receptor 1.2.2. Model/framework imports, network, unreviewed scientific
artifact opens and NumPy exponential/tanh/matrix calls are blocked. Tests take
0.87 s including startup; saved-data analysis takes 0.32 s. Cumulative child
RSS high-water across both processes is 66.6 MiB, not an exclusive analysis
measurement. CPU affinity 0/1, one numerical thread, nice 10 and 1 GiB address
space ceiling preserve the existing 4 GB task intent.

**Disposition:** retain modern aggregate numerical improvements while reporting
these original advantages. Further diagnostics should distinguish upstream
rounding, final-activation error and compensation before proposing a correction.
Do not choose a runtime per peptide based on the unavailable FP64 answer, change
precision/ties/selectors or imitate legacy artifacts automatically. Original
FAIL reports, D40 scope, pending dev3 disposition and H0–H4 receiving remain
unchanged. No new learned/activation calls, GPU, training, release, commit or push
are authorized by this saved-data review. Retain resources through 2026-11-13.

The [provider findings](https://github.com/uibcdf/hydramp/issues/1#issuecomment-6613192150)
and [consumer update](https://github.com/uibcdf/peptidemt/issues/8#issuecomment-6613198584)
were fetched back and verified exactly; the [publication receipt](evidence/hydramp_amp_error_attribution_issue_updates.json)
records both comment identities and body digests.

## Later finite component attribution — 2026-11-03

The [activation follow-up](hydramp_amp_activation_attribution.md) now separates
FP64-evaluated upstream error from final-activation approximation and their sum.
Among the 58 native wins, 31 have opposing native component signs and 17 show
an actual reduction in absolute upstream error through compensation. These are
different predicates from this earlier saved final-error/logit-error sign
indicator (20); the original analysis remains unchanged. A more accurate modern
activation at identical native logits can worsen the complete score in eight
cases. Three of the seven modern ties are already tied in the FP64 reference
rounded to float32; four are not. Preserve these limits alongside the modern
aggregate improvements. The exact finite attribution is complete; private
consumer receiving and fresh integrated qualification are tracked separately.
