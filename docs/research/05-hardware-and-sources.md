# LFU (low-frequency ultrasound) senescence device — source recovery + hardware replication research

Date: 2026-09-16. Encoding: UTF-8.
Scope: (Part 1) recovery of primary sources on the Sheetz lab / Mechanobiologics LFU device; (Part 2) market/component research for three replication architectures + calibration, plus physics sanity checks.

Legend: ✅ = verified from primary source retrieved this session (raw file kept in the scratchpad `lfu/` folder); ⚠️ = unverified / recalled / secondary; 🔧 = my own calculation or engineering judgement.

---

# PART 0 — EXECUTIVE SUMMARY OF WHAT CHANGED

1. ✅ **The "ONDA MCT-2000 hydrophone" is not a hydrophone.** It is the **Onda MCT-2000 *cavitation meter*** (ondasonics.com), used with an **HCT-series cleaning-tank hydrophone** probe. Its sibling MCT-1200 datasheet states the measured parameters are "Fundamental Frequency F0 (kHz)" and **"Total Pressure, PTOT (kPa or unitless) * — *kPa units require self-calibration to absolute reference"**, with a **1–60 s time-averaging interval** and a useful hydrophone range of **20–1200 kHz**. Three consequences:
   - the reported "4 kPa" is a **broadband, time-averaged total pressure reading of a cleaning-tank meter**, not a calibrated peak-negative pressure. Peak vs RMS is therefore **neither** in the classical sense: closest interpretation is a *time-averaged total (RMS-like) pressure*, over 1–60 s, including harmonics.
   - if the lab never performed the "self-calibration to an absolute reference", the meter reads in **arbitrary units** — which is consistent with their Figure S1B heat map being labelled in **mV (<20 mV … ~180 mV)** rather than kPa.
   - a replication that measures with a *calibrated* hydrophone + oscilloscope will not automatically be measuring the same quantity as they did.
2. ✅ **Units in the literature are genuinely inconsistent: Pa vs kPa.** bioRxiv v2/v3/v4 and the authors' own figure axis labels say **"4 Pa" / "2.2 pa_33" / "8pa"**; the published Aging Cell paper says **"4 kPa"**; the patent says **"6–7 kilopascal"** *and* in one place "3.5–4 Pa"; the UTMB osteoarthritis trial registration says **"4–10 Pascals"**. 🔧 Physics (below) says the effect-relevant number must be **kPa**: 4 Pa corresponds to ~13 **picometres** of particle displacement and ~5×10⁻¹⁰ W/cm², which is below ambient lab noise; 4 kPa gives ~13 nm, matching the 11–65 nm surface displacements independently measured by the Tijore lab at 1–5 kPa.
3. ✅ **Actual transducer hardware is now known** for two branches of this work:
   - Sheetz/Singapore branch (Tijore et al.): **Beijing Ultrasonic PZT4 piezoceramic rings, 25×10×4 mm and 16×8×4 mm**, with an **aluminium cone** to widen the field to ~5 cm and "attenuate the amplitude to form plane waves", **epoxy + silicone-rubber coated**, glued to the tank bottom, "signal generator & amplifier" outside, sample 8 cm above.
   - Tijore's own lab (IISc, 2026 papers): **APC International Langevin transducer APC 90-4050**, bonded with high-strength epoxy to a steel container, driven by a **PiezoDrive PDU 210 ultrasound driver**, calibrated with an **impedance analyser**, pressure measured with a **FEL Communications hydrophone** into a **Digilent 410-321 (Analog Discovery 2) USB oscilloscope**, 3D-printed dish holder with height adjustment, vacuum-degassed water. **This is a directly copyable architecture.**
4. ✅ **The human bathtub is patented**: WO2020223359A1 / US20220047894 "Systems and Methods for Immersion Mechanotherapy", Mechanobiologics LLC (Margadant, Kenney, Sheetz) — bathtub with transducers on bottom + side walls, **robotic/articulated arm carrying transducers**, phased arrays, **"neutral generator" with net-zero feed voltage / inverted piezo crystals for shock safety**, cone-shaped reflective interior wall, foam/sponge absorbers to kill standing waves, **95–105 °F** water, chlorination, proximity sensors.
5. ✅ **The osteoarthritis trial (NCT06562374, UTMB) is currently SUSPENDED.** Its device text is the source of the "33 kHz, 4–10 Pascals, 1.6 s on / 1.6 s off, generators encased in epoxy within the baths" wording.
6. ✅ Mike Sheetz **died in spring 2025**; work continues at UT Health San Antonio (Barshop Institute, Kureel, Volpi, Rasmussen) under XPRIZE Healthspan Milestone 1 ("Rejuvenation Through Low Frequency Ultrasound", $250k), where a **custom LFU "spa"** has been installed.

---

# PART 1 — SOURCES

Everything below was retrieved without any paywall bypass: Europe PMC REST (`fullTextXML`, `supplementaryFiles`), NCBI `efetch` (PMC), bioRxiv PDFs, ClinicalTrials.gov API v2, Onda's own site, Google Patents HTML (curl + browser UA), WIPO Patentscope (browser), and the Wix-rendered mechanobiologics.com HTML.

## 1a. AJP-Endo 2025 — "Low-frequency ultrasound reverses insulin resistance and diabetes-induced changes in the muscle transcriptome in aged mice" (doi 10.1152/ajpendo.00470.2024)

**How accessed** ✅: `journals.physiology.org` returned 403 to curl with a browser UA; Unpaywall reports hybrid-OA with only a publisher link and a **submitted version** in PMC; Europe PMC `fullTextXML` returned HTTP 500. **What worked:** NCBI E-utilities —
`https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=12145165&rettype=xml` → 78 kB JATS with the full author manuscript (PMC12145165, PMID 40323206). Saved as `lfu/ajp_pmc.xml` / `.txt`.

**Apparatus & schedule** ✅ (quotes condensed):
- "whole-body LFU treatments were administered by **submerging an ultrasound transducer in degassed water at 37 °C**" — note 37 °C here vs 32–35 °C in the Aging Cell paper.
- "frequency of **32.248 kHz**, pressure of **4 kPa**, duty cycle of **1.5 s on and 1.5 s off**".
- "Mice were partially submerged in a **ventilated compartment** in the degassed water bath"; sham mice placed in the bath without LFU.
- **30 min per session, twice per week, for 4 weeks** (Mon+Thu or Tue+Fri). Treatment protocol cross-referenced to Kureel 2025.
- No transducer model, generator, amplifier or hydrophone is named in this paper.

**Animals / design** ✅: aged C57BL/6J, 80 weeks old, Jackson; 5 groups × 16 (8M/8F) → 10–15 at terminus: NC (normal chow sham), HFHS, HFHS+LFU, HFHS/STZ, HFHS/STZ+LFU. Diabetes induced by HFHS + 2×40 mg/kg streptozotocin after 4 weeks of diet. OGTT at baseline, post-induction, post-LFU; body composition by EchoMRI; CFAB functional battery (treadmill, rotarod, grip, wheel, inverted cling); permeabilised-fibre mitochondrial respiration (soleus, white gastrocnemius); bulk mRNA-seq (3M+2F per group).

**Results** ✅ — this is the **negative** paper of the series:
- HFHS ± STZ increased adiposity, fasting glucose, glucose AUC, HOMA-IR; STZ strongly worsened glucose tolerance without big insulin changes; HOMA-β and HbA1c unchanged.
- **"LFU treatment did not improve any measures of body composition or blood glucose control"**; **no improvement in physical function (CFAB)**; mitochondrial respiration only a non-significant trend.
- Transcriptome: LFU altered 503 genes (HFHS) and 339 genes (HFHS/STZ); **260 of 503 HFHS-induced changes were reversed** by LFU; 29 genes changed by LFU in both models (27 down), dominated by immune/B-cell genes (Btla, Cd79b, Ighd, Ms4a1, Lat, Lck, Ltb, Ly6d, Spib, Irgm2), lipid (Etnk2, Lpin2), cell cycle (Mki67, Dlgap5, Slain1, Zc3h12d), and Socs1/Socs3.
- No increase of p16/p21/p53 in skeletal muscle by qPCR (p21 up in liver in HFHS/STZ).
- Authors' conclusion: LFU acts on inflammation/immune-cell function in muscle, **not** on glycaemic control or performance in this model.

## 1b. Aging Cell 2025 — Kureel et al., doi 10.1111/acel.70008 — INCLUDING SUPPLEMENTARY

**How accessed** ✅: Europe PMC `fullTextXML` for PMC12151899 (183 kB) **plus** the supplementary bundle endpoint
`https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12151899/supplementaryFiles` → 23 MB zip containing `ACEL-24-e70008-s001.docx` (all supplementary figure legends + the Figure S1 artwork) and `-s002.docx` (gene tables). Figure S1A/B artwork extracted from `word/media/image5.png` and `image6.png`; the bar-chart axis labels were recovered from the embedded **EMF** vector files (`image1.emf`…`image4.emf`).

### Figure S1A — the setup schematic (this *is* the "slide")
Rendered on white (the PNG has transparent background, which is why the text looks missing in some copies). Content ✅:
- A generic bench **generator box** (BioRender clip-art, no model) → cable → **beaker**.
- A **vacuum flask on a magnetic stirrer**, arrow labelled **"Vacuum"** → the beaker: this is the **degassing** step (vacuum + stirring), not boiling.
- **Two beakers**: left one with **two mice on a mesh** at the waterline; right one with a **culture dish floating/supported** near the surface. In **both**, the transducer at the bottom is drawn as a **truncated-cone potted puck** (pink) with a cable — consistent with the "aluminium cone + epoxy potting" description in the cancer papers and with the photograph in Tijore's Figure S7.
- Printed "Ultrasound Settings:" block:
  - **Varying Power Input: 135 V–275 V**
  - **32,248 Hz**
  - **1.5 s Duty Cycle**
  - **30 min Total (600 pulses)**
  - **7–10 cm above transducer**
  - **Output power: 4–8 Pa**   ← note: **Pa**, not kPa, on the authors' own slide.
- 🔧 600 pulses × (1.5 s on + 1.5 s off) = 1800 s = 30 min ✓ internally consistent.
- 🔧 "135–275 V" is the **electrical drive amplitude range** (almost certainly V peak-to-peak into the piezo), not a mains voltage: it maps onto the 1×/1.3×/2× "power levels" used in the mouse dosing study (275/135 ≈ 2.0).

### Figure S1B — the field map
✅ A circular (dish-shaped) 5×5-ish grid heat map of "LFU output power at the location of treatment", colour-scaled **"Low Power <20 mV" → "High Power ~180 mV"**. So the field was mapped **in millivolts of hydrophone/meter output**, peaked near the centre, roughly a factor **9× spread** across the treatment plane. 🔧 That ±ratio is important: the "4 kPa" figure is a *point* value in a strongly non-uniform field.

### Optimisation experiments (recovered axis labels) ✅
- **S1C** — growth at 48 h vs power at **33 kHz vs 39 kHz**; x-categories: `Control, 2.2 pa_33, 3.8 pa_33, 7.2 pa_33, 10 pa_33, 2.2 pa_39, 3.8 pa_39, 7.2 pa_39, 10 pa_39`.
- **S1D** — 33 kHz only; x-categories: `Control, 4 pa, 5.2 pa, 6.4 pa, 8 pa` (this is the "4–8" range).
- **S1E** — growth vs treatment duration.
- **S1F** — duty cycle: `Control, 1.25 on_1.5 off, 1.5 on_1.5 off, 1.75 on_1.5 off, 1.25 off_1.5 on, 1.75 off_1.5 on` — i.e. they varied the ON and OFF times by ±0.25 s around 1.5 s and 1.5/1.5 won. Legend: "The power level was 4 kPa at 33 kHz for 30′."
  🔧 So the duty-cycle optimum is *sharp at the ±17 % level*, which is a strong claim for a mechanism nobody has identified, and is the single most replication-critical parameter after pressure.

### Methods text ✅
- In vitro: plates parafilm-wrapped; "placed on a **plastic mesh**, mounted in a water tank with an ultrasound transducer"; "water in the tank was **degassed and heated to 35 °C**"; "distance between the sample and transducer approximately **9–10 cm**"; "output power of the transducer was measured at the plate location by a calibrated needle hydrophone (**ONDA MCT-2000**)"; "power (4 kPa), frequency **32.248 kHz**, duty cycle 1.5 on / 1.5 off for **20–30 min**".
- In vivo: "Aged mice (>22 months) were treated in a **4 L glass beaker with an internal plastic cylinder of 13 cm height and 15.2 cm diameter**. A **plastic mesh** on top of the cylinder supported the mice … Degassed, **32–35 °C** water filled the beaker to a level **1 inch above the mesh so that half of them were in water**." Sham = same bath, 30 min, no ultrasound.
- Cells positioned **7–10 cm above the transducer**, "in the far field".
- Dose study ✅: sham + 5 LFU groups (n≈6–8 each): **D1** daily, **D2** every 2nd day, **D3** every 3rd day at 1× power, plus **1.3×** and **2×** power daily; 2 weeks on / 2 weeks off / 2 weeks on. Outcome: "the **best survivors had the lowest doses** of ultrasound (D2 and D3) with about 50 % survival at 1000 days"; wheel-running 7–10× sham; combined D2+D3 significantly longer-lived; the 2× group nevertheless showed no damage and better fur. 🔧 i.e. **dose–response is non-monotonic; more is not better**.
- Vendor/model information for the **transducer, generator and amplifier is absent from this paper and its supplement.** The only hardware model named anywhere is the Onda meter.

### bioRxiv 10.1101/2022.12.08.519320 v1→v4 — methods diff ✅
(all four PDFs downloaded from `biorxiv.org/content/…v{n}.full.pdf`)

| Item | v1 (2022-12-12) | v2 (2024-02-05) | v3 (2024-02-20) | v4 | Aging Cell (2025) |
|---|---|---|---|---|---|
| Title | "Rejuvenating Senescent Cells and Organisms with Only Ultrasound" | "…without Senolysis" | same | same | "Rejuvenation of Senescent Cells, In Vitro and In Vivo, by LFU" |
| Hydrophone | "a calibrated hydrophone" | "calibrated needle hydrophone (**onda**)" | same | "calibrated needle hydrophone (**ONDA MCT-2000**)" | ONDA MCT-2000 |
| Optimum pressure | not stated in methods | "**4 Pa**" | "**4 Pa**" | "**4 Pa**" | "**4 kPa**" |
| Frequency | — | 32.2 kHz | 32.2 kHz | 32.2 kHz | 32.248 kHz |
| Tank / distance | 9–10 cm, degassed, 35 °C | same | same | same | same |
| Mouse vessel | 4 L beaker, cylinder 13 cm × 15.2 cm | same | same | same | same |
| Transducer model | never given | never given | never given | never given | never given |

🔧 **Conclusion: no version of this paper ever identifies the transducer, generator or amplifier.** The "kPa" appears only at the final journal stage, while the authors' own figure artwork still says "pa". Someone building this must resolve the unit question experimentally (see Part 3 physics).

### What the *patent* adds (US20240001155A1 / WO2024030212A1, "Reversal of cellular senescence by treatment with low frequency ultrasound", Mechanobiologics Inc., inventors Sheetz, Kureel, Margadant; priority 2022-06-30) ✅
Fetched as HTML from Google Patents with a browser UA (later blocked — see "what failed").
- "Cells were treated with **pressure pulses of 6–7 kilopascal** in water, using **32.249 kHz** … for 30 minutes"; mice: "intermittent ultrasound of **32.249 kHz and 6–7 kilopascal** … 30 minutes at duty cycles of 1.5 s on and 1.5 s off". Elsewhere: "**3.5–4 Pa**" for the same optimum — the patent contains *both* unit scales.
- Claimed pressure ladder: "approximately **170 Pa, 340, 510, 680, 850, 990, 1130, 1300, 1470, 1640, 1810, 1980, 2150, 2320, 2490, 2660, 2830, 3000, 3500, 4000, 4500 Pa or more**". 🔧 Note the ~170 Pa quantisation — that looks like an instrument step, e.g. a fixed mV→Pa scale factor.
- Claims **30–100 kHz** administration; broad range "20 kHz–500 kHz", intensity "<3 W/cm²", elsewhere "<500 mW/cm²".
- Engineering remarks that matter for a replication:
  - "**Controlled beam travel, beam geometry, and vat geometry are key**".
  - "the methods are configured to **avoid build up standing waves and unplanned foci**. **Beam steering and frequency sweeps** (e.g. jitter or staggering) … **absorbed materials can be added to the treatment vat** that will suppress high order reflections."
  - "the methods described herein are **inefficient** in the sense that clean and directed ultrasound is administered at expense of electrical power"; "the amount of energy absorbed by the tissue is minimal (**1–3 % of the sound power produced**)".
  - **Non-sinusoidal drive is explicitly contemplated**: "a rectangular wave has very strong contributions at 2×–7× the base frequency. If operated at **10 kHz**, it will still meet our researched frequency domains. If operated between **18–20 kHz**, it will likely work well without being considered ultrasound and without being heard by the majority of patients." 🔧 i.e. the inventors themselves think the active agent may be *harmonic content*, which makes a cheap square-wave driver arguably closer to the original than a clean sine.
  - "the ultrasound is administered to a subject at a **'full body ultrasound spa'**".

## 1c. Other Sheetz / Margadant / Tijore / Kureel LFU papers — apparatus details

All retrieved via Europe PMC `fullTextXML` + `supplementaryFiles` (all open access).

### Tijore et al. 2025, *Bioeng Transl Med* 10:e10737, "Ultrasound-mediated mechanical forces activate selective tumor cell apoptosis" (PMID 40060768, PMC11883105) ✅ — **the best hardware description in the whole corpus**
> "The **custom-made ultrasound device** was developed in the lab … Briefly, we used **ring transducers with diameters of 16 and 25 mm made of PZT4 material (Beijing Ultrasonics 25 × 10 × 4 and 16 × 8 × 4 piezoceramic rings)**. An **aluminum cone is mounted on the rings to widen the field to some 5 cm diameter and attenuate the amplitude to form plane waves**. **Epoxy and silicon rubberized coats** were added to transducers to improve the wave emission. The transducer was **fixed to the bottom of the ultrasound water tanks**. The water tank was placed in an **incubator to maintain 37 °C**… Sealed samples were then placed **8 cm above the transducer top**. The tank was filled with **degassed DI water**…"
- Cites for the device: **ref 35 = Tijore, Margadant, Yao, Sheetz, "Systems and methods for cancer treatment", US patent app 17/607,819 (2022)**; ref 36 = DeAngelis & Schulze, "Performance of PZT8 versus PZT4 piezoceramic materials in ultrasonic transducers", *Phys. Procedia* 87:85–92 (2016).
- **Figure S10** (supplementary PDF, p. 11): block diagram — **"Signal generator & amplifier" → cable → "Transducer" (drawn as a small cylinder) sitting in a "Water bath", with the "Well plate" above**; the whole bath inside an incubator. No models.
- **Figure S7** (p. 8): photograph of the actual tank — vertical glass/acrylic tank, perforated shelf, eggs on a shelf at the waterline, **the transducer at the bottom is a white potted puck (cone/cup shape) with a red/black twisted pair**.
- Parameters ✅: in vitro **33 kHz, 50 % duty (1 s on / 1 s off), 2 h, 39 mW/cm² (labelled "200 V")**; 120 kHz gave **no** apoptosis; in vivo mice **39 kHz, 1 h/day, 2–3 weeks**, at **39 mW/cm² (200 V), 51.5 mW/cm² (300 V), 166 mW/cm² (400 V)**; mice on a **1.5 cm-thick gel pad directly on the transducer** in degassed water.
- 🔧 **This is the key cross-calibration**: the same lab expresses "power" as **V drive** *and* **mW/cm²**. 39 mW/cm² ⇒ p = √(2·Z·I) = √(2·1.48e6·390) ≈ **34 kPa peak**. 51.5 mW/cm² ⇒ 39 kPa; 166 mW/cm² ⇒ 70 kPa. So the *cancer* work runs at tens of kPa, and the *rejuvenation* work at 4–8 (k)Pa — i.e. the rejuvenation dose is ~1/10 to 1/5 of the tumour-killing dose **if** the rejuvenation number is in kPa, and 1/10000 if it is in Pa. This is a strong independent argument that "4 kPa" is the right reading, since 4 Pa would be an absurd extrapolation.

### Singh et al. 2021, *Bioeng Transl Med* 6:e10233, "Enhanced tumor cell killing by ultrasound after microtubule depolymerization" (PMC8459596) ✅
- "low-frequency US (**33 kHz**) for 2 h with **7.7 mW/cm²** power intensity and a **50 % duty cycle**"; "samples … placed **8 cm above transducer** in the US tank, which was mounted in the incubator with 37 °C". Device construction: "details of customize-built US device fabrication were mentioned previously" (→ Tijore 2020 bioRxiv). 🔧 7.7 mW/cm² ⇒ **15 kPa peak**.

### Zangoui, Singh, Sheetz, Kenney 2025, *J Bacteriol* 207(9) e00176-25 (PMC12445081) ✅
- LFU **30 min every other day, 6–9 times** before *Salmonella* oral gavage; old C57BL/6J 21–24 months; controls placed in the bath unpowered. **No new apparatus detail** — defers entirely to Kureel 2025. 4-fold lower liver CFU; ICAM-1, SDF-1, KC/CXCL1 restored to young levels.

### Tijore lab (IISc Bangalore), 2026 — **the most replicable rig published so far**
- **Saigaonkar et al., "Ultrasound-Generated Nanoscale Mechanical Stimulation to Regulate Stem Cell Differentiation", *ACS Nanosci Au* 2026 (PMC13087965)** ✅ Methods verbatim:
  > "The **impedance analyzer** was used to calibrate the **Langevin transducer (APC International)**. The transducer is **bonded to the container with the epoxy having high bonding strength**. The platform for the transducer is designed and **3D-printed** … A dish holder was 3D-printed … and to provide a **height adjustment mechanism for sound pressure calibration** … The transducer bonded to the setup was actuated using an **Ultrasound Driver (Piezo Drive, PDU 210)**. The sound pressure (kPa) inside the culture dishes filled with cell culture media was measured by a **hydrophone (FEL Communications)** connected to the **USB oscilloscope (Digilent, 410-321)**. Required ultrasound pressure was achieved by **controlling the applied actuation voltage** … **Vacuum-degassed water** was added to the tank…"
  - Quantitative pressure↔displacement calibration (laser interferometer, 127 scan points over ~1 cm²) ✅:
    | US pressure | 1 kPa | 2 kPa | 3 kPa | 5 kPa | 10 kPa | 20 kPa |
    |---|---|---|---|---|---|---|
    | vertical displacement of dish glass | 11 nm | ~30 nm | 40 nm | 65 nm | 118 nm | 236 nm |
    Mean over the dish 41 ± 19 nm SD (at 5 kPa).
  - Biology: 39 kHz, 50 % duty, 30 min/day × 7 d: **2–5 kPa promotes hMSC spreading/growth and osteogenesis; 10–20 kPa kills; >50 kPa lethal in 1 h; 100 kHz does nothing.** 🔧 This independently reproduces "there is a narrow low-kPa window", at 39 kHz.
- **Luha et al., "Revealing biomechanical vulnerabilities in oral cancer cells using 3D coculture platform and low-frequency ultrasound", *Mater Today Bio* 2026 (PMC13315667)** ✅: "**Langevin piezoelectric transducer (APC 90-4050)**", "bonded to a **steel container** and placed on a custom-made **3D printed platform with adjustable XYZ**", "**39 kHz**, 50 % duty, **Ultrasound Driver (PDU 210)**", "pressure … measured with a hydrophone connected to a **USB oscilloscope (Digilent 410-321)** by submerging it in culture medium, followed by replacing it with the experimental samples", "**the voltage applied to the transducer was adjusted to achieve the desired pressure levels**", 50–75 kPa for apoptosis.

### Patents ✅
| Publication | Title | Assignee / inventors | Relevance |
|---|---|---|---|
| **US20240001155A1** (=WO2024030212A1, EP4561696A1; app 18/217,362; prio 63/357,618 of 2022-06-30) | Reversal of cellular senescence by treatment with LFU | Mechanobiologics Inc — Sheetz, Kureel, Margadant | dose/parameters, "full body ultrasound spa", standing-wave & absorber remarks, square-wave/harmonics remark |
| **US20220203138A1** (app 17/607,819) | Systems and Methods for Cancer Treatment | Tijore, Margadant, Yao, Sheetz | the device cited by the BTM papers (ring PZT4 + cone) |
| **WO2020223359A1 / US20220047894** | **Systems and Methods for Immersion Mechanotherapy** | **Mechanobiologics LLC — Margadant, Kenney, Sheetz**; prio 62/840,850 of 2019-04-30 | **the bathtub** |

**WO2020223359A1 — extracted device teaching** ✅ (read via WIPO Patentscope in the browser pane; Google Patents was blocking this IP):
- "therapeutic **spas and/or hot tubs** for ultrasonic treatments, facilitated with configurable and controllable ultrasound generators (e.g. **phased arrays or sliding panels** of ultrasonic generators)".
- Transducers "**disposed to a bottom, and side walls**" of the bathtub, "**mounted at spaced locations**"; may be "**immersed in the liquid**", or outside the vessel, or coupled by a **waveguide**; "**packaged and sealed in a panel** for sterilization", panel removable.
- "the one or more transducers may be **carried by a robotic arm**… may be a **gantry, such as a three-axis gantry**… may be a **6-axis robot arm**… can be **passively moved by a user**… compliant mode". → this is the origin of the "articulated arms" description; the patent says **1 to 1000** transducers, "may have different amplitudes and/or a phase relationship", "constant progressive phase shift or variable phase shift", optionally **different frequencies per transducer** to make a composite waveform.
- **Safety architecture** 🔑: "the one or more transducers may be customized to be a **neutral generator** to provide additional user safety. For example, with use of transducer or antenna arrays that have **net feed voltages adding up to zero or near zero**, safe human contact may be provided even in the case of a failure of the insulation. The array … can be built with **alternating coil direction or transducers with inverted piezo crystals** thereby allowing for a zero net voltage."
- **Standing-wave management**: interior wall shaped as an **expanding cone**, or paraboloid / Fresnel rings / "moth eye" profiles; "a **soft medium with scattering kernels therein (e.g. foams or sponges)**" on the interior surface to absorb excess energy. Wall materials: glass, aluminium, steel, fibreglass, porcelain, high-temperature ceramic.
- **Thermal/water**: heater to **95–105 °F (35–40.5 °C)**; temperature sensors + controller; filtration and recirculation through **hydrotherapy jet nozzles**; **chlorine** dosing for hygiene; transducer cooling (passive fins or thermoelectric).
- **Dose**: 20–250 kHz, "low intensity" **<500 mW/cm²** (ladder down to 10 mW/cm²), long exposure (hours), duty-cycle modulated; penetration "at least 0.1–20 cm".
- Sensors: proximity/ultrasonic/camera user positioning, ECG/respiration inputs, PID-controlled arm.

## 1d. Company, trial, press

### mechanobiologics.com ✅
Wix site; `curl` with a browser UA returns fully-rendered text. `sitemap.xml` → `pages-sitemap.xml` lists only `/` and `/blank` … `/blank-6` (the nav labels are HOME, ABOUT=/blank, FOUNDER=/blank-1, SCIENCE & TECHNOLOGY=/blank-2, TEAM=/blank-3, MILESTONES=/blank-4, INVESTORS=/blank-5, NEWS & MEDIA=/blank-6). Extracted content:
- **Company**: "Mechanobiologics, Inc. develops innovative low-frequency ultrasound (LFU) devices for both **medical and wellness** applications… In the wellness space, our **spa-based systems** are designed to support healthy aging by enhancing skin thickness, improving elasticity…". Claimed pipeline: osteoarthritis (clinical trials "ongoing"), immune stimulation, Alzheimer's models (3xTG-AD study with the UTMB Brain Health Institute, manuscript in preparation), glucose intolerance/insulin resistance.
- **Team** (photo caption): Lisheng Xu, **Linda Kenney**, Shuhan Liu, Dasvit Shetty, Mrinal Shah, Moirangthem Kiran Singh, Yong Hwee Foo, Priscilla Liu, Parisa Zangoui, Yuki Yamanaka — i.e. the company is now essentially **Linda Kenney's lab** (Kenney is Sheetz's widow and a co-inventor on the immersion patent).
- **Milestones page** lists the three patent publication numbers (20220203138, **20220047894**, 20240001155) — this is how the immersion patent was identified.
- **News page** reproduces the UT San Antonio newsroom article (5 June, by Claire Kowalick): UT Health San Antonio named **XPRIZE Healthspan semifinalist and Milestone 1 winner ($250 000)** for **"Rejuvenation Through Low Frequency Ultrasound"**; after Sheetz's death in spring 2025 the XPRIZE Foundation, UTMB and **Linda Kenney** transferred the Milestone 1 award to UT Health San Antonio; the work is now at the **Sam and Ann Barshop Institute for Longevity & Aging Studies**, where "**a custom-designed low-frequency ultrasound spa was recently installed**… uses painless ultrasonic waves delivered through water, and is being prepared for **initial human trials in older adults**". Quotes from Blake Rasmussen, Sanjay Kureel (moved to Barshop in 2025), Elena Volpi. Milestone 2 finalists announced **July 2026**; $81 M grand prize 2030.
- ⚠️ **Nothing on the site describes the device hardware** — no transducer count, no "10–12 transducers on articulated arms". That description is **not corroborated by any source I could reach**; the closest primary support is the patent's robotic-arm/1-to-1000-transducer language.

### Clinical trial ✅ — **NCT06562374**, retrieved from `https://clinicaltrials.gov/api/v2/studies/NCT06562374`
- Title: "Low Frequency Ultrasound for Osteoarthritis Healing and Rehabilitation"; sponsor **University of Texas Medical Branch, Galveston**; start 2024-07-31; **overall status: SUSPENDED** (as of this retrieval).
- Device text: "The ultrasound will be delivered at a **frequency of 33 kHz at power levels of 4-10 Pascals** with a program of **1.6 seconds on and 1.6 seconds off**. The **generators will be encased in epoxy within the Osteoarthritis baths.** The intervention will be repeated every second or third day to allow time for healing."
- Arm: "30 min at either a power level of **4 or 10 Pascals** to determine which power level is optimal"; adults ≥40 with ≥6 months chronic knee pain; single site.
- 🔧 Note the **1.6 s** here vs **1.5 s** everywhere else, and **"Pascals"** again. The phrase "generators … encased in epoxy within the baths" most plausibly means **potted transducer/driver assemblies submerged in the (knee-sized) baths**, matching the potted-puck transducers in the mouse rig — not mains-powered generators in the water.

### What I could NOT access, and exactly what was tried
| Target | Attempts | Outcome |
|---|---|---|
| AJP-Endo **published** (typeset) version + its supplementary figures | `journals.physiology.org` with browser UA (403); Unpaywall (only publisher link + PMC submitted version); Europe PMC fullTextXML (HTTP 500) | Got the **author manuscript** via NCBI efetch; the *supplemental figures* (Suppl. Fig. 1–5) of that paper were not in the PMC package |
| Google Patents (after ~2 successful fetches) | curl + browser UA; WebFetch; browser pane | **HTTP 503 "automated queries"** — the whole IP is rate-limited by Google. Worked around via WIPO Patentscope for WO2020223359A1 |
| **US20220203138A1** (cancer device patent) full text | Google Patents (503); USPTO `image-ppubs.uspto.gov/.../downloadPdf/20220203138` → PDF is a **scanned image**, no text layer; uspto.report / justia / patentguru / freepatentsonline / unifiedpatents → 403 / Cloudflare / JS-only; Espacenet → Cloudflare challenge even in the browser pane | **Eventually READ** via WIPO Patentscope, family member **WO2020223242A1** (PCT/US2020/030288, applicant Mechanobiologics LLC, inventor Ajay Sanjay Tijore). Result: it is a **method/system patent with no vendor-specific hardware** — 5–30 / 30–250 kHz / 150 kHz–1 MHz ranges, <500 mW/cm² "low intensity, high amplitude", duty-factor modulation, 1–1000 transducers with progressive or variable phase shift, optional per-transducer different frequencies ("composite waveform"), gel-pad coupling, and the same "**neutral generator**" concept. The ring-PZT4-plus-aluminium-cone detail exists **only in the BTM 2025 methods section**, not in the patent. |
| Wayback Machine snapshots of mechanobiologics.com | `archive.org/wayback/available` and CDX API | **Internet Archive returned 429 then "Temporarily Offline"** during this session. (Live site was fully readable anyway.) |
| YouTube/podcast transcripts, further news coverage, UTMB "ultrasound spa" photos | — | **Session web-search budget (200 calls) was exhausted** by the parallel component research; DuckDuckGo HTML scraping worked only intermittently (202 challenge). Not completed. |

---

# PART 2 — HARDWARE: THREE ARCHITECTURES

*(Sections A, B and the calibration/instrumentation section are inserted below from the dedicated component research; section C from the human-scale/safety research.)*

<!--PART2A-->
<!--PART2B-->
## Architecture C — multi-channel array "bathtub" (8–16 channels), human immersion

> ⚠️ All IEC clause numbers and limit values in this section are **recalled domain knowledge, not re-verified against the standards' text** in this session (the session's web-search budget ran out). Buy and read IEC 60601-1, 60601-2-5 and IEC 60364-7-701/702 before designing to them (~€300–900 total).

### C.1 Blunt risk statement
A naked human fully immersed in ~250 L of conductive water, with energised hardware in the water, a kW-class heater nearby, and an acoustic exposure that **no standard covers**. Immersion collapses body impedance to roughly its internal value (~500 Ω) and makes contact area effectively unbounded; incapacitation (not electrocution) at single-digit mA is enough to drown someone. Additionally the source literature is internally inconsistent about pressure by ~1000× (Part 1), and the mouse data show **lower dose gave better survival**. Never run with a person in the water and a mains heater energised at the same time; never run unattended.

### C.2 Acoustics of a human-scale tub at 33 kHz 🔧
| Quantity | Value |
|---|---|
| λ at 33 kHz (37 °C, c = 1524 m/s) | **46 mm** (node-to-antinode 23 mm) |
| Particle displacement at 4 kPa | 13 nm; particle velocity 2.7 mm/s; acceleration ≈ 56 g |
| Modes below 33 kHz in 0.25 m³ | ≈ **11 000** (≈1 mode/Hz) |
| Schroeder frequency (water-rescaled, f_s ≈ 19 142·√(T60/V)) | **≈ 8.6 kHz** for T60 = 50 ms |

**The tub is a diffuse (statistical) field, not a modal one.** You cannot tune out the standing waves; you must average over them. In a diffuse field |p| is Rayleigh-distributed and intensity exponential: the spatial SD of intensity **equals its mean**, ~2 % of the volume exceeds 2× the nominal pressure, ~0.01 % exceeds 3×. Field decorrelation length ≈ λ/2 ≈ 2.3 cm — so simply **asking the subject to shift position every couple of minutes** is a free and effective averaging mechanism.

Other facts worth knowing:
- Water absorption at 33 kHz ≈ 10⁻⁵ Np/m → negligible; **tissue** absorption at 0.5 dB·cm⁻¹·MHz⁻¹ ⇒ 0.017 dB/cm ⇒ ~0.3 dB through a torso. **The body is nearly acoustically transparent at 33 kHz** — this is whole-body, not surface, exposure; the only strong reflectors are gas bodies (lung, bowel) and bone.
- **Tub material matters**: industry notes immersibles are not used in plastic tanks because "the plastic absorbs the ultrasonic energy" ([Best Technology](https://www.besttechnologyinc.com/ultrasonic-cleaning-systems/immersible-ultrasonic-transducers-cleaners/)). 🔧 For this application that absorption is a **feature**: an **acrylic** tub damps the field and shortens T60, at the cost of drive power you have in abundance. Steel or glass would be far more reverberant.
- The **free water surface is a pressure-release boundary** (R ≈ −1): a guaranteed node at the surface, strong gradients at the waterline (chest height).
- Diffuse-field power balance W = (c/4)·S·ᾱ·E with p_rms = 2.83 kPa, S ≈ 2 m², ᾱ ≈ 0.2 → **≈ 0.5 W acoustic total → ~2–5 W electrical for 12 channels**. Compare industrial cleaning at 30–100 W per gallon ⇒ ~2–7 kW in 250 L: **you need ~10⁻³ of a cleaner's power density.**

### C.3 Drive architecture for 8–16 channels
**Key fork** 🔧: a Langevin at resonance has Q of several hundred → −3 dB bandwidth of ~66 Hz at 33 kHz, so you **cannot sweep ±500 Hz and keep amplitude flat**. Because you only need tens of mW per channel, the better choice is to **drive deliberately off-resonance from a low-impedance source**, where the load is essentially C₀ (5–10 nF ⇒ X_C ≈ 690 Ω at 7 nF, 0.15 VA per channel at 10 V rms). You lose efficiency you don't need and gain a **flat, arbitrarily ditherable response**. (Engineering judgement — must be validated on the bench with a hydrophone.)

| # | Architecture | Ch | Phase control | Notes |
|---|---|---|---|---|
| **A** | Multichannel **96/192 kHz audio interface** + 12 wideband amps | 8–16 | arbitrary, sample-accurate | Everything (freq, phase, dither, envelope, sequencing) becomes software; same clock can record the hydrophone. ⚠️ must verify the converter's reconstruction filter passes 33 kHz (Nyquist 48 kHz at 96 kS/s); amps must be wideband, not audio-band-limited |
| **B** | **MCU (RP2040/STM32/ESP32) PWM → gate driver → half-bridge** | 8–32 | fine, per channel | Cheapest. Published RP2040 multichannel square-wave generator achieves 4 ns granularity / 0.17 ns jitter ([ResearchGate](https://www.researchgate.net/publication/389059884_Scaleable_Multichannel_Square-Wave_Sequence_Generator_Based_on_the_RP2040_Microcontroller)); 1° of phase at 33 kHz = 84 ns. Square wave ⇒ harmonics at 99/165 kHz (which the patent arguably *wants*) |
| **C** | Central **DDS (AD9833 / AD9959)** + per-channel gate/amp | any | coarse, or 4-ch hardware-synced | Simple; but a single master oscillator is the wrong primitive if you want *de*-synchronisation |
| **D** | **HV583-class** shift-register HV driver — cf. [Open Source Ultrasonic Phased Array](https://hackaday.io/project/159467-open-source-ultrasonic-phased-array) (256 ch, BeagleBone PRU, 40 kHz, 12–80 V, 5-bit phase, 30 mA/ch) | 128–256 | 5-bit | Proven open design at an adjacent frequency; overkill |
| **E** | **Ultraino** (MIT licence; Arduino Mega 64-ch, or DriverNano16) — [GitHub](https://github.com/asiermarzo/Ultraino), [paper](https://doi.org/10.1109/tuffc.2017.2769399) | 16 or 64 | π/5 (36°) | Complete open HW+SW+field-simulation package at the right channel count; designed for 40 kHz **airborne**, needs retargeting to water |

🔧 Recommended: **A as the drive, B as an independent safety/interlock MCU** that can only *cut* drive power, so a bug in the drive host cannot defeat the interlocks.

### C.4 Standing waves: synchronise or de-synchronise?
Coherent channels produce a **stationary** interference pattern — permanent hot spots parked on the same 2 cm of tissue for 30 minutes. That is the failure mode to design against. Industry confirms both problem and fix: sweeping generators exist precisely because "fixed frequency designs tend to create hot spots and standing waves" ([UPCORP](https://www.upcorp.com/technical-information/)); see also US patents [5895997](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5895997), [5462604](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5462604), [8652262](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8652262) (frequency modulation) and [4836684](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/4836684) ("phase diversifier"). The Mechanobiologics senescence patent itself calls for "beam steering and frequency sweeps (jitter or staggering)" and absorbers in the vat.

| Technique | Implementation | Effect 🔧 |
|---|---|---|
| **Per-channel frequency offset** *(primary)* | ch_i at f0 + i·Δ, Δ = 7–40 Hz | Pattern scans continuously; beat periods 2.3–140 ms ⇒ 11–700 pattern cycles inside each 1.5 s burst. Free |
| **Global sweep 32.0–33.0 kHz** | 10–100 sweeps/s | Field correlation bandwidth ≈ 1/T60 ≈ 20 Hz ⇒ ~50 independent realisations. Needs off-resonance drive |
| **Per-channel random phase re-draw** | new phase every 10–20 ms | 80–160 realisations per burst; cheapest in architecture A |
| **Sequential channel firing** | round-robin | Removes inter-channel interference but each source still standing-waves with the walls; diagnostic mode only |
| **Aperiodic transducer placement** | no symmetry, no equal spacing | Free |
| **Subject movement** | shift position every ~2 min, or slowly move the arms at mm/s | 2 cm fully decorrelates the field; very effective |
| ✗ Water circulation | — | **Does not** homogenise the acoustic field (2 mm/s vs 1500 m/s); keep it for temperature and bubble sweeping only |

🔧 Combined estimate: 12 incoherent sources × ~50 sweep realisations ⇒ spatial SD of time-averaged intensity from ~100 % down to ~4 % (1/√600). **Verify by hydrophone mapping; do not assume.**

### C.5 Sequencing and interlocks 🔧
- 1.5 s on / 1.5 s off with a **10–50 ms raised-cosine ramp** on each burst edge (a hard gate on a resonant load overshoots and clicks broadband).
- Hard 30-minute session cut in the interlock MCU, independent of the host.
- Interlocks that must **remove drive power**: two cross-checked water-temperature sensors **plus** a third electromechanical thermostat in series with the heater contactor; water level; insulation/earth-leakage monitor on the SELV bus; latching E-stops for bather and attendant; attendant presence; per-channel drive-current sense (detects a flooded transducer). **Heater contactor mechanically open whenever the tub is occupied.**

### C.6 Electrical safety
**Applied-part class** ⚠️: design to **Type CF** (floating, cardiac-grade) — the thorax is immersed in a conductive medium in contact with the energised part, so the current path is across the heart.

Leakage-current limits (µA) ⚠️ *(recalled; verify)*:

| Current | B | BF | **CF** |
|---|---|---|---|
| Patient leakage AC, normal condition | 100 | 100 | **10** |
| Patient leakage AC, single fault | 500 | 500 | **50** |
| Patient leakage DC, NC / SFC | 10 / 50 | 10 / 50 | 10 / 50 |
| Mains on applied part (MOAP) | – | 5000 | **50** |
| Patient auxiliary AC, NC / SFC | 100 / 500 | 100 / 500 | 10 / 50 |
| Touch current NC / SFC | 100 / 500 | 100 / 500 | 100 / 500 |
| Earth leakage NC / SFC | 5000 / 10000 | same | same |

**MOPP isolation** ⚠️ at 250 V working voltage: 1×MOPP = 1500 V AC test, 4.0 mm creepage, 2.5 mm clearance; **2×MOPP = 4000 V AC, 8.0 mm, 5.0 mm**. IEC 60601-1 requires **2×MOPP between mains and patient**. 🔧 Easiest compliant route: buy a certified **2×MOPP medical AC/DC module** (Mean Well RPS/MPM, XP Power ECM/AHM, TDK-Lambda CUS-M; 12/24 V, 15–350 W, ~€50–250) and never bring mains into the wet-side enclosure.

**Installation zones** ⚠️: IEC 60364-7-701 (bathrooms) — **zone 0 = the interior of the tub**; in zone 0 only **SELV ≤12 V AC rms / ≤30 V ripple-free DC**, equipment IPX7, **SELV source located outside zones 0–2**, all circuits behind a **30 mA RCD**, supplementary equipotential bonding. IEC 60364-7-702 (pools) is architecturally identical. IEC 60335-2-60 (whirlpool baths) ⚠️: ≤30 mA RCD, bonding, heater thermal cut-outs, water-temperature limiting. 🔧 **Since the whole system needs <5 W, build the transducer bus at 12 V SELV — it costs nothing.**

**RCD choice** ⚠️: IEC 61008/61009 general-type 30 mA breaks in ≤300 ms at IΔn, ≤40 ms at 5IΔn; UL 943 Class A GFCI trips at 4–6 mA. **Type AC is unacceptable** with switching electronics; **Type B** (detects smooth DC residuals that can magnetically blind type A/AC devices) is required. 🔧 **30 mA is the code minimum and is not adequate for a naked immersed human** — use a **10 mA type B RCD** *plus* the floating SELV architecture *plus* an **insulation-monitoring device (IMD)** on the floating bus, aborting on the **first** fault (a floating system hides the first fault; the second one kills).

Layered defence, in order: (1) 12 V floating SELV, source outside the room, 2×MOPP from mains; (2) insulation monitoring, abort on first fault; (3) double insulation + potting; (4) supplementary equipotential bonding of tub, plumbing, taps, drain, frame to one point; (5) 10 mA type B RCD; (6) 1:1 isolation transformer for mains-side gear; (7) heater disconnected during occupancy; (8) E-stops, attendant, hard timer.

**Why immersion is different** ⚠️: IEC 60479-1 thresholds — perception ~0.5 mA, **let-go ~10 mA**, tetany/respiratory arrest ~20–30 mA, fibrillation ~30–50 mA+. In water, skin impedance vanishes (1 kΩ–100 kΩ dry → ~500 Ω internal), contact area is unbounded, and the body (≈0.5 S/m) is a **better conductor than the water** (0.02–0.05 S/m) so it concentrates any gradient through itself. 12 V across an immersed body could push ~24 mA — which is exactly why 12 V is the immersed SELV ceiling. **Sanitiser salts raise conductivity and make this worse.**

**Patent-derived trick worth stealing** ✅: WO2020223359 describes a "**neutral generator**" — transducer arrays whose **net feed voltages sum to zero** (alternating coil direction / inverted piezo crystals), so an insulation failure presents no net potential to the bather. Combined with a floating SELV bus this is a genuinely good idea.

**Potting / corrosion** 🔧: commercial immersibles are welded **316L** or 304 stainless with hard-chrome faces, and crucially the **generator is external, not in the water** ([Crest](https://crest-ultrasonics.com/immersible-ultrasonic-transducer/), [BJ Ultrasonic](https://www.bjultrasonic.com/shop/500w-ultrasonic-immersible-transducer/)) — contrary to "generators encased in epoxy within the baths"; with <5 W there is no reason to put electronics in the tub. Use **two independent barriers**; the cable entry is the usual failure point (use a silicone/PU bonded jacket — PVC-jacketed stranded cable wicks water along the strands for metres); epoxy is harder/more moisture-resistant, polyurethane survives thermal cycling and vibration better; expect **potting/metal delamination** as the long-term failure mode at 33 kHz + 40 °C + daily cycling, and re-qualify seals on a schedule; halogen sanitisers pit 316L (consider titanium faces, or don't chemically sanitise).

### C.7 Exposure limits and cavitation at 33 kHz
Intensity 🔧: I = p_rms²/ρc → **4 kPa peak = 0.53 mW/cm² I_SPPA (0.27 mW/cm² at 50 % duty)**; 10 kPa peak = 3.3 mW/cm². That is ~2700× below the FDA diagnostic I_SPTA.3 720 mW/cm² and ~11 000× below the IEC 60601-2-5 physiotherapy 3 W/cm² ceiling ⚠️. Acoustic heating of the tub over a session: ~+0.001 °C. **Thermally trivial.**

**The regulatory gap, stated plainly**: IEC 60601-2-5 (physiotherapy), IEC 61689 (physiotherapy field measurement), IEC 62127-1 (hydrophones), IEC 61161 (radiation-force balance) all start at ~**0.5 MHz**; FDA Track 3 is MHz diagnostic; ACGIH / Health Canada Safety Code 24 TLVs (105 dB at 10–20 kHz, 110 dB at 25 kHz, 115 dB at 31.5–100 kHz ⚠️) are **airborne** and are set by hearing/subjective effects. ⚠️ ACGIH is recalled to carry a note reducing values by ~30 dB when the body is immersed / in contact with the medium — **find and read that note**. There is **no dose metric, no limit and no calibration chain** for whole-body liquid-coupled kHz exposure.

**Cavitation** 🔧: use the **Blake threshold**, not MI (the Apfel–Holland MI is defined for ~0.5–10 MHz short pulses; quoting MI = 0.022 here would be meaningless). p_B ≈ p0 + 0.77σ/R0 ⇒ 655 kPa (0.1 µm nuclei), 156 kPa (1 µm), ~102–107 kPa (≥10 µm); empirically ~0.1–0.15 MPa at 20–40 kHz in air-saturated water ⚠️. With a diffuse-field 3× local peak, margins are **~80×** (degassed/tissue), **~9–13×** (gassy water at 4 kPa nominal) and **~3.4×** (gassy water at 10 kPa nominal).

🔧 **The resonant-bubble problem is the real one.** Minnaert resonance at 33 kHz ⇒ **R ≈ 100 µm**, precisely the size of bubbles that nucleate on skin, body hair and tub walls in warm water. Resonant bubbles are Q-amplified (10–50), their inertial thresholds fall to tens of kPa, they produce **stable cavitation + microstreaming shear** far below inertial thresholds (the mechanism of low-frequency sonophoresis, which permeabilises skin *by design*), and **rectified diffusion grows sub-resonant bubbles toward the resonant size over 30 min** — the bath gets more dangerous as the session runs. Free mitigations: shower first, no surfactant residue, wipe skin and walls after entry, **no jets, no aeration, no ozone injection, no splashing during fill**. ⚠️ Speculative: alveolar diameter (~200–300 µm) is uncomfortably close to the resonant size, and since the body is acoustically transparent at 33 kHz the lung is the one strong internal gas reflector; note the mouse protocol immersed only the **lower half** of the animal.

### C.8 Water and thermal management for 150–300 L
- **Temperature**: source protocol used **32–37 °C**, not hot-tub heat. 🔧 Target **35–37 °C**; this removes hyperthermia/syncope risk entirely. Hot-tub guidance (CPSC/ANSI ⚠️) caps at 40 °C; the immersion patent says 95–105 °F. Fail-safe = 2 electronic sensors cross-checked + 1 electromechanical thermostat in series with the heater.
- **Energy**: 250 L from 15→36 °C = 21.9 MJ = **6.1 kWh** (~2–3 h at 2–3 kW). Standing loss of an open tub at 36 °C ≈ 200–500 W (evaporation-dominated) — use a cover. 🔧 **Best option: fill from the domestic hot-water supply blended at the tap and use no in-tub heater at all**, which deletes the largest electrical hazard; a covered 250 L tub drifts only ~1–2 °C in 30 min. Otherwise use an **external** heat exchanger, interlocked out during occupancy.
- **Degassing 250 L — honest answer: you can't, not properly.** Vacuum degassing needs a sealed vessel (an open tub can't be evacuated); boiling is absurd (≈25 kWh); **ultrasonic degassing works but requires cavitation-level intensity** — self-defeating here (industry: run the ultrasonics 5–10 min and "fine bubbles will suddenly appear and begin to rise", [Best Technology FAQ](https://www.besttechnologyinc.com/faq/degassing-ultrasonic-cleaning-tanks/); Hielscher's own figure of <1.75 % dissolved gas is for **5 gallons with vacuum**). The only real option at this volume is a **membrane contactor (Liqui-Cel-class) on a recirculation loop** — ~5 L/min, ~10 turnovers ≈ 8 h overnight to take O₂ from ~9 mg/L to <1 mg/L, ~€600–2000. Free partial substitute: **fill hot (50–55 °C) and let it cool to 36 °C** (the water ends up *undersaturated*), fill through a submerged hose (no falling stream), stand covered 1–2 h, skim. **Since the cavitation safety case rests entirely on the absence of nuclei, this is a first-order unresolved problem, not a detail.**
- **Sanitation**: 250 L at 36 °C is an ideal incubator (*Pseudomonas* folliculitis, *Legionella*, *M. avium*). But ozone aerates, halogens raise conductivity and pit stainless. 🔧 **Drain and refill every session** (€1–2 of water) solves sanitation, degassing, conductivity and corrosion simultaneously; UV on a non-aerating loop is an acceptable adjunct.

### C.9 Rough BOM for a 12-channel human-scale system 🔧 (EUR, single-unit DIY)
| Category | Low | High | Notes |
|---|---|---|---|
| Acrylic tub 200–300 L + frame + plumbing | 400 | 1 500 | acrylic preferred (damping) |
| 12 × bare Langevin stacks | 150 | 400 | **33 kHz is not a catalogue frequency** — expect to characterise and bin units |
| *(alt.)* sealed 316L immersible modules, custom 33 kHz | 1 200 | 4 000 | reference: ~$450 for a 500 W 28 kHz 9-transducer 304SS immersible box (wildly over-powered) |
| Potting, silicone-jacketed cable, glands, housings | 150 | 500 | two-barrier construction |
| Articulated arms / aperiodic mounting | 250 | 700 | |
| Drive, option A (audio interface + 12 wideband amps + host) | 600 | 1 800 | |
| Drive, option B (MCU + gate drivers + filters + PCB) | 100 | 350 | |
| Independent safety MCU, contactors, E-stops, sensors | 150 | 400 | |
| Certified **2×MOPP medical AC/DC**, 12 V SELV | 60 | 250 | |
| Isolation transformer + **10 mA type B RCD** + **IMD** + bonding | 400 | 1 500 | IMD €200–800, non-negotiable |
| **Metrology**: hydrophone flat at 33 kHz + preamp + positioner | 500 | 6 000 | Aquarian-class ~€200–500 (nominal calibration) vs Onda HCT / B&K 8103 / RESON TC4013 €2 500–5 000 |
| Pump/filter, 2× PT1000 + mechanical thermostat, external HX | 250 | 800 | preferably **no in-tub heater** |
| Membrane degasser (optional) | 0 | 2 000 | only real option at 250 L |
| IEC standards purchase | 300 | 900 | |
| **Total, minimal viable** | **≈2 800** | | option B, bare transducers, cheap hydrophone, no degasser |
| **Total, defensible** | | **≈15 000** | option A, sealed transducers, calibrated hydrophone, IMD, degasser |

🔧 The cost distribution is the story: transducers + drive electronics are ~15 % of a defensible build. **Metrology and electrical safety dominate, and they are the parts you cannot skip** — a build with €500 of transducers and no calibrated hydrophone cannot tell 4 kPa from 400 kPa.

### C.10 Must be measured before any human enters 🔧
1. Hydrophone map of the whole tub on a ≤2 cm (λ/2) grid, loaded and unloaded, in every drive mode; report mean/SD/99th percentile/max, not one number.
2. Verify the de-synchronisation actually flattens the time-averaged field (target few-% SD).
3. Measure **harmonic content** (99, 165, 231 kHz from square-wave drive).
4. Backlit photography of bubble formation on an immersed arm over 30 min — if bubbles form and persist, the cavitation case fails.
5. Leakage current into the water, normal and single-fault, against the ≤10 / ≤50 µA CF targets.
6. Insulation resistance of every wetted assembly before and after 100 thermal cycles and 100 h operation.
7. Full fault injection: cut the SELV conductor in the water; short the bus to water; fail a temperature sensor; hang the drive host.


---

# PART 3 — PHYSICS SANITY CHECKS 🔧

Constants used: fresh water at 35 °C — ρ = 994 kg/m³, c = 1520 m/s, **Z = ρc = 1.51×10⁶ Pa·s/m** (1.48×10⁶ at 20 °C). λ(33 kHz) = **4.6 cm**. ω = 2π·33 kHz = 2.07×10⁵ s⁻¹.

### 3.1 Pressure → intensity → power
Plane wave, p = peak amplitude: I = p²/(2Z).

| p (peak) | I | I over Ø5 cm cone aperture (19.6 cm²) | I over Ø15.2 cm beaker cross-section (181 cm²) | particle displacement ξ = p/(Zω) |
|---|---|---|---|---|
| **4 Pa** | 5.3×10⁻¹⁰ W/cm² | **10 nW** | 96 nW | **13 pm** |
| **8 Pa** | 2.1×10⁻⁹ W/cm² | 42 nW | 384 nW | 26 pm |
| **4 kPa** | **0.53 mW/cm²** | **10.4 mW** | **96 mW** | **13 nm** |
| **8 kPa** | 2.1 mW/cm² | 42 mW | 384 mW | 26 nm |
| 39 mW/cm² (Tijore cancer dose) | 39 mW/cm² | 0.77 W | 7.1 W | 111 nm |
| cleaning bath, ~100 kPa | 330 mW/cm² | 6.5 W | 60 W | 320 nm |

**Verdict on units**: the 4 Pa reading implies **picometre** displacements and **nanowatt** acoustic powers — physically meaningless as a biological stimulus and impossible to measure with a cleaning-tank meter whose job is to see 10–300 kPa. The 4 kPa reading implies **13 nm** particle displacement, which matches the **11 nm at 1 kPa / 65 nm at 5 kPa** interferometer measurements published independently by the Tijore lab (their dish-bottom displacement is a few × the free-field particle displacement, as expected for a resonant glass membrane). **Design your replication for 4–8 kPa and instrument it so that you can also detect if the true value was 4–8 Pa.**

### 3.2 Electrical power needed — 4 L beaker
Acoustic power required at the plane of the sample: **10–100 mW** (table above), i.e. ~**0.1 W**. But:
- The tank is **extremely reverberant** at 33 kHz: absorption in fresh water at 33 kHz is ~10⁻⁵ Np/m (α/f² ≈ 25×10⁻¹⁵ Np·m⁻¹·Hz⁻²), so essentially **zero**; all losses are at the walls, the free surface (pressure-release, R≈−1) and the sample. A glass beaker is a good resonator → the steady-state field builds up well above the single-pass value, so **less** input power is needed than the plane-wave estimate, but the field is also dominated by modes.
- Electroacoustic efficiency of a Langevin at resonance: 50–90 %; of a PZT ring + cone driven **off resonance**: 1–10 %.
- 🔧 **Estimate: 0.1–3 W electrical** for the mouse beaker. With a "135–275 V" drive this implies a high-impedance, largely reactive load: a 25×10×4 mm PZT4 ring has C₀ of order 1–3 nF → at 33 kHz X_C ≈ 1.6–5 kΩ, so 200 Vpp (≈71 V rms) gives 14–44 mA reactive, **1–3 VA**, of which the real part is a fraction. Everything is consistent with a **small piezo driver (PiezoDrive PDU/PDUS-class, ≤210 Vpp) rather than an RF power amplifier**.
- **Sanity cross-check with the published intensity figures**: 39 mW/cm² over a 5 cm aperture = 0.77 W acoustic ⇒ a few watts electrical — exactly what a PDU-class driver delivers, and consistent with the same lab's "200 V / 300 V / 400 V" power labels.

### 3.3 Bathtub scale
For 4 kPa peak everywhere in a 200–250 L tub:
- Plane-wave-equivalent through a 0.9 m² cross-section: 5.3 W/m²·0.9 = **~5 W acoustic**; at 10 kPa, **~30 W acoustic**.
- A diffuse-field energy-balance estimate (W = (c/4)·S·ᾱ·E with S ≈ 2 m², ᾱ ≈ 0.2) gives **~0.5–1 W acoustic** for 4 kPa rms — an order of magnitude *less*, because a reverberant tank recycles energy.
- 🔧 Take the bracket: **0.5–30 W acoustic total**, hence **2–150 W electrical** for the whole tub, i.e. **0.2–12 W per channel for 12 channels.** Even the pessimistic end is ~1 % of a comparable-volume ultrasonic cleaner (which would run 2–7 kW). **This device is a milliwatts-to-watts machine, not a kilowatt machine** — which is exactly why a SELV (≤12 V AC / ≤30 V DC) architecture is feasible.
- Acoustic heating: 5 W × 1800 s × 50 % duty = 4.5 kJ into 250 L = **+0.004 °C**. Thermally irrelevant; the water heater, not the ultrasound, is the thermal system.

### 3.4 Cavitation margin
- Blake threshold (quasi-static, correct framework at 33 kHz — the Apfel–Holland MI is defined for ~0.5–10 MHz short pulses and should **not** be quoted here): p_B ≈ p₀ + 0.77·σ/R₀ ⇒ ~**655 kPa** for 0.1 µm nuclei, **156 kPa** for 1 µm, **~102 kPa** for ≥10 µm. Empirically, 20–40 kHz sonication of air-saturated water cavitates at ~**0.1–0.15 MPa** ⚠️ (commonly cited; not re-verified here).
- At 4–8 kPa nominal, with a diffuse-field 3× local peak, worst case ~24 kPa → **4–25× below** the gassy-water threshold and ~40× below the degassed/tissue threshold. **Degassing is what buys this margin**, which is why every paper in the series insists on it.
- 🔧 Resonant-bubble caveat: Minnaert radius at 33 kHz is **~100 µm** — exactly the size of bubbles that nucleate on skin/hair/dish walls in warm water. Resonant bubbles have thresholds far below Blake and produce microstreaming shear well below inertial cavitation. In a 4 L degassed beaker this is controllable; in a 250 L tub it is the dominant unresolved risk (see section C).

### 3.5 Field geometry / "far field"
- Rayleigh distance of a 5 cm aperture at λ = 4.6 cm: z₀ = a²/λ = (2.5 cm)²/4.6 cm ≈ **1.4 cm**. So "7–10 cm above the transducer" is indeed beyond the near field — but only by 5–7 Rayleigh distances, and with a beam that is diverging strongly (sin θ ≈ 0.61λ/a = 1.1 → **no directivity at all**; the aperture is only ~1 λ across). 🔧 **There is effectively no beam.** The "far field" language is a formality: the 4 L beaker at 33 kHz is a **modal cavity** (a 15.2 cm × ~20 cm cylinder is ~3λ × 4λ), which is exactly why their own field map shows a 9× variation across the sample plane. Any replication must map the field with a hydrophone on a ≤λ/4 ≈ 1 cm grid and report the distribution, not a single number.
- 🔧 Practical implication: **beaker/tank geometry, water level, and the mesh/dish position are first-class experimental variables.** Copying "9–10 cm" without copying the vessel will not reproduce the field.

### 3.6 Hydrophone signal levels (for choosing instrumentation)
Sensitivity conversion: M[V/Pa] = 10^(M_dB/20) with M_dB in dB re 1 V/µPa, then ×10⁶.

| Hydrophone | Sensitivity | Output at 4 kPa peak | Output at 4 Pa |
|---|---|---|---|
| B&K 8103 (−211 dB re 1 V/µPa) | 28 µV/Pa | **113 mV** | 113 µV |
| Teledyne RESON TC4013 (−211 dB) | 28 µV/Pa | 113 mV | 113 µV |
| Aquarian AS-1 / H2a (−208 dB, with preamp ≈ −165 dB) | 40 µV/Pa bare; ~5.6 mV/Pa with H2a preamp | 160 mV bare / 22 V with preamp (clips) | 160 µV |
| Typical medical needle hydrophone (−265 dB) | 0.056 µV/Pa | 0.22 mV | 0.2 nV |

🔧 **This resolves the Figure S1B "<20 mV … ~180 mV" colour scale**: those readings are consistent with a **B&K/RESON-class underwater hydrophone (≈28 µV/Pa) seeing ~0.7–6.4 kPa**, i.e. **the kPa interpretation**, and are *not* consistent with a medical needle hydrophone or with 4 Pa. Use an underwater-acoustics hydrophone (or an Onda HCT + MCT meter, which is what they used), **not** a medical needle hydrophone whose calibration starts at 250 kHz–1 MHz.

### 3.7 Replication checklist implied by the physics
1. Resolve **Pa vs kPa** on your own rig by measuring with a calibrated hydrophone at a known drive voltage, and by cross-checking with a laser vibrometer/interferometer against the Tijore 1 kPa→11 nm table.
2. Map the field on a ≤1 cm grid; publish mean, SD, min, max over the sample plane (their own spread is ~9×).
3. Reproduce the **duty cycle to ±0.05 s** (their optimum is sharp at ±0.25 s) and the **frequency to ±0.05 %** (32.248 kHz was chosen over 33 and 39 kHz).
4. Degas, and **measure** dissolved O₂ — the whole safety and reproducibility argument rests on nuclei-free water.
5. Log water temperature (32–37 °C across the papers — itself an uncontrolled variable).
6. Consider that the inventors think **harmonic content may matter** (patent: rectangular wave, 2×–7× harmonics): record the drive waveform, don't assume a pure sine.
