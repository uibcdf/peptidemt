(about-peptidemt)=
# About

PeptideMT is an incubating UIBCDF MolSysSuite component. It owns peptide-specific
scientific questions, occurrence attribution, assessment orchestration and
selection policy. MolSysMT owns general molecular-system operations and FASTA
interpretation; MolSysViewer owns visualization, and TopoMT owns topography.

The implemented increment evaluates external sequence proposals. Macrel is one
optional evaluator: its AMP/hemolysis predictions keep their native method and
domain limits. Predicted properties, experimental evidence and demonstrated
activity remain different kinds of evidence. See {ref}`evaluator-catalog`.

## Installing development sources

Routine development uses the suite's `molsyssuite@uibcdf_3.14` Conda profile and
editable component clones. With Conda supplying the dependencies, install this
checkout using:

```bash
python -m pip install --no-deps --no-build-isolation --editable .
```

Verify the interpreter, package import origin and dependency closure for the
environment you use. The shared profile has separately recorded pre-existing
dependency findings; the isolated qualification and CI environments have their
own clean-closure evidence. There is no claimed public PeptideMT package route.

Memory inputs and saved-result selection require neither Macrel nor MolSysMT.
FASTA ingestion selects the public source-preserving MolSysMT reader. The
qualified Macrel route additionally needs its exact provider/assets, MolSysMT
serialization and that route's Biopython capability. PeptideMT installs or
downloads none of these automatically. See {ref}`evaluator-macrel`.

## Citing actual work

For Macrel predictions, cite the original method {cite:p}`santos2020macrel` and
record the actual Macrel version, model hashes and execution environment.
PeptideMT's retained bibliography distinguishes the scientific criterion,
executed software and the modlAMP-derived reference implementation adapted inside
Macrel. It does not claim modlAMP was an executed dependency.

Record the PeptideMT and MolSysMT revisions actually used. PeptideMT has no
assigned release DOI in this delivery; do not invent one. Optional Ackredit
capture preserves detached bibliography and original producer versions.
Reading a saved result creates no new scientific credit.

```{bibliography}
```

For questions or actionable defects, use the
[owning repository](https://github.com/uibcdf/peptidemt). Scientific scope and
decisions remain in its maintained developer guide.
