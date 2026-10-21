"""Sanity checks on the built site. No dependencies; exits non-zero on failure.

Checks:
  1. every internal link and anchor target resolves
  2. every page is reachable from the navigation
  3. no leftover include directives or placeholder text
  4. the research notes and outreach files referenced from the site exist

Run: python tools/check_links.py
"""

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

errors = []
pages = sorted(p for p in DOCS.glob("*.html"))
names = {p.name for p in pages}

if not pages:
    sys.exit("no built pages found in docs/ — run python site/build.py")

ids_by_page = {}
for page in pages:
    html = page.read_text(encoding="utf-8")
    ids_by_page[page.name] = set(re.findall(r'id="([^"]+)"', html))

for page in pages:
    html = page.read_text(encoding="utf-8")

    for directive in re.findall(r"<!--\s*include:[^>]*-->", html):
        errors.append(f"{page.name}: unexpanded include {directive}")

    for placeholder in ("TODO", "TKTK", "lorem ipsum"):
        if placeholder in html:
            errors.append(f"{page.name}: contains placeholder text {placeholder!r}")

    for href in re.findall(r'href="([^"]+)"', html):
        if href.startswith(("http://", "https://", "mailto:")):
            continue
        target, _, anchor = href.partition("#")
        if not target:  # same-page anchor
            if anchor and anchor not in ids_by_page[page.name]:
                errors.append(f"{page.name}: anchor #{anchor} does not exist on this page")
            continue
        if target.endswith(".html"):
            if target not in names:
                errors.append(f"{page.name}: link to missing page {target}")
            elif anchor and anchor not in ids_by_page[target]:
                errors.append(f"{page.name}: link to {target}#{anchor} -> anchor missing")
        else:
            if not (DOCS / target).exists():
                errors.append(f"{page.name}: link to missing file {target}")

nav_targets = set(re.findall(r'<nav class="main"[^>]*>(.*?)</nav>',
                             (DOCS / "index.html").read_text(encoding="utf-8"), re.S))
nav_links = set(re.findall(r'href="([^"]+\.html)"', "".join(nav_targets)))
for page in pages:
    if page.name not in nav_links:
        errors.append(f"{page.name}: built but not present in the navigation")

if errors:
    print("FAILED:")
    for e in errors:
        print("  -", e)
    sys.exit(1)

print(f"OK: {len(pages)} pages, links and anchors resolve, all pages in the navigation.")
