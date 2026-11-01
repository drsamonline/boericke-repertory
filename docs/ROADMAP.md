# Roadmap — enhancements that keep the promise

Every item here is judged by one rule, the same one the app is built on:

> **No internet after load. No external dependency. No service that can be switched off,
> rate-limited, paywalled or discontinued.**

That rules out a lot of fashionable things — a CDN, a hosted font, an analytics script, a
cloud sync, an "AI" endpoint, an icon service, an embedded map, a third-party PDF library.
It leaves a surprising amount that is genuinely better for a clinical tool: everything below
runs from the same single file, on a laptop in a consulting room with the Wi-Fi off.

Ordered roughly by value per unit of work. Nothing here is a promise; it is a list.

---

## A. Search and repertorisation

| # | Enhancement | Why it matters | Notes |
|---|---|---|---|
| A1 | **Query operators** — `"exact phrase"`, `-exclude`, `or` | A repertory search is a clinical query, not a keyword box. Exclusion is how you cut a big rubric down. | Pure string logic over the existing index. No library. |
| A2 | **Typo tolerance** (edit distance ≤ 1, precomputed) | The source is OCR'd text and users type from memory: *burnign*, *gelsemum*. | Build a small deletion-index at load; ~50 ms for 6,110 rubrics. |
| A3 | **Browse without searching** — chapter → section → rubric tree | The book's own structure is a navigation path; some practitioners think in chapters, not words. | Reuses `PATHS`, already computed. |
| A4 | **Must-have vs nice-to-have rubrics** (Boenninghausen-style elimination) | Right now every selected rubric scores equally. Marking a rubric *essential* and another *optional* is how a chart is actually reasoned. | Chart maths only; no data change. |
| A5 | **Configurable grade weighting** | Boericke's 1/2 scale is the default; some schools weight 1/2/3. Let the practitioner choose and **show the scale on the chart** so it stays auditable. | Store in `localStorage`; print the scale in the header. |
| A6 | **Saved searches** | "The three rubrics I use every Monday" is a real workflow. | Array in `localStorage`, exportable with the case. |
| A7 | **Per-rubric personal notes** | "In my experience this rubric is unreliable." Kept on the device, never merged into the source text. | Separate key; never exported unless asked. |
| A8 | **Curated `see also` links** between near-duplicate rubrics | The cleaning pass merged exact duplicates; near-duplicates remain and are a known hazard. | A small hand-curated table shipped in the file. |
| A9 | **Search inside the chart** — filter the remedy table by name/grade | At 29+ rows the table is long. | Client-side filter. |

## B. Cases, privacy and the record

| # | Enhancement | Why it matters | Notes |
|---|---|---|---|
| B1 | **Encrypted local vault** — AES-256-GCM, key from a passphrase via PBKDF2 | Cases carry patient names and prescriptions. Today they sit in plain `localStorage`. This is the single biggest credibility upgrade available. | WebCrypto is in the browser: **zero dependencies**. Same approach as `app-encrypted-case-log`. |
| B2 | **Many patients, many cases** — a patient list with its own search | One flat case list stops working at about twenty cases. | Schema change + a small migration. |
| B3 | **Autosave draft + undo** | Losing a half-built chart to a stray tap is the most common real complaint. | Debounced write, in-memory undo stack. |
| B4 | **One-page case sheet** — a print stylesheet that fits an A4 sheet: patient, rubric list with grades, ranked remedies, prescription | Printing the raw chart wastes paper and looks unfinished. | CSS only (`@media print`). |
| B5 | **Export everything, import everything** — one JSON of all cases, plus CSV of any chart | Data you cannot get out is data you do not own. | Already half-built; extend to bulk. |
| B6 | **Backup reminder** | Browser storage is cleared by "clear browsing data". A quiet warning when cases exist and no export has ever been made. | One flag in `localStorage`. |

## C. Offline and installability

| # | Enhancement | Why it matters | Notes |
|---|---|---|---|
| C1 | **Service worker, done correctly** — HTML network-first, assets cache-first with background refresh, `CACHE` bumped every release, `registration.update()` on load, **build stamp in the footer** | A cache-first worker is how a shipped fix stays invisible. This is the trap the estate already hit once. | No dependency; the worker is a ~40-line file. |
| C2 | **Manifest + install on `play/`** | The landing page has one; the app should install to the home screen too, full-screen, still offline. | `manifest.webmanifest` + icons already generated. |
| C3 | **File System Access API** — open and save a case file directly, with the download fallback | Removes the download/upload round trip on Chromium; degrades to today's behaviour elsewhere. | Feature-detect; never required. |
| C4 | **Search index in a Web Worker** | Keeps typing instant if the repertory grows or a second book is bundled. | Structured clone, no library. |
| C5 | **Command palette** (`Ctrl/⌘+K`) over rubrics, remedies and cases | One keystroke to anywhere; matches how the rest of the estate behaves. | Reuses the existing search index. |
| C6 | **Printable A4/A5 layout for the whole repertory** | Some practitioners want the book back on paper. | `@media print` over the whole tree. |

## D. Content and data quality

| # | Enhancement | Why it matters | Notes |
|---|---|---|---|
| D1 | **Remedy synonyms and abbreviations** — `Ign` → *Ignatia amara*, with the canonical name always shown | The source uses abbreviations; the abbreviation is also how people search. | Pure data table, bundled. |
| D2 | **Original source line for each rubric** — the Boericke text beside the parsed rubric | Traceability. This is the design principle of `app-thermals` applied here. | Requires a bundled source extract; still one file, still offline. |
| D3 | **Chapter and section introductions** from the book | Orientation before the first search. | Bundled text. |
| D4 | **Data audit page** — counts, orphan remedies, grade distribution, duplicate candidates | Lets a reader check the cleaning rather than trust it. | Generated at build time, shipped as static content. |
| D5 | **Cross-book groundwork** — a second repertory (Kent, Boenninghausen) in the same shell | The shell is book-agnostic already; a book switcher is mostly data plumbing. | One file per book, or a bundle with a selector. |

## E. Accessibility and language

| # | Enhancement | Why it matters | Notes |
|---|---|---|---|
| E1 | **Chart table semantics** — proper `th`/`scope`, a caption, focus trap in the remedy modal | The chart is a data table and should be announced as one. | Markup only. |
| E2 | **Text size and spacing control** | Long reading sessions; low-vision practitioners. | CSS variables, remembered. |
| E3 | **Hindi and Gujarati UI** | The estate already ships trilingual companions; the clinical vocabulary is the hard part, not the strings. | Bundled JSON dictionaries, no i18n library. |
| E4 | **High-contrast theme** alongside light/dark/auto | Already has light/dark/auto; a third palette is cheap. | One more `data-theme` block. |

## F. Releases, icons and distribution

The build pipeline already produces the portable `.exe` and the signed `.apk` from the same
commit as the demo. What it does not yet do is *present* them.

| # | Enhancement | Why it matters | Status |
|---|---|---|---|
| F1 | **One icon source, all sizes** — `docs/icon.svg` → PNG 512/192/180/32, `.ico`, maskable variant | Done: `scripts/icons.py`. No icon service, no download. | ✅ done |
| F2 | **Windows `.ico` with six embedded sizes** for the portable build | A default Electron/WebView icon in the taskbar reads as unfinished. | ✅ asset done — still to be wired into `app-builder` |
| F3 | **Android adaptive icon** — separate foreground and background layers with the 66% safe zone | Android crops and masks icons; a single flat PNG gets clipped. | asset to add |
| F4 | **Locally drawn social card** (1280×630) replacing the external socialify image | The last network dependency in the repo's own metadata. | ✅ done: `scripts/social.py` |
| F5 | **Tagged releases with notes, not just `app-latest`** — `v1.1.0` with a short "what changed" and a screenshot | A rolling tag tells a reader nothing about when a feature arrived. | next |
| F6 | **Release assets that carry the artwork** — attach `icon-512.png`, `icon.ico`, the single `index.html` and a `SHA256SUMS` file to each tagged release | Lets a downloader verify the file and gives the release page a face. | next |
| F7 | **A release strip on the landing page** — version, date, icon, one line | Turns the page from a brochure into a changelog you can read at a glance. | next |
| F8 | **Repo social preview set from the same card** | GitHub's own preview is the first thing anyone sees. | manual, one-time |

## G. Deliberately not on the list

Kept here so the omissions read as decisions rather than gaps:

- **No cloud sync or accounts.** A patient record that syncs is a patient record that leaks.
- **No "AI repertorisation".** A ranked chart you cannot check by hand is worse than no chart.
- **No analytics, no crash reporting, no A/B tests.** There is no server to receive them.
- **No third-party PDF, charting or UI library.** Every one of them is a network fetch and a
  future breakage; the app has no dependency and should keep it that way.
- **No web fonts.** System fonts render instantly, offline, and cost nothing.

---

## Suggested order

1. **B1 encrypted vault** — the largest gain in trust for the least surface area.
2. **A1 + A2 search operators and typo tolerance** — the daily-use improvement.
3. **C1 + C2 service worker and install** — done carefully, with the build stamp.
4. **B4 + B3 one-page case sheet and autosave** — the polish practitioners notice.
5. **F5 + F6 + F7 tagged releases with icons and notes** — the public face of the work.
6. **A4 + A5 elimination and weighting** — the feature that changes how the tool is used.
