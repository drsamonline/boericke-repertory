# Roadmap — enhancements that keep the promise

Every item here is judged by one rule, the same one the app is built on:

> **No internet after load. No external dependency. No service that can be switched off,
> rate-limited, paywalled or discontinued.**

Status is honest: **done** means it ships in the app and is covered by a test; **next** means it
is designed but not built; **declined** means it was considered and rejected with a reason.

---

## Delivered

| # | Enhancement | Note |
|---|---|---|
| A1 | **Query operators** — `"exact phrase"`, `-exclude`, `a or b` | parsed properly; phrases match across path separators |
| A2 | **Typo tolerance** — edit distance 1 including transpositions | only fires when nothing matched at all; vocabulary built from rubric names at load |
| A3 | **Browse by chapter** — lazy tree with counts | the book's own structure, not a guess at words |
| A4 | **Must-have rubrics** — Boenninghausen-style elimination | misses are faded, or filtered out |
| A5 | **Configurable grade weights** | 1/2/3, printed on the chart and in the print sheet |
| A6 | **Saved searches** | query + chapter filter, 40 kept |
| A7 | **Per-rubric notes** | kept on the device, keyed by rubric path |
| A8 | **Similar rubrics** — computed, not curated | word overlap within a chapter, labelled a heuristic |
| A9 | **Filter the chart** by remedy name | plus a must-only filter |
| A4b | **Elimination by repertory section** | "must: every rubric" or "must: one per chapter", remembered between sessions |
| B1 | **Encrypted vault** — AES-256-GCM, PBKDF2-SHA256 200,000 | key never stored; round trip tested in `scripts/vault_test.mjs` |
| B2 | **Patient grouping and case search** | grouped by patient, searchable across notes, prescription and top remedies |
| B2b | **Visit history per patient** | each patient shows its visit count and date range, with a **New visit** action that keeps the earlier one |
| B3 | **Autosaved draft and undo** | `Ctrl`/`Cmd + Z`, 30 steps |
| B4 | **One-page A4 case sheet** | `@media print`, `@page` margins, page-break rules |
| B5 | **CSV of a chart, CSV of every case, JSON of everything** | plain-text exit from every screen |
| B6 | **Backup reminder** | shown when cases exist and nothing has ever been exported |
| C1 | **Service worker done correctly** — HTML network-first, assets cache-first, `CACHE` bumped, `update()` on load, build stamp | the trap this estate already hit once |
| C2 | **Manifest and install on `play/`** | plus generated icon sizes |
| C3 | **File System Access** with a download fallback | `showSaveFilePicker` when present, never required |
| C5 | **Command palette** on `Ctrl`/`Cmd + K` | rubrics, remedies and cases in one box |
| D1 | **Remedy alias table** | *Gelsemium* finds *Gels*; partial by design, it only ever widens a search |
| D4 | **Data audit panel** | recomputed in the app from the embedded dataset |
| D2b | **A citation for any rubric** | path, chapter, edition and the grade split, copyable offline — generated from the chart's own data so it cannot drift |
| D2c | **Every rubric verified against the source** | all 5,415 remedy-bearing rubrics aligned; 5,319 identical; the 96 that differ are listed with the source's own line and marked ⚠ on the row |
| E1 | **Table semantics and a focus trap** | `scope`, `caption`, trapped Tab in both overlays |
| E2 | **Text size control** | three steps, remembered |
| — | **Interface language** | English only, by decision: the app is for a practitioner reading Boericke, and a half-translated clinical interface is worse than one language done properly |
| E4 | **High-contrast theme** | alongside light / dark / auto |
| F1 | **One icon source, all sizes** | SVG → PNG 512/192/180/32, `.ico` |
| F2 | **The release pipeline embeds the real mark** | `docs/play/icon.png` is the file `make_icons.py` reads first, so the `.exe` and `.apk` stop falling back to a monogram |
| F3 | **Android adaptive icon layers** | foreground inside the 62% safe zone + background |
| F4 | **Locally drawn social card** | replaced the external socialify image |
| F5 | **Tagged release with notes** | `v1.2.0`, not just the rolling `app-latest` |
| F6 | **Release assets carrying the artwork** | icon PNGs, the single `index.html`, `SHA256SUMS` |

## Next

| # | Enhancement | Why it is not done yet |
|---|---|---|
| F8 | **Repo social preview set from the card** | GitHub only accepts it from the web UI, not the API |

## Declined, with the reason

| # | Idea | Decision |
|---|---|---|
| C4 | **Search index in a Web Worker** | **measured and declined.** A full scan of all 6,110 rubrics averages **2.75 ms** (`node` benchmark, 80 runs) — well inside one frame. A worker would add a second copy of the index and a `postMessage` round trip for no perceptible gain. Revisit only if a second book is bundled. |
| C6 | **Print the whole repertory** | 6,110 rubrics is a book, not a sheet. A generated PDF is the honest artefact; the print stylesheet is tuned for a case sheet instead. |
| D3 | **Chapter introductions from the book** | **delivered as the prefatory note** — the author's own five rules, quoted in full in About. There is no separate per-chapter introduction in the digitisation, and inventing one would be writing the book. |
| — | **Cloud sync or accounts** | a patient record that syncs is a patient record that leaks. |
| — | **"AI repertorisation"** | a ranked chart you cannot check by hand is worse than no chart. |
| — | **Analytics, crash reporting, A/B tests** | there is no server to receive them, by design. |
| — | **Third-party PDF, charting or UI library** | every one is a network fetch and a future breakage. |
| — | **Web fonts** | system fonts render instantly, offline, and cost nothing. |

---

## The rule, restated for whoever picks this up

If a change needs a network call, a package, a service or an account, it does not go in this
app — it goes in a different app. The whole value of this one is that it opens in a consulting
room with no signal and works, and that a chart it produces can be checked by hand against the
page.
