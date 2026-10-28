# W3 installed Macrel qualification preparation

Status: **preparation; revised shared-host envelope authorized on 2026-10-28**.
Owner: [PeptideMT #6](https://github.com/uibcdf/peptidemt/issues/6).
Navigation: [work order](increment_1_work_order.md) · [M1–M8](v0_1_increment_1.md#5-acceptance-specification-for-increment-1)
· [W2 boundary](w2_macrel.md) · [governance](governance.md).

## Candidate bytes inspected without execution

Candidate: official PyPI `macrel-1.6.1-py3-none-any.whl`, 1,843,654 bytes,
SHA-256 `7c0bf4c5d2fc98d02dd797522d92c2345c7c011ca818fe3e017fe2fd3aa22ef1`.
The downloaded file matches the PyPI 1.6.1 JSON digest. Inspection reads the
archive and gzip payloads only; Macrel has not been installed or imported and
neither ONNX head has executed.

| Installed asset candidate | Compressed SHA-256 | Uncompressed SHA-256 |
| --- | --- | --- |
| `AMP.onnx.gz` | `0a674ef6f774c26e6d2f80d550df3fc54973ae05bfeee1b9dfd905e027a4a388` | `90d7fea888758a5c1426949cb21a33ed132bfde2216d85324ab6ebc939d59cb4` |
| `Hemo.onnx.gz` | `6c68af240d43f6fde2eff64645f7f5cedf215b619e510b75c47b257b0713e8b1` | `172d8ca1b45eeadcfdac9631d6915368bd962177e19d2991e0bdab9fbaea8724` |

The wheel carries MIT metadata and the upstream MIT license, whose SHA-256 is
`82b88a2b069538c4c6078e9790171a74a0aba315acb8994625b4a2b6d2a79a83`.
Its README states that Macrel as a whole is MIT. The
[exact source](https://github.com/BigDataBiology/macrel/tree/190462605913844dca74b184869755609fbb20b2)
includes the same project license; model documentation reports training metrics,
not a separate model-specific grant. Record this scope as provider-stated terms,
not an independent license adjudication or validation of the training datasets.

The feature source explicitly acknowledges modlAMP-derived code and BSD-3
licensing. The wheel contains only the project MIT notice. Preserve the upstream
acknowledgment and the original modlAMP BSD notice in qualification records;
the exact modlAMP revision adapted by Macrel is unspecified. No model, source
adaptation or training corpus is redistributed by this qualification. Any future
redistribution needs its own notice/terms review. No external service, account,
registration or new use-dependent commitment is part of the proposed local run.

## Small upstream-derived fixture

Freeze these four sequence views before obtaining native scores:

| View | Original upstream source | Purpose |
| --- | --- | --- |
| `FLPVLAGLTPSIVPKLVCLLTKKC` | `macrel/tests/test_features.py` in the exact wheel/tag | Native AMP/Hemo outcome coverage candidate |
| `HGRHVTLKDIVLDLQPPDPVGLHCYEQLVDSSEDEVDEVDGQDSQPLKQHFQIVTC` | Same upstream test | Distinct composition/outcome coverage candidate |
| `AA` | `macrel/tests/data/very_short.faa` at the exact source tag | Upstream very-short regression |
| `F` | Same upstream source fixture | Upstream one-residue regression |

These are bounded upstream code-test fixtures under the project's stated MIT
terms; retain its notice with a copied fixture. Native model labels and numerical
values are **unknown until executed**. If the pool fails to cover both signs for
both heads, report M2 incomplete rather than invent labels or search silently.
The larger `example_seqs/expep.faa.gz` was inspected for provenance but is not
selected or redistributed. The `tests/peptides/expep.faa.gz` repository path is
a symlink to that larger fixture, not gzip bytes itself.

Add one duplicate occurrence, repeated full proposal headers, leading M,
terminal/internal stop, lowercase, ambiguity, missing/empty sequences and explicit
unassessed chemistry. Inputs stay in memory. MolSysMT owns compatible serialization.
Generated repeated/truncated copies at lengths 99, 100, 109 and 110 test only the
approved engineering/applicability boundary; they do not establish activity or a
new ordinary out-of-scope route. Direct native qualification may probe those
lengths under M5; ordinary adapter admission remains unchanged.

## Proposed actual-host resource envelope

The work order section 2 requires investigator/maintainer authorization of the
host and bounds before live execution. After reviewing the actual shared-host
specifications and the reduced proposal, the investigator authorized proceeding
on 2026-10-28. This disposition covers the following bounded qualification,
not scientific bundle acceptance, larger workloads or GPU use:

| Bound | Proposal |
| --- | --- |
| Provider environment | Task-owned isolated Linux CPU/CPython 3.14 Conda profile; prove real import origins and dependency closure before execution. Preserve the named shared profile. |
| Scientific calls | At most four sequential live calls: direct compatible reference, adapter mixed pool, direct M5 boundaries, direct leading-M comparison. No exploratory additional calls. |
| Submitted size per call | At most 32 records and 8,192 UTF-8 bytes of sequence plus occurrence-token text. |
| Wall time | At most 120 seconds per child; at most 480 seconds across the four live calls. |
| Address space | Linux `RLIMIT_AS` at 4 GiB per child; retain at least 8 GiB host `MemAvailable` before starting each call. This is not reserved RAM or a measured inference RSS guarantee. |
| Process/CPU | One child at a time; two ONNX intra-op threads, sequential graph execution, one inter-op thread, spinning disabled; BLAS/OpenMP/MKL/NumExpr at one thread. Affinity is restricted to logical CPUs 0 and 1, verified to represent distinct physical cores. Low process priority (nice at least +10). No GPU. |
| Storage | Use the task-owned ignored directory under `/home`, with a 3 GiB environment/result budget checked before each call; avoid bulk writes to RAM-backed `/tmp`. |
| Retry | Zero automatic retries. Stop and retain any failure, nonidentical parity or exhausted bound. |
| Storage/use | Local qualification artifacts and small result manifests only; no publication or redistribution of weights/training data. |

Record the authorization reference, exact source, actual process controls,
memory/time use and any failed gate with the results. Installation/resolution
and engine-free attribution checks are separate preparation and do not consume
the four-call allowance. Stop on failure; there are no automatic retries.

### Shared-host review requested by the investigator — 2026-10-28

The original proposal allowed native thread defaults and an 8 GiB address-space
cap. After the investigator identified concurrent host work, that proposal was
reduced and reviewed before the later authorization recorded above. The runner
and adapter now implement the reduced controls. Controlled tests verify CPU
affinity, child-only numerical environment, priority, memory-headroom refusal and
restoration of scoped ONNX options without executing a model.

Observed host: Intel Xeon E5-2630 v4, one socket, ten physical cores/twenty logical
CPUs, 2.20 GHz nominal and 3.10 GHz reported maximum. Linux exposes 30.7 GiB RAM;
the sampled `MemAvailable` was 16.3 GiB. Swap is 8 GiB, approximately 98% occupied;
no swap-in/out pages moved in a separate two-second observation. Memory PSI
averages were zero in the sampled window. CPU load averages were about
1.96/2.42/2.43; a two-second CPU sample averaged 13.6%, with one logical CPU busy.
These are momentary observations, not reserved capacity or a host-wide guarantee.

Storage: `/home` resides on a 3 TB WDC WD30PURZ SATA rotational disk with 2.4 TiB
free; `/` is on a 128 GB Intel NVMe SSD with 76 GiB free. `/tmp` is a 16 GiB
RAM-backed filesystem with approximately 13 GiB occupied. The qualification
environment is already under `/home` and reports 1.9 GiB of linked/copy payloads;
that size is not all incremental allocation because of package-cache hard links.

Measured without model loading: imports used approximately 62 MiB RSS. Default
numerical-library startup created twenty threads and 2.78 GiB virtual address
space; setting BLAS/OpenMP/MKL to one thread reduced that to one thread and
263 MiB virtual address space. This does not predict inference peak memory.
The installed ONNX Runtime 1.25.1 accepts the proposed SessionOptions, verified
without constructing any inference session. Its
[documented thread controls](https://onnxruntime.ai/docs/performance/tune-performance/threading.html)
support explicit thread counts and disabling spinning. Both native-reference
and adapter calls must share the recorded settings and retain exact parity.

## Attribution and remaining gates

The new optional portable boundary uses public Ackredit >=0.9.0 APIs after a
completed child operation. Host-owned offline bibliography survives absence and
failure. It credits only observed completed serialization/features/prediction,
preserves application sessions, original software versions and detached records,
and distinguishes adapted modlAMP reference code from an executed dependency.
Saved-result reading creates no new credit. Source receiving tests use a real
provider with controlled completion evidence; they do not execute Macrel.

The first clean Conda resolution failed because `pyrodigal` was unavailable to
the solver; adding Bioconda produced the same result. The Bioconda file inventory
has no Python 3.14 builds, while official PyPI publishes a CPython 3.14 Linux
wheel for Pyrodigal 3.7.1, SHA-256
`51a73df081f49577d50a89676409e7288d26a36d04c5c34c0f40183898e43cb6`.
This supplies a concrete controlled acquisition alternative, not a tested install.
An unconstrained ONNX Runtime solve selected CUDA and is rejected: the candidate
must select an actual CPU build and fit the measured available storage before provisioning.
The successful solve selects CPU ONNX Runtime 1.25.1, consistent with Macrel's
upstream Pixi upper bound. The exact 246-package Conda transaction is retained
with artifact digests. A cross-filesystem copy into `/tmp` hit a quota; its
rolled-back partial environment was removed. The same transaction succeeds in
the task-owned ignored `local_data/w3-20261028-hNmM4w/qualification-env`, sharing
the package-cache filesystem. Only the verified Pyrodigal and Macrel wheels are
added with `--no-deps`; the resulting `pip check` passes. This is preparation,
without any ONNX inference session or model execution.

The first public MolSysMT 0.23.0 serialization probe revealed that this release
treats `amino_acids_1:F` literally, while newer inspected source understands the
prefix. Bare canonical `F`, `AA`, `ACD` and the primary fixture convert unchanged.
The adapter now uses this already-supported public bare-string route and retains
its strict unchanged-view check. This is a consumer API compatibility correction;
no provider function, molecular normalization or scientific admission rule is
reimplemented. The original W2 receipt remains bound to its original source.
Do not modify unrelated shared dependencies, omit required Macrel metadata or
claim that an installed flag proves usable native execution.

M1 starts with exact native values, all columns and both classifiers observed.
M2 labels follow that actual bundle. M3–M8 combine native obligations with the
retained engine-free controls. An empty or failed result is explicit; controlled
fixtures, attribution capture and administrative CI never substitute for native
qualification or investigator scientific acceptance.
