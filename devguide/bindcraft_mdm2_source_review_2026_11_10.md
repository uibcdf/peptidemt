# BindCraft–MDM2: source access and reproducibility review

Status: **source review delivered; no model or chemical domain admitted**,
2026-11-10. Owner: [PeptideMT #33](https://github.com/uibcdf/peptidemt/issues/33).
The investigator commissions this review after the
[docking/binder exploration](peptide_protein_binding_survey_2026_11_10.md).
Its outcome informs the [comparative pilot proposal](mdm2_comparative_pilot_proposal.md).
The [source receipt](evidence/bindcraft_mdm2_source_review_2026_11_10.json)
binds actual documents, observations and bounded inspection jobs.

## Finding

The study is valuable evidence for short-peptide binder design and deserves
further investigation. The reviewed public package is **not yet a received
benchmark of chemically identical inputs, calibrated affinities and experimentally
determined poses**. Separate its experimental specimens, design sequences,
predicted structures and assay stages before drawing a comparison.

Recommend a first, fixed-input structural pilot using the already qualified
1YCR reference. Keep this 2025 study as a separate candidate experimental arm
while resolving its identity and endpoint questions. Neither the study's promise
nor our document acquisition selects BindCraft, HADDOCK3 or Boltz-2 for execution.

## Actual sources and access

Primary study: Filius et al., *Evaluating BindCraft for Generative Design of
High-Affinity Peptides*, DOI [10.1021/acschembio.5c00774](https://doi.org/10.1021/acschembio.5c00774),
online 18 November 2025. PMID 41251237; PMCID PMC12723675.

The ordinary PMC page returned a browser-check document in this run. Its contents
were not treated as article text and no challenge was solved. The documented
[NLM BioC Open Access service](https://www.ncbi.nlm.nih.gov/research/bionlp/APIs/BioC-PMC/)
supplied the article's machine-readable text. The received document identifies
both the expected PMCID and DOI. It is a BioC transformation, not a claim to
possess the original publisher HTML or its images. Retain passage offsets/indices
and original metadata. Acquisition-resource attribution: Comeau, Wei, Islamaj
Doğan and Lu (2019), [PMC text mining subset in BioC](https://doi.org/10.1093/bioinformatics/btz070),
separate from the experimental authors and from executed scientific models.

The public [ACS Figshare supplement](https://acs.figshare.com/articles/journal_contribution/Evaluating_BindCraft_for_Generative_Design_of_High-Affinity_Peptides/30647311)
is version 1, DOI `10.1021/acschembio.5c00774.s001`, and supplies one 55-page PDF.
The received 2,588,492 bytes match Figshare's published MD5 and have SHA-256
`2c0a9e0daf8fbe927e5cd0d9ed43dc2fa3a05c0b50f7a90257808400a1eb6d5d`.
Text extraction and full-page visual inspection of the relevant tables, chemical
displays and selected traces are retained. The receipt identifies which pages
were visually inspected; it does not claim every LC-MS trace was independently
reanalyzed or all 55 pages visually validated.

The BioC article states CC BY 4.0; the Figshare supplement metadata states
CC BY-NC 4.0. Preserve both observations. No common redistribution permission is
inferred and no full paper, supplement or derived dataset is publicly released.
No author or third-party repository was contacted or written to.

## Usable evidence and limits

| Source material | What can be retained now | Limit for the planned study |
| --- | --- | --- |
| Main article, design methods; SI Table S4, physical page 8 | Named filter/settings families, target-source and site description | Not the executed commit, complete configuration, checkpoint/seed or complete campaign output |
| SI Table S1, page 2 | Fifteen labelled screening rows, quantities and fit-quality fields | A single-concentration screening stage; its error kind is not established as SD/SEM/CI |
| Main Figure 1f description | Separate later concentration-series results | Do not replace its endpoint with the screening table or digitize it without a new explicit source policy |
| SI Figure S1, page 3 | A reported p53 reference and competition evidence | Competition and labelled-peptide kinetic measurements remain different observations |
| SI LC-MS panels, pages 9–24 and 39–41 | Literal specimen labels and displayed chemical annotations | Need a specimen-to-assay join; mass/label agreement alone is not full chemical identity |
| Structural illustrations | Author-predicted interaction hypotheses | No experimental pose truth for the newly designed complexes is supplied by those illustrations |

### Chemical entities and sample correspondence

The visually checked screening displays include an acetylated biotinylated-lysine/
beta-alanine extension and a C-terminal primary amide. Competition displays
for B1/B17 instead show acetylated, amidated cores without that extension.
The p53 reference also has its own labelled specimen display. A design sequence,
labelled screening specimen and unlabelled competition specimen must therefore
remain distinct entities until their relationship is explicitly admitted.
Removing the tag is a scientific approximation, not format conversion.

The main text's positional biotinylation descriptions conflict; the displayed
specimen annotations provide useful additional evidence without authorizing
silent correction of the original wording. Full stereochemistry, assay receptor
construct/provenance and equivalence to the crystallographic construct still
need evidence. The inspected MDM2 assay methods do not identify those receptor
details. MolSysMT owns any later molecular interpretation/construction; no
local graph assembly or sequence parser is introduced here.

### Endpoint and quality correspondence

Table S1's screening fits and the later reported binding curves are separate
assay stages. Poor-fit numeric entries do not become reliable affinities merely
because a number is printed. Conversely, poor fit alone does not establish a
chemically verified nonbinder. Preserve every row and its actual quality status.
The source's fit-quality rule is not adopted as a PeptideMT bioactivity definition.

The unqualified `Error` columns cannot be relabelled as SD or interpreted as a
confidence interval. Unknown replicate counts and raw-curve availability remain
unknown. Do not apply D53's source-specific SD receiving contract to this source
or pool its kinetic BLI endpoint with Li 2010 SPR-competition Kd.

### Identity and reporting discrepancies to preserve

- SI Table S1 contains B16; the MDM2 LC-MS caption inventory instead includes
  B15 and B19, which are absent from that table. B15's inspected image header
  also says B15. Do not rename B15 to B16 to force a match.
- SI Figure S38, physical page 41, has a B1 caption while its internal specimen
  header says B17. Keep both source occurrences and the conflict.
- SI Figure S1's caption refers to four concentrations while listing two; the
  displayed legend has two. Do not invent two missing observations.
- The main Results/SI Table S4 and main Figure 1 caption give different site
  descriptions. The supplementary table supports the Results description, but
  the actual executed input configuration is still not received.
- The main narrative's seven/eight kinetic-count wording remains unreconciled.
  Retain the distinction between generated, selected, purified, screened and
  subsequently characterized populations.

These are source-custody questions, not evidence that BindCraft itself has a bug
or that the experimental binding results are false. Findings remain in authorized
PeptideMT records; external publication/contact has not been authorized.

## Reproducibility disposition

The reviewed Figshare package lists only the PDF. It does not deliver the complete
generated campaign, original target input file, machine-readable ranks/predicted
complexes, exact executed configuration/checkpoints/seeds, raw instrument exports
or an exact software/environment snapshot. This is a statement about the reviewed
delivery, not proof that no other copy exists. The article allows further data
requests, but that statement is not permission for us to contact anyone.

Current public BindCraft source is independently inspectable; it is not the
paper's authenticated runtime. Its named settings do not prove byte identity
with the executed files. No modern rerun would establish faithful reproduction
merely by obtaining a similar number of binders.

**Disposition:** suitable for an attributed design-evidence review and a future
source-specific assay-admission proposal. Not ready as an independent pose
reference, a complete affinity-ranking benchmark, or an exactly reproducible
generation experiment. Its prior exposure is explicit. The next structural
pilot can use 1YCR without treating these unresolved specimens as admitted inputs.

## Inspection scope and resources

All work is source/document inspection. No molecular provider was imported,
no chemical state was constructed or repaired, no weights were downloaded and
no docking/generation ran. PDF jobs used the existing process supervisor,
serial CPU0/1, one numerical thread, a self-selected 512 MiB aggregate sampled
RSS stop and a 4 GiB available-host reserve, within the investigator's ceiling.
Each retained job declares its time/address-space/output bounds. Acquisition
requests are individually size/time bounded and keep their source metadata.
Documentation/inspection checks do not provide model or biological qualification.
