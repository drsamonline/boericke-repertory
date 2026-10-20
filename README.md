# Boericke's Repertory — Digital Edition

A single-file, offline web application for **Dr. Oscar E. Boericke's *Repertory*** — the
clinical companion to William Boericke's *Pocket Manual of Homoeopathic Materia Medica*
(9th edition, 1927).

Compiled and designed by **Dr. Sohil Momin**.

---

## What it does

- **Search** 6,110 rubrics by symptom text, parent path or remedy name.
- **Repertorise** — select rubrics and get an automatic chart that scores every remedy
  across them (italic *grade 2* = 2 points, plain *grade 1* = 1 point) and ranks by total.
- **Save cases** — patient details, notes and prescription stored together; reload, print,
  and export/import as JSON.
- **Works completely offline** — one HTML file, no server, no build step, no internet.
- Light / dark / auto themes and four accent palettes; mobile friendly.

## Use it

Open `index.html` in any modern browser. That's the whole installation.

You can also host it for free on **GitHub Pages** (Settings → Pages → deploy from the
default branch) and share the link.

## Data

| | |
|---|---|
| Rubrics | 6,110 |
| Unique remedies | 1,461 |
| Chapters | 25 |

The dataset has been cleaned: remedies are de-duplicated (OCR variants merged into one
canonical name), duplicate rubrics are merged, and remedy-less category headings are kept
for structure but never appear in search results — so every rubric shown carries at least
one remedy.

## Credits

- **Content** — *Repertory* by **Oscar E. Boericke, M.D.** (1927), companion to the
  *Pocket Manual of Homoeopathic Materia Medica*, 9th ed., by **William Boericke, M.D.**
  Text digitised from the public-domain edition at homeoint.org (presented by Médi-T).
- **Design and application** — © 2026 **Dr. Sohil Momin**.

## Licence

Free to use, copy, modify and distribute, **provided that attribution is given** —
credit to *Oscar E. Boericke, M.D.* for the content and to *Dr. Sohil Momin* for the
design and application. See [LICENSE](LICENSE) for the full terms. Attribution is
**compulsory in all copies and derivative works**.

## Disclaimer

Provided "as is", for study and reference by qualified practitioners. Not a substitute
for professional homoeopathic or medical judgment.
