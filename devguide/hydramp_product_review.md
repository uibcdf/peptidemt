# HydrAMP independent-product review: consumer handoff

Status: **initial owner review delivered; product work remains**, 2026-11-03.
Provider owner: [HydrAMP #4](https://github.com/uibcdf/hydramp/issues/4).
Consumer tracking: [PeptideMT #32](https://github.com/uibcdf/peptidemt/issues/32).
Existing disposition: [D41 experimental AMP use](hydramp_dev3_acceptance.md).

The investigator authorizes proceeding with the independent-tool review after
the retained-data tutorial. The provider's local modern worktree contains the
authoritative review, independent user guide, provisional model card and a
standard-library saved-native-record example. Their exact paths/hashes and
checks are retained in the [review receipt](evidence/hydramp_product_review.json).
These are local/uncommitted provider records, not falsely linked published files.

Owner paths relative to the HydrAMP modern worktree
`../hydramp/local_data/pytorch-comparison`:

- `devguide/pytorch_product_review.md` — assessment and prioritized backlog.
- `devguide/pytorch_user_guide.md` — independent Python API and setup boundaries.
- `devguide/pytorch_model_card.md` — intended use, evidence, chemistry and limits.
- `devtools/review_saved_pytorch_case.py` — no-engine/no-consumer saved example.

## Assessment and consumer implications

The exact modern core is an independent expert Python library. All five provider
Python files match the accepted wheel; no runtime source, dependency pin, lock,
weights, precision or licence is changed. The wheel declares NumPy/Torch and
optional modlAMP, without PeptideMT. Existing direct owner generation evidence
is reused; this review does not execute a new live generation.

The independent product remains incomplete:

1. Current entry-point documentation was stale/mixed with legacy preparation.
   New current-status banners, guide and model card now distinguish modern D41
   experimental use from historical remaining-work statements.
2. There is no modern console command or package `__main__`. A CLI is a possible
   workflow choice, not a prerequisite for a Python library or authority to
   design a new scientific interface silently.
3. `GenerationTrace` is an in-memory NumPy/native object without an independent
   portable scientific result/provenance reader/writer. A new owner contract
   needs explicit design review; PeptideMT's existing receipt is not copied back
   as if it were a provider-owned format. Metadata profile reuse remains #2.
   Before that design, review Recorda's platform record/provenance responsibilities
   and Ackredit's portable attribution contract; reuse applicable supported tools
   rather than introducing generic infrastructure in HydrAMP. The provider owns
   its scientific generation fields, not every surrounding record service.
4. The low-level API does not provide the host supervision, execution ledger or
   parent attribution supplied by PeptideMT's own adapter. An independent caller
   workflow needs its own documented policy and reviewed resource controls.
5. Local exact runtime closure and qualification do not supply a public installer,
   modern CI or release. uv's CPU index is not encoded by ordinary wheel runtime
   metadata. Source is still uncommitted, and wheel presentation lacks project
   URLs/long description. Those are product-delivery tasks under #4.

The priority is current documentation and a truthful reproducible example, then
an approved independent result/workflow contract, followed by any justified CLI
and clean install/CI/artifact delivery. None requires changing the accepted
scientific core merely to recover legacy FP32 identity.

## Actual independent validation

Static audit inspects wheel metadata, eight exports, twelve source test modules
and original-reference preservation without importing any scientific library.
Test-module inventory is not a new pytest execution or expanded test count.
Earlier 76 package/13 controller checks and all real scientific evidence retain
their exact original scope and receipts.

The new owner example runs successfully with **PeptideMT, NumPy, Torch and other
scientific imports blocked** in the isolated Python 3.14.7 worker. It reads only
the exact retained native developer JSON, SHA-256
`8976a778f981ee14875b6c3b2bcc3478e027ab6a6425b435d1c46cd3eec5a26a`.
It verifies the original 4 + 16 + 16 phase sizes and repeated native rows, and
prints counts rather than sequences. Original recorded calls are historical;
new scientific calls are zero. Wrong-file and missing-file cases reject, and
help works without the package or artifacts. All four invocations are bounded,
CPU-only, with network/scientific-array opens blocked.

This is one pinned qualification-record inspector, not a new general portable
trace schema. The raw native record is not redistributed or made a public
download. The provider guide's live API block is displayed and syntax-checked,
not executed. Current and legacy source/licence boundaries remain preserved.

## Remaining scientific and ownership limits

No new acceptance, other-family capability, biological result or model call
follows. Preserve both numerical/global-rank FAILs and the original's genuine
pointwise advantages. The small H4 pool's lack of a joint Macrel hit remains.
Artifact byte-identity/use limits and unpublished source/wheel status remain.
Scientific-output comparison is #3, numerical precision #1, family/successor
feasibility #5 and possible original-author handoff #6. Their work stays open;
no external contact or publication is made.
