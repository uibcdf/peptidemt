# HydrAMP H0–H1 environment review

Status: **installation and guarded imports reproduced; full H0/H1 remain partial**,
2026-10-30. Owning work: [PeptideMT #8](https://github.com/uibcdf/peptidemt/issues/8)
and [D38 qualification](pending_proposals/qualify_hydramp_increment_2.md).
The [machine-readable receipt](evidence/hydramp_h0_h1_review.json) retains exact
inputs, versions, native metadata discrepancies, origins and log hashes.

## Outcome and remaining gate

The official starter's locked deployment installs in a new isolated Linux CPU
Python 3.8.20 worker. TensorFlow 2.2.1, Keras 2.3.1, NumPy 1.18.5, SciPy 1.9.3,
scikit-learn 0.23.2, joblib 0.17.0, pandas 1.1.4, modlAMP analysis and the native
`HydrAMPGenerator` class import successfully. All 61 installed versions match the
official lock. The 41 installed `amp` Python files match the original source bytes.
The worker occupies about 1.95 GB of logical file content; shared cache links mean
this is not a measurement of additional unique physical disk use.

No generator was instantiated, scientific artifact deserialized, model evaluated
or peptide generated. These observations establish an install/import milestone,
not model-load compatibility, reproducibility of outputs or scientific acceptance.
H0/H1 remain partial until the exact bundle/use review, explicit deployment-profile
disposition and authorized model-load qualification. Existing M1–M8 and selectors
are unchanged.

## Exact inputs and local-use review

| Input | Identity and evidence |
| --- | --- |
| Native source | `szczurek-lab/hydramp@6590d2f4c2963f25d30669052a4c4a857e0e7279`; installed `direct_url.json` names this commit. |
| Official starter | `szczurek-lab/hydramp-starter-kit@7804df862872ccc6d09fe01c41bafbca194cfa31`. |
| Starter lock | Git blob `4fa8903e9da9ca0ab6873665e5928ec95fbf22c6`; SHA-256 `f116c4a16f1e2cfc551ba1c1d43af58b756a0fc8ce927c1586427fb432a804a4`. |
| Assets | Reuse the [65-file receipt](evidence/hydramp_reference_assets.json), including 60 checkpoint files and the earlier 42 numeric-header checks. |
| PCA | 18,711 bytes; SHA-256 `a3a5dcea04e91421be363c047249b93fa46e99e128aec929e1f6b0f0e488a26d`; not deserialized. |
| Deployment tool | Official PyPI `uv==0.9.18`, installed only in the task workspace. |

Both frozen repositories contain the University of Warsaw MIT text. The starter
[provenance statement](https://github.com/szczurek-lab/hydramp-starter-kit/blob/7804df862872ccc6d09fe01c41bafbca194cfa31/README.md#model--data-provenance)
identifies the epoch-37 checkpoint and original PCA release. This is publisher
provenance; the full original model archive was not downloaded for a second byte
comparison. The [paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC10017685/)
links original code and data archives. On 2026-10-30, the original
[data/model archive](https://zenodo.org/records/7420278) API identifies its licence
as `mit-license`, including its listed `models.zip`; the
[code archive](https://zenodo.org/records/7420189) API uses `other-open`, while the
selected repository's actual licence text is MIT. Archive metadata and checksums
are retained separately from downloaded-file verification.

The intended candidate use is bounded local research qualification with retained
copyright/licence notices and method/software attribution. Training data are not
needed or acquired for this native de novo route. Database reuse, training,
redistribution and commercial/output-rights clearance are outside this review.
The paper's disclosed patent P.443243 concerns newly generated AMPs; it is not
interpreted here as either a blanket model-use ban or freedom to exploit outputs.

Static PCA inspection finds the expected `sklearn.decomposition._pca.PCA` and
`joblib.numpy_pickle.NumpyArrayWrapper` names and a serialized scikit-learn 0.23.2
marker. `pickletools` stops at embedded array bytes. This is a partial static
observation, not safe-deserialization certification. Exact-artifact review and
the fresh execution envelope still precede loading.

## Reproduced installation contract

The earlier [plain-pip failure](evidence/hydramp_preparation.json) is preserved.
The official starter explicitly substitutes two packages' dependency metadata:

- HydrAMP 1.2.0 is resolved as code only; the starter declares its inference stack.
- modlAMP 4.2.3 is resolved against NumPy, SciPy, Matplotlib, scikit-learn, pandas
  and requests, excluding the unavailable MySQL database dependency and other
  declarations outside that selected profile.

This uses the starter's existing
[metadata declarations](https://github.com/szczurek-lab/hydramp-starter-kit/blob/7804df862872ccc6d09fe01c41bafbca194cfa31/pyproject.toml),
following uv's [dependency-metadata mechanism](https://docs.astral.sh/uv/concepts/resolution/#dependency-metadata).
No source, scientific function, original wheel metadata or lockfile was patched.

The task workspace holds verified copies of the starter manifest, README,
licence, source package, `.python-version` and `uv.lock`. A minimal reproduction
from those exact inputs, using a separate worker path and the previously recorded
Conda Python 3.8.20 bootstrap, is:

```bash
export UV_CACHE_DIR="$HYDRAMP_PREPARATION_ROOT/uv-cache"
export UV_PROJECT_ENVIRONMENT="$HYDRAMP_PREPARATION_ROOT/worker"
export UV_PYTHON_DOWNLOADS=never
export UV_CONCURRENT_BUILDS=1
export UV_CONCURRENT_DOWNLOADS=2
export UV_CONCURRENT_INSTALLS=1
export CUDA_VISIBLE_DEVICES=-1
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
export NUMEXPR_NUM_THREADS=1 TF_NUM_INTRAOP_THREADS=1 TF_NUM_INTEROP_THREADS=1
cd "$HYDRAMP_PREPARATION_ROOT/project"
taskset -c 0,1 nice -n 10 "$HYDRAMP_UV" sync --locked \
  --no-install-project --python "$HYDRAMP_PY38"
```

The recorded installation additionally used an 8 GiB address-space ceiling and
600-second process-group wall-time guard. It completed in 95.229 seconds.
The starter application was not installed or run: its quota filling, challenge
filters, novelty checks and ranking are not the commissioned native route.

Imports ran from a neutral directory with `python -I`, two-core affinity,
one-thread native-library settings, an 8 GiB address-space ceiling and a
120-second wall limit. Python audit guards rejected network connections and
opening `.npy`, `.joblib`, `.h5`, `.hdf5`, `.keras` or `.pkl` artifacts. The probe
imported the listed modules and inspected the class signature without calling
its constructor; it completed in 16.956 seconds. The exact probe and logs are
retained in the ignored task workspace with receipt digests.

## Native metadata discrepancy and disposition

`uv pip check --python WORKER/bin/python` exits **1**, reporting eight discrepancies:

| Package | Original declaration | Locked worker |
| --- | --- | --- |
| HydrAMP | `cloudpickle~=1.4.1` | `1.3.0` |
| HydrAMP | `seaborn~=0.11.0` | Not installed |
| HydrAMP | `setuptools~=50.3.1` | `75.3.4` |
| HydrAMP | `argparse` distribution | Not installed; Python supplies the standard-library module |
| HydrAMP | `gdown>=5.2.0` | Not installed |
| modlAMP | `nose>=1.3.7` | Not installed |
| modlAMP | `lxml>=3.6.4` | Not installed |
| modlAMP | `mysql-connector-python==8.0.17` | Not installed |

The cause is the starter's deliberate resolution-time overrides: installed wheels
retain their original metadata. A separate PEP 508 check using the two declared
substitutions and the remaining packages' real requirements finds zero effective
profile discrepancies; it does not change the native failure into a pass.
Source inspection locates seaborn in the training/data loader and gdown in asset
acquisition. Successful imports are evidence for this selected entry point only,
not for every installed module or deferred training/database function.

The investigator-facing disposition is therefore **an explicit inference-only
candidate profile**, pending review under #8, rather than clean full-package
qualification. Preserve the eight native discrepancies in every bundle review.
PeptideMT maintainers own that disposition; review it before model loading and
again by **2026-11-13**. A future upstream inference extra or reviewed packaging
correction can remove the override requirement after native closure and actual
scientific parity are verified. No provider modification is needed to explain
this expected difference, and none was made.

The reusable deployment improvement is reported to the provider in
[HydrAMP #12](https://github.com/szczurek-lab/hydramp/issues/12), linking PeptideMT
#8 and exact consumer evidence. It requests an auditable supported inference
profile, not a model port or changed scientific behavior.

## Next bounded work and retention

Adapter preparation can continue under D38, preserving the existing MolSysMT,
DepDigest, SMonitor and Ackredit responsibilities. Before scientific execution,
present the exact bundle, this deployment profile, permitted local use and a
fresh shared-host CPU/thread/RAM/disk/time/process envelope. H2 retains four total
generation calls and 52 requested outputs; H4 needs its own fresh Macrel budget.
This preparation snapshot does not grant either budget.

The existing [HydrAMP #11](https://github.com/szczurek-lab/hydramp/issues/11)
reports optional-filter callback pairings. At the frozen source, the commissioned
`filter_out=False` branch exits before `get_filtering_mask`; no affected option
is enabled. No numerical reproduction or upstream repair is claimed here.

The ignored `hydramp-h1-20261030-6jc5a1me` workspace retains the worker, inputs,
logs and caches for #8. Original HydrAMP assets/bootstrap and W3/FASTA resources
remain separate. Reassess task caches at bundle disposition or receiving. No
shared environment, public dependency manifest, engine adapter or scientific
package behavior changed in this checkpoint.
