# HydrAMP public data receiving and installed-wheel qualification

Status: **provisional public data API implemented and installed receiving passes**,
2026-11-03. Owner: [PeptideMT #8](https://github.com/uibcdf/peptidemt/issues/8).
The investigator requests continuing after the
[bounded private composition](hydramp_h4_qualification.md). This engineering
continuation does not infer broad dev3 acceptance or another model allowance.

## Delivered boundary

`from peptidemt import HydrAMPReceipt` now exposes the already tested receiving
class as a provisional public data contract. Its implementation remains private;
the old private import path is retained. `from_trace` receives an already produced
owner trace; direct construction can preserve raw partial/failed output.
`to_json`, `from_json`, `issues` and `inputs` retain their v1 meanings.

The provider owns generation, sampling, PCA, neural computations, original-token
scoring, descriptors and codec. PeptideMT owns detached receipt, occurrence
correspondence, input composition and interpretation. No descriptor formula,
molecular parser or chemistry operation is introduced. Native HydrAMP scores
stay in generation context and never replace Macrel columns. A readable receipt
or compatible input cannot qualify a generator. Unknown chemistry stays unknown.

The new [user page](../docs/content/user/generation_results.md), navigation and
[API reference](../docs/api/public.rst) document this actual data boundary and
the remaining scientific limits. At this data-receiving milestone, no generation execution API was exposed.
The subsequent [isolated adapter milestone](hydramp_execution_adapter.md) now
implements that separate route with installed controlled tests and a separately
authorized real-checkpoint case: 16 proposals, exact retained native results and
trace, exact saved replay and captured attribution. This execution proof is
separate from data receiving; broader scientific acceptance remains pending.

## JSON integrity fix and reuse

The private receipt reader previously used ordinary `json.loads`, which silently
accepts duplicate keys. For example a duplicated nested sequence or score tag
could overwrite the earlier value while leaving an otherwise valid document.
`ResultSet` already rejected duplicate keys. Its existing rule is extracted once
into the private data-layer `load_json` operation, and both readers use it.

Four regressions reject duplicated `seed`, nested `sequence`, `provider` and
`float_hex` fields. The existing ResultSet duplicate-key behavior is preserved.
Normal v1 output bytes, native fields, precision, correspondence and selection
are unchanged. This is structural evidence protection, not a new scientific
acceptance criterion or schema version. A future semantic/schema change needs
an explicit migration record; the Python interface remains provisional.

The optional-engine worksheet now records this persisted-data route separately.
It has no engine-availability requirement, provider import, installer, model
download or completed scientific operation. It adds no dependency/extra,
DepDigest execution guard, SMonitor operational event or Ackredit capture.
Existing ordinary argument/format errors remain `TypeError`/`ValueError`;
there is no new ArgDigest normalization or physical quantity conversion.
Original attribution survives data receiving without claiming another execution.

## Exact local wheel and checks

The [receipt](evidence/hydramp_public_receiving.json) pins the local, unpublished
`peptidemt-0.1.0+118.g1f8c444.dirty-py3-none-any.whl`, SHA-256
**`1f5eed48b1d94d6d0d97b85d40400a958d693623717f17d9265147f1abb8919e`**.
This is an uncommitted development candidate, not a public distribution or release.

The wheel is built offline without dependency acquisition, installed only in a
new task-owned virtual environment over the unchanged frozen W3 site-packages,
and verified against **22 original wheel members**, excluding generated RECORD.
Every installed package Python file matches both the exact wheel and current
source. Import origin is the new environment's installed package, not this
checkout or the older inherited PeptideMT distribution. `pip check` passes.
The original W3 and modern HydrAMP environments are not updated or uninstalled.

**41 installed qualification checks pass** on Linux/Python 3.14.10: 21 receipt
cases, 18 source-controller/transport cases and two W1 compatibility cases.
The controller tests remain source controls and do not become installed model
qualification. Published Pytest Receptor **1.1.0**, the repository's reviewed
test-tool pin in that frozen profile, agrees with native JUnit. Total process
time is 4.33 s, kernel child RSS high-water about 56.7 MiB.

The source profile also covers 41 distinct cases with published Receptor 1.2.2
in the seven-distribution Python 3.14.7 worker. Its first run has 40 passes and
one harness failure: an existing subprocess test assumes an editable/source
import path that the minimal worker did not supply. That single case then
passes with explicit source PYTHONPATH; both reports remain retained. No
implementation changed to address that test-environment mismatch.

The exact installed public API also rereads the original two H4 generation
receipts and all three assessment files, preserving every JSON byte after
canonical serialization, all 32 proposals, 34 eligible assessment rows including
the controls, both complete rankings and selections. Models, scientific artifacts,
network and attribution providers are blocked. This is a **saved-data replay**,
not another execution of H3/H4 or a new scientific comparison.

Sphinx 9.1.0 tools from the shared development profile build HTML and doctests
against this exact installed consumer package, with `-n -W --keep-going` and
engine/artifact/network guards. HTML builds with no warnings; six memory-input
doctests pass. Ordinary generation/assessment snippets are displayed, not run.
No hosted site is deployed. The installed receiving worker and documentation
tool environment are different profiles, recorded separately.

## Preserved history and remaining work

The source snapshot under
`local_data/hydramp-public-receiving-umevqhn1/prior-source/` retains the exact
pre-promotion consumer files. In particular the old H4-pinned private receiver
is recoverable byte-for-byte at SHA-256
`befeab875836a1d71277642fb541c95c13dab80fcff166eefc76f7c02ed98f04`.
Old receipts are immutable history and refer to their original candidate; they
are not relabelled as tests of this new wheel. Original models, reference outputs,
environments, numerical FAIL reports and scientific limits are preserved.

The earlier H4 sample has no generated Macrel AMP-positive/NonHemo hit; all nine
AMP-positive rows are Hemo-positive. Those same sequences/order match the
retained original. This remains a finite computational limitation, not evidence
of biological superiority or a port-specific sequence regression.

This step has **zero new model, PCA, descriptor or Macrel calls**. Existing call
allowances stay exhausted. A future generation execution adapter needs its own
implementation, host/call plan, actual installed-provider execution and optional
attribution evidence; new real execution needs the agreed approval. Investigator
scientific disposition remains pending. This installed data proof covers Linux/
Python 3.14 only; full-minor CI, other platforms, commit/push and public package
publication are not claimed. Retain resources through 2026-11-13.

The [existing consumer issue update](https://github.com/uibcdf/peptidemt/issues/8#issuecomment-6617017005)
was fetched back and verified exactly. The
[publication receipt](evidence/hydramp_public_receiving_issue_update.json)
retains the final body and identifier; #8 remains open for the remaining work.
