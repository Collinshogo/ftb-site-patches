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
