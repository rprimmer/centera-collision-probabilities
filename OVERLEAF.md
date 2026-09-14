# Overleaf source package

Upload `dist/centera-collisions-overleaf.zip` as a new Overleaf project.
Select `centera-collisions.tex` as the main document and pdfLaTeX as compiler.

- `sections/*.tex`: manuscript, editable mathematics, and 33 references.
- `fig/iterated-hash.tex`: editable TikZ diagram; edit nodes and coordinates.
- `fig/*-table.tex`: editable tables.
- `metadata.tex`: original title, authors, and June 2005 date.
- `preamble.tex`: layout and packages.

No shell escape, Office files, or external conversion tools are required.
The ZIP's `latexmkrc` lets Overleaf manage its output directory. To test the
extracted ZIP locally, run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error centera-collisions.tex
```

The local project uses `make` to generate `build/centera-collisions.pdf` and
`make overleaf` to regenerate the ZIP. Original documents in `Attic/` remain
local and are excluded from the ZIP and Git repository. Historical technical
claims are preserved; see the repository README for known source issues.
