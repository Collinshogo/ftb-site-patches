#!/usr/bin/env python3
"""Apply Whop checkout links to the site catalog (site-session side; no access to the private repo needed).
Usage, from the goal33-site clone root:  python3 <patches>/apply_whop_links.py <patches>/data/whop_links.json
whop_links.json = {"<slug>": {"id": "prod_...", "url": "https://whop.com/<store>/<route>/"}, ...} — written by the Whop
publisher (research repo, _work/tools/whop_publish.py) and copied here verbatim. Slugs are the site catalog slugs.
Bundles: "the-books" -> bundles.books_all.whop, "all-access" -> bundles.all_access.whop.
Then regenerate: python3 _tools/rebuild_index.py && python3 _tools/gen_pages.py && python3 _tools/gen_plan.py
A slug in the file that is not in the catalog is reported and skipped; a catalog product with no link keeps its own page as the buy target."""
import json, sys
links = json.load(open(sys.argv[1]))
cat = json.load(open("_tools/catalog2.json"))
seen = set()
for p in cat["strategies"]:
    l = links.get(p["slug"])
    if l and l.get("url"):
        p["whop"] = l["url"]; seen.add(p["slug"]); print(f"  {p['slug']:14} -> {l['url']}")
for slug, key in (("the-books", "books_all"), ("all-access", "all_access")):
    l = links.get(slug)
    if l and l.get("url"):
        cat["bundles"][key]["whop"] = l["url"]; seen.add(slug); print(f"  {slug:14} -> {l['url']}")
missing = [s for s in links if s not in seen]
if missing: print("  !! not in catalog, skipped:", ", ".join(missing))
json.dump(cat, open("_tools/catalog2.json", "w"), indent=2, ensure_ascii=False)
print(f"applied {len(seen)} links; now regenerate the pages")
