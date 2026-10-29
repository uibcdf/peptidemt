# Scientific resources: catalogue and Discussions

Status: **investigator-approved label-based reorganization implemented**,
2026-10-29. All nineteen existing discussions are retained. Five family/role
labels classify fourteen resource cards; five existing indexes remain navigation
and comparison guides. Card texts are unchanged and index changes only append
navigation. The [reorganization receipt](evidence/discussion_reorganization.json)
records before/after body hashes, retained identities, labels and verified searches.

The three resource-type categories retain their existing GitHub names/slugs.
Visual renaming/grouping, form rendering and index pinning remain browser tasks;
these are not claimed as completed. The initial [opening-post receipt](evidence/scientific_resources_discussions.json)
and [resource-card receipt](evidence/resource_card_discussions.json) remain dated
publication evidence rather than being overwritten by this reorganization.
Navigation: [design guide](README.md) · [source survey](generative_resource_survey.md)
· [family/resource semantics](functional_families.md).

## Accepted structure and resource ownership

The investigator authorizes implementation of the final recommendation:

```text
Scientific Resources                         section
  Models and Tools                           category
    One discussion per maintained tool/model
  Datasets and Benchmarks                    category
    One discussion per maintained data/benchmark resource
  Literature and Resources                   category
    One discussion per reading/guide that merits its own conversation
```

Announcements, Q&A and Ideas keep their required names/formats. All three
resource-type categories use open-ended discussions. Families and reviewed
computational roles are labels, not additional categories. This keeps six
categories regardless of the number of families. Versions/checkpoints of one
resource retain their technical provenance within its existing discussion and
versioned records; an individually distinct project/model may warrant its own
record rather than being conflated merely because it shares a family.

Repository maintainers own triage and the controlled label vocabulary, without
a response-time promise. Each resource links its maintained technical record;
accepted/deferred/rejected conclusions retain date/reason and a revisit trigger
for deferral, with bidirectional links. Concrete implementation, missing
capabilities and defects go to owning issues. Discovery threads remain useful
independently of bounded work. The organization does not change D35–D38, accept
models, grant inference calls or redefine scientific families.

## Labels and reviewed scope

Labels belong to an entire discussion. Native Discussion comments cannot carry
labels. Consequently, independently filterable resources retain their own
existing discussions; short discovery notes can still be comments. Source-supported
multifamily resources can carry several family labels without duplicate cards;
general resources can have no family label.

| Label | Meaning |
| --- | --- |
| `family:amp` | AMP-related resource scope; consult source evidence. Not scientific qualification. |
| `family:cpp` | CPP-related resource scope; uptake is distinct from cytosolic delivery. |
| `role:generation` | Source-documented generation; does not qualify execution or generated outputs. |
| `role:prediction` | Source-documented prediction/scoring; consult native endpoints and qualification limits. |
| `role:search` | Source-documented search, optimization or screening; not permission to execute. |

Roles describe the reviewed operation featured in the card, not every internal
scoring head or a qualified standalone API. For example, LightCPPgen has both
prediction and search labels for its separate native operations; ELP–EEP is
classified as a screening/search workflow. Internal scores in a generator do
not automatically turn it into an independent assessment provider. Family labels
are navigation/source scope, not measured activity, cytosolic delivery or
bundle-wide scientific acceptance. Qualification remains in the exact technical
records; no generic accepted/validated labels are introduced.

Fourteen resource cards receive these labels. The five general/family indexes
remain guides rather than independently labelled resource cards, so family/role
queries return individual records rather than mixing them with navigation.
Maintainers add future family/role labels only with a clear definition and
reviewed resource evidence. The vocabulary is shared with issues/PRs: existing
reporting and `component:*` labels are preserved, and no issues or PRs were
relabeled.

## Filtered navigation

All links below were verified against GitHub's discussion search API. Category
queries use the actual current names, including Tools and Models and Reading
List. The intended display names do not imply that a UI rename already occurred.

| View | Matching individual records or category entries |
| --- | --- |
| [AMP resources](https://github.com/search?q=repo%3Auibcdf%2Fpeptidemt+label%3A%22family%3Aamp%22&type=discussions) | 7 |
| [CPP resources](https://github.com/search?q=repo%3Auibcdf%2Fpeptidemt+label%3A%22family%3Acpp%22&type=discussions) | 7 |
| [Generation resources](https://github.com/search?q=repo%3Auibcdf%2Fpeptidemt+label%3A%22role%3Ageneration%22&type=discussions) | 7 |
| [Prediction/scoring resources](https://github.com/search?q=repo%3Auibcdf%2Fpeptidemt+label%3A%22role%3Aprediction%22&type=discussions) | 5 |
| [Search/optimization resources](https://github.com/search?q=repo%3Auibcdf%2Fpeptidemt+label%3A%22role%3Asearch%22&type=discussions) | 2 |
| [AMP generation](https://github.com/search?q=repo%3Auibcdf%2Fpeptidemt+label%3A%22family%3Aamp%22+label%3A%22role%3Ageneration%22&type=discussions) | 6 |
| [CPP prediction/scoring](https://github.com/search?q=repo%3Auibcdf%2Fpeptidemt+label%3A%22family%3Acpp%22+label%3A%22role%3Aprediction%22&type=discussions) | 4 |
| [CPP models and tools](https://github.com/search?q=repo%3Auibcdf%2Fpeptidemt+category%3A%22Tools+and+Models%22+label%3A%22family%3Acpp%22&type=discussions) | 6 |
| [CPP datasets and benchmarks](https://github.com/search?q=repo%3Auibcdf%2Fpeptidemt+category%3A%22Datasets+and+Benchmarks%22+label%3A%22family%3Acpp%22&type=discussions) | 1 |
| [Models and tools](https://github.com/search?q=repo%3Auibcdf%2Fpeptidemt+category%3A%22Tools+and+Models%22&type=discussions) | 16 |
| [Datasets and benchmarks](https://github.com/search?q=repo%3Auibcdf%2Fpeptidemt+category%3A%22Datasets+and+Benchmarks%22&type=discussions) | 2 |
| [Literature and resources (current Reading List category)](https://github.com/search?q=repo%3Auibcdf%2Fpeptidemt+category%3A%22Reading+List%22&type=discussions) | 1 |
| [AMP prediction/scoring](https://github.com/search?q=repo%3Auibcdf%2Fpeptidemt+label%3A%22family%3Aamp%22+label%3A%22role%3Aprediction%22&type=discussions) | 1 |

These are dated counts, not future completeness promises. Resource-type category
views also include the preserved indexes. Family/role views return labelled
resource cards. The [AMP guide #10](https://github.com/uibcdf/peptidemt/discussions/10)
and [CPP guide #11](https://github.com/uibcdf/peptidemt/discussions/11) now link to
these filters; their bodies and the other three index bodies retain their previous
content with appended navigation.

## Current category names and remaining browser work

| Intended display name | Observed current name | Observed slug / form filename |
| --- | --- | --- |
| Models and Tools | Tools and Models | `tools-and-models` |
| Datasets and Benchmarks | Datasets and Benchmarks | `datasets-and-benchmarks` |
| Literature and Resources | Reading List | `reading-list` |

The functional reorganization uses these existing category IDs, so no discussion
needs recreation or transfer. When a browser is available, rename the two display
names, confirm grouping under Scientific Resources and check open-ended formats,
rendered forms and optional index pinning. Then read back the resulting slugs:
update form filenames and category-specific filter URLs only if those observations
require it. No guessed aliases, new family categories or premature form removals.

## Organization history and evidence boundaries

On 2026-10-29 the bootstrap created three resource categories and nineteen
conversations. Subsequent discussion considered type sections with repeated
family categories, a family-first structure with role labels, and family threads
containing resource comments. The repeated-category plan was reopened after the
25-category constraint was considered; comment-based records lose independent
label filtering. The investigator then approved the current small-category,
per-resource, family/role-label model for implementation, explicitly preserving
already published discussions. Earlier suggestions are superseded rather than
additional migration instructions.

Official [discussion management](https://docs.github.com/en/discussions/managing-discussions-for-your-community/managing-discussions),
[search documentation](https://docs.github.com/en/search-github/searching-on-github/searching-discussions)
and [schema](https://docs.github.com/en/graphql/reference/discussions) document
shared labels, category/label search, `Discussion` as `Labelable`, and the absence
of label support on `DiscussionComment`. Live permission/schema inspection preceded
implementation. Fifteen existing labels were preserved; five new labels were
created additively and independently read back. Thirteen actual search queries
were verified. API observations do not certify browser-only configuration.

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

## Bootstrap publication and category observations


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

The bootstrap used family index conversations within a shared tools category.
They remain optional guides/comparisons. The accepted label-based organization
provides direct family/role filtering while retaining all existing conversations.

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
| [#11 CPP — tools, evidence and research questions](https://github.com/uibcdf/peptidemt/discussions/11) | Tools and Models | Family-oriented collection linked to the bounded CPP survey; define uptake/access context without implying qualified CPP capability. |
| [#12 Datasets and benchmarks — catalogue and evaluation questions](https://github.com/uibcdf/peptidemt/discussions/12) | Datasets and Benchmarks | Entry point for data sources, endpoints, partitioning and fair comparison, linked to the existing family/data review. |
| [#13 Reading list — papers and scientific questions](https://github.com/uibcdf/peptidemt/discussions/13) | Reading List | Entry point for methodological and biological reading, linked to existing literature and topical guides. |

The first resource-card set is maintained in [AMP cards](amp_resource_cards.md)
and the [CPP resource survey](cpp_resource_survey.md), including a separate
CPPsite3 data record. These records reuse previous AMP qualification/source
evidence and add bounded CPP source inspection; they do not commission adapters.

Existing family index conversations remain useful guides or comparisons.
Filtered label links provide direct discovery; a coordinating discussion is not
required for every new family. Retain cross-links for overlapping functions and
use focused discussions for genuine comparative questions.

Families are navigation, not an exclusive taxonomy. For each association,
distinguish a function actually studied by a versioned resource from a proposed
future application. A CPP mention is not proof of cytosolic access; AMP scores
do not establish CPP or ACP activity. Keep assay/organism/cell/chemistry context.

## Initial resource conversations

These are permanent discovery/stewardship conversations, separate from bounded
implementation and qualification issues. The [card-publication receipt](evidence/resource_card_discussions.json)
records their identities, exact body hashes and index updates.

| Resource | Navigation | Conversation | Maintained record | Labels |
| --- | --- | --- | --- | --- |
| Macrel | AMP | [#14](https://github.com/uibcdf/peptidemt/discussions/14) | [Record](amp_resource_cards.md#macrel) | `family:amp`, `role:prediction` |
| HydrAMP | AMP | [#15](https://github.com/uibcdf/peptidemt/discussions/15) | [Record](amp_resource_cards.md#hydramp) | `family:amp`, `role:generation` |
| PLUM | AMP | [#16](https://github.com/uibcdf/peptidemt/discussions/16) | [Record](amp_resource_cards.md#plum) | `family:amp`, `role:generation` |
| OmegAMP | AMP | [#17](https://github.com/uibcdf/peptidemt/discussions/17) | [Record](amp_resource_cards.md#omegamp) | `family:amp`, `role:generation` |
| ARCADIAMP | AMP | [#18](https://github.com/uibcdf/peptidemt/discussions/18) | [Record](amp_resource_cards.md#arcadiamp) | `family:amp`, `role:generation` |
| AMP-Designer | AMP | [#19](https://github.com/uibcdf/peptidemt/discussions/19) | [Record](amp_resource_cards.md#amp-designer) | `family:amp`, `role:generation` |
| PepDiffusion | AMP | [#20](https://github.com/uibcdf/peptidemt/discussions/20) | [Record](amp_resource_cards.md#pepdiffusion) | `family:amp`, `role:generation` |
| CPP_Design | CPP | [#21](https://github.com/uibcdf/peptidemt/discussions/21) | [Record](cpp_resource_survey.md#cpp_design) | `family:cpp`, `role:generation` |
| LightCPPgen | CPP | [#22](https://github.com/uibcdf/peptidemt/discussions/22) | [Record](cpp_resource_survey.md#lightcppgen) | `family:cpp`, `role:prediction`, `role:search` |
| MLCPP 2.0 | CPP | [#23](https://github.com/uibcdf/peptidemt/discussions/23) | [Record](cpp_resource_survey.md#mlcpp-20) | `family:cpp`, `role:prediction` |
| pLM4CPPs | CPP | [#24](https://github.com/uibcdf/peptidemt/discussions/24) | [Record](cpp_resource_survey.md#plm4cpps) | `family:cpp`, `role:prediction` |
| CPPpred-En | CPP | [#25](https://github.com/uibcdf/peptidemt/discussions/25) | [Record](cpp_resource_survey.md#cpppred-en) | `family:cpp`, `role:prediction` |
| ELP–EEP discovery | CPP | [#26](https://github.com/uibcdf/peptidemt/discussions/26) | [Record](cpp_resource_survey.md#elpeep-discovery) | `family:cpp`, `role:search` |
| CPPsite3: data resource | CPP / data | [#27](https://github.com/uibcdf/peptidemt/discussions/27) | [Record](cpp_resource_survey.md#cppsite3-data-resource) | `family:cpp` |

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
| CPP and cellular access | [Bounded resource survey](cpp_resource_survey.md), [functional definitions](functional_families.md) and [CPP project guides](cpp_guided_projects.md). Generator, classifier, uptake, escape and formulation-dependent delivery roles remain distinct; no CPP route is installed or qualified. |
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

The following English texts preserve the initial opening content. Published
indexes subsequently received the navigation additions recorded in the dated
receipts. Those receipts identify each exact state; these historical excerpts
are not a claim that the current index bodies are unchanged.

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
