# Boericke's Repertory — Digital Edition

A single-file, offline web application for **Dr. Oscar E. Boericke's *Repertory*** — the
clinical companion to William Boericke's *Pocket Manual of Homoeopathic Materia Medica*
(9th edition, 1927).

Compiled and designed by **Dr. Sohil Momin**.

![Search](screenshots/search.png)
![Repertorisation chart](screenshots/chart.png)

---

## Features

**Search**
- Instant search across 6,110 rubrics by symptom text, parent path or remedy name.
- Matched terms are highlighted; filter to any of the 25 chapters.
- Full keyboard control: `/` to focus search, `↑` `↓` to move, `Enter` to add a rubric.

**Repertorise**
- Tap rubrics to build a chart that scores every remedy across them
  (italic *grade 2* = 2 points, plain *grade 1* = 1 point) and ranks by total.
- Sort by total score, rubric count or remedy name; top-10 remedy bars.
- Print straight from the app (no pop-ups) or export.

**Remedy browser**
- Tap any remedy inside a rubric to see **every rubric that lists it**, with its grade —
  a fast way to check a remedy's full clinical picture.

**Cases**
- Save patient details, notes and prescription alongside the rubric selection and chart.
- Reload, print, export/import as JSON.

**Everything else**
- Fully **offline** — one HTML file, no server, no build step, no internet, no tracking.
- Modern responsive UI with light / dark / auto themes and five accent colours.
- Works on phone, tablet and desktop.

## Use it

Open `index.html` in any modern browser. That's the whole installation.

To host it free on **GitHub Pages**: Settings → Pages → deploy from the default branch,
then share the link.

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
