# Historical HydrAMP data receiver and autonomous saved review

Status: **local model-free implementation and controlled data qualification
complete**, 2026-11-05. Owner:
[PeptideMT #32](https://github.com/uibcdf/peptidemt/issues/32); scientific follow-up:
[HydrAMP #3](https://github.com/uibcdf/hydramp/issues/3).

The investigator's continuation after the D46 work-order report commissions the
first data-only receiver/inspection-replay cycle. Its
[implementation authority](evidence/hydramp_historical_data_authorization.json)
retains the exact pre-implementation [work order](hydramp_historical_work_order.md)
and a byte-identical copy. This extends preparation to implementation without
changing the approved scientific view or authorizing a native input/model stage.

## Delivered behavior

[`devtools/hydramp_historical_data.py`](../devtools/hydramp_historical_data.py)
receives the exact D46 authorization, reviewed historical manifest and C0 source
JSON. The three SHA-256 pins identify the approved finite set; there is no CLI
profile/hash override. Changed bytes return an explicit rejection rather than
becoming another approved dataset. Source file references inside JSON are
preserved as evidence, not followed automatically.

The tool validates occurrence/source/string-hash correspondence, chemistry and
omitted-feature evidence, original assay columns, raw values/censoring, unknowns,
exposure and repeated observations. The inspection retains every original
review row. No string is normalized, clipped, encoded or passed through an
unannotated `SequenceRecord`; no chemical identity or mass is reconstructed.

Saved snapshots retain the three complete original JSON texts and are
revalidated on load. No cached success or supplied summary is trusted. The
snapshot can be moved and reviewed without its source files, PeptideMT imports,
scientific engines or model assets. Saving never overwrites an existing file.
Only explicit, bounded JSON reads are supported; invalid/duplicate-key/nonfinite
JSON and unreviewed schemas/profiles are rejected.

This is a PeptideMT developer tool for finite scientific-data correspondence,
not a package-level input API, generic journal, molecular parser or chemistry
admission extension. Standard-library JSON/hashing helpers remain private.
MolSysMT/PyUnitWizard/HydrAMP retain their existing responsibilities; no missing
owner capability, new dependency or provider defect is established.

## Actual receiving and replay

The [execution evidence](evidence/hydramp_historical_data_implementation.json)
pins code, tests, sources, snapshot and guarded run. The actual finite files
receive successfully with:

- 42 table occurrences / 39 descriptive raw-string groups;
- 35 displayed numeric MIC values and seven `>` bounds;
- both original observations for each of the three repeated strings;
- six strings with published-pool overlap, unresolved checkpoint/fragment
  exposure and zero qualified independent test members;
- all source chemistry/unknowns retained, with unchanged general annotated-record
  admission and zero model payloads/calls.

The isolated guarded process receives copies, deletes those input copies and
then reopens the saved snapshot. Other source JSON reads are denied, including
the embedded original absolute paths. Receive/inspect native exit codes are
both zero and the complete reports compare exactly. The actual original files
remain unchanged. Peak RSS is **21.59 MiB**, elapsed **0.0743 s**, CPU affinity
0/1. Scientific/model/molecular packages, parameter/PCA reads, network and child
dispatch are blocked; none is used. This is data receiving/replay qualification,
not installed-package or biological validation.

## Developer commands

From the repository, use the shared development interpreter or its activated
environment. Supply explicit locations for the three unchanged reviewed files:

```bash
python devtools/hydramp_historical_data.py receive \
  --authorization devguide/evidence/hydramp_historical_view_authorization.json \
  --review local_data/hydramp-historical-view-vt45bq1w/review-manifest.json \
  --source local_data/hydramp-C0-audit-yqpagjub/measured-panel-audit.json \
  --output /tmp/hydramp-historical-review.json

python devtools/hydramp_historical_data.py inspect \
  /tmp/hydramp-historical-review.json
```

The output path must not already exist. Successful commands print a JSON
inspection. Invalid input produces a structured rejection on stderr and exit 2;
there is no execution command. The referenced ignored source files are local
audit artifacts, not distributed package data. A new clean checkout needs their
exact reviewed bytes; synthetic test controls are not substitutes for the panel.

## Controlled evidence and remaining scientific work

[`tests/test_hydramp_historical_data.py`](../tests/test_hydramp_historical_data.py)
contains **38 passing cases** using minimal synthetic observations and private
test bindings, not paper tables or a CLI authorization override. It exercises
the eighteen planned control themes, precise semantic rejection causes, immutable
source receiving, autonomous replay, malformed input, no-overwrite behavior,
unchanged public chemistry admission and fresh-process model/file/network/
dispatch guards. Synthetic controls do not qualify another real cohort.
One reporting-protocol test also passes: **39 selected tests total**, native
exit zero through Pytest Receptor. The earlier 36-case development pass is
retained separately; later changes add JSON overflow/surrogate handling.

Repository Ruff lint passes and all 174 Python files satisfy its format check.
No full scientific campaign, M1–M8 execution, original–modern model comparison,
learned/artificial-weight network or installed-package matrix is repeated.
There is no new model bundle, numerical acceptance, scientific endpoint/class
truth, unit conversion, independent cohort or biological quality verdict.

C0 remains partial. Next model-free scientific work is adequate source-use,
checkpoint-exposure and entity/assay/endpoint qualification, including whether
and how mass units can be related to the native pooled molar-class definition.
Preserve repeated values and source ambiguities. Any native codec/input/scoring
stage still needs a separate exact bundle/observations/batch/host/call plan and
approval. D35/M1–M8, D41/D44/D45/D46 and exhausted execution budgets persist.
No model execution, molecular construction, mass/alignment/unit operation,
installation, commit/push/release or third-party contact occurs in this cycle.
