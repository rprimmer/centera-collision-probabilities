LATEXMK ?= latexmk

.PHONY: all pdf clean clean-all distclean overleaf check help

all: pdf

# latexmk discovers dependencies (including figures) and resolves references.
pdf:
	$(LATEXMK) centera-collisions.tex
	cp build/centera-collisions.pdf centera-collisions.pdf

# Restrict cleanup to generated files in build/; retain the finished PDF.
clean:
	$(LATEXMK) -c centera-collisions.tex

clean-all: distclean

distclean:
	$(LATEXMK) -C centera-collisions.tex

check:
	python3 scripts/check-math.py

overleaf:
	python3 scripts/package-overleaf.py

help:
	@echo 'make            Build and refresh centera-collisions.pdf with pdfLaTeX'
	@echo 'make clean      Remove build intermediates; keep the PDF'
	@echo 'make distclean  Remove build outputs; keep the top-level PDF'
	@echo 'make overleaf   Package editable sources in dist/centera-collisions-overleaf.zip'
