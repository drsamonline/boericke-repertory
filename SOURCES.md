# Sources — what is in the app, and what could not be

This file exists because a repertory that quotes its source has to be able to say exactly where
each claim came from, and — just as importantly — where it does not.

## What the app ships

| | |
|---|---|
| **Rubrics, grades and remedy lists** | Oscar E. Boericke, *Repertory* (1927), the companion volume to William Boericke's *Pocket Manual of Homoeopathic Materia Medica*, 9th ed. |
| **Digitisation** | the public-domain edition at homeoint.org, presented by Médi-T (2000) — `homeoint.org/books4/boerirep/` |
| **Prefatory note** | quoted in full in the app's **About → How the repertory is arranged**, from the same digitisation (`books4/boerirep/note.htm`) |
| **Grade convention** | the author's own: italics mark "the more frequently verified clinical remedy" (grade 2); everything else is grade 1 |
| **Application, cleaning, design** | © 2026 Dr. Sohil Momin |

The cleaning applied to the text is documented in the README and recomputed live in
**About → Data audit**: OCR variants of a remedy name merged into one canonical name, duplicate
rubrics merged, remedy-less category headings kept for structure but never shown in search.

## What was attempted and could not be shipped

**D2 — the original source line beside each rubric.** The intent was to show, for every rubric,
the exact line as digitised, so a reader could check the parse against the book.

Three chapter pages were fetched from the digitisation to test this:

- `books4/boerirep/mind.htm` — returned, truncated mid-sentence at *"Joy, exces"*
- `books4/boerirep/ears.htm` — returned, truncated mid-sentence at *"Cal. picr., Cha"*
- `books4/boerirep/note.htm` — the prefatory note, **complete** (it is short)

Every chapter page is cut at the same fixed response budget, so a chapter can never be retrieved
whole through the tools available here. The sandbox itself cannot reach homeoint.org at all (the
host is not on the egress allowlist), so a direct download is not an option either.

Partial alignment was rejected on purpose: attaching a quotation to *some* rubrics and silently
omitting it from others produces an app that looks complete and is not — which is the one failure
mode a clinical reference must not have. A partly-quoted rubric beside a graded remedy list reads
as though the source says nothing more, and that is a lie the reader cannot detect.

**What ships instead, and is exact:** a **citation** for any rubric — the full path, the chapter,
the edition, and the grade-2 and grade-1 remedies listed separately, ready to copy into a case
note. It is generated from the same data the chart uses, so it cannot drift from it. Press the
`❝` button on any rubric row.

**D3 — chapter introductions.** The book's own prefatory note *is* the introduction, and it is
quoted in full. Per-chapter introductory prose does not exist in the digitisation as a separate
element; inventing it would be writing the book rather than quoting it.

**D5 — a second repertory (Kent, Boenninghausen).** The app shell is book-agnostic, but a second
dataset of this size cannot be obtained whole through the same route (see above), and shipping a
second book inside the same single file would roughly double it. It stays a plan, not a promise.

## How to verify any of this

```bash
bash scripts/check.sh          # 27 browser assertions + 6 crypto assertions
```

Two of the assertions check the citation directly: that it names the edition, and that it carries
the rubric path and the grade split. The prefatory note is checked for presence in the About panel.
