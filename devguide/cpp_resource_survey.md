# CPP resources: generation, assessment and delivery evidence

Status: **investigator-requested bounded discovery and source inspection**,
2026-10-29. Navigation: [catalogue](tools_catalog.md) ·
[CPP conversation](https://github.com/uibcdf/peptidemt/discussions/11) ·
[functional semantics](functional_families.md) · [case guides](cpp_guided_projects.md)
· [source inventory](evidence/cpp_resource_survey.json).

This first survey separates generation/redesign, CPP classification, uptake,
endosomal escape and productive cytosolic delivery. None is interchangeable with
passive membrane permeability or binding a chosen protein. Assay, cell, cargo,
chemistry and exposure context must accompany conclusions. A source label is not
an assay-independent biological truth.

Five new repositories were frozen and their small source files inspected;
CPP_Design's earlier exact source evidence is reused. Asset filenames/sizes are
metadata observations, including pointer-sized files; no candidate weight was
downloaded, deserialized or loaded. Live service/documentation pages have a date
and URL, not a frozen dataset identity. No model/API prediction, environment
installation, training, GPU job or scientific benchmark ran for this survey.

## CPP_Design

- **Role:** EvoDiff fine-tuning/generation and CPP assessment within a separate
  closed-loop optimization study.
- **Source:** [reused frozen source](https://github.com/IoriYamahata/CPP_Design/tree/9e8e5afb66dc66c951af27bf64eef23f2806f6b3)
  and [primary paper](https://pubs.acs.org/doi/10.1021/acs.jcim.6c01267).
- **Observed route/assets:** Python 3.9/CUDA recipe; fine-tuned state/classifier
  files visible. Base EvoDiff assets may be obtained by native code.
- **Limits/question:** source/artifact terms, complete base/adapter identity and
  a bounded CPU route remain unresolved. The earlier tree contained no license
  file. Determine the usable native generation boundary separately from the
  study's target/selectivity/optimization claims and computational assays.
  No such closed-loop or target-conditioned execution is commissioned here.

## LightCPPgen

- **Role:** LightGBM CPP scoring plus genetic optimization with sequence-similarity
  and anomaly criteria; useful as a search/redesign candidate, not a generic
  target-conditioned generator.
- **Source:** [frozen source](https://github.com/gabribg88/LightCPPgen/tree/4834b0744bb70126e165968bfd110d252eead66a)
  and [published study](https://www.sciencedirect.com/science/article/pii/S0924857925001669).
- **Observed route/assets:** CLI has separate `score`/`optimize` subcommands;
  `models/LightCPP_20.pickle` is listed. The native fast featurizer uses the
  published 20-feature contract; the CLI checks feature-name compatibility.
- **Limits/question:** paper reproduction recommends Python 3.9 with old exact
  pins. README claims MIT, but no license file was found in the frozen tree;
  the recommended `requirements-optimizer.txt` is also absent. Resolve the
  minimal dependency/terms route and validate native scoring before adopting
  optimization. Changing feature subsets requires a matching featurizer.
  The [existing model-access issue](https://github.com/gabribg88/LightCPPgen/issues/1)
  is historical context, not proof of current artifact completeness.

## MLCPP 2.0

- **Role:** two distinct predictions: CPP class and uptake efficiency among
  sequences called CPP. Neither output alone establishes cytosolic delivery.
- **Primary sources:** [official server](https://balalab-skku.org/mlcpp2/),
  [output help](https://balalab-skku.org/mlcpp2/help/),
  [dataset page](https://balalab-skku.org/mlcpp2/download/) and
  [2022 study](https://www.sciencedirect.com/science/article/pii/S002228362200184X).
- **Observed availability:** public input/help pages and separate layer-1/layer-2
  training/independent dataset links. No sequences were submitted.
- **Limits/question:** this survey establishes no local redistributable runtime,
  stable service API or exact downloaded dataset. Negative construction, pooled
  source overlap and the native uptake definition need review before comparison.
  A web form is not an installed, reproducible provider qualification.

## pLM4CPPs

- **Role:** CPP classification using protein-language-model embeddings and CNNs.
- **Source:** [frozen source](https://github.com/drkumarnandan/pLM4CPPs/tree/2d648806c241f1dc64d9e4ff9d9f4baeb28a5d1f)
  and [author-hosted primary paper](https://www.grains.k-state.edu/research/ccl/files/publication_pdf/2025_JCIM_Nandan_PLM%20CPPs.pdf)
  (DOI `10.1021/acs.jcim.4c01338`). MIT code is present.
- **Observed route/assets:** embedding notebooks, datasets and HDF5 model names;
  some listed files are only 133–134 bytes. Metadata does not establish complete
  received assets or the exact embedding/scaler/CNN combination.
- **Limits/question:** the README inference example fits `StandardScaler` to
  the new prediction batch. Mathematically, a singleton batch becomes an all-zero
  standardized embedding, and changing batch composition can change normalized
  inputs. This is an unexecuted source-level concern, not a reproduced model
  failure. Recover the actual training preprocessing before any qualification.
  Existing [local/web discrepancy #1](https://github.com/drkumarnandan/pLM4CPPs/issues/1)
  and [padding/pooling report #2](https://github.com/drkumarnandan/pLM4CPPs/issues/2)
  remain upstream reports, not independently proven causes of each other.

## CPPpred-En

- **Role:** CPP classifier combining conventional descriptors, PLM features and
  an ensemble of classical models; not a generator or uptake-efficiency estimator.
- **Source:** [frozen source](https://github.com/YE-MJ/CPPpred-En/tree/339eed196edd2e62a97c8bc0b1f0458f86e5f34d).
  Associated study DOI: `10.1016/j.compbiomed.2025.110590`.
- **Observed route/assets:** precomputed-feature benchmark scripts and named
  selected classifier weights for CPP924 and MLCPP datasets. README recommends
  Python 3.9.20; requirements pin old scientific libraries and CUDA packages.
- **Limits/question:** no license file was found. Test scripts using prepared
  features do not establish a complete arbitrary-sequence inference route.
  Receive feature extraction/base PLMs, feature ordering, scalers and ensemble
  weights together; inspect data overlap before claiming independent agreement
  with MLCPP or pLM4CPPs. No Python 3.14 or installed CPU support is established.

## ELP–EEP discovery

- **Role:** regression-driven screening/design of endosomolytic peptides in an
  elastin-like-polypeptide nanoparticle delivery context.
- **Source:** [frozen source](https://github.com/sayoeweje/elp-eep-discovery/tree/bf48ecf09cef7aec49cd020fbf087a5d5b122d4e)
  and [primary study](https://www.nature.com/articles/s41587-025-02664-2).
- **Observed route/assets:** MIT code, training/screen spreadsheet names and a
  script that fits regression models and screens helical peptide combinations.
  README recommends a Python 3.7 environment and Biopython 1.78; the script
  imports legacy `Bio.SubsMat`.
- **Limits/question:** this is a formulation- and cargo-dependent workflow, not
  a universal free-peptide cytosolic-access classifier or a ready inference
  service. It supplies a relevant endpoint/reference and data lead. Review
  primary assay context, training cost and input provenance before reuse; do
  not convert reported delivery results into PeptideMT experimental evidence.

## CPPsite3: data resource

- **Role:** experimentally annotated CPP database, not a predictor or generator.
- **Primary sources:** [home](https://webs.iiitd.edu.in/raghava/cppsite3/),
  [API documentation](https://webs.iiitd.edu.in/raghava/cppsite3/api.php),
  [downloads](https://webs.iiitd.edu.in/raghava/cppsite3/downloads.php) and
  [database paper](https://www.sciencedirect.com/science/article/pii/S1359644625001345).
- **Observed availability:** API documentation describes chemistry, chirality,
  termini, cell/cargo, uptake and localization fields. Natural/non-natural
  sequence and structure download links are visible; no dataset was downloaded.
- **Limits/question:** the home page reports about 4,143 unique sequences, while
  the paper highlights report 4,285. These are distinct dated source statements,
  not an independently counted dataset. Reconcile versions/count units and terms
  before acquisition. Preserve assay context, repeated observations and chemical
  forms; annotation of entry does not guarantee endosomal escape or cytosolic
  delivery. Experimental positives do not automatically supply measured negatives
  or an independent benchmark against models trained on earlier CPPsite releases.

## Additional lead: LLM-CPP-prediction

[Frozen source](https://github.com/hhy507/LLM-CPP-prediction/tree/fa9a466798035f1fef8ddcf4263d20c54a82a1ec)
and [2026 primary paper](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2026.1845913/full)
describe deterministic features derived from LLM-proposed rules, classical CPP
classifiers and computationally assessed candidates. MIT code and model filenames
are visible. Old NumPy/scikit-learn/SciPy constraints, native generation entry
points and exact preprocessing still require review. The separate direct-LLM
baseline invokes external services; it is not required merely to evaluate fixed
rule features. This lead has no resource conversation yet. Reported computational
candidates are not experimentally established delivery vehicles.

## Bounded priorities and stewardship

For further source/terms review, LightCPPgen and CPP_Design offer complementary
optimization and generative routes. MLCPP 2.0 is a useful uptake-definition/data
reference. pLM4CPPs and CPPpred-En need preprocessing/artifact clarification;
their scores should not be combined as independent calibrated evidence. ELP–EEP
is particularly relevant to the later cargo/endosomal-escape question.

These are recommendations for investigation, not selected dependencies or a new
CPP implementation commission. The current HydrAMP work, Macrel acceptance and
two selectors retain their exact scope. Keep actionable adoption work in owning
issues when commissioned; maintainers own these discovery conversations.
General molecular representations, chemistry and formats remain in MolSysMT.
