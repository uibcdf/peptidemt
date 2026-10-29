SPHINXBUILD ?= python -m sphinx
SPHINXOPTS ?= -n -W --keep-going
BUILDDIR ?= _build

.PHONY: html doctest clean
html:
	$(SPHINXBUILD) -b html $(SPHINXOPTS) . $(BUILDDIR)/html

doctest:
	$(SPHINXBUILD) -b doctest $(SPHINXOPTS) . $(BUILDDIR)/doctest

clean:
	rm -rf $(BUILDDIR)
