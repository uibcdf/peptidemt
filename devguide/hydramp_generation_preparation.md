# HydrAMP generation wrapper: Python 3.14 preparation

Status: **implemented experimental route; installed-wheel synthetic checks pass**,
2026-11-02. D38–D40 / PeptideMT #8. Real pretrained generation, complete native
properties and PeptideMT integration remain unqualified.
The [published work update](https://github.com/uibcdf/peptidemt/issues/8#issuecomment-6595558884)
and MolSysMT handoff are verified in the
[publication receipt](evidence/hydramp_generation_issue_updates.json).

## Candidate and preserved reference

The investigator asked to continue toward a modernized HydrAMP. A new local
`peptidemt-pytorch-generation` worktree at `../hydramp/local_data/pytorch-generation`
preserves both earlier port branches, their exact wheels/workers and all failed
outputs. It starts from **dev0**, whose twelve-input numerical deviation is accepted
under [D40](hydramp_behavioral_acceptance.md); it does not adopt dev1's failed GRU
layout candidate. D40 does not automatically qualify the new dev2 artifact.

The package is experimental `hydramp-torch==0.0.0.dev2`, wheel SHA-256
`0ed1c1db2eb54c9c13c71fc06bf57d0211edeca7c84db8946c2754985ae7a687`.
The [receipt](evidence/hydramp_generation_preparation.json) binds source, exact
wheel/installation, frozen dependency graph, tests and resource observations.
All fifty tracked original `amp/` and MIT licence files match
`6590d2f4c2963f25d30669052a4c4a857e0e7279`. Dev0's `inference.py` and `prior.py`
are byte-identical in the new candidate; original preparation-era docstrings in
those frozen files do not replace the later execution/D40 records.

The new package adds generation and an explicit original-provider compatibility
adapter, with no copied descriptor algorithms or general molecular-system tools.
Scientific arrays, descriptors, classification definitions and chemistry are not
silently changed. Code/reports remain local/uncommitted; no package publication,
public support range, scientific acceptance or suite admission is claimed.

## Prepared generation route

`HydrAMPGenerator` accepts an existing inference core and numeric PCA projection.
It loads no checkpoint or pickle on construction. The selected call supports
`mode='amp'`, `filter_out=False`, `n_attempts=1` and an explicit uint32-range seed.
Unsupported filtering/non-AMP/repeated-attempt requests fail before a model call.

The wrapper composes:

1. A local seeded `RandomState` normal draw, preserving host NumPy RNG state.
2. Numeric PCA inversion in the original precision, then both AMP/MIC conditions
   set to one and the final float32 conversion for the decoder.
3. One decoder invocation and original-token AMP/MIC scoring, retaining internal
   zero positions. Strings are not re-encoded for scoring.
4. Original occurrence order for the native string-only control view; AMP-descending
   stable occurrence order for `properties=True`, followed by descriptor calls on
   that ordered string list. Duplicates and empty projections are retained rather
   than repaired, dropped, resampled or refilled.

`unconstrained_generation` exposes the native list-of-dicts/strings view.
`generate_with_trace` also retains original input-order numeric arrays and an
explicit returned-order-to-input mapping. Its trace is an internal qualification
object, **not** PeptideMT's portable provenance or Ackredit attribution contract.
Read-only array snapshots prevent accidental ordinary assignment; no deep security
or immutable serialization guarantee is asserted.

The prepared stable sort is tested on artificial ties. It does not establish
parity of the actual original pandas path; the full native comparison is still
required. The original scores retain their precision/meaning and are distinct
from Macrel, measured activity, concentration or biological confidence.

## Descriptor ownership and current limit

The default `properties=True` requires an explicitly selected provider. Its
availability is checked **before sampling, PCA inversion or model execution**.
Without a provider, the route fails explicitly; it does not return invented or
partial properties. `properties=False` is an engineering control, not a substitute
for qualifying the commissioned complete native return contract.

`LegacyModlampProperties` prepares the original modlAMP **4.2.3** call contract.
It delegates calculations to that provider and fixes the inspected native
parameters explicitly: Eisenberg hydrophobicity, hydrophobic moment window 1000 /
angle 100 degrees / max modality, charge at pH 7 with `amide=True`, and the
original isoelectric-point method. The length field counts the model-projected
symbols; it does not infer a chemically resolved molecular system.

**The modlAMP compatibility route is not installed or qualified in Python 3.14.**
It is not a working advertised extra or installation recipe. This artifact's
clean dependency closure covers the NumPy/PyTorch base, not that optional route.
The adapter rejects other provider versions rather than silently selecting an
unqualified alternative. Scientific descriptor outputs have not been computed;
its three checks use a spy provider only. Dependency/import/computation failures
propagate, with no automatic backend substitution or retry.

The pH/amide settings are native descriptor assumptions, not evidence that a
generated molecular proposal has known terminal chemistry. MolSysMT's existing
charge definitions and per-group Eisenberg lookup cannot be presumed equivalent.
The need for reusable sequence-level descriptors is recorded in existing
[MolSysMT #485](https://github.com/uibcdf/molsysmt/issues/485#issuecomment-6595490991),
with `component:peptidemt`, exact inspected references, semantics, interim route
and removal/review condition. MolSysMT owns implementation/priority. No sibling
source was edited and no upstream third-party issue was published.

The interim adapter can be replaced only after supported owner operations and
scientific definitions are reviewed and qualified for this native output contract.
Review by 2026-11-13. Do not copy acid/base, hydrophobic-moment or pI algorithms
into PeptideMT or this fork to bypass that ownership.

## Installation and artificial evidence

A fresh isolated Python 3.14.7 worker uses the same **seventeen external versions**
as dev0, including NumPy 2.4.6 and CPU PyTorch 2.15.0+cpu. The external lock graph
is unchanged. Offline installation/checking succeeds for eighteen distributions;
nine installed wheel payload members, excluding RECORD, match the exact wheel.
The shared suite environment and all earlier workers remain unchanged.

The first direct-source build failed because the sibling worktree was read-only
inside the sandbox. That log is retained. The successful build used a task-owned
byte-identical snapshot of the provider source, with no metadata/dependency
patch or override. No learned-call retry occurred.

**74 installed-wheel artificial tests pass:** 25 core tests, 22 existing comparison/
trace controls, 24 generation tests and 3 provider-call tests. They exercise raw
seeded inputs, precision and conditions, original-token scoring, duplicate and
tie occurrence mapping, unchanged host RNG, string-only control, pre-execution
rejection, provider absence/failure propagation, malformed outputs and an actual
complete zero-weight CPU core, including empty projected strings.

The guard blocks network, actual legacy providers and real scientific array/
pickle/HDF opens outside artificial pytest storage. The provider spy is not an
installed/scientifically exercised modlAMP backend. Tests used CPU affinity 0/1,
one native thread, nice 10, an 8 GiB virtual ceiling and 120 s timeout. Measured
whole-worker wall time was **20.65 s** (pytest reports 8.83 s); kernel child peak
RSS **338.49 MiB**, within the investigator's 4 GB task RAM intent. No GPU,
pretrained model/PCA load/forward, real descriptor or Macrel call occurred.
Ruff checks/format pass for all five changed/new Python files.

## Next qualification

The subsequent [dev3 comparison candidate](hydramp_full_comparison.md) has a
clean optional-properties dependency closure using explicitly configured modlAMP
4.3.3, and model-free five-descriptor parity on eight published occurrences.
That separate record supersedes the unqualified descriptor-deployment status
for its exact profile; it does not retroactively change dev2 or qualify neural
generation. The later exact neural plan has now executed under separate investigator approval;
its report preserves matching observable outputs and the failed internal-probability
criterion, without retroactive dev2 or general dev3 acceptance.

The [original HydrAMP resource inventory](hydramp_upstream_test_resources.md)
identifies upstream data, archived outputs and evaluation notebooks that can
supply prospective regression fixtures. They have not been adopted/executed,
and the original benchmark settings differ from our commissioned route.
The [comparison framework](hydramp_upstream_test_resources.md#comparing-the-modernized-port-with-the-original)
separates scientific fidelity, measured software/resource improvements and any
future claim of scientific superiority. No new execution allowance is granted.

Resolve and qualify the descriptor deployment/owner route; then bind this exact
candidate and a prospectively selected broader fixture to an explicit finite
resource/call proposal. Keep the original D40 evidence and diagnostic FAIL reports.
Full native properties/order/seed behavior, portable result/provenance, the
PeptideMT adapter and H0–H4 acceptance remain pending. Existing learned-call
allowances are exhausted; no new execution, GPU, training, analogue generation,
feedback, target conditioning, package release or model redistribution follows.
