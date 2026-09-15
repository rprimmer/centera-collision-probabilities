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
  including acknowledgements and the references.
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

The corrected edition uses the single-column layout of the previous Centera
project and retains original authorship and the June 2005 date, with an explicit
September 14, 2026 revision notice. It includes all original numbered sections,
an editable TikZ figure, and two editable tables. The original transcription is
preserved at [commit 30902ccc9b4bad08714be6f3d0805e2bd9cac8d4](https://github.com/rprimmer/centera-collision-probabilities/tree/30902ccc9b4bad08714be6f3d0805e2bd9cac8d4).

## Corrections to historical qualifications

The corrections distinguish mathematical results, conditional workload models,
and historical product descriptions. This edition is not a new assessment of
all current cryptanalytic attacks or an empirical certification of Centera.

| Issue | Correction |
| --- | --- |
| Birthday bound treated as an actual probability | Added the exact product and exponential approximation. At the square-root scale the probability is 39.35%; the 50% point is about 1.17741 times that scale. |
| Fixed target versus any target | Distinguished second preimages from arbitrary-pair collisions; added the generic multi-target model. Fixed-target mean waiting time is `2^n`, not `2^(n-1)`, for independent ideal trials. |
| MD5 values and notation | Replaced ambiguous byte sequences with 32-bit register integers, explained little-endian serialization, and corrected the step's word index and rotation notation. |
| Unindexed final hash state | Replaced (2.2) with a consistently indexed length-strengthened recurrence and a proof with an explicit suffix-free encoding condition. Removed the use of the historical Lai–Massey discussion as a universal second-preimage lower bound. |
| GM tick units and quantization | Defined a 1,024 ms tick, an integer per-node per-tick write cap, and `B = A ceil(m/1024)`. Kept quantization and partial boundary ticks in the full union bound. |
| GM “Not possible” and universal online-attack claims | Replaced these with conditional probabilities and write-path assumptions. Distinguished random contents, prearranged MD5 collisions, repeated contents, and caller-controlled G. |
| Unsupported M++ attack costs | Described the multicollision calculation as a conditional estimate, with its work units and success probability. Removed the unsupported `2^119` second-preimage claim: truncating SHA-256 does not truncate its chaining state. |
| Rounded table values and storage units | Recomputed all M probabilities to three significant figures; distinguished logical decimal payload from physical protected storage. |
| SHA-1 “no practical collisions” | Replaced the historical statement with the documented 2017 full collision and added RFC 6151's MD5 security qualification. |

The illustrative 1,000-year workload uses 365-day years:

- M at 10,000 files/second: approximately **1.46 × 10^-10**.
- M++ at the same rate: approximately **1.10 × 10^-46**, under a joint
  independent uniform 248-bit-output model.
- GM at 100 nodes and 10,240 writes per tick per node: conditional upper
  bound approximately **3.92 × 10^-41**, under the stated 198-bit pair model.

The GM bound assumes coherent monotone timestamps without reuse, sequential
counters without resets inside a tick, and fresh independent uniform G values.
A long-term average write rate cannot substitute for the required per-tick cap.
For repeated content or prearranged MD5 collisions, only the 70-bit G factor
remains under that randomness assumption. If the caller can choose G, that
factor supplies no protection against that caller.

### Evidence and unresolved assumptions

Primary sources consulted for the corrections:

- [RFC 1321](https://www.rfc-editor.org/rfc/rfc1321.html), sections 2–3 and the
  reference implementation: MD5 words, byte order, initialization, and steps.
- [Kelsey and Schneier, second-preimage attacks](https://www.schneier.com/wp-content/uploads/2016/02/paper-preimages.pdf):
  the long-message attack and its chaining-state-width assumptions.
- [Joux, multicollisions](https://www.iacr.org/archive/crypto2004/31520306/multicollisions.pdf):
  limits of concatenated iterated-hash security claims.
- [CWI, first collision for full SHA-1](https://ir.cwi.nl/pub/25624) and
  [RFC 6151](https://www.rfc-editor.org/rfc/rfc6151.html): subsequent security findings.

The archived correspondence reports a raw-write path with caller control of G.
Which historical releases and permissions allowed it, actual timestamp and
counter semantics, and the original “100Mb” size limit still require product
or implementation evidence. The text now gives conditional interpretations
rather than selecting an unverified unit. A concrete M++ second-preimage cost
remains unestablished. Other historical product descriptions and reference URLs
are retained without a comprehensive release-history or link audit.

## Verification

Run `make check` for the standard-library Python checks in
[scripts/check-math.py](scripts/check-math.py). They compare exact small-space
birthday probabilities with the union bound, enumerate counter offsets around
wrap boundaries, verify every revised table probability, and check file-size
padding and MD5 byte order. These tests validate the stated mathematical model;
they do not validate historical Centera behavior.

The corrected PDF and extracted Overleaf package are checked for successful
compilation, resolved references, and matching text. Visual review covers every
page. The 12 numbered equation labels remain; the bibliography now contains
35 entries (33 historical references and two later security references).
Original archive checksums remain unchanged. Local verification records are
kept in `.conversion-baseline/`.
