# Centera Content Address: Collision and Preimage Resistance

LaTeX conversion of **Collision and Preimage Resistance of the Centera Content
Address**, by Robert Primmer and Carl D'Halluin, June 2005.

## Build

Requires pdfLaTeX and latexmk (for example, MacTeX or TeX Live), with the
packages listed in [preamble.tex](preamble.tex), including TikZ.

```sh
make
make overleaf
```

| Command | Result |
| --- | --- |
| `make` | Build `build/centera-collisions.pdf` |
| `make clean` | Remove intermediates; retain PDF |
| `make distclean` | Remove intermediates and generated PDF |
| `make overleaf` | Create `dist/centera-collisions-overleaf.zip` |

The Overleaf ZIP contains only editable sources and its own output-directory
configuration. See [OVERLEAF.md](OVERLEAF.md). Python 3 is required only for
ZIP packaging. Neither Pandoc nor Office applications are build dependencies.

## Layout

- [centera-collisions.tex](centera-collisions.tex): root document and reading order.
- [metadata.tex](metadata.tex), [preamble.tex](preamble.tex), [macros.tex): metadata,
  layout, packages, and common helpers.
- [sections/](sections/): abstract and the eight original numbered sections,
  including acknowledgements and all 33 references.
- [fig/](fig/): one editable TikZ diagram and two editable LaTeX tables.
- [scripts/package-overleaf.py](scripts/package-overleaf.py): source-only packager.
- `build/` and `dist/`: generated local outputs, excluded from Git.
- `Attic/`: all 19 original documents, research references, diagrams, and
  correspondence, preserved byte-for-byte and excluded from Git.
- `.conversion-baseline/`: local source extraction, original SHA-256 manifest,
  conversion intermediate, and validation records, excluded from Git.

## Conversion scope

The final, 10-page `Attic/Centera Collision Probs.pdf` is the authority for
mathematics, numbering, tables, and figure content. The matching
`Attic/WP - Centera Content Address - v2.21.odt` supplied the prose.
The Word document and every other original are retained unchanged.

The new 16-page PDF uses an 11-point, single-column layout matching the
previous Centera paper project. Original title, authors, affiliations,
June 2005 date, section order, claims, references, and three content notes
are retained. Layout and pagination are intentionally different. Figure 1
was reconstructed in TikZ; both tables use editable text and mathematics.
The third note is placed directly under Table 2 to keep it with its marker.

All 12 numbered equations and inline formula images were transcribed into
LaTeX. Equation, section, table, and figure references lost in the ODT import
were restored against the PDF. Citations are linked `\cite`/`\bibitem` entries
with original numbering. Broken import markup and equation spacing were
removed; redundant/unbalanced parentheses in the unnumbered MD5 step were
normalized. Table 1's scientific notation is typeset as powers of ten.

## Historical source qualifications

This is a historical transcription, not an updated cryptographic assessment.
Statements such as “presently,” attack costs, product limits, and release plans
refer to June 2005. Historical reference URLs are retained without verification.

The following issues are retained rather than silently rewritten:

- Table 2 says **“Not possible”** for GM even though the prose estimates a
  nonzero collision probability and discusses attacks with very high cost.
  The archived June 7, 2005 correspondence explicitly records this objection,
  also distinguishes attacks on a given file from attacks on any file in a
  system, and qualifies the claim that the G component cannot be controlled.
- The birthday expression in (5.2) is an upper bound. The M++ text uses the
  bound at `q = 2^124` as an approximately 50% probability; an upper bound
  alone does not establish that probability.
- Equation (2.2) ends with `H_(t+1)` although its displayed recurrence ends
  at `i = t`; the final length-block step is not explicitly indexed there.
- The MD5 initial values in (3.1) retain the original byte-order presentation;
  they should not be copied uncritically as implementation word constants.
- The GM analysis mixes per-second rates with 1,024-millisecond timestamp
  units, omits the additive quantization term in later approximations, and
  assumes random behavior for M and G. The original approximations and
  conditions are preserved.
- The source's “100Mb” notation, use of “preimage” for a given-file
  second-preimage discussion, rounded probabilities, and security assertions
  are retained.

These notes identify source limitations; no new security proof or empirical
validation of Centera is claimed.

## Verification

All pages were rendered for visual review. The final build has no unresolved
references, missing characters, overfull/underfull boxes, or LaTeX warnings.
The 12 numbered equations, 33 bibliography entries, section labels, two tables,
and figure were checked. Clean source-only builds, incremental behavior,
cleanup and rebuild commands, and an extracted Overleaf ZIP were tested
locally. No build on the Overleaf service was performed. SHA-256 comparison
confirmed that all 19 originals remain unchanged in `Attic/`.
