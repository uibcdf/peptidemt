# W1 sequence, result and selection tools

Status: engine-independent implementation under D35/D36,
tracked in [PeptideMT #4](https://github.com/uibcdf/peptidemt/issues/4).
Navigation: [index](README.md) · [scientific contract](v0_1_increment_1.md)
· [work order](increment_1_work_order.md).

These tools receive proposals and saved evaluation data. They do not install,
import or execute Macrel, calculate its features, supply molecular coordinates
or qualify any scientific model. The small public boundary is provisional;
global chemical identity and the architecture's deferred questions stay open.

## Ordered inputs

```python
from peptidemt import SequenceRecord, parse_fasta, prepare_sequences, read_fasta

inputs = prepare_sequences(
    [
        SequenceRecord(
            "ACD",
            header="original complete header",
            context={"target": "retained, unused by this operation"},
        ),
        "MACD",
        "ACD",  # a separate occurrence, even though the sequence repeats
    ]
)
fasta_inputs = prepare_sequences(
    parse_fasta(">same header\nAC\nD\n>same header\nACD\n")
)
# For a file: prepare_sequences(read_fasta("proposals.fasta"))
```

`SequenceRecord` retains sequence, full header, chemical annotations, context,
source and raw FASTA record. `None` is an incomplete sequence; an empty string
is an empty sequence. Inputs receive zero-based occurrences and run-local tokens
`input-0`, `input-1`, etc. These are not molecular identifiers. Pair tokens with
the result snapshot; do not merge different input pools by token alone.

FASTA ingestion joins sequence lines and removes line terminators only. It retains
CRLF/raw text, repeated headers and empty records; spaces, lowercase, stops and
modifications are not silently normalized. Nonblank content before the first
header raises `ValueError` with its line number. Blank input returns an empty
collection. I/O/encoding errors propagate with their original cause.

`InputRecord.issues` explains operation-specific incompatibilities. Only unchanged
uppercase canonical-symbol sequences shorter than 100 residues, without leading M
or explicit unqualified chemistry, receive a `provider_sequence`. Other proposals
remain intact. This does not prove empirical applicability for every length 1–99.
Explicit `chemistry` annotations are retained and left unassessed by this first
sequence-only route; no projection of an annotated chemical realization is
implemented. Use `context` for source/assay/target information that is not a chemical
realization. Neither field supplies invented termini, stereochemistry or bonds.

## Receiving original results

```python
from peptidemt import Provenance, ProviderRow, ResultSet

# A deliberately invented, non-scientific fixture; not a Macrel prediction.
snapshot = ResultSet(
    snapshot_id="example-fixture-1",
    inputs=prepare_sequences(["ACD"]),
    rows=(
        ProviderRow(
            "input-0",
            {
                "Sequence": "ACD",
                "AMP_probability": 0.4,
                "is_AMP": False,
                "Hemolytic_probability": 0.1,
                "Hemolytic": "NonHemo",
                "AMP_family": "ALP",
            },
        ),
    ),
    provenance=Provenance(
        provider="invented-fixture",
        bundle_id="toy-values-1",
        evidence_kind="controlled-fixture",
        details={"provider_executed": False, "scientific_data": False},
    ),
)
```

`ResultSet` receives already obtained data; it never calls an evaluator. Every row
keeps its native columns and explicit token. All input occurrences, unmatched,
duplicate and reordered provider rows survive. `outcomes` gives a row index and
issues for each occurrence; `anomalies` references duplicate/unknown original row
indices. Duplicate-token rows cannot be attributed uniquely and remain unranked.
Other individually reconciled rows can remain eligible. Headers/sequence equality
and row order are never used as an implicit join.

The required columns and strict `>0.5` labels follow the accepted Macrel contract.
Nonfinite/out-of-range/non-numeric scores, missing fields, inconsistent labels,
changed sequence views and unknown composition categories remain visible as
exclusion reasons. Negatives and additional native columns are preserved. No
descriptor formula, classifier, rounding or missing-score replacement is supplied.

The optional `failures` mapping retains producer-reported causes by token, such
as `unavailable_provider`, `missing_assets`, `load_failure`, `feature_failure`,
`scoring_failure` or `timeout`. These are explanations, not biological negatives
or an exhaustive platform status vocabulary. A failure prevents ranking even if
a row is also supplied. No row/score is manufactured for an empty/incompatible
pool or a failed producer. W2 will own actual invocation and diagnostic behavior.

One snapshot has one source bundle. `Provenance` requires provider, bundle identity
and evidence kind (`native`, `imported`, or `controlled-fixture`), with a detached
details mapping. Native/imported rows require a caller-supplied
`qualification_reference` before ranking; this reference is an assertion to audit,
not qualification performed by W1. Do not combine rows from different bundles or
mark real unqualified data as a controlled fixture to bypass qualification.
Controlled selection reports retain that evidence kind explicitly.

Actual producers must retain original dtypes, model/asset digests, import/source
identity, access route, terms/fixtures, settings, environment, actual execution,
warnings, artifacts, timing and applicable limits in `details`. No native telemetry
is invented. W1 accepts detached Python scalars/mappings/lists/tuples; a later
adapter must preserve the value and record original dtype when exporting native
array scalars. No cache reuse or chemical equivalence policy is introduced.

## Two policies and saved-result replay

```python
from peptidemt import ResultSet, select

restored = ResultSet.from_json(snapshot.to_json())
amp_first = select(restored, policy="amp-first", k=2)
hemo_first = select(restored, policy="hemolysis-first", k=2)
```

Both scores must be finite, comparable and attributable to the unchanged input
view under the agreed scope. AMP-first orders AMP descending, hemolysis ascending;
hemolysis-first reverses those priorities. Original occurrence order breaks exact
ties. The second objective only breaks first-objective ties. There is no native
AMP-label gate, safety threshold, averaging, calibration or deduplication.

`Selection` retains snapshot/provenance, policy, requested count, complete ranking,
selected and eligible-but-unselected tokens, excluded tokens/reasons and tie rule.
It returns at most k occurrences. k=0, empty rankings and unmet counts are valid;
negative counts and non-integer/boolean counts raise ordinary Python errors.
Two identical sequences can occupy two positions. Selection supplies no evidence
of biological activity, safety, chemical uniqueness or synthesis approval.

The versioned `peptidemt.results@1` JSON envelope uses tagged mappings and exact
hexadecimal Python floats, including invalid nonfinite values retained as anomaly
evidence. Tags cannot collide with user metadata because mappings are also tagged.
No rounding or unsafe object deserialization occurs. Reading validates schema,
occurrence order and data types and recomputes outcomes from original values.
Unknown schema versions, duplicate JSON keys and malformed data are rejected.
Metadata is copied into immutable containers; modifying a caller-owned list/dict
cannot rewrite historical evidence. Store `to_json()` text with ordinary UTF-8
file operations when persistence is wanted; this is a bounded snapshot format,
not a project database or global identity system.

Run `python examples/w1_selection.py` for the approved invented Q1–Q5 fixture.
Q1–Q5 correspond to input-0–input-4. AMP-first selects input-2/input-3;
hemolysis-first selects input-1/input-2; input-4 lacks a hemolysis score and remains
excluded. No provider executes. Tests exercise engine-free parts of M3–M8 only;
live parity, asset/runtime qualification and both actual ONNX heads remain W2–W3.
