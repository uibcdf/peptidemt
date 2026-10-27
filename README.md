# PeptideMT

[![MolSysSuite: Scientific Component](https://img.shields.io/badge/MolSysSuite-scientific%20component-0b7285?labelColor=24292f)](https://github.com/uibcdf/molsyssuite/blob/main/devguide/repository_badges.md#scientific-component)
[![MolSysSuite policy](https://github.com/uibcdf/peptidemt/actions/workflows/molsyssuite-policy.yml/badge.svg?branch=main)](https://github.com/uibcdf/peptidemt/actions/workflows/molsyssuite-policy.yml)
[![Python 3.11 | 3.12 | 3.13](https://img.shields.io/badge/Python-3.11%20%7C%203.12%20%7C%203.13-3776AB?logo=python&logoColor=white)](https://github.com/uibcdf/molsyssuite/blob/main/devguide/python_policy.md)
[![License](https://img.shields.io/github/license/uibcdf/peptidemt)](https://github.com/uibcdf/peptidemt/blob/main/LICENSE)

**Incubating MolSysSuite component; official bootstrap qualification in progress.**

PeptideMT is a computational peptide-design platform intended to generate,
redesign, evaluate and optimize peptide sequences by exploring regions of
sequence space conditioned on molecular targets, bioactive peptide families
and configurable constraints. This definition is provisional.

Target-directed design is a central motivation, but a protein target is not
required for every functional family or design task. De novo design and
redesign are equally within the intended scope. A computational campaign can
finish without experimental validation; predicted properties, experimental
evidence and demonstrated activity must remain distinguishable.

Start with the [design guide](devguide/README.md). The present repository contains
documentation, not an implemented scientific library or a fixed public API.
Macrel 1.6.1 is the approved first evaluator qualification candidate. No scientific
operation or provider is implemented or qualified by this bootstrap.

The accepted conceptual architecture separates scientific design intent,
computational plans and execution evidence. Functional families remain independent
of their models. See the [four worked cases](devguide/design_examples.md), including
target-free CPP + AMP design, and the [working methodology](devguide/design_methodology.md);
class names, APIs and storage representations remain open.

## Ecosystem and admission

PeptideMT is registered as a primary, incubating, actively developed scientific
Python component. Central admission is
[`8a94e16f`](https://github.com/uibcdf/molsyssuite/commit/8a94e16f1ba26122304df264e89c4eca15afaf5a),
under [MolSysSuite #146](https://github.com/uibcdf/molsyssuite/issues/146).
The official starter is integrated using `policy-v1.5.10` plus that separate
admission SHA. Component W0 receiving remains pending in
[PeptideMT #1](https://github.com/uibcdf/peptidemt/issues/1).

The source package currently exposes no scientific public API. Baseline import,
reporting, lint and installed-package checks establish engineering readiness only.
No package has been publicly distributed and no OS-support claim is made.
Required Python compatibility lanes cover 3.11–3.14, with 3.14 for routine work.
Routine development uses the shared `molsyssuite@uibcdf_3.14` environment.
Central registration of this development authorization and its fresh integration
receipt are tracked in the [W0 record](devguide/pending_proposals/complete_w0.md).
The badge above follows the frozen policy's public-admission inventory; the
executed source compatibility matrix separately covers Python 3.11–3.14.

## Development

Read [MOLSYSSUITE_GUIDE.md](MOLSYSSUITE_GUIDE.md) and [AGENTS.md](AGENTS.md).
Activate the shared Conda environment `molsyssuite@uibcdf_3.14`, then install
this clone with `python -m pip install --no-deps --no-build-isolation --editable .`.
The member's `devtools/conda-envs/development_env.yaml` and `test_env.yaml` remain
bootstrap/CI and clean qualification fixtures. They do not require a separate
daily environment. Read [PYTEST_RECEPTOR_GUIDE.md](PYTEST_RECEPTOR_GUIDE.md) and
[GH_RUN_RECEPTOR_GUIDE.md](GH_RUN_RECEPTOR_GUIDE.md) for reporting and Actions
evidence. Check interpreter/import origins and `python -m pip check`, retaining
any existing dependency findings explicitly, before running
`python -m pytest --receptor=llm`, `ruff check .`, `ruff format --check .` and
`python devtools/devguide_index.py --check`.

The full baseline suite runs for pushes/PRs on Linux/Python 3.14, and on every
supported minor through manual dispatch and the weekly matrix. The source-only
baseline has no meaningful scientific coverage report; no Codecov percentage,
model readiness or package-channel badge is claimed. Reassess coverage when W1
introduces scientific behavior. This is not a release or a public install route.

## Working agreement

The design guide is the source of truth for ongoing design discussions.
User-approved directions, pending proposals, research hypotheses, verified
observations and open questions have separate statuses. Recommendations do not
become accepted decisions automatically.

D36 authorizes the increment-1 W0–W4 work order under D35/M1–M8. W0 is in progress
in [MolSysSuite #146](https://github.com/uibcdf/molsyssuite/issues/146); W1–W4 start
only after genuine central admission and official staged bootstrap complete.
This is a specific admission-issue exception, not authority to open other
development issues or publish packages.
P07 is accepted conceptually: incomplete proposals, chemical realizations and
evaluated views retain explicit relationships and attribution. Hypothetical
realizations may supply missing information without rewriting original proposals.
Canonical identity, state grouping, identifiers, persistence, concrete interfaces
and initial chemistry support remain open. P08 also adopts an extensible
[functional concept catalog and qualified resources](devguide/functional_families.md#p08-conceptual-alternatives-and-generative-use),
including justified indirect guidance and distinct search/assessment roles.
The [strategy comparison](devguide/generative_strategies.md) explores reuse of
existing models. The current [capability/composition discussion](devguide/capabilities_and_composition.md)
records P09's conceptual closure under D21–D26: small optional, evidence-linked
capabilities and explicit compositions, with all seven principles accepted.
Concrete interfaces, schemas and implementation remain deferred.
The [bounded horizon review](devguide/future_horizons.md#9-bounded-extensibility-review-after-p09-approval)
examines libraries, target states and transformation products without new MVP
commitments. The current [P04 analysis](devguide/evaluation_and_selection.md)
records accepted alternative 2 and seven principles (D27–D28): evaluation,
feasibility, purpose-specific selection and bounded computational conclusions.
The X/Y selectivity case adopts distinct scientific requirements, operational
checks and explicit evidence links (D29), without universal thresholds or a
constraint engine. The [multiobjective analysis](devguide/multiobjective_optimization.md)
compares scalar, Pareto, hierarchical/constrained, uncertainty-aware and diversity
policies on invented X/Y/CPP/hemolysis candidates. D30 now accepts preserving
original objectives/evaluations and separating exploration, results/tradeoffs and
purpose-specific selection. No mandatory Pareto archive or universal fitness
follows. The operational extension compares continued generation, additional
computation and synthesis/experimental selection, with proposed obligations for
future components. No concrete optimizer or numerical policy is adopted.
D31 now accepts scoped restrictions, authorized provisional exploration,
uncheckable requirements and contextual fronts with seven qualifications. The
[bounded uncertainty/diversity/budget synthesis](devguide/uncertainty_diversity_budget.md)
records **C1–C5 accepted and P04 closed conceptually under D32**. Capability-specific
contracts/interfaces remain pending. D33 now accepts **B as the V0.1 direction**:
A external-proposal assessment is increment 1; real sequence generation/redesign
with functional evaluation and reproducible selection is the minimum useful
increment 2. Genuine feedback is a priority extension subject to viability; C
structural integration is deferred. The [bounded scope proposal](devguide/v0_1_scope.md)
reviews Macrel/HydrAMP/PepMLM feasibility, controls, contracts and acceptance cases.
Target-directed capability is an explicit priority after the first functional core.
D34 now accepts **AMP compatibility plus adverse hemolysis** as first coverage
and **Macrel then HydrAMP** as qualification candidates. The
[increment-1 specification](devguide/v0_1_increment_1.md) is now accepted under
**D35**, including strict sequence preservation, both selectors, M1–M8 and
provisional chemical/length scope. Its scientific design is closed, subject to
real qualification. The [commissioning brief](devguide/increment_1_work_order.md)
specifies operational prerequisites, official admission/starter work, test lanes
and required evidence. D36 now grants conditional implementation authorization;
builds/assets, actual environment/terms and completed admission remain to qualify.
H0–H4 stays a proposal outside this assignment.
The [expanded engine review](devguide/protein_peptide_design_engines.md)
examines general protein/peptide engines, Chaperone and RFD4, their evidence and
optional integration routes. No definitive generator, mandatory backend or API
is selected.

Documentation and commit messages use English, following the suite convention.
Scientific discussion with the investigators may continue in Spanish.

[MIT License](LICENSE).
