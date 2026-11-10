(peptidemt-home)=
# PeptideMT

PeptideMT develops peptide-specific assessment and selection workflows in
MolSysSuite. The implemented first increment accepts sequence proposals,
preserves their provenance, evaluates compatible views with an optional qualified
Macrel resource and applies two reproducible computational ordering policies.

Macrel 1.6.1 is accepted for this bounded exploratory role under D37. Other
evaluators can later contribute their own scoped evidence; their scores are not
automatically interchangeable. The provisional HydrAMP data boundary receives
and replays existing generation evidence without a model. The separate provisional
generation execution adapter has controlled installed tests and one accepted
real-checkpoint case under D41. The provisional analogue receiving/isolated
redesign boundary now has artificial R1/R2 qualification; its real consumer R3
case remains pending. Target-conditioned capabilities remain future work.

::::{grid} 1 2 2 3
:gutter: 3

:::{grid-item-card} Getting started
:link: user-quickstart
:link-type: ref
Prepare proposals and select from saved results without running a model.
:::

:::{grid-item-card} Macrel
:link: evaluator-macrel
:link-type: ref
Understand the accepted resource, inputs, outputs and operational limits.
:::

:::{grid-item-card} Qualification evidence
:link: macrel-qualification
:link-type: ref
Read what was tested and what remains biologically unestablished.
:::

:::{grid-item-card} HydrAMP results
:link: hydramp-results
:link-type: ref
Preserve generated proposals and compose them with separate assessment.
:::

::::

This is provisional development documentation. No public package release or
hosted documentation deployment is implied. Start with the implemented workflow;
the larger scientific direction remains documented in the repository design guide.

```{toctree}
:maxdepth: 2
:hidden:

content/about/index
content/user/index
content/showcase/index
api/index
content/developer/index
```
