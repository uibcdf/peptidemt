(hydramp-workflow)=
# From generated proposals to saved assessment and selection

This tutorial follows the accepted experimental AMP workflow through its
**existing saved results**. Replaying it imports no HydrAMP, Torch, NumPy,
Macrel, MolSysMT or ONNX Runtime, loads no model/PCA and creates no new scientific
attribution. It uses the public PeptideMT data readers and both existing selectors.

The retained experiment produced two batches of sixteen proposals, seeds 1001
and 1002. Thirty strings were compatible with the accepted Macrel route; two
leading-M occurrences remain explicitly excluded. The experiment used a private
source extension. The later public generation adapter has its own real installed
case; this tutorial does not turn those separate proofs into a newly executed
all-public live chain. D41 accepts the reviewed resource for experimental AMP
generation, with its recorded scientific limits.

## The three stages

| Stage | Real operation | What this tutorial does |
| --- | --- | --- |
| Generation | HydrAMP produces an unfiltered AMP batch and its original trace. | Read the original {class}`peptidemt.HydrAMPReceipt` JSON. |
| Assessment | Macrel evaluates compatible, unchanged strings; incompatible proposals remain present. | Read the matching {class}`peptidemt.ResultSet` JSON, with original producer provenance and exclusions. |
| Selection | PeptideMT applies a declared computational preference. | Run {func}`peptidemt.select` with both current policies on the saved assessments. |

Sequence, token, chemistry and numerical meanings remain unchanged by replay.
The library re-derives eligibility from saved evidence; it does not trust an
imported eligible flag. A failure or missing result is not a negative prediction.

## Obtain the matching retained files

Use a source checkout with the development PeptideMT installed and your
authorized local copy of the H4 receipts. The original task retains them under:

```text
local_data/hydramp-h4-qualification-mc6nax6v/run/assessment/
```

These research receipts are **not bundled downloads**. This page does not
redistribute their peptide sequences or full trace payloads. If the files are
unavailable, do not reconstruct them or substitute an invented result under the
same name. The publicly bundled {ref}`Macrel saved case <macrel-saved-case>`
provides a separate starting example without those local artifacts.

Original byte identities, retained in the H4 execution receipt:

| File | SHA-256 |
| --- | --- |
| `seed_1001-generation.json` | `ecf2b2744a573b93dae55975562c0ddd7bf8a7486fe7e75c19ca93a3c8ee3161` |
| `seed_1001-assessment.json` | `580d24df56b56c1a70284c5e0467fa1503a1cafd113e4891b6eb28449acacf78` |
| `seed_1002-generation.json` | `12561ebc504c6f8da7ac031830bcc634821cc2be6739907f76fe6cea53b1637a` |
| `seed_1002-assessment.json` | `3a63dc1249b20a656fe1d480be3b056882cb2b9e38ee33f6b89f92aa3df39adc` |

## Replay a batch

From the repository root, run the maintained example against seed 1001:

```bash
saved_dir=local_data/hydramp-h4-qualification-mc6nax6v/run/assessment
python -B -I examples/replay_hydramp_workflow.py \
  --generation "$saved_dir/seed_1001-generation.json" \
  --generation-sha256 ecf2b2744a573b93dae55975562c0ddd7bf8a7486fe7e75c19ca93a3c8ee3161 \
  --assessment "$saved_dir/seed_1001-assessment.json" \
  --assessment-sha256 580d24df56b56c1a70284c5e0467fa1503a1cafd113e4891b6eb28449acacf78 \
  --k 4
```

For seed 1002, change both filenames and both hashes to its table entries.
The script verifies each digest before decoding JSON. It then requires exact
equality of the complete generation inputs and assessment inputs, including
occurrence order, source context and provenance. Matching sequence strings alone
does not establish that two files describe the same operation. For example,
mixing the newly executed public generation receipt with the earlier private
assessment is not justified by their identical sequence views.

The example prints counts, exclusions, reported failures, row anomalies, native
label observations and both full rankings using occurrence tokens. It does not
print peptide sequences or replace their original files. Its source is displayed
below; Sphinx does not execute this inclusion:

```{literalinclude} ../../../examples/replay_hydramp_workflow.py
:language: python
```

## Expected observations

Both batches retain sixteen proposals and have fifteen eligible occurrences.
At k=4 the unchanged selectors produce:

| Batch | `amp-first` | `hemolysis-first` |
| --- | --- | --- |
| Seed 1001 | `input-0`, `input-6`, `input-1`, `input-9` | `input-8`, `input-14`, `input-13`, `input-15` |
| Seed 1002 | `input-3`, `input-2`, `input-7`, `input-0` | `input-11`, `input-14`, `input-6`, `input-13` |

An occurrence token is local to its assessment snapshot; `input-0` from one
batch is not identified with `input-0` from the other. Preserve the snapshot and
all duplicate occurrences when recording a selection.

`amp-first` orders by Macrel AMP descending, hemolysis ascending and original
occurrence. `hemolysis-first` reverses the first two priorities. HydrAMP's native
AMP/MIC fields remain generation evidence and do not replace these Macrel values.
Native MIC is not a measured concentration; AMP scores are not demonstrated
activity. No joint-label gate, trimming, preselection, rounding or refill is added.

Across both pools, nine of thirty compatible occurrences are Macrel AMP-positive,
and all nine are also Hemo-positive. No joint AMP-positive/NonHemo hit occurs.
All four AMP-first selections in each batch are Hemo-positive; all four
hemolysis-first selections are AMP-negative. The selectors faithfully implement
preferences, without guaranteeing joint feasibility or biological safety.

These same sequence pools/order match retained original HydrAMP output at these
seeds. The joint-label result is therefore not a port-specific sequence regression
on these inputs. It is a finite computational observation, not a general efficacy
benchmark, a synthesis recommendation or independent biological validation.

## Moving from replay to a new run

For a future generation, follow {ref}`hydramp-execution` with the exact reviewed
bundle, worker interpreter, use conditions and caller-authorized limits. Receive
and save its actual receipt, then use its own `inputs` for the separately
authorized Macrel assessment described in {ref}`hydramp-results`. Save that
matching assessment before applying these same selectors.

Constructing configuration objects, reading this tutorial or accepting D41 does
not replenish an exhausted execution allowance. New generation/assessment needs
its actual finite host/call authorization. Documentation builds and this replay
example perform neither operation. Molecular-system transport remains MolSysMT-
owned when assessment executes; saved JSON readers require no molecular parser.

The original [H4 execution report](https://github.com/uibcdf/peptidemt/issues/8#issuecomment-6616590411),
[public adapter result](https://github.com/uibcdf/peptidemt/issues/8#issuecomment-6618614382)
and [D41 decision](https://github.com/uibcdf/peptidemt/issues/8#issuecomment-6619182159)
retain their distinct evidence. Future scientific/product questions stay in
[PeptideMT #32](https://github.com/uibcdf/peptidemt/issues/32) and its linked
provider issues; no new benchmark or family capability is inferred from replay.
