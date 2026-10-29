---
summary: Delegate source-preserving FASTA interpretation to the molecular-system owner.
issue: uibcdf/peptidemt#5
status: open
opened: 2026-10-27
closed:
verification: measured
area: [input, interoperability, ownership]
guard:
normative:
blocked_by: []
supersedes: []
---

# Delegate FASTA ingestion to MolSysMT

## Provider delivery update — 2026-10-28

MolSysMT #513 is closed as implemented at published source `ae24866ba`:
public `file_fasta.parse_records/read_records` retain raw records, full headers,
every occurrence and source spans, without Bio or chemical admission. Existing
normalized conversions are unchanged; no new package is published. The former
provider blocker is resolved; this consumer record remains open for actual API,
source/dependency and behavioral qualification, then migration/removal of the
local parser. W3 continues with in-memory proposals as explicitly directed.
The previous measurements below remain historical evidence, not observations of
the new provider source or a completed consumer adoption claim.

## Development environment update — 2026-10-28

The investigators clarified that current platform development consumes the
components' development sources in the shared Conda environment; a public
MolSysMT package release is not a migration prerequisite. The clean editable
clone was advanced from `3781031d0` to
`71fbe4f46d3c70e4e973c8025f01752a8c9b1084` with `git pull --ff-only`.
Reinstalling editable with `--no-deps --no-build-isolation` refreshed its stale
metadata to `0.23.0+322.g71fbe4f46`, without changing dependency versions.

Python 3.14.7 in `molsyssuite@uibcdf_3.14` imports that clone. Actual public
`file_fasta.parse_records/read_records` calls preserved complete headers,
repeated occurrences, empty records, raw text and decoded-character spans under
LF, CRLF and CR. A separate `ACD` conversion/recognition/FASTA serialization
probe passed. These probes execute no models. The environment retains the same
twelve unrelated dependency findings; no clean dependency-closure claim follows.

The remaining work is PeptideMT's adapter, error/compatibility behavior and
repeatable dependency acquisition/tests, followed by removal of its local
parser. The provider capability is available now in development. This evidence
does not relabel the original W3 wheel or qualify new model executions.

## What

The investigators reaffirmed owner-based reuse across MolSysSuite after reviewing
W1. PeptideMT currently implements FASTA interpretation in `parse_fasta` and
`read_fasta`. MolSysMT owns reusable molecular-format ingestion; PeptideMT retains
design occurrence attribution, original evidence and scientific admission policy.
The provider proposal is [MolSysMT #513](https://github.com/uibcdf/molsysmt/issues/513).
This consumer migration follows [PeptideMT #4](https://github.com/uibcdf/peptidemt/issues/4)
without replacing its exact-source behavioral receipts or historical record.

## How and measured evidence

The installed MolSysMT source was
`uibcdf/molsysmt@3781031d0c1d08f34b2aa966ad0b82bf3b64a31d`, reporting
`0.23.0+286.g3781031d0`, in `molsyssuite@uibcdf_3.14`. Three controlled temporary
FASTA files were passed through public `msm.convert(path,
to_form="biopython.SeqRecord")` and the delivered PeptideMT parser. No peptide
geometry, topology, target or scientific model was constructed or evaluated.

| Probe | MolSysMT observation | Consumer implication |
| --- | --- | --- |
| Full repeated descriptions, CRLF/multiline and empty last record | Both routes returned ACD, ACD and an empty sequence, retaining full descriptions and occurrences. MolSysMT's returned objects did not expose verbatim record text. | Do not falsely report that full headers, duplicates or empties are lost. Retain raw source correspondence for D35. |
| Header plus sequence lines containing spaces, lowercase and a stop | The joined unnormalized text was `" acD A*"`; MolSysMT returned `"acDA*"`. | A blind replacement changes the supplied sequence view. Parsing transformations need explicit evidence; PeptideMT's strict admission cannot silently accept a changed input. |
| Leading-M sequence MACD | MolSysMT preserved MACD. | The M-clipping restriction concerns the approved Macrel route, not general molecular validity or a MolSysMT defect. |

The relevant public `basic/convert.py`, FASTA/one-letter forms, peptide builder,
mutator and chemical-template entry points were compared with inspected remote
main `cf4f415503616cdd2eeef0784abd0df9dcea3a7e`; those relevant paths were
unchanged. This does not claim execution of the newer entire source. The primary
MolSysMT worktree stayed clean and was not advanced or edited. Temporary probe
files were removed on completion.

Sources: [public conversion](https://github.com/uibcdf/molsysmt/blob/3781031d0c1d08f34b2aa966ad0b82bf3b64a31d/molsysmt/basic/convert.py),
[FASTA-to-SeqRecord route](https://github.com/uibcdf/molsysmt/blob/3781031d0c1d08f34b2aa966ad0b82bf3b64a31d/molsysmt/form/file_fasta/to_biopython_SeqRecord.py),
[FASTA-to-topology route](https://github.com/uibcdf/molsysmt/blob/3781031d0c1d08f34b2aa966ad0b82bf3b64a31d/molsysmt/form/file_fasta/to_molsysmt_Topology.py).
The last route builds a representative-atom topology and normalizes residue
letters; it is not a substitute for preserving incomplete source proposals.

## Why and ownership

General format interpretation belongs to its owner even when a consumer needs
additional provenance. Calling the local parser only "proposal ingestion" does
not settle that ownership question. The previous W1 characterization is corrected
by this follow-up; its delivered behavior and 53-test/installed/CI evidence remain
facts about their original source, not evidence that reuse is already complete.

Source-preserving ingestion is independently useful to other consumers. The
provider chooses the API, parser implementation, optional dependencies and any
compatibility changes. PeptideMT must not implement a replacement general parser,
use provider private internals or relax D35 to fit a normalized view. It will
retain source-to-occurrence correspondence and its own ranking/admission rules.

## What was refuted

- This is not a claim that normalizing FASTA whitespace is an upstream bug.
- MolSysMT already preserves full descriptions, repeated entries and leading M
  on the tested SeqRecord route; none is an alleged missing operation.
- Existing MolSysMT #243 concerns avoidable Biopython use in elementary sequence
  operations and explicitly separates FASTA/PIR. #242 evaluates a sequence value
  object. Neither establishes the requested source-preserving reader, and no
  new sequence class is required by this consumer proposal.
- W1 does not construct/modify molecular topology, coordinates or targets.
  Its candidate ranking is distinct from MolSysMT atom/group selection. Scientific
  route checks, occurrence/provenance records and saved prediction data remain
  consumer responsibilities.

## Interim duplication and removal

Owner: Diego Prada-Gracia/UIBCDF for PeptideMT adoption; MolSysMT owns provider
triage and delivery. Review by **2026-11-27**. The existing local FASTA code is
retained unchanged for reviewed migration, with its ownership gap visible here;
this is not a claim of an accepted permanent exception or permission to extend
the duplicated parser. Removal requires an owner-approved public capability,
exact source/artifact and dependency-route evidence, then a consumer migration
that preserves D35 input behavior and both selectors. Reporting alone does not
approve the provider API, change another repository's source or publish packages.

## Acceptance criteria

1. Qualify an actual public MolSysMT route for this use, preserving original text,
   full headers, duplicates, empty records and occurrence correspondence; expose
   transformations or incompatible input explicitly.
2. Delegate reusable FASTA interpretation, retaining PeptideMT's design-specific
   provenance/admission and strict sequence-preservation requirements.
3. Remove duplicated format handling, preserve compatibility intentionally and
   exercise whitespace, malformed records, emptiness, ties and saved-result replay.
4. Adopt actual dependency acquisition and applicable optional-route diagnostics
   with the owner tools when the route appears; never add an unused dependency
   or claim qualification from import alone.
5. Update linked provider/consumer issues and archive this record only on verified
   migration. D35/D36 and M1–M8 retain their accepted scientific meaning.
