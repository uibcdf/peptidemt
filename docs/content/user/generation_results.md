(hydramp-results)=
# Receiving and replaying HydrAMP results

{class}`peptidemt.HydrAMPReceipt` is the provisional public data boundary for
the selected modern HydrAMP AMP route. It receives an existing result, retains
its original evidence and supplies unchanged proposals for assessment. Importing,
constructing or reading a receipt loads no model, weights, PCA, NumPy or Torch.

The current evidence covers local experimental `hydramp-torch 0.0.0.dev3` and
its explicit descriptor profile. D41 accepts that exact resource for experimental
AMP generation, preserving its numerical and scientific limitations. This data
API does not launch generation. The separate provisional
{ref}`execution adapter <hydramp-execution>` has controlled installed tests and
one separately approved real-checkpoint case with exact retained native output,
trace, saved replay and captured parent attribution. Existing host/call permissions
are exhausted; a new scientific run still needs an authorized exact bundle
and resource allowance.

## Receiving an already produced trace

The provider's `GenerationTrace` comes from the selected unfiltered AMP route
with `properties=True`, an explicit seed and one attempt. The caller retains
the actual source, checkpoint/PCA, implementation, runtime, method attribution
and permitted-use evidence in {class}`peptidemt.Provenance`.

```python
from peptidemt import HydrAMPReceipt

# trace, requested_count and provenance belong to the already completed run.
receipt = HydrAMPReceipt.from_trace(
    trace,
    snapshot_id="my-generation-snapshot",
    requested_count=requested_count,
    provenance=provenance,
)
print(receipt.issues)
```

The example receives data; it does not invoke the generator. A provenance
reference identifies evidence supplied by the caller and does not certify an
arbitrary bundle. Receiving imported data creates no new scientific execution
or Ackredit credit. Preserve attribution that came with the original operation.

Native results remain in **returned order**. `returned_input_indices` maps them
to the original draw order, including duplicates. The receipt keeps original
tokens and their zero positions, sequence views, native AMP/MIC scores, sampled
latents and conditioning. Additional retained PCA output or actual submitted
decoder input may be supplied as `original_trace` fields when available; no
missing intermediate is reconstructed. FP64 conditioning and FP32 submitted
decoder input have different meanings.

`issues` records count mismatches, incomplete runs, malformed values and ambiguous
source correspondence. Raw anomalous output remains visible; per-occurrence
trace is attached only when correspondence can be established. For partial or
failed output, construct a receipt with the actual raw fields, `completed=False`
and reported `failures`. An empty completed result remains distinct from failure.
Neither path repairs, refills, deduplicates or retries generation.

## Saving without the generator

```python
from pathlib import Path
from peptidemt import HydrAMPReceipt

Path("generation.json").write_text(receipt.to_json(), encoding="utf-8")
restored = HydrAMPReceipt.from_json(Path("generation.json").read_text(encoding="utf-8"))
assert restored.to_json() == receipt.to_json()
inputs = restored.inputs
```

The `peptidemt.hydramp_receipt@1` schema preserves detached data and exact
float-hex values, including anomalies and original provenance. Both this reader
and {class}`peptidemt.ResultSet` reject duplicate JSON keys at any nesting level;
an overwritten sequence, score or provenance value cannot silently replace
original evidence. Unknown schema versions are rejected rather than guessed.
Changing scientific meaning or this v1 contract requires a documented migration;
the public Python interface remains provisional.

Every returned occurrence becomes an existing {class}`peptidemt.InputRecord`.
Its generation context retains original evidence and receiving issues. Sequence
views do not establish termini, stereochemistry or molecular realization.
Incompatible leading-M strings remain visible with the ordinary input reasons.
Molecular interpretation and file handling remain with MolSysMT.

## Separate assessment and selection

With a qualified Macrel resource and caller-authorized limits, these inputs can
be assessed using the existing optional route:

```python
from peptidemt import assess_macrel, select

# limits and macrel_qualification_reference must describe the authorized run.
results = assess_macrel(
    inputs,
    snapshot_id="my-assessment-snapshot",
    limits=limits,
    qualification_reference=macrel_qualification_reference,
)
amp = select(results, policy="amp-first", k=4)
hemo = select(results, policy="hemolysis-first", k=4)
```

This displayed block executes real assessment when a caller runs it; it is not
executed by the documentation build. The core and saved receipt remain usable
without Macrel. Native HydrAMP `amp`/`mic` values stay in generation context;
they never replace Macrel's AMP/hemolysis measurements. Native `mic` is not a
physical concentration. Input compatibility, generator qualification and a
scientific conclusion remain separate questions.

The existing selectors rank eligible Macrel evidence by the two documented
lexicographic preferences. They do not impose joint AMP/hemolysis feasibility.
In the bounded 32-proposal experiment, 30 strings were compatible and all nine
Macrel AMP-positive outputs were also Hemo-positive. These same sequences and
returned order matched the retained original HydrAMP outputs at those seeds.
This finite result demonstrates composition and a tradeoff, rather than measured
activity, safety or a port-specific sequence regression. See the
[executed report](https://github.com/uibcdf/peptidemt/issues/8#issuecomment-6616590411).
The maintained local qualification record is
`devguide/hydramp_h4_qualification.md`.

For a complete saved-data walkthrough with matching-file checks and both
rankings, follow {ref}`hydramp-workflow`.
