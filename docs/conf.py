"""Build the provisional documentation against the installed PeptideMT."""

project = "PeptideMT"
copyright = "2026, UIBCDF"
release = "development"

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.napoleon",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinxcontrib.bibtex",
]
myst_enable_extensions = ["colon_fence"]
source_suffix = {".md": "markdown", ".rst": "restructuredtext"}
root_doc = "index"
language = "en"
exclude_patterns = ["_build", "README.md", "**/AGENTS.md"]
nitpicky = True
autodoc_typehints = "none"
autodoc_member_order = "bysource"
bibtex_bibfiles = ["bibliography.bib"]
bibtex_default_style = "alpha"
html_theme = "pydata_sphinx_theme"
html_title = "PeptideMT development documentation"
html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/uibcdf/peptidemt",
            "icon": "fa-brands fa-github",
        }
    ]
}
html_show_sourcelink = False
