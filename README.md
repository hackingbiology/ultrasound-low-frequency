# ultrasound-low-frequency

Open-hardware, open-source, **reproducibility-first** low-frequency ultrasound (LFU) device for research on cellular senescence. It is a [HackingBiology](https://hackingbiology.com) project, companion to [biohack.it](https://biohack.it).

The goal is to rebuild, as cheaply as possible and with a published dose calibration, the class of device described by the University of Texas mechanobiology work (Sheetz lab / Mechanobiologics): about 33 kHz, 4–8 kPa, pulsed 1.5 s on/off, 30 min per session, delivered by immersion in warm degassed water. We then measure senescence-related biomarkers before and after.

> **Research hardware. Not a medical device.** No therapeutic claim is made. See `docs/research/01-source-analysis.md` §5 for evidence strength, IP and regulatory notes.

## Tracks

- **A — Device**: reverse-spec → architecture → bench prototype → acoustic calibration → safety envelope → reproducibility kit.
- **B — Measurement**: before/after protocol with blood/urine markers from a local lab, plus functional endpoints aligned with the UT trials.

## Documents

- [01 — Source analysis](docs/research/01-source-analysis.md): papers, patents, trials, and consolidated parameters.

## License

To be decided (proposed: CERN-OHL-S-2.0 for hardware, AGPL-3.0 for firmware/software, CC BY-SA 4.0 for docs).
