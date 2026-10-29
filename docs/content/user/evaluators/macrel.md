(evaluator-macrel)=
# Assessing peptide views with Macrel

**Accepted under D37 on 2026-10-29:** the executed Macrel 1.6.1 bundle is qualified
for D35 exploratory computational assessment/ranking, with the limits below.
Macrel supplies its native sequence descriptors and AMP/Hemo classifiers
{cite:p}`santos2020macrel`. PeptideMT owns orchestration, occurrence attribution
and selection; it does not reimplement the predictor.

## Compatible views and limits

The ordinary route accepts unchanged uppercase canonical amino-acid sequences
shorter than 100 residues, without leading M or explicit unassessed chemistry.
Empty, incomplete and incompatible proposals remain recorded and unscored.
Native Macrel clips initial M; PeptideMT excludes that view rather than assigning
the changed sequence's score to the original. This is a preprocessing limitation,
not biological invalidity of methionine.

The sequence view does not determine termini, protonation, stereochemistry or
crosslinks. Modified/cyclic/noncanonical realizations are not qualified by this
route. Successful direct short/long boundary probes do not widen ordinary scope
or demonstrate empirical usefulness at those lengths. A model AMP label is not
experimental activity; `NonHemo` is not a safety certificate.

## Requesting a live assessment

Use {func}`peptidemt.prepare_sequences`, then {func}`peptidemt.assess_macrel`.
The latter requires an explicit {class}`peptidemt.MacrelLimits` and snapshot ID.

:::{important}
The following code is displayed, not executed by documentation builds. Use it
only with an installed qualified resource and separately authorized bounds for
the actual host. The original four-call qualification allowance is exhausted.
:::

```python
from peptidemt import MacrelLimits, assess_macrel, prepare_sequences


def assess_example(limits: MacrelLimits):
    """Receive the limits authorized for the actual host from the caller."""
    inputs = prepare_sequences(["ACD", "MACD", "ACD"])
    return assess_macrel(
        inputs,
        snapshot_id="my-assessment",
        limits=limits,
        qualification_reference="reference-to-the-reviewed-bundle-evidence",
    )
```

Call `assess_example` only after supplying an authorized `MacrelLimits` instance.
A `qualification_reference` is a caller assertion, not certification.
The installed Linux child uses native `fasta_features` and prediction with
`keep_negatives=True`. MolSysMT serializes unchanged compatible views to the
native FASTA transport. Input occurrences are reconciled by opaque tokens.

Bounds cover submitted record count, UTF-8 sequence/token bytes, child wall time
in seconds and virtual address space in bytes. `memory_bytes` limits address
space, not resident RAM. Optional CPU affinity, priority, numerical/ONNX thread,
available-memory and temporary-storage controls are scoped to the child. There
are no automatic retries. Empty/all-incompatible pools launch no provider.

## Inspecting outputs and failures

Each native row preserves `Sequence`, `AMP_probability`, `is_AMP`,
`Hemolytic_probability`, `Hemolytic` and `AMP_family`, plus original extra fields.
The native strict `>0.5` label rule is retained. `AMP_family` is a native
composition category, not an experimentally established bioactive-family label.
All native negatives survive.

Result validation exposes changed views, unknown/duplicate/missing rows, invalid
scores and inconsistent labels as explicit eligibility/anomaly data. Operational
failures retain diagnostics and submitted-occurrence causes. No provider,
missing asset, import failure or timeout generates a synthetic prediction or
silently changes the method. See {ref}`macrel-qualification` for live versus
controlled evidence and {ref}`macrel-saved-case` for the actual saved outputs.

## Provenance and availability

Macrel 1.6.1's inspected official wheel and both model assets are identified by
hash in the qualification record. The scientific reference used a clean installed
MolSysMT source wheel at `3781031d0`; current reader development uses its own
documented later source. Development sources are an authorized route, independent
of public package availability. Unverified public installer hints remain disabled.

PeptideMT automatically installs or downloads no provider or model. Optional
Ackredit >=0.9.0 capture happens after observed completed operations and preserves
detached bibliography/original versions. Absence retains host bibliography;
diagnosed attribution failure retains completed results. Applications own
sessions; saved reading earns no new credit. See {ref}`about-peptidemt`.
