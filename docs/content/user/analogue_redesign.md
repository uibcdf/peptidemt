(analogue-redesign)=
# Analogue proposals and their ancestry

PeptideMT's provisional redesign boundary preserves ordered prototype proposals,
native HydrAMP analogue results and the relationship of every returned candidate
to its parent and attempted row. **R1/R2 have artificial-parameter evidence; R3
now passes one bounded real installed-consumer case.** That structural case
produces one candidate with improved HydrAMP scores but worse Macrel AMP and
hemolysis scores than its parent. It establishes receiving and reproducibility;
scientific utility, activity and safety remain unqualified. The accepted
experimental HydrAMP dev5 method and its numerical limits are separate from this
new consumer qualification; dev6 adds its reusable sequence codec.

## Inspect and replay saved data

The data API needs no HydrAMP, Torch, Macrel or model assets:

```python
from pathlib import Path
from peptidemt import HydrAMPAnalogueReceipt, ResultSet, select

receipt = HydrAMPAnalogueReceipt.from_json(
    Path("analogue-receipt.json").read_text(encoding="utf-8")
)
print(receipt.outcomes)  # Every original parent, including incompatible/no-hit.
print(receipt.issues)  # Receiving failures are recomputed.
children = receipt.proposals()  # Requires complete, consistent evidence.

assessment = ResultSet.from_json(
    Path("analogue-assessment.json").read_text(encoding="utf-8")
)
if assessment.inputs != children:
    raise ValueError("Assessment belongs to different proposals or ancestry")
amp_first = select(assessment, policy="amp-first", k=4)
hemolysis_first = select(assessment, policy="hemolysis-first", k=4)
```

Use `examples/replay_analogue_workflow.py RECEIPT --assessment ASSESSMENT --k 4`
for the same check and an ancestry report. It performs no new model/assessment
call. Content identifiers detect changed data/relationships; they do not
authenticate a producer or prove that caller-declared native work occurred.
Controlled evidence stays labelled controlled. Replay creates no fresh credit.
An unsupported schema or changed content digest raises an error at loading;
supported envelopes retain malformed native fields with recomputed issues.

## Input compatibility and returned views

Use the existing prepare_sequences, parse_fasta or read_fasta tools. FASTA
interpretation remains MolSysMT-owned. HydrAMP's first prototype route admits
nonempty canonical uppercase sequences of length 1–25, including initial M,
without explicit chemical annotation. Preserve all other inputs and their
incompatibilities rather than altering chemistry, case, length or symbols.
Unknown chemistry stays unknown; technical compatibility is not biological
applicability. HydrAMP-owned encode_sequences supplies the native model tokens.

Equal parent strings keep separate occurrences. Native attempts remain in
attempt-major order, with explicit provider-to-original-parent mapping. The
returned proposal pool follows original parent order then native lexical bucket
order, and retains equal candidates from different parents. Exact selector
ties favor the earlier proposal occurrence; no global deduplication follows.

Children inherit no measured parent properties or chemical annotations. Raw
model tokens and zero-removed projected strings remain separate views; native
scores are not copied to a re-encoded representation. An empty/initial-M child
remains recorded with its current Macrel incompatibility. Incomplete/malformed
generation data remain inspectable but cannot silently yield usable proposals.

## Explicit execution and interpretation

The provisional redesign_hydramp operation uses an explicit installed worker,
HydrAMPAnalogueBundle and HydrAMPLimits. The bundle pins encoder/decoder/heads,
source/runtime identity and use conditions; it requires neither PCA nor modlAMP.
One call makes two encoder, one decoder and four classifier evaluations.
It does not call Macrel, select, retry or refill. R3's exact separately authorized
allowance is exhausted. Further real use needs its own bundle/host/call review;
package availability alone is
insufficient. Host and worker must contain the same PeptideMT source and
installed version; the qualified local wheel and an unchanged shared editable
metadata label are not interchangeable. There is no public automatic
installation/acquisition route.

Assessing `receipt.proposals()` uses the existing assess_macrel operation with
its own explicit limits and qualification reference. Native HydrAMP AMP/low-MIC-
class improvement, Macrel AMP/hemolysis predictions and measured biological
effects are distinct. The two existing selectors are unchanged. Parent baseline
assessment is a separate explicit operation; parents are not automatically
added to the candidate pool. Higher native reward is not independent predictive
or biological improvement over the parent.

The implementation record, `devguide/hydramp_redesign_implementation.md`, retains
exact artifacts, artificial tests, failures and limits. The maintained
[PeptideMT #32 handoff](https://github.com/uibcdf/peptidemt/issues/32) tracks this
consumer work and its evidence.
