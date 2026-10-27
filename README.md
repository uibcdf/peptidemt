# PeptideMT

**Experimental scientific and architectural design workspace.**

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
No generator, predictor, molecular representation or first demonstrator has
been selected.

The accepted conceptual architecture separates scientific design intent,
computational plans and execution evidence. Functional families remain independent
of their models. See the [four worked cases](devguide/design_examples.md), including
target-free CPP + AMP design, and the [working methodology](devguide/design_methodology.md);
class names, APIs and storage representations remain open.

## Ecosystem and admission

PeptideMT is intended to evolve into a MolSysSuite scientific component.
Formal registration in the central `suite.toml`, Python-component generation,
policy workflow adoption and installation qualification are **pending**.
Creating this design repository does not establish suite admission.

The [official starter route](https://github.com/uibcdf/molsyssuite/blob/14b2e74c4395e112a47cdcd51259767e7af7589d/devguide/new_component_starter_kit.md)
requires admission before generating a Python package. This documentation-only
workspace deliberately makes no package, platform-support or release claim.
Its eventual implementation must use that route rather than treating this
minimal workspace as an already qualified component.

## Working agreement

The design guide is the source of truth for ongoing design discussions.
User-approved directions, pending proposals, research hypotheses, verified
observations and open questions have separate statuses. Recommendations do not
become accepted decisions automatically.

The current scope authorizes documentation and repository setup only. Scientific
implementation and development issues require a subsequent agreement.
P07 is accepted conceptually: incomplete proposals, chemical realizations and
evaluated views retain explicit relationships and attribution. Hypothetical
realizations may supply missing information without rewriting original proposals.
Canonical identity, state grouping, identifiers, persistence, concrete interfaces
and initial chemistry support remain open. P08 also adopts an extensible
[functional concept catalog and qualified resources](devguide/functional_families.md#p08-conceptual-alternatives-and-generative-use),
including justified indirect guidance and distinct search/assessment roles.
The [strategy comparison](devguide/generative_strategies.md) explores reuse of
existing models. The current [capability/composition discussion](devguide/capabilities_and_composition.md)
examines provider operations, strategy requirements, plan choices and actual
execution; these proposed principles do not select a definitive generator or API.

Documentation and commit messages use English, following the suite convention.
Scientific discussion with the investigators may continue in Spanish.

[MIT License](LICENSE).
