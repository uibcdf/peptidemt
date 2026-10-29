# Increment 1: investigator review brief

Status: **recommendation prepared; investigator disposition pending**.
Owner: [PeptideMT #6](https://github.com/uibcdf/peptidemt/issues/6).
This reviews the commissioned D35/D36 result. It does not reopen its architecture,
M1–M8, chemistry or selectors. [Assessment](w3_assessment.md) and
[work order](increment_1_work_order.md) retain the detailed evidence and authority.

## Proposed disposition

Codex recommends accepting the **specific executed Macrel 1.6.1 bundle as an
exploratory computational assessment/ranking reference within D35**, subject to
the existing unchanged-sequence admission and limits below. This recommendation
is not an investigator-approved decision. Acceptance of these results does not
approve another model run, publication or increment.

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

Central guide/inventory receiving remains [MolSysSuite #152](https://github.com/uibcdf/molsyssuite/issues/152)
until its owner-reviewed changes are accepted and published. The existing
SMonitor #54 external audit limitation retains its own owner and bounded direct
catalog evidence. Neither is silently converted into scientific acceptance.

An investigator disposition should name this bundle and exploratory scope,
accept the stated limits, or identify the particular unmet gate or restriction
requiring further work. Record that disposition in #6 and the maintained guide.
No disposition has been inferred from authorization to prepare this review.
W4's tests, documentation, saved example and artifact evidence are available;
final increment-1 closeout awaits the separate receiving and investigator outcomes.
