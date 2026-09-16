# 06 — Electrical and thermal safety standards for a human-immersion 33 kHz bath

Working notes, 2026-09-16. **Not engineering sign-off.** Compiled with AI assistance from public sources; several figures are flagged as unverified. A real human-scale build needs a qualified electrical engineer and, if anything is ever supplied to another person, a regulatory advisor.

Legend: **[F]** sourced fact · **[I]** inference · **[?]** could not verify.

## 0. The framing conclusion

**No product standard covers this device.** A bathtub with 150–300 L of water, a fully immersed person, and 8–16 energised 33 kHz transducers in the water falls between:

- **IEC 60601-2-5** (ultrasonic physiotherapy) — nearest particular standard, but its scope is "a *single* plane unfocused circular transducer per treatment head, producing *static* beams", and its conformity tests route through **IEC 61689, whose range is 0.5–5 MHz** [F]. 33 kHz is a factor of 15 below that floor.
- **IEC 60335-2-60** (whirlpool baths/spas) — **explicitly excludes "appliances intended for medical purposes"** [F].
- **IEC 60364-7-701 / -702** (installation zones for baths and pools) — applies to the installation, and permits **only 12 V a.c. / 30 V d.c. SELV** for anything a person in the water can touch [F].

## 1. IEC 60601-1 — general medical electrical safety

### Applied-part types
- **B**: earth-referenced. **BF**: floating (galvanically isolated). **CF**: floating, cardiac-grade. [F]
- **[I]** A transducer in galvanic contact with the bather's water is an *applied part*, and here the "applied part" is a ~200 L conductive volume surrounding the torso. Classify **BF at minimum**; design to CF leakage numbers.

### Leakage-current limits (normal condition / single-fault) [F]
| Test | Type B | Type BF | Type CF |
|---|---|---|---|
| Earth leakage (3rd ed. general) | 5000 / 10 000 µA | same | same |
| Touch (enclosure) current | 100 / 500 µA | 100 / 500 | 100 / 500 |
| **Patient leakage (a.c.)** | 100 / 500 µA | 100 / 500 µA | **10 / 50 µA** |
| Mains on applied part (SFC) | n/a | 5000 µA | 50 µA |
| Patient auxiliary (a.c.) | 100 / 500 µA | 100 / 500 | 10 / 50 |

d.c. patient leakage **10 µA NC** for all types [F]; 50 µA SFC is the standard pairing **[?]**.
Sources disagree on earth leakage (5/10 mA in 3rd ed. vs 500 µA/1 mA quoted by some vendors) — the 5/10 mA figures are better supported [F].

**Frequency scaling [?]** — one secondary source states patient-auxiliary current is limited to 100 µA from 0.1 Hz–1 kHz, then **100·f µA (f in kHz) up to 100 kHz**, i.e. ~**3.3 mA at 33 kHz**. Verify clause 8.7.3 before relying on it. **[I]** If true, 60601-1 leakage rules barely constrain the drive frequency, and the real constraints come from the installation standards.

### MOP / MOPP at 250 V working voltage, pollution degree 2, material group II/IIIa [F]
| | Dielectric withstand | Creepage | Clearance |
|---|---|---|---|
| 1 × MOOP | 1500 V a.c. | 2.5 mm | — |
| 2 × MOOP | 3000 V a.c. | 5 mm | — |
| 1 × MOPP | 1500 V a.c. | 4.0 mm | 2.5 mm |
| **2 × MOPP** | **4000 V a.c.** | **8.0 mm** | **5.0 mm** |

Caveats [F/I]: these assume pollution degree 2 — a wet-environment product would plausibly be assessed at **pollution degree 3** (IEC 60335-2-60 clause 29.2 declares whirlpool baths PD3 unless insulation is enclosed), which increases creepage. Altitude increases clearance. The 2020 revision's tables are stricter **[?]**.

## 2. IEC 60601-2-5 — ultrasonic physiotherapy (numbers worth copying anyway)

From the 2000 edition (via its identical Chinese adoption GB 9706.7-2008) and the 2009 3rd-edition preview [F]:

| Clause | Requirement |
|---|---|
| 35 | Unwanted side radiation from a hand-held head < **100 mW/cm²** (degassed water, 22 ± 3 °C) |
| 42.3 item 7 | Heads for use in water only: **15 min fully immersed at rated power** |
| 42.3 item 8 | **Radiating-surface temperature ≤ 41 °C** |
| 44.6 101 | Treatment head **IPX7** |
| 50.1.103 | Power indication accurate to **±20%** |
| 51.5 | Effective intensity **≤ 3 W/cm²**, normal *and* single-fault |
| 51.101 | Output control must reach **< 5% of rated power** |
| 51.103 | Timer range **≤ 30 min**, defined accuracy |
| 51.104 | **Beam non-uniformity ratio ≤ 8.0** |
| 51.105 | Output stable within ±20% over 1 h at max output |
| 56.3 aa) | **Bend protection at the treatment-head cable entry** |
| 6.8.2 aa) 3) | Instructions must emphasise, **where the applied part is Type B, the hazards from improper electrical installation** |

Definitions: ERA = beam cross-section at 0.3 cm from the face × 1.354; effective intensity = P / ERA; BNR = peak pressure² / spatial mean pressure² over the ERA. The standard defines ultrasound as above ~16 kHz and requires marking in kHz below 1 MHz, so 33 kHz is *nominally* in scope but *practically* unverifiable under it. [F/I]

## 3. Installation standards: the water rules

### IEC 60335-2-60 (whirlpool baths) [F]
- Portable appliances **class II or III**; whirlpool baths **≥ IPX5**.
- 8.1.4: **any energised part is considered a live part** (the SELV exemption is removed).
- 11.8: water at the bath inlet **≤ 50 °C** if a heating element is fitted.
- **22.35: parts accessible to the user in the bath shall only be supplied at SELV not exceeding 12 V.**
- 24.101: thermal cut-outs used for compliance **shall not be self-resetting**.
- 24.102: class III needs a safety isolating transformer rated at least IPX4.
- 25.1 / 27.2: class I permanently connected, with an external equipotential bonding terminal.
- 7.12.1: live parts other than ≤12 V SELV must be **inaccessible to a person in the bath**; supply through an RCD **≤ 30 mA**.

### IEC 60364-7-702 (pools) and -701 (bathrooms) [F]
| Zone | Extent | Max SELV | IP |
|---|---|---|---|
| 0 | Inside the basin | **12 V a.c. / 30 V d.c.** | IPX8 (pools), IPX7 (baths) |
| 1 | 2.0 m horizontally / 2.5 m vertically (pools) | 25 V a.c. / 60 V d.c. | IPX4–5 |
| 2 | +1.5 m | — | IPX2–5 |

- The **safety source must be outside zones 0, 1 and 2**.
- **Supplementary equipotential bonding** of all extraneous conductive parts in zones 0–2; **2.5 mm² sheathed / 4 mm² unsheathed** copper.
- 30 mA RCD; the pool section notes "for swimming pools for medical use, special requirements may be necessary".

## 4. Why no RCD protects the bather

- **Thresholds** [F]: IEC personnel RCDs are 30 mA (10 mA available); US Class A GFCIs trip at 4–6 mA with an inverse-time curve (≈5.6 s at 6 mA, ≈1.0 s at 20 mA, ≈100 ms at 100 mA). General RCDs may take up to **300 ms**.
- **Physiology** [F], IEC 60479-1: perception from 0.5 mA; **let-go ~5 mA** for exposures > 6 s; ~40 mA for > 2 s can cause ventricular fibrillation. The data is valid **15–100 Hz**, with body-impedance data only to **20 kHz** — 33 kHz is outside the standard entirely.
- **Immersion** [I]: removes the skin barrier over the whole body; what remains is internal impedance of a few hundred ohms, and the current path is set by the field geometry in the water. This is why the installation standards cap in-water parts at 12 V.
- **Electric shock drowning** [F]: low-level a.c. causes skeletal muscular paralysis in **fresh** water, leading to drowning; salt water is safer because it shunts current around the body. Marina standards allow only 4–30 mA of leakage before tripping.
- **Frequency** [F/I]: Type AC/A/F/B RCDs — only Type B covers smooth d.c., and IEC 62423 characterises Type B operation only **up to 1000 Hz**. A 33 kHz residual component is outside every device's tested range, and smooth d.c. can magnetically blind Type A/AC devices.

**[I] Conclusion: protection must come from galvanic isolation and construction, with insulation monitoring as the fault detector, not from residual-current tripping.**

## 5. The architecture that follows [I, built on F]

1. Mains → transformer with **2 × MOPP**, safety source outside the wet zones.
2. **Floating secondary**; nothing in the water bonded to protective earth (the medical IT-system model of IEC 60364-7-710, where a first fault does not create a shock path and an **insulation monitoring device** alarms on degraded insulation rather than disconnecting — threshold commonly ~50 kΩ, transformers deliberately small, 3.15–10 kVA **[?]**).
3. **SELV along the cable; step-up inside the potted head.** The installation rules cap in-water parts at 12 V a.c. / 30 V d.c., but a Langevin transducer wants 100–275 V. Carrying SELV to the head and doing the step-up and resonant matching *inside* the sealed assembly is the way to satisfy both.
4. **Neutral-generator topology** (from WO 2020/223359): arrays with net-zero feed voltage, alternating coil direction or inverted piezo crystals.
5. **IPX7/IPX8 potting, double insulation, bend protection at the gland.** With 8–16 immersed heads the failure rate is multiplied; the 33 kHz drive is a fatigue mechanism at the potting interface, and potting compounds absorb water over years. A wear-out mechanism, not a one-shot failure.
6. **Supplementary equipotential bonding** of everything reachable.
7. A **Type B RCD upstream of the isolating transformer** as a backstop for the mains-side wiring only — it protects the installation, not the bather.

## 6. Thermal limits and fail-safes

- **Water ≤ 40 °C** (consumer hot-tub ceiling); ~37.8 °C considered safe for a healthy adult; above body temperature the hazard is drowsiness → unconsciousness → drowning. Hot-tub thermostats may err by up to ~2 °C, so measure independently. [F]
- **Pregnancy**: water above ~38.9 °C can cause fetal damage in the first trimester; core temperature should stay below ~38.3–39.0 °C; epidemiological data associates hot-tub use with substantially increased miscarriage risk. **Absolute exclusion.** [F]
- **Heater inlet ≤ 50 °C**; **transducer radiating surface ≤ 41 °C** after 15 min immersed at rated power. [F]
- **Two independent layers**: control thermostat plus a separate **non-self-resetting** thermal cut-out that kills heater and transducers independently of the controller; two sensors with disagreement detection; a failed sensor reads as over-temperature. [F/I]
- **Hard session timer** regardless of temperature. Bulk water temperature is not a proxy for tissue temperature near a transducer face — a 12 W head deposits ~12 kJ in 15 minutes and needs agitation to spread it. [F/I]

## 7. Not verified, flagged

- Exact ohm values of IEC 60479-1 Tables 1–3 (dry / water-wet / saltwater-wet body impedance).
- The 50 µA SFC d.c. patient-leakage figure.
- The 60601-1 frequency-scaling clause for patient leakage above 1 kHz (~3.3 mA at 33 kHz).
- The IEC 62127-1 lower frequency bound.
- IEC 60364-7-701 zone-1 SELV limit (sources conflict: 12 V vs 25 V a.c.).
- IEC 60364-7-710 insulation-monitor threshold and transformer kVA range.
- Quantitative in-water incapacitation currents — chase the NFPA Fire Protection Research Foundation report on hazardous voltage/current in marinas and Rifkin & Shafer (2008), *In-Water Shock Hazard Mitigation Strategies*.

## Sources

IEC 60601-1 leakage and MOPP tables via ebme.co.uk, Advanced Energy, Avnet Abacus, Rigel Medical · IEC 60601-2-5:2000 full text via GB 9706.7-2008 (cmde.org.cn) and the IEC 60601-2-5:2009 official preview · IEC 61689 and IEC 61161 scopes via the IEC webstore · IEC 60335-2-60:2002 full text (PDF) and the ed. 4.0 VDE preview · IEC 60364-7-702:1997 preview (normservis.cz) and BS 7671 section guides (Elec-Mate) · IEC 60479-1 thresholds via EMF-Portal (Figure 20) and the ed. 4.1 VDE preview · IEC 62423 via the TISI reprint · electric shock drowning via ESDPA and Robson Forensic · hot-tub temperature via US CPSC guidance · medical IT systems / IEC 60364-7-710 via secondary technical sources.
