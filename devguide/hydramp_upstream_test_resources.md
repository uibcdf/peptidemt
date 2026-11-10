# Original HydrAMP: reusable test data and evaluation resources

Status: **source/metadata inventory; fixture adoption pending**, 2026-11-02.
Consumer: PeptideMT #8 / D38–D40. The investigator asks whether original tests,
benchmarks and data can improve qualification of the modernized port.
The [published inventory update](https://github.com/uibcdf/peptidemt/issues/8#issuecomment-6595889388)
is verified in the [publication receipt](evidence/hydramp_upstream_resource_issue_update.json).

The subsequent [full comparison preparation](hydramp_full_comparison.md) acquires
only the small published results CSV member and checks eight descriptor cases.
The acquisition/execution limits stated below describe this earlier inventory
checkpoint; its recommendation is not a claim that those later scalar checks
remain unexecuted. No training data or neural execution follows from either record.

## What was inspected

The upstream default branch is still `master` at
`6590d2f4c2963f25d30669052a4c4a857e0e7279`, matching our preserved scientific
reference. The [source inspection receipt](evidence/hydramp_upstream_test_resources.json)
pins fifteen inspected source/notebook files; the
[published resource metadata](evidence/hydramp_upstream_resource_metadata.json)
records the official starter's data inventory and primary URLs. Source inspection
covers the original Git tree, not the tests subsequently added to our fork.

The original tree has **91 tracked files**. No conventional `tests/`, `test_*.py`,
`*_test.py`, `pytest.ini` or `tox.ini` path was found in that revision. This does
not establish absence on every other branch/release. It does establish that the
original master does not provide a ready conventional unit-test suite to run
instead of the port's artificial tests.

There is substantial **scientific evaluation code, published data and saved
results**, which serve different purposes from an automatic regression suite.

## Resource map

| Resource | Observed material | Possible use | Current limit |
| --- | --- | --- | --- |
| [Original data archive preview](https://zenodo.org/records/7420278/preview/data.zip?include_deleted=0) | MIC data, AMP/assumed-negative data, UniProt train/validation/test files, DBAASP activity subsets and comparison-generator resources | Native-head/descriptor input fixtures and scientific-evaluation context | Training or assumed-negative labels do not establish independent experimental validation |
| [Official starter data description](https://github.com/szczurek-lab/hydramp-starter-kit/blob/7804df862872ccc6d09fe01c41bafbca194cfa31/data/README.md) | Versioned `data/training/` files, with publisher descriptions and source attribution | Small, hash-pinned acquisition without downloading all historical models/wheels | Publisher schema/row descriptions were inspected, not every data file's content; database terms still apply |
| [Original results archive preview](https://zenodo.org/records/7420278/preview/results.zip?include_deleted=0) | `hydra_unconstrained.csv`, `unconstrained_HydrAMP.joblib`, `thresholding.csv` and other stored experiments | Candidate generated-sequence fixture and distribution/reference analysis | Member contents, columns, exact generation settings and checkpoint mapping not yet verified; no pickle loaded |
| [Unconstrained notebook](https://github.com/szczurek-lab/hydramp/blob/6590d2f4c2963f25d30669052a4c4a857e0e7279/scripts/unconstrained_generation.ipynb) | Original generation and saved-result procedure | Recover input/output definitions and experiment configuration | Includes PCA fitting and `n=50000` with 64-fold latent replication; not a small executable smoke test |
| [Physicochemical notebook](https://github.com/szczurek-lab/hydramp/blob/6590d2f4c2963f25d30669052a4c4a857e0e7279/scripts/figures/UnconstrainedGeneration_PhysicochemicalProperties.ipynb) | Native descriptor calls, reference populations, quantile/p-value output construction | Check definitions and choose descriptor comparison cases | Uses original modlAMP and large populations; source inspection alone gives no expected scalar golden values |
| [Condition-evaluation notebook](https://github.com/szczurek-lab/hydramp/blob/6590d2f4c2963f25d30669052a4c4a857e0e7279/scripts/figures/UnconstrainedGeneration_Conditions.ipynb) | Stored-condition distributions and comparisons with AMP-LM, Dean-VAE, Muller-LSTM and AMP-GAN | Original scientific benchmark context | Includes positive/negative modes and repeated-choice statistics that differ from the commissioned one-attempt route |
| [CAS script](https://github.com/szczurek-lab/hydramp/blob/6590d2f4c2963f25d30669052a4c4a857e0e7279/amp/evaluation/scripts/run_cas.py) / [NAS script](https://github.com/szczurek-lab/hydramp/blob/6590d2f4c2963f25d30669052a4c4a857e0e7279/amp/evaluation/scripts/run_nas.py) | Auxiliary classifier training/cross-validation and generated-data experiments | Understand original evaluation logic | Training is outside D38/D39; these are not migration regression tests |
| [Paper and supplementary resources](https://pmc.ncbi.nlm.nih.gov/articles/PMC10017685/) | Paper identifies Supplementary Data 8/9 as external-classifier evaluation datasets; Data 5 includes tested peptides and physicochemical/auxiliary-score information | Candidate independent evaluation context and descriptor/reference comparisons | Files not downloaded/read; distinguish original generated outputs, experimental measurements and model scores |

The archived previews identify a roughly 10.7 MB compressed `data.zip` and 378.3 MB
`results.zip`; these are advertised archive sizes, not the README's approximate
unpacked descriptions or measurements of downloaded bytes. No archive was fetched.
The DVC manifests separately advertise 20 data files / 30,566,627 unpacked bytes
and 16 results files / 872,974,869 bytes. Preserve those distinct metadata surfaces.
The existing selected checkpoint/PCA receipt remains in force; this inventory
neither reacquires nor replaces its exact assets.

## Compatibility gaps to preserve rather than silently fix

- The CAS/NAS code imports `amp.evaluation.nas_cas`, absent from the inspected
  tree. This is an unresolved source dependency, not a measured runtime failure.
  No training script was launched or unrelated component repaired.
- Figure notebooks reference `positives_test.tsv` and `negatives_test.tsv`, which
  are not listed in the archived data preview. Their mapping to the paper's
  supplementary tables or generated splits is unverified.
- Saved generation populations are not automatically golden outputs for our
  `softmax=True`, `mode='amp'`, `filter_out=False`, `n_attempts=1` route. Original
  activation, repetition/selection, PCA, checkpoint, seed and filtering settings
  must match before numerical parity claims.
- The starter distinguishes `antibacterial.fasta`, a challenge novelty-exclusion
  reference, from the original training data. It is not a biological negative
  set or a substitute for the original held-out evaluation.

## Comparing the modernized port with the original

The investigator asks whether the port can work as well as, or better than, the
original. Treat these as distinct questions, without an overall improvement
claim or a new accepted scientific benchmark:

| Question | Prospective comparison | Permitted interpretation |
| --- | --- | --- |
| Is the implementation faithful? | Same checkpoint/PCA, raw latent bytes/seeds, conditions and selected native route; compare tokens, strings, occurrences, order, scores and properties | Fidelity on the actual tested fixture, retaining D40 limits and original diagnostic failures |
| Does deployment/inference improve? | Record installation/dependency closure and separate import/load, preprocessing, network and result times; compare peak RSS with equal CPU affinity/native threads/batches and no GPU | Measured software/resource improvement, with environment, first/subsequent call and shared-host effects explicit |
| Does scientific prediction or generation improve? | A separately specified, source/overlap-reviewed held-out or experimental benchmark, with target/assay and endpoint meanings fixed | A bounded scientific performance result only after appropriate design/execution; numerical portability, higher native scores or faster runtime alone do not prove better peptides |

The immediate objective remains **preserved scientific behavior with a modern
implementation**. Pretrained coefficients are unchanged; modernization alone is
not a new learned method or evidence of increased antimicrobial potency/safety.
The twelve-input D40 disposition and 74 artificial dev2 tests do not decide
broader equivalence or superiority.

Prepare the matched native/port fixture, descriptor provider and exact timed
worker route before asking for a finite new execution allowance. Count all
initial, repeated and warm-up model calls in that proposal. First/subsequent
calls and cold process startup must be reported separately; do not claim cold OS
caches or a stable speedup from a few executions on this shared machine. Reuse
paired scientific runs for initial timing observations where appropriate rather
than adding unapproved benchmark calls. Earlier whole-worker legacy/port timings
include different setup work and do not establish a controlled speedup.

No wider scientific superiority criterion, larger numerical tolerance, extra
model, auxiliary-classifier training or transfer to other peptide families is
adopted. The original paper datasets/figures inform the design; they do not waive
the complete native descriptor/provenance qualification or new host/call review.

## Recommended next fixture preparation

1. Inspect the smallest relevant published files and their terms/source mapping:
   candidate original sequence/MIC files, the small `hydra_unconstrained.csv`
   member and supplementary descriptor/evaluation tables. Record acquired-byte
   hashes and schemas before adopting a subset; do not reconstruct missing data
   silently or infer a schema from a filename.
2. Propose a small versioned subset for **native-head and descriptor regression**.
   Preserve identifiers, duplicates, chemical unknowns, target/assay/units and
   native preprocessing. Molecular formats/operations use MolSysMT; no local
   FASTA parser or descriptor formula is introduced. Existing owning descriptor
   work remains [MolSysMT #485](https://github.com/uibcdf/molsysmt/issues/485).
3. Separately qualify **generation** with matched raw latent/seed bytes and the
   exact native/port checkpoint route. A peptide dataset exercises heads and
   properties; it does not by itself test a de novo generator's latent mapping.
   Bind proposed native results to exact input/configuration/environment evidence.
4. Keep broader predictive/distributional benchmarks separate. Training data are
   usable for regression but cannot demonstrate generalization; experimental MIC
   is not the native MIC-head score. Large NAS/CAS training and other generator
   implementations remain outside the present commission.

This is a recommendation and resource inventory, not an accepted new scientific
benchmark or an execution allowance. No archive/table contents were acquired,
CSV/FASTA/XLSX parsed, pickle deserialized, model/PCA loaded, real descriptor
computed, model trained or GPU used. No upstream issue/comment was published.
All prior D40/source/environment/evidence limits remain unchanged. Before actual
learned/descriptor calls, prepare the exact candidate fixtures/use and fresh
finite host/call proposal. The existing test-resource findings stay in #8.
