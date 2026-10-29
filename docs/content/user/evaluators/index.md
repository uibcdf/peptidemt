(evaluator-catalog)=
# Evaluators and functional evidence

An evaluator contributes method-specific evidence about a supplied peptide view.
PeptideMT preserves that view, the resource's identity and original outputs,
then applies an explicitly selected computational policy.

Macrel is the first accepted optional resource. It predicts native AMP and
hemolysis labels/scores for compatible sequence views. Hemolysis is an additional
adverse-effect prediction; it does not define every bioactive family. Other
resources may later assess other families or complement the same family.
Scores from different resources are not automatically calibrated,
interchangeable, independent or suitable for averaging.

This catalog documents implemented resources only. A new evaluator needs its own
scientific role, representation/domain limits, original outputs, provenance and
qualification evidence. No universal evaluator/plugin API is introduced here.

```{toctree}
:maxdepth: 1

macrel
macrel_qualification
```
