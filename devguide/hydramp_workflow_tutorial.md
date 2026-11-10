# HydrAMP saved-workflow tutorial

Status: **retained-data tutorial delivered; guarded replay verified**, 2026-11-03.
Owner: [PeptideMT #32](https://github.com/uibcdf/peptidemt/issues/32).
Resource disposition: [D41 experimental AMP acceptance](hydramp_dev3_acceptance.md).

The investigator requests continuing after acceptance and preservation of the
future scientific/product issues. The delivered [user tutorial](../docs/content/user/hydramp_workflow.md)
and [example](../examples/replay_hydramp_workflow.py) cover generation receipt →
matching assessment receipt → both unchanged selectors using original saved data.
They execute no generator, assessment, model, PCA, descriptor or attribution
provider. The example is displayed, not executed, during Sphinx builds.

The [evidence receipt](evidence/hydramp_workflow_tutorial.json) pins source,
original saved artifacts and actual guarded validation. Both original H4
generation/assessment file pairs retain their execution hashes. No sequence or
trace payload is copied to a new fixture or bundled with this tutorial. Users
need an authorized local copy; the page explicitly identifies that availability
limit and the separate already-public Macrel example.

## Actual verification

The exact installed consumer wheel from the accepted adapter milestone reads
both H4 batches. Each has sixteen proposals, fifteen eligible occurrences and
one retained exclusion. At k=4, both selected lists and all complete rankings
match the original H4 result summary exactly. Nine of thirty eligible occurrences
are native Macrel AMP-positive; no joint AMP-positive/NonHemo hit occurs. Those
are observations on saved labels, not new predictions or biological evidence.

Three separate negative invocations reject:

1. An incorrect generation digest before reading a scientific result schema.
2. Generation seed 1001 paired with assessment seed 1002, even with both actual
   file digests supplied.
3. The newer public generation receipt paired with the old private seed-1001
   assessment, despite identical sequence views. Full source context/provenance
   differs; equality of text alone is insufficient evidence of correspondence.

All five invocations run in the existing isolated installed consumer Python
3.14.10, CPU 0/1, one numerical thread, nice 10, 1 GiB virtual-address ceiling and
15 s per-case timeout. The guard blocks scientific/NumPy/Ackredit imports,
scientific-array opens, unreviewed JSON files and network. Native exit status
is zero for the two successful replays and two for each expected CLI rejection.
No scientific call occurs, and no old execution allowance is refilled.

## Ownership and remaining scope

The example calls public `HydrAMPReceipt.from_json`, `ResultSet.from_json` and
`select`; it introduces no library API, molecular parser, descriptor, prediction
or selection formula. Simple example CLI options use argparse and file hashing
uses hashlib. Molecular handling during real assessment remains MolSysMT-owned.
The public result readers retain strict JSON/float semantics and derive eligibility
from evidence. Incomplete generation is rejected for this walkthrough; saved
assessment failures/anomalies and all exclusions remain explicit in its summary.

The tutorial explains the separate private H4 and later public-generation proofs,
run-local occurrence identities, native versus Macrel scores and hypothetical
future real execution. It does not claim an executed all-public live chain,
scientific equivalence, joint feasibility, safety, a new supported environment
or a general efficacy benchmark.

This delivers the tutorial item under #32; comparison, standalone-product review,
other-family/successor feasibility and original-author questions remain open in
their owning issues. There is no new scientific decision, precision change,
training, GPU, external contact, package publication, commit or push. Retain
task resources through 2026-11-13 and review retention before cleanup.
