# ultrasound-low-frequency

**Site: https://hackingbiology.github.io/ultrasound-low-frequency/**

Open-hardware, open-source, **reproducibility-first** low-frequency ultrasound (LFU) device for DIY biohacking research on cellular senescence — and a protocol to measure its biological effects on yourself. A [HackingBiology](https://hackingbiology.com) project, companion to [biohack.it](https://biohack.it).

The goal is to rebuild, as cheaply and as reproducibly as possible, the class of device described in University of Texas mechanobiology research (Sheetz lab / Mechanobiologics): about 33 kHz, 4–8 kPa, pulsed 1.5 s on/off, 30 min per session, delivered by immersion in warm degassed water — with a published calibration so that other people can build their own and know they are delivering the same dose.

> **Research hardware. Not a medical device. Nothing is sold.** No therapeutic claim is made. The evidence is preclinical and comes from a single lab, and the long-term safety of reversing cellular senescence in humans is unknown — including its oncogenic risk. See the [DIY biohacking](https://hackingbiology.github.io/ultrasound-low-frequency/diy-biohacking.html) and [IP](https://hackingbiology.github.io/ultrasound-low-frequency/ip.html) pages.

## Sections of the site

| Page | Contents |
|---|---|
| [Overview](https://hackingbiology.github.io/ultrasound-low-frequency/) | Goals, roadmap, the path from the first build to many self-built kits |
| [Evidence](https://hackingbiology.github.io/ultrasound-low-frequency/evidence.html) | Papers, trials, consolidated parameters, source conflicts |
| [Hardware](https://hackingbiology.github.io/ultrasound-low-frequency/hardware.html) | Three architectures with pros/cons and block diagrams, dose definition, acceptance test |
| [Open questions](https://hackingbiology.github.io/ultrasound-low-frequency/open-questions.html) | What we need from Mechanobiologics / UT to reproduce the exposure |
| [Analyze biological feedback](https://hackingbiology.github.io/ultrasound-low-frequency/biological-feedback.html) | Crosswalk of what they measured vs what we can; markers, kits, Italian labs, n-of-1 design |
| [DIY biohacking](https://hackingbiology.github.io/ultrasound-low-frequency/diy-biohacking.html) | Potential benefits, potential risks, exclusions, house rules |
| [IP rights](https://hackingbiology.github.io/ultrasound-low-frequency/ip.html) | Patent landscape, claim analysis, what a non-commercial DIY project may and may not do |

## Repository layout

```
docs/            published site (GitHub Pages, /docs on main) + docs/research/*.md working notes
site/pages/      page fragments with front matter; files starting with _ are includes
site/build.py    static builder: python site/build.py
```

Research notes: [01 source analysis](docs/research/01-source-analysis.md) · [02 review of a prior ChatGPT analysis](docs/research/02-chatgpt-analysis-review.md) · [03 IP analysis](docs/research/03-ip-analysis.md) · [04 biomarkers and Italian lab availability](docs/research/04-biomarkers-italy.md) (Italian) · [05 hardware and primary sources](docs/research/05-hardware-and-sources.md) · [06 electrical safety](docs/research/06-electrical-safety.md). Outreach draft: [enquiry to Mechanobiologics and UT](docs/outreach/mechanobiologics-enquiry.md).

## License

Multi-licensed by content type — see [LICENSE.md](LICENSE.md):
**CERN-OHL-S-2.0** (hardware) · **AGPL-3.0-only** (software/firmware) · **CC BY-SA 4.0** (documentation and data).

These licences grant no rights under third-party patents; see [the IP page](https://hackingbiology.github.io/ultrasound-low-frequency/ip.html).
