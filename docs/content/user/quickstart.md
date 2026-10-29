(user-quickstart)=
# Preparing inputs and selecting saved results

You can prepare proposals and replay selections without installing a scientific
engine. Every supplied occurrence remains distinct, even if sequences repeat.

```{doctest}
>>> from peptidemt import SequenceRecord, prepare_sequences
>>> inputs = prepare_sequences(["ACD", "ACD", "MACD", SequenceRecord(None)])
>>> [item.token for item in inputs]
['input-0', 'input-1', 'input-2', 'input-3']
>>> inputs[0].provider_sequence
'ACD'
>>> inputs[2].issues
('sequence_changing_native_preprocessing',)
>>> inputs[3].issues
('incomplete_sequence',)
```

{class}`peptidemt.SequenceRecord` retains the supplied sequence, full header,
chemical annotations, context, source and raw FASTA record. `None` denotes an
incomplete view; `""` denotes an empty one. Neither implies a molecular realization.
{func}`peptidemt.prepare_sequences` assigns run-local occurrence tokens; pair
them with the result snapshot rather than treating them as global identities.

## Reading FASTA through its owner

The selected route requires the MolSysMT development capability delivered under
[MolSysMT #513](https://github.com/uibcdf/molsysmt/issues/513). The provider used
by the recorded reader CI is source
`71fbe4f46d3c70e4e973c8025f01752a8c9b1084`; a new public package release is not a
prerequisite for authorized development-source use.

```python
from peptidemt import parse_fasta, prepare_sequences, read_fasta

records = parse_fasta(
    ">full repeated header\r\nAC\r\nD\r\n>full repeated header\nACD\n"
)
inputs = prepare_sequences(records)
# For an existing file: inputs = prepare_sequences(read_fasta("proposals.fasta"))
```

PeptideMT delegates to public `molsysmt.form.file_fasta.parse_records/read_records`.
Full headers, duplicate/empty records, source labels and verbatim record text
survive. Only CR/LF delimit lines; spaces, lowercase, stops and Unicode separators
remain literal. File paths follow the owner's `.fa`/`.fasta` contract.

Nonblank content before a header raises `ValueError` with the owner's diagnostic
as cause. Invalid UTF-8 remains `UnicodeDecodeError` with the owner diagnostic as
cause; other file I/O failures propagate. Unsupported paths retain the owner
argument error. An unavailable or broken provider is not replaced with a local
parser. See {func}`peptidemt.parse_fasta` and {func}`peptidemt.read_fasta`.

## Replaying results

Download the original JSON in {ref}`macrel-saved-case`, then read it with the
public result API. This reads existing evaluations and performs no inference:

```python
from pathlib import Path
from peptidemt import ResultSet, select

results = ResultSet.from_json(
    Path("qualified-computational.json").read_text(encoding="utf-8")
)
amp = select(results, policy="amp-first", k=3)
hemo = select(results, policy="hemolysis-first", k=3)
print(amp.selected)  # ('input-0', 'input-4', 'input-2')
print(hemo.selected)  # ('input-1', 'input-3', 'input-2')
```

{class}`peptidemt.ResultSet` retains original rows, precision, provenance,
incompatible proposals and diagnosed anomalies. Its `outcomes` explain
per-occurrence eligibility; `anomalies` describe duplicate or unknown output
tokens. A failure or missing value never becomes a negative model prediction.

{func}`peptidemt.select` applies exactly two lexicographic policies:

| Policy | Ordering |
| --- | --- |
| `amp-first` | AMP descending, hemolysis ascending, original occurrence |
| `hemolysis-first` | Hemolysis ascending, AMP descending, original occurrence |

Neither policy adds label filters, deduplication, rounding, score imputation or
a biological acceptance threshold. `k=0` retains ranking but selects nothing.
Inspect exclusions and model meaning before using a selected list for a purpose.
