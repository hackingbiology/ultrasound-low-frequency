# 01 — Source analysis: the UT / Mechanobiologics low-frequency ultrasound (LFU) device

Status: working notes, v0.1 (2026-09-16). Every number below carries its source. Where sources disagree the conflict is shown, not resolved silently.

## 1. Who and what

| Item | Fact | Source |
|---|---|---|
| Origin lab | Michael P. Sheetz (mechanobiology), University of Texas Medical Branch, Galveston. Sheetz is deceased ("the late Michael P. Sheetz"). | [S1], [S5] |
| Company | **Mechanobiologics, Inc.**, Santa Fe NM — "Health & rejuvenation through ultrasound technology"; mechanical treatments for cancer, aging, injury. Contact listed: Linda Kenney. | [S5], TimePie 2026 slides |
| Key paper | Kureel SK, … Sheetz MP. *Rejuvenation of Senescent Cells, In Vitro and In Vivo, by Low-Frequency Ultrasound.* **Aging Cell 2025**, doi:10.1111/acel.70008 (preprint bioRxiv 10.1101/2022.12.08.519320, v1–v4). | [S1], [S2] |
| Related paper | LFU reverses insulin resistance / diabetes-induced muscle transcriptome changes in aged mice. *Am J Physiol Endocrinol Metab* (doi:10.1152/ajpendo.00470.2024). Not yet read (paywall/403). | [S6] |
| IP | US 2024/0001155 A1 and EP 4561696 A1 "Reversal of cellular senescence by treatment with low frequency ultrasound" (inventors Sheetz, Kureel, Margadant; priority 2022-06-30; EP **pending**). Slide: **US Patent 12,714,885 "Systems and Methods for Immersion Mechanotherapy", granted 8/2026**, three more pending (full text not yet retrieved). | [S3], [S4], slide |
| Human trials | (a) **NCT06562374** UTMB Galveston, PI Thomas Blackwell — knee osteoarthritis pilot, n=10, **SUSPENDED by IRB** (2026-03). (b) **NCT07168525** UT Health San Antonio (Barshop Institute), PI Blake Rasmussen, XPRIZE Healthspan collaborator — healthy aging RCT, n=20, age ≥70, sham-controlled, recruiting, primary completion est. 2026-10. | [S7], [S8] |

## 2. Physical parameters — consolidated

| Parameter | Paper (Aging Cell 2025) | Patent US20240001155 | NCT06562374 (OA, human) | NCT07168525 (aging, human) | TimePie slide (mice) |
|---|---|---|---|---|---|
| Frequency | **32.2 kHz** optimal (33 > 39 kHz) | 32.249 kHz; claimed 20–500 kHz | 33 kHz | "low frequency" | 33 kHz |
| Pressure | **4 kPa** (hydrophone) — preprint v2 says "4 Pa" | 6–7 kPa in water; pulses 170 Pa–4.5 kPa+; intensity 1–450 mW/cm², <3 W/cm² | "4–10 Pascals" | n/a | **4–8 kPa** output |
| Duty cycle | 1.5 s on / 1.5 s off | 1.5/1.5 s (also 2–60 s) | **1.6 s / 1.6 s** | n/a | "1.5 s" |
| Session | 30 min | 2 min–2 h; example 30 min | 30 min | **45 min** | 30 min (= 600 pulses) |
| Schedule | mice: daily / every 2nd / every 3rd day; 1×, 1.3×, 2× power | 10 sessions in 1 month; human examples daily ×5 | every 2nd–3rd day | **3×/week × 8 weeks** | — |
| Geometry | target 7–10 cm above transducer (far field); 4 L glass beaker; cylinder 13 cm h × 15.2 cm Ø; plastic mesh | 9–10 cm; frequency sweep / beam steering against standing waves | "generators encased in epoxy within the baths" | bathtub fitted with device | transducer at bottom of water column, mice on wire mesh |
| Water | degassed; 35 °C (cells), 32–35 °C (mice) | degassed, 32–35 °C | — | — | — |
| Drive | not specified | not specified | — | — | **"varying power input 135–275 V"** |
| Calibration | ONDA **MCT-2000** needle hydrophone | — | — | — | — |

### 2.1 The Pa vs kPa conflict — resolved by physics

Plane-wave intensity in water: I = p² / (2ρc), ρc ≈ 1.5 × 10⁶ Rayl (p = peak amplitude).

| p (peak) | I | Consistent with patent 1–450 mW/cm²? |
|---|---|---|
| 4 Pa | ≈ 5 × 10⁻¹⁰ W/cm² | No — below ambient noise, physically meaningless as a stimulus |
| 4 kPa | ≈ 0.53 mW/cm² | Yes (low end) |
| 8 kPa | ≈ 2.1 mW/cm² | Yes |
| 10 kPa | ≈ 3.3 mW/cm² | Yes |

(If the quoted value is RMS rather than peak, intensities double.) **Working target: 4–8 kPa at the target, 32–33 kHz.** The "Pa" in the preprint v2 and the OA trial record is almost certainly a unit typo. Still to confirm: peak vs peak-to-peak vs RMS.

Other derived numbers:
- Wavelength at 33 kHz in water ≈ **4.5 cm**, so a 4 L beaker or a bathtub is only a few wavelengths across. **Standing waves and hot/cold spots are the main reproducibility risk**; the patent mentions frequency sweep / beam steering. Measuring the field (a map, not a single point) is required.
- Mechanical Index ≈ p[MPa] / √f[MHz] = 0.004–0.008 / √0.033 ≈ **0.02–0.04** (diagnostic imaging limit 1.9). Far below inertial-cavitation thresholds for degassed water at 33 kHz. Degassing still matters: at this frequency, gas nuclei *can* cavitate, which changes the dose and adds risk.
- 30 min at a 50% duty cycle gives 900 s of sonication, about 0.5–2 J/cm² of energy crossing the target. Heating is negligible (the 32–35 °C water bath dominates).

## 3. Device architecture (inferred)

Three form factors come from the same physics:

1. **Cell dish** (in vitro): transducer at the bottom of a degassed, 35 °C water tank; dish sealed with parafilm, on a mesh 7–10 cm above.
2. **Mouse beaker**: 4 L glass beaker, transducer at the bottom, mice on a wire mesh half-immersed, 32–35 °C. The sessions are simply "a warm bath for mice".
3. **Human "ultrasound spa"**: bathtub (prototype: a wooden-framed tank in a garage/workshop; later a fiberglass tub). Photo shows **~10–12 transducer heads on articulated arms** around the tub rim, pointing into the water, plus a benchtop generator and laptop. Subject sits immersed. 45 min × 3/week × 8 weeks (RCT).

The claimed feature is multi-transducer immersion with cycled (and probably swept) emission. The US 12,714,885 claims must be read before we design a human-scale version.

Likely hardware class: 135–275 V drive at 33 kHz strongly suggests **Langevin (bolt-clamped sandwich) piezo transducers of the ultrasonic-cleaning / welding type**, driven by a switching generator with an impedance-matching inductor. This is the same component family as industrial ultrasonic cleaners, which is the key to a low-cost build.

## 4. Biological claims (what we will try to measure)

In vitro, after one 30-min LFU session, senescent cells (>90% SA-β-gal+) showed:
- **Growth resumed**: EdU uptake, observed divisions, population doublings up to P24.
- **Markers reversed**: SA-β-gal, p16, p21, cell size, telomere length (increased), 5mC, H3K9me3, γH2AX, nuclear p53, ROS / mitoROS.
- **SASP blocked**: IL-6, IL-8, IL-10, IL-15, TNF-α, IFN-γ, VEGF, MIP-1α. RNA-seq: 50 genes up, 140 down, including IGF2, IGFBP2, FGF7, C1QTNF7.
- **Proposed mechanism**: Ca²⁺ entry → autophagy ↑, mTORC1 ↓, SIRT1 moves from nucleus to cytoplasm; mitochondrial fission ↑.

In vivo (C57BL/6J, started at 22–25 months):
- **Tissue markers**: SA-β-gal-stained area in kidney/pancreas ~70% (sham) vs 10–20% (LFU); lower p16/p21.
- **Activity**: wheel running 7–10× sham at 29 and 32 months.
- **Other function**: treadmill improved in all groups; inverted cling improved in 3 of 5 groups; weight and fur maintained.
- **Lifespan**: D2+D3 groups combined ≈50% survival at 1000 days; **individual groups (n = 7–8) not statistically significant**. No tumors at autopsy.

## 5. Critical assessment

- **Evidence strength**: a single lab. The mouse longevity groups are small, and lifespan is not significant per group. The one human safety pilot (OA) was **suspended by its IRB**; the reason is not public. The healthy-aging RCT (n = 20) has no results yet (est. late 2026). There has been no independent replication. This is exactly the gap an open, reproducible device can fill.
- **Dose ambiguity**: Pa/kPa, peak/RMS and 1.5 vs 1.6 s disagree across sources. Nobody outside the group can currently reproduce "the dose". Our first deliverable should therefore be a **dose definition plus a calibration method**, not a box.
- **Human-trial endpoints are mostly functional**: knee-extension strength, SPPB, TUG, 6MWT, DEXA, cognition. Blood endpoints are "senescence via IHC/biochemistry/RNA-seq" and "immune aging via epigenetics". That is directly relevant to Track B.
- **IP / freedom to operate**:
  - One granted US patent plus a pending US/EP family. Patents are territorial: the EP application is not granted.
  - In Italy, CPI art. 68 exempts private non-commercial acts and experimental use.
  - Publishing an open design is different from selling kits or treatments.
  - **Needs a proper legal check before any distribution; this note is not legal advice.**
- **Regulatory**: the UT trials classify it as a *non-significant-risk* investigational device. In the EU, any therapeutic claim makes it a medical device under the MDR. Position ours as open research hardware.

## 6. Implications for the open build (to discuss)

1. **Start with the mouse/cell geometry as the reference instrument** (one transducer, one beaker, degassed 35 °C water). It is the best-documented configuration and the cheapest to calibrate. Scale up to a limb/foot bath next, and to a full tub last.
2. **Target spec v0**:
   - frequency 32–33 kHz, with optional ±1 kHz sweep;
   - 4–8 kPa at the target plane, 7–10 cm above the transducer;
   - pulsing 1.5 s on / 1.5 s off;
   - 30 min per session;
   - water degassed, 32–35 °C.
3. **BOM hypothesis** (prices and availability still to verify):
   - a 33 kHz (or 28/40 kHz for tests) Langevin cleaning transducer;
   - an off-the-shelf digital ultrasonic generator board with frequency tracking/sweep, or a DIY half-bridge driver plus matching inductor under microcontroller control for exact gating;
   - a thermostat heater;
   - a degassing method (boil-and-cool or vacuum).
4. **Calibration**: build a DIY PZT hydrophone and calibrate it once against a reference hydrophone (ONDA-class) at a university lab. Map the field in 3D to find hot spots. Publish the map with every build.
5. **Track B endpoints** should mirror NCT07168525 so our data are comparable: functional (grip, knee strength, SPPB/TUG/6MWT), body composition, epigenetic clock, plus local-lab inflammatory/SASP proxies.

## 7. Open questions / to retrieve

- [ ] Full text + claims of **US 12,714,885** and the three pending applications (transducer layout, sweep, control).
- [ ] Aging Cell **Supplementary Fig. S1** (setup schematic) and methods supplement: transducer/generator models.
- [ ] AJP-Endo diabetes paper (parameters, blood/metabolic markers).
- [ ] bioRxiv v1→v4 diff on the pressure units.
- [ ] Reason for the IRB suspension of NCT06562374.
- [ ] Mechanobiologics tumor-cell paper (PubMed 40060768), the same apparatus family.
- [ ] Slide set from TimePie 2026 (Fabio): any more parameter slides?

## Sources

- [S1] Kureel et al., Aging Cell 2025 — https://pmc.ncbi.nlm.nih.gov/articles/PMC12151899/ · https://onlinelibrary.wiley.com/doi/10.1111/acel.70008
- [S2] bioRxiv 2022.12.08.519320 — https://www.biorxiv.org/content/10.1101/2022.12.08.519320v4.full
- [S3] US20240001155A1 — https://patents.google.com/patent/US20240001155A1/en
- [S4] EP4561696A1 — https://patents.google.com/patent/EP4561696A1/en
- [S5] Mechanobiologics — https://www.mechanobiologics.com
- [S6] AJP Endocrinology & Metabolism — https://journals.physiology.org/doi/full/10.1152/ajpendo.00470.2024
- [S7] NCT06562374 — https://clinicaltrials.gov/study/NCT06562374
- [S8] NCT07168525 — https://clinicaltrials.gov/study/NCT07168525 · UT Health XPRIZE news: https://news.uthscsa.edu/ut-health-san-antonio-team-named-xprize-healthspan-semifinalist/
- TimePie Longevity Forum 2026 (Shanghai), Mechanobiologics talk — slide photos kept privately (not redistributed).
