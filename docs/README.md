# Building the provisional documentation

PeptideMT uses Sphinx, MyST Markdown and the PyData theme, following the inspected
[MolSysMT documentation guide](https://github.com/uibcdf/molsysmt/blob/71fbe4f46d3c70e4e973c8025f01752a8c9b1084/docs/README.md)
and [MolSysViewer documentation conventions](https://github.com/uibcdf/molsysviewer/blob/73a6f388e09146650349dfe83564ae318ba20298/docs/AGENTS.md).
The structure is provisional; only implemented capabilities have user pages.
The scientific decision history and immutable evidence remain in `devguide/`.

Routine work uses `molsyssuite@uibcdf_3.14`, with the documentation tools supplied
by Conda. The minimal reproducible build fixture is
[`docs_env.yaml`](../devtools/conda-envs/docs_env.yaml); it needs neither Macrel
nor MolSysMT. Install this clone after its dependencies are present:

```bash
python -m pip install --no-deps --no-build-isolation --editable .
python -m sphinx -b html -n -W --keep-going docs docs/_build/html
python -m sphinx -b doctest -n -W --keep-going docs docs/_build/doctest
```

Open `docs/_build/html/index.html`. The build validates navigation, API references
and citations. Doctests exercise memory inputs only; ordinary code blocks and
literal-included scripts are displayed, not executed. The saved-results download
comes from the original committed JSON, without a duplicated fixture or model.
No notebook, live inference, asset download or website deployment occurs.

- `index.md`: landing page and section navigation.
- `content/about/`: scope, development installation and citation.
- `content/user/`: inputs, results, selectors and evaluator documentation.
- `content/showcase/`: the original saved Macrel case and replay instructions.
- `api/`: reference extracted from the installed public API.
- `content/developer/`: contributor/build routes and links to design evidence.

Pages use stable MyST labels and `{ref}`/API roles. Narrative pages are Markdown;
no notebook execution infrastructure or per-page governance files are needed by
this initial layout. Generated HTML stays ignored. The build-only documentation
workflow checks this fixture and retains a preview artifact; it deploys no site.
