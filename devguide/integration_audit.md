# Integration audit and evidence snapshot

Inspection: **2026-10-26**. Status: **bounded verified source observations**.
Navigation: [index](README.md) · [architecture](architecture_alternatives.md).

This preserves the preceding audit rather than replacing it with a generic
ecosystem description. Repository trees, manifests, selected implementations,
documentation and tests were inspected through GitHub. No libraries were
installed and no scientific tests or benchmarks were executed by this audit.

**Implemented** means corresponding code exists in the stated scope.
**Partial/experimental** identifies bounded or unstable coverage.
**Proposed** identifies a PeptideMT use, never an implemented integration.
Provider-reported release qualification was not independently replayed.
Code presence, source tests, installed compatibility and scientific validation
are separate evidence levels. The snapshots below are not a tested cohort.

## Eleven MolSysSuite repositories

### SMonitor

Implemented: structured diagnostics, catalogs, signals and support bundles.
Public exports include signal, emit and diagnostic_scope; no mandatory
dependencies in its manifest.
[Exports](https://github.com/uibcdf/smonitor/blob/ebdd0542156ed1dbe8df93141dbddbc74132a6f0/smonitor/__init__.py),
[integration recipe](https://github.com/uibcdf/smonitor/blob/ebdd0542156ed1dbe8df93141dbddbc74132a6f0/docs/content/user/library-integrators/first-runnable-integration.md).

Proposed: PeptideMT diagnostic catalog for unavailable engines, unsupported
chemistry and incomplete runs. Scientific scores/provenance stay result data.

### ArgDigest

Implemented: normalization/digestion and declarative function contracts.
FunctionContract and Domain describe admissible keywords, including domains
depending on other arguments.
[Implementation](https://github.com/uibcdf/argdigest/blob/cd9c4f3ab80e892075fc5bee9b4ae9ce0ab5e018/argdigest/core/function_contract.py),
[MolSysMT configuration](https://github.com/uibcdf/molsysmt/blob/e395e52646dab2ecb480d3d67aa7254be99b8524/molsysmt/_argdigest.py).

Proposed: objective/constraint consistency and backend-option validation.
The family vocabulary and scientific applicability remain PeptideMT-owned.

### DepDigest

Implemented: dep_digest, dependency configuration and DeclaredRegistry.
Enumeration, adapter inspection and execution are distinct. Inspecting an
adapter does not certify engine availability or scientific success.
[Contract](https://github.com/uibcdf/depdigest/blob/0884f0cc1dd60b79ed01930e68d80c87e51744c9/docs/content/user/declared-registry.md),
[tests inspected](https://github.com/uibcdf/depdigest/blob/0884f0cc1dd60b79ed01930e68d80c87e51744c9/tests/test_declared_registry.py).

Proposed: selectively load model adapters; retain execution guards and exact
provider requirements. An unavailable selected engine must not silently change.

### PyUnitWizard

Implemented: shared quantities, conversion and forms. Suite libraries declare
the shared policy only if the application has not selected one.
[Suite implementation](https://github.com/uibcdf/molsysmt/blob/e395e52646dab2ecb480d3d67aa7254be99b8524/molsysmt/_pyunitwizard.py).

Partial: QuantityRecord interchange is explicitly provisional.
[Codec](https://github.com/uibcdf/pyunitwizard/blob/9d74f0e1e911d78c1906948e74ce8da93935557d/pyunitwizard/record.py).
Proposed: concentrations, masses, distances and energies with meaning/units
retained. Pin provisional boundaries. A classifier score is not measured affinity.

### MolSysMT

Implemented molecular operations include get/select/convert/extract and adapters.
[Public exports/loading](https://github.com/uibcdf/molsysmt/blob/e395e52646dab2ecb480d3d67aa7254be99b8524/molsysmt/__init__.py).

Relevant concrete capabilities:

- [build_peptide](https://github.com/uibcdf/molsysmt/blob/e395e52646dab2ecb480d3d67aa7254be99b8524/molsysmt/build/build_peptide.py): native
  one-/three-letter construction and explicit LEaP; recognized terminal caps.
  [Regression tests](https://github.com/uibcdf/molsysmt/blob/e395e52646dab2ecb480d3d67aa7254be99b8524/tests/build/build_peptide/test_build_peptide_extended.py)
  cover standard residues, caps, geometry and sequence/SMILES ambiguity.
- [mutate](https://github.com/uibcdf/molsysmt/blob/e395e52646dab2ecb480d3d67aa7254be99b8524/molsysmt/build/mutate.py): native/PDBFixer
  reconstruction have different coverage. Native targets may retain missing
  heavy atoms with an explicit warning.
- [get_peptide_chemical_template](https://github.com/uibcdf/molsysmt/blob/e395e52646dab2ecb480d3d67aa7254be99b8524/molsysmt/physchem/get_peptide_chemical_template.py):
  explicit residue/terminal states and declared disulfides. The coordinate-free
  factory excludes capped/cyclic/modified backbones and arbitrary links, and
  explicitly leaves stereochemistry unspecified. It is not a universal
  modified-peptide or declared-L-chemistry builder.
- [ChemicalStates](https://github.com/uibcdf/molsysmt/blob/e395e52646dab2ecb480d3d67aa7254be99b8524/molsysmt/native/chemical_states.py):
  states share a stable atom-index domain. Changed atom inventories cannot
  automatically become alternative states on the same axis.
- [get_charge](https://github.com/uibcdf/molsysmt/blob/e395e52646dab2ecb480d3d67aa7254be99b8524/molsysmt/physchem/get_charge.py) and
  [get_hydrophobicity](https://github.com/uibcdf/molsysmt/blob/e395e52646dab2ecb480d3d67aa7254be99b8524/molsysmt/physchem/get_hydrophobicity.py):
  reuse named definitions. Tabulated residue charge and OpenMM-derived charge
  have different meanings; do not duplicate reference tables.

Partial/experimental: build_peptide, mutate, ChemicalStates, templates, interaction
objects and several map/interchange operations are experimental in the
[stability registry](https://github.com/uibcdf/molsysmt/blob/e395e52646dab2ecb480d3d67aa7254be99b8524/devguide/api_stability_registry.md).
A built structure does not certify a bound conformation, rotamer, complete
chemistry, force field or energy minimum.

Proposed: a small adapter using public operations, conversion reports and
sequence/group/atom/structure/state correspondence. PeptideMT owns design
intent and peptide-level specification, not another topology engine.
Generic chemical extensions should be agreed with MolSysMT.

### MolSysViewer

Implemented: Mol*-based viewer, new_view, scenes and AddonSpec/entry points
under molsysviewer.addons.
[Host contract](https://github.com/uibcdf/molsysviewer/blob/84b08909ad66593415f5c58716099375c191ac79/docs/content/developer/addons.md),
[factory](https://github.com/uibcdf/molsysviewer/blob/84b08909ad66593415f5c58716099375c191ac79/molsysviewer/new_view.py).

Proposed: optional molsysviewer_peptidemt inside the future toolkit distribution.
Scientific APIs remain headless/composable; removing display does not delete
scientific outputs. Partial: edit reconciliation has bounded retained-axis
source receiving, not arbitrary added-atom synchronization/installed compatibility.

### TopoMT

Implemented: [get_topography](https://github.com/uibcdf/topomt/blob/5f6239f0ee21fecca947f73790b139053c6aaa62/topomt/get_topography.py) dispatches
native/provider routes; [get_provider_output](https://github.com/uibcdf/topomt/blob/5f6239f0ee21fecca947f73790b139053c6aaa62/topomt/get_provider_output.py)
preserves original-provider results.
The [ADR](https://github.com/uibcdf/topomt/blob/5f6239f0ee21fecca947f73790b139053c6aaa62/devguide/third_party_architecture_adr.md) separates
method identity from library/CLI/server/files/local implementation.

Proposed: target-site topography and geometric context. Coverage and requirements
are method-specific. A pocket score is not peptide-binding evidence; a peptide
epitope need not resemble a small-molecule pocket.

### DockingMT

Implemented: DockingProblem/Protocol/Backend, poses/results, dock, dock_many,
fixed-pose score and audit.
[Exports](https://github.com/uibcdf/dockingmt/blob/e83963bf09a11edb3e4e84d87bdea09eac34cfb6/dockingmt/__init__.py),
[backend interface](https://github.com/uibcdf/dockingmt/blob/e83963bf09a11edb3e4e84d87bdea09eac34cfb6/dockingmt/engines/base.py).

Partial: concrete Vina capabilities cover rigid receptor, explicit flexible
ligand torsions, box search and Vina/Vinardo scoring. This is not a qualified
general peptide-docking solution. Preparation qualification remains provider-owned.

Verified limit: [_validate_vina_intent](https://github.com/uibcdf/dockingmt/blob/e83963bf09a11edb3e4e84d87bdea09eac34cfb6/dockingmt/core/protocol.py)
rejects nonempty constraints and search_guidance before execution. Passing
CPP/pharmacophore requirements there will not guide current Vina.

Proposed: consume normalized poses/scores, preserving preparation, maps and hashes.
Specialized peptide docking engines belong to DockingMT; candidate-design
decisions belong to PeptideMT. Docking scores are not calibrated affinity.

### PharmacophoreMT

Implemented: [dispatcher](https://github.com/uibcdf/pharmacophoremt/blob/8e83a64c829bd187bc929ca02d5b5117441a5302/pharmacophoremt/modeler/dispatcher.py)
and [ComplexBasedModeler](https://github.com/uibcdf/pharmacophoremt/blob/8e83a64c829bd187bc929ca02d5b5117441a5302/pharmacophoremt/modeler/complex_based.py)
consume ligand selection and named cached MolSysMT observations on the same
unchanged prepared source.
[Tests](https://github.com/uibcdf/pharmacophoremt/blob/8e83a64c829bd187bc929ca02d5b5117441a5302/tests/test_complex_based_facade.py) protect the
absence of implicit preparation/detection and preserve coordinates.

Proposed: reusable interaction hypotheses/evaluators. Pharmacophore-guided
generation additionally needs a compatible generator/optimizer. No universal
sequence-to-pharmacophore score is assumed.

### ElastNetMT

Implemented: [ElasticNetworkModel](https://github.com/uibcdf/elastnetmt/blob/f643829f9eca62fdc38678164a336f4ec1bc04dd/elastnetmt/model/elastic_network_model.py),
GNM/ANM and native matrix infrastructure.
[Physical tests](https://github.com/uibcdf/elastnetmt/blob/f643829f9eca62fdc38678164a336f4ec1bc04dd/tests/physical/test_spectral_contract.py)
cover spectrum/nullity validity and preserving state after failure.

Proposed: optional collective target-motion analysis/conformer-selection studies.
It is not a peptide folding, permeability or binding predictor. Value for short
flexible peptides and installed compatibility need separate evidence.

### MolSys-AI

Verified: umbrella, not a Python runtime package; its pyproject configures tools.
Server/Client/Agent live in separate internal repositories.
[README](https://github.com/uibcdf/molsys-ai/blob/a5bd037fddebef397e8bc84bf5591a6c859945bd/README.md),
[architecture](https://github.com/uibcdf/molsys-ai/blob/a5bd037fddebef397e8bc84bf5591a6c859945bd/devguide/ARCHITECTURE.md).

Proposed: consume typed PeptideMT operations later. It does not supply a ready
family predictor or binder generator. Target architecture is not runtime
integration evidence.

## Snapshot revisions

| Repository | Inspected commit |
| --- | --- |
| smonitor | [ebdd0542156ed1dbe8df93141dbddbc74132a6f0](https://github.com/uibcdf/smonitor/tree/ebdd0542156ed1dbe8df93141dbddbc74132a6f0) |
| argdigest | [cd9c4f3ab80e892075fc5bee9b4ae9ce0ab5e018](https://github.com/uibcdf/argdigest/tree/cd9c4f3ab80e892075fc5bee9b4ae9ce0ab5e018) |
| depdigest | [0884f0cc1dd60b79ed01930e68d80c87e51744c9](https://github.com/uibcdf/depdigest/tree/0884f0cc1dd60b79ed01930e68d80c87e51744c9) |
| pyunitwizard | [9d74f0e1e911d78c1906948e74ce8da93935557d](https://github.com/uibcdf/pyunitwizard/tree/9d74f0e1e911d78c1906948e74ce8da93935557d) |
| molsysmt | [e395e52646dab2ecb480d3d67aa7254be99b8524](https://github.com/uibcdf/molsysmt/tree/e395e52646dab2ecb480d3d67aa7254be99b8524) |
| molsysviewer | [84b08909ad66593415f5c58716099375c191ac79](https://github.com/uibcdf/molsysviewer/tree/84b08909ad66593415f5c58716099375c191ac79) |
| topomt | [5f6239f0ee21fecca947f73790b139053c6aaa62](https://github.com/uibcdf/topomt/tree/5f6239f0ee21fecca947f73790b139053c6aaa62) |
| dockingmt | [e83963bf09a11edb3e4e84d87bdea09eac34cfb6](https://github.com/uibcdf/dockingmt/tree/e83963bf09a11edb3e4e84d87bdea09eac34cfb6) |
| pharmacophoremt | [8e83a64c829bd187bc929ca02d5b5117441a5302](https://github.com/uibcdf/pharmacophoremt/tree/8e83a64c829bd187bc929ca02d5b5117441a5302) |
| elastnetmt | [f643829f9eca62fdc38678164a336f4ec1bc04dd](https://github.com/uibcdf/elastnetmt/tree/f643829f9eca62fdc38678164a336f4ec1bc04dd) |
| molsys-ai | [a5bd037fddebef397e8bc84bf5591a6c859945bd](https://github.com/uibcdf/molsys-ai/tree/a5bd037fddebef397e8bc84bf5591a6c859945bd) |
| moli | [d6c85a79b412cbdf58d867312d5ec5200160499b](https://github.com/uibcdf/moli/tree/d6c85a79b412cbdf58d867312d5ec5200160499b) |
| nextia | [32d12e20fae26f00a523d0ed4812e46def8a64e9](https://github.com/uibcdf/nextia/tree/32d12e20fae26f00a523d0ed4812e46def8a64e9) |
| praxis | [17e1856fa45a50b26097b19be28accb7ab88f689](https://github.com/uibcdf/praxis/tree/17e1856fa45a50b26097b19be28accb7ab88f689) |
| sabueso | [a9b1e637c57f330d4c4dee394c15d90fdbe69823](https://github.com/uibcdf/sabueso/tree/a9b1e637c57f330d4c4dee394c15d90fdbe69823) |
| recorda | [ff52fa5d8628d796f413b833c8abe73907990cf9](https://github.com/uibcdf/recorda/tree/ff52fa5d8628d796f413b833c8abe73907990cf9) |
| moli-agent | [08d0e2b809e7e5c46add5ee554ae9528831f7454](https://github.com/uibcdf/moli-agent/tree/08d0e2b809e7e5c46add5ee554ae9528831f7454) |

## Dependencies and conventions

The ten scientific/support Python manifests admit Python 3.11–3.14. SMonitor has
no required dependencies; DepDigest requires SMonitor; ArgDigest requires both.
PyUnitWizard requires those providers, NumPy and Pint. Optional reverse extras
do not by themselves establish a required runtime cycle.

MolSysMT and MolSysViewer require each other in package metadata. The
[central graph policy](https://github.com/uibcdf/molsyssuite/blob/14b2e74c4395e112a47cdcd51259767e7af7589d/devguide/dependency_graph_policy.md)
recognizes them as a coordinated publication unit. Making MolSysMT optional does
not remove its viewer dependency when installed.

TopoMT, DockingMT, PharmacophoreMT and ElastNetMT require MolSysMT.
PharmacophoreMT additionally requires RDKit/NGLView; ElastNetMT includes
scikit-learn/lindelint and native build infrastructure. A sequence core with
optional adapters is worth comparing, not an adopted package split.

Provider README publication limits were inspected. No live CI or full installed
cross-version matrix was independently qualified. The suite separates source,
installed artifacts and scientific claims.

## Six MolI repositories

| Owner | Implemented observation / limitation | Proposed relationship |
| --- | --- | --- |
| [MolI](https://github.com/uibcdf/moli/blob/d6c85a79b412cbdf58d867312d5ec5200160499b/README.md) | Architecture/governance and bounded receiving exercises; not a full project runtime. | PeptideMT remains within the MolSysSuite governance domain. |
| [Sabueso](https://github.com/uibcdf/sabueso/blob/a9b1e637c57f330d4c4dee394c15d90fdbe69823/devguide/ARCHITECTURE.md) | Cards, SourceAssertions, knowledge resolution/stores/packets exist; scientific coverage is bounded. | Optional pinned target/family/source knowledge. No CPP/AMP dataset coverage is assumed. |
| [Praxis](https://github.com/uibcdf/praxis/blob/17e1856fa45a50b26097b19be28accb7ab88f689/src/praxis/__init__.py) | Experimental catalog, applicability, sequential execution, audit and benchmarks. Source 0.1.1 is distinct from a public package route. | Reusable cross-tool methodology; PeptideMT retains native algorithm settings. |
| [Recorda](https://github.com/uibcdf/recorda/blob/ff52fa5d8628d796f413b833c8abe73907990cf9/src/recorda/__init__.py) | Experimental recording API 0.3.3, declared boundaries and references; public qualification is provider-reported. | Record calls while producer-owned results preserve scientific meaning. |
| [Nextia](https://github.com/uibcdf/nextia/blob/32d12e20fae26f00a523d0ed4812e46def8a64e9/devguide/INITIAL_SLICE.md) | Design/proposals; no scientific runtime package in the inspected tree. | Future project Questions/Evidence/Candidates/Decisions, without blocking initial computation. |
| [Moli agent](https://github.com/uibcdf/moli-agent/blob/08d0e2b809e7e5c46add5ee554ae9528831f7454/devguide/ARCHITECTURE.md) | Architecture/contracts; no agent implementation in the inspected tree. | Optional scientific reasoning, not mandatory execution or scientific authority. |

Additional verified seams:

- [SourceAssertion](https://github.com/uibcdf/sabueso/blob/a9b1e637c57f330d4c4dee394c15d90fdbe69823/sabueso/core/source_assertion_store.py)
  distinguishes database imports, human curation and rule/model extraction.
  [KnowledgePacket](https://github.com/uibcdf/sabueso/blob/a9b1e637c57f330d4c4dee394c15d90fdbe69823/sabueso/core/packets.py) composes pinned knowledge
  with conflicts and unknowns.
- [Praxis RecordaRecorder](https://github.com/uibcdf/praxis/blob/17e1856fa45a50b26097b19be28accb7ab88f689/src/praxis/recording.py) borrows an
  application-owned session.
- [Recorda activation tests](https://github.com/uibcdf/recorda/blob/ff52fa5d8628d796f413b833c8abe73907990cf9/tests/test_activation.py) preserve native
  return identity and session ownership. Activation does not observe arbitrary
  calls or implement distributed replay.
- [MolI receiving example](https://github.com/uibcdf/moli/blob/d6c85a79b412cbdf58d867312d5ec5200160499b/examples/sabueso_recorda/README.md) records
  consumption of preserved Sabueso artifacts, explicitly excluding full
  ProjectContext/EventLedger/general exchange semantics.
- [Learning loop](https://github.com/uibcdf/moli/blob/d6c85a79b412cbdf58d867312d5ec5200160499b/architecture_1.0/LEARNING_LOOP.md) requires explicit
  promotion of project experience into knowledge or methods.

A peptide candidate as a domain result differs from its contextual role in a
Nextia project. Result, SourceAssertion, Observation, Evidence and recording
event remain distinct. The central September infrastructure census is historical
and must not override subsequently implemented Praxis/Recorda source.

## Ownership conclusion

Keep peptide specification, family/model associations, generation/search,
objectives, constraints and selection in PeptideMT. Reuse molecular chemistry
from MolSysMT, docking from DockingMT, topography from TopoMT, pharmacophores
from PharmacophoreMT, networks from ElastNetMT and presentation from MolSysViewer.
Reusable methodology, recording and project meaning remain with Praxis, Recorda
and Nextia. These are recommendations; no adapter or dependency is implemented.
