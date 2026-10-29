(macrel-qualification)=
# Qualification evidence and remaining uncertainty

D37 accepts the specific executed Macrel 1.6.1 bundle for exploratory ranking
within D35. This page explains confidence in the integration and the bounds of
that evidence. The original records, hashes and historical failed preparations
remain unchanged in the repository.

## Exact executed reference

| Item | Recorded identity |
| --- | --- |
| Numerical PeptideMT package | `7a299d1a9e1b264c2f872e94d35b76d67c548a0a` |
| Corrected qualification driver | `a1b5e3a178679eb71f47bf6a693a43955879b97d` |
| Macrel | Official 1.6.1 wheel and its original AMP/Hemo ONNX assets |
| Molecular serialization provider | MolSysMT source `3781031d0c1d08f34b2aa966ad0b82bf3b64a31d` |
| Environment | Linux x86_64, CPython 3.14.10, CPU ONNX Runtime 1.25.1 |
| Attribution | Public Ackredit 0.9.0 |

The four authorized calls took 21.38 s combined, with maximum observed child
RSS about 514 MiB, two assigned CPU cores, sequential execution, no GPU and no
model retry. The input-preparation error retained in the record occurred before
any inference and consumed zero calls. No new model call accompanies acceptance
or this documentation build.

## Checks supporting integration confidence

| Gate | Executed evidence |
| --- | --- |
| M1: native parity | Both real ONNX heads execute; all compared feature/prediction columns, values and dtypes match native extraction/prediction exactly, without added tolerance. |
| M2: both signs | Six evaluated occurrences cover three native AMP positives/three negatives and three Hemo/three NonHemo. These are model outcomes. |
| M3: attribution | All 17 original occurrences remain accounted for; duplicates/full repeated headers survive. Controlled missing/extra/reordered/duplicate output cases protect mapping. |
| M4: preprocessing/chemistry | Native initial-M clipping is observed directly; the adapter excludes that original view. Other incompatible/partial/explicit chemistry cases retain their causes. |
| M5: boundaries | Direct F/AA and 99/100/109/110 probes record operational output and native warning. Ordinary admission remains <100; empirical applicability is separate. |
| M6: precision/validity | Native scores and labels remain unchanged. Controlled malformed/nonfinite/missing outputs and exact-0.5 cases retain their distinct guards. |
| M7: selectors/replay | Both approved ordering policies, ties, duplicates, empty/short sets and k=0 are checked. The real saved case replays without a model. |
| M8: failures | Actual empty/all-incompatible pools launch no provider; controlled absence, transitive failure, missing/corrupt assets/output and timeout retain truthful failure evidence. |

Live comparisons and controlled faults have different roles. Shared native code
between direct Macrel and the adapter makes parity evidence about faithful
integration. It does not independently validate the predictor's biological
accuracy. Exact software test counts also remain bound to their original source:
101 for the original numerical candidate, 103 for its later delivery and 117 for
the later owner-backed reader delivery. Their recorded source/installed and
Linux Python 3.11–3.14 CI checks do not turn into new live model qualification.

## Scientific limits

This small frozen set is not an independent experimentally labeled benchmark.
It does not estimate sensitivity, specificity, calibration, efficacy or safety
for a future application. Duplicated occurrences and constructed length strings
are useful attribution/boundary cases, not independent biological validation.
Very short successful calls do not establish a valid predictive length domain.
No empirical lower-length threshold is invented.

Scores retain their native names and interpretation. Different resources' scores
must not be silently averaged or treated as interchangeable family probabilities.
The two selectors are computational reference orderings with no label filter,
deduplication or synthesis acceptance rule. Their actual consequences are shown
in {ref}`macrel-saved-case`.

The scientific acceptance is for this reproducible reference. Later source,
environment, model, preprocessing or chemistry changes need checks appropriate
to the affected boundary; a development update is not automatic scientific
equivalence. Public package/platform qualification and redistribution are
separate from this accepted source-development capability.

## Evidence trail

- [Native assessment](https://github.com/uibcdf/peptidemt/blob/ab9d83d611aaaf0659105020e8995fe49bc89d64/devguide/w3_assessment.md)
- [Exact sources, hashes and raw artifact manifest](https://github.com/uibcdf/peptidemt/blob/ab9d83d611aaaf0659105020e8995fe49bc89d64/devguide/evidence/w3_summary.json)
- [Owner-backed FASTA receiving](https://github.com/uibcdf/peptidemt/blob/6e79878211b14093a41bb52a6dbf02b9e959128a/devguide/evidence/fasta_owner_adoption.json)
- [Accepted central engineering receiving](https://github.com/uibcdf/molsyssuite/issues/152)
- [Component scientific disposition and delivery](https://github.com/uibcdf/peptidemt/issues/6)

The external SMonitor src-layout audit limitation remains owned in
[SMonitor #54](https://github.com/uibcdf/smonitor/issues/54), with direct installed
catalog/configuration checks retained. It is not a failure of either classifier.
The original pinned Pytest Receptor warning remains in its own historical test
receipt and does not alter the passing test exit status.
