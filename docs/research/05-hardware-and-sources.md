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

Order: **A** = adapted commercial bath; **B** = bare Langevin + custom low-power driver (**recommended**); **C** = multi-channel human bathtub; **D** = calibration, instrumentation, degassing, thermal and software, common to all three.

⚠️ Sourcing caveat for the whole of Part 2: the session's 200-call web-search budget was exhausted by the parallel component research, so later work relied on direct URL/sitemap traversal, vendor sitemaps and open APIs (BIPM KCDB, Crossref, OpenAlex, GitHub). Several vendors (AliExpress, Alibaba, eBay, Mouser, analog.com, st.com, thorlabs, RS, uspto.report, justia) block scripted access entirely and their prices could not be verified; every such item is flagged.

## Architecture A — adapted commercial ultrasonic bath

### A.1 Who actually sells 32–35 kHz
**No EU/US vendor sells 32.2–33 kHz off the shelf**, but **33 kHz is a genuine mass-produced Asian frequency** — it is the resonance of the standard 60 W bolted Langevin with a ~45–48 mm face (the dishwasher/washing-machine part), catalogued by at least three Chinese factories plus a whole Indian/Singaporean ecosystem.

| Frequency | Vendors | Relevance |
|---|---|---|
| 25 kHz | Branson GCX, Crest, Blackstone-NEY, Elma xtra ST, Bandelin Technik | too low |
| **30 kHz** | **Crest** push-pull transducers 240–720 W (in the POWERSONIC manual, not on the website) | closest Western |
| **33 kHz** | **Yunyisonic (CN), OKS (CN), Granbo (CN, transducer only), Pulisonic (CN), Alstron (SG), Analab / Spire / Bionics / Trans-o-sonic / Athena (IN)** | **exact target** |
| 35 kHz | Bandelin RK / DT / Super RK; Codyson CD-4831 | near |
| 37 kHz | Elma (all lines) | near |
| 40 kHz | Branson, Guyson, Bandelin smart ST, most Chinese benchtop, most own-brand | too high |
| "on request" | **Guyson HS3** — "other frequencies available on request" | only Western custom route |

### A.2 Western lab baths — specs, control, price (captured 2026-09-16)
| Vendor / model | Freq | Tank | HF nom/peak W | Power adjust | Sweep | Degas | Pulse | Heater | External trigger | Price |
|---|---|---|---|---|---|---|---|---|---|---|
| **Bandelin Super RK 103 H** | 35 kHz | **4.0 L**, 240×140×150 | 140 / 560 | **none** | SweepTec, **not defeatable** | no | no | 200 W, 30–80 °C | none | **€1 319** net ([link](https://bandelin.com/en/shop/sonorex-ultrasonic-baths/sonorex-super-rk-ultrasonic-baths/sonorex-super-rk-103-h-ultrasonic-bath-with-heater/)) |
| Bandelin RK 100 H | 35 | 3.0 L | 80 / 320 | none | always on | no | no | 140 W | none | €907 net |
| **Bandelin DIGITEC DT 103 H** | 35 | 4.0 L | 140 / 560 | none | always on | **yes** | no | 200 W | none | €1 427–1 521 inc VAT |
| **Bandelin DT 102 H-RC** | 35 | 3.0 L | 80 / 320 | none | always on | yes | no | 140 W | **IR remote; command set supplied free on request** | n/c |
| Bandelin DIGIPLUS DL | 35 | — | — | **20–100 % in 10 % steps** | yes | yes | — | yes | none | **discontinued** — best used-market target |
| **Bandelin smart ST 103 H** | **40** | 4.0 L | 140 / 560 | **10–100 %** | yes | yes | **interval 1–60 s** | 200 W | USB/Eth logging only | **€1 519** net |
| **Elma Elmasonic P 60 H** | **37 / 80 switchable** | 5.75 L (4.3 working), 300×151×150 | 180 / 720 | **30–100 % in 10 % steps** | **selectable (defeatable)** | yes + auto-degas | "+20 % amplitude" | 400 W | none | **CHF 1 886 / USD 2 399** |
| Elma P 30 H | 37/80 | 2.75 L | 120 / 480 | 30–100 % | yes | yes | yes | 200 W | none | CHF 1 410 |
| Elma EASY 40H | 37 | 3.9 L | 120 / 480 | none | none | none | none | 200 W | none | cheapest Elma |
| **Branson Bransonic CPX3800H** | 40 | 5.7 L | ~110 | **70 %/100 % only** | always on | yes ≤99 min | no | 180 W | none | **$1 487** |
| Crest Powersonic P500 | 45 / 132 | 1.4–5.4 gal | 120 | 9 steps | D/H/T variants | yes | — | 400 W | none (benchtop) | quote |
| Guyson GUK-15 | 40 | 15 L | 360 | adjustable | yes | yes | — | 500 W | undocumented | quote |
| VWR / Fisher / Cole-Parmer own-brand | 35/37/40 | — | — | — | — | — | — | — | none | ⚠️ unverified (403/JS-only); Fisher simply resells Branson CPXH |

Bandelin RK/DT 103 H is dimensionally perfect (4.0 L, 240×140×**150 mm** → the 7–10 cm standoff fits) and closest in frequency at 35 kHz — but has **zero power control, zero gating and non-defeatable sweep**. Elma P 60 H has the best control set of any lab bath but is 37 kHz with no external interface.

### A.3 Asian 33 kHz — the actual frequency match
**Yunyisonic (Shenzhen)** — the only turnkey 33 kHz benchtop line found. All SUS304, **0–100 % adjustable power**, sweep, pulse, degas, timer 1–9999 s, heater 20–80 °C, drain valve:

| Model | Tank | Internal mm | Transducers | US power | Heater | Price |
|---|---|---|---|---|---|---|
| YL0203-33 | 3.2 L | 240×135×100 | 2 × 50 W | 0–100 W | 300 W | $182.45 |
| ⭐ **YL0205-33** | **4.8 L** | **240×135×150** | 2 × 50 W | 0–100 W | 300 W | **$198.73** |
| YL0304-33 | 4.5 L | 300×150×100 | 3 × 50 W | 0–150 W | 450 W | $210.35 |
| YL0306-33 | 6.5 L | 300×150×150 | 3 × 50 W | 0–150 W | 450 W | $242.20 |
| **YL0614-33** | 14 L | 300×240×**200** | 6 × 50 W | 0–300 W | 600 W | $340.67 |
([source](https://www.yunyisonic.com/product/4-8l-100w-33khz-assisted-particle-dispersion-washing-burette/)) — 150 mm-deep tanks only just allow the 7–10 cm standoff; the 200 mm-deep YL0614-33 is comfortable at the cost of 14 L.

**Indian / Singaporean 33 kHz**: Analab Scientific **AU33-x series "33 ± 3 kHz"** (₹28k–67k); Spire Automation SAII-US-4, 4 L / 150 W, "33 ± 3 kHz" (quote); Bionics Scientific BST/USC "33 kHz ± 3"; **Alstron ALT-33xxxx** — "standard models are equipped with an ultrasonic frequency of 33 kHz", has sweep, but nothing below 12 L; Athena Technology 33 ± 3 kHz on the chiller series only (₹65 500 for 10 L / 500 W); Trans-o-sonic 33/25 kHz industrial only. ⚠️ **"33 ± 3 kHz" means 30–36 kHz** — looser than the 32.2–33 kHz window; measure every unit on arrival. ⚠️ Drawell DW-300DTY contradicts itself (title 25/33/40/59, spec table 25/28/40/59) — do not trust. Oscar Ultrasonics, Toshcon, Labman, Enertech, Sonic India publish no frequency at all.

### A.4 ⛔ The decisive caveat: a cleaning bath cannot be turned down to 4–8 kPa
**Step 1 — what a bath produces.** Bandelin RK 103 H: 140 W nominal HF over a 240×140 mm floor (336 cm²) ⇒ at 50–70 % efficiency, **0.21–0.29 W/cm² ⇒ 78–93 kPa** plane-wave equivalent. Cross-check: cleaning baths *do* cavitate, and the measured inertial threshold in air-saturated water at 25–33 kHz is **196–253 kPa** (Blake threshold, Hong & Son 2022; Viciconte et al. 2025) — at standing-wave antinodes a bath exceeds that. **Tens to hundreds of kPa is the right order.**

**Step 2 — the gap**: from 86 kPa you need **−20.6 dB to reach 8 kPa, −26.6 dB to reach 4 kPa** (from a more favourable 30 kPa at 7–10 cm: −11.5 / −17.5 dB).

**Step 3 — what the dial gives**: power dials are labelled in electrical power and pressure ∝ √P, so 40 % = −4.0 dB, 30 % = −5.2 dB, 20 % = −7.0 dB, **10 % (the best in the market, Bandelin smart ST) = −10.0 dB**. ⇒ **You need 12–27 dB; the best dial gives 10 dB. Even optimistically you remain 6–16 dB hot, and blind without a hydrophone.**

**Step 4 — is "power %" a burst chop?** Only two vendors answer in writing:
- **Branson GCX** (verbatim): *"True variable power control makes the cavitational intensity **(not duty cycle)** infinitely and linearly variable from 20 % to 100 %."* → real amplitude control.
- **Crest GTI/GPI**: closed-loop constant-power regulation with "amplitude limiting" indicator, **4–10 V external power setpoint**, and **duty cycle: 100 % continuous**.
- **Elma**: the manual only says "can be set between 30 % and 100 % in steps of 10 %" — ⚠️ **mechanism never stated** (circumstantial: their Pulse mode is described as "an increase of the *amplitude*", their Degas as "specialized *modulation and clocking*").
- **Branson CPXH**: "lower the *amplitude*… manipulating the output waveform" — hedged, two steps only.
- **Chinese OKS** states outright that its generator "uses a **pulse width control**" — PWM of the half-bridge at the carrier: monotonic but uncalibrated, and it changes harmonic content.
🔑 **If a bath's "%" were an audio-rate burst chop, the consequence is not envelope impurity — it is that the pressure *during* each burst is still 80+ kPa, i.e. cavitating.** You would be running a cavitating ~100 kPa field at low duty, not a 4 kPa field. That is the fatal failure mode.

**Step 5 — mains modulation.** Every lab bath uses "double half-wave operating mode" (Bandelin's phrase) or "line modulated sine wave output" (Blackstone-NEY) — hence the universal 1:4 nominal:peak ratio. The carrier is **already amplitude-modulated at 100/120 Hz**; your 1.5 s gate would be a slow envelope on a fast one. Only **Crest** specifies 100 % continuous duty.

**Step 6 — sweep.** Bandelin SweepTec is permanently on and not defeatable (RK/DT/smart ST); Branson CPXH sweep always on; Blackstone-NEY ±1 kHz at 25 kHz / ±2 kHz at 40 kHz. A ±1 kHz swept carrier is a ±3 % frequency smear on a protocol specified to 32.248 kHz. Only **Elma P (selectable), Branson GCX (user-set bandwidth and rate) and Crest** let you control it.

**How much acoustic power you actually need** over that same 240×140 mm floor: **182 mW at 4 kPa, 726 mW at 8 kPa** — i.e. **under 2 % of one 60 W transducer**, 0.2–0.9 % of a 140 W bath, ≈0.4–1.5 W electrical, which into a 33 kHz Langevin (|Z| < 20 Ω at resonance) is **3–5.5 V rms**. You are not "turning a bath down"; you are asking it to run three orders of magnitude below design point.

### A.5 Remote / enable inputs (for the 1.5 s gate)
| Product | Interface | Confidence |
|---|---|---|
| ⭐ **Crest POWERSONIC GT/GTI/GPI/GPS** | 25-pin SUB-D: **ultrasonic enable = potential-free contact to GND (~5 V / 2 mA)**; external power setpoint **4–10 V** (40–100 %); power monitor 0–10 V out; error relay; panel lock ([manual](https://crest-ultrasonics.com/wp-content/uploads/2021/03/manual-powersonic-generators-gt-gti-gpi-gps.pdf)) | best documented ⚠️ line being "streamlined" — confirm current model keeps the I/O |
| ⭐ **Branson GCX** | "OEM connection — external control ultrasonic on/off", 25-pin D-shell, RS-485, local/remote switch ([datasheet](https://www.branson.emerson.com/is/content/emerson/en/corporate/branson/documents/branson-gcx-ultrasonic-generator.pdf)) | excellent, but 25/40/80/120/170 kHz only |
| Bandelin DT-xxx-RC | IR interface, command set free on request | only lab-bath-level interface; ⚠️ IR latency at 0.33 Hz gating unproven; drops to IP 23 |
| Bandelin LG generators | RS-232 + "remote-control socket" | ⚠️ dry-contact capability unverified |
| **OKS-QXDY generator (33 kHz!)** | "supports remote control connection and PLC system integration" | ⚠️ **electrical form undocumented** — the single biggest open question on the Asian route |
| Bandelin smart ST | built-in interval 1–60 s in 1 s steps | ⚠️ 1 s integers ≠ 1.5 s, and it is 40 kHz |
| Elma P/Select/EASY, Branson CPXH, Skymen, Granbo | **none** | mains switching only — **don't** (µC reboot + soft start every 3 s) |

### A.6 Components: immersibles, generators, bare transducers
| Item | Freq | Power | Price | MOQ |
|---|---|---|---|---|
| **OKS immersible plate** | 20/25/28/30/**33**/40/54/68/80/100/125/200 kHz | 300–3000 W | **$650** | 1 |
| **OKS-QXDY generator** | **33 kHz standard option** | 300–3000 W | **$238** | 1 |
| OKS-HJPCBDY driver PCB | 20/25/28/30/**33**/40…, sweep 23–40 kHz adjustable, auto frequency tracking | 300–3000 W | **$55** | 1 |
| OKS-DLB600W driver board | 20–40 kHz (25/28/**33**/40) | 50–600 W | $140 | 1 |
| PLS-WDLB2000W (Pulisonic) | 25–40 kHz incl. 33 | 2000 W | $230 | 1 |
| ⭐ **OKS-QXHUNQ33K transducer** | **33 ± 0.5 kHz**, PZT-8, 48 mm face × 62 mm, Cs 4800 pF, Z ≤ 20 Ω | 60 W | **$7.50** | **1** |
| Granbo GB4-5533-60W | **33 ± 0.5 kHz**, 55×56 mm, Cs 5000 pF | 60 W | $13 (1–49) / $6 (100+) | 10 |
| Pulisonic 33 K dishwasher transducer | 33 kHz | 60 W | $6.80 | 1 |
| Skymen / Granbo immersibles | 28 / 40 only | 300–2400 W | quote / $423–1 446 | — |
| Bandelin Tauchschwinger T3169 | 25 / 40 | — | €3 771 inc VAT | — |
⚠️ ±0.5 kHz = 32.5–33.5 kHz: brackets but does not guarantee 32.2–33 kHz — **buy 5–10 at $7.50 and bin them with a NanoVNA**, then drive at a *manually set* frequency rather than letting an auto-tracking generator hunt.

### A.7 Verdict on Architecture A
| Rank | Option | Cost | Risk |
|---|---|---|---|
| 1 ⭐ | **Bare 33 kHz Langevin ($7.50–13) + your own wideband amp + function generator** (→ Architecture B) | <€200 + amp | you build the matching network and characterise the field |
| 2 | **Yunyisonic YL0205-33 ($199) / YL0614-33 ($341)** used as a *tank + bonded transducer + heater assembly*, stock generator replaced by your driver | $199–341 | stock generator is still 100–500× too hot; built-in "Pulse" period undocumented and almost certainly ≪1.5 s |
| 3 | OKS 33 kHz immersible ($650) + QXDY generator ($238) | $888 | interface form unknown; 300 W minimum ≈ 400× target |
| 4 | Crest POWERSONIC (30 kHz push-pull) + immersible | quote | best-documented control anywhere (dry contact, 4–10 V setpoint, 0–10 V readback, 100 % duty) but 30 ≠ 33 kHz, legacy line |
| 5 | Guyson HS3 custom frequency | quote + NRE | only Western vendor advertising custom frequencies; interface undocumented |
| 6 | Branson GCX (25 kHz) | quote | only written "amplitude, not duty cycle" guarantee + dedicated US on/off |
| 7 | Bandelin RK/DT 103 H | €1 319 | perfect geometry, 35 kHz, available today — but no power control, no gate, sweep always on, mains-modulated. ⭐ **Buy one as the *positive control* for cavitation tests, not as the source** |

## Architecture B — bare Langevin / PZT transducer + custom low-power driver (**the recommended route**)

> Provenance note: the component agent could not find the ring/cone details in the papers it reached and flagged them as unverified. **They are verified** — see Part 1c: they are in the *Methods* of Tijore et al., *Bioeng Transl Med* 2025 (PMC11883105), and "135–275 V / 4–8 Pa" is on Figure S1A of the Aging Cell supplement (PMC12151899, file `ACEL-24-e70008-s001.docx`). Both files are in the scratchpad.

### B.0 The two reference implementations to copy
| | Sheetz/Singapore rig (BTM 2025) ✅ | Tijore IISc rig (2026) ✅ |
|---|---|---|
| Transducer | PZT4 rings **25×10×4 mm** and **16×8×4 mm** (Beijing Ultrasonic) + **aluminium cone** to ~5 cm, epoxy + silicone coated | **APC International Langevin, APC 90-4050** |
| Mounting | glued to tank bottom | epoxy-bonded to a steel container on a 3D-printed XYZ platform |
| Drive | "signal generator & amplifier" (unnamed), 200/300/400 V labels | **PiezoDrive PDU 210 ultrasonic driver** |
| Tuning | not described | **impedance analyser** calibration |
| Pressure measurement | Onda MCT-2000 cavitation meter (+HCT probe) | **FEL Communications hydrophone → Digilent 410-321 (Analog Discovery 2) USB scope** |
| Water | degassed DI, 37 °C, tank in an incubator | **vacuum-degassed**, tank on a temperature-regulated metal stage |
| Sample | 8 cm above transducer, parafilm-sealed dishes on a mesh | 3D-printed height-adjustable dish tray |

🔧 The IISc rig is the one to clone: every element is a catalogue part, and they publish a pressure↔displacement calibration (1 kPa → 11 nm) you can check yourself.

### B.1 Transducers — what you can actually buy
⭐ **A stock 33 kHz Langevin exists and costs $8.50.** (Verified on live vendor pages, Sep 2026.)

| Model | Freq | Power | Face Ø | Length | C₀ | Zm | Material | Price | URL |
|---|---|---|---|---|---|---|---|---|---|
| **BJC-3360T-48HS** | **33 ±1 kHz** | 60 W | **48 mm** | 58 mm | 3800 pF | 10–20 Ω | PZT-8 | **$8.50** | [bjultrasonic](https://www.bjultrasonic.com/shop/33khz-60w-ultrasonic-cleaning-transducer/) |
| BJC-30100T-68H | 30 ±1 kHz | 100 W | 68 mm | 61 mm | 5200 pF | 10–20 Ω | PZT-8 | $13.50 (OOS) | [link](https://www.bjultrasonic.com/shop/30khz-100w-ultrasonic-cleaning-transducer/) |
| BJC-2860T-59HS | 28 ±1 kHz | 60 W | 59 mm | 68 mm | 3800 pF | 10–20 Ω | PZT-4 | $7.00 | [link](https://www.bjultrasonic.com/shop/28khz-60w-ultrasonic-cleaning-transducer/) |
| BJC-2560T | 25 ±1 kHz | 60 W | 59 mm | 77 mm | 5400 pF | 10–20 Ω | PZT-4 | $7.00 | [link](https://www.bjultrasonic.com/shop/25khz-60w-ultrasonic-cleaning-transducer/) |
| Oksultrasonic 33 kHz | 33 kHz | — | — | — | — | — | — | $6.50, MOQ 1 | [made-in-china](https://oksultrasonic.en.made-in-china.com/product/WKvJzMtAXspS/China-Small-Ultrasonic-Transducer-for-Cleaning-28kHz-33kHz-40kHz-54kHz-120kHz.html) |
| Granbo 33 kHz 60 W | 33 kHz | 60 W | — | — | — | — | — | $13/10 pc, $6/100 pc | [made-in-china](https://granbosonic.en.made-in-china.com/product/hURpqmrgFYWE/China-60W-Ultrasonic-Cleaning-Transducer-for-Efficient-Heavy-Duty-Applications-with-Efficient-33kHz-Frequency.html) |

**33 kHz is a Chinese-catalogue frequency and is absent from every Western catalogue.** Western options:

| Vendor | Nearest parts | Price | Notes |
|---|---|---|---|
| **Steminc** (Miami) | SMBLTD63F25H2 25 kHz $67.85; **SMBLTDF30H100 30 kHz $80.52** (C₀ 5 nF, Zm ≤25 Ω, Qm 1000); SMBLTD45F40H 40 kHz $47.49 | $46–81 | MOQ 1, but ⚠️ **$76–90 shipping for the first unit**, weekly batches, all sales NCNR ([catalogue](https://www.steminc.com/PZT/en/bolt-clamped-langevin), [shipping](https://www.steminc.com/PZT/en/shippinginfo)). **No 33 or 35 kHz** |
| **APC International** | 28/40/50/80/120 kHz ultrasonic power transducers | ⚠️ quote-only | [page](https://www.americanpiezo.com/products-services/ultrasonic-power-transducers/). The exact part used by the Tijore lab, **APC 90-4050**, is a catalogue/quote item — ⚠️ I could not retrieve its datasheet (product URL 404s; site search is JS-only) |
| Sinosonics | 35 kHz 300–500 W $170; 30 kHz 800 W $200 | $170–200 | over-powered by ~10⁴ for this use |
| PI Ceramic, CTS/Meggitt, SinapTec | 20–80 kHz | RFQ only | |
| ⛔ Hainertec | — | — | domain parked / 403 — unverifiable |

**The exact PZT4 rings from the papers, in stock** ✅:

| Part | OD×ID×T | C₀ | Radial f_r | Thickness f_t | Zm | Qm | Price |
|---|---|---|---|---|---|---|---|
| Ring 25×10×4 (PZT4/5/8 selectable) | 25 × 10 × 4 mm | 935 pF ±10 % | **66 kHz** | 512 kHz | ≤15 Ω | ≥800 | **$22 / pack** ([link](https://www.bjultrasonic.com/shop/5pcs-25104-ring-piezoelectric-ceramic/)) |
| Ring 16×8×4 | 16 × 8 × 4 mm | 340 pF ±10 % | **96 kHz** | 512 kHz | ≤20 Ω | ≥800 | **$20 / pack** ([link](https://www.bjultrasonic.com/shop/5pcs-1684-ring-piezoelectric-ceramic/)) |
| Cheaper equivalents | 25×10×4 | — | — | — | — | — | $4.00/pc [Sinosonics](https://www.sinosonics.com/shop/piezo-ceramic-ring-25mm/); $0.10–0.30/pc at 50+ [Shouguang Feitian](https://fttransducers.en.made-in-china.com/product/naDplkIyIArz/China-Factory-Direct-Different-Size-Piezoelectric-Ceramic-Rings-for-Ultrasonic-Cleaning.html) |

⚠️ Pack size ambiguous (titles say 10 pc, slugs say `5pcs-`, shipping weight says 5) — confirm before paying.

🔑 **Critical insight**: at 32.248 kHz these rings sit at **~½ their radial resonance and ~1/16 their thickness resonance** — they are quasi-static capacitive drivers. **The 33 kHz comes entirely from the half-wave longitudinal resonance of the bolted column** (steel back mass + rings + aluminium front mass/cone + preload bolt). You cannot buy "33 kHz rings"; ring size only sets C₀ and power handling (2× 25×10×4 ≈ 1.87 nF; 2× 16×8×4 ≈ 0.68 nF). Bolt preload (~20–30 MPa) is a design parameter and the most common DIY failure. ⚠️ Beware Steminc's "PZT-8 Ring 50 mm 33 kHz" (SMR5020T5811, $42.20) — that 33 kHz is the ring's free *radial* mode, not a transducer resonance.

**Ordering to Italy**: Beijing Ultrasonic is a normal WooCommerce shop — MOQ 1, PayPal, ships in 48 h by DHL (≤10 days); custom parts 10–30 days; 1-year warranty. Budget **22 % Italian import VAT + ~€15 DHL handling**; ⚠️ freight quoted only at checkout (est. $35–60 for ~1.5 kg). Piezoceramics are RoHS-exempt and not dual-use controlled at these ratings.

### B.2 Impedance, matching, and the aluminium cone
**Butterworth–Van Dyke**: motional Rm–Lm–Cm ∥ static C₀. Measured anchors from the literature:
- 30 kHz Langevin **radiating into water**: f_r 30.90 kHz, f_a 31.26 kHz, |Z|min **130.7 Ω**, |Z|max 13.59 kΩ, **η = 6.36 % CW / 8.43 % pulsed, 9.73 W acoustic at 200 Vpp** ([PMC9696829](https://pmc.ncbi.nlm.nih.gov/articles/PMC9696829/)).
- 40 kHz underwater transducer BVD: C₀ 4.40 nF, R₁ 20.64 Ω, L₁ 139.5 mH, C₁ 448.8 pF ⇒ **Qm ≈ 854, BW ≈ 23 Hz** ([PMC11768801](https://pmc.ncbi.nlm.nih.gov/articles/PMC11768801/)).

**Series inductor to tune out C₀**, L = 1/((2πf)²C₀) at 32.248 kHz:

| C₀ | \|X_C₀\| | L |
|---|---|---|
| 0.68 nF (2× 16×8×4) | 7258 Ω | 35.8 mH |
| 1.87 nF (2× 25×10×4) | 2639 Ω | 13.0 mH |
| **3.8 nF (BJC-3360T)** | **1299 Ω** | **6.41 mH** |
| 5.4 nF | 914 Ω | 4.5 mH |
| 80 nF (20-element immersible pack) | 60 Ω | 0.29 mH |

Why the series L, in order of importance at these power levels:
1. ⭐ **Voltage step-up by Q-multiplication** — this explains "135–275 V": with X_C₀ = 1299 Ω and ~50 Ω of loss, Q ≈ 25, so a **24–48 V bus produces 135–275 V across the piezo with no HV supply**.
2. **Harmonic suppression** — a series LC tuned at f₀ presents 2.67·X₀ at the 3rd harmonic; with Q = 20 the 3rd falls from 33 % to ~0.6 %.
3. Cancelling reactive current — least important here (at resonance reactive current is only ~8 % of motional current).
⚠️ Inductor Q sets the achievable step-up: at 32 kHz a 13 mH coil with Q = 30 adds 88 Ω of loss, Q = 100 adds 26 Ω. Use a ferrite pot/gapped E-core, **not** an iron-powder choke.

**Measuring resonance** — ⭐ **NanoVNA-H/H4 (€50–90), S21 series-through**: O/S/L calibrate, DUT between CH0 and CH1, the S21 LOGMAG dip is f_r ([procedure](https://0x9900.com/measure-resonance-using-a-nanovna/)); within ~1 % of a lab impedance analyser. Cheap alternative: function generator + series sense resistor + scope. **Measure every unit** — a ±1 kHz vendor tolerance is 20–60 bandwidths wide.

⚠️ **The under-appreciated risk: thermal drift.** Loaded Qm in water 100–500 ⇒ BW 65–320 Hz, while Langevin df/dT is typically −5 to −20 Hz/°C. A 5 °C rise moves you 0.2–0.9 bandwidths off resonance, so **an open-loop fixed-frequency drive will not hold constant pressure over a 30-minute exposure.** Mitigate by re-tuning from live current/phase, PLL tracking, deliberately lowering Q, or hydrophone monitoring throughout. Note the tension: commercial cleaning generators do track — but they also sweep ±0.5–2 kHz, which destroys the fixed-frequency protocol.

**Gating is benign**: envelope τ = Q/(πf) ⇒ 1–8 ms, ring-up/down 5–42 ms, <3 % of the 1500 ms gate. Gate at a zero crossing with a 1–5 ms raised-cosine envelope.

**What the cone really does** 🔧 (baffled-piston numbers):

| Aperture | ka | R_r (norm.) | D₀ | DI | −6 dB half-angle |
|---|---|---|---|---|---|
| 16 mm | 1.09 | 0.49 | 2.44 | 3.9 dB | >90° (near-omni) |
| 25 mm (bare ring) | 1.71 | 0.90 | 3.25 | 5.1 dB | >90° |
| **50 mm (cone)** | **3.42** | **1.02** | **11.5** | **10.6 dB** | **40°** |
| 100 mm | 6.84 | 0.99 | 47.2 | 16.7 dB | 19° |

The cone **narrows** the beam, not widens it (the papers' wording is loose); its real functions are to enlarge the aperture, raise radiation resistance from 0.90 to 1.02 (⇒ ~4.5× more power radiated for the same face velocity) and act as a velocity transformer. At 7–10 cm a 40° half-angle already covers ~17 cm — enough to insonify a dish or a mouse. ⚠️ Adding a cone to a stock 33 kHz unit pulls f_r down by several kHz. 🔧 **Since the BJC-3360T already has a 48 mm face ≈ the papers' "~5 cm", consider skipping the cone entirely.**

### B.3 Signal generation
1.5 s ON at 32 248 Hz = **48 372 cycles exactly**; burst period 3.000 s; 600 repeats per session.

| Model | Freq resolution / accuracy | Amplitude | 1.5 s on/off gating | Price |
|---|---|---|---|---|
| ⭐ **Siglent SDG1032X** | 1 µHz, ±25 ppm | 20 Vpp HiZ | ✅ best — N-cycle/gated, internal burst period 1 µs–1000 s, SCPI-scriptable | **$299–359** ([Saelig](https://www.saelig.com/product/sdg1032x.htm)) |
| Rigol DG1022Z | 1 µHz, **±1 ppm** | 10 Vpp/50 Ω | ✅ N-cycle + internal period 1 µs–500 s (⚠️ "Gated" needs an external trigger) | $249 ([TestEquity](https://www.testequity.com/product/31530-1-DG1022Z)) |
| FeelTech FY6900 | 1 µHz, ±20 ppm | ~24 Vpp | ⚠️ indirect — use CH2 at 0.333333 Hz as the trigger; **verify on a scope** | ~$70 |
| JDS6600 / Koolertron | same DDS family | ~24 Vpp | ⚠️ same CH2-trigger architecture | €55–190 ⚠️ |

**MCU / DDS alternatives** (frequency error vs the 65–320 Hz transducer bandwidth):

| Source | Resolution / error at 32.248 kHz | Note |
|---|---|---|
| AD9833 (28-bit, 25 MHz) | 0.093 Hz step | ~0.65 Vpp out, needs gain, €3–8 ⚠️ (datasheet values from general knowledge — analog.com blocked) |
| AD9850 / AD9851 (32-bit) | 0.029 / 0.042 Hz | €4–12 |
| RP2040 NCO + DMA→DAC | 0.116 µHz at 500 kSa/s | ⭐ cleanest |
| RP2040 PWM ÷3876 | 32 249.7 Hz = **+54 ppm** | ✅ adequate |
| ESP32 ÷2481 / STM32F4 ÷5210 | −91 / −72 ppm | ✅ adequate |

🔧 **Integer PWM division is good enough** — every modern MCU lands within ±3 Hz, and crystal tolerance (±30 ppm ≈ ±1 Hz) dominates. The problem with PWM is that it is a *square wave*, not that it is mistuned, and the tuned tank fixes that.

### B.4 Amplifiers
**Lab RF amps are the wrong tool** (50 Ω source into a capacitive load, 20–1000× overkill): E&I 240L (10 kHz–12 MHz, 40 W, ⚠️ ~$1.5–3 k used), AR 25A250A (25 W, **$5 995 used**, [AccuSource](https://accusrc.com/product-Amplifier-Research-25A250A-11450)). ⭐ The exception is the **Krohn-Hite 7500** (DC–1 MHz, 75 W, **140 Vrms open-circuit, 625 mA**, THD <0.05 %): **$2 370 new** ([DigiKey](https://www.digikey.com/en/products/detail/krohn-hite-corporation/7500/13283314)), **$1 495 used** ([AccuSource](https://accusrc.com/product-Krohn-Hite-7500-9480)) — a voltage-source output whose 140 Vrms brackets the "135–275 V" range.

⭐ **Piezo-specific drivers are the sweet spot** (prices verified on piezodrive.com):

| Model | Output | Bandwidth | Current | Fit at 33 kHz | Price |
|---|---|---|---|---|---|
| ⭐ **PiezoDrive PDm200** | +100 V to ±200 V | signal 200 kHz, **power BW 63 kHz @100 Vpp** | 300 mA | ✅✅ 200 Vpp into 4 nF = 166 mApp | **$330** |
| PDu150 (3-ch) | −30…+150 V | power BW 80 kHz | 100 mA/ch | ✅ marginal at C₀ 4 nF | $413 |
| MX200 | ±200 V | ⚠️ n/s | 1 A | ✅ most headroom | $545 |
| **PDUS210** (what the Tijore lab uses, "PDU 210") | **0–800 Vpp**, sine only, isolated output, 210 W max, **20–200 kHz** (6 kHz–500 kHz with modification), USB/RS485 API, 4 DIO, single & continuous pulse generation, series **or parallel (anti-)resonance tracking**, 1 ms frequency update | — | 32 Ap-p max | 🎯 purpose-built; **variants**: -800 (282 Vrms, Zopt 400 Ω), **-400 (141 Vrms, Zopt 100 Ω)**, -200, -100, -50 | **$4 141** ([PiezoDrive](https://www.piezodrive.com/ultrasonic-drivers/), [specs](https://www.piezodrive.com/drivers/pdus210-ultrasonic-driver/)) |
| ⚠️ Thorlabs MDT694B | 0–150 V | ⚠️ likely only a few kHz into capacitive loads → probably unusable | — | verify first | ~$1 200 ⚠️ |

🔧 Note how well the **PDUS210-400 variant (400 Vpp / 141 Vrms, optimal load 100 Ω, 20–200 kHz)** matches both the "135–275 V" slide and the measured |Z|min ≈ 130 Ω of a 30 kHz Langevin in water. If you want to *be* the reference rig, this is the part — at 12× the price of the whole budget build.

**Cheap path — can audio class-D pass 33 kHz? Yes** 🔧 (computed from TI datasheet filter values):

| Output filter | f_c (differential) | \|H\| at 32.2 kHz (8 Ω) | Verdict |
|---|---|---|---|
| TPA3116: 10 µH + 680 nF | 43.2 kHz | +2.3 dB | ✅ passes as-is |
| TPA3255: 10 µH + 1 µF | 35.6 kHz | +3.9 dB | ⚠️ on the knee |
| TPA3251: 22 µH + 680 nF | 29.1 kHz | attenuated | ❌ |
| **Modified 10 µH + 220 nF** | **75.9 kHz** | flat | ✅✅ one-component fix, still 29 dB rejection at 450 kHz |

⚠️ **The real class-D gotcha is damping, not bandwidth**: filter Q = R√(C/L_eff) — 4 Ω speaker Q 0.89 (flat); Langevin at series resonance (~30 Ω) Q 6.7 (peaking, burst-edge ringing); at anti-resonance (~1 kΩ) **Q ≈ 224 → catastrophic peaking, oscillation or shutdown**. Fix with a Zobel (R ≈ √(L_eff/C) ≈ 4.5–6.7 Ω + 470 nF) or simply hang a 4–8 Ω power resistor across the transducer (wasting watts is irrelevant at 42 mW acoustic). Avoid Bluetooth/DSP boards (20 kHz anti-alias filters). Class-D outputs are floating BTL — awkward with a grounded hydrophone.

🔧 **Class-AB is more defensible for a bioeffect experiment** (no output LC ⇒ no corner, no ringing, no 400 kHz switching residue near the hydrophone): **LM3886** GBWP 8 MHz, slew 19 V/µs ⇒ at A_v = 21 closed-loop BW ≈ 380 kHz, and 28 Vpk at 33 kHz needs only 5.8 V/µs — €12–25 a kit. TDA7293 swings ~90 Vpp but needs 9.3 V/µs against a 15 V/µs limit ⚠️.

**Step-up transformer**: ⭐ hand-wound ferrite toroid (3C90/N87, ~20:180 turns) — €3, flat 5 kHz–300 kHz, 1:8 from 40 Vrms = 320 Vrms. ⚠️ 70/100 V line-audio transformers are only specified to 15–18 kHz (try, but measure). ❌ Never reverse a 50 Hz mains toroid.

### B.5 Half/full-bridge direct drive
- **Gate drivers**: ⭐ **UCC27714** (600 V, 4 A, 3.3 V logic, [datasheet](https://www.ti.com/lit/ds/symlink/ucc27714.pdf)) or **IR2104/IR2184** (single PWM input, built-in deadtime, and an **SD pin that doubles as the 1.5 s hardware gate**). Avoid bare IR2110 (no deadtime).
- **MOSFETs**: ⭐⭐ low-voltage devices + transformer (IRF540N/IRFZ44N from 24–48 V into 1:8) beat a 400 V bus; at 33 kHz and a few watts, switching loss is irrelevant, so optimise for gate charge and safety. If you must go HV, use modern superjunction (STP12NM50N, IPP60R125P6), not IRF740 (no margin on 400 V) or IRFP460 (huge Qg).
- **DC bus needed for 135–275 Vrms** (full bridge, fundamental RMS = 0.900·V_dc):

| Target | Untuned | Series-L tuned, Q≈10 | 1:8 transformer |
|---|---|---|---|
| 135 Vrms | 150 V | **~15 V** | ~19 V |
| 275 Vrms | 306 V | **~31 V** | ~38 V |

🔧 **A 48 V bus covers the entire range — there is no reason to put 300–400 V on a bench for a 42 mW experiment.**
- **Square-wave harmonics**: 3rd at 33.3 % (−9.5 dB), 5th at 20 %, THD 48.3 %. This matters because your result will be attributed to "33 kHz" while ~11 % of the power is at 99 kHz; harmonics can excite spurious radial/flexural modes; and they inflate the measured peak pressure in a flattering direction. Series L + the transducer's own narrowband resonance cuts the 3rd to ~0.6 %. **Verify with an FFT.** (But note: the patent explicitly contemplates exploiting rectangular-wave harmonics — so *document* the waveform rather than assuming which is "correct".)
- ⚠️ **Skip AliExpress "ultrasonic cleaner driver boards"**: trimmers cover only ±2–5 kHz around nominal (a 40 kHz board will never reach 33 kHz) and most auto-track frequency, destroying the one variable you are controlling. ⛔ Marketplace prices unverifiable (AliExpress/Alibaba CAPTCHA, eBay 403).

### B.6 Potting and waterproofing
⭐ **Acoustic matching is a non-issue at 33 kHz** 🔧 — λ = 44.8 mm, λ/4 = 11.2 mm, so a proper matching layer would be a **19 mm slab**, not a coating. Three-layer transmission Al→coating→water:

| Coating | 1 mm | 2 mm | 3 mm | 5 mm |
|---|---|---|---|---|
| bare Al/water | T = 0.2903 | | | |
| epoxy (Z 2.85) | +0.01 dB | +0.06 dB | +0.14 dB | +0.40 dB |
| filled epoxy (Z 4.75) | +0.02 | +0.08 | +0.19 | +0.53 dB |
| polyurethane (Z 1.80) | +0.01 | +0.06 | +0.15 | +0.40 dB |
| silicone (Z 1.08) | −0.13 | −0.48 | −0.94 | −1.86 dB |

2 mm of epoxy at 33 kHz is only **9° of phase**. ⭐ **Mass loading beats impedance mismatch**: 3 mm of epoxy over a 50 cm² face adds ~18 g to the vibrating tip and pulls f_r down — so **pot first, then measure f_r, then set the generator.** Reference impedances (MRayl, from [Onda's tables](https://www.ondacorp.com/wp-content/uploads/2020/09/Liquids.pdf)): water 1.48 (20 °C) / 1.51 (35 °C); Sylgard 184 1.08; RTV-60 1.41; **sonar PU (Ren RP-64xx) 1.54–1.63** (why PU is the hydrophone-window material); unfilled epoxy 2.85; filled epoxy 3.1–4.7; PMMA 3.26; aluminium 17.33; PZT-4 ~34.5 ⚠️.

| Product | Why | Price |
|---|---|---|
| ⭐ **Loctite EA E-30CL** | best default — 10 500 cP flows void-free, clear (inspectable), 19.7 kV/mm | ~$25–35 / 50 mL |
| Loctite EA E-120HP | toughened, 25 kV/mm, but ⚠️ 1000 h salt fog → 45 % of initial strength; an adhesive, not an immersion barrier | $24.46 / 50 mL |
| ⭐ **Conathane EN-9** | TDS names it for "cable and connector potting… watertight electrical connectors"; PU hydrolytic stability | ⚠️ quote |
| Smooth-On ReoFlex 40 | SG 1.02 ⇒ Z ≈ 1.7 MRayl, 1500 cP, no degassing needed | trial 0.91 kg |
| West System 105/206 | cheapest per kg, EU stock; ⚠️ no water-absorption or dielectric data published | ~€37/kg |
| Araldite 2011 | best EU high-street structural epoxy | €25–40 / 50 mL |
| Sylgard 184 | Z 1.08 (closest to water) but ⚠️ €279 / 1.1 kg at Farnell IT | €279 |

⚠️ Uralite 3140 **no longer exists** (discontinued Hexcel/Ren name); 3M Scotchcast 2130/2131 are **polyurethane, not epoxy**, and discontinued/obsolete.
**Two silicone traps**: (1) **acetoxy RTV releases acetic acid — corrosive to aluminium and piezo electrodes**; use neutral-cure or addition-cure PDMS. (2) Addition-cure PDMS is **inhibited by amines** — amine-cured epoxy leaves Sylgard permanently tacky (test on a coupon), and unfilled PDMS has **no adhesion** to aluminium or cured epoxy without a silane primer, so unprimed silicone over epoxy creates a water path and is worse than nothing. ⭐ Correct order: **epoxy underneath as structure + dielectric; a thin silicone skin on top only**.
**Cable entry**: ⭐ Blue Robotics potted penetrator **$5–6**, or **WetLink compression penetrator $13–17, 1000 m rated, re-openable** ([link](https://bluerobotics.com/store/cables-connectors/penetrators/wlp-vp/)). ⚠️ SubConn is quote-only and rated only 300 V. ⚠️ **IP68 ≠ permanently submerged** (1 m/30 min mated test). The failure nobody warns about: **multi-conductor cable wicks water inside the jacket, past any gland, for metres**. ⭐ Best answer for a tank rig: **zero connectors in the water** — one continuous cable from the transducer over the rim to a dry driver.

**"Generators encased in epoxy within the baths"** — ⚠️ don't. Heat is survivable, but 600 gate cycles/session against a 50–80 ppm/K CTE cracks rigid epoxy and a crack is a water path to a live node; electrolytics cannot vent; there is **zero serviceability** (fatal for a project that needs iterative retuning); and any void becomes a partial-discharge site at 275 V/33 kHz. Every commercial immersible puts **only transducers** in the sealed box and the generator in a rack outside.

### B.7 Immersible transducer packs — the wrong purchase
| Vendor | Freq | Power | Plate | Price | Generator |
|---|---|---|---|---|---|
| Beijing Ultrasonic 300 W | 25/28/40 kHz ("other freq: contact us") | 5 × 60 W | 200×200×100 | **$400** | separate |
| Beijing Ultrasonic 600 W | same | 10 × 60 W | 500×350×100 | $625 | separate |
| Beijing Ultrasonic 1200 W | same | 20 × 60 W | 500×400×100 | $958 | separate |
| Yunyisonic | 28/40 kHz | 300–2400 W | SUS304 | $398–2012 | bundled at top end |
| Crest, Blackstone-NEY, Elma, Bandelin, Telsonic, Tovatech | — | — | — | ⚠️ quote only | separate |

⚠️ **33 kHz packs are essentially unobtainable off the shelf.** And electrically they are the wrong load:

| N elements | C₀ total | \|X_C₀\| @33 kHz | R_r parallel | L to tune | V for 3 W | I for 3 W |
|---|---|---|---|---|---|---|
| 1 | 4.0 nF | 1206 Ω | 15 Ω | 5.8 mH | 6.7 V | 0.45 A |
| 5 (300 W) | 20 nF | 241 Ω | 3.0 Ω | 1.16 mH | 3.0 V | 1.00 A |
| **20 (1200 W)** | **80 nF** | **60 Ω** | **0.75 Ω** | 291 µH | **1.5 V** | **2.00 A** |

⚠️ A 1200 W pack presents **0.75 Ω** — at 200 V you would be asking for 53 kW and destroy it in under a second; and 80 nF at 200 V draws **3.3 A of purely reactive current** while delivering milliwatts. Any custom pack driver must be low-voltage/high-current, the opposite of the reference design. ⚠️ No vendor states whether a matching inductor is inside — **measure with an LCR meter before connecting anything**. ⭐ Buy the $8.50 BJC-3360T instead.

### B.8 Independent physics check by the component agent 🔧 (complements Part 3)
The plane-wave-at-the-face model **understates** the required power, because 4 kPa is specified at 7–10 cm in the far field (Rayleigh distance of a 5 cm aperture at 33 kHz is only 13.6 mm). Using the baffled-piston far-field relation p(r) = ρc·u₀·k·a²/(2r):

| Model | 4 kPa | 8 kPa |
|---|---|---|
| A. plane wave at the 5 cm face | 11 mW | 42 mW |
| **B. far-field piston, measured at 7 cm** | **29 mW** | **116 mW** |
| **B. far-field piston, measured at 10 cm** | **59 mW** | **236 mW** |
| C. reverberant 4 L beaker, Q = 50 | 59 mW | 237 mW |
| C. reverberant 4 L beaker, Q = 200 | 15 mW | 59 mW |

Three independent models converge on **tens to a couple of hundred mW acoustic**. With the **measured** 6.4 % electroacoustic efficiency of a real 30 kHz Langevin radiating into water (not the 20–50 % typical of MHz transducers): **0.3–4 W electrical**, ≤5 W with margin. Scaling the same measured device linearly in voltage gives **64 Vpp for 4 kPa and 129 Vpp for 8 kPa** — which brackets the reported "135–275 V" and suggests that figure is a transducer voltage at/near anti-resonance, not evidence of high power.

Beaker modal analysis: **~173 modes below 32.2 kHz, 62 Hz spacing**; at Q ≤ 50 the modal bandwidth (645 Hz) overlaps ~10 modes ⇒ genuinely diffuse field. Sustaining power P = ωE/Q:

| Vessel | 4 kPa, Q = 50 | 4 kPa, Q = 200 | 8 kPa, Q = 50 |
|---|---|---|---|
| 4 L beaker | 59 mW ac / 0.85 W el | 15 mW / 0.21 W | 237 mW / 3.4 W |
| **Bathtub 200 L** | **3.0 W ac / 42 W el** | 0.74 W / 10.6 W | 11.8 W / 169 W |

⇒ a bathtub with 10–12 transducers lands at **~1–10 W electrical each** — exactly the duty point of a cheap Langevin, and an independent rationale for the multi-transducer bathtub architecture.

### B.9 Three costed builds ⭐
| Build | Contents | Cost |
|---|---|---|
| **Budget** | FY6900 (€70) + LM3886/TDA7293 class-AB kit (€20) + ±25–35 V linear PSU (€25) + hand-wound 1:8 ferrite toroid (€8) + series L (€10) + passives/enclosure (€17) — no output LC, so no corner or ringing problem | **~€150** |
| ⭐ **Recommended** | **Siglent SDG1032X (€300) + PiezoDrive PDm200 (€305)** + cabling (€35): natively covers 135–275 V at 33 kHz with current to spare, correct hardware 1.5 s gating, no transformer, no HV bench hazard, fully citable in a methods section | **~€640** |
| **Lab-grade** | SDG1032X or DG1022Z + used **Krohn-Hite 7500 ($1 495)** + HV probe + dummy load | **~€1 600** |
| *(reference-identical)* | SDG-class generator + **PiezoDrive PDUS210-400 ($4 141)** + APC Langevin — i.e. literally the Tijore-lab rig | ~€4 500 |

Whole-system BOM including transducer, VNA, potting and hydrophone: **minimum ~$312 / mid ~$2 631 / lab-grade ~$15 400** (the last dominated by an Onda HCT + MCT-2000, ⚠️ quote-only, est. $8 k).

### B.10 Recommended path ⭐
1. Buy **2× BJC-3360T-48HS ($8.50 ea)** + **10× 25×10×4 PZT4 rings ($22)** + **10× 16×8×4 PZT4 ($20)** — ~$59 of goods, PayPal, DHL, ~10 days. Path A (finished 33 kHz unit) is the working instrument; Path B (build the stack from the papers' exact rings) is the fidelity build.
2. **Measure |Z| vs f on a NanoVNA before anything else** — that one measurement decides between "11 Vpp into 15 Ω" and "275 V into 1 kΩ", i.e. between the €150 and the €1 600 tier.
3. Consider **skipping the cone** (48 mm face ≈ the papers' ~5 cm; a cone detunes by kHz).
4. Drive: SDG1032X + PDm200 (€640) if you want it citable; FY6900 + LM3886 + 6.4 mH series L (€150) if you want it cheap.
5. **Plan for thermal drift** — the biggest threat to a constant 30-minute dose.
6. **Degas and verify with a DO meter** (target < ~4 mg/L O₂ vs ~9 mg/L saturation; €30–80 aquarium meter).
7. Human bathtub exposure: **battery-powered SELV or not at all** (see section C).

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


## Section D — calibration, instrumentation, degassing, thermal, software (applies to all three architectures)

### D.1 What the source lab's instrument actually is ✅
**Onda MCT-2000 is a benchtop *cavitation meter*** (digitiser + spectrum analyser, 232×113×215 mm), not a hydrophone. It reads out **F₀, direct-field pressure P₀ (kPa), stable cavitation P_S and transient cavitation P_T**, with the probe being a separate **HCT-0320** cleaning-tank hydrophone (Teflon shaft 270 × 3 mm, **useful range 20 kHz–1.2 MHz**, max 70 °C, pH 4–12, 1.5 m cable with **NPL-traceable calibration stored in the LEMO connector**). The cheaper **MCT-1200** reads F₀ + P_TOT only, and its datasheet states **"Total Pressure, P_TOT (kPa or unitless) * — *kPa units require self-calibration to absolute reference"**, with a **1–60 s time-averaging interval** ([HCT/MCT-1200 datasheet](https://ondasonics.com/wp-content/uploads/2023/10/Onda_HCT-0320_MCT-1200_DataSheet.pdf), [HCT/MCT-2000 datasheet](https://www.ondacorp.com/wp-content/uploads/2020/07/Onda_HCT-0320_MCT-2000_DataSheet.pdf), [product page](https://www.ondacorp.com/cleaning-tank-hydrophones/)). ⚠️ **"HCT-0310" does not exist** in Onda documentation — the cleaning-tank line is HCT-**0320**. Both meters are quote-only (⚠️ est. ~$8 k for HCT+MCT-2000).

🔑 Consequences for interpreting "4 kPa": it is a **time-averaged, broadband total pressure** from a cleaning-tank meter, not a calibrated peak-negative pressure — and if the self-calibration step was skipped it is in arbitrary units, which fits the paper's mV-scaled field map. ⚠️ Worth emailing the authors: the MCT outputs kPa, yet Figure S1B is in mV, so either they read the HCT raw on a scope or used a second sensor.

### D.2 Hydrophone selection — the counter-intuitive rule
Conversion: **M[V/Pa] = 10^(M_dB/20) × 10⁶**; 4 kPa = **192.0 dB re 1 µPa**, 8 kPa = **198.1 dB**.

| Hydrophone | Sensitivity | µV/Pa | @4 kPa | @8 kPa | Verdict |
|---|---|---|---|---|---|
| **B&K 8103 / Teledyne RESON TC4013** | −211 dB | 28.2 | **113 mV** | 225 mV | ⭐ reference choice |
| **Aquarian AS-1 / S1n** | −208 dB | 39.8 | **159 mV** | 319 mV | ⭐ best value |
| **Cetacean CR3** | −207 dB | 44.7 | 179 mV | 357 mV | ⭐ factory spot-cal per unit |
| B&K 8104 / 8105 | −205 dB | 56.2 | 225 mV | 450 mV | ✅ |
| RESON TC4033 / TC4034 | −203 / −218 dB | 70.8 / 12.6 | 283 / 50 mV | 566 / 101 mV | ✅ |
| RESON TC4037 | −193 dB | 224 | 896 mV | 1.79 V | ✅ but 36 mm ≈ λ/1.3 — bulky |
| Benthowave BII-7181 | −221 dB | 8.9 | 36 mV | 71 mV | ✅ |
| **RESON TC4038** | −228 dB | 4.0 | 16 mV | 32 mV | ❌ **trap — range starts at 50 kHz** |
| Onda HNR-0500 needle | −258 dB | 0.126 | 0.5 mV | 1.0 mV | ❌ needs LNA, **no valid calibration at 33 kHz** |
| Aquarian H2a | −180 dB LF, ≈−220 dB at 100 kHz (a 40 dB slide), ±4 dB only 20 Hz–4 kHz | — | 4.0 V | 8.0 V | ❌ clips; value at 32 kHz mid-slope and unspecified |
| Aquarian H2d (XLR) | −165 dB | 5623 | **22.5 V** | 45 V | ❌ gross clip |
| B&K 8106, RESON TC4014/4032/4035, Cetacean C57/icListen HF | preamplified | — | — | — | ❌ **all clip at 1.0–2.5 kPa** |

> ⭐ **Rule 1: buy passive, not "smart."** The entire preamplified/digital hydrophone market is built for ocean ambient noise and saturates 1–2 orders of magnitude below 192–198 dB re 1 µPa.
> ⭐ **Rule 2: a normal oscilloscope is entirely sufficient.** A passive hydrophone straight into a 1 MΩ input gives **113–450 mV**; at 50 mV/div an 8-bit scope resolves ~1 % of signal. **No preamplifier is required or wanted.**
> ⭐ **Rule 3: medical needle/membrane/fibre-optic hydrophones genuinely do not work at 32 kHz** — not electrically but *acoustically*: with λ = 46.6 mm ≫ element and shaft, diffraction and edge waves from the shaft dominate ([PMC10079648](https://pmc.ncbi.nlm.nih.gov/articles/PMC10079648/)). Onda's medical-line calibrations start at 1 MHz; Precision Acoustics' ISO 17025 accreditation is **1–40 MHz only** and they refer low-frequency customers to NPL.

**Published prices** (almost everything else is quote-only): Aquarian **AS-1 $413** (10+: $330), **S1n $379**, H2d $229, PA6 preamp $75, IEPE1 $80; Precision Acoustics needle systems "from £2 943 + VAT" (2021 list). ⚠️ Aquarian units are **not individually calibrated** — the vendor explicitly warns that any given AS-1, especially with long cable, can deviate from published specs.

**Inferring the paper's sensor from "<20 mV … ~180 mV"**: if 180 mV ↔ 4 kPa ⇒ **45.0 µV/Pa = −206.9 dB**, i.e. Cetacean CR3 (−207) / Aquarian AS-1 (−208) / B&K 8104–8105 (−205) class; if 180 mV ↔ 8 kPa ⇒ 22.5 µV/Pa = −213 dB ≈ B&K 8103 / TC4013. **Either way the implied sensitivity is 22–45 µV/Pa — the standard passive underwater-hydrophone class — and the "4 Pa" reading would require 45 V/Pa, which does not exist.** The "<20 mV" floor then corresponds to ~440 Pa. 🔑 **This is independent confirmation that the working pressure is kPa, not Pa.**

### D.3 DIY hydrophones
Your application is the easy case: a bare PZT-5H tube/disc potted in polyurethane lands at **−190 to −215 dB (20–300 µV/Pa)** ⇒ **80 mV–1.2 V at 4 kPa**, and self-noise (the usual DIY killer) is irrelevant 60–80 dB above where it matters. Keep the element small so its radial resonance stays far above 33 kHz.

| Resource | What it gives |
|---|---|
| *Low-Cost Hydrophone for Passive Acoustic Monitoring of Dolphin Vocalizations*, Remote Sensing 15(7):1946 (2023), OA | full build + calibration — [10.3390/rs15071946](https://doi.org/10.3390/rs15071946) |
| *Construction, calibration and field test of a home-made low-cost hydrophone system* | the canonical DIY paper — [10.1121/1.3573502](https://doi.org/10.1121/1.3573502), [10.1121/1.3508712](https://doi.org/10.1121/1.3508712) |
| *Validación de hidrófonos de bajo costo* (2025, OA) | independent validation vs references — [ojs.inidep.edu.ar](https://ojs.inidep.edu.ar/index.php/mafis/article/download/436/522) |
| *Development of a PVDF needle-type hydrophone*, IEEE INDUSCON 2018 | [10.1109/induscon.2018.8627232](https://doi.org/10.1109/induscon.2018.8627232) |
| *Broadband Reference PVDF Membrane Hydrophone*, IEEE IUS 2006 | [10.1109/ultsym.2006.147](https://doi.org/10.1109/ultsym.2006.147) |
| *Calibration and performance of a high-temperature cavitometer*, Sens. Actuators A 2016, OA | **calibrating a cavitation sensor in the tens-of-kHz band — directly on point** ([PDF](https://www.sciencedirect.com/science/article/pii/S0924424716300243/pdf)) |
| [Supermagnum/piezoelectric](https://github.com/Supermagnum/piezoelectric), /hydrophone, /piezo-balanced | piezo buffers/preamps, PZT-5H tube recommendations, op-amp choices, LSK389B balanced PCB, build photos |
| [mo-seph/PiezoPreamp](https://github.com/mo-seph/PiezoPreamp), htarold/piezo-agc-preamp | preamp schematics, AGC |
| ⭐ [SamC873/FUSF_Hydrophone_Scanner](https://github.com/SamC873/FUSF_Hydrophone_Scanner) | **Focused Ultrasound Foundation's open-source 3-axis tank scanner** — the field-mapping rig this project needs |

**Uncertainty**: uncalibrated DIY ±3–6 dB (factor 1.4–2 in pressure); comparison-calibrated in your own tank ±1–2 dB; national lab ±0.5 dB. ⚠️ **Your spec window (4→8 kPa) is only 6 dB wide, so ±3 dB DIY uncertainty cannot distinguish 4 from 8 kPa. Calibration is not optional.**

### D.4 Where you can actually get a 32 kHz calibration
Queried against the **BIPM KCDB** (recognised CMCs), not marketing copy — **only two national labs in the world hold a CMC at 32.2 kHz**:

| Lab | Range | Method | Uncertainty (k=2) |
|---|---|---|---|
| **NPL (UK)** | **2 kHz – 500 kHz** | three-transducer spherical-wave reciprocity | **0.5 dB** |
| **NPL (UK)** | 2 kHz – 1 MHz | comparison with reference hydrophone, IEC 60565 | 0.7 dB |
| VNIIFTRI (RU) | 3.15 kHz – 200 kHz | IEC 60565 reciprocity | 0.6 dB |

**PTB, NIST, KRISS, NIM, NRC, INRIM, CENAM, INMETRO, NPLI, UME all start at ≥0.5–1 MHz** (medical-ultrasound oriented). It is specifically NPL's *underwater acoustics* division that covers this band. Commercially, **Onda calibrates 0.03 kHz – 60 MHz per IEC 62127** — the only commercial lab verified to span 32.2 kHz. ⚠️ No calibration price could be obtained from anyone. ⭐ **Path: buy one calibrated passive reference, then comparison-calibrate DIY units in your own tank by substitution.**

### D.5 Oscilloscopes and DAQ
| Device | BW | Max SR | Bits | Memory | Streaming | Price | Verdict |
|---|---|---|---|---|---|---|---|
| ⭐ **Siglent SDS804X HD** | 70 MHz | 2 GSa/s | **12** | 100 Mpts | ✗ | **€409** | best bench buy; HW 2 Mpt FFT, 70 µV rms front end |
| Rigol DHO804 | 70 MHz | 1.25 GSa/s | 12 | 25 Mpts | ✗ | €417 | equivalent class |
| Rigol DS1054Z | 50 MHz | 1 GSa/s | 8 | 24 Mpts | ✗ | €427 | 8-bit — needs external filtering for cavitation work |
| Siglent SDS1104X-E | 100 MHz | 1 GSa/s | 8 | 14 Mpts | ✗ | €511 | |
| Hantek DSO2D10 | 100 MHz | 1 GSa/s | 8 | 8 Mpts | ✗ | ~$180–230 | fine for pressure reading only |
| ⭐ **PicoScope 2206B** | 50 MHz | 500 MS/s | 8 (→12 enh.) | 32 MS | **9.6 MS/s gap-free (31 via SDK)** | **€463** | only true broadband streaming at this price |
| ⭐ **Digilent Analog Discovery 3** | 9 MHz (30+ with BNC) | 125 MS/s | **14** | 32 kpts/ch | record ~10 MS/s RAM | **$379 / €469** | scriptable (Python SDK) — ideal for gated capture; **the Tijore lab uses the older AD2 (Digilent 410-321)** |
| NI USB-6212 | — | 400 kS/s | 16 | — | DMA to disk | $300–600 used | covers f/2…6f, no broadband |
| ❌ NI USB-6009 | — | 48 kS/s | 14 | — | — | $250–400 | **Nyquist 24 kHz — 32.2 kHz aliases to 15.8 kHz. Do not use** |
| ❌ ADS1256 / MCP3008 | — | 30 kSPS / ~50 kSPS | 24 / 10 | — | — | $40 / $4 | below or barely at the fundamental |
| ⭐ **192 kHz audio interface** (Scarlett 2i2, MOTU M2) | — | 192 kHz | 24 (>100 dB DR) | — | unlimited | €180–220 | best dynamic range per euro; captures 16.1 / 32.2 / 48.3 / 64.4 / 80.5 kHz. ⚠️ AA filter often rolls off 40–60 kHz, AC-coupled, uncalibrated absolute level |

**Adequacy**: (a) reading 4 kPa at 33 kHz — anything except the three ❌ rows; (b) subharmonic 16.1 kHz + ultraharmonics 48.3/80.5 kHz — needs ≥250 kS/s and **≥12 bit or external notch/HPF** (8 bits ≈ 48 dB SFDR, and the subharmonic sits 40–60 dB down); (c) broadband cavitation noise to ~1 MHz — PicoScope streaming, AD3 record mode, or snapshot mode on any bench scope. 🔧 **You don't need 30 min of continuous broadband capture** — take a 200 ms snapshot at 5 MS/s every 10 s phase-locked to the ON window (180 snapshots ≈ 360 MB); both PicoSDK and WaveForms script this in Python. ⭐ Best pairing: **SDS804X HD (€409) for field mapping + AD3 ($379) or PicoScope 2206B (€463) for scripted passive cavitation detection ≈ €800–880.**

### D.6 Cavitation detection
**Is 4–8 kPa safe?** Yes, with margin — *if* you degas:

| Source | Condition | Threshold | Margin at 4–8 kPa |
|---|---|---|---|
| Hong & Son, *Ultrason. Sonochem.* 2022 ([10.1016/j.ultsonch.2022.105932](https://doi.org/10.1016/j.ultsonch.2022.105932)) | Blake threshold, 500 nm nucleus, 1 atm | **196 kPa** | **25–49×** |
| same, literature survey | air-saturated water, 0.02–4.8 MHz | 20–620 kPa (lowest at lowest f) | ⚠️ **only 2.5–5×** at the bottom end |
| same | degassed, 2.5 nm nuclei | 25.9–27.4 MPa | 3 000–6 000× |
| Viciconte et al., *Phys. Fluids* 37, 012104 (2025) ⚠️ paywalled | **25 kHz, air-saturated tap water** | **≈253 kPa** | 32–63× |
| same | **25 kHz, degassed** | **≈659 kPa** | 82–165× |
| Galloway, *JASA* 26 (1954) | ~27 kHz | 1 atm (air-sat) → hundreds of atm (degassed) | — |
| Blake, large-nucleus limit | — | floor ≈ 100 kPa | 12.5–25× |

🔑 **The weak link is not inertial cavitation but *stable* cavitation of pre-existing bubbles**, which happens far below the Blake threshold: at 32.2 kHz the **Minnaert resonant bubble is ~100 µm radius** (R·f ≈ 3.26 m·Hz) — exactly what nucleates on a plastic mesh, a dish wall or a heater element. **Degassing, pre-wetting every surface and avoiding gas entrainment matter more than the pressure margin.** (MI, formally MHz-only, would read 0.022.)

**Method literature**: Neppiras *JASA* 1968 ([10.1121/1.1970448](https://doi.org/10.1121/1.1970448)) and *Phys. Rep.* 61 (1980) for the subharmonic; Morton/ter Haar/Stratford/Hill *UMB* 1983 ([10.1016/0301-5629(83)90008-x](https://doi.org/10.1016/0301-5629%2883%2990008-x)) linking f/2 to biological damage; **Hodnett & Zeqiri 1997** ([10.1016/S1350-4177(97)00042-4](https://doi.org/10.1016/S1350-4177%2897%2900042-4)) for the NPL broadband-integrated-noise metric; **Frohly et al. *JASA* 108 (2000)** ([10.1121/1.1312360](https://doi.org/10.1121/1.1312360)) — a direct template for a 20 kHz-class PCD; Zeqiri et al. *IEEE TUFFC* 50 (2003) parts [I](https://doi.org/10.1109/TUFFC.2003.1244751)/[II](https://doi.org/10.1109/TUFFC.2003.1244752); Johansen/Song/Prentice 2018 ([10.1016/j.ultsonch.2018.01.007](https://doi.org/10.1016/j.ultsonch.2018.01.007)) on *building* a PCD; Yasui 2023 ([10.1016/j.ultsonch.2022.106276](https://doi.org/10.1016/j.ultsonch.2022.106276)) on what broadband noise physically is. ⭐ **BS EN IEC 63001 — "Measurement of cavitation noise in ultrasonic baths and ultrasonic reactors"** is the closest thing to a standard method for exactly this problem (⚠️ edition year unverified, IEC/ANSI webstores 403) — **buy it** (~€200).

**Recipe** 🔧: second receiver off-axis, ≥1 λ (~50 mm) from the transducer face → **high-pass 40–100 kHz or twin-T notch at 32.2 kHz BEFORE the amplifier** (the fundamental is 40–70 dB above what you are looking for and will saturate any front end) → ≥20 ms records (≤50 Hz bins) at ≥2.5 MS/s, Hann window, 10–50 averages → metrics: subharmonic 16.1 kHz, ultraharmonics 48.3/80.5/112.7 kHz (the classic precursor to inertial collapse), and broadband "inertial cavitation dose" (RMS with harmonic/ultraharmonic bins excised, integrated 100 kHz–1 MHz and over time). **Record a transducer-off floor and a sub-threshold reference first** — the claim is "no elevation above baseline at 4–8 kPa", which requires a baseline.

**Hardware**: ⭐ a **bare 27 mm piezo disc potted in epoxy/silicone + coax (€1–5)** is the best cheap PCD (uncalibrated but the question is relative); DIY front end = 2-pole Sallen-Key HPF at 80–100 kHz or twin-T notch + OPA1656/OPA827, gain 40–60 dB (€15–40); Aquarian AS-1 doubles as primary sensor; Precision Acoustics needles are ❌ for measuring 32 kHz but ✅ as 0.5–15 MHz PCD receivers (£1 225–1 355, 2021 list); Sonic Concepts Y-102/Y-107 is the commercial gold standard (quote).

**Cheap qualitative negative controls** (all should be **negative** at 4–8 kPa): **aluminium-foil erosion** (Saikova et al., *Molecules* 2026, [10.3390/molecules31081291](https://doi.org/10.3390/molecules31081291)) ~€1; **sonochemiluminescence with luminol** (McMurray & Wilson, *J. Phys. Chem. A* 103:3955 (1999), [10.1021/jp984503r](https://doi.org/10.1021/jp984503r); mapping practice in Garcia-Vargas et al. 2025, [10.1016/j.ultsonch.2025.107395](https://doi.org/10.1016/j.ultsonch.2025.107395)) ~€20 + a DSLR long exposure; **KI (Weissler) dosimetry** ~€20. ⭐ Run the **positive** control in a €40 cleaner to prove the test works — this is where a cheap bath earns its keep.

### D.7 Degassing
Henry's law sets the budget: to reach ≤20 % saturation you only need **≤0.2 atm ≈ 20 kPa absolute**, and water-vapour pressure is the floor (3.17 kPa at 25 °C, 5.63 kPa at 35 °C). ⇒ **a cheap 1/4 HP single-stage pump is entirely sufficient; a two-stage 0.1 Pa pump buys nothing.** Spend the difference on a bigger chamber and a stirrer — agitation and surface renewal set the rate.

| Option | Achievable DO | Price | Notes |
|---|---|---|---|
| ⭐ **VEVOR 3-gal chamber + 3.5 CFM 1/4 HP single-stage** | 2–3 mg/L in one cycle, <2 mg/L in two | **$136.30** ([Home Depot](https://www.homedepot.com/p/VEVOR-3-Gallon-Vacuum-Chamber-and-3-5-CFM-Pump-Kit-Stainless-Steel-Chamber-Single-Stage-Vacuum-Pump-Degassing-Chamber-Kit-ZKBZKTTZDJ14OVZFDV1/333961504)) | claimed 5 Pa, realistically 20–50 Pa — irrelevant |
| Water aspirator / venturi on a tap | ~2–3 kPa | €15–30 | ✅ adequate given the vapour-pressure floor |
| ⭐ **Boil 5 min + cool sealed** | **<2 mg/L** (Precision Acoustics guidance) | **~€0** | cheapest reliable route; **must cool sealed with minimal headspace** or it re-gasses; improves sterility |
| Helium sparging | displaces N₂/O₂, does not reduce total dissolved gas | €200–400 | He raises the cavitation threshold — good; follow with a brief vacuum step |
| Membrane contactor (Liqui-Cel MiniModule, IDEX Degasi) | 2–4 ppm | ~$300–4 000 ⚠️ | best for continuous recirculation (and the only option at bathtub scale) |
| Bath "degas" mode | partial | €40–200 | ⚠️ **it works by cavitating** — fine as pre-treatment in a *separate* vessel, **never** in the acoustic tank (quantified in Asakura & Yasuda 2022, [10.1016/j.ultsonch.2021.105890](https://doi.org/10.1016/j.ultsonch.2021.105890)) |

**Procedure**: fill → pull to ~3–5 kPa absolute (gauge ≈ −29 inHg) → it effervesces then simmers → **hold 20–30 min with a stirrer bar** → break vacuum slowly → **siphon, don't pour**.

**DO meters**: ⭐ Milwaukee MW600 galvanic ±1.5 % ~$250; ⭐ DFRobot Gravity SEN0237-A analog/Arduino $169 (⚠️ accuracy not specified, ~±0.5–1 mg/L after 2-point cal); Hanna HI9147 ±1 % $690; Apera DO850 optical ~$699; Atlas Scientific EZO DO kit $319–337; YSI ProODO ~$1 500–2 200 ⚠️.

**Targets**: air-saturated freshwater is 9.09 mg/L at 20 °C, 8.26 at 25 °C, **7.07 at 35 °C**. Vendor practice: Precision Acoustics ≤2.5 ppm, FUS Instruments <2 mg/L, Onda AQUAS-10 ≤4 ppm; ⚠️ **IEC/TR 62781** ("conditioning of water for ultrasonic measurements") is the governing document but its full text could not be obtained (IEC/ANSI/GlobalSpec all 403) and it is guidance, not a numeric limit. ⭐ **Recommended target DO ≤ 2 mg/L (≈24 % sat at 25 °C); stretch ≤1 mg/L. Measure at the start AND end of every run** — DO rises during a run from surface re-absorption, and the heater accelerates it.

### D.8 Heating and thermostat
🔑 **Architectural decision first: do not put a circulator, impeller or bubbler in the acoustic tank** — flow causes sample advection, microstreaming (which confounds the very mechanism under study), surface entrainment that destroys your degassing, and a moving scatterer field. ⭐ **Put the 4 L acoustic tank inside a larger outer bath** held at ~33.5 °C by a sous-vide or lab circulator: zero moving water in the acoustic path, and 4 L has ~16.7 kJ/K of thermal mass so 30 min of drift is small.

| Device | Accuracy | Price | Use |
|---|---|---|---|
| ⭐ **Inkbird ITC-308 + any dumb heater** | ±1 °C spec, **±0.3–0.5 °C after offset calibration** | $36–56 | best value; small NTC probe = low scatter |
| ⭐ **Inkbird ISV-100W sous-vide** | **±0.1 °C over 8 h** (independent test) | $126 | outer bath only |
| Eheim Jäger TruTemp 100 W | ±0.5 °C, 18–34 °C | $32.95 | cheap; glass body is a strong scatterer — keep off-axis, switch off during acquisition |
| Julabo CORIO / LAUDA Alpha A | ±0.03–0.05 °C | €822–978 | gold standard, outer bath |

**Logging**: ⭐ **PT100/PT1000 + MAX31865** (Class A ±0.15 °C, ±0.05 °C after 1-point offset; 3 × 30 mm probe; $14.95 + $14.95) — smallest metal probe; DS18B20 (±0.5 °C, 6 × 50 mm SS, $9.95) has ka ≈ 0.4 and its hollow air-filled tube behaves closer to pressure-release, which is worse; type-K is acoustically smallest but ±2 °C is useless in a 3 °C window; fibre-optic/thin-wire thermistors (€300+) are the acoustically invisible "proper" answer. **Placement: ≥2 cm laterally from the sample and entirely out of the transducer→sample column**; verify by mapping with the probe in and out (<5 % change at the sample plane). Better: log the **outer** bath continuously and the acoustic tank only during the 1.5 s OFF windows.

### D.9 Software and open-format practice 🔧
- **Firmware**: MicroPython/CircuitPython or Arduino on an RP2040 for the 1.5 s gate + session timer + interlocks; expose a serial command set; log every gate edge with a timestamp.
- **Field mapping**: [FUSF_Hydrophone_Scanner](https://github.com/SamC873/FUSF_Hydrophone_Scanner), or a converted 3D printer (Ender-class) running Marlin/GRBL with the hydrophone on the extruder mount; drive it with `pyserial` G-code and trigger a Digilent AD3 or PicoScope capture at each point. Save raw waveforms (not just peak values) as HDF5/NPZ + a CSV index; publish the scan grid, tank geometry, fill level and water temperature with every map.
- **Analysis**: Python (numpy/scipy) — per-point peak, RMS, FFT magnitude at f₀, harmonic ratios, subharmonic/ultraharmonic/broadband cavitation metrics; store calibration constants (V/Pa, cable capacitance, date, reference used) in the dataset metadata.
- **Data publication**: raw + processed data, scan scripts and firmware in one repo under an open licence; report the pressure metric explicitly (peak vs RMS vs time-averaged-total) — the ambiguity in the source literature is precisely what this project should not repeat.

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

---

# PART 4 — SYNTHESIS: WHAT TO BUILD, AND WHAT IS STILL UNKNOWN

## 4.1 The minimum honest replication (bench scale, no humans) 🔧
| Function | Item | Cost |
|---|---|---|
| Source | 5–10 × 33 ± 0.5 kHz 60 W Langevin (OKS-QXHUNQ33K $7.50 / Granbo / BJC-3360T-48HS $8.50), binned on a NanoVNA | **$40–90** |
| *(fidelity variant)* | PZT4 rings 25×10×4 + 16×8×4 from Beijing Ultrasonic ($42) + machined aluminium cone + bolt/back mass | +$42 + machining |
| Tank | 4 L glass beaker + 13 cm × 15.2 cm plastic cylinder + plastic mesh (as in the paper), or a Yunyisonic YL0205-33 shell ($199) | €20–199 |
| Drive | Siglent SDG1032X (€300) + PiezoDrive PDm200 (€330) — or FY6900 + LM3886 + 6.4 mH series L (€150) | €150–640 |
| Gate | MCU (RP2040) driving the amplifier enable, 1.5 s / 1.5 s, 600 cycles, logged | €10 |
| Tuning | NanoVNA-H4 | €50–90 |
| Pressure | Aquarian AS-1 ($413) → **calibrated by Onda or NPL at 32.2 kHz** | $413 + cal |
| Acquisition | Siglent SDS804X HD (€409) for mapping + Digilent AD3 ($379) or PicoScope 2206B (€463) for scripted cavitation detection | €800–880 |
| Field mapping | FUSF open-source scanner or a converted 3D printer + steppers | €100–200 |
| Cavitation PCD | potted 27 mm piezo + 80 kHz HPF + OPA1656 | €25 |
| Degassing | boil-and-seal (€0) or VEVOR 1.5–3 gal + 3.5 CFM pump ($130) + stirrer | €0–130 |
| DO meter | DFRobot Gravity SEN0237-A ($169) or Milwaukee MW600 ($250) | $169–250 |
| Thermal | outer bath + Inkbird ISV-100W ($126) + PT1000/MAX31865 ($30) | $156 |
| Negative/positive controls | Al foil + luminol + a €40 cleaner as positive control | €60 |
| Standard | BS EN IEC 63001 (cavitation noise in ultrasonic baths) | ~€200 |
| **Total** | | **≈ €1 900–2 600** |

Note the shape of this BOM: **the acoustic source is ~2 % of it.** Everything else is metrology — which is the correct proportion for a project whose entire scientific value rests on knowing the delivered pressure.

## 4.2 Priority order of experiments 🔧
1. **Impedance sweep** of each transducer on the NanoVNA (before buying any amplifier).
2. **Drive at a known voltage, measure pressure with a calibrated hydrophone at 7–10 cm** → settle **Pa vs kPa** definitively. Cross-check against the Tijore 1 kPa → 11 nm interferometer table if you can borrow a vibrometer.
3. **Map the field** over the sample plane on a ≤1 cm grid; publish mean/SD/min/max. Their own map spans ~9×.
4. **Cavitation negative controls** (foil, luminol, PCD spectra) at the working pressure, and the positive control in a cheap cleaner.
5. Only then do biology: senescent-cell growth at 33 kHz vs 39 kHz, power ladder 2.2/3.8/4/5.2/6.4/7.2/8/10 (k)Pa, duty ladder 1.25/1.5/1.75 s, exactly as in Figure S1C–F.
6. Log water temperature and DO at start and end of every run; record the drive waveform (harmonics matter, per the patent).

## 4.3 Open questions that no accessible source answers
| # | Question | Why it matters | Best route |
|---|---|---|---|
| 1 | **Pa or kPa?** | 10⁶ in intensity | direct measurement; or email the authors (Kureel is now at UT Health San Antonio / Barshop; Margadant and Kenney at Mechanobiologics) |
| 2 | Was the MCT meter ever **self-calibrated to an absolute reference**, or were the numbers "unitless"? | decides whether "4 kPa" is a pressure at all | ask the authors; the meter's own datasheet flags the requirement |
| 3 | Which **transducer/generator/amplifier** did the UTMB rig actually use? | exact replication | never published; the Singapore-lineage rig (ring PZT4 + cone) and the IISc rig (APC + PiezoDrive PDU 210) are the two documented designs |
| 4 | Peak, RMS or time-averaged total pressure? | factor ~1.4–3 | the MCT reads a **time-averaged total** over 1–60 s, which is closest to RMS-including-harmonics |
| 5 | What are the "**10–12 transducers on articulated arms**" of the human bath? | architecture C | not in any accessible source; the immersion patent teaches 1–1000 transducers on bottom/side walls and on a robotic arm/gantry |
| 6 | Why is **NCT06562374 suspended**? | safety/regulatory signal | ClinicalTrials.gov gives no reason; check UTMB IRB records or ask |
| 7 | Does the effect need **32.248 kHz specifically**, or any 30–40 kHz? | whole design | the papers test only 33 vs 39 vs 120 kHz; the patent claims 30–100 kHz and even suggests 10–20 kHz square-wave harmonics would do |
| 8 | Is the 1.5 s duty optimum real? | the sharpest unexplained parameter | their own data show ±0.25 s changes the result; it is the cheapest thing to re-test |

## 4.4 Files kept in the scratchpad (`lfu/`)
`PMC12151899.xml/.txt` (Aging Cell), `acel/ACEL-24-e70008-s001.docx` + `.txt` + `media/word/media/image5.png` (Figure S1A schematic, rendered on white as `w_image5.png`) and `image6.png` (field map), `PMC11883105.xml/.txt` + `tij/BTM2-10-e10737-s002.pdf` + `page7.png`/`page10.png` (tank photo, block diagram), `PMC8459596`, `PMC12445081`, `PMC13315667`, `PMC13087965` (IISc rigs), `ajp_pmc.xml/.txt` (AJP-Endo author manuscript), `brx_v1..v4.pdf/.txt` (all four bioRxiv versions), `pat_sen.html/.txt` (US20240001155A1), `app20220203138.pdf` (scanned USPTO image), `NCT06562374.json`, `hct.pdf` (Onda HCT/MCT datasheet), plus the helper scripts `x2t.py` and `kw.py`.
