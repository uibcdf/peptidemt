# HydrAMP C0: source inventory, exact overlap and measured-panel eligibility

Status: **model-free audit delivered; no independent cohort qualified**,
2026-11-04 (local date). Scientific owner:
[HydrAMP #3](https://github.com/uibcdf/hydramp/issues/3); consumer:
[PeptideMT #32](https://github.com/uibcdf/peptidemt/issues/32). This report advances
C0 of the [comparison proposal](hydramp_scientific_comparison_protocol.md).
It does not approve that proposal's endpoints, chemistry views, similarity rule,
sample sizes, equivalence margins or execution. The earlier proposal and its
byte-identical owner mirror retain their original hashes.

## Finding and consequence

Public data are available and useful. Their availability does **not** supply an
independent measured cohort compatible with the current HydrAMP consumer route.
The source inventory and exact raw-string overlap checks are complete for the
named files below. C0 as a whole remains partial: chemical-entity agreement,
assay interpretation, component-specific checkpoint exposure, source-use terms
and an approved relatedness analysis still precede a frozen cohort.

- The thirteen compared Zenodo members match the pinned starter files byte for
  byte. This establishes a reusable public reference inventory, not the identity
  of the Google Drive archive or the history of particular checkpoint weights.
- Deep_AMP's thirty functional designs are 39–49 residues long; none fits the
  unchanged 1–25-residue HydrAMP route. Its quantified synthetic panel contains
  22 of those designs. No truncation, initial-M removal or negative relabelling
  is performed to obtain eligible cases.
- Original HydrAMP Tables 1–2 contain 42 occurrences / 39 distinct sequences,
  all within the sequence length/alphabet view. The article explicitly states
  that **all synthesized peptides have a C-terminal amide group**. Retaining
  that annotation makes all 42 incompatible with the current unassessed-chemistry
  gate. Erasing it would change the scientific contract.
- Six of those 39 historical strings occur in the inspected published pools;
  three occur in `mic_data.csv`. This is evidence of source-pool overlap, not
  proof of which individual rows fitted a named checkpoint. The other 33 are
  not thereby certified independent.

The evidence is useful for faithful historical regression and for designing a
later scientific comparison. It establishes neither generalization nor better
biological proposals from the modern port.

## Sources acquired and identity established

The [evidence receipt](evidence/hydramp_C0_data_audit.json) retains exact source,
provider, script, output and PDF identities. Raw files and row-level audit data
stay in ignored `local_data/hydramp-C0-audit-yqpagjub/`; public issue updates
contain summaries and public source links, not uploaded attachments.

1. [Zenodo record 7420278](https://zenodo.org/records/7420278): only `data.zip`
   was acquired, 10,676,535 bytes. Its MD5
   `5168e9260c27df1d50a76eb5ecab7aef` matches the published metadata. For each
   of thirteen named training/reference members, the computed Git blob SHA-1
   equals the corresponding blob at
   [starter commit 7804df86](https://github.com/szczurek-lab/hydramp-starter-kit/tree/7804df862872ccc6d09fe01c41bafbca194cfa31/data/training).
   Per-member SHA-256, schemas, counts and duplicate occurrences are retained.
   Generated benchmark files elsewhere in the ZIP are not treated as fitting
   data or as measured ground truth.
2. [Deep_AMP commit a44465f7](https://github.com/amirpandi/Deep_AMP/tree/a44465f704f3224120fd3b1c0bc2d5823a1181c8/data):
   `500gen.txt` and the actual filename `30AMP.txt` are retained unchanged.
   The pinned README's plural spelling does not rename the source file.
3. The investigator supplied the main articles and supplementary-information
   PDFs for [HydrAMP](https://doi.org/10.1038/s41467-023-36994-z) and
   [Deep_AMP](https://doi.org/10.1038/s41467-023-42434-9). All four were hashed
   and text-inspected. The relevant HydrAMP Tables 1–2 and Deep_AMP
   Supplementary Tables 5 and 10 were rendered and visually inspected before
   extracting table observations. The corresponding public full-text XML is
   independently retained with its acquisition metadata.

The HydrAMP README's Google Drive link is real and remains a candidate source.
No Drive-versus-Zenodo archive equivalence was established. Selected publisher
XLSX/supplement downloads failed with DNS resolution errors; that observation
does not show that the data are absent, prohibited or globally inaccessible.
The supplied PDFs allow this audit to proceed without another manual download.
No separate models, wheels or generated-results archive was acquired for C0.

## Original published reference pools

The rightmost column applies the **existing** `analogue_input_issues` contract
to the original strings with no supplied chemistry. It is a syntactic
sequence-view count, not chemical-entity eligibility or a reconstructed fit set.

| ZIP member under `data/` | Occurrences | Distinct strings | Length range | Sequence-view-compatible occurrences |
| --- | ---: | ---: | ---: | ---: |
| `Uniprot_0_25_train.csv` | 180,194 | 180,194 | 7–25 | 180,194 |
| `Uniprot_0_25_val.csv` | 22,524 | 22,524 | 7–25 | 22,524 |
| `Uniprot_0_25_test.csv` | 22,524 | 22,524 | 7–25 | 22,524 |
| `mic_data.csv` | 4,546 | 4,546 | 2–190 | 3,444 |
| `unlabelled_positive.csv` | 20,313 | 20,313 | 2–710 | 11,131 |
| `unlabelled_negative.csv` | 25,762 | 25,762 | 34–200 | 0 |
| `veltri_positive.csv` | 2,021 | 2,021 | 11–183 | 892 |
| `veltri_negative.csv` | 1,897 | 1,897 | 11–186 | 854 |
| `dbaasp/dbaasp_clean.fasta` | 3,038 | 3,038 | 10–25 | 3,038 |
| `dbaasp/high_ecoli_activity.fasta` | 929 | 824 | 10–25 | 929 |
| `dbaasp/low_ecoli_activity.fasta` | 394 | 366 | 10–25 | 394 |
| `dbaasp/high_saureus_activity.fasta` | 586 | 533 | 10–25 | 586 |
| `dbaasp/low_saureus_activity.fasta` | 299 | 286 | 10–25 | 299 |

The union has 275,226 distinct raw strings, of which 239,940 pass that
sequence-only view. The three UniProt split files have no pairwise exact-string
intersection. Other pools overlap: for example, 2,182 MIC strings occur in the
unlabelled-positive pool. Two full strings occur in both unlabelled positive
and negative pools; source labels are preserved rather than reconciled by fiat.
`veltri_negative.csv` membership also overlaps the unlabelled-positive pool;
filename labels cannot be promoted to a common experimental endpoint.

This is **not** a claim that the raw negative pool was unusable by the original
training procedure. Static inspection of
[`AMPDataManager`](https://github.com/szczurek-lab/hydramp/blob/6590d2f4c2963f25d30669052a4c4a857e0e7279/amp/data_utils/data_loader.py)
shows length filtering of positives and sampling of shorter subsequences from
long negative inputs. Absence from full original strings does not exclude
exposure to a derived fragment. This audit does not execute or recreate that
sampling, recover checkpoint-specific fit logs, or treat raw-pool membership as
proof of fitting exposure.

The original MIC notebook uses the nominal test subset during final validation
and early stopping. The preparation notebook pools E. coli measurements by
sequence and averages `value`, then exports only sequence/value. The original
strain, chemistry, assay conditions and observation-level censoring cannot be
recovered from that two-field table alone. The starter's log10(MIC/µM)
description and the notebook's strict `value < 1.5` label remain source
observations; no clinical breakpoint, unit conversion or cohort label is
adopted by this audit. Assumed negatives remain assumed negatives.

## Deep_AMP: sequence lists, screening and measured activity

| Inspected material | Actual content | Role and current eligibility |
| --- | --- | --- |
| `500gen.txt` | 503 distinct records, headers `gen1` through `gen503`, 35–48 residues | Candidate list; zero sequence-view-compatible records. Its mapping to the reported 500 screened candidates is unresolved. No three records are silently removed or called controls. |
| `30AMP.txt` | 32 distinct records: AMP1–AMP30 plus BP100 and CecropinB | Thirty selected functional designs, 39–49 residues; zero compatible designs. The two named controls remain separate. |
| Supplementary Table 10 | 22 synthesized designs with E. coli MIC, B. subtilis MIC, CC50 and HC50 in µM | Quantified synthetic panel, not thirty MIC-tested designs or 500 measured negatives. All 22 exceed 25 residues. Reported `>` bounds and replicate counts are preserved. |

The only string in `30AMP.txt` passing the bare sequence view is the 12-residue
BP100 control. That is not an independent designed-cohort member and does not
qualify its exact experimental chemical entity. Its initial M is retained.
No exact raw-string intersection was found between either whole sequence list
and the thirteen HydrAMP pools above. This limited result is not a homology,
fragment-exposure or chemical-identity certificate.

The paper distinguishes cell-free production/growth screening from subsequent
chemical synthesis; eight of the thirty functional designs did not yield a
successfully synthesized peptide. Those failures are not negative purified-
peptide MIC observations. Repository biochemical tables provide descriptors
and tags; their presence is not a substitute for the quantitative assay table.

The Methods text describes MIC using the **highest** concentration with no
visible growth. This source wording needs interpretation before endpoint
qualification; it is retained as an unresolved textual ambiguity, without
silently redefining the values. Synthesis-resin information is not promoted
here to explicit, verified peptide-level termini. No author contact or report
in the third-party repository is made.

## Historical HydrAMP panel and chemistry gate

Table 1 supplies eleven occurrences; Table 2 supplies thirty-one. Three strings
repeat between them, leaving 39 distinct strings. All 42 occurrences pass the
bare alphabet/length view; **none passes when the documented C-terminal amide
annotation is retained**. Raw table cells, source/table row identifiers,
chemistry evidence, exact overlap-member lists and original units remain in
the row-level audit. The six overlapping strings account for seven table
occurrences; three distinct strings occur in the MIC source pool.

Table 1's strain header/caption names E. coli ATCC **43927**, whereas the
Methods names ATCC **43827**. The audit preserves both strings and flags the
ambiguity. Table 2's distinct strain columns are not pooled. MIC/MBC and HC50
remain separate endpoints, `>` bounds are retained, and µg/mL is not converted
to µM using an assumed molecular mass. Model/preselection history also makes
these panels unsuitable for an unqualified generalization claim.

This observation identifies a **consumer scientific-view decision**, not a
MolSysMT parser defect. A later proposal may explicitly relate a documented
amidated experimental entity to an unchanged sequence-model input for a stated
question. That relation requires investigator review, retained provenance and
tests; this audit neither implements it nor clears `SequenceRecord.chemistry`.

## Execution, terms and follow-up

FASTA interpretation uses PeptideMT's existing receiver calling MolSysMT's
public `file_fasta.parse_records`; no parser, alignment or molecular-identity
implementation is copied. The shared development provider is MolSysMT
`71fbe4f46d3c70e4e973c8025f01752a8c9b1084`, version
`0.23.0+322.g71fbe4f46`, from the local editable source. The PeptideMT source
hashes for its current admission and receiver are retained because those files
are local/uncommitted work. Owner/consumer runtime sources and environments
are not changed by C0.

The two guarded analysis processes run sequentially on CPU 0/1, with one
numerical thread and no network in analysis. Their reported maximum RSS is
252.33 MiB and 224.76 MiB. Imports of model engines and reads of common
checkpoint/PCA formats are forbidden. **Zero learned-model, Macrel, PCA,
descriptor, training, GPU or new alignment calls occur.** PDF extraction is a
separate read-only document tool operation. No package is installed, no old
scientific campaign is repeated, and no exhausted budget is reused.

The article licences and Zenodo's MIT metadata identify source-level notices;
they do not by themselves clear redistribution or every incorporated database's
terms. Source-use review remains partial. The locally supplied PDFs are not
uploaded. No new issue, upstream message, commit, push or package release is made.
Existing scientific-comparison and consumer issues retain this finding; product
modernization remains separately tracked by HydrAMP #4.

Next work can continue without models:

1. Prepare a concrete experimental-entity/sequence-view proposal for historical
   replication, preserving the amide annotation, assay estimand and source
   limitations. Approval would qualify a specific view, not biological
   equivalence or an independent external benchmark.
2. Resolve the assay/source-use and checkpoint-exposure evidence needed for
   that panel. Keep source ambiguities explicit; third-party contact still
   requires separate permission.
3. For an independent performance question, identify a separate measured
   cohort compatible with the approved length/chemistry view. Freeze its source,
   observations, exclusions and exposure/relatedness policy before predictions.
   Deep_AMP's full-length designed panel cannot fill this role under the current
   25-residue contract. No approved 128-case cohort exists yet.
4. Review the scientific endpoint, relatedness policy, uncertainty and absolute
   quality/equivalence criteria before any future exact bundle/input/host/call
   authorization. Existing D41/D44/D45 acceptance and exhausted allowances remain
   unchanged.
