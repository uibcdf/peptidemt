(macrel-saved-case)=
# Replaying the accepted Macrel case

The original mixed pool has 17 proposals: six native evaluated occurrences and
eleven excluded occurrences. Inputs `input-0` and `input-4` are separate copies
of the same 24-residue sequence. AA and F are upstream very-short operational
fixtures; `input-13` is a constructed length probe.

| Occurrence | Length | Native AMP score | Native hemolysis score |
| --- | ---: | ---: | ---: |
| `input-0` | 24 | 1.0 | 0.9207921028137207 |
| `input-1` | 56 | 0.04950517416000366 | 0.04950517416000366 |
| `input-2` (AA) | 2 | 0.5148515701293945 | 0.37623775005340576 |
| `input-3` (F) | 1 | 0.3960397243499756 | 0.28712886571884155 |
| `input-4` | 24 | 1.0 | 0.9207921028137207 |
| `input-13` | 99 | 0.0792081356048584 | 0.6336634159088135 |

With k=3, `amp-first` selects `input-0`, `input-4`, `input-2`;
`hemolysis-first` selects `input-1`, `input-3`, `input-2`. The first policy includes
duplicate Hemo-labeled occurrences and AA. The second includes native AMP
negatives. Both implement the approved ordering; neither list is a biological
or synthesis recommendation.

Download the {download}`original result JSON <../../../devguide/evidence/w3_native/qualified-computational.json>`
for the short reader in {ref}`user-quickstart`. The payload retains original
producer versions, exclusions, exact scalar values, native dtypes and portable
bibliography. Reading it does not call Macrel or create new scientific credit.

From a source checkout with PeptideMT installed, you can also run:

```bash
python -I examples/replay_macrel_qualification.py
```

The maintained script includes assertions about the original result and both
selections. It is shown below; Sphinx does not execute this literal inclusion.

```{literalinclude} ../../../examples/replay_macrel_qualification.py
:language: python
```

See {ref}`macrel-qualification` before drawing conclusions from these scores.
The original inference used memory proposals. The later owner-backed FASTA
reader has separate tests and is not relabeled as part of that model run.
