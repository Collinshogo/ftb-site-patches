# AFT Whop product URLs (authoritative)

Returned by the Whop API when the products were created on the AFT store
(`biz_G9AWq2Fgg1uLUM`, route `aft-official`). Source of truth for any buy link. All are VISIBLE.

⚠ **Four do not follow the catalog slug** — `undertow`, `relay`, `meridian` and `closer` were renamed
before launch and their Whop route follows the product NAME. A rule like "`<slug>-mnq` becomes
`<slug>-aft`" sends four of twenty buyers to the wrong product. Copy from this table; do not derive.

`the-books` is the site's number-one row — Continuum + Midas run as one account, $1,200/mo. It is not
in `strategies[]`; `rebuild_index.py` synthesises it, and its link comes from `bundles.books_all.whop`.

| catalog slug | Whop URL |
|---|---|
| `aftershock` | https://whop.com/aft-official/aftershock-aft/ |
| `all-access` | https://whop.com/aft-official/all-access-aft/ |
| `closer` | https://whop.com/aft-official/counterweight-aft/ |
| `confluence` | https://whop.com/aft-official/confluence-aft/ |
| `continuum` | https://whop.com/aft-official/continuum-aft/ |
| `first-light` | https://whop.com/aft-official/first-light-aft/ |
| `lantern` | https://whop.com/aft-official/lantern-aft/ |
| `meridian` | https://whop.com/aft-official/the-pendulum-aft/ |
| `midas` | https://whop.com/aft-official/midas-aft/ |
| `relay` | https://whop.com/aft-official/headline-risk-aft/ |
| `slipstream` | https://whop.com/aft-official/slipstream-aft/ |
| `the-alloy` | https://whop.com/aft-official/the-alloy-aft/ |
| `the-assay` | https://whop.com/aft-official/the-assay-aft/ |
| `the-books` | https://whop.com/aft-official/the-books-aft/ |
| `the-bullion` | https://whop.com/aft-official/the-bullion-aft/ |
| `the-fix` | https://whop.com/aft-official/the-fix-aft/ |
| `the-ingot` | https://whop.com/aft-official/the-ingot-aft/ |
| `the-kilo` | https://whop.com/aft-official/the-kilo-aft/ |
| `the-print` | https://whop.com/aft-official/the-print-aft/ |
| `triad` | https://whop.com/aft-official/triad-aft/ |
| `undercurrent` | https://whop.com/aft-official/undercurrent-aft/ |
| `undertow` | https://whop.com/aft-official/the-press-aft/ |

Regenerate with `_work/tools/whop_publish.py` in `Collinshogo/trading-bots`; it writes
`research/products/WHOP_PUBLISH_RESULT.json`, from which this table is copied verbatim.
