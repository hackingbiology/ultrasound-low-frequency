# Misurare la senescenza cellulare prima/dopo un intervento LFU (ultrasuoni a bassa frequenza)
## Protocollo di biomarcatori per un progetto di biohacking open source in Italia

**Versione:** 2026-09-16 · **Autore:** ricerca condotta per HackingBiology / biohack.it
**Encoding:** UTF-8 · **Stato:** documento di ricerca, non consulenza medica

> ⚠️ **Avvertenza generale.** Questo documento descrive *come misurare*, non *cosa fare*. LFU sull'uomo non ha
> alcun dato clinico pubblicato (il paper Kureel/Sheetz 2025 è in vitro + topi; l'unico RCT umano, NCT07168525,
> è iniziato il 29/10/2025 e terminerà a dicembre 2026). Qualunque auto-sperimentazione va discussa con un medico;
> nessun esame del sangue può escludere un tumore (§7).

---

## 0. Contesto: cosa stiamo cercando di misurare

### 0.1 L'intervento
Kureel, Maroto, … Rasmussen, Sheetz, *Aging Cell* 2025, "Rejuvenation of Senescent Cells, In Vitro and In Vivo,
by Low-Frequency Ultrasound", doi:10.1111/acel.70008 — parametri ottimali riportati: **32,2 kHz, ~4 kPa,
30 min, duty cycle 1,5 s on / 1,5 s off**; nei topi trattamenti giornalieri→ogni 3 giorni, cicli di 2 settimane.
Marcatori usati nel paper: SA-β-gal, p16, p21, EdU/proliferazione, SASP (IL-6, IL-8, TNF-α, IFN-γ, VEGF, MIP-1α),
lunghezza telomerica, 5mC, morfologia mitocondriale; in vivo SA-β-gal su rene e pancreas, performance fisica.
Meccanismo proposto: ingresso di **Ca²⁺ via Piezo1** → dinamica dell'actina → autofagia → inibizione mTORC1,
traslocazione di SIRT1. **Nessun dato umano. Nessun tumore osservato in topi >300 giorni.**
<https://pmc.ncbi.nlm.nih.gov/articles/PMC12151899/> · <https://onlinelibrary.wiley.com/doi/10.1111/acel.70008>

### 0.2 Il trial umano di riferimento (NCT07168525, UT Health San Antonio)
20 soggetti ≥70 anni, 10 LFU vs 10 sham, **vasca da bagno con trasduttore, 45 min, 3×/settimana per 8 settimane**,
single-blind. **Outcome primario:** forza di estensione del ginocchio (dinamometro Biodex), baseline→8 settimane.
**Secondari:** SPPB, TUG, 6MWT, "cellular senescence" su sangue (IHC + biochimica + RNA-seq), "immune aging"
(epigenetica), NIH Toolbox Face-Name memory, massa magra e massa grassa DEXA; prelievi a baseline e 8 settimane
(inclusa HbA1c). <https://clinicaltrials.gov/study/NCT07168525>

→ **Implicazione di design:** il trial usa **2 soli punti temporali (0 e 8 settimane)** e un braccio sham identico.
Un n-of-1 non ha il braccio sham, quindi deve compensare con **più baseline ripetuti** e con marcatori a bassa
variabilità intra-individuale (§5).

### 0.3 Il problema di fondo: non esiste un gold standard ematico per la senescenza
- Olinger & Basisty, *Ageing Research Reviews* 2026, "A Compendium of Circulating Biomarkers of Senescence in
  Humans": i marcatori circolanti con più evidenza trasversale sono **GDF15 (19 studi), Activin A (12), IL-6 (10),
  MMP1 (10), MMP7**; moderati: TNFR1, OPN, FAS, CCL11, MMP2, cistatina C, TIMP1, IGFBP2. Limite esplicito:
  «è attualmente impossibile discernere i tessuti di origine … e distinguere la senescenza da altri fattori».
  <https://pmc.ncbi.nlm.nih.gov/articles/PMC13408882/>
- Nessuno di questi marcatori è *specifico* per le cellule senescenti: sono marcatori di
  infiammazione/stress/mitocondri che *correlano* con il carico senescente.
- Ne consegue la strategia: **pannello multi-marcatore + funzione fisica**, non un singolo numero.

---

## 1. Stato dell'arte 2024-2026: senescenza misurata dal sangue

### 1.1 p16INK4a (CDKN2A) mRNA nei linfociti T CD3+ — il marcatore "storico"
- **Cosa misura:** espressione di p16 (inibitore di CDK, effettore del blocco del ciclo cellulare) in linfociti T
  purificati. È il marcatore ematico più vicino al concetto di "carico senescente".
- **Evidenza:** Liu, Sharpless et al., *Aging Cell* 2009 (PMC2752333): 10-15 mL sangue, isolamento CD3+ via
  MACS (>90% purezza), qRT-PCR TaqMan normalizzata su 18S + β2-microglobulina, dati log2. Correlazione con l'età
  r = 0,63 (R² 0,40), **~10× di aumento su sei decadi**; fumo ≈ raddoppia la pendenza; attività fisica correla
  negativamente (r −0,38…−0,42); correlazione con IL-6 plasmatica r 0,27-0,33; stabilità test-retest verificata
  in 7 soggetti ritestati >4 settimane dopo. <https://pmc.ncbi.nlm.nih.gov/articles/PMC2752333/>
- **Esercizio (12 settimane, 2×/sett., anziani):** Englund et al., *Aging Cell* 2021 — riduzione di p16, p21 e
  cGAS nei CD3+ e di diverse proteine SASP (incl. MPO, PAI-1/serpin E1).
  <https://onlinelibrary.wiley.com/doi/10.1111/acel.13415> · <https://pmc.ncbi.nlm.nih.gov/articles/PMC8282238/>
- ⚠️ **Confondente critico per LFU:** Lepola, Guan & Burd, *Innovation in Aging* 2025 — **l'attivazione del
  linfocita T induce p16 in modo Ca²⁺-dipendente** (segnale CD3, amplificato da IL-2, abolito da ciclosporina A).
  Poiché LFU agisce proprio via **influsso di Ca²⁺/Piezo1**, un aumento acuto di p16 nei T potrebbe riflettere
  attivazione e non senescenza. Campionare **≥48-72 h dopo l'ultima seduta** e registrare infezioni/vaccini.
  <https://pmc.ncbi.nlm.nih.gov/articles/PMC12761409/>
- **Disponibilità commerciale:** **Sapere Bio** (Research Triangle Park, NC) — reagenti p16 usati in numerosi
  paper; il prodotto clinico è **SapereX** (espressione di p16, p14, LAG3, CD28, CD244 in linfociti T periferici),
  laboratorio **CLIA/CAP**, disponibile «in select clinics as part of an IRB-approved registry», ordinabile solo
  da medici longevity/concierge. Prezzo non pubblicato; **nessuna evidenza di accettazione di campioni dall'Italia**.
  <https://www.saperex.com/> · <https://www.saperebio.com/newsroom>
  🚩 **NON VERIFICATO:** spedizione internazionale, stabilità del campione nel transito, prezzo.
  "HealthSpan Diagnostics" non risulta più come fornitore attivo di un test p16 (nessun riscontro web 2026). 🚩
- **Alternativa realistica in Italia:** farlo fare a un laboratorio di ricerca partner (§2.3): 10-15 mL EDTA,
  isolamento CD3+ con microbeads, RNA + RT-qPCR. Costo materiali ~40-90 €/campione (kit isolamento + RNA + qPCR),
  fattibile in qualunque laboratorio universitario di biologia molecolare. 🚩 stima, non listino 🚩

### 1.2 p21, cGAS, pannelli trascrittomici (SenMayo)
- p21 (CDKN1A) si misura con la stessa RT-qPCR su CD3+; ridotto dall'esercizio (Englund 2021).
- **SenMayo** (125 geni; Saul et al., *Nat Commun* 2022) è il gene set di riferimento per la senescenza su
  RNA-seq/NanoString; validato su tessuti e tracciante della clearance di cellule p16+ nei modelli.
  <https://pubmed.ncbi.nlm.nih.gov/35974106/> — NB: nel trial NCT07168525 la senescenza ematica è misurata
  anche via **RNA-seq**, quindi SenMayo su PBMC/CD3+ è l'analogo "home-brew" più vicino al protocollo ufficiale.
- Evidenza per un uso n-of-1: **debole** (nessun dato di ripetibilità intra-soggetto pubblicato). 🚩

### 1.3 Citofluorimetria: T senescenti (CD28-null, CD57, KLRG1, CD8 TEMRA) e SA-β-gal
- **CD28⁻/CD57⁺/KLRG1⁺ CD8⁺, TEMRA (CD45RA⁺CCR7⁻):** fenotipo di differenziazione terminale, aumenta con l'età,
  ma è **fortemente guidato dal CMV**: la frequenza di CD28-null CD8⁺ dipende dalla sieropositività CMV più che
  dall'età. Quindi va misurato lo status CMV IgG una volta sola, e i confronti sono solo intra-persona.
  <https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2017.00649/full>
  ⚠️ caveat di specificità: cellule CD28⁻CD57⁺ in pazienti oncologici producono granuli citotossici e IFN-γ
  **senza essere senescenti** → il fenotipo non equivale a senescenza.
  <https://www.tandfonline.com/doi/full/10.1080/2162402X.2024.2367777>
- **SA-β-gal in citometria su PBMC:** Martínez-Zamudio et al., *Aging Cell* 2021 — substrato fluorogenico di
  2ª generazione; la frazione SA-βGal-high cresce con l'età soprattutto nei **CD8⁺** (media 64% nei donatori
  in sesta decade); tali cellule hanno p16/p21 alti, foci di danno al DNA e proliferazione ridotta.
  <https://pmc.ncbi.nlm.nih.gov/articles/PMC8135084/>
  Kit: **CellEvent Senescence Green Flow Cytometry Assay** (Thermo C10840, 50 test, ~350 USD; C10841 200 test)
  <https://www.thermofisher.com/order/catalog/product/C10840>; alternativa **SPiDER-βGal** (Dojindo).
  Richiede PBMC freschi (ideale <4-6 h dal prelievo) e un citofluorimetro → **solo con laboratorio partner**.
- Evidenza: **media-alta** come marcatore di età; **nessun dato n-of-1** sulla ripetibilità settimana-su-settimana. 🚩

### 1.4 Lunghezza telomerica
- **Metodi:** qPCR T/S (economico, rumoroso), **flow-FISH** (RepeatDx, clinico, per sospette telomeropatie),
  **HT Q-FISH** (Life Length, misura >100.000 telomeri, riporta % di telomeri corti).
- **Rumore:** simulazione di Nettle et al., *PLOS One* 2019 — l'errore sui Cq si amplifica nel rapporto T/S,
  produce correlazioni basse tra misure successive e un artefatto di "regressione verso la media" che imita
  l'accorciamento dipendente dal basale. CV intra-assay tipico 2-3%, inter-assay ~3%, ma la ripetibilità
  reale del T/S crolla rapidamente con piccoli aumenti dell'errore.
  <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0216118>
- **Verdetto per 8 settimane di LFU: inutile.** La variazione biologica attesa in 2 mesi è ordini di grandezza
  sotto il rumore analitico. Ha senso solo come misura "una tantum" di caratterizzazione basale.
- **Disponibilità EU/Italia:** Life Length (Madrid) – test TAT personale **399 €** in Europa (via partner);
  <https://lifelength.com/> · <https://telomas.com/pages/partners-life-length>. In Italia: pacchetti "longevità"
  di centri privati (es. Centro Medico Diagnostico San Pietro) includono la lunghezza telomerica
  <https://www.cmdsanpietro.it/service/anti-aging-e-longevity/percorso-longevita-check-up-in-day/>;
  NutriHealth Genomics e GEK Lab (BioAge) offrono test telomerici DTC (🚩 metodo e prezzo non verificati: le
  pagine non erano accessibili al fetch 🚩). Riferimento storico di mercato: ~500 € per il test ematico.
- Kit per laboratorio partner: **ScienCell Absolute Human Telomere Length qPCR (8918)** ≈ 561 USD/kit
  <https://www.fishersci.com/shop/products/telomeres-nucleotide-kit/NC1503693>.

### 1.5 γH2AX nei linfociti
- Foci endogeni di γH2AX in PBMC aumentano linearmente con l'età fino a ~57 anni e si associano a patologie
  età-correlate (PLOS One 2012). <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0045728>
- Alta variabilità inter-persona, richiede microscopia/citometria standardizzata, nessun fornitore clinico.
  **Evidenza per n-of-1: bassa.** Solo con partner accademico e solo come endpoint esplorativo.

### 1.6 Pannelli SASP plasmatici (il cuore pratico del protocollo)
- **Schafer et al., *JCI Insight* 2020** (doi 10.1172/jci.insight.133668) — "The senescence-associated secretome
  as an indicator of age and medical risk": in una coorte 20-90 anni, **GDF15 e Activin A** sono i migliori
  predittori dell'età cronologica, seguiti da **TNFR1** (ognuno ≥10% della varianza); un pannello di 7 fattori
  (**GDF15, FAS, osteopontina/OPN, TNFR1, Activin A, CCL3/MIP-1α, IL-15**) predice gli eventi avversi
  post-chirurgici meglio dell'età o di un singolo marcatore. <https://insight.jci.org/articles/view/133668>
- **St. Sauver et al., *Aging Cell* 2023** (Mayo, n=1923 ≥65 anni): i 5 marcatori più associati a mortalità sono
  **GDF15, RAGE, VEGFA, PARC/CCL18, MMP2**. <https://onlinelibrary.wiley.com/doi/10.1111/acel.14006>
- **Interventi che spostano il SASP** (utile per capire gli effetti attesi):
  - **D+Q, malattia renale diabetica** (Hickson 2019, *EBioMedicine*): p16 −35%, p21 −17%, SA-βgal −62% nel
    tessuto adiposo; p16/p21 −38%/−30% nell'epidermide; **IL-1α, IL-2, IL-6, IL-9, MMP-2, MMP-9, MMP-12
    significativamente più bassi 11 giorni dopo** 3 giorni di terapia.
    <https://www.thelancet.com/article/S2352-3964(19)30591-2/fulltext>
  - **D+Q, IPF** (Justice 2019, *EBioMedicine* 40:554-563, n=14, open-label): endpoint primari di fattibilità;
    miglioramenti funzionali (6MWT, gait speed) con SASP come outcome esplorativo.
    <https://www.thelancet.com/journals/ebiom/article/PIIS2352-3964(18)30629-7/pdf>
  - **Restrizione calorica**: ↓GDF15, OPN, FAS, MMP1, TNFR1, IL-7, PAI-1 (Olinger & Basisty 2026, compendio).
  - **Esercizio 12 settimane**: ↓MPO, PAI-1, ADAMTS1, p16/p21 nei CD3+ (Englund 2021).
  → **Ordine di grandezza degli effetti attesi: 10-30% su singoli analiti, in studi con decine di soggetti.**
    Un n-of-1 vede solo variazioni ≳ RCV (§5) — cioè, realisticamente, solo GDF15 e marcatori funzionali.
- **cfDNA / cf-mtDNA:** aumenta con l'età e con l'infiammazione; livelli bassi correlano con buona salute ed
  esercizio (Teo et al., *Aging Cell* 2019). Molto sensibile a pre-analitica (emolisi, tempo di centrifugazione)
  e all'esercizio acuto. **Esplorativo.** <https://onlinelibrary.wiley.com/doi/full/10.1111/acel.12890>
- **suPAR:** marcatore di attivazione immunitaria/infiammazione cronica, predittore di mortalità; nel compendio
  2026 associato a mortalità e a molti outcome. In Italia è usato **in ambito ospedaliero** (es. Policlinico di
  Milano, algoritmo anakinra nel COVID) con immunoturbidimetria ViroGates.
  🚩 Non ho trovato nessun listino di laboratorio privato italiano che offra suPAR al cittadino. 🚩
  <https://biochimicaclinica.it/en/valutazione-di-un-pannello-di-biomarcatori-come-surrogato-del-recettore-solubile-dellattivatore-del-plasminogeno-di-tipo-urochinasico-supar-per-lindicazione-al-trattamento-con-anak/>

### 1.7 Orologi epigenetici (DNAm)
- **Quali:** PhenoAge, GrimAge/GrimAge2 (2ª gen.), **DunedinPACE** (3ª gen., "ritmo" di invecchiamento),
  **OMICmAge**, **SYMPHONYAge**, cloni PC-based (Higgins-Chen).
- **Affidabilità tecnica:** DunedinPACE fu costruito su 173 CpG selezionati per alta affidabilità test-retest
  (ICC 0,96-0,97 nel paper originale, eLife 2022) <https://elifesciences.org/articles/73420>.
  Le versioni **PC** degli orologi riducono la differenza tra repliche tecniche da ~9 anni a <1 anno.
- ⚠️ **Dato 2026 che cambia il quadro:** Sehgal et al., *Aging Cell* 2026;25(8):e70635 — su repliche tecniche
  DunedinPACE/GrimAge/PhenoAge/Horvath si collocano attorno a **ICC 0,7-0,8**, mentre SystemsAge e i PC-clocks
  superano 0,90; e soprattutto la **stabilità biologica a breve termine** di quasi tutti gli orologi è
  **ICC 0,4-0,7**, con cadute a "poor" dopo un pasto o uno stress acuto; «la riproducibilità tecnica non predice
  la stabilità biologica». L'aggiustamento per le frazioni immunitarie **riduce** l'affidabilità biologica,
  segno che la composizione cellulare porta segnale vero (ed è anche il principale confondente).
  <https://pmc.ncbi.nlm.nih.gov/articles/PMC13418614/>
- **Magnitudine attesa di un effetto reale:** in CALERIE (2 anni di restrizione calorica, n=220) l'effetto su
  DunedinPACE è stato **~2-3% di rallentamento, d di Cohen 0,2-0,3**, mentre PhenoAge e GrimAge non si muovevano.
  <https://www.nature.com/articles/s43587-022-00357-y> · <https://pmc.ncbi.nlm.nih.gov/articles/PMC10737863/>
  → **In n-of-1 a 8 settimane l'effetto atteso è ben dentro il rumore.** Usare gli orologi solo come contesto,
  mai come endpoint primario, e solo se si possono fare **campioni duplicati** (vedi §5.6).
- **Fornitori che raggiungono l'Italia / UE** (prezzi indicativi 2026):
  | Fornitore | Campione | Orologi | Prezzo | Note |
  |---|---|---|---|---|
  | TruDiagnostic TruAge Complete | sangue capillare su card (DBS) | OMICmAge, DunedinPACE, SYMPHONYAge, stima telomeri, composizione immunitaria | ~400-460 € (+100-130 € IVA/handling import US) | non spedisce più direttamente in UE/UK: canale ufficiale **Lola Health** (£337,50-375) <https://lolahealth.com/products/trudiagnostic-truage-test> |
  | Elysium Index | saliva | linea PhenoAge | ~280 € + import | <https://longevity-germany.com/en/guide/epigenetic-tests> |
  | myDNAge | sangue **o urina** | Horvath | ~280 € + import | unica opzione su urina |
  | epiAge / Muhdo | saliva | multi-clock DNAm | 180-220 € | kit UE, niente dogana |
  | GlycanAge (glicani IgG, **non** DNAm) | DBS | "GlycanAge" | **323 €** | laboratorio Genos, Zagabria (UE) <https://glycanage.com/price-and-plans> |
  | Hurdle/Chronomics | saliva | biological age | 🚩 prezzo/disponibilità IT non verificati 🚩 | canale Bayer DTC |
  | Tally Health | tampone buccale | TallyAge | 🚩 spedizione UE non verificata 🚩 | |
  Fonte tabella prezzi: <https://longevity-germany.com/en/guide/epigenetic-tests> (guida 2026, non listino ufficiale) 🚩
- **Alternativa "fai da te bene":** array **Illumina Infinium MethylationEPIC v2.0** presso un service EU
  (es. Diagenode <https://www.diagenode.com/en/p/infinium-methylation-epic-array-v2-service>), poi calcolo degli
  orologi con software open (DunedinPACE package, pyaging, ClockFoundation). Riferimento di prezzo pubblico
  disponibile solo US: **412 USD/campione** (University of Iowa Genomics)
  <https://humangenetics.medicine.uiowa.edu/genomics-division/microarray/microarrays-and-fees>. 🚩 prezzo EU da
  richiedere 🚩 — Questa via consente **duplicati tecnici e campioni appaiati processati sullo stesso chip**,
  che è l'unico modo serio di usare gli orologi in un n-of-1.

### 1.8 Orologi proteomici (Olink / SomaScan)
- Evidenza accademica solida: proteomic age clock su UK Biobank (2.897 proteine, 204 selezionate) e orologi
  **organo-specifici** (Wyss-Coray, *Nature Medicine* 2025) che predicono mortalità e malattia.
  <https://www.nature.com/articles/s41591-025-03798-1> · <https://olink.com/publication/proteomic-aging-clock-predicts-mortality-and-risk-of-common-age-related-diseases-in-diverse-populations>
- **Consumer:** **Vero Bioscience** (OrganAge™, tecnologia Stanford/Wyss-Coray) annuncia un test domiciliare
  >5.000 proteine con obiettivo **~200 USD a regime**; **Teal Omics** è ancora essenzialmente research-stage.
  <https://www.verobioscience.com/> · <https://insider.fitt.co/press-release/vero-combines-stanfords-proteomic-organ-and-cell-aging-technologies-to-build-a-new-clinical-and-consumer-tool-for-predictive-health/>
  🚩 **NON VERIFICATO:** disponibilità in Italia/UE, prezzo reale, ripetibilità test-retest. 🚩

### 1.9 Urina — parliamone onestamente
| Analita | Significato | Perché è debole |
|---|---|---|
| 8-oxo-dG / 8-OHdG | danno ossidativo al DNA | **Non è un marcatore di senescenza**: misura il turnover di riparazione ossidativa di tutto l'organismo. Forte variazione diurna (campioni notturni più variabili), dipendenza dal metodo di normalizzazione (creatinina vs volume): correlazione tra i due metodi r 0,73 ma variabilità intra-soggetto diversa. ELISA ≠ LC-MS/MS (ELISA sovrastima). <https://pmc.ncbi.nlm.nih.gov/articles/PMC12101107/> · <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7313038/> |
| 8-oxo-Gsn (RNA) | ossidazione RNA | Aumento monotono con l'età in coorti cinesi, proposto come "età fisiologica"; richiede UHPLC-MS/MS, non disponibile come routine. <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5835306/> |
| F2-isoprostani | perossidazione lipidica | Robusto come marcatore di stress ossidativo *sistemico*, ma richiede GC-MS/LC-MS; nessun legame diretto con carico senescente. |
| Metaboliti NAD (N-metilnicotinammide, 2-PY, 4-PY) | flusso NAD⁺ | Interpretazione ambigua, fortissima dipendenza da dieta/supplementi. |
| "SASP urinario" | — | **Non esiste** un pannello urinario SASP validato. |
**Conclusione:** l'urina va raccolta (24 h o primo mattino) solo se si ha accesso a LC-MS/MS presso il partner;
altrimenti **non merita budget**. È l'anello più debole di tutto il protocollo.

---

## 2. Tier 2 — kit e piattaforme per un laboratorio partner

### 2.1 ELISA singleplex (R&D Systems Quantikine e simili)
| Analita | Kit tipico | Note |
|---|---|---|
| GDF-15 | R&D **DGD150** (96 pozzetti, siero/plasma/urina, ~3,5 h) <https://www.rndsystems.com/products/human-gdf-15-quantikine-elisa-kit_dgd150> | il marcatore SASP con la miglior evidenza |
| Activin A | R&D DAC00B | 2° miglior predittore di età (Schafer 2020) |
| Osteopontina (OPN) | R&D DOST00 | pannello 7-SASP |
| PAI-1 / Serpin E1 | R&D DSE100 | ridotto dall'esercizio |
| TNF RI (TNFRSF1A) | R&D DRT100 | pannello 7-SASP |
| MMP-7 | R&D DMP700 | compendio 2026 |
| IL-6 hs | R&D HS600C (high-sensitivity) | indispensabile la versione hs |
**Prezzi:** i listini R&D/Fisher non sono pubblici senza login; l'ordine di grandezza per un kit Quantikine da
96 pozzetti è **~500-800 €** (≈ 40 campioni in doppio). 🚩 stima, non verificata a listino 🚩

### 2.2 Multiplex
- **Olink Target 96 Inflammation** (PEA, 92 proteine, 1 µL di campione, 88 campioni/piastra) —
  <https://olink.com/products/olink-target-96> · service provider certificati: TATAA Biocenter (EU, GLP),
  Psomagen, Discovery Life Sciences. 🚩 **Prezzo non pubblico**; ordine di grandezza tipicamente citato
  ~350-500 €/campione per un pannello, ma va chiesto preventivo e **il minimo d'ordine è di norma una piastra**
  (88 campioni) → poco adatto a n-of-1 salvo consorzio con altri partecipanti. 🚩
- **Luminex / MSD**: il formato usato in Hickson 2019 e St. Sauver 2023. Un pannello custom 10-20-plex costa
  tipicamente 800-1.500 € per piastra (96 pozzetti). 🚩 stima 🚩 — **Vantaggio decisivo per n-of-1: tutti i
  campioni (pre e post) si analizzano nella stessa piastra, azzerando la varianza inter-assay.**

### 2.3 Biologia molecolare / citometria
| Saggio | Materiale | Costo indicativo |
|---|---|---|
| p16/p21 RT-qPCR su CD3+ sortati | microbeads CD3 (MACS/EasySep), estrazione RNA, RT, TaqMan (p16, p21, cGAS + 2 housekeeping) | ~40-90 €/campione di consumabili 🚩 |
| SA-β-gal in citometria | CellEvent Senescence Green C10840 (50 test, **350 USD**) <https://www.thermofisher.com/order/catalog/product/C10840> o SPiDER-βGal | ~7 USD/test + anticorpi di superficie |
| Immunofenotipo senescenza T | CD3/CD4/CD8/CD45RA/CCR7/CD28/CD57/KLRG1 | ~15-30 €/campione di anticorpi 🚩 |
| Telomeri qPCR assoluti | ScienCell 8918, **~561 USD/kit** <https://www.fishersci.com/shop/products/telomeres-nucleotide-kit/NC1503693> | sconsigliato per 8 settimane |
| EPIC v2 methylation array | service EU (Diagenode) | ~400 USD/campione (rif. US) 🚩 |

---

## 3. Tier 1 — cosa si ordina davvero in un laboratorio privato italiano

### 3.1 Realtà del mercato italiano
- **Nessuna prescrizione necessaria** per gli esami di laboratorio pagati privatamente (es. tipizzazione
  linfocitaria: «prescrizione medica: non necessaria, digiuno 8 h»).
  <https://cup24.it/prestazione/58cfe5614e531/>
- **Le differenze di prezzo sono enormi** tra listini "tariffari regionali" e centri privati. Due riferimenti
  reali: listino Gruppo Pavanello (Veneto, PDF pubblico) vs comparatore cup24/cupsolidale per Roma.
  <https://www.unive.it/pag/fileadmin/user_upload/ateneo/lavora_con_noi/convenzioni/centri_medici/pavanello/Gruppo_Pavanello_Listino_laboratorio_privato.pdf>
  (🚩 il PDF non riporta una data: prezzi da confermare 🚩)
- **Struttura del nomenclatore:** l'immunofenotipo si tariffa **per marcatore** («MARKERS IMMUNOLOGICI
  LINFOCITARI, 14,40 € ciascuno, max 100,80 € per 7 marcatori») → è quindi possibile chiedere al laboratorio
  di aggiungere **CD28 e CD57** al pannello CD3/CD4/CD8/CD19/CD16-56, se il citometro ha i reagenti.

### 3.2 Tabella Tier 1 (ordinabile oggi in Italia)
| Esame | Cosa misura / relazione con senescenza | Evidenza | Campione & pre-analitica | Prezzo Italia (fonte) | Variabilità |
|---|---|---|---|---|---|
| **hs-CRP** | infiammazione sistemica; proxy grezzo di inflammaging | alta come predittore di rischio, **bassa** come marker di senescenza | siero, digiuno non necessario, **evitare infezioni/traumi 2 sett.** | PCR 4,20 € (Pavanello); hs-CRP in genere 5-15 € | **pessima**: CV totale mediano 0,44 (range 0,27-0,76), ICC 0,62 in meta-analisi <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0304961> |
| **IL-6 (hs)** | SASP core; correla con p16 nei T (r 0,27-0,33) | alta a livello di coorte | siero o plasma EDTA; **centrifugare entro 1-3 h**, aliquotare, −80 °C; ritmo circadiano (picco notturno, nadir ~08:00) <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0165799> | 17,35 € (Pavanello) · 101,10 € (AgapeLab FI) · **56-237 € a Roma** <https://cup24.it/c/roma/5d08e5fe76c41/> | CVI 21,5%, CVA 6,4%, II 0,85 (Aziz 2019) → RCV bidirezionale ≈ **62%** |
| **TNF-α** | SASP | media | siero, stessa pre-analitica | 40,00 € ("fattore necrosi tumorale", Pavanello); 33,60-153 € a Roma <https://www.cupsolidale.it/c/roma/5d08ef289fa07/> | CVI 12,7%, CVA 8,2% → RCV ≈ **42%** |
| **IL-1β, IL-8, IL-10** | SASP secondari | bassa (spesso sotto il limite di rilevabilità con metodi routinari) | come sopra | ~17-40 € cad. (analoghi IL-2/IL-6) | IL-8 CVI 51% → RCV ≈ **143%**; IL-1β CVI 31% → RCV ≈ **86%** (Aziz 2019) <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6744707/> |
| **GDF-15** | miglior singolo marcatore SASP/età | **la più alta** tra i marcatori circolanti | siero o plasma; stabile; evitare esercizio intenso 48 h prima | **da verificare**: Roche Elecsys GDF-15 è CE-IVD sul mercato italiano <https://diagnostics.roche.com/it/it/products/params/elecsys-gdf-15.html>, ma 🚩 non ho trovato alcun listino privato italiano che lo offra 🚩 → chiedere a Synlab/Lifebrain/CDI o farlo in ELISA dal partner | **ottima**: CVA 1,8%, CVI 7,6%, CVG 23,6%, II 0,35, **RCV +24,3% / −19,5%** (Sithiravel, *CCLM* 2021) <https://pmc.ncbi.nlm.nih.gov/articles/PMC8997700/>; Krintus 2019 CVI 6,3%, RCV 23% |
| **Fibrinogeno** | infiammazione/coagulazione | bassa | citrato | 2,30 € | moderata |
| **Ferritina** | infiammazione + riserve marziali | bassa | siero | 11,50 € | alta (acute phase) |
| **Omocisteina** | metabolismo 1-C, rischio CV | bassa | plasma EDTA **in ghiaccio, centrifuga rapida** (sale se il campione resta a T ambiente) | 10,05 € | moderata |
| **Emocromo + NLR** | rapporto neutrofili/linfociti = inflammaging a costo zero | media (predittore di mortalità) | EDTA | 4,10 € | CVI ~15-20% sui conteggi |
| **Tipizzazione linfocitaria (CD3/4/8/19/16-56)** ± **CD28, CD57** | immunosenescenza | media; **confusa dal CMV** | EDTA, analisi entro 24-48 h | 14,40 €/marcatore, 100,80 € per 7 (Pavanello); pannelli completi es. Eurofins Lamm <https://www.lammlab.it/analisi/pannello-linfocitario-completo> | moderata; richiedere **stesso laboratorio e stesso citometro** |
| **CMV IgG** | confondente obbligatorio da conoscere | — | siero, **una sola volta** | 9,70 € | — |
| **HbA1c / insulina / HOMA-IR** | metabolismo (HbA1c è nel protocollo NCT07168525) | media | HbA1c EDTA; insulina a digiuno 12 h | HbA1c 9,35 € · insulina 8,50 € | HbA1c CVI ~1,5-2% (ottima); insulina CVI ~20-30% |
| **Cistatina C** | funzione renale + marcatore SASP-adiacente (compendio 2026) | media | siero | 15,20 € | CVI ~5% |
| **IGF-1 (somatomedina C)** | asse GH/IGF, ipotesi mTOR | media | siero, mattino | 16,90 € | CVI ~10-15% |
| **β2-microglobulina** | turnover linfocitario, correlato di età | media | siero | 9,50 € | moderata |
| **NT-proBNP** | stress cardiaco, co-varia con GDF-15 | alta (cardio) | plasma | 12,55 € | CVI ~30-40% |
| **Pannello base**: glicemia, creatinina/eGFR, ALT/AST/GGT, albumina, lipidi, TSH, vitamina D, elettroforesi | contesto e sicurezza | — | — | 1,10-14,35 € cad. | — |
| **suPAR** | attivazione immunitaria cronica, mortalità | media-alta | plasma | 🚩 **non trovato in listini privati italiani**; disponibile in contesto ospedaliero/ricerca 🚩 | dati BV recenti su 20 soggetti sani, 8 settimane (Scand J Clin Lab Invest 2026) <https://www.tandfonline.com/doi/full/10.1080/00365513.2026.2713138> (🚩 valori numerici non estratti: paywall 🚩) |
| **Telomeri** | vedi §1.4 | bassa per 8 settimane | sangue | Life Length 399 € (EU); pacchetti IT ~300-500 € | inadeguata a rilevare 8 settimane |

**Marcatori che NON si trovano in routine in Italia** (→ Tier 2/3): Activin A, osteopontina, TNFR1, MMP-2/7/9,
PAI-1, CCL3, IL-15, RAGE, PARC/CCL18, p16 su T, SA-β-gal citometrico, γH2AX, cfDNA quantitativo.

---

## 4. Tier 3 — mail-in / omiche

| Test | Cosa dà | Prezzo | Caveat |
|---|---|---|---|
| TruAge Complete (via Lola Health, UE) | OMICmAge, DunedinPACE, SYMPHONYAge, telomeri stimati, **composizione immunitaria** | ~£337-375 / ~400-460 € (+import se US) | DBS su card; ICC biologica 0,4-0,7 (Sehgal 2026) → serve duplicato |
| GlycanAge | infiammazione glicomica IgG; risponde a interventi in 3-6 mesi | 323 € | complementare, non sostitutivo |
| epiAge / Muhdo | DNAm age | 180-220 € | validazione peer-review più debole 🚩 |
| myDNAge | Horvath (anche **urina**) | ~280 € | clock di 1ª gen., poco utile per interventi |
| EPIC v2 array presso service EU + clock open-source | tutto (PC-clocks, DunedinPACE, SenMayo se abbinato a RNA) | ~400 USD/campione (rif. US) 🚩 | **la sola via che consente duplicati tecnici e randomizzazione su chip** |
| Olink Target 96 Inflammation via service | 92 proteine incl. molti SASP | preventivo, minimo 1 piastra 🚩 | ideale se più partecipanti |
| Vero OrganAge (proteomico) | età d'organo | ~200 USD annunciati 🚩 | disponibilità UE non verificata |
| SapereX (p16 + rete immunitaria) | il marcatore più "senescenza-specifico" | n.d. 🚩 | solo cliniche US, registro IRB |

---

## 5. Disegno n-of-1: come non ingannarsi

### 5.1 Il concetto chiave: Reference Change Value (RCV)
Per un marcatore con variazione analitica CVA e biologica intra-individuale CVI:

> **RCV(95%, bidirezionale) = 1,96 × √2 × √(CVA² + CVI²) ≈ 2,77 × CVT**

Con **k campioni mediati prima** e **k dopo**, il termine √2 diventa √(2/k):

> **RCV_k = 1,96 × √(2/k) × CVT** → con k=3 il requisito si riduce del **42%**.

| Marcatore | CVA | CVI | CVT | RCV (1 vs 1) | RCV (media di 3 vs media di 3) | Fonte |
|---|---|---|---|---|---|---|
| **GDF-15** | 1,8% | 7,6% | 7,8% | **±21,6%** (paper: +24,3/−19,5) | **±12,5%** | Sithiravel, CCLM 2021 |
| GDF-15 (2° studio) | — | 6,3% | — | 23% | — | Krintus, CCLM 2019 <https://www.degruyterbrill.com/document/doi/10.1515/cclm-2018-0908/html> |
| **IL-6** | 6,4% | 21,5% | 22,4% | **±62%** | **±36%** | Aziz, BMC Immunol 2019 |
| **TNF-α** | 8,2% | 12,7% | 15,1% | **±42%** | **±24%** | idem |
| IL-1β | 4,0% | 30,9% | 31,2% | ±86% | ±50% | idem |
| IL-8 | 3,5% | 51,4% | 51,5% | ±143% | ±82% | idem |
| **hs-CRP** | ~5% | ~30-45% (CV totale mediano 0,44) | ~44% | **≈ ±120%** | **≈ ±70%** | Meta-analisi PLOS One 2024 |
⚠️ Il paper BMC Immunology riporta RCV più bassi (IL-6 33,6%, TNF-α 22,2%): probabilmente con una formula
monodirezionale/diversa. **Ho ricalcolato con la formula standard** e raccomando di usare i valori qui sopra
(più conservativi). 🚩 discrepanza segnalata 🚩

**Lettura operativa:** con un solo prelievo pre e uno post, **solo GDF-15 può mostrare un cambiamento
interpretabile** a fronte degli effetti attesi (10-30%). IL-6 e hs-CRP, da soli, **non sono utilizzabili**
in n-of-1 se non mediando più prelievi.

### 5.2 Numero di baseline
- **Minimo:** 2 prelievi di baseline a distanza di 7-14 giorni.
- **Raccomandato:** **3 baseline** (settimane −4, −2, 0) e **3 post** (settimane 8, 9, 10 oppure 8, 10, 12),
  tutti mediati. Questo dimezza quasi il RCV (§5.1) e permette di stimare empiricamente il *proprio* CVI.
- **Ideale (design ABA):** baseline ×3 → LFU 8 settimane → post ×3 → washout 8 settimane → re-test ×2.
  Un ritorno verso il basale dopo il washout è l'evidenza più forte ottenibile senza sham.

### 5.3 Standardizzazione pre-analitica (non negoziabile)
1. Stessa ora del giorno, **07:30-09:00**, digiuno 12 h, solo acqua (IL-6 ha un ritmo circadiano con nadir
   mattutino; GDF-15 risente del pasto meno, ma standardizzare comunque).
2. **Nessun esercizio intenso nelle 48 h precedenti**: dopo una maratona GDF-15 sale **4,2-4,5×** e torna al
   basale in 24-48 h <https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2020.550102/full>;
   anche 1 h al 67% VO₂max dà +34-64%.
3. **Nessuna infezione/vaccinazione/trauma/chirurgia nelle 4 settimane precedenti**; annotare allergie stagionali,
   parodontiti, cistiti.
4. Alcol 0 nelle 48 h; sonno ≥6 h; stesso stato di idratazione; misurare peso e pressione a ogni prelievo.
5. **Provetta e processazione identiche ogni volta**: siero *oppure* plasma EDTA — mai alternare.
   Centrifugare entro 1-3 h, aliquotare in provette da 0,5 mL, **congelare a −80 °C**, evitare cicli di
   scongelamento. Il ritardo di centrifugazione altera le citochine già a 3 h e in modo opposto tra siero e plasma
   <https://pmc.ncbi.nlm.nih.gov/articles/PMC12369616/>.
6. **Batch analysis:** conservare tutti i campioni e analizzarli **nella stessa seduta/piastra** alla fine dello
   studio. Questo elimina la varianza inter-assay ed è l'unico modo per far scendere CVA vicino al valore del kit.
   (Questo vale per il partner di ricerca; per il laboratorio privato di routine, chiedere almeno **lo stesso
   laboratorio e lo stesso metodo** a ogni prelievo e annotare il metodo sul referto.)
7. Registrare farmaci e integratori; congelare le abitudini (dieta, allenamento) per tutta la durata.

### 5.4 Timing rispetto alle sedute LFU: effetti acuti vs cronici
- **Segnale acuto atteso in senso opposto:** Gwak et al., *Aging Cell* 2025 mostrano che LIPUS **aumenta
  selettivamente la secrezione di SASP** dalle cellule senescenti (via ROS → p38-NF-κB), reclutando monociti/
  macrofagi che poi fagocitano le cellule senescenti. <https://onlinelibrary.wiley.com/doi/10.1111/acel.14486>
  → Un prelievo poche ore dopo una seduta potrebbe mostrare **SASP in aumento** anche se l'effetto cronico
  è di riduzione.
- **Rischio p16 falsamente elevato:** l'attivazione T Ca²⁺-dipendente induce p16 (§1.1); LFU agisce via Ca²⁺/Piezo1.
- **Regola:** prelievo cronico **≥48-72 h dopo l'ultima seduta** (idealmente 72 h) e **sempre allo stesso
  intervallo** dalla seduta precedente.
- **Opzionale e interessante:** una sotto-serie "acuta" (pre-seduta, +2 h, +24 h su una singola seduta) per
  descrivere la risposta acuta di IL-6/GDF-15 — ma etichettata esplicitamente come esplorativa.
- Il bagno caldo di per sé (vasca, 45 min) ha effetti emodinamici e sull'IL-6: **il controllo sham
  "vasca senza ultrasuoni" del trial è esattamente per questo**. In n-of-1, il periodo di washout (§5.2)
  e/o sessioni "vasca senza LFU" alternate ne sono il surrogato più vicino.

### 5.5 Batteria funzionale minima (allineata a NCT07168525)
| Test | Attrezzatura | MCID/soglia di cambiamento reale |
|---|---|---|
| **Forza di estensione del ginocchio** (primario nel trial) | dinamometro isocinetico (Biodex) — in n-of-1 sostituibile con dinamometro portatile/hand-held o 1RM leg extension | 🚩 nessun MCID consolidato per HHD in sani; usare la media di 3 prove e SEM misurato su di sé 🚩 |
| **SPPB** | cronometro, sedia, spazio 4 m | piccolo **0,5 punti**, sostanziale **1,0 punto** (Perera 2006, JAGS) |
| **Velocità del cammino 4 m** | cronometro | piccolo **0,05 m/s**, sostanziale **0,10 m/s** (id.) |
| **6MWT** | corridoio ≥20 m, cronometro | piccolo **20 m**, sostanziale **50 m** (id.) |
| **TUG** | sedia + cono 3 m | usare media di 3 prove; variazione >~1 s indicativa 🚩 |
| **30-s chair stand** | sedia | complemento a basso costo |
| **Handgrip** | Jamar / Jamar Plus | ICC 0,98 negli anziani; **SEM 1,64 kg, MDC ~3,55 kg (9%)** in uno studio con Jamar Plus <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0270132> |
| **VO₂ proxy** | Cooper 12 min, o step test, o HRV/HR di recupero a 1 min | segnale robusto e a costo zero se standardizzato |
Fonte MCID: Perera, Mody, Woodman, Studenski, *JAGS* 2006 — gait speed piccolo 0,04-0,06 m/s e sostanziale
0,08-0,14 m/s; SPPB 0,27-0,55 e 0,99-1,34 punti; 6MWD 19-22 m e 47-49 m.
<https://pubmed.ncbi.nlm.nih.gov/16696738/>
**Regola pratica:** ogni test funzionale va ripetuto **3 volte per sessione** e in **3 sessioni di baseline**,
così da stimare il proprio SEM e derivare MDC = 1,96·√2·SEM.

### 5.6 Se si usano gli orologi epigenetici
- Prelevare **2 campioni indipendenti per punto temporale** (duplicato biologico) e, se si usa l'array,
  chiedere che i campioni pre/post siano **sullo stesso chip in posizioni randomizzate**.
- Riportare sempre **anche la composizione immunitaria stimata** (le frazioni cellulari sono il principale
  driver dei cambiamenti a breve termine).
- Interpretare l'esito solo come "coerente/non coerente" e mai come effetto quantificato: a 8 settimane la
  variazione attesa è << rumore (CALERIE: 2-3% su 2 anni).

### 5.7 Analisi
- Predefinire **endpoint primario unico** (proposta: **GDF-15 plasmatico**, media di 3 pre vs media di 3 post)
  e dichiarare tutto il resto esplorativo, per evitare il multiple-testing mascherato.
- Riportare ogni marcatore come **Δ% con il proprio RCV** accanto. "Δ −18% con RCV ±12,5%" è un risultato;
  "IL-6 −25% con RCV ±62%" non lo è.
- Pubblicare dati grezzi + codice (coerente con lo spirito open source del progetto): questo è ciò che rende
  utile un n-of-1 anche quando è statisticamente debole — l'aggregazione di più n-of-1 identici.

---

## 6. Pannelli raccomandati

### 6.1 Pannello minimo (il "non fare meno di così")
Per ciascun punto temporale (3 pre + 3 post; ≥48-72 h da ogni seduta, 07:30-09:00, digiuno):
1. **Emocromo con formula** (→ NLR) — 4-10 €
2. **hs-CRP** — 5-15 €
3. **IL-6 ad alta sensibilità** — 17-100 €
4. **GDF-15** ← **endpoint primario** (routine se il laboratorio lo esegue, altrimenti congelare plasma e farlo
   in ELISA batch dal partner) — 30-80 € 🚩
5. **HbA1c, glicemia, insulina (HOMA-IR)** — ~25 €
6. **Creatinina/eGFR + cistatina C, ALT/AST/GGT, albumina, lipidi** — ~40 €
7. **Aliquote extra di plasma/siero congelate a −80 °C** ("biobanca personale") — costo ~0, valore altissimo
8. Una tantum a baseline: **CMV IgG**, elettroforesi sieroproteica, TSH, vitamina D, ferritina, omocisteina
9. **Batteria funzionale** §5.5 ×3 sessioni pre e ×3 post — costo: un dinamometro (~50-150 €) e un cronometro

**Costo indicativo totale minimo:** ~150-400 € per punto temporale in centro privato italiano ×6 =
**900-2.400 €**, più il dinamometro. (Con listino tipo Pavanello si sta nella fascia bassa; a Roma nella alta.)

### 6.2 Pannello "fatto bene" (con laboratorio partner)
Tutto il minimo, più:
- **SASP multiplex** (Luminex/MSD custom o Olink Target 96 Inflammation) con almeno:
  GDF15, Activin A, TNFR1, OPN, FAS, CCL3, IL-15, IL-6, MMP-2, MMP-7, MMP-9, PAI-1, RAGE, CCL18, TIMP1, IGFBP2
  — **tutti i campioni nella stessa piastra**.
- **p16 + p21 + cGAS RT-qPCR su CD3+ sortati** (10-15 mL EDTA, processati entro 2-4 h).
- **Citometria**: CD3/CD4/CD8/CD45RA/CCR7/CD28/CD57/KLRG1 + **SA-β-gal (CellEvent/SPiDER)** su PBMC freschi.
- **RNA-seq su PBMC o CD3+** con scoring **SenMayo** (replica il "RNA-seq" del protocollo NCT07168525).
- **DNAm EPIC v2** in duplicato, stesso chip → DunedinPACE, PC-PhenoAge/PC-GrimAge, SYMPHONYAge, frazioni immunitarie.
- **cfDNA / cf-mtDNA** quantitativo (esplorativo, pre-analitica rigidissima).
- **DEXA** (massa magra/grassa) a baseline e a 8 settimane, come nel trial — in Italia ~60-120 € privato. 🚩
- Opzionale urina 24 h → 8-oxo-dG/8-oxo-Gsn e F2-isoprostani **in LC-MS/MS**, solo se il partner li ha.

### 6.3 Timeline di campionamento consigliata
```
Sett. −4   Prelievo B1 + funzionale F1 + (una tantum: CMV, DEXA, telomeri, orologio epigenetico #1)
Sett. −2   Prelievo B2 + funzionale F2
Sett.  0   Prelievo B3 + funzionale F3            → inizio LFU (45 min, 3×/sett.)
Sett.  4   (opzionale) prelievo intermedio M1, ≥48-72 h dall'ultima seduta
Sett.  8   FINE LFU → Prelievo P1 (72 h dopo l'ultima seduta) + funzionale F4 + DEXA + orologio #2
Sett.  9   Prelievo P2
Sett. 10   Prelievo P3 + funzionale F5
Sett. 16   (washout) Prelievo W1 + funzionale F6  → verifica del ritorno al basale
Opzionale: serie acuta su 1 singola seduta (pre, +2 h, +24 h) in settimana 5
```

---

## 7. Monitoraggio di sicurezza oncologica — con onestà

**Premessa non aggirabile:** un intervento che **riporta in proliferazione cellule senescenti** rimuove, in
linea di principio, una barriera anti-tumorale (la senescenza oncogene-indotta). Il paper Kureel 2025 riporta
**nessun tumore in topi seguiti >300 giorni** e nessuna apoptosi indotta, ma:
- **nessun dato umano esiste**;
- **nessun esame del sangue può escludere un tumore.** I marcatori tumorali (CEA, CA125, CA19-9, PSA) **non sono
  raccomandati come screening in persone asintomatiche**: bassissimo valore predittivo positivo, falsi positivi
  che portano a imaging e procedure invasive con complicanze fino al 15%, nessun beneficio di mortalità
  dimostrato. <https://journal.waocp.org/article_92301.html>
- **GDF-15 è esso stesso elevato in molti tumori**: un suo *aumento* inatteso non è "invecchiamento",
  va interpretato clinicamente.

### Cosa è ragionevole fare (e perché)
| Misura | Razionale | Frequenza |
|---|---|---|
| **Aderire ai programmi di screening organizzati italiani** (mammografico 50-69, cervicale 25-64, colon-retto SOF 50-69) | è l'unico screening con beneficio di mortalità dimostrato <https://www.osservatorionazionalescreening.it/content/la-diffusione-degli-screening-oncologici-italia-nel-2023> | secondo programma regionale |
| **Emocromo con formula + striscio se anomalo** | intercetta citopenie/leucocitosi; economico | ogni prelievo |
| **LDH, elettroforesi sieroproteica (± immunofissazione se picco)** | linfoproliferativi, MGUS/mieloma | baseline, 8 sett., 6 mesi |
| **Funzione epatica e renale, calcio, fosfatasi alcalina** | organo-tossicità e segnali indiretti | ogni prelievo |
| **Peso, sintomi B (febbre, sudorazioni notturne, calo ponderale >5%), linfoadenopatie** | il sintomo batte il biomarcatore | diario settimanale |
| **Visita dermatologica / mappatura nei** | la pelle è esposta a qualsiasi effetto proliferativo ed è ispezionabile | baseline e 12 mesi |
| **PSA (uomini, età-appropriato) con decisione condivisa** | non è screening universale, ma se già in programma va mantenuto | come da medico |
| **Follow-up lungo** | gli eventi oncologici non compaiono in 8 settimane: prevedere controlli a 6 e 12 mesi | 6 e 12 mesi |
**Da NON fare:** pannelli di marcatori tumorali "a tappeto" come rassicurazione; test MCED (Galleri) non è
disponibile/approvato in Italia e la sua submission FDA è attesa nel 2026
<https://www.galleri.com/> 🚩 disponibilità IT non verificata, presumibilmente assente 🚩.
**Regola di stop:** qualunque anomalia persistente (citopenia, picco monoclonale, LDH in salita, calo ponderale,
linfonodo persistente) → **interrompere e consultare un medico**, non "rimisurare tra un mese".

---

## 8. Sintesi delle criticità e degli elementi non verificati

### Criticità metodologiche principali
1. **Nessun marcatore ematico di senescenza è specifico**; il migliore singolo (GDF-15) è anche il più
   aspecifico clinicamente (cardio, rene, cancro, esercizio, mitocondri).
2. **Gli effetti attesi (10-30%) sono dello stesso ordine del rumore** per quasi tutti i marcatori infiammatori
   → senza baseline ripetuti si producono solo falsi positivi.
3. **LFU può avere effetti acuti opposti a quelli cronici** (SASP ↑ acuto, Gwak 2025) e può indurre p16 nei T
   via Ca²⁺ → il timing dei prelievi è parte del risultato.
4. **Gli orologi epigenetici sono biologicamente instabili a breve termine** (ICC 0,4-0,7, Sehgal 2026):
   inadatti come endpoint a 8 settimane.
5. **Il bagno caldo è un intervento a sé**: senza sham, il washout è l'unico controllo interno.

### Elementi 🚩 NON VERIFICATI 🚩 da chiudere prima di partire
- Disponibilità e prezzo del **GDF-15** in un laboratorio privato italiano (contattare Synlab, Lifebrain/Cerba,
  CDI, Bianalisi, Unilabs chiedendo esplicitamente "Elecsys GDF-15 Roche").
- Disponibilità di **suPAR** per privati in Italia (probabilmente no).
- **SapereX**: accettazione di campioni dall'estero, prezzo, stabilità RNA nel transito.
- Prezzi EU reali di **Olink Target 96**, **Luminex custom**, **EPIC v2** (servono preventivi).
- Prezzi/metodo dei provider telomerici italiani (NutriHealth Genomics, GEK Lab): pagine non accessibili al fetch.
- **Data del listino Gruppo Pavanello** (PDF senza data) e applicabilità fuori Veneto.
- Disponibilità in UE di **Tally Health**, **Hurdle/Chronomics**, **Vero OrganAge**.
- Valori numerici di variazione biologica di **suPAR** (articolo Scand J Clin Lab Invest 2026 dietro paywall).
- **MCID della forza di estensione del ginocchio** con dinamometro portatile in adulti sani.
- Stime di costo dei kit ELISA R&D (~500-800 €) e dei consumabili p16 RT-qPCR (~40-90 €/campione): **stime**,
  non listini.

---

## 9. Fonti principali

**Intervento e trial**
- Kureel S, Maroto R, … Rasmussen BB, Sheetz MP. *Aging Cell* 2025, doi:10.1111/acel.70008 — <https://pmc.ncbi.nlm.nih.gov/articles/PMC12151899/>
- NCT07168525 "Ultrasound for Healthy Aging" — <https://clinicaltrials.gov/study/NCT07168525>
- Gwak H et al. *Aging Cell* 2025, LIPUS → SASP ↑ e clearance macrofagica — <https://onlinelibrary.wiley.com/doi/10.1111/acel.14486>

**Biomarcatori di senescenza**
- Schafer MJ et al. *JCI Insight* 2020;5(12):e133668 — <https://insight.jci.org/articles/view/133668>
- Olinger B, Basisty N. *Ageing Res Rev* 2026, compendio dei biomarcatori circolanti — <https://pmc.ncbi.nlm.nih.gov/articles/PMC13408882/>
- St. Sauver J et al. *Aging Cell* 2023, SASP e mortalità (n=1923) — <https://onlinelibrary.wiley.com/doi/10.1111/acel.14006>
- Liu Y, … Sharpless NE. *Aging Cell* 2009, p16 nei T CD3+ — <https://pmc.ncbi.nlm.nih.gov/articles/PMC2752333/>
- Englund DA et al. *Aging Cell* 2021, esercizio ↓ p16/p21/SASP — <https://onlinelibrary.wiley.com/doi/10.1111/acel.13415>
- Lepola, Guan, Burd. *Innov Aging* 2025, p16 indotto da attivazione T Ca²⁺-dipendente — <https://pmc.ncbi.nlm.nih.gov/articles/PMC12761409/>
- Martínez-Zamudio RI et al. *Aging Cell* 2021, SA-βGal citometrico nei CD8⁺ — <https://pmc.ncbi.nlm.nih.gov/articles/PMC8135084/>
- Hickson LJ et al. *EBioMedicine* 2019 (D+Q, DKD) — <https://www.thelancet.com/article/S2352-3964(19)30591-2/fulltext>
- Justice JN et al. *EBioMedicine* 2019;40:554-563 (D+Q, IPF) — <https://www.thelancet.com/journals/ebiom/article/PIIS2352-3964(18)30629-7/pdf>
- Saul D et al. SenMayo, *Nat Commun* 2022 — <https://pubmed.ncbi.nlm.nih.gov/35974106/>
- Teo YV et al. cfDNA e invecchiamento, *Aging Cell* 2019 — <https://onlinelibrary.wiley.com/doi/full/10.1111/acel.12890>

**Orologi e variabilità**
- Belsky DW et al. DunedinPACE, *eLife* 2022 — <https://elifesciences.org/articles/73420>
- Sehgal R et al. *Aging Cell* 2026;25(8):e70635, affidabilità biologica vs tecnica — <https://pmc.ncbi.nlm.nih.gov/articles/PMC13418614/>
- Waziry R et al. CALERIE / DunedinPACE, *Nature Aging* 2023 — <https://www.nature.com/articles/s43587-022-00357-y>
- Nettle D et al. errore di misura nel qPCR telomerico, *PLOS One* 2019 — <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0216118>
- Sithiravel C et al. variazione biologica di GDF-15, *CCLM* 2021 — <https://pmc.ncbi.nlm.nih.gov/articles/PMC8997700/>
- Krintus M et al. *CCLM* 2019, GDF-15 — <https://www.degruyterbrill.com/document/doi/10.1515/cclm-2018-0908/html>
- Aziz N et al. *BMC Immunology* 2019, variazione biologica di IL-6/TNF-α/IL-8/IL-1β — <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6744707/>
- Meta-analisi variabilità CRP/hs-CRP, *PLOS One* 2024 — <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0304961>
- Meta-analisi ritmo diurno IL-6, *PLOS One* 2016 — <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0165799>
- Ritardo di centrifugazione e citochine, 2025 — <https://pmc.ncbi.nlm.nih.gov/articles/PMC12369616/>
- GDF-15 dopo maratona, *Front Physiol* 2020 — <https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2020.550102/full>

**Funzione fisica**
- Perera S et al. *JAGS* 2006, MCID di gait speed/SPPB/6MWD — <https://pubmed.ncbi.nlm.nih.gov/16696738/>
- Affidabilità dinamometria di presa negli anziani, *PLOS One* 2022 — <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0270132>

**Italia / costi**
- Listino laboratorio privato Gruppo Pavanello (PDF) — <https://www.unive.it/pag/fileadmin/user_upload/ateneo/lavora_con_noi/convenzioni/centri_medici/pavanello/Gruppo_Pavanello_Listino_laboratorio_privato.pdf>
- Comparatore cup24/cupsolidale: IL-6 Roma — <https://cup24.it/c/roma/5d08e5fe76c41/> · TNF-α Roma — <https://www.cupsolidale.it/c/roma/5d08ef289fa07/>
- AgapeLab Firenze, IL-6 101,10 € — <https://www.agapelab.it/analiti/interleukin-6-il6>
- Eurofins Lamm, pannello linfocitario completo — <https://www.lammlab.it/analisi/pannello-linfocitario-completo>
- Synlab Italia, elenco prestazioni (PDF; fetch bloccato, da consultare manualmente) — <https://synlab.it/images/amministrazione-trasparente/synlab-italia/Allegato%201%20Carta%20dei%20Servizi%20Laboratorio%20SYNLAB%20Italia_Elenco%20prestazioni.pdf>
- Roche Elecsys GDF-15 (IT) — <https://diagnostics.roche.com/it/it/products/params/elecsys-gdf-15.html>
- Life Length (telomeri, 399 € in Europa) — <https://lifelength.com/> · <https://telomas.com/pages/partners-life-length>
- GlycanAge prezzi — <https://glycanage.com/price-and-plans>
- Guida prezzi test epigenetici 2026 — <https://longevity-germany.com/en/guide/epigenetic-tests>
- Lola Health (canale UE/UK TruDiagnostic) — <https://lolahealth.com/products/trudiagnostic-truage-test>
- Osservatorio Nazionale Screening — <https://www.osservatorionazionalescreening.it/content/la-diffusione-degli-screening-oncologici-italia-nel-2023>
- Uso inappropriato dei marcatori tumorali negli asintomatici — <https://journal.waocp.org/article_92301.html>

**Kit**
- Thermo CellEvent Senescence Green C10840 — <https://www.thermofisher.com/order/catalog/product/C10840>
- R&D Quantikine GDF-15 DGD150 — <https://www.rndsystems.com/products/human-gdf-15-quantikine-elisa-kit_dgd150>
- ScienCell 8918 telomeri — <https://www.fishersci.com/shop/products/telomeres-nucleotide-kit/NC1503693>
- Olink Target 96 — <https://olink.com/products/olink-target-96> · Diagenode EPIC v2 — <https://www.diagenode.com/en/p/infinium-methylation-epic-array-v2-service>
