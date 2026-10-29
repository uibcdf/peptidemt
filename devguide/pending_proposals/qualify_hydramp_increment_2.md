---
summary: Review the bounded HydrAMP route and commissioning gates for real generation.
issue: uibcdf/peptidemt#8
status: open
opened: 2026-10-29
closed:
verification: inspected
area: [generation, qualification, integration]
guard:
normative:
blocked_by: []
supersedes: []
---

# Increment 2 readiness: bounded HydrAMP qualification

Status: **proposal for investigator review**, 2026-10-29. This record prepares
the next commission; it is not acceptance of HydrAMP or execution permission.
The investigator requested continuing after D37 and completed increment-1
delivery at `b872f32965f50ccec64c46659176ca8c8acf727c`.

## What and why

D33 requires real learned generation/redesign plus assessment/selection for the
minimum useful V0.1. D34 names HydrAMP as the first generator candidate after
Macrel. Propose qualifying **one native de novo route**, using the existing
[H0–H4 plan](../v0_1_increment_1.md#62-qualification-gates-with-a-small-execution-budget).
No general architecture, new family ontology, feedback optimizer or second
generator interface is needed to answer whether that route works.

Increment 1 is completed under D35/D36 and accepted under D37. Its
[acceptance receipt](../evidence/increment_1_acceptance.json), M1–M8, molecular
contracts, exact native evidence and both selectors remain unchanged. Generation
must add actual proposals, not import a fixed pool and call it learned generation.

## Read-only findings

Official branch identities were checked through GitHub on 2026-10-29 and match
the previous inspected pins:

| Source | Immutable identity and inspected inputs |
| --- | --- |
| HydrAMP 1.2.0 source | `szczurek-lab/hydramp@6590d2f4c2963f25d30669052a4c4a857e0e7279`; [native generator](https://github.com/szczurek-lab/hydramp/blob/6590d2f4c2963f25d30669052a4c4a857e0e7279/amp/inference/inference.py), [package requirements](https://github.com/szczurek-lab/hydramp/blob/6590d2f4c2963f25d30669052a4c4a857e0e7279/setup.py) |
| Official starter, asset/environment reference | `szczurek-lab/hydramp-starter-kit@7804df862872ccc6d09fe01c41bafbca194cfa31`; [manifest](https://github.com/szczurek-lab/hydramp-starter-kit/blob/7804df862872ccc6d09fe01c41bafbca194cfa31/pyproject.toml), [provenance](https://github.com/szczurek-lab/hydramp-starter-kit/blob/7804df862872ccc6d09fe01c41bafbca194cfa31/README.md#model--data-provenance), [model configuration](https://github.com/szczurek-lab/hydramp-starter-kit/blob/7804df862872ccc6d09fe01c41bafbca194cfa31/checkpoint/model/model_config.json) |

The starter declares Python >=3.8,<3.9, TensorFlow 2.2.1, Keras 2.3.1 and an
older numerical stack. It overrides HydrAMP's dependency metadata and modlAMP's
database requirement. These are explicit upstream deployment choices, **not a
tested dependency solution for PeptideMT**. A plain install and the starter's
custom resolution route are different candidates; any required override needs
an explained, reproducible dependency contract before qualification.

The starter identifies an epoch-37 model and a PCA decomposer. Git tree metadata
lists 60 checkpoint files totaling 3,718,445 bytes, including layer/configuration
files. That is an inventory size, not a download, SHA256 receipt, complete runtime
size or RAM estimate. Model/data provenance still needs artifact-specific review;
public access and an MIT code license alone do not settle every intended use or
redistribution right. No numerical weights or PCA blob were downloaded or
deserialized here.

## Proposed scientific boundary

Use the native softmax constructor and `unconstrained_generation` with
`mode='amp'`, `filter_out=False`, `n_attempts=1`, `properties=True`, an explicit
seed and bounded positive `n_target`. The inspected branch breaks after its
batch rather than refilling a quota. Preserve its native return order, duplicates,
AMP/MIC scores and descriptors. Internal conditioning/scoring and token argmax
remain part of the method; this is not an unconditional or decision-free sampler.

Retain these distinct layers: HydrAMP conditioning and native scores; generated
sequence occurrences and their provenance; separate Macrel assessment of
compatible unchanged strings; and either existing PeptideMT selector. Native
`mic` is not a concentration, and native `amp` is not Macrel's `AMP_probability`.
Agreement is not independent biological validation. The original decoder token
layout may differ from the returned string's re-encoding; preserve that unknown
instead of asserting unobserved token-level equivalence.

Account for every returned occurrence and any requested/returned-count mismatch.
Keep empty/malformed/noncanonical/unexpected-length output and incomplete runs
explicit; do not silently repair, deduplicate, refill or assign a failed view's
score to a different molecule. Macrel's leading-M/chemistry rules remain in force.
No inferred termini, stereochemistry or crosslinks are added to generated strings.

## Proposed commissioning sequence

| Stage | Reviewable result and stopping condition |
| --- | --- |
| H0: artifact/use preflight | Exact source, checkpoint/PCA inventory and byte digests, applicable terms and permitted local use. Unresolved necessary rights stop acquisition/use; redistribution is not requested. |
| H1: isolated deployment | One reproducible Linux CPU legacy worker, installation/import origins and truthful dependency closure. Preserve the Python 3.14 suite host and shared environments. No silent TensorFlow modernization or copying the generator. Source inspection and solver success cannot establish model-load success. |
| H2: bounded native calls | Retain the proposed four calls/52 requested outputs from H0–H4. An allocation is direct smoke n=4, direct n=16/seed A, adapter n=16/seed A, adapter n=16/seed B. The repeated seed supplies parity/repeatability evidence within four total generation calls, not four direct plus four adapter calls. No retry/refill. |
| H3: fidelity/repeatability | Compare actual returned sequences/order/scores/descriptors for the direct/adapter repeated case and preserve any variation. A seed alone is no promise of bitwise repeatability. Usable real output is required; controlled stand-ins cover failures only. |
| H4: end-to-end assessment | Preserve all generated proposals, assess compatible strings with the qualified Macrel route, and apply both unchanged selectors. Compare the same pool before/after selection and a declared small procedural control. Freeze the control and its budget before execution; it is not a replacement generator or an efficacy benchmark. |

Before model loading or generation, inspect the actual shared host and agree the
worker's CPU/thread, wall-time, RAM/address-space, disk and child-process limits.
Use no GPU at this stage. The previous Macrel allowance is exhausted: H4 requires
its **own fresh call/input/resource budget**, including the control and any parity
calls. Do not invent that budget from the 52 requested HydrAMP outputs. Insufficient
resources or an unmaintainable runtime return this candidate for reconsideration.

Reuse MolSysMT for molecular/FASTA operations; keep peptide-specific orchestration
in PeptideMT under the canonical component map. Preserve DepDigest, SMonitor and
Ackredit boundaries. The MolSys-AI umbrella concerns suite understanding/operation;
its presence is not a reason to relocate this peptide generator there. Propose any
missing independently reusable sibling operation to its owner before duplication.

## Scope, exclusions and acceptance of this proposal

This issue closes when investigators accept, narrow or decline the concrete next
commission and the decision is recorded with explicit execution prerequisites.
No new accepted decision is inferred from preparing this record. If approved,
implementation/evidence needs a linked owning work record and actual H0–H4
results before scientific acceptance; unresolved stages remain partial.

Analogue generation, feedback, protein-target conditioning, altered chemistry,
new selection rules, training, package/model redistribution and publication are
outside this proposed commission. Preserve original W3 artifacts while useful;
[retained-resource review #7](https://github.com/uibcdf/peptidemt/issues/7) has its
own owner and disposition. The new documentation-tooling inventory handoff
[MolSysSuite #156](https://github.com/uibcdf/molsyssuite/issues/156) stays separate
from completed #151/#152 receiving.

## What was refuted

- Acceptance of Macrel is not acceptance of a generator, a new inference budget
  or a complete generative V0.1.
- A visible starter checkpoint or historical Python 3.8 recipe is not a qualified
  installed runtime, trusted deserialization receipt or distribution permission.
- The starter's quota-filling challenge workflow is not required by this proposal.
- Native scores, external assessment and downstream filtering do not demonstrate
  functional feedback or measured antimicrobial activity/safety.
