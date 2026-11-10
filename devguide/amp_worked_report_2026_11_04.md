# Worked AMP evidence report — 2026-11-04

Status: **retained-data report delivered under PeptideMT #33**. No new model
execution. Task: examine what the current generate–assess–select route says
about desired AMP compatibility and adverse hemolysis, and which subsequent
computation would be informative. Navigation: [continuation plan](continuation_plan_2026_11_04.md).

## Evidence and coverage

This report uses the original [H4 execution](hydramp_h4_qualification.md), its
[receipt](evidence/hydramp_h4_execution.json), and the audit's hash-verified
[saved-pool observations](evidence/peptidemt_scientific_audit_2026_11_04_observations.json).
The seed-1001/1002 assessment SHA-256 values remain
`580d24df56b56c1a70284c5e0467fa1503a1cafd113e4891b6eb28449acacf78` and
`3a63dc1249b20a656fe1d480be3b056882cb2b9e38ee33f6b89f92aa3df39adc`.
The four W3 control occurrences are excluded from all generated-pool denominators.

| Question | Available evidence | Conclusion / unresolved part |
| --- | --- | --- |
| Did a real selected generator propose sequences? | Retained exact HydrAMP dev3 source/artifacts and generation/receiving evidence | Yes for the bounded historical route, including each original occurrence; no general generator-quality conclusion. |
| Were all proposals assessed unchanged? | Macrel result mapping and exclusions | 30/32 could use the approved route. Two initial-M sequences remain unassessed because native preprocessing would change them. They are not biological negatives. |
| Are the proposals AMP-compatible? | Nine native Macrel AMP-positive labels among 30 eligible assessments | A model-specific predictive observation; no MIC, organism-specific activity or calibrated probability claim. |
| Is hemolysis unfavorable? | Thirteen native Hemo labels and 17 NonHemo labels among those 30 | Predictive labels; no concentration-dependent lysis, cytotoxicity or safety evidence. |
| Does any evaluated proposal have both AMP-positive and NonHemo labels? | Zero of 30 eligible rows, also zero of 32 observable proposals | No observed complete joint-label result. Unsupported/unassessed rows remain unknown; this is not a biological failure-rate estimate. |
| Do the selectors change the decision? | The existing two exact selectors on each unchanged pool, k=4 | Yes; their shortlists have no overlap within either pool. Neither can select a joint-label hit absent from the pool. |
| Are candidates diverse or new? | 16 distinct strings in each pool | This report establishes within-pool exact-string uniqueness only, not cross-pool uniqueness, sequence-cluster diversity, chemical identity, novelty against training or mechanism. |
| Are molecular targets or CPP functions addressed? | No such executed operation in this route | Unassessed, even if an application stores related context. |
| Is chemical realization complete? | Preserved unresolved sequence chemistry and declared descriptor conventions | No implied stereochemistry, termini or modification support; no score transfer to all realizations. |

## Denominators and actual selections

There are 32 observable proposed occurrences, 30 compatible/eligible assessments
(93.75% route coverage), nine AMP-positive assessments (9/30) and 17 NonHemo
assessments (17/30). Counts overlap by their actual labels; zero have both desired
native labels. All nine AMP-positive assessments are Hemo. Failed or unsupported
assessment does not become a zero-valued score or a measured negative.

| Pool | Proposed / eligible | AMP-positive / eligible | NonHemo / eligible | AMP-first shortlist: AMP-positive / NonHemo | Hemolysis-first shortlist: AMP-positive / NonHemo |
| --- | --- | --- | --- | --- | --- |
| Seed 1001 | 16 / 15 | 4 / 15 | 9 / 15 | 4 / 0 of 4 | 0 / 4 of 4 |
| Seed 1002 | 16 / 15 | 5 / 15 | 8 / 15 | 4 / 0 of 4 | 0 / 4 of 4 |

These are two historical computational pools, not independent biological
replicates or a powered estimate. Native label rules and both selectors are
unchanged. The joint-label observation is an exploratory diagnostic, not a new
acceptance gate imposed by this report.

## Decisions this evidence supports

Changing ranking alone cannot create an absent joint-label result. It is more
informative to examine the proposal distribution and the evaluator's dependence
on sequence features before constructing a new selection rule. More generated
samples may yield different outcomes, but the current data do not quantify the
benefit of doing so. Exact-string duplicate collapse does not explain these
within-pool results.

The [prospective comparison brief](amp_comparison_brief_2026_11_04.md) proposes a
restricted control question about sequence order beyond length/composition. It
would distinguish one aspect of the current predictive result; it would not
prove biological superiority or resolve all generator/evaluator bias. The exact
model/data overlap and external experimental validity remain unknown.

An investigator can retain the existing computational results, choose that
control study, choose another endpoint, or defer new inference. A negative or
inconclusive study is a legitimate outcome. No new model evaluation, sequence
transformation or family/target claim occurs while preparing this report.
