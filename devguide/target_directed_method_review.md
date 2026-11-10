# Target-directed demonstrator: bounded evaluation-method review

Status: **read-only feasibility analysis and recommendations**, 2026-11-06.
Current disposition, 2026-11-10: the T1a review holds in this dated analysis
are historical; [D53 receiving is complete](mdm2_t1a_qualification.md).
The next [T1b proposal](mdm2_t1b_proposal.md) remains unaccepted. No docking or
affinity method has been selected or executed by this preparation.
The investigator's subsequent [broader alternatives discussion](peptide_protein_binding_survey_2026_11_10.md)
now compares binder generators and modern complex prediction alongside classical
docking; the earlier HADDOCK3-first recommendation is not a selected protocol.
Owner: [PeptideMT #33](https://github.com/uibcdf/peptidemt/issues/33), under
[D52 preparation](target_directed_demonstrator.md).
Inputs: [experimental/provider review](target_directed_evidence_review.md).
The [T1a proposal](mdm2_t1a_proposal.md) remains unchanged and awaits investigator
review. This analysis selects or executes no model and adds no implementation
commission. [Source receipt](evidence/target_directed_method_review.json).

## Scientific recommendation

Separate three questions before selecting a tool: can it model an appropriate
pose, can its scores order the admitted experimental affinities, and does using
those scores improve the selected candidates against the references? Evidence
for one question does not answer the next. The [T0 controls](mdm2_t0_qualification.md)
answer none of the latter two questions.

For the future owner-led peptide-docking feasibility review, **HADDOCK3 is a
reasonable first candidate to discuss with DockingMT**, because its current
source declares the routine Python version and includes an explicit peptide
workflow. This is a technical-preparation recommendation, not an accepted
MDM2 affinity evaluator. FlexPepBind is a useful methodological reference for
the separate binding-specificity question. ADCP remains a candidate, with source,
distribution, chemistry and license alignment unresolved. No method currently
has demonstrated superiority or qualified MDM2 affinity ranking in PeptideMT.

Avoid starting another modernization project before establishing whether an
existing qualified route answers the scientific question. A CLI can be an
isolated provider route without requiring its entire engine to become a Python
3.14 library. Such isolation would still need exact bundle/use, data-preservation,
failure and resource qualification; it is not permission to run a candidate.

## HADDOCK3: modern technical candidate, distinct scientific evidence

The inspected source at
[`62bef1fc2d9fc99b350f252be1389a6ca3d17f2d`](https://github.com/haddocking/haddock3/tree/62bef1fc2d9fc99b350f252be1389a6ca3d17f2d)
declares Python `>=3.10,<3.15`, including a Python 3.14 classifier. Its
[`examples/docking-protein-peptide`](https://github.com/haddocking/haddock3/tree/62bef1fc2d9fc99b350f252be1389a6ca3d17f2d/examples/docking-protein-peptide)
contains separate full and test configurations over 1NX1. The test configuration
requests ten cores, so it is not a suitable shared-host configuration to copy.
These are inspected declarations/examples, not our installed or executed evidence.

The [current peptide guide](https://www.bonvinlab.org/haddock3-user-manual/bpg/peptides.html)
recommends peptide conformational ensembles and links an
[MDM2–p53 tutorial](https://www.bonvinlab.org/education/molmod/docking/).
That tutorial concerns a mouse MDM2 homology model and the historical web-server
workflow. It does not qualify HADDOCK3, a human experimental construct or peptide
affinity ranking. Its interface restraints are information used in docking,
not independent validation of the resulting interaction.

The Python project declares Apache 2.0. Its
[`DISCLAIMER.md`](https://github.com/haddocking/haddock3/blob/62bef1fc2d9fc99b350f252be1389a6ca3d17f2d/DISCLAIMER.md)
and [installation guide](https://www.bonvinlab.org/haddock3-user-manual/download-haddock3.html)
identify separately governed CNS components, including non-profit/commercial-use
conditions. The installation route can acquire a CNS executable. No complete
bundle-license, binary-platform or dependency-closure qualification is claimed.
No package or executable is installed in this review.

Before adoption, DockingMT would own the supported workflow/adapter and define
which receptor/peptide representation, terminal/state treatment, restraints,
conformations, scoring and output mappings are actually supported. Molecular
preparation and output interpretation must use MolSysMT's public tools; the
historical tutorial's editing/concatenation instructions are not a reason to add
those operations to PeptideMT.

## Rosetta FlexPepDock and FlexPepBind: related, different questions

The [official FlexPepDock documentation](https://docs.rosettacommons.org/docs/latest/application_documentation/docking/flex-pep-dock)
distinguishes refinement, near-site ab-initio docking, rescoring and minimization.
Refinement assumes a suitable starting complex; neither refinement nor its
near-site ab-initio mode is fully blind docking. Documentation benchmarks and
scores concern structural modelling; they do not establish a universal conversion
to experimental Kd. The documented sampling can be expensive: do not treat a
small demonstration run as qualification of the full scientific protocol.

FlexPepBind's [original FTase study](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1002170)
adapts structural constraints and scoring to a particular specificity problem
and tests experimental outcomes. This provides a useful validation pattern,
not an already validated MDM2 model. Any target-specific fitting here would need
independent evaluation data and an explicit scientific commission.

The current Rosetta source at
[`eddc15bbac60cf91302d3faf76895bd6d215cc50`](https://github.com/RosettaCommons/rosetta/tree/eddc15bbac60cf91302d3faf76895bd6d215cc50)
has a [non-commercial license agreement](https://github.com/RosettaCommons/rosetta/blob/eddc15bbac60cf91302d3faf76895bd6d215cc50/LICENSE.md);
PyRosetta has a separate agreement. Source visibility does not establish
unrestricted redistribution. No Rosetta/PyRosetta environment, binary or
protocol compatibility is qualified here. A future docking route belongs in
DockingMT rather than a local PeptideMT wrapper.

## ADCP: version and representation must match the actual candidate

The [official overview](https://sannerlab.github.io/software/adcp/index.html)
lists 1.1 as current and 1.0 as deprecated. The
[1.1 manual](https://sannerlab.github.io/software/adcp/1.1/documentation.html)
inherits the FAQ's uncapped docking representation. Its optional OpenMM
reranking documents replacement of unsupported nonstandard residues by standard
residues or alanine. Those transformations could change the evaluated entity;
adding caps afterwards does not establish that the docking score evaluated the
original capped molecule. No such approximation is accepted for PeptideMT.

The source linked from that site is inspected at
[`1768a5414dcb3069ee306302145a1d371427f02e`](https://github.com/sannerlab/ADCP/tree/1768a5414dcb3069ee306302145a1d371427f02e).
Its `runADCP.py` contains Python 2 print syntax and the Python 3.14 AST inspection
stops at line 149. This is source inspection, **not an execution failure of a
qualified 1.1 distribution**, and does not prove that every ADCP route fails on
Python 3.14. Its launcher defaults to detected CPU count unless limited.

There is also an unresolved source/distribution licensing correspondence:
the site's current license description, the pinned repository's BSD-2-Clause
root file and the launcher's LGPL header are different records. The exact
acquired engine, launcher, data and dependencies would need their actual terms
and correspondence checked before adoption. No license conclusion is inferred
from a GitHub classifier or an older article. No external issue or author
contact is made; the finding remains in this authorized internal review.

The first inspection script incorrectly assumed every Python file could be
parsed by Python 3.14; its failure is retained. The corrected inventory records
the refusal without changing upstream code. No local ADCP port, residue fallback
or native-model execution follows.

## Reuse for future peptide variants

MolSysMT already provides
[`build.mutate`](https://github.com/uibcdf/molsysmt/blob/ed09f64539a5af6c1dbe9bd352c7ef65dcd4a7a6/molsysmt/build/mutate.py).
Its native route has bounded heavy-atom reconstruction and can return an
incomplete target with a warning. Its explicit PDBFixer route can perform
whole-system repair/H addition and round retained coordinates through PDB text.
A requested mutation name therefore does not certify a complete, faithful or
energetically qualified molecular state. A future proposal policy belongs in
PeptideMT; the actual molecular substitution and its mapping belong in MolSysMT.
No substitution, repair or sequence proposal is executed in this review.

## Requirements for the later comparison

These are recommendations for the next scientific review, not accepted new
endpoints, selectors or algorithms:

1. Choose whether the immediate evaluation concerns pose quality or relative
   affinity. Bind the declared human construct, peptide chemistry, measurement,
   reference preparation and admissible transformations before execution.
2. For affinity ordering, consider equal-length, within-series comparisons
   first, retaining all other source records and their disposition. Pooling
   peptide lengths or parent series can give an easy association that fails
   to help choose a better variant within a series.
3. Use an existing crystallographic binding site only as declared input
   information. A result conditioned on a known holo structure is not blind
   recognition or a demonstration on an unbound target. Do not derive restraints
   from the same held-out affinity/mutation labels being used to evaluate it.
4. Distinguish empirical energy, internal strain, interaction score and any
   calibrated affinity estimate. Keep original units and score direction;
   do not relabel an engine score as measured Kd or a probability of binding.
5. Compare against retaining the parent and simple selection references under
   a fixed candidate/selection budget, with predeclared ties and missing-score
   behavior. A useful ranking statistic alone does not show improvement over
   the parent. Use a supported statistics provider for general calculations.
6. Preserve all failures and search budgets. Different sampling effort or
   taking the best of more attempts can change score minima. Stability across
   a declared finite seed/conformation set is separate from experimental accuracy.
7. Keep prior source-result exposure explicit. Decide the independence question
   for training, method selection, calibration and final evaluation separately.
   The already read pilot is exploratory; more docking does not make it blind.
8. Report a null or adverse result without optimizing until it becomes positive.
   New-candidate predictions remain hypotheses; affinity improvement does not
   establish uptake, selectivity, adverse-property control or cellular efficacy.

These requirements preserve the full design/selection objective. T1a evidence
curation, a pose pilot and an affinity-ranking study are dependencies with
different claims; none alone completes the demonstrator.

## Current disposition

One check of the existing provider threads found the previously posted consumer
comments and no later substantive owner response. No running job or promised
owner delivery is inferred from that observation. The existing handoffs in
[MolSysMT #447](https://github.com/uibcdf/molsysmt/issues/447#issuecomment-6679876257)
and [DockingMT #33](https://github.com/uibcdf/dockingmt/issues/33#issuecomment-6679884695)
remain sufficient for this unselected-method preparation; no duplicate issue or
additional external publication is made.

The next implementation decision remains the already submitted T1a scientific
contract. This review adds evidence for the subsequent method choice while
leaving that proposal's exact bytes and accepted T0/AMP results unchanged.
