# Full HydrAMP modernization: own-use direction and proposed stages

Status: **investigator-stated evolution objective; module work orders proposed**,
2026-11-03. Provider planning: [HydrAMP #4](https://github.com/uibcdf/hydramp/issues/4).
Consumer: [PeptideMT #32](https://github.com/uibcdf/peptidemt/issues/32).

Progress, 2026-11-04: separate dev4 now implements the deterministic encoder and
passes its [finite real-weight E2 comparison](hydramp_encoder_E2.md); its allowance
is exhausted and D41/dev3 remains the accepted generation resource. The next
[analogue contract](hydramp_analogue_work_order.md) is prepared for review under
#4. A1 artificial implementation was subsequently authorized under D43 and is
now delivered as [installed artificial dev5](hydramp_analogue_A1.md) after the
audit; real analogue qualification remains unapproved.
The source-inventory table below retains its earlier dated starting point.

## Direction and collaboration timing

The investigator steers the work toward our own needs and explicitly emphasizes
modernizing HydrAMP's complete original functional scope rather than stopping
at the current partial inference port. A faithful, validated and maintainable
modernization could strengthen a later collaboration proposal. Author interest
remains unknown, and breadth without evidence is not a collaboration guarantee.

**Do not contact original authors now.** Possible contact belongs at the end,
after substantial modernization/validation and internal review, and still needs
explicit permission for its recipient, channel and content. Existing
[HydrAMP #6](https://github.com/uibcdf/hydramp/issues/6) retains that deferred item.
Contact or an upstream response is not a prerequisite for planning our own work.

This is direction for a staged programme, not an implicit commission to implement
every module, train models, load new artifacts or run experiments immediately.
[D41](hydramp_dev3_acceptance.md), exact accepted dev3, D35/M1–M8 and existing
execution limits are unchanged. Each new scientific capability needs its own
concrete readiness/work order before implementation and finite host/call approval
before real execution. No new accepted D-number or architecture is assigned here.

## Proposed meaning of complete modernization

Cover HydrAMP's original scientific functions and the software needed to use,
train and evaluate them on a modern stack. Preserve original definitions and
reference evidence; improve usability without silently changing the method.
Do not equate completeness with copying every old notebook or implementing all
comparison models that happen to be present in the repository. Classify those
ancillary materials during the inventory rather than silently expanding scope.

The following inventory is based on source inspection of original
`6590d2f4c2963f25d30669052a4c4a857e0e7279` and the exact modern dev3. It is not
an executed qualification of the missing modules.

| Area | Existing evidence / missing scope | Proposed treatment |
| --- | --- | --- |
| Decoder and native AMP/MIC heads | Modern CPU inference exists, with D41's finite evidence and retained numerical/rank FAILs. Heads score original tokens; a complete independent sequence-prediction workflow is not delivered. | Keep accepted core frozen. Inventory original prediction/preprocessing paths and define any new supported sequence-facing operation before porting it. |
| Remaining de novo behavior | The modern accepted route is unfiltered AMP, one attempt, explicit seed, softmax and properties. Original code also exposes non-AMP mode, filtered/refill behavior and stochastic decoding choices. | List and prioritize original modes separately. Native filtering/count/attempt/order semantics are scientific behavior, not packaging defaults. No new filter is added to PeptideMT's current route. |
| Encoder and latent posterior | Original encoder and posterior scale path exist; modern loader/core deliberately excludes them. | Candidate first new scientific module: reproduce original representations and posterior parameters with declared inputs and synthetic checks before pretrained qualification. |
| Analogue/redesign generation | Original path uses encoder, posterior-derived noise/temperature, both original heads and prototype-relative filtering. No modern analogue route is accepted. | Follow encoder with a separate analogue work order covering randomness, prototype/occurrence mapping, duplicates, no-hit results, scoring and descriptors. |
| Filters and original selection | Source inspection reveals apparent mask/dispatch defects in original optional filters. | Track in [HydrAMP #7](https://github.com/uibcdf/hydramp/issues/7). Establish intended/observed behavior with artificial controls, then seek explicit compatibility-versus-correction disposition. Preserve original reference and current unfiltered resource. |
| Training of classifiers and generative model | Original notebooks, master trainer, data generators, losses and Gumbel/gradient paths exist. Modern inference uses frozen buffers/eval mode and rejects training. | A substantial separate phase, not switching `.train()` on the inference port. Inventory data, objectives, gradients, optimization, checkpoint/resume and evaluation before a trainable design or training resource plan. |
| Evaluation and reproducible experiments | Original notebooks/scripts and retained comparison evidence are available; a modern independent evaluation workflow is incomplete. | Reuse accepted evidence, classify useful original analyses, review datasets/assay meanings and overlap, and specify prospective comparisons under #3. Do not rerun until the actual question and budget are approved. |
| Data/configuration and deployment | Exact local inference profile and internal documentation exist. Generic acquisition, modern full-workflow CI, independent portable results and release delivery remain incomplete. | Support the chosen modules incrementally. Reuse owning tools for molecular files/operations and applicable record/attribution infrastructure. Avoid building an unrelated platform inside HydrAMP. |

## Suggested order and acceptance boundaries

1. Complete the capability/dependency matrix and select a bounded first module.
   The encoder is a useful first candidate because it enables original redesign;
   its own scientific inputs/outputs and comparison criteria must be agreed first.
2. Qualify encoder inference, then the original analogue/redesign route as a
   distinct increment. Resolve optional-filter semantics explicitly, preserving
   original behavior as evidence rather than silently propagating or fixing bugs.
3. Complete the other original inference workflows that our actual use requires,
   with each supported mode and its limitations recorded independently.
4. Design trainable modules and a reproducible training/evaluation pipeline as
   a separate scientific phase. The inference port and its memory observations
   do not establish training correctness or a suitable training resource budget.
5. Consolidate full user documentation, regression/CI, installation and artifact
   delivery against the chosen completeness matrix. Only then prepare a possible
   author-facing handoff for internal review; no automatic contact follows.

This order is a proposal to discuss, not a promise that every original feature
will be ported unchanged or a commission to start training. Use separate candidate
artifacts for later modules, preserve accepted dev3 and all original SHA/environment
evidence, and do not overwrite the existing acceptance identity.

## Scientific fidelity and ownership

Retain weights/equations/score meanings when modernizing the original method.
Keep demonstrated modern numerical improvements and genuine original pointwise
advantages explicit. A corrected original filter, new preprocessing, stochastic
sampling rule, training objective or new acceptance criterion requires a recorded
scientific choice; it cannot be hidden as routine modernization.

HydrAMP owns its model-specific encoding and scientific methods. Molecular-system
reading/manipulation remains MolSysMT-owned; reuse supported FASTA/file operations
instead of transplanting a local molecular parser. Review Recorda/Ackredit and
other applicable provider boundaries before general record or attribution work.
PeptideMT remains the orchestrator and selection-policy owner, not the model's
training implementation. New standalone conveniences must follow actual module
needs, rather than dictate a new scientific architecture in advance.

Other-family prediction/generation or a new learned successor remains the separate
feasibility question in #5. Faithfully modernizing the original and inventing a
new method have different evidence and identity. This programme creates no
automatic new-family capability, training permission, GPU allowance, package/model
publication or outreach authority.

## Inspection limits

The current step reads original source only. It does not import a scientific
framework, load parameters/PCA, compute descriptors, generate sequences, execute
filters, train or download data. Filter observations are source-level findings
pending focused validation in our fork. No original-author repository is modified.
