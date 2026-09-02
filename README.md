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
