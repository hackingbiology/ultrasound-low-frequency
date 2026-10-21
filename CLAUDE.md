# CLAUDE.md — working conventions for this repository

Read this first. Everything needed to resume this project lives in the repository: **a `git clone` is sufficient.** Nothing is stored only on one machine except the private material listed at the bottom.

## Where the state is

| File | What it holds |
|---|---|
| **[docs/STATE.md](docs/STATE.md)** | **Start here.** Current phase, decisions already taken, what is next, what is deliberately out of scope |
| [docs/memoria-claude/](docs/memoria-claude/) | Mirror of Claude's own memory note for this project — the condensed findings, kept in sync by hand |
| [docs/research/](docs/research/) | The long working notes (sources, IP, biomarkers, hardware, electrical safety) |
| [README.md](README.md) | What the project is, the site map, licensing |

## What this project is

An open-hardware, non-commercial, reproducibility-first replication of the ~33 kHz low-frequency ultrasound work of the Sheetz lab / Mechanobiologics, plus the measurement protocol to tell whether anything happened. Published as a static site.

**Hard boundaries, not up for re-litigation** (they are reasoned out in `docs/STATE.md` and on the site):
- No kits, boards or devices are sold or shipped. Builders buy their own parts.
- No treatments offered to anyone, no medical claims anywhere.
- Cancer stays out of scope as a purpose — the only granted patent covers exactly tumour apoptosis.
- Every number on the site carries its source, and conflicts between sources are shown rather than resolved silently.

## The site

Static, no framework, no dependencies beyond the Python standard library.

```bash
python site/build.py      # rebuilds docs/ from site/pages/
```

- `site/pages/*.html` are page fragments with a front-matter comment (`title:`, `description:`).
- Files starting with `_` are **fragments**, not pages: they are pulled in with `<!--include: _name.html -->`.
- `site/meta.json` holds the date shown in the footer. **Bump it by hand** when publishing a meaningful update — it is deliberately not `today()`, so that rebuilds are byte-identical and CI can verify `docs/` is in sync.
- `docs/` is the published output and **is committed**. GitHub Pages serves it from `main` → `/docs`.
- Styling lives in `docs/assets/site.css`; the Jost font is embedded base64 in `docs/assets/fonts.css` (copied from biohack.it), so the site has no external dependency except Google-free fonts already inlined.

After editing any page: **rebuild, then commit both `site/pages/` and `docs/`.** A CI workflow fails the push if they diverge.

## House style for the content

- English on the site and in the repo; the project owner writes in Italian, so replies in chat are in Italian.
- Verify numbers against the primary source before publishing them. Several figures circulating about this work are wrong, including in the papers themselves (the Pa/kPa ambiguity, the "needle hydrophone" that is a cavitation meter).
- Mark anything unverified as unverified, inline. Never launder a guess into a fact.
- Negative and inconvenient results are published too — the largely negative diabetes paper, the mouse tumours that grew faster at high power, the embryo mortality. That is the point of the project.

## Private material, deliberately not in the repo

- **TimePie 2026 conference slide photographs**: `C:\Users\admin\hackingbiology-refs\lfu-timepie-2026\` on the owner's machine. Third-party content, not ours to redistribute. Everything they show is reproduced as text and data on the Evidence page, so the repo does not depend on them.
- Journal PDFs are never committed; cite by DOI or PMC link instead.

## Related

Sibling project: [biohack.it](https://biohack.it) (`hackingbiology/biohackit`) — the protocol and biomarker platform this feeds into.
