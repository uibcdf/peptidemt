# Peptide-design challenges: watchlist and participation review

Status: **discovery watchlist; no participation commitment**, 2026-11-03.
Entry point: [Datasets and Benchmarks #12](https://github.com/uibcdf/peptidemt/discussions/12)
· [catalogue](tools_catalog.md).

Challenges are evaluation resources with an organizer, edition, protocol and
participation terms. They belong in the existing Datasets and Benchmarks category.
The existing index holds the watchlist; an actively reviewed challenge has one
resource discussion with source-supported family labels. Early links can remain
index comments until they merit a maintained record. No new category, family
hierarchy or generic accepted/validated label is needed.

For future additions, record official source and edition, observed date/status,
known deadlines, family/endpoints, sequence chemistry, expected outputs, novelty
and data-overlap rules, reproducibility, model/data disclosure and reuse terms,
cost/access questions and the reason to revisit. Keep unknowns explicit. Review
participation separately from discovering a resource; registration, contacting
organizers, submitting designs, committing public assets or running generators
requires the appropriate investigator authorization.

## AMP Challenge 2027

Resource discussion: [#31](https://github.com/uibcdf/peptidemt/discussions/31),
category Datasets and Benchmarks, label `family:amp`.

**Disposition:** monitor and review when formal dates/protocol/terms are available,
or when investigators commission participation assessment. No deadline, organizer
contact, team registration or public disclosure commitment is made here.

Official [repository](https://github.com/szczurek-lab/amp-challenge-2027/tree/5c8a5d8e2551c8cf572d3d3bfcfe7633b109d91e),
commit `5c8a5d8e2551c8cf572d3d3bfcfe7633b109d91e`, reviewed 2026-11-03.
The [source receipt](evidence/scientific_resources_intake_20261103.json) pins the
inspected README, validator, example generator and manifest/license. The linked
[Kaggle page](https://www.kaggle.com/competitions/amp-challenge) yields no readable
rules/calendar in this review; current submission status is not independently
established. The repository's competition-proposal PDF is present but not reviewed;
its filename does not establish official conference acceptance or final rules.

### Source-reported requirements

The [README](https://github.com/szczurek-lab/amp-challenge-2027/blob/5c8a5d8e2551c8cf572d3d3bfcfe7633b109d91e/README.md)
describes antimicrobial design for clinically relevant bacterial strains,
including resistant ESKAPE pathogens. Its current requirements include:

- **Outputs:** 50,000 unique sequence proposals and a ranked top 100, with the
  method, training/external data, filters and ranking documented.
- **Chemistry:** 20 canonical amino acids, lengths 8–50, linear chains with free
  termini; no amidation or other terminal/chemical modifications.
- **Novelty:** no full-library exact match against the named antibacterial
  reference; top-100 Levenshtein ratio must not exceed 0.8 against that reference.
  This is a declared novelty rule, not a biological-success guarantee.
- **Minimum benchmark track:** weights/inference code may be in a private
  repository with organizer read access, alongside the other required material.
- **Full/co-authorship-eligibility track:** public weights/code/docs, permissive
  OSI-approved licensing, full training-data disclosure/release, `uv.lock`, defined
  Python version, default `uv run generate` entry point and fixed-seed repeatability.
  Eligibility language is not a promise of authorship.

### What the inspected example actually establishes

The [validator](https://github.com/szczurek-lab/amp-challenge-2027/blob/5c8a5d8e2551c8cf572d3d3bfcfe7633b109d91e/scripts/verify_submission.py)
clones a submitted repository, installs dependencies, executes generation twice,
checks file sizes/alphabet/length/duplicates, top-list membership, reference overlap
and the stated Levenshtein threshold, and compares complete output bytes for
reproducibility. None of it is executed here. Structural success is not assay
validation or proof of chemical termini, rights or scientific ranking quality.

The [example generator](https://github.com/szczurek-lab/amp-challenge-2027/blob/5c8a5d8e2551c8cf572d3d3bfcfe7633b109d91e/src/amp_challenge_2027/generate.py)
samples only K/P symbols from stored probabilities and scores by original list
position. It is a format/reproducibility template, not an antimicrobial efficacy
baseline. The repository code is BSD-3-Clause; verify separate data/model and
competition commitments before future reuse or submission. No dataset or numeric
weights are downloaded or interpreted in this review.

### PeptideMT relevance and unresolved questions

This could eventually assess reproducible proposals, selection and independent
experimental outcomes. It does not itself expand PeptideMT's scientific work
order or qualify a provider. [OmegAMP](omegamp_review.md) is an independent
candidate, already in its own discussion; a challenge is not a reason to replace
the current HydrAMP qualification without review.

Before proposing participation, establish final calendar and eligibility,
organisms/assays and scoring/experimental budget, permitted training/model/data
use and disclosure, costs/IP/publication commitments, and genuine independence
from training/reference sets. Preserve the distinction between code licences
and asset/use permission. The existing HydrAMP descriptor profile includes an
amidated charge convention; it cannot silently establish the challenge's free-
termini chemical interpretation. Native length limits, accepted Macrel input
views and D35 selectors also require a separately reviewed challenge workflow.

The benchmark's similarity rule should use the responsible reusable provider,
and molecular-system/FASTA operations remain with MolSysMT. No challenge parser,
new selector, large generation run, model training, package publication or new
scientific acceptance is introduced by cataloguing this opportunity.

The [Discussions publication receipt](evidence/scientific_resource_discussion_updates_20261103.json)
records independent body/label/category readback and retained prior records.
These new versioned review files are local working-tree records; their public
Discussions provide complete source links until a separate source publication.
