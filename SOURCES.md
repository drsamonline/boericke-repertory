# Sources — what is in the app, and how it was checked

A repertory that quotes its source has to be able to say exactly where each claim came from, and —
just as importantly — where it does not.

## What the app ships

| | |
|---|---|
| **Rubrics, grades and remedy lists** | Oscar E. Boericke, *Repertory* (1927), the companion volume to William Boericke's *Pocket Manual of Homoeopathic Materia Medica*, 9th ed. |
| **Digitisation the data came from** | the public-domain edition at homeoint.org, presented by Médi-T (2000) — `homeoint.org/books4/boerirep/` |
| **Prefatory note** | quoted in full in the app's **About → How the repertory is arranged**, from the same digitisation (`books4/boerirep/note.htm`) |
| **Grade convention** | the author's own: italics mark "the more frequently verified clinical remedy" (grade 2); everything else is grade 1 |
| **Verification text** | a complete HTML transcription of the same public-domain edition, published at `github.com/sudhirbrahma/REPERTORY-by-Oscar-E.-BOERICKE` (a 4.4 MB Word export of the book) |
| **Application, cleaning, design** | © 2026 Dr. Sohil Momin |

The cleaning applied to the text is documented in the README and recomputed live in
**About → Data audit**: OCR variants of a remedy name merged into one canonical name, duplicate
rubrics merged, remedy-less category headings kept for structure but never shown in search.

## The source check

Every rubric in the app was aligned against the transcription and compared remedy by remedy,
grade by grade. The result is shipped inside the app and shown at **About → Source check**:

| | |
|---|---:|
| Rubrics that carry remedies | **5,415** |
| Aligned to a line in the source | **5,408** (99.9%) |
| Identical — same remedies, same grades | **5,319** (98.2%) |
| Differ in some way | **96** |

The 96 are **listed individually in the app**, each with the source's own line and exactly what
differs: a remedy present in the book and missing here, a remedy present here and not in the book,
or a grade that disagrees. They are also marked with a small ⚠ on the result row, so a practitioner
can see at a glance where the parse departs from the book.

That is the honest form of "quoting the source": not a decorative quotation on every page, but a
claim that can be falsified rubric by rubric, with the disagreements published rather than hidden.

### How the alignment was done

1. The transcription was parsed into 8,220 candidate rubric lines, anchoring on the bold name runs
   the Word export uses (splitting on `<br>` was wrong — the export wraps a rubric name across a
   line break, which silently cut names in half).
2. Each line's remedy list was read with italics as grade 2 and plain text as grade 1.
3. Every app rubric was matched by normalised name; where a name occurs more than once, the remedy
   sets decide (Jaccard overlap ≥ 0.5, best candidate wins). 2,384 of the matches needed that
   tie-break, 3,709 were unique on the name alone.
4. The result ships as a 6,110-bit set (identical or not) plus the 97 differing lines — 22 kB in
   total, because the source lines are only carried where they disagree.

## What was attempted first, and failed

The obvious route was to quote the homeoint pages directly. Three were fetched:

- `books4/boerirep/mind.htm` — returned, truncated mid-sentence at *"Joy, exces"*
- `books4/boerirep/ears.htm` — returned, truncated mid-sentence at *"Cal. picr., Cha"*
- `books4/boerirep/note.htm` — the prefatory note, **complete** (it is short)

Every chapter page is cut at the same fixed response budget, and the build sandbox cannot reach
homeoint.org directly (the host is not on the egress allowlist). That is why the verification uses
a complete transcription obtained through GitHub instead — the same public-domain text, in a form
that can actually be read whole.

## Scope

This is **one book**. A second repertory is not planned: the app's value is a single file that opens
with no signal and produces a chart a practitioner can check by hand against the page, and a second
dataset would roughly double the file for a second book rather than a better one.

## How to verify any of this

```bash
bash scripts/check.sh          # 28 browser assertions + 6 crypto assertions
```

Five assertions cover the source check: that the data shipped, that more than 95% of rubrics verify
identical, that a known difference carries the source's line, that an identical rubric reports
identical, and that the panel is present in About.
