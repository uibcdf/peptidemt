# Migration transfer: GitHub source and private ZIP

Status: **investigator-commissioned source synchronization and private transfer**,
2026-11-10. Owner: [PeptideMT #33](https://github.com/uibcdf/peptidemt/issues/33).
This follows the [decision-context checkpoint](migration_checkpoint_2026_11_10.md).
The investigator explicitly asks for a clean PeptideMT clone synchronized with
GitHub, and a ZIP containing the material unavailable from GitHub with placement
instructions. This supplies PeptideMT commit/push authority for the reviewed
existing work; it does not commission new science, a package release or a
HydrAMP source commit/push.

## Source publication and privacy boundary

Publish the reviewed PeptideMT implementation, tests, maintained documentation
and metadata-only evidence in its existing repository. A normal clean Git
status is the source-completion condition; retained ignored data need not be
deleted. Fetch/pull preserves human work and uses fast-forward-only integration.
No destructive reset, clean or forced push is required.

The complete source/administrative selection passes 440 tests locally with the
retained published Pytest Receptor 1.2.2 wheel. Ruff and format checks pass.
This is controlled code/data verification, not a repeated learned campaign or
proof of scientific performance. The shared profile still has the known
Amber-extra dependency failures under MolSysSuite #82; selected test success
does not relabel that global check. Exact-head Actions remain separate evidence.

Original private native H4 preparation/execution records remain byte-preserved
and explicitly ignored at their original `devguide/evidence/` paths. They travel
in the private ZIP, rather than publishing their native sequence contents.
Existing published W3 fixtures retain their original public status. Do not
redact or rewrite a frozen private receipt merely to fit GitHub publication.
Scientific raw outputs, papers, assets, local environments and credentials do not
become public source because the investigator requests repository synchronization.

## Why copying `.git` is unnecessary

At initial inspection, PeptideMT main and actual GitHub main both point to
`1f8c444e4619499cae8ad9970122c5f40adf6127`, with no stashes. The unpublished
PeptideMT changes are working-tree files, not exclusive old commits. Once the
authorized changes are committed and pushed, GitHub supplies their history.

HydrAMP's public master remains
`6590d2f4c2963f25d30669052a4c4a857e0e7279`. Its local dev7 commit
`a77baff9de97e8ab4ae101b9b0c79122dea22ce3`, dev8 commit
`6a3ff905635a4bd744854cd540f8513916aa99f0`, named experimental branches and
dirty worktrees need independent preservation. A small portable Git bundle
retains unpublished objects/refs, without copying raw `.git` directories or
machine-specific worktree pointer files. Source overlays retain uncommitted
bytes. This is private custody, not permission to publish the fork's branches.

The transfer inventory also identifies nested provider worktrees used by old
qualification tasks. Restore their recorded bases/branches before their file
overlays; cloning the latest main is not a replacement for a qualified source.
Git author configuration, credentials, hooks and cached/reflog state are not
scientific inputs to transplant. Authenticate normally on the destination.

## ZIP layout and placement

The private ZIP contains `RESTORE.md`, an exact `MANIFEST.json`, a per-case
`CASES.tsv` and the concrete source/worktree registry. It has no raw `.git`
directory or worktree pointer file. The destination workspace is a parameter,
not a hardcoded old home directory.

| ZIP area | Destination and purpose |
| --- | --- |
| `payload/workspace/peptidemt/` | Non-GitHub files at the same relative paths in the new PeptideMT clone, including `local_data` and the two private native H4 receipts |
| `payload/workspace/hydramp/` | Exact local fork/worktree files at their original workspace-relative paths; unpublished source stays distinct from public master |
| `payload/papers/amp_papers/` | Investigator-provided PDFs in the chosen destination papers directory, normally `~/amp_papers` |
| `payload/old-tmp/` | Retained referenced temporary files, staged under the destination's `peptidemt/local_data/migrated-tmp/`; original receipts keep old paths |
| `history/` | Portable bundles for recorded unpublished/source-worktree identities; import them using Git, never extract a raw `.git` |
| `environment/` | Source runtime/version records to guide rebuilding and receiving; they do not qualify relocation of existing Conda prefixes |

`CASES.tsv` records each local task/worktree case and its exact destination
relative to the chosen workspace. Nested run subdirectories retain their
original relative layout. The registry gives each Git root, common owner,
branch and commit; the manifest provides current sizes/hashes/link targets and
the explicit exclusions or unavailable historical references.

Restore in order: verify the ZIP checksum and manifest; clone the recorded
repositories; import the required private Git objects/branches; create the
recorded worktrees in empty destination paths; then place the payload files.
Use a fresh staging workspace and refuse to overwrite unrelated or changed
files. Create a relocation record rather than rewriting historical absolute
paths, producer versions or scientific receipts.

The ZIP is a private migration archive, not a public dataset or release asset.
Do not execute copied environments, model files, PCA pickles or binaries just
to unpack it. Old qualified environments remain historical source evidence;
the actual destination runtime/native dependencies need receiving. Do not
infer destination GPU usability from the old source-host report.

## Completion and resumption

The actual ZIP inventory, checksum, byte verification, source commit and
upstream/CI outcomes are recorded in the private transfer task identified by
`local_data/peptidemt-migration-zip-current-path.txt`. Check those observed
outcomes before claiming the transfer is ready or the source synchronized.
Excluded active transfer outputs and unavailable historical files are disclosed;
the archive must not recursively include itself.

The earlier TAR remains a dated partial recovery artifact. The new ZIP supersedes
it as the requested transfer route; keep original source data until destination
verification succeeds. Destination receiving itself is still pending.

After restoration, continue from the decision-context checkpoint: inspect the
actual host/profile, resolve the 1YCR molecular recipe through MolSysMT and the
peptide-pose/provider boundary through DockingMT, then review the concrete
scientific prescription before new docking/model execution. Accepted W0–W4,
HydrAMP, T0 and T1a evidence is retained without repeating campaigns. D49 routine
execution authority, scientific boundaries and scope-specific resource limits
are unchanged by source publication or migration.
