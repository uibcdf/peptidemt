# Scientific resources: catalogue and Discussions

Status: **three-category layout accepted; catalogue, forms and five opening
conversations published**, 2026-10-29. API readback verifies categories,
descriptions and the published bodies, including their navigation cross-links.
The investigator explicitly authorized publication of these five texts and the
catalogue/forms. The [publication receipt](evidence/scientific_resources_discussions.json)
records the source commit, form hashes, discussion identities and body hashes.
Section grouping, actual open-ended formats and rendered forms have not been
independently verified in the browser.
Navigation: [design guide](README.md) · [source survey](generative_resource_survey.md)
· [family/resource semantics](functional_families.md).

## Assessment and observed precedents

Discussions is suitable for permanent discovery, comparison, questions and
scientific deliberation. A versioned catalogue provides maintained navigation and
dated technical state. Owning issues remain appropriate for bounded integration,
defects and qualification. A catalogue has no completion criterion that would
make it a useful permanently open implementation issue.

Initial read-only authenticated GitHub observation on 2026-10-29 found the
following state, before the investigator created the three resource categories:

| Repository | Discussions state and observed use |
| --- | --- |
| PeptideMT | Enabled; Announcements, Q&A and Ideas; zero discussions. Existing setup is received in [closed #3](https://github.com/uibcdf/peptidemt/issues/3). |
| TopoMT | Enabled; common categories plus External Tools and Reading List; eleven discussions, including catalogue #68 and five provider conversations #69–#73. |
| DockingMT | Enabled; common categories; one welcome announcement. No tool-catalogue conversation observed. |
| PharmacophoreMT | Enabled; common categories; zero discussions. |
| ElastNetMT | Enabled; common categories; zero discussions. |

TopoMT is the concrete analogue: [catalogue discussion #68](https://github.com/uibcdf/topomt/discussions/68),
[fpocket conversation #69](https://github.com/uibcdf/topomt/discussions/69), and its
[maintained catalogue](https://github.com/uibcdf/topomt/blob/5f6239f0ee21fecca947f73790b139053c6aaa62/devguide/external_tools_catalog.md).
The inspected catalogue blob `cb03f68f7a9fe7ffbca4fd38bb395ccc64fc61dc`
matches the live main document. Its conversations link to technical records
instead of copying their changing evidence. The other three peers do not currently
provide that same catalogue precedent.

This fits the [MolSysSuite Discussions policy](https://github.com/uibcdf/molsyssuite/blob/31613c2322eab767fb316c5737bf4f56cba48d6d/devguide/github_discussions.md):
keep the three common categories, give local extensions a purpose/owner/durable
destination, provide a form for additional intake, and move actionable work to
owning issues. API observation verifies names, descriptions and Q&A answerability;
it does not independently certify UI-only category-format settings.

## Accepted category layout and observed configuration

The investigator selected the following categories for **Scientific Resources**
and reported creating all three. A subsequent authenticated API readback on
2026-10-29 verifies their exact names, slugs and descriptions, each with
`isAnswerable=false`. Announcements, Q&A and Ideas remain present; Q&A is
answerable. Five opening discussions have subsequently been published and verified.

| Category / slug | Purpose | Intended format | Maintained destination |
| --- | --- | --- | --- |
| [Tools and Models](https://github.com/uibcdf/peptidemt/discussions/categories/tools-and-models) / `tools-and-models` | Compare generators, predictors, software and learned models, including capabilities, availability, licences and limitations. | Open-ended discussion | This catalogue, [resource survey](generative_resource_survey.md), provider records and qualification evidence. |
| [Datasets and Benchmarks](https://github.com/uibcdf/peptidemt/discussions/categories/datasets-and-benchmarks) / `datasets-and-benchmarks` | Discuss databases, datasets and evaluation resources, provenance, context, coverage, data leakage and reproducibility. | Open-ended discussion | This catalogue, [functional-family/data review](functional_families.md), and dataset or qualification records when needed. |
| [Reading List](https://github.com/uibcdf/peptidemt/discussions/categories/reading-list) / `reading-list` | Discuss papers and reviews, their relevance, findings, limitations and open questions. | Open-ended discussion | This catalogue, [literature review](literature.md), and relevant topical scientific guides. |

The API readback is category-level evidence; it does not prove section nesting,
distinguish every non-Q&A format or verify rendered intake forms. The intended
open-ended formats and section grouping are separate browser checks.

The initial proposal was one **Tools and Resources** category, followed by a
section containing only that category. The investigator correctly challenged the
value of a single-category section. On 2026-10-29, the proposal was revised to
the three distinct categories above; the investigator then created them.
These are complementary levels:
[GitHub sections group categories](https://docs.github.com/en/discussions/managing-discussions-for-your-community/managing-categories-for-discussions),
and conversations belong to categories. A section alone does not provide a place
to post a tool. The old broad category name is superseded by **Tools and Models**.

Do not initially make AMP, CPP and every further family separate categories.
Family index conversations allow a multifunctional tool to have one canonical
conversation with links from several indexes. Family categories would make these
indexes more visible in the sidebar, but a conversation still has one category;
duplicating its history across families would create avoidable maintenance.
Reconsider that tradeoff if traffic or distinct stewardship later justifies it.

- **Purpose:** collect and discuss peptide-design/evaluation resources and their
  evidence, contexts, limitations and integration relevance.
- **Accountable owner:** PeptideMT repository maintainers until explicit named
  delegation, following the common policy; no response-time promise.
- **Durable destination:** this versioned catalogue, the dated source surveys,
  provider-specific records when useful, and existing scientific decisions.
- **Disposition:** curate new evidence into the relevant record; accepted,
  deferred or rejected choices retain date/reason and a revisit condition for
  deferral. Link the conversation and destination both ways. Concrete work gets
  an owning issue. Recording a resource is not adoption or execution authority.

Published opening conversations:

| Conversation | Category | Purpose |
| --- | --- | --- |
| [#9 Tools and models — catalogue and discovery](https://github.com/uibcdf/peptidemt/discussions/9) | Tools and Models | Stable entry/index; introduce stewardship and link family conversations and the maintained catalogue. Recommend pinning it. |
| [#10 AMP — generators, predictors and evaluation resources](https://github.com/uibcdf/peptidemt/discussions/10) | Tools and Models | Collect and compare AMP resources, initially linking the source survey. Preserve generative conditioning, evaluation and adverse properties as distinct roles. |
| [#11 CPP — tools, evidence and research questions](https://github.com/uibcdf/peptidemt/discussions/11) | Tools and Models | Begin the next family-oriented collection. A focused CPP survey is still pending; define uptake/access context without implying qualified CPP capability. |
| [#12 Datasets and benchmarks — catalogue and evaluation questions](https://github.com/uibcdf/peptidemt/discussions/12) | Datasets and Benchmarks | Entry point for data sources, endpoints, partitioning and fair comparison, linked to the existing family/data review. |
| [#13 Reading list — papers and scientific questions](https://github.com/uibcdf/peptidemt/discussions/13) | Reading List | Entry point for methodological and biological reading, linked to existing literature and topical guides. |

Add ACP and other family/function conversations when their discovery work begins.
Use a family conversation as an index and cross-cutting discussion. As a resource
needs deeper stewardship, give it one canonical conversation and link it from all
relevant family indexes. This supports overlapping/multiple functions without
duplicating a resource's technical history in several family threads. Cross-family
questions can also have their own focused discussion.

Families are navigation, not an exclusive taxonomy. For each association,
distinguish a function actually studied by a versioned resource from a proposed
future application. A CPP mention is not proof of cytosolic access; AMP scores
do not establish CPP or ACP activity. Keep assay/organism/cell/chemistry context.

## Category intake forms

Three published forms match the API-observed category slugs:

- [Tools and Models](../.github/DISCUSSION_TEMPLATE/tools-and-models.yml);
- [Datasets and Benchmarks](../.github/DISCUSSION_TEMPLATE/datasets-and-benchmarks.yml);
- [Reading List](../.github/DISCUSSION_TEMPLATE/reading-list.yml).

Each requires only a resource/reference name, source/identifier and reason for
relevance or question. Category-specific optional fields cover:

- function/family and context, allowing several or unknown values;
- roles: generation, evaluation, search/workflow, representation or benchmark/data;
- code/model/data availability and known licence/runtime evidence;
- observations, limitations and the question to discuss;
- existing related discussion, catalogue record or owning issue.

A new link need not arrive with a completed installation/benchmark audit. Keep
unknowns visible and use the form to aid triage, not as a scientific acceptance
checklist. Before starting another resource conversation, search the catalogue
and existing discussions and link the relevant one when it already exists.
All three share the maintainer ownership and disposition rules above. Choose
the category by the conversation's main subject and cross-link related records.
Do not create a Reading List entry for every paper cited by a tool or dataset;
use it when the reading merits a scientific conversation of its own.

[GitHub requires the forms on the default branch](https://docs.github.com/en/discussions/managing-discussions-for-your-community/creating-discussion-category-forms).
Local YAML/structure checks do not prove live rendering. These files are published
on `main`, verified by a GitHub tree readback. Browser rendering, section grouping
and actual open-ended category formats remain unverified: this session has no
available browser, and creating an in-app browser tab returned unavailable.
Pinning the three category entry points (#9, #12 and #13) remains a browser action;
the inspected public GraphQL mutation surface has no discussion-pinning operation.
These UI tasks do not prevent using the published catalogue and conversations.

## Versioned catalogue and initial family navigation

This file is the maintained navigation point. The
[2026-10-29 generative-resource survey](generative_resource_survey.md) remains a
dated source assessment, with its [exact source inventory](evidence/generative_resource_survey.json).
New observations can update maintained records without rewriting what a previous
source snapshot established. Installation, full hashes, measured outputs and
qualification assertions stay in the corresponding technical records.

| Function/context | Starting references and evidence scope |
| --- | --- |
| AMP and adverse hemolysis | [Macrel acceptance](increment_1_review.md), [HydrAMP qualification work](pending_proposals/qualify_hydramp_increment_2.md), and the [generator survey](generative_resource_survey.md). Only the stated Macrel bundle is accepted; listed generators remain separately qualified or proposed as recorded. |
| CPP and cellular access | [Functional definitions](functional_families.md), [CPP project guides](cpp_guided_projects.md), and CPP_Design in the [source survey](generative_resource_survey.md). These are definitions/research references, not an installed CPP route or a completed CPP census. |
| ACP and selective cellular activity | [CPP-like anticancer case](case_study_cpp_anticancer_mdm2_mdmx.md), [family semantics](functional_families.md), TACaPe/PepGenWL/MMCD in the [survey](generative_resource_survey.md). Context and actual trained-asset availability remain explicit. |
| Target-conditioned or broader chemical design | [Existing engine review](protein_peptide_design_engines.md) and later resources in the [survey](generative_resource_survey.md). Preserve native target/chemistry meanings and the current commissioning limits. |

Resource records should link official sources, reviewed version/date, supported
inputs/outputs, known/unknown conditions of use, scientific limitations, relevant
conversations and bounded work. Roles and readiness are separate facts: a tool
can be both a comparison reference and an optional provider. Catalogue presence
does not certify installation, scientific usefulness or general family support.

## Issues and current work

[PeptideMT #8](https://github.com/uibcdf/peptidemt/issues/8) remains the bounded
HydrAMP preparation/qualification theme. Its survey references are historical
work context, not ownership of the permanent discovery area. Keep source and
qualification evidence, failures and future implementation decisions linked to
that issue. Do not convert or close it merely to relocate broad collection.

Existing [Discussions setup #3](https://github.com/uibcdf/peptidemt/issues/3) is
complete. A useful local category is a new extension, not evidence of a failed
common-category rollout. No new permanently open catalogue issue is proposed.

## Opening post texts

The following English texts were reviewed before publication. Each published
conversation also contains navigation links to the other four conversations;
the publication receipt identifies the exact published body hashes.

### Tools and models — catalogue and discovery

This is the permanent conversation for discovering and comparing tools,
models and computational methods relevant to PeptideMT.

The [versioned catalogue](https://github.com/uibcdf/peptidemt/blob/main/devguide/tools_catalog.md)
maintains navigation and stewardship. Start with the
[source survey](https://github.com/uibcdf/peptidemt/blob/main/devguide/generative_resource_survey.md),
then follow the [AMP](https://github.com/uibcdf/peptidemt/discussions/10) and
[CPP](https://github.com/uibcdf/peptidemt/discussions/11) conversations.

Resources are nonexclusive and can contribute several roles or functions. Share
official sources, what they could contribute, context and open questions. Unknown
licence, runtime, assets or applicability remain unknown until investigated.
Catalogue membership does not imply integration or approval to execute a model.

Concrete defects, integrations and qualification phases use owning issues;
maintained conclusions and scientific decisions link back to the conversation.
PeptideMT's maintainers own triage under the shared Discussions policy.
Related data and benchmark resources belong in Datasets and Benchmarks; papers
that merit their own scientific discussion belong in Reading List. Cross-link
related conversations rather than copying their technical histories.

### AMP — generators, predictors and evaluation resources

Collect and compare resources relevant to antimicrobial peptide design and
assessment here. The [source survey](https://github.com/uibcdf/peptidemt/blob/main/devguide/generative_resource_survey.md)
provides the initial nonexclusive inventory, including HydrAMP, PLUM, OmegAMP,
ARCADIAMP and AMP-Designer, with their separate source/runtime/asset limitations.

Distinguish generative priors/conditions, native internal scoring, external
assessment, selection, MIC context, hemolysis/toxicity and experimental evidence.
Species conditioning is different from binding a named protein. Link new sources
and explain the scientific or operational question; measured results and full
qualification records remain in the versioned guide and their owning issues.

### CPP — tools, evidence and research questions

Collect sources for cell-penetrating peptide design and assessment here. The
focused CPP tool survey is a next research exercise. Initial context is available
in the [family guide](https://github.com/uibcdf/peptidemt/blob/main/devguide/functional_families.md)
and [CPP project guides](https://github.com/uibcdf/peptidemt/blob/main/devguide/cpp_guided_projects.md).

For each source, explain whether the endpoint concerns uptake, cytosolic delivery,
endosomal escape, cargo/context dependence or another defined observation. Link
code, models/data and primary studies when available. Keep predictor, generator,
workflow and benchmark roles distinct. Tools can also appear in other family
indexes, through links to a shared resource conversation rather than duplicate
technical records. Nothing here establishes an already qualified CPP capability.

### Datasets and benchmarks — catalogue and evaluation questions

Collect and discuss data sources and evaluation benchmarks relevant to peptide
design and assessment here. Start with the existing
[functional-family and data review](https://github.com/uibcdf/peptidemt/blob/main/devguide/functional_families.md)
and the [scientific-resource catalogue](https://github.com/uibcdf/peptidemt/blob/main/devguide/tools_catalog.md).
These source reviews are not newly executed benchmarks.

Link the official resource and version or access date when known. Explain the
measured or predicted endpoint, assay/organism/cell and chemical context, source
provenance, reuse conditions and relevant controls or negative data. For proposed
comparisons, discuss partitions, similarity/duplicate controls, possible training
overlap, metrics and reproducibility. Unknowns and untested concerns are welcome.

Maintained evidence and conclusions stay in the relevant versioned guide, linked
both ways. Concrete curation, implementation and qualification work uses owning
issues. Cross-link related tool and reading conversations; inclusion does not
approve a dataset, establish a fair comparison or authorize a scientific run.

### Reading list — papers and scientific questions

Collect papers and reviews that inform peptide research and PeptideMT development
here. Existing starting points are the
[literature review](https://github.com/uibcdf/peptidemt/blob/main/devguide/literature.md),
[functional-family review](https://github.com/uibcdf/peptidemt/blob/main/devguide/functional_families.md)
and [CPP project guides](https://github.com/uibcdf/peptidemt/blob/main/devguide/cpp_guided_projects.md).

For a new reading, link the primary publication or preprint, explain why it
matters, summarize the relevant findings and identify limitations or questions.
Distinguish source-reported results, our interpretations and independently
reproduced evidence. A citation alone is not PeptideMT scientific validation.

Papers that only document an existing tool or dataset can be referenced in that
conversation. Open a separate reading thread when its methods, biological
meaning or evidence merit discussion. Maintained conclusions link to the relevant
versioned guide; actionable work and decisions retain their owning records.
