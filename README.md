# ftb-site-patches

Patch series for futurestradingbots.com (`Kkongmerc/goal33-site`), prepared by the All Fluence Trading
director session. Public on purpose: a session sourced from the site repo can only fetch public repos.

| File | Base | Contents |
|---|---|---|
| `site_patch_aft-mnq-lineup-v2.patch` | site `main` @ `78da080` (2026-09-01 23:48 ET) | ONE commit: the ten MNQ products at their $10k-drawdown multiples, scaled trade logs, glyphs/skins, "Backtest-verified" wording, "Shown at Multiplier N" on every product page + a Mult column in the index table, plan-finder guard, the 60-day Performs-as-Published guarantee in the terms and buy boxes. Removed products archived in `_tools/archive/catalog2.removed-2026-09-02.json`. |

Apply on a checkout of the site's `main`:

```
git fetch origin
git checkout -b aft-mnq-lineup-v2 origin/main
git am -3 site_patch_aft-mnq-lineup-v2.patch
git push -u origin aft-mnq-lineup-v2
```

Merging that branch into `main` is the deploy (GitHub Pages).
