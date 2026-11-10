# HydrAMP: clean locked public-dependency installation

Status: **exact Linux/Python 3.14 base/test dependency route qualified**,
2026-11-05. Owner: [HydrAMP #4](https://github.com/uibcdf/hydramp/issues/4);
consumer: [PeptideMT #32](https://github.com/uibcdf/peptidemt/issues/32).
The investigator commissions continued product development after the
[local dev7 source consolidation](hydramp_product_baseline.md). This milestone
addresses installation engineering without changing scientific methods or
qualifying new model execution.

## What is now demonstrated

The unchanged private dev7 wheel installs with freshly downloaded public
dependencies in a new isolated CPython 3.14.7 environment on Linux x86_64.
No retained third-party dependency payload is copied into this environment.
The original shared interpreter/installer tools and exact own wheel are reused;
this is not a freshly acquired Python or build-toolchain qualification.

Source remains local commit `a77baff9de97e8ab4ae101b9b0c79122dea22ce3`, tree
`2476a08a50d32779db2f43683928450e62b66f91`. The owner worktree stays clean.
The wheel remains SHA-256
`18347066126c439279328224ef71b158f9077a1a67954c742839e0596393c83d`.
All nine source/wheel/installed runtime modules agree byte for byte; all thirteen
hashed entries in the own wheel's RECORD verify. Source, dependency pins,
scientific assets and accepted dev3/dev5 resources are unchanged.

The supported uv export operation reads the immutable 42-package universal
lock and selects base plus the existing test extra. Windows-only colorama is
excluded by its actual marker on this host. Packaging's supported wheel-tag
parser selects seventeen compatible Linux/Python wheels; no local resolver or
new molecular/file-format utility is implemented.

All seventeen exact wheel URLs respond with HTTP 200. Native pip downloads them
sequentially from PyPI file hosting and the PyTorch CPU host, with retries and
caching disabled. Native required-hash checks and a separate SHA-256/size check
verify every retained archive: **238,486,838 bytes** in total. The public-source
URLs, filenames, versions and hashes are retained in the
[execution receipt](evidence/hydramp_public_installation.json).

The fresh environment receives those locked dependencies offline through uv,
then the unchanged private own wheel. All five native steps succeed: download,
dependency sync, own-wheel install, dependency check and installed metadata
inspection. Native `uv pip check` reports **eighteen compatible distributions**.
NumPy is 2.4.6 and Torch is 2.15.0+cpu; no dependency version is substituted.

## Executed route and reusable evidence

The retained fixture is
`local_data/hydramp-public-install-z5lh31o1`. Its
`exact-public-wheel-urls.txt` binds the selected lock URLs/hashes;
`locked-base-test-requirements.txt` is the actual supported uv export. These
are qualification inputs, not a second maintained package version table.

The finite driver uses the existing pip/uv operations below, with the exact
paths recorded in its receipt. A fresh stdlib venv is created without pip or
system site packages. `HYDRAMP_WORK`, `HYDRAMP_ENV`, `HYDRAMP_UV` and
`HYDRAMP_WHEEL` refer to the selected fixture, new environment, retained
uv 0.9.18 executable and exact private wheel respectively.

```bash
python -I -B -m pip download --no-deps --no-index --require-hashes \
  --no-cache-dir --only-binary=:all: --disable-pip-version-check \
  --progress-bar off --retries 0 --timeout 15 \
  --dest "$HYDRAMP_WORK/wheels" \
  --requirement "$HYDRAMP_WORK/exact-public-wheel-urls.txt"
"$HYDRAMP_UV" --offline pip sync --python "$HYDRAMP_ENV/bin/python" \
  --no-index --find-links "$HYDRAMP_WORK/wheels" --require-hashes --no-build \
  "$HYDRAMP_WORK/locked-base-test-requirements.txt"
"$HYDRAMP_UV" --offline pip install --python "$HYDRAMP_ENV/bin/python" \
  --no-deps --no-index --no-build "$HYDRAMP_WHEEL"
"$HYDRAMP_UV" --offline pip check --python "$HYDRAMP_ENV/bin/python"
```

This tests an exact lock/archive installation, not an unconstrained latest
dependency resolution. The owner wheel remains a private supplied artifact;
the work does not publish or newly acquire it from a package index. The common
offline dependency-route auditor's inventoried Conda/workflow profile does not
cover this unregistered fork's selected pip-wheel route; native supported
installers and their exact records are used instead of copying its machinery.

## Installed behavior and resources

The exact existing codec tests run against this new installed prefix, confined
to their own test/configuration directory. All **seventeen pass**, native exit 0,
with complete Pytest Receptor evidence received through `read_artifact` and
`artifact.final.data`. All sixteen exports are present. The fixture has no
PeptideMT, TensorFlow, Keras, Macrel or modlAMP package. Guards reject foreign
model imports, parameter/PCA reads, neural construction/evaluation, network and
child dispatch during the installed check. New learned reads and neural
evaluations are **zero**. The developer supervisor is reused by file; this does
not add a PeptideMT dependency to HydrAMP.

Both substantive workers run sequentially with CPU0/1 affinity, one numerical
thread, nice 5, 180 s wall, explicit 120 s CPU and 8 GiB virtual address limits,
sampled 2 GiB aggregate RSS stop and at least 8 GiB host RAM available. The
installation's task-output cap is 4 GiB for wheel archives, unpacked dependency
cache and environment; its observed logical output is about 2.10 GB. The codec
worker's separate output cap remains 64 MiB. No guard fires and no GPU is used.

| Worker | Supervised wall | Peak sampled controller/worker RSS |
| --- | ---: | ---: |
| Public acquisition and installation | 41.39 s | 262,524,928 bytes (about 250 MiB) |
| Installed codec checks | 9.01 s | 310,358,016 bytes (about 296 MiB) |

The preliminary one-second HEAD probe requested a kernel CPU limit through a
helper that does not apply that option. Its request facts remain usable, but
no kernel CPU-limit compliance is claimed for that probe. The substantive
installation and codec workers explicitly apply the limit. An existing task
cache interrupted a preparation-only mkdir, and the first receipt reader used
the wrong access on ArtifactRecord; both caller mistakes are diagnosed and
corrected without repeating successful network requests or tests. Their
dispositions remain pinned; no provider code or common supervisor is patched.

## Remaining product boundary

This closes the retained-payload-only gap for the exact **base/test dependency
installation**. Public HydrAMP distribution, a clean public source-build
toolchain, other platforms/interpreters, optional modlAMP and console-script
qualification remain separate. Installed codec success supplies no new model,
numerical fidelity, biological utility, scientific acceptance or family claim.

The next product design task is a concrete independent scientific result and
provenance contract under #4/#32, with Recorda/Ackredit responsibilities reviewed
before any new schema or API. No feedback, target-conditioned operation,
training, GPU, release or author contact follows from this engineering work.

The [closeout](evidence/hydramp_public_installation_closeout.json) records scoped
documentation checks, resource cleanup/retention and the
[existing issue updates](evidence/hydramp_public_installation_issue_updates.json).
Retain verified public archives, the fresh installed fixture and useful evidence
for the next product milestone, owned by #4/#32, with review on 2026-11-19.
The task-local installer cache is disposable after verification. Earlier
baseline receipts and scientific evidence keep their exact bytes and scope.
