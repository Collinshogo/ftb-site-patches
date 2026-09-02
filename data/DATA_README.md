# Product data for the Strategy-Tester-style panel (for KCON's build)

One JSON per product slug (`continuum`, `aftershock`, `slipstream`, `relay` = Headline Risk, `undertow` = The Press,
`meridian` = The Pendulum, `closer` = Counterweight, `lantern`, `first-light`, `undercurrent`, `confluence`).
Same shape as `_tools/trades/<slug>.json` on the site (drop-in replacement) plus a `tester` block and `provenance`.

**Source:** each file is computed from the TradingView List-of-Trades export of the **sell script itself**
(the "(AFT)" product a customer receives), taken on 2026-09-02 over 2026-01-01 → 2026-09-02 at the product's
shown Multiplier (`mult` in the catalog; every $ figure and contract count is already multiplied). The
`full`/`best` stat sets and `equity`/`daily` are as before. Never publish the research exports themselves.

## `tester`
- `performance_summary.all|long|short`: net_profit, gross_profit, gross_loss, profit_factor, max_runup,
  max_drawdown_closed, trades, winning, losing, percent_profitable, avg_trade, avg_win, avg_loss,
  ratio_avg_win_loss, largest_win, largest_loss, avg_minutes_in_trade — the TradingView Performance Summary /
  Trades Analysis rows, computed from closed trades (USD).
- `ratios`: sharpe_daily, sortino_daily (annualised from daily P&L, 252 days), trading_days, best_day, worst_day.
- `tv_summary`: where the desktop captured TradingView's own Performance Summary for the run (Continuum,
  Confluence, Undercurrent): `net`, `max_drawdown` (TradingView's OPEN-position max DD at 1×), `trades`,
  `max_drawdown_at_mult`, `net_at_mult`, `basis`. **Use `tv_summary.max_drawdown_at_mult` as the "Max drawdown"
  figure when present and label it "TradingView"; otherwise show `max_drawdown_closed` labelled
  "closed-trade".** A trade list cannot reproduce open-position drawdown.
- `list_columns` + `list`: the List of Trades — trade, side, entry_time_hour, exit_time_hour (**rounded to the
  hour on purpose**: exact minute times plus prices let a reader recover the strategy's stop/target distances),
  entry_px, exit_px, contracts, profit_usd, cumulative_usd, exit_kind (Stop / Target / Break-even stop /
  Session close / Trailing stop / Reversal / Exit — generic on purpose, never the internal signal names).
- Not derivable from a trade list and therefore absent: buy-and-hold return, per-trade run-up/drawdown, bars in
  trade (minutes are given instead).

## Properties tab (static text, same for every product unless noted)
Initial capital $25,000 · commission $0.75 per contract per side · slippage 2 ticks · order fills on bar close
(no fills on order events) · pyramiding per product (books 8, legs as shipped) · margin 0/0 · 1-minute chart ·
symbol MNQ1! (continuous) · window 2026-01-01 → 2026-09-02 · Multiplier as shown.

## Windows
The catalog's headline "best window" for Aftershock, Headline Risk, The Pendulum and Counterweight starts in
2025 (from the longer source record); these tester files cover the sell script's own 2026 run. Show the tester
panel with its own window stated ("record of the sell script, 2026-01-01 → 2026-09-02"); do not mix the two.
