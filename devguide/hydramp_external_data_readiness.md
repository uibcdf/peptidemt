# External HydrAMP validation data: bounded gap review

Status: **model-free follow-up delivered; no independent same-endpoint cohort
qualified**, 2026-11-05. Scientific owner:
[HydrAMP #3](https://github.com/uibcdf/hydramp/issues/3); consumer:
[PeptideMT #32](https://github.com/uibcdf/peptidemt/issues/32).
The investigator commissions this review after the completed historical
comparison. It changes no scientific endpoint, chemistry admission or model.

## What was reused and what this review adds

The [C0 audit](hydramp_C0_data_audit.md) already established the thirteen
published/starter corpus identities and historical/Deep_AMP limitations. The
[target-provenance review](hydramp_historical_endpoint_review.md) already traced
the native pooled molar target and nominal-test validation use. Those inventories,
training reconstructions and scientific campaigns were not rerun.

This review inspects retained checkpoint metadata and two later experimental
sources, and computes a new candidate panel's exact-string overlap against the
existing thirteen corpora. The [receipt](evidence/hydramp_external_data_readiness.json)
retains exact source bytes/revisions, guarded analysis, owner-reader identities,
resource use, access limits and dispositions. All model/parameter/PCA imports
and reads, prediction, native encoding, molecular transformations and new class
labels are prohibited. No raw candidate sequences are published here.

## Checkpoint exposure: narrower known facts

The retained epoch-37 model has seventeen JSON configuration files. Their
inspected keys describe architecture, layer behavior and initialization. They
do not provide a fitting-row manifest, sampled-negative-fragment ledger,
component-specific split membership or a link between such a ledger and these
exact weights. The numerical parameter files were not opened or deserialized.
This observation concerns this retained bundle; it does not assert that no
other original training record exists.

The already inspected MIC notebook uses its nominal test subset during final
fitting validation/early stopping. Original data management also samples short
fragments from longer negative examples. Consequently:

- Published `test` filenames do not certify untouched model selection.
- Absence from full strings does not rule out exposure through a fragment.
- Later publication is not proof that a particular sequence or measurement
  postdates every fitting or selection step of an incompletely traced checkpoint.
- Exact source-pool overlap is evidence about known corpora, not a reconstruction
  of every row that actually fitted each component.

The original-reference commit and the epoch-37/starter provenance statement
remain distinct from independently verified original-Drive byte identity.
No new attribution of fitting history or change to the accepted bundles follows.

## Candidate 1: AMP-Diffusion reported experimental MICs

The original publication is Torres et al.,
[Cell Biomaterials (2025), DOI 10.1016/j.celbio.2025.100183](https://doi.org/10.1016/j.celbio.2025.100183).
The [challenge starter's experimental directory](https://github.com/szczurek-lab/ampdiffusion-starter-kit/tree/1a862af9078e6b55c87d1fa576f3da81851ba94b/experimental)
provides a curated measured-MIC table, separate from its newly generated
candidate lists. This is a candidate experimental source, not commissioning or
adoption of the AMP-Diffusion model.

The exact [CSV](https://github.com/szczurek-lab/ampdiffusion-starter-kit/blob/1a862af9078e6b55c87d1fa576f3da81851ba94b/experimental/mic.csv)
is 46,598 bytes, SHA-256
`3da5adb7814f00b5f331eedd3dc909c55ee66cc1561e1bf33d5c1753d30eb82d`;
its Git blob matches `19f2ec63b88e7b42c4dbbe904e1a1dcffb943ce6` exactly,
including line endings. Analysis checks a complete 46-peptide ×11-strain grid,
one consistent literal sequence per ID and 46 distinct sequence strings.

| Observation | Actual finding | Consequence |
| --- | --- | --- |
| Source coverage | 506 rows, 46 peptide IDs, eleven strains | Rows across strains are not independent peptide cases |
| Current sequence-only gate | 35 peptides pass; eleven exceed 25 residues | Preserve all originals; no shortening, repair or new length admission |
| E. coli observations | ATCC 11775, AIC221 and AIC222; zero ATCC 25922 rows | No candidate row supplies the unchanged D46/D47 strain-specific endpoint |
| Potential narrow ATCC 11775 subset | 35 sequence-view-compatible rows: twelve `=` and twenty-three `>` relations | Exact measurements and censored bounds remain distinct; these are not adopted positive/negative labels |
| Reported unit | µM; curated right-censoring ceiling is 64 µM | No substitution of bounds or automatic conversion to the historical µg/mL endpoint |
| Known exact corpus overlap | Zero of all 46 strings, including zero of the 35 compatible strings, match any of the thirteen retained pools | Favorable known-corpus evidence; fragment/relatedness and checkpoint-specific exposure remain unresolved |
| Assay metadata in this CSV | Medium is MHB; inoculum, pH and salt fields are blank in all 506 rows | Missing metadata remains unknown pending primary-source verification |
| Chemistry metadata | `modification` is blank in every row | Blank is not evidence of free termini or absence of modifications |

FASTA members of the known corpus were read through the existing PeptideMT
transport to **MolSysMT `file_fasta.parse_records`**, using the current editable
development source. CSV handling is ordinary tabular metadata audit. Existing
PeptideMT admission supplies only the finite sequence-view check. No local
FASTA parser, mass calculation, chemical canonicalization, sequence mutation,
alignment, fragment sampler or generic molecular utility was implemented.

The curation README attributes the data to the paper and states CC BY 4.0; the
starter repository separately supplies an MIT code notice. The full primary
experimental table, row transcription, termini/stereochemistry and complete
assay conditions were not independently verified here. Official article/PDF
retrieval returned HTTP 403; the supplied local paper folder contains the four
earlier HydrAMP/Deep_AMP PDFs, not this paper. Code notices are not a substitute
for source-data provenance/use review. No raw data are redistributed.

## Candidate 2: AMPSphere experimental study

The [2024 Cell primary article](https://pmc.ncbi.nlm.nih.gov/articles/PMC11666328/)
reports experimental MICs in µM and lists E. coli ATCC 11775 and two MG1655-derived
strains, rather than the current ATCC 25922 case. Its assay medium also differs
from the AMP-Diffusion curation. Candidate selection includes Macrel filtering,
and one selection arm uses additional predictors; the nominal random arm is
still sampled within filtered candidates. These observations limit possible
generality and independence from the selection procedure. The resource remains
useful for a different, explicitly scoped question. No row-level cohort or
length/chemistry eligibility is claimed: this review stops at the source/assay
gate, without downloading its large catalogue or silently pooling strains.

## Disposition and concrete next choices

**No newly examined record is qualified for the unchanged ATCC 25922 /
reported-mass historical endpoint.** This is a bounded conclusion about the
inspected sources, not a claim that no suitable external data exist anywhere.
The broader C0 audit remains partial. The completed historical agreement and
its primary AUC of 0.653846 remain unchanged.

The 35-row AMP-Diffusion ATCC 11775 subset is a concrete candidate for a future
**external-assay transportability** study. It is not yet an accepted independent
test set. The recommended order is:

1. Verify the curation against the original experimental table and methods,
   preserving chemical entities, censoring, replicates and source-use evidence.
   Document any irrecoverable fields rather than filling defaults.
2. Review the proposed change of strain/estimand and reported-molar endpoint
   explicitly. Retain µM as reported during review; a physical mass conversion
   would additionally require adequate entity data and MolSysMT/PyUnitWizard.
   No new cutoff, probability-calibration target or binary labels are selected
   by this audit.
3. Agree a defensible exposure/relatedness policy and the exact claim it permits.
   Do not equate zero literal overlap with no homology or proof of unseen
   checkpoint inputs. Use the owning component's supported operations when a
   molecular comparison is actually specified; report real missing capabilities
   there instead of adding them to PeptideMT.
4. Freeze a cohort and prospective metrics only after those scientific choices.
   Counts may shrink; the old unapproved 128-case C2 proposal is not fulfilled by
   these 35 source rows. A later run would use its own bounded D49 declaration.

This would assess the fixed MIC head on a different assay, not biological
quality of generated peptides, other families or general AMP membership. New
training, models, feedback and target-conditioned design remain separate work.
No implementation is modified to obtain closer legacy agreement.

Keep existing #3/#32 open. The independent-product review in HydrAMP #4 can
progress without treating these unresolved scientific data questions as a reason
to postpone all product work. No new issue or message is sent to either external
source repository; their curation limitations are retained in our authorized
owning records. Model budgets are unchanged; the guarded data analysis took
2.62 s and peaked at 255,660,032 bytes sampled aggregate RSS, with one numerical
thread on CPU0/1 and zero neural evaluations. Evidence owner: #3/#32; retention
review by 2026-11-19.
