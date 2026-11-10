# OmegAMP: source review and future qualification questions

Status: **source-reviewed discovery resource; not installed or qualified**,
2026-11-03. Existing conversation: [#17](https://github.com/uibcdf/peptidemt/discussions/17).
Navigation: [AMP card](amp_resource_cards.md#omegamp) · [catalogue](tools_catalog.md).

## Reviewed source and contribution

Official source remains
[`szczurek-lab/OmegAMP@20b691b5`](https://github.com/szczurek-lab/OmegAMP/tree/20b691b5b6f74ef86bc83f34d5610e30cd456c96),
the same commit as the 2026-10-29 survey. The [intake receipt](evidence/scientific_resources_intake_20261103.json)
pins twelve inspected text files across this and the challenge repository; no
checkpoint, embedding binary or dataset is acquired or executed.

The [README](https://github.com/szczurek-lab/OmegAMP/blob/20b691b5b6f74ef86bc83f34d5610e30cd456c96/README.md)
describes diffusion-based AMP generation and separate broad/species/strain
classifiers. The [inference guide](https://github.com/szczurek-lab/OmegAMP/blob/20b691b5b6f74ef86bc83f34d5610e30cd456c96/README-Inference.md)
supports de novo, analogue, fixed-motif and combined routes, with length, charge,
Eisenberg hydrophobicity and AMP conditioning. The so-called unconditional route
still fixes the AMP condition. These property controls are not arbitrary protein
target conditioning or evidence of another peptide family's applicability.

The programmatic generator returns sequences and conditioning; optional output
paths can suppress files. FASTA-driven analogue/motif modes follow input record
counts and correspondence rather than `num_samples`. Seed defaults to `None`;
an explicit seed option is not demonstrated deterministic parity. A separate
prediction CLI exists, but its assets, calibration, contexts and result contract
need their own review. The maintained discussion keeps its reviewed generation
labels; no standalone predictor qualification is inferred.

The README cites a 2026 TMLR/OpenReview paper. The official OpenReview page
requires browser verification in this review, so its biological performance
claims are not independently assessed or transferred to PeptideMT.

## Operational limits before a future commission

The README recommends Python 3.11. The
[manifest](https://github.com/szczurek-lab/OmegAMP/blob/20b691b5b6f74ef86bc83f34d5610e30cd456c96/pyproject.toml)
declares Python >=3.11, a PyTorch/Lightning stack, exact scikit-learn 1.7 and
XGBoost 2.0.3, plus training/notebook/web dependencies. `torch ~= 2.2` is a
compatible-release range, not an exact PyTorch 2.2 pin. No Python 3.14 resolution,
CPU memory qualification or installed minimal inference environment is claimed.

The [loader](https://github.com/szczurek-lab/OmegAMP/blob/20b691b5b6f74ef86bc83f34d5610e30cd456c96/project/config.py)
constructs the data module and calls its training-stage setup before checkpoint
loading. The [entry point](https://github.com/szczurek-lab/OmegAMP/blob/20b691b5b6f74ef86bc83f34d5610e30cd456c96/project/scripts/inference/generate_samples.py)
contains a hardcoded 1,000-step schedule. A small output request therefore does
not itself establish a small neural-call or resource budget. Trace actual asset,
data and initialization requirements before proposing bounded inference.

MIT code licensing is verified from the source file; the README links generator
weights and embedding data on Drive. Those external bytes and asset-specific
permissions remain unverified. Code licensing alone does not qualify the exact
bundle, redistribution or a challenge's public-model/training-data requirements.

## Relevance and disposition

OmegAMP is a useful complementary candidate to HydrAMP and PLUM because its
native diffusion/motif/property controls offer distinct operations. This is a
reason to preserve its resource record, not a measured ranking or authorization
to begin another integration. D38/D39 remain the current bounded HydrAMP work.

The [challenge watchlist](peptide_design_challenges.md) provides a separate place
to assess future participation. Before any new OmegAMP execution or use in a
submission: review exact assets/terms, native chemistry/property meanings,
reproducibility, actual preprocessing/selection and a finite host/call envelope.
Reuse MolSysMT for molecular-system/file operations at the consumer boundary.
No model is installed, weights downloaded, training/inference run, external
report sent or participation commitment made by this discovery update.

The [follow-up in the existing OmegAMP conversation](https://github.com/uibcdf/peptidemt/discussions/17#discussioncomment-19381855)
provides self-contained public source evidence while this new maintained review
remains local. The original opening post and generation/family labels are retained.

The [Discussions publication receipt](evidence/scientific_resource_discussion_updates_20261103.json)
records independent body/label/category readback and retained prior records.
These new versioned review files are local working-tree records; their public
Discussions provide complete source links until a separate source publication.
