# STATE — where the project is

Last updated: 2026-10-21. Keep this file current; it is the first thing read when the project is picked up on another machine.

## Phase

**Research and design complete enough to start building. Nothing has been built or measured yet.**

The site documents: the evidence and its contradictions, three hardware architectures with costed bills of materials, the acoustic and electrical safety analysis, the IP landscape, the measurement plan, and the testing path. No transducer has been bought.

## Decisions already taken — do not re-open without a reason

| Decision | Date | Rationale lives in |
|---|---|---|
| Own public repo under the `hackingbiology` org | 2026-09-16 | — |
| Licences: CERN-OHL-S-2.0 (hardware), AGPL-3.0-only (code), CC BY-SA 4.0 (docs and data) | 2026-09-17 | [LICENSE.md](../LICENSE.md) |
| Dose target v0: 32.2–33 kHz, **4–8 kPa peak**, 1.5 s on / 1.5 s off, 30 min, degassed water 32–35 °C, target 7–10 cm from the transducer | 2026-09-16 | [hardware #dose](https://hackingbiology.github.io/ultrasound-low-frequency/hardware.html#dose) |
| Architecture **B** (open driver + stock Langevin) is the reference build; A is a practice bench; C is last | 2026-09-16 | [hardware](https://hackingbiology.github.io/ultrasound-low-frequency/hardware.html) |
| Target the **bathtub already at home**, as a removable battery-powered retrofit — not a purpose-built tub | 2026-09-17 | [home-bathtub](https://hackingbiology.github.io/ultrasound-low-frequency/home-bathtub.html) |
| **Hand first**: one hand treated, the other as control, blinded, crossover — this is the first real experiment | 2026-10-14 | [hand-first](https://hackingbiology.github.io/ultrasound-low-frequency/hand-first.html) |
| Hand, not foot; **non-invasive measures only for now** (paired skin biopsies deferred) | 2026-10-14 | idem |
| Cancer / tumour apoptosis stays **out of scope as a purpose**; the cancer assay is used only as a biological dosimeter with a partner lab | 2026-10-12 | [cancer-branch](https://hackingbiology.github.io/ultrasound-low-frequency/cancer-branch.html) |
| No sales, no kits, no treatments, no medical claims | 2026-09-16 | [ip](https://hackingbiology.github.io/ultrasound-low-frequency/ip.html) |

## The five findings that drive everything

1. **The published dose is ambiguous by a factor of 1000.** The preprint, the figure axes and one trial registration say "Pa"; the journal version says "kPa". Physics and the sister lab's interferometry support kPa, so we build to 4–8 kPa — and instrument well enough to detect if it was really Pa.
2. **The instrument in the paper is not a hydrophone.** The Onda MCT-2000 is a cavitation meter reporting a time-averaged total pressure, whose kPa scale needs a self-calibration the paper never mentions. Their own field map is in millivolts, with a ninefold spread across the sample plane.
3. **The window is narrow.** Dose ladder: 2–5 kPa grows cells, 4–8 rejuvenates, 10–20 kills normal stem cells, ~34 kills tumour cells, ~70 made mouse tumours grow *faster* than controls. Our target and the tumour-killing dose are only 12–18 dB apart — less than the error of an uncalibrated hydrophone.
4. **No RCD protects a person in water**, and no RCD type is characterised above 1 kHz. Protection must come from a floating supply, SELV along the cable with the step-up sealed inside the potted head, and insulation monitoring.
5. **The exposure sits 12–18 dB above the ACGIH waterborne limit**, whose evidence base is tinnitus. Hearing is the live human risk, not tissue damage — hence head out of the water.

## Next steps, in order

1. **Send the outreach emails** — drafted in [docs/outreach/mechanobiologics-enquiry.md](outreach/mechanobiologics-enquiry.md), awaiting the owner's review. Record answers against their question IDs on the open-questions page, with date and source.
2. **Buy and characterise transducers**: 5–10 × BJC-3360T-48HS at about $8.50, then measure |Z| vs frequency on a NanoVNA *before* anything else — that measurement decides between the €150 and the €1,600 driver tier.
3. **Calibration path**: find a lab with a hydrophone calibrated at 32 kHz (only NPL in the UK and VNIIFTRI hold a recognised capability at this frequency; Onda calibrates commercially). Buy one passive reference, then transfer-calibrate.
4. **Bench rig** on a 4 L beaker: driver, gating, degassing, field map, cavitation detection, acceptance test.
5. **Hand study**: build the two-basin rig, pre-register the protocol, recruit a third party for randomisation and blinding.
6. Partner lab for the in-vitro arm (oncogenic safety + biological dosimeter). Not started.

## Open threads

- No reply yet from Mechanobiologics or UT Health San Antonio (not yet contacted).
- Research note 07 for the cancer branch was never written — its verified numbers live directly on the cancer-branch page instead.
- A few figures in the research notes are flagged unverified; they are marked inline.
- **Blocked sources are blocked by bot protection, not by IP** (checked 2026-11-24 through a residential-IP tunnel): `register.epo.org` returns 403 with a JavaScript challenge, `patents.justia.com` returns 403, and Google Patents still 404s US 12,714,885. A different exit IP does not help, so do not spend a shared residential line on them. The remaining routes for the docket items (W1–W4) are: EPO OPS with credentials, USPTO Patent Center, or a real browser session — not plain `curl`.

## Environment

The project moved from a Windows laptop to server sd-172212 on 2026-11-17 and survived it unchanged, because a clone is all it needs. It lives at `/home/ubuntu/progetti/ultrasound-low-frequency`, owned by `ubuntu`. Nothing else is required: no services, no cron, no database.

## How to resume on another computer

```bash
git clone https://github.com/hackingbiology/ultrasound-low-frequency.git
cd ultrasound-low-frequency
python site/build.py          # must produce zero diff in docs/
```

Then read `CLAUDE.md`, this file, and `docs/memoria-claude/`. Nothing else is needed: no secrets, no local databases, no server. The only thing not in the repo is a folder of third-party conference photographs, which nothing depends on.
