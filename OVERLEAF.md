# Overleaf source package

Upload `dist/centera-collisions-overleaf.zip` as a new Overleaf project.
Select `centera-collisions.tex` as the main document and pdfLaTeX as compiler.

- `sections/*.tex`: manuscript, editable mathematics, and 35 references.
- `fig/iterated-hash.tex`: editable TikZ diagram; edit nodes and coordinates.
- `fig/*-table.tex`: editable tables.
- `metadata.tex`: title, original authors/date, and corrected-edition date.
- `preamble.tex`: layout and packages.

No shell escape, Office files, or external conversion tools are required.
The ZIP's `latexmkrc` lets Overleaf manage its output directory. To test the
extracted ZIP locally, run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error centera-collisions.tex
```

The local project uses `make` to generate `build/centera-collisions.pdf` and
`make overleaf` to regenerate the ZIP. Original documents in `Attic/` remain
local and are excluded from the ZIP and Git repository. The September 14, 2026 corrected edition revises mathematical and security
claims; see the repository README for corrections and unresolved assumptions.
