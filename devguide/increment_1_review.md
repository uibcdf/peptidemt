# Increment 1: investigator review brief

Status: **accepted by the investigator on 2026-10-29 under D37**.
Owner: [PeptideMT #6](https://github.com/uibcdf/peptidemt/issues/6).
This reviews the commissioned D35/D36 result. It does not reopen its architecture,
M1–M8, chemistry or selectors. [Assessment](w3_assessment.md) and
[work order](increment_1_work_order.md) retain the detailed evidence and authority.

## Accepted disposition

The investigator accepts the specific executed Macrel 1.6.1 bundle as an
exploratory computational assessment/ranking resource within D35, retaining the
existing unchanged-sequence admission and the limits below. Macrel is one
optional evaluator in the extensible resource catalog. Acceptance follows the
in-conversation evidence report and explicit investigator decision; the earlier
recommendation is now adopted with that scope. It grants no new inference
allowance, publication, chemistry expansion or later increment.

The exact numerical package is PeptideMT source
`7a299d1a9e1b264c2f872e94d35b76d67c548a0a`, with qualification driver
`a1b5e3a178679eb71f47bf6a693a43955879b97d`. It ran on Linux x86_64/Python
3.14.10 with Macrel 1.6.1, CPU ONNX Runtime 1.25.1, Ackredit 0.9.0 and the
unchanged MolSysMT owner-source wheel at
`3781031d0c1d08f34b2aa966ad0b82bf3b64a31d`. Exact artifact/model hashes,
dependency versions and the recorded use/fixture terms remain in the
[preflight](evidence/w3_preflight.json), [summary](evidence/w3_summary.json) and
[native manifest](evidence/w3_native/manifest.json).

Later delivery and FASTA adoption have their own
[installed receipt](evidence/w3_delivery.json) and
[owner-reader receipt](evidence/fasta_owner_adoption.json). They preserve the
original numerical producer and cannot be relabeled as a new model execution.
Routine development uses editable sibling revisions; it does not await a public
MolSysMT package release. The scientific reference above remains identifiable.

## Evidence supporting that recommendation

- Four authorized CPU calls completed; both native heads execute and all compared
  native feature/prediction columns, values and dtypes match exactly. No tolerance
  or rounding was introduced. Both signs for both heads are represented.
- All 17 input occurrences remain accounted for: six scored and eleven excluded.
  Duplicate sequences and full repeated headers retain independent identities.
  Native initial-M clipping is observed directly; ordinary admission excludes
  that original view rather than silently submitting a changed peptide.
- M1–M8 retain their documented live/control allocation. Direct F/AA and
  99/100/109/110 probes establish operational behavior only. Malformed-output,
  absence, timeout and row-reconciliation controls remain identified as controls.
- The real saved snapshot replays both approved policies unchanged. Portable
  attribution retains actual software versions and detached bibliography; a
  fresh reader imports no Macrel/Ackredit and earns no new calculation credit.
- The latest owner-backed FASTA delivery passes 117 source/installed tests and
  four Linux Python 3.11–3.14 installed-reader CI lanes. Those are engineering
  compatibility checks; real model execution remains the specific 3.14.10 bundle.

## Limits to accept explicitly

The ordinary route uses unchanged uppercase canonical sequence views shorter
than 100 residues, without leading M or explicit unassessed chemistry. It does
not infer termini, stereochemistry, crosslinks or a molecular realization.
Operational success on F/AA or direct out-of-scope length probes supplies no new
empirical applicability claim and does not widen ordinary admission.

Native AMP/Hemo outputs are computational predictions. A positive AMP score
does not demonstrate activity; `NonHemo` does not certify safety. AA's native
AMP probability of 0.5148515701293945 is preserved rather than interpreted as
empirical validation. The training-length/domain uncertainties in the assessment
remain explicit; no new lower-length or biological threshold is adopted.

The approved reference selectors impose no label filter or deduplication. With
k=3, `amp-first` returns `input-0`, `input-4`, `input-2`, including two duplicate
occurrences with native Hemo labels. `hemolysis-first` returns `input-1`,
`input-3`, `input-2`, including native AMP negatives. These are the intended
computational ordering rules, not synthesis or biological acceptance decisions.

The executed host envelope used two assigned CPU cores, no GPU, sequential
children and no model retries. Actual combined wall time was 21.38 s and peak
child RSS about 514 MiB. The four-call allowance is exhausted; this review uses
saved evidence only. No new live execution follows from accepting the receipt.

## Closeout distinction

Central engineering receiving is complete under
[MolSysSuite #152](https://github.com/uibcdf/molsyssuite/issues/152), accepted at
`b12f7230b297cdc0b22a649e6e625207d7fc4c1d`. PR #154 is resolved through that
reviewed direct route. The existing SMonitor #54 external audit limitation has
its own owner and direct catalog/configuration evidence; public delivery is
separate and uncommissioned.

The investigator also requested provisional user documentation covering actual
use, limitations and confidence evidence. Its [build guide](../docs/README.md)
records the inspected sibling conventions. W4 documentation/build checks pass,
with the [acceptance receipt](evidence/increment_1_acceptance.json) retaining the
separate identities and #6 receiving final exact-head CI conclusions. The new
documentation-tooling inventory handoff is MolSysSuite #156; earlier #152
receiving remains completed. Original model
artifacts, versions, evaluations and the exhausted four-call allowance are
preserved. This is acceptance of the bounded result, not a new execution or
acceptance of future resources.
