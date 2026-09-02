# ftb-site-patches

Patch series for futurestradingbots.com (`Kkongmerc/goal33-site`), prepared by the All Fluence Trading
director session. Public on purpose: a session sourced from the site repo can only fetch public repos.

| File | Base | Contents |
|---|---|---|
| `site_patch_aft-mnq-lineup-v5.patch` | site `main` @ `c2b5e50` (2026-09-02 ~01:10 ET) | ONE commit: the eleven MNQ products (Confluence included), the All Fluence Trading logo in header and footer, a data-driven "Use code AFT at checkout" line next to every buy button (`promo` object in catalog2.json), Risk/trade · Max loss · Return on risk/mo on every product page and in the index table, main page: "Net" → "Profit" (highlighted), the line "All strategies simulated based on a $10,000 or less drawdown." above the table, "MNQ/NQ" → "MNQ", and the call to action "Select any of the profitable strategies below to see the trade details and results.", at their $10k-drawdown multiples, scaled trade logs, glyphs/skins, "Backtest-verified" wording, "Shown at Multiplier N" on every product page + Mult and RoDD/mo columns in the index table, headline metric = average monthly return on drawdown as a percentage (overall RoDD shown as a percentage with its window), plan-finder guard, the 60-day Performs-as-Published guarantee in the terms and buy boxes. Removed products archived in `_tools/archive/catalog2.removed-2026-09-02.json`. |

Apply on a checkout of the site's `main`:

```
git fetch origin
git checkout -b aft-mnq-lineup-v5 origin/main
git am -3 site_patch_aft-mnq-lineup-v5.patch
git push -u origin aft-mnq-lineup-v5
```

Merging that branch into `main` is the deploy (GitHub Pages).

v2 (base 78da080) is superseded by v3 and was removed.
v3 (base d711af9) is superseded by v4 and was removed.
v4 (base 5adcbf2) is superseded by v5 and was removed.

## v6 — 2026-09-03 (base: goal33-site `main` @ 8c73a46)
`site_patch_aft-lineup-v6.patch` — apply from the site repo root on a fresh branch off `main`:

```
git fetch origin && git checkout -b aft-lineup-v6 origin/main
git apply --3way site_patch_aft-lineup-v6.patch     # (download the patch from this repo first)
git add -A && git commit -m "Lineup v6" && git push -u origin aft-lineup-v6
```
What it changes: the index spec table is centred in every cell; headings read "Win Rate" and "Profit Factor";
the Profit column is now **Avg Monthly Profit** in green (e.g. `+$59,023 per month`), Risk/trade and RoR/mo are
retired from the table (they stay on the product pages); every flagship pane shows its avg monthly profit and win
rate in the centre; five MGC products join (Midas gold book, The Assay, The Kilo, The Print, The Fix — The Ingot is
held back until its standalone matches the book leg); every product page carries "This strategy was optimized
from … to …" + the best-RoDD window statement and a downloadable CSV of that window's trades
(`strategies/data/<slug>-best-window-trades.csv`). Pipeline: gen_pages → rebuild_index → gen_plan → css restamp
(all already run; the patch carries the generated pages). `data/` gains the five MGC Strategy-Tester JSONs.

## v7 — 2026-09-03 (base: goal33-site `main` @ 8c73a46; SUPERSEDES v6 — apply v7 only)
`site_patch_aft-lineup-v7.patch` — same three commands as v6 with `v7` in the names. Everything in v6 plus:
**Triad** (the MNQ Strong Book: FVG continuation + both 08:30 range fades, shown at ×3 by the owner's call) and
**The Alloy** (the gold Level-Reclaim + FVG-Continuation combo, ×3) join the lineup; The Print and The Fix are
parked until the fresh exports of their re-cut vectors land (they return in v8 with The Ingot). `data/` carries
every listed product's Strategy-Tester JSON, including the two combos.

## v8 — 2026-09-03 (base: goal33-site `main` @ 3165f01 = v7 applied; apply v8 on top)
`site_patch_aft-lineup-v8.patch` — the product page's report is now a facsimile of TradingView's Strategy Tester:
top strip (name tab · date chip with DEEP badge · 25 K USD · Default detalization · Script execution), four
alternate tabs — **Overview** (Key stats + the Performance chart with the cumulative PnL line, per-trade bars,
right axis, day strip, Performance-analysis pill row + Breakdown cells), **Performance** (Breakdown · Periodical
monthly table · Profits and losses by signal / by side), **Trades** (Distribution histogram + donut, Streaks,
details), **List of trades** (+ Side column). Zero JS, no inline styles, fits the column at 1400 / 1024 / 375.
`data/*.json` rows now carry side · signal · qty · return % (columns listed in each file's `trades_columns`).
Round 4 (re-cut, same file): Streaks is TradingView's per-trade streak chart (Count / Amount toggle, four streak
stats); the trade-list CSV link sits under the report; **Buy now** at the top (hero) and the middle (under the
report); the combined-books index row takes each book back to one multiple, merges the two curves and sizes to the
largest whole multiplier holding the merged drawdown under $10,000 (never below ×3) — currently ×6, drawdown 1× and
at ×K both shown; a profitable worst month renders green. The Vault (gold 08:30 range fade) is dropped from the lineup and its data file removed.
Round 5 (re-cut, same file): **The Bullion** (gold London breakout) joins the gold singles and The Fix is relabelled
as the London fade; every product page opens with a centred "$X average monthly profit with a Y% return on drawdown!"
headline; the discount sits beside every call to action; the monthly special is a scrolling banner at the top and
bottom of every page (paused on hover and under reduced-motion); the report's top strip and bottom block are
compressed, the title block centred with the date / 25 K USD / ticks / bar-close chips on the left; report stat
cells larger; Headline Risk's worst month verified (Aug 25, a real losing month, not a data error); the daily-results calendars show up to nine months.
Round 6 (re-cut, same file): the index gains **Coming soon** sections for MYM, M2K, MES, additional gold and SIL, listing
only constructions that passed the validation sweep (no prices or links yet); Recoil (MNQ 08:30 failed-break reclaim) is
registered as an unlisted draft pending a larger-target vector.
Round 7 (re-cut, same file): **new pricing** by average monthly profit at the shown multiplier — ≤$10k → $75 · $10–14k →
$125 · $14–18k → $200 · $18–20k → $275 · $20k+ → $350; Midas $550 · Triad $700 · Slipstream $700 · Continuum $950 · The Books $1,200 ·
All-Access $1,500 (books included; $1,200/mo with 3 months up front). Every index table now shares one column plan so
rows align across sections; section titles centred. The Performance chart now plots the best window only, from zero at its start (Lantern, The Alloy and every other page). Index hero rewritten: "Automated Futures Trading" headline, SEO title and meta description, the "Use code AFT" lines removed. Every strategy row on the index is clickable anywhere (full-cell links, row hover).
Same three commands with `v8` in the names.


## Whop checkout links (how they reach the site session)
The Whop store is created by the Whop publisher in the research repo, which the site session cannot read. The flow:
1. The session holding the Whop key runs `_work/tools/whop_publish.py` (research repo). It writes
   `research/products/WHOP_PUBLISH_RESULT.json` = `{slug: {id, url}}` with the real per-product checkout URLs.
2. That session copies the file here verbatim as `data/whop_links.json` and pushes this repo.
3. The site session runs, from the site clone root: `python3 <patches>/apply_whop_links.py <patches>/data/whop_links.json`,
   regenerates (`_tools/rebuild_index.py`, `gen_pages.py`, `gen_plan.py`), verifies no `goal33systems` link remains
   (`grep -c goal33systems index.html strategies/*.html`), commits and pushes.
**Status 2026-09-03 (evening):** DONE — the store holds all 22 products, `data/whop_links.json` is populated from the
store's own records, and `site_patch_whop-links.patch` has the links already applied. Re-run `apply_whop_links.py` only
if the catalog is rebuilt from a source that drops the `whop` fields.

## whop-links-v4_2026-09-02.patch — point every buy link at the AFT Whop store
Base: site `main` @ `31bbe8f`. **Supersedes v3** (v3 predates the combined-books product and is deleted).

Three source files, no generated HTML:
- `_tools/catalog2.json` — each strategy's `whop`, `bundles.all_access.whop`,
  `bundles.books_all.whop`, and `whop_store` → `https://whop.com/aft-official/`
- `_tools/gen_pages.py` — the All-Access buy box links to its own product, not the store front
- `_tools/rebuild_index.py` — **the combined books row** (Continuum + Midas, $1,200/mo, the site's
  number-one row) hardcoded `whop: WHOP_STORE`; it now reads `bundles.books_all.whop`

    git checkout -b whop-links main
    git am -3 whop-links-v4_2026-09-02.patch
    python3 _tools/gen_pages.py && python3 _tools/rebuild_index.py && python3 _tools/gen_plan.py
    git commit -am "Regenerate pages for the AFT store links"
    git push -u origin whop-links

Verified on a clean checkout of `31bbe8f`: after the generators, zero `goal33systems` in any
live-facing page, 98 `aft-official` links, and the combined books row pointing at `the-books-aft`.

**All 22 Whop products are now VISIBLE**, so this is safe to merge — the earlier "do not merge"
warning no longer applies.

⚠ If `main` has moved and the patch conflicts, do NOT hand-resolve `catalog2.json` — take the URLs
from `WHOP_PRODUCT_URLS.md` beside this file and re-apply the three source edits.


## `site_patch_whop-links.patch` — 2026-09-03 (base: `main` @ 31bbe8f) — **supersedes site_patch_the-books-page.patch**
Two commits, both needed:
1. **The Books bundle page restored.** The books moved into the `strategies` list and `CAT["books"]` went empty, so
   `gen_pages.py` silently stopped generating `/strategies/the-books.html` while the index's Continuum + Midas row, both
   book pages' breadcrumb and their back-link still pointed at it. The generator now derives its books list from
   `strategies` (kind == "book"); the page is generated again with corrected copy (both engines, $1,200/mo) and the
   index row links to the page instead of the `/#books` anchor.
2. **Real checkout links.** Every buy link now points at the live AFT store product. The links are NOT guessed: they
   come from the store's own product records, each of which carries its site catalog slug in `metadata.aft_slug`, so
   the mapping is exact (e.g. `closer` → `counterweight-aft`, `meridian` → `the-pendulum-aft`, `relay` →
   `headline-risk-aft` — three cases a name-based guess would have got wrong). `whop_store` is set to the store root,
   and The Books / All-Access pages carry their own product links. `data/whop_links.json` holds the slug → {id, url}
   map used, for re-application after any regeneration.
   **Verified:** 22 products live, each with a visible monthly renewal plan whose price matches the catalog; 42 checkout
   links across the index, plan finder and product pages; zero references to the old store remain.
Apply: `git checkout -b aft-whop-links main && git am < site_patch_whop-links.patch`, then regenerate
(`python3 _tools/gen_pages.py && python3 _tools/rebuild_index.py && python3 _tools/gen_plan.py`), verify
`grep -c goal33systems index.html strategies/*.html` is zero everywhere and `ls strategies/the-books.html` exists.

## ~~`site_patch_the-books-page.patch`~~ — superseded by `site_patch_whop-links.patch` (which contains this commit)
Fixes the dead **Continuum + Midas** link. The books moved into the `strategies` list and `CAT["books"]` went empty, so
`gen_pages.py` silently stopped generating `/strategies/the-books.html` while the index row, both book pages' breadcrumb
and their back-link still pointed at it. The generator now derives the books list from `strategies` (kind == "book"),
the bundle page is generated again (Continuum + Midas, $1,200/mo, copy corrected from "all four engines"), and the
index row links to the page instead of the `/#books` anchor.
Apply: `git checkout -b aft-the-books-page main && git am < site_patch_the-books-page.patch`, then
`python3 _tools/gen_pages.py && python3 _tools/rebuild_index.py && python3 _tools/gen_plan.py`, verify
`ls strategies/the-books.html` and that the index row href is `/strategies/the-books.html`, and push.
