# IP analysis — LFU "senescence reversal" (Sheetz / Mechanobiologics) vs. an open-hardware DIY replication in Italy

Research memo, compiled 2026-09-16. **Not legal advice.** This is a technical/documentary reconstruction of the patent landscape from public sources, written by an AI assistant, not by a qualified attorney (*consulente in proprietà industriale* / patent attorney). Every operational decision — especially anything involving money, kits, third parties or human subjects — needs review by an Italian/EU IP counsel and, for anything touching human use, by a medical-device regulatory advisor.

Target project parameters assumed: ~32.2–33 kHz, 4–8 kPa, 1.5 s on / 1.5 s off, 30 min, immersion in degassed warm water; open-hardware, non-commercial, documented publicly on GitHub, based in Italy.

---

## 0. Executive summary (the short version)

1. **The only *granted* patent in the whole landscape is US 12,714,885 B2 (Mechanobiologics, Inc., issued 25 Aug 2026)**, and every one of its three independent claims (1, 16, 38) is limited to **tumor cells** and to triggering a **mechanically-induced apoptotic process in tumor cells** — not to senescence reversal. Verified from the granted patent PDF (facsimile pages read directly).
2. **It is a US patent only.** The immersion-mechanotherapy family (WO2020223359 / WO2020223242) **never entered the European phase** — the EPO recorded "PCT application non-entry in European phase" for both (2022). There is therefore **no European patent, and nothing enforceable in Italy, from that family**. Confirmed via INPADOC legal events.
3. The **senescence** claims are all still **applications, none granted anywhere**: US 18/217,362 (US 2024/0001155 A1) received a **non-final rejection mailed 2026-02-25**; EP 4 561 696 A1 is pending at the EPO with examination requested (IT among the designated states); a parallel University of Texas family (US 2024/0399175 A1, EP 4 447 814, JP, AU, WO 2023/114011) got a **final rejection in the US (2025-12-03)** and is still pending.
4. **In Europe the senescence claims as filed are methods of therapy → excluded by EPC Art. 53(c)** (and Italian CPI art. 45(4)). They must be rewritten (device claims, in-vitro claims, or arguably-cosmetic/athletic-performance claims) to survive. Scope in Italy, if anything ever grants, will be materially narrower than the US filing.
5. **For a private, non-commercial, experimental DIY build in Italy today, the patent-infringement risk is essentially nil**: (i) nothing is granted in Italy; (ii) even if something granted later, art. 68(1)(a) CPI (private, non-commercial acts) and 68(1)(a-bis) (experimental acts relating to the subject-matter of the patented invention) plus UPCA art. 27(a)/(b) cover exactly this use case; (iii) patents are territorial — a US patent has no effect in Italy.
6. **The real risks are elsewhere**: selling kits or assembled devices (even at cost), offering "treatments" to other people, US-facing instructions that could be framed as inducement under 35 U.S.C. § 271(b), medical-device regulation (EU MDR), and ordinary safety/liability. Recommendations in §8.

---

## 1. Patent inventory

| # | Publication / patent | Title | Applicant / assignee | Jurisdiction | Key dates | Status (as of Sep 2026) | Family |
|---|---|---|---|---|---|---|---|
| 1 | **US 12,714,885 B2** (appl. 17/515,025; pre-grant pub. US 2022/0047894 A1) | Systems and Methods for Immersion Mechanotherapy | Mechanobiologics, Inc. (Santa Fe, NM); inv. Kenney, Sheetz, Margadant | **US only** | filed 2021-10-29; CIP of PCT/US2020/030488 (2020-04-29) and PCT/US2020/030288 (2020-04-28); prov. 62/840,850 (2019-04-30) and 62/841,520 (2019-05-01); pub. 2022-02-17; **granted 2026-08-25** | **GRANTED**, 38 claims, PTA +635 days | A |
| 2 | WO 2020/223359 A1 (PCT/US2020/030488) | Systems and methods for immersion mechanotherapy | Mechanobiologics LLC | PCT | filed 2020-04-29, pub. 2020-11-05 | **Ceased** — "PCT application non-entry in European phase" (EP 20798044), non-entry DE | A |
| 3 | WO 2020/223242 A1 (PCT/US2020/030288) → US 2022/0203138 A1 (17/607,819) | Systems and Methods for Cancer Treatment | Mechanobiologics LLC; inv. Tijore, Margadant, Yao, Sheetz | PCT / US | filed 2020-04-28 | PCT ceased, **no EP national phase** (EP 20798654); US **abandoned 2025-02-03** after final rejection | A |
| 4 | **US 2024/0001155 A1** (appl. **18/217,362**) | Reversal of cellular senescence by treatment with low frequency ultrasound | Mechanobiologics Inc.; inv. Sheetz, Kureel, Margadant | US | prov. 63/357,618 (2022-06-30); filed 2023-06-30; pub. 2024-01-04 | **Pending**; docketed 2026-01-20; **non-final action mailed 2026-02-25**. No B1/B2 grant found. | B |
| 5 | WO 2024/030212 A1 (PCT/US2023/026815) | idem | Mechanobiologics Inc. | PCT | filed 2023-06-30, pub. 2024-02-08 | International phase closed; EP regional phase entered 2025-02-28 | B |
| 6 | **EP 4 561 696 A1** (appl. **EP 23850582.0**) | idem | Mechanobiologics Inc. | EP (incl. **IT**) | EP entry 2025-02-28; pub. 2025-06-04; **examination requested 2025-02-06** | **Pending**, no grant, no Art. 94(3)/71(3) visible in INPADOC yet | B |
| 7 | US 2024/0399175 A1 (appl. 18/719,116) | Reversal of senescence by ultrasound irradiation | **Board of Regents, University of Texas System**; inv. Sheetz, Kureel, Rasmussen, Maroto | US | prov. 63/290,969 (2021-12-17); filed 2022-12-01 (PCT/US2022/051482); pub. 2024-12-05 | **Pending**; non-final 2025-05-07, **final rejection 2025-12-03**, re-docketed 2026-05-04 (RCE/appeal presumed) | C |
| 8 | WO 2023/114011 A1 / **EP 4 447 814 A1 / A4** (EP 22908221.9) / JP 2024-546976 / AU 2022415191 | idem | Board of Regents, UT System | PCT / **EP (incl. IT)** / JP / AU | EP exam requested 2024-07-17; A1 pub. 2024-10-23; **supplementary search report (A4) despatched 2026-04-13**, IPC reclassified to A61N 7/00 | **Pending** everywhere | C |
| 9 | US 2021/0244972 A1 / KR 10-2021-0101481 | Device for removing senescent cells comprising ultrasound output unit | **Korea Institute of Science and Technology (KIST)** — third party | US / KR | prio. 2020-02-10 | US **abandoned 2023-11-04** | D (third-party) |

Sources: [US12714885B2 PDF facsimile (USPTO)](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12714885) · [US20220047894A1](https://patents.google.com/patent/US20220047894A1/en) · [WO2020223359A1](https://patents.google.com/patent/WO2020223359A1/en) · [WO2020223242A1](https://patents.google.com/patent/WO2020223242A1/en) · [US20220203138A1](https://patents.google.com/patent/US20220203138A1/en) · [US20240001155A1](https://patents.google.com/patent/US20240001155A1/en) · [WO2024030212A1](https://patents.google.com/patent/WO2024030212A1/en) · [EP4561696A1](https://patents.google.com/patent/EP4561696A1/en) · [US20240399175A1](https://patents.google.com/patent/US20240399175A1/en) · [EP4447814A1](https://patents.google.com/patent/EP4447814A1/en) · [US20210244972A1](https://patents.google.com/patent/US20210244972A1/en)

**"Three others pending" (from the slide) — reconciliation.** Searching Google Patents by assignee "Mechanobiologics" returns exactly 4 documents (items 2, 3, 4 above + US 2022/0047894, the pre-grant publication of the now-granted patent). By inventor Sheetz + ultrasound, and by inventor Kureel/Margadant, the only additions are the UT System family (items 7–8). So the plausible reading of "three others pending" is: **US 18/217,362 + EP 23850582.0 + the UT System family** (which itself counts as US/EP/JP/AU). ⚠️ *Unverified*: whether any **continuation** of 17/515,025 was filed before grant (very common practice). Google Patents does not yet index US 12,714,885 (404 on `/patent/US12714885B2/en`), patents.justia.com returned HTTP 403, and both USPTO Patent Center API and EPO Register returned 401/403 to unauthenticated fetches. **Assume a continuation exists until checked in Patent Center (appl. 17/515,025 → "Continuity Data").**

### Term / expiry estimates (⚠️ estimates, not certified)

- **US 12,714,885**: 20 years from the earliest US/PCT filing whose benefit is claimed under §120/§365(c) = **2020-04-28 → 2040-04-28**, plus **635 days PTA** stated on the face → **≈ 23 Jan 2042**, subject to maintenance fees (3.5/7.5/11.5 yr) and to any terminal disclaimer (none visible on the face page).
- US 18/217,362, if granted: filed 2023-06-30 → **≈ 2043-06-30** + PTA.
- EP 4 561 696, if granted: 20 years from 2023-06-30 → **2043-06-30** (annuities per state).
- EP 4 447 814 (UT), if granted: 20 years from 2022-12-01 → **2042-12-01**.

---

## 2. Claims analysis

### 2.1 US 12,714,885 B2 — the only granted patent

Read directly from the granted facsimile (cols. 21–24). Three independent claims:

**Claim 1 (device).** "A device for treating **tumor cells** in a subject", comprising:
- (a) an **immersion element containing a liquid medium to immerse a body part** of the subject; and
- (b) **one or more ultrasound transducers** configured to generate a **sequence of programmed cycles of waves** to the body part **through the liquid medium**, with a **modulation pattern, intensity and frequency sufficient to apply periodic forces to the tumor cells and non-tumor cells** for a period of time that **triggers a mechanically-induced apoptotic process in the tumor cells without mechanically damaging the tumor cells and the non-tumor cells**,
- wherein the apoptotic process is **triggered by periodic stretching of the tumor cells, rather than by heat or high temperature**, and the modulation/intensity/frequency are configured to cause **stretching and relaxation of the tumor cells sufficient to activate the mechanically-induced apoptotic process**.

**Claim 16 (method).** Same, as a method: providing the immersion element + generating the programmed cycles, with identical "tumor cells / mechanically-induced apoptosis / periodic stretching, not heat" limitations.

**Claim 38 (device, in-vitro flavour).** Device comprising an immersion element containing a liquid medium **to immerse a plurality of cells comprising tumor cells and non-tumor cells** + transducers, same apoptosis-by-stretching limitations. (No "subject" — this one reaches a **bench/cell-culture** apparatus.)

**Dependent claims (summary).** 2/17 tumor = cancer or metastasized cells · 3/18 immersion element **shaped/geometrically configured to regulate the wave field** · 4/19 medium is **water** · 5–6/20–21 transducers on a **robotic arm** · 7/22 **phased array** · 8/23 **sealed/water-proof** transducers · 9/24 **30 kHz–250 kHz** (claim 9 also ≤250 mW/cm²) · 10/25 **5 kHz–50 kHz** (claim 10 also ≤250 mW/cm²) · 11/26 periodic forces preserve normal cells · 12/27 parameters chosen from tumor-cell type · 13–14/28–29 **treatment plan**, generated by **machine learning** · 15/30 controller driven by **sensor data** · 31 different procedures by adjusting the wave cycles · 32–34 **power ≤ 250 mW/cm²** · 35–37 **period of time ≈ 2 hours or more**.

**What this does and does not cover — practical read:**

| Aspect | Comment |
|---|---|
| **Purpose limitation** | Every independent claim requires **tumor cells** and **mechanically-induced apoptosis in tumor cells triggered by periodic stretching**. A device built and documented for **senescence reversal in normal cells / research** is aimed outside the claimed purpose. |
| **But: apparatus claims cover capability** | In US practice, an apparatus claim's "configured to … sufficient to" language is a **capability** limitation. The Sheetz cancer work used **33 kHz** (Tijore et al., *Bioeng. Transl. Med.* 2025; 39 kHz in mice) — the *same* frequency band as the senescence protocol. So an identical water-bath + 33 kHz + pulsed-modulation rig could be argued to be "configured to" trigger mechanical apoptosis in tumor cells. This is a real (if second-order) argument **in the US only**. Counter-arguments: the claim also requires the modulation/intensity to be *configured* to that end (design intent + programming), "without mechanically damaging" both cell populations, and claim 1 requires immersion of **a body part of a subject**. |
| **Elements a design can avoid** | (i) **no immersion vessel** (coupling gel / contact transducer / dry sonotrode) → outside all independents; (ii) **no programmed "cycles"**, i.e. CW or non-modulated → arguably outside; (iii) frequency outside 5–50 / 30–250 kHz only escapes the *dependents*, not the independents (independents have **no frequency limit at all** — do not rely on frequency to design around); (iv) avoid robotic arm / phased array / ML treatment planning / sensor-driven controller → avoids many dependents but dependents are irrelevant if you are outside the independent claim. |
| **Doesn't matter in Italy** | Territorial: a US patent grants rights only for making/using/selling/offering/importing **in the United States** (35 U.S.C. § 271(a)). Building and using one in Italy is not infringement of it, full stop. |

Source for claims: [US 12,714,885 B2 facsimile, cols. 21–24](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12714885); pre-grant text at [US 2022/0047894 A1](https://patents.google.com/patent/US20220047894A1/en). Note the claims **were amended during prosecution**: the published 2022 claims (33 claims) recited generic "target cells"; the granted claims add "tumor cells", "without mechanically damaging", "periodic stretching rather than heat", and the ≤250 mW/cm² / ≥2 h claims. That narrowing is exactly what leaves senescence use outside the granted scope.

### 2.2 US 2024/0001155 A1 (appl. 18/217,362) — senescence, US

Published claims (20), verbatim key ones:

- **Claim 1** (independent): "A method of treating an ailment in a subject, the method comprising administering a **therapeutic amount of pulsed or modulated ultrasound** to the subject." — breathtakingly broad; this is why it drew a rejection.
- **Claim 12** (independent): "A method of **slowing the aging process and/or reducing signs of aging** … administering a therapeutic amount of pulsed or modulated ultrasound."
- **Claim 17** (independent): method of treating an ailment associated with elevated senescent-cell burden: (a) **identifying a tissue with an elevated senescent cell burden**, (b) administering **pulses of LFU** to the tissue, **thereby reducing the number of senescent cells**.
- Dependents: LFU (cl. 2, 13); **30–100 kHz** (cl. 3, 19); applied to senescent cells (4); long list of senescence-associated diseases (6, 18); mitochondrial disease (7–8); combination with **Rho-kinase inhibitor or senolytic** (9–10, 14–15); **treatment duration 30–45 minutes** (11, 16); wound/bone healing, perfusion, recovery (20).

**Status:** pending; **non-final Office action mailed 2026-02-25** (INPADOC/USPTO STPP events on the Google Patents page). No granted B1/B2 with this title exists in the Google Patents index as of this check. Note the claims contain **no pressure limitation** and **no immersion limitation** — if they ever grant in this form (unlikely), they'd cover the *therapeutic use* in the US, not the hardware.

### 2.3 EP 4 561 696 A1 (EP 23850582.0) — senescence, Europe

Claims as published (95 claims, from the WO text; the EP A1 republishes the PCT claims). Independent claims: **1** (treating an ailment by administering a "stressor"), **13** (slowing aging / reducing signs of aging by a stressor), **20** (identify tissue with elevated senescent-cell burden + administer LFU in bursts/modulated intensities), **21** (treating an ailment with LFU), **35** (slowing aging with LFU), **43** and **75** (reversing senescence **in cells**), **55** (LFU on cultured cells → take supernatant → treat senescent cells with it), **63** (**increasing athletic performance**), **81** (identify tissue with senescent cells + administer a stress).

Parameter dependents worth memorising, because they are the numbers a DIY build will hit:
- **cl. 31, 40, 46, 60, 72, 89: "32 – 33 kHz and about 6 – 7 kPa"** ← the project's target parameters sit on top of this.
- cl. 11, 19: "about **20 – 40 kHz and about 6 – 11 kPa**"; cl. 41, 47, 73, 90: "20–40 kHz and about **3–11 kPa**"; cl. 61: "20–40 kHz and about **2–11 kPa**"; cl. 32: "20–40 kHz and about 11 kPa".
- cl. 10, 18, 30, 39, 45, 59, 65, 88: **treatment 30–45 minutes**; cl. 66: over ≥30 days.
- cl. 84: "**modulating cycles of ultrasound, each cycle comprised of an 'on' period followed by an 'off' period**" ← the 1.5 s on/off duty cycle.
- cl. 85 adjusting power output per cycle; cl. 86 **controlled beam travel, beam geometry and vat geometry**; cl. 91 **beam steering / frequency sweeps to homogenise the field**; cl. 92 **absorbent material to absorb ultrasonic energy**; cl. 54, 95 "**full body ultrasound spa**".

**EPO status** (from INPADOC legal events on Google Patents; the EPO Register itself returned HTTP 403 to automated fetch — ⚠️ *verify manually at* https://register.epo.org/application?number=EP23850582):
- EP regional phase entered **2025-02-28**; **examination requested 2025-02-06** (code 17P, effective 2025-02-06).
- **Designated contracting states (code AK, 2025-06-04): AL AT BE BG CH CY CZ DE DK EE ES FI FR GB GR HR HU IE IS IT LI LT LU LV MC ME MK MT NL NO PL PT RO RS SE SI SK SM TR** — **Italy is designated.**
- Validation/extension states deleted (2025-11-05). HK reference (2026-01-30) indicates a Hong Kong re-registration hook.
- No Art. 94(3) communication, no Rule 71(3) intention to grant, **no grant** visible. Non-entry into DE national phase of the PCT is irrelevant (the EP route covers DE).

**Why these claims cannot grant as filed in Europe:** EPC **Art. 53(c)** excludes "methods for treatment of the human or animal body by surgery or therapy". Claims 1, 13, 20, 21, 35, 81 are exactly that. Italian **CPI art. 45(4)** mirrors it nationally. Survivable routes for the applicant: (i) **in-vitro/ex-vivo claims** (43, 55, 75 — cultured cells) — not excluded; (ii) **purely cosmetic / non-therapeutic** claims ("reducing signs of aging", "increasing athletic performance") — EPO case law allows cosmetic methods **only if the cosmetic effect is clearly separable from any therapeutic effect**, which is contestable here; (iii) **device/apparatus claims** — but the PCT as filed is method-heavy, and Art. 123(2) limits what can be pulled from the description; (iv) "substance or composition for use" claims under Art. 54(4)/(5) are **not available for devices** — an ultrasound machine cannot get novelty from a new therapeutic purpose. **Expected outcome: whatever grants in Europe will be much narrower than the US filing, and may be in-vitro or apparatus-shaped.** ⚠️ This is my analysis, not a documented EPO position.

**Additional novelty exposure (analysis, unverified by an EPO file inspection):**
- The inventors' own preprint **"Rejuvenation of Senescent Cells … by Low-frequency Ultrasound"** was posted on **bioRxiv 2022-12-08** ([v4](https://www.biorxiv.org/content/10.1101/2022.12.08.519320v4); published version: *Aging Cell* 2025;24:e70008, [doi](https://onlinelibrary.wiley.com/doi/10.1111/acel.70008)). Europe has **no grace period**: any claim in EP 4 561 696 **not validly entitled to the 2022-06-30 priority** is anticipated by the authors' own preprint (filed PCT 2023-06-30).
- **WO 2023/114011 A1** (UT System, same lead inventor) published **2023-06-22**, **eight days before** the PCT filing date of the Mechanobiologics case → full Art. 54(2) prior art for anything not entitled to priority.
- The earlier **WO 2020/223359 A1** (immersion + programmed ultrasound cycles, 5–50 / 30–250 kHz, water medium, published 2020-11-05) is prior art against the hardware aspects of the senescence family.

### 2.4 UT System family (US 2024/0399175 A1, EP 4 447 814, WO 2023/114011)

Independent claims: **1** "A non-invasive method of **treating aging** comprising: **mechanically stretching at least one living cell** in an amount sufficient to delay at least one aging characteristic"; **22** "A method of **reducing cellular senescence** comprising applying a **repetitive low frequency ultrasound treatment** to at least one living cell, wherein [it] delays at least one aging characteristic."
Notable dependents: cl. 4 / 43 **immersion design with one or more chambers, full immersion, absorber shield around the treatment zone, transducers and absorber contacting the patient or insulated by the immersion medium**; cl. 23 **wavelength ≥ average cell diameter**; cl. 8 (EP) frequency list "5, 10, 15, 20, 25, 30, 35, 40 … kHz"; cl. 9/30 intensity list "10 … 500 … <500 mW/cm²"; cl. 6/25 **5–60 min, repeated daily→twice weekly**; cl. 15/37 controller architecture (**remote drivers limiting energy for patient safety, neutral drivers with zero net voltage across transducer elements, transducer stacks reducing peak voltage**); cl. 18/34 transducer technologies (piezo, voice coil, capacitive membrane, spark discharge, phased array, synthetic aperture …).

**This family is the one that most directly claims the senescence protocol AND is prosecuted in Europe with Italy designated.** US: final rejection 2025-12-03, re-docketed 2026-05-04. EP: supplementary European search report despatched **2026-04-13** (EP 4 447 814 A4); examination pending; same Art. 53(c) problem for claims 1 and 22 as written.

---

## 3. What a DIY, non-commercial project **in Italy** can do

Legal basis:
- **CPI art. 68(1)(a)** — the exclusive right does **not** extend to "**atti compiuti in ambito privato ed a fini non commerciali**" (acts done privately and for non-commercial purposes). [Brocardi — art. 68 CPI](https://www.brocardi.it/codice-della-proprieta-industriale/capo-ii/sezione-iv/art68.html)
- **CPI art. 68(1)(a-bis)** — nor to "**atti compiuti a titolo sperimentale relativi all'oggetto dell'invenzione brevettata**" (acts done experimentally relating to the subject-matter of the patented invention). Unlike the US, this exemption is **broad and purpose-based**, and is generally understood to cover research *on* the invention (verifying, improving, designing around), including in institutional settings; it does **not** cover using the invention as a mere tool for unrelated commercial production.
- **UPCA art. 27(a) and (b)** — identical carve-outs for acts done **privately and for non-commercial purposes** and for **experimental purposes relating to the subject-matter of the invention**, applicable to European patents with unitary effect and to classic EPs litigated before the UPC. Italy participates in the UPC (Milan seat of the central division). [Commented UPC — art. 27](https://commentedupc.com/agreement/article-27/)
- **Territoriality** — Italian/EP patents bite only in their states; **US 12,714,885 has no effect in Italy** (its own statutory reach is acts "within the United States", 35 U.S.C. § 271(a)).
- **CPI art. 45(4)** / **EPC art. 53(c)** — methods of surgical/therapeutic treatment of the human body are not patentable in Italy/EPO, so even a future EP grant cannot cover the *act of treating a person*; only devices/in-vitro methods can be covered.

**Therefore, today, in Italy, the project can:**
- ✅ **Build one or more prototypes** of the transducer/tank/driver and use them in the lab or at home for research and self-experimentation. Nothing is granted in Italy; and even if something granted tomorrow, 68(1)(a)/(a-bis) + UPCA 27(a)/(b) apply.
- ✅ **Run in-vitro experiments** (cells in a dish inside the water bath), publish the results, replicate or fail to replicate the Aging Cell findings. In-vitro claims are the ones most likely to survive in Europe, but experimenting *on the claimed invention* is the paradigm case for the experimental-use exemption.
- ✅ **Publish the complete design, firmware, BOM, calibration procedure and data on GitHub.** Publication is not an act of "making, using, offering, selling or importing" under CPI art. 66 / UPCA art. 25–26. Writing about how to build a patented thing is not patent infringement in Italy or in the EU (and patent specifications are themselves published documents). **Caveat:** avoid copy-pasting substantial text or figures *from* the patent documents into your repo without attribution — that's a copyright question, not a patent one; short quotes with citation are fine, and USPTO/EPO publications are generally freely reusable, but don't reproduce the papers (Aging Cell is © Wiley).
- ✅ **Use the published patent applications as a technical source.** That's what publication is for; there is no "contamination" doctrine in Europe (and the US doctrine of wilfulness only matters for damages, which require infringement in the first place).
- ✅ **Discuss, present, teach, demo** the device at hackspaces/conferences (a non-commercial demo is not an offer for sale; see grey areas below).

## 4. What it **cannot** do (or must not do without counsel)

- ❌ **Sell kits, PCBs, transducers-as-a-set, or assembled devices** — even "at cost", even "for research use only". A sale is a commercial act; it takes you out of art. 68(1)(a) instantly, and it creates EU **MDR 2017/745** exposure the moment the thing is presented for a medical purpose. Selling into the US would additionally expose you to US 12,714,885 (direct infringement under §271(a) as an importer/seller, or contributory infringement under §271(c)) if the device falls within its claims.
- ❌ **Offer treatments/sessions to other people**, paid or free, in a wellness/spa/clinical setting. That's (i) commercial or at least non-private use, (ii) potentially the unlicensed practice of medicine and an unregistered medical device in Italy, (iii) the exact subject matter of the pending claims ("full body ultrasound spa" is literally recited in EP claims 54 and 95).
- ❌ **Make medical claims** ("reverses aging", "treats osteoarthritis", "senolytic") on a website, in a README or on a product page. This is the fastest route from "open-hardware research" to "unregistered medical device with misleading health claims" under MDR art. 7 and Italian consumer/advertising rules — independently of patents.
- ❌ **Human experimentation on third parties** without ethics approval (Comitato Etico), informed consent, and — for a device study — MDR clinical-investigation rules. Self-experimentation by the builder is a different, thinner, but non-zero risk category.
- ❌ **Crowdfunding a production run** — that is an "offer for sale" and commercial intent, in both EU and US law.

## 5. Grey areas (flagged, not resolved)

| Grey area | Why it's grey |
|---|---|
| **"Non-commercial" with any money flow** | Donations, Patreon, Open Collective, charging for materials, an associazione selling to its members: Italian doctrine reads art. 68(1)(a) as requiring acts that are *both* private *and* non-commercial. Reimbursement at cost among a research group is probably fine; a "contribution" for a shipped board is probably not. |
| **Distributing physical parts for free** | Free distribution is not "selling", but CPI art. 66(2) covers "mettere in commercio" and "usare"; giving devices to third parties who then use them at home moves the use outside your private sphere. Low risk while nothing is granted in Italy; re-assess if EP 4 447 814 / EP 4 561 696 grant. |
| **Publishing instructions read by US users** | No direct infringement by you (acts outside the US). **Inducement, 35 U.S.C. § 271(b)**, requires knowledge of the patent **and** specific intent to encourage the infringing acts (*Global-Tech v. SEB*, 563 U.S. 754 (2011)). A neutral, research-framed publication that does not target US users, does not instruct anyone to *treat tumors by immersion*, and does not supply hardware, is a weak inducement case — but your repo will demonstrably show knowledge of the patent if you cite it. Mitigation in §8. |
| **Building it *as if* for tumor treatment** | Anything in the repo saying "this also kills cancer cells" edges the hardware toward the granted US claims' functional language and supplies intent evidence. Keep cancer out of the project's stated purpose. |
| **University/institutional use in Italy** | Art. 68(1)(a-bis) covers experimental acts on the invention; using the device as a routine *tool* in funded contract research is closer to the commercial edge. Italian experimental use is far more generous than the US, but not unlimited. |
| **Reproducing the exact 32–33 kHz / 6–7 kPa numbers** | Those numbers are recited in EP claims 31/40/46/60/72/89. In Italy that only matters if an EP grants with those claims *and* your acts are commercial. For an open publication it's actually useful: your published measurements become prior art/defensive material. |
| **UPC opt-out geography** | If EP 4 561 696 or EP 4 447 814 grants, it may be enforced via the UPC across Italy + participating states in one action. The art. 27(a)/(b) exemptions still apply, but the practical cost of being sued in the UPC is high even when you win. |

## 6. US perspective

- **Direct infringement (§271(a))** requires making/using/offering/selling in, or importing into, the US. An Italian builder doing none of those is untouchable under US 12,714,885.
- **US experimental use is essentially dead**: *Madey v. Duke University*, 307 F.3d 1351 (Fed. Cir. 2002) — the common-law exception is limited to acts "for amusement, to satisfy idle curiosity, or for strictly philosophical inquiry", and does **not** apply to acts in furtherance of an institution's legitimate business (including a university's research mission). A US collaborator replicating this in a university lab has **no meaningful research shield** for anything falling inside the claims. (The §271(e)(1) safe harbour only covers activity reasonably related to FDA submissions — potentially relevant if a US partner is generating data for an FDA pathway; unlikely here.)
- **Medical-practitioner immunity, 35 U.S.C. § 287(c)**: bars remedies against a licensed practitioner/health-care entity for performing a patented **medical activity** — but expressly **excludes** "the use of a patented machine, manufacture, or composition of matter in violation of such patent". Since '885's claims are device-centred, this immunity is largely unavailable.
- **Inducement (§271(b))/contributory (§271(c))**: see grey areas. Supplying a component "especially made or adapted" for infringing use, with no substantial non-infringing use, is contributory infringement — another reason not to ship transducer/driver kits to the US.
- **Design-around headroom in the US**: the granted independents require immersion + programmed modulated cycles + tumor-cell apoptosis by stretching. A senescence rig documented for **normal-cell rejuvenation and in-vitro research**, with no tumor-apoptosis functionality or claims, is a substantial distance from claims 1/16, and claim 38 still requires the "tumor cells and non-tumor cells" immersion and the apoptosis-by-stretching configuration. ⚠️ Whether "configured to" is read as capability or as design intent is the swing issue, and it is genuinely uncertain.

## 7. Prior art relevant to an open design (useful both defensively and for freedom-to-operate)

| Prior art | Why it matters |
|---|---|
| **WO 2020/223359 A1 / WO 2020/223242 A1** (Mechanobiologics, pub. 2020-11-05) | Their own earlier publication of immersion + programmed ultrasound cycles, water medium, **5–50 kHz / 30–250 kHz**, transducer arrays, treatment planning. **Not patented in Europe** (no EP phase) → this content is **free to use in Europe** and is prior art against later claims. |
| **US 2022/0203138 A1** (abandoned 2025) & **US 2021/0244972 A1 / KR 10-2021-0101481** (KIST, abandoned) | KIST's "device for removing senescent cells comprising an ultrasound output unit" (prio. 2020-02-10) claims ultrasound at "5 kHz–450 MHz, −10 to 10 MPa, PRF 0.02 Hz–500 kHz, duty cycle 0.1–99.9%" targeting senescent cells — **published, abandoned, and squarely prior art** for senescent-cell-directed ultrasound devices. |
| **Low-frequency therapeutic ultrasound, 20–100 kHz** — MIST Therapy (Celleration), FDA 510(k) **K050129** (2005), transducer nominal **40 kHz** (measured 39.5 kHz, harmonics 79/118.5/158 kHz) | Decades of 20–100 kHz therapeutic ultrasound on human tissue with documented biological effects. [Characterization of the MIST beam, PubMed 23562019](https://pubmed.ncbi.nlm.nih.gov/23562019/) |
| **Söring Sonoca-185, 25 kHz** ultrasound-assisted wound debridement | Commercial low-frequency ultrasound in an irrigation/liquid coupling context, long predating 2019. |
| **Ultrasonic cleaning baths, 20–45 kHz, with degassing and pulsed modes** | Ubiquitous commodity hardware: immersion vessel + piezo transducers + pulsed/sweep drive. Any claim to "immersion vessel + transducers + on/off cycles" *per se* is hard to sustain over this. This is exactly the commodity base an open design should sit on and cite. |
| **US 3,499,437 (Balamuth, 1970)** and other references cited on the face of US 12,714,885 | The examiner's own cited art shows the long history of ultrasonic therapy hardware. |
| **Kureel et al., bioRxiv 2022-12-08 → *Aging Cell* 2025;24:e70008**; Tijore et al., *Bioeng. Transl. Med.* 2025 (33 kHz in vitro, 39 kHz in mice) | The scientific disclosure of the protocol itself — published, citable, and (for Europe) potentially novelty-destroying against non-priority-entitled claims. |

**Defensive publication.** Publishing the project's own design decisions, measured pressures, duty-cycle schedules, tank geometry, absorber design and calibration method — **dated, versioned, and archived** — makes them prior art against **future** filings by anyone (including Mechanobiologics continuations, which are still live: the US senescence case is in prosecution and continuations of 17/515,025 are likely). To make the publication robust: tag releases, push to a timestamped third-party archive (Zenodo DOI, Internet Archive, arXiv/bioRxiv for the methods paper, or a formal defensive-publication venue such as IP.com / Research Disclosure / TDCommons), and keep the git history public. Note this **defends the commons; it does not give you freedom to operate** against claims that already have an earlier priority date.

## 8. Recommendations

1. **Frame the project explicitly as non-commercial research and self-study.** Put it in the README and in the licence header: no sales, no kits, no services, no medical claims, no treatment of third parties. This single framing is what art. 68(1)(a)/(a-bis) CPI and UPCA art. 27(a)/(b) key on.
2. **Never sell or ship hardware** — not kits, not PCBs, not "at cost", not to the US. Point people to a BOM of generic parts they buy themselves from ordinary suppliers.
3. **Keep cancer/tumour out of the project's stated purpose and out of the firmware feature set.** The only granted patent is a tumour-apoptosis patent; staying rhetorically and functionally far from it is cheap insurance.
4. **Avoid therapeutic claims entirely.** Describe measured physical output (kHz, kPa, duty cycle, field uniformity) and, if you run cells, report biomarkers. No "treats", no "cures", no "anti-aging therapy".
5. **Add an IP/legal notice to the repo**: list the patents/applications (numbers + links), state that the project makes no representation of freedom to operate, that it is published for research and documentation purposes under art. 68 CPI / UPCA art. 27, and that **users outside Italy — especially in the US — are responsible for their own compliance** including with US 12,714,885. A clear, neutral notice that *discourages* infringing US use is also the best available answer to a §271(b) inducement theory.
6. **Do a defensive publication** of your own design (Zenodo DOI + git tags + a methods preprint). Cheap, fast, and it protects the commons against continuations still in prosecution.
7. **Choose a licence that matches**: CERN-OHL-S v2 or CERN-OHL-W for hardware, plus a non-patent-granting notice; note that open-hardware licences do **not** grant you rights under third-party patents — only under the contributors' own.
8. **Monitor four dockets** (quarterly is enough): (a) **US 17/515,025** for continuations; (b) **US 18/217,362** (response to the 2026-02-25 non-final action); (c) **EP 23850582.0** (EP 4 561 696) — Art. 94(3) communications, amended claims, grant; (d) **EP 22908221.9** (EP 4 447 814, UT System) — examination after the 2026-04-13 supplementary search report. If either EP case heads toward grant with claims that reach hardware or in-vitro use, re-run this analysis **before** any change of activity. If you want to influence the outcome, third-party observations under **EPC art. 115** are free and anonymous, and the prior art in §7 is the ammunition.
9. **Get Italian/EU counsel before**: any money changes hands; any device leaves your hands; any human other than you is exposed; any public demo where devices are offered; any institutional/university collaboration; any US collaborator replicates the build.
10. **Regulatory, not IP, but adjacent**: a device used only by its maker on themselves is not "placed on the market" under **MDR 2017/745** and is outside CE-marking duties, but the moment it is supplied to anyone else for a medical purpose, MDR applies (including, for in-house builds, the narrow health-institution exemption of MDR art. 5(5)). Electrical safety (LVD/EMC) and acoustic-exposure safety also apply to anything given to others. Treat mains-powered ultrasonic drivers around a water tank as a genuine electrical hazard independent of any law.

---

## 9. What could not be verified

| Item | Why | How to close the gap |
|---|---|---|
| Whether a **continuation of US 17/515,025** was filed before the 25 Aug 2026 grant | Google Patents has not yet indexed US 12,714,885 (404); Justia returned HTTP 403; USPTO Patent Center API returned 401 unauthenticated | USPTO Patent Center → appl. 17/515,025 → "Continuity Data"; or Patent Public Search for recent Mechanobiologics filings |
| **EPO Register detail** for EP 23850582.0 and EP 22908221.9 (examination communications, pending claim sets, representative, annuity status) | register.epo.org returned HTTP 403 to both direct fetch and WebFetch | Open register.epo.org manually, or use EPO OPS with credentials; INPADOC events used here are a partial proxy |
| The **exact pressure/intensity and duty cycle** used in the Tijore cancer paper (to judge how close the cancer device is to the senescence device) | Only the abstract/partial text was retrievable; frequency (33 kHz in vitro, 39 kHz in mice) confirmed, pressures not | Read the full *Bioeng. Transl. Med.* 2025 methods section |
| Whether **Mechanobiologics has any non-published (unfiled/unpublished) applications** | 18-month publication delay means filings after ~March 2025 may not be visible | Re-check assignee searches quarterly |
| **JP 2024-546976 / AU 2022415191** prosecution status (UT family) | Not examined in this pass; irrelevant to Italy | Google Patents / J-PlatPat / AusPat if ever relevant |
| Italian case law applying art. 68(1)(a)/(a-bis) to hobbyist hardware | No Italian decisions on point were located in this pass | Counsel / Italian IP databases (De Jure, Darts-IP) |

---

### Source list (primary)

- US 12,714,885 B2 granted text (PDF facsimile): https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12714885
- US 2022/0047894 A1 (pre-grant pub. of 17/515,025): https://patents.google.com/patent/US20220047894A1/en
- US 2024/0001155 A1 (18/217,362): https://patents.google.com/patent/US20240001155A1/en
- WO 2024/030212 A1: https://patents.google.com/patent/WO2024030212A1/en
- EP 4 561 696 A1: https://patents.google.com/patent/EP4561696A1/en · Register (403 on fetch): https://register.epo.org/application?number=EP23850582
- US 2024/0399175 A1 (UT System): https://patents.google.com/patent/US20240399175A1/en
- EP 4 447 814 A1 (UT System): https://patents.google.com/patent/EP4447814A1/en
- WO 2020/223359 A1: https://patents.google.com/patent/WO2020223359A1/en · WO 2020/223242 A1: https://patents.google.com/patent/WO2020223242A1/en · US 2022/0203138 A1: https://patents.google.com/patent/US20220203138A1/en
- US 2021/0244972 A1 (KIST): https://patents.google.com/patent/US20210244972A1/en
- CPI art. 68: https://www.brocardi.it/codice-della-proprieta-industriale/capo-ii/sezione-iv/art68.html
- UPCA art. 27: https://commentedupc.com/agreement/article-27/
- Kureel et al., bioRxiv 2022-12-08: https://www.biorxiv.org/content/10.1101/2022.12.08.519320v4 · Aging Cell 2025: https://onlinelibrary.wiley.com/doi/10.1111/acel.70008
- Tijore et al., Bioeng. Transl. Med. 2025 (33 kHz): https://pubmed.ncbi.nlm.nih.gov/40060768/
- MIST Therapy beam characterization (40 kHz nominal / 39.5 kHz measured, 510(k) K050129): https://pubmed.ncbi.nlm.nih.gov/23562019/

*Prepared 2026-09-16. Again: not legal advice.*
