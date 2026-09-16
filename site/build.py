"""Build the static site: wraps site/pages/*.html fragments in the shared layout into docs/.

Each page fragment starts with a front-matter block:
<!--
title: Page title
description: One-line description
-->
Run: python site/build.py
"""

import datetime
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = ROOT / "site" / "pages"
OUT = ROOT / "docs"

NAV = [
    ("index.html", "Overview"),
    ("evidence.html", "Evidence"),
    ("hardware.html", "Hardware"),
    ("open-questions.html", "Open questions"),
    ("biological-feedback.html", "Biological feedback"),
    ("diy-biohacking.html", "DIY biohacking"),
    ("ip.html", "IP rights"),
]

LAYOUT = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} · LFU Open Hardware</title>
<meta name="description" content="{description}">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/fonts.css">
<link rel="stylesheet" href="assets/site.css">
<script>try{{var t=localStorage.getItem('theme');if(t)document.documentElement.dataset.theme=t}}catch(e){{}}</script>
</head>
<body>
<header class="top"><div class="in">
<a class="brand" href="index.html"><img src="assets/favicon.svg" alt=""><span>LFU <b>Open</b> Hardware</span></a>
<nav class="main" aria-label="Sections">{nav}</nav>
<button class="theme-btn" type="button" onclick="(function(){{var d=document.documentElement,c=d.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'),n=c==='dark'?'light':'dark';d.dataset.theme=n;try{{localStorage.setItem('theme',n)}}catch(e){{}}}})()" aria-label="Toggle theme">◐</button>
</div></header>
<main>
{body}
</main>
<footer class="site"><div class="in">
<span>A <a href="https://hackingbiology.com" target="_blank" rel="noopener">HackingBiology</a> project · companion to <a href="https://biohack.it" target="_blank" rel="noopener">biohack.it</a></span>
<span><a href="https://github.com/hackingbiology/ultrasound-low-frequency" target="_blank" rel="noopener">Source on GitHub</a> · research notes, not medical advice · built {built}</span>
</div></footer>
</body>
</html>
"""


def parse(text):
    m = re.match(r"\s*<!--(.*?)-->", text, re.S)
    meta = {}
    if m:
        for line in m.group(1).strip().splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
        text = text[m.end():]
    return meta, text.strip()


def main():
    built = datetime.date.today().isoformat()
    for src in sorted(PAGES.glob("*.html")):
        meta, body = parse(src.read_text(encoding="utf-8"))
        nav = "".join(
            f'<a href="{href}"{" aria-current=\"page\"" if href == src.name else ""}>{label}</a>'
            for href, label in NAV
        )
        html = LAYOUT.format(
            title=meta.get("title", src.stem),
            description=meta.get("description", ""),
            nav=nav,
            body=body,
            built=built,
        )
        (OUT / src.name).write_text(html, encoding="utf-8")
        print("built", src.name)
    (OUT / ".nojekyll").write_text("", encoding="utf-8")


if __name__ == "__main__":
    main()
