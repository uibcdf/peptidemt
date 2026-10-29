(developer-guide)=
# Developer guide

The repository's
[developer guide](https://github.com/uibcdf/peptidemt/tree/main/devguide) owns
scientific design, decisions and evidence. User documentation describes the
implemented API and accepted scope. D37 records the investigator's Macrel
acceptance; D35/D36 and M1–M8 retain their approved meanings.

## Working locally

Read root `AGENTS.md`, `MOLSYSSUITE_GUIDE.md` and the relevant provider guides.
Routine development uses `molsyssuite@uibcdf_3.14`, with Conda dependencies and
no-deps editable clones. Inspect interpreter/import origins and distinguish
known shared dependency findings from clean isolated qualification evidence.
Reuse molecular operations from MolSysMT and report provider needs to their owners.

The source package is under `src/peptidemt`, controlled tests under `tests` and
small runnable examples under `examples`. The current tests and full-minor CI
do not execute Macrel models. Real qualification evidence has a separately
authorized host budget and exact bundle. Local test reporting uses
`python -m pytest --receptor=llm`; CI uses the `ci` profile.

## Maintaining documentation

The provisional Sphinx/MyST/PyData layout follows MolSysMT and MolSysViewer.
Narrative pages use stable labels and API roles. The API reference extracts
actual installed functions/classes. The site contains no live notebook or
inference execution. The displayed Macrel call needs caller-supplied authorized
limits; the saved-result example only reads original evidence.

With dependencies from `devtools/conda-envs/docs_env.yaml`, build from the root:

```bash
python -m sphinx -b html -n -W --keep-going docs docs/_build/html
python -m sphinx -b doctest -n -W --keep-going docs docs/_build/doctest
python devtools/devguide_index.py --check
```

See [the source build guide](https://github.com/uibcdf/peptidemt/blob/main/docs/README.md)
for the inspected sibling revisions and dependency fixture. HTML/API/reference
warnings fail the build. Doctests exercise only memory-input examples. Generated
HTML is ignored; build CI retains a preview artifact and deploys no website.

## Evidence and reporting

Keep model identity, fixtures, unrounded outputs, input correspondence and
original producer versions. Archive resolved issue-backed reports and regenerate
their indexes. Acceptance of this exact resource does not authorize another
scientific model, chemistry/preprocessing changes, publication or later increment.

[PeptideMT #6](https://github.com/uibcdf/peptidemt/issues/6) owns this increment's
scientific disposition and delivery. The accepted
[central receipt](https://github.com/uibcdf/molsyssuite/issues/152) is separate
from the model evidence. Reports of broader provider or suite limitations retain
their respective owners.
