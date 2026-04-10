# SISTEMA UNICO DI PROGETTAZIONE INDUSTRIALE AVANZATA

**Acronimo:** SUPIA  
**Codice:** GQAOA-UTA-SUPIA-001  
**Versione:** 1.0  
**Autorità:** GQAOA .INC — GAIA QUANTUM AMPEL OPT-INS ARCHITECTURE  
**Architetto:** Amedeo Pelliccia  
**Data:** 2026-04-11  
**Stato:** Baseline attiva  
**Lingue operative:** IT (primaria) · EN · ES · DE · FR

---

> *"Aggiungere valore, espandere il potenziale."*  
> V(t) = dΦ / dW_r · σ(t)  
> dove σ(t) è il coefficiente amplificatore dello sforzo solitario.

---

## INDICE

0. [Scopo e Campo di Applicazione](#0-scopo-e-campo-di-applicazione)
1. [Filosofia Progettuale](#1-filosofia-progettuale)
2. [Architettura del Sistema](#2-architettura-del-sistema)
3. [I 10 Domini (000–999)](#3-i-10-domini-000999)
4. [La Griglia OPT-INS a 6 Assi](#4-la-griglia-opt-ins-a-6-assi)
5. [Grammatica Identificativa Universale](#5-grammatica-identificativa-universale)
6. [Spina Dorsale — SSOT + PUB](#6-spina-dorsale--ssot--pub)
7. [Ciclo di Vita dell'Artefatto (LC01–LC14)](#7-ciclo-di-vita-dellartefatto-lc01lc14)
8. [Orchestrazione dell'Incertezza (KNOT → KNU)](#8-orchestrazione-dellincertezza-knot--knu)
9. [Tokenomics — Teknia Token (TT v3.14)](#9-tokenomics--teknia-token-tt-v314)
10. [Disegno Tecnico — Norme, Proiezioni, Tolleranze](#10-disegno-tecnico--norme-proiezioni-tolleranze)
11. [Pubblicazione Tecnica — S1000D + IETP](#11-pubblicazione-tecnica--s1000d--ietp)
12. [Progettazione Digitale — Gemello, Simulazione, V&V](#12-progettazione-digitale--gemello-simulazione-vv)
13. [Registro Completo dei 1000 Capitoli](#13-registro-completo-dei-1000-capitoli)
14. [Istanziazione per Programma](#14-istanziazione-per-programma)
15. [Pila di Governance](#15-pila-di-governance)
16. [Allineamento Normativo](#16-allineamento-normativo)
17. [Appendici](#17-appendici)

---

## 0. SCOPO E CAMPO DI APPLICAZIONE

### 0.1 Scopo

Il SUPIA stabilisce **un unico sistema integrato** per la progettazione, documentazione, verifica, pubblicazione e gestione del ciclo di vita di artefatti ingegneristici complessi — dall'aeronautica allo spazio, dalla difesa all'automazione, dalla città aerea alla computazione quantistica.

Il SUPIA non è un catalogo né un manuale di classificazione. È un **sistema operativo di progettazione** in cui ogni atto — definire un requisito, tracciare un disegno, registrare un'incertezza, distribuire un incentivo — avviene entro la medesima struttura, con la medesima grammatica, con la medesima tracciabilità.

### 0.2 Campo di applicazione

| Dimensione | Copertura |
|------------|-----------|
| Settori | Aerospazio, spazio, difesa, gemelli digitali, energia, materiali avanzati, automazione terrestre, mobilità aerea urbana, sicurezza cibernetica, computazione quantistica |
| Fasi del ciclo di vita | Concetto → Definizione → Sviluppo → Produzione → Operazione → Manutenzione → Ritiro / Circolarità |
| Tipi di artefatto | Requisiti, specifiche di progetto, disegni tecnici, modelli analitici, procedure di prova, evidenze di sicurezza, moduli di dati S1000D, grafici ICN, passaporti digitali DPP |
| Programmi attivi | AMPEL360 Q100, GAIA-SPACE-LAUNCHER, SPACET Q10 |
| Programmi futuri | Qualsiasi programma che adotti il manifesto UTA |

### 0.3 Documenti correlati

| Codice | Titolo |
|--------|--------|
| GQAOA-UTA-SUDDI-001 | Sistema Universale di Documentazione e Disegno Tecnico Industriale |
| GQAOA-OPT-INS-STD-1.1 | OPT-INS Framework Standard |
| GQAOA-AMPEL360-MRS-1.1-001 | Mission Requirements Specification |
| GQAOA-ASIT-NIB-SPEC-001 | NeuronBit Information Specification |
| GQAOA-MUSIC-MCC-SPEC | Musical Cryptographic Communication Stack |

---

## 1. FILOSOFIA PROGETTUALE

### 1.1 I sette principi

| # | Principio | Enunciazione | Conseguenza operativa |
|---|-----------|-------------|----------------------|
| P1 | **Unica Sorgente di Verità** | Ogni artefatto ha un unico luogo autoritativo | Nessuna copia non governata; ogni modifica è tracciata |
| P2 | **Pubblicazione Derivata** | Ogni deliverable è generato dalla sorgente, mai scritto indipendentemente | La CSDB è sempre a valle della SSOT |
| P3 | **Incertezza Esplicita** | Ciò che non si sa è dichiarato con la stessa disciplina di ciò che si sa | Ogni nodo aperto è un KNOT; ogni artefatto prodotto è un KNU |
| P4 | **Tracciabilità Bidirezionale** | Ogni artefatto è collegato verso l'alto (a un'incertezza e un requisito) e verso il basso (a un'evidenza) | Nessun artefatto orfano; nessun requisito senza copertura |
| P5 | **Incentivo Proporzionale all'Impatto** | Chi riduce incertezza è ricompensato in modo misurabile | Formula TT: w_i = α·Ê_i + (1-α)·Î_i |
| P6 | **Scala Universale** | Lo stesso schema si applica a un bullone e a un concetto di agenza quantistica | Grammatica UTA-DDD-SS-ss-nn identica per 1000 capitoli |
| P7 | **Determinismo Quantico in Definendum** | L'atto di definire un artefatto ne fissa lo stato — documentare è progettare | La frontiera tra progetto e documentazione è dissolta |

### 1.2 Il modello concettuale

```
                    ┌─────────────────────────┐
                    │     PROGETTAZIONE        │
                    │                         │
                    │   Definire = Fissare    │
                    │   Documentare = Creare  │
                    │   Misurare = Conoscere  │
                    │   Incentivare = Allineare│
                    └────────────┬────────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              │                  │                  │
         ┌────▼────┐       ┌────▼────┐        ┌────▼────┐
         │  SSOT   │       │  KNOT   │        │   TT    │
         │ Verità  │◄─────►│Incertezz│◄──────►│Incentivo│
         │ unica   │       │esplicita│        │allineato│
         └────┬────┘       └────┬────┘        └────┬────┘
              │                  │                  │
              └──────────────────┼──────────────────┘
                                 │
                          ┌──────▼──────┐
                          │    PUB      │
                          │ Deliverable │
                          │  derivato   │
                          └─────────────┘
```

### 1.3 Cosa rende SUPIA diverso

| Sistema convenzionale | SUPIA |
|----------------------|-------|
| Tassonomia e baseline sono sistemi separati | La tassonomia *è* la baseline |
| Documentazione descrive ciò che è stato progettato | Documentazione *è* progettazione |
| Incertezze gestite informalmente | Ogni incertezza ha un ID, un proprietario, una scadenza, un premio |
| Incentivi scollegati dal processo tecnico | Ogni riduzione di incertezza genera ricompensa calcolabile |
| Pubblicazione tecnica come deliverable a sé | PUB è generata automaticamente dalla SSOT |
| 1 settore per framework | 10 domini, 1000 capitoli, un'unica grammatica |

---

## 2. ARCHITETTURA DEL SISTEMA

### 2.1 Vista d'insieme a sei livelli

```
┌─────────────────────────────────────────────────────────────────┐
│  LIVELLO 6 — REGISTRO (LEDGER)                                  │
│  TT tokenomics · catena hash SHA-256 · AWARDS_TT.csv            │
│  finance/ledger.json                                             │
├─────────────────────────────────────────────────────────────────┤
│  LIVELLO 5 — PUBBLICAZIONE (PUB)                                │
│  S1000D CSDB · BREX · DM/PM/DML · IETP · EXPORT (PDF/HTML)     │
├─────────────────────────────────────────────────────────────────┤
│  LIVELLO 4 — VERIFICA E VALIDAZIONE                             │
│  LC06 Verifica · LC07 Validazione                                │
│  DO-178C · DO-254 · DO-160 · ECSS-E-ST-10 · MIL-STD-882        │
├─────────────────────────────────────────────────────────────────┤
│  LIVELLO 3 — EVIDENZE INGEGNERISTICHE                           │
│  LC02 Requisiti · LC03 Sicurezza · LC04 Progetto                │
│  LC05 Analisi · LC08 Configurazione · LC09 Produzione           │
│  LC10 Operazioni · LC11 Manutenzione · LC12 Cura del Cliente   │
│  LC13 Formazione · LC14 Ritiro / Circolarità                    │
├─────────────────────────────────────────────────────────────────┤
│  LIVELLO 2 — ORCHESTRAZIONE DELL'INCERTEZZA                    │
│  LC01: KNOTS.csv → KNU_PLAN.csv → RACI.csv → TIMELINE.csv      │
│  TOKENOMICS_TT.yaml → AWARDS_TT.csv                            │
├─────────────────────────────────────────────────────────────────┤
│  LIVELLO 1 — TASSONOMIA ESEGUIBILE                              │
│  UTA 000–999 · OPT-INS 6 assi · manifesto per programma        │
│  PROGRAMME_MANIFEST.yaml                                        │
├─────────────────────────────────────────────────────────────────┤
│  LIVELLO 0 — ONTOLOGIA                                          │
│  NeuronBit · MonKBit · MonKeyBeast · bitbot · moonbyte          │
│  MonQuid · MonTeraby                                             │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 Flusso di informazione

```
Incertezza          Evidenza            Deliverable         Incentivo
    │                   │                    │                   │
    ▼                   ▼                    ▼                   ▼
 KNOT ──────► KNU ──────► SSOT/LCxx ──────► PUB/CSDB ──────► TT
 (LC01)      (artefatto)  (registrazione)   (pubblicazione)   (ricompensa)
    │                                            │
    └────────── tracciabilità bidirezionale ──────┘
```

---

## 3. I 10 DOMINI (000–999)

### 3.0 Mappa topologica

```
 ╔══════════════════════════════════════════════════════════════════════╗
 ║  SPAZIO UNIVERSALE DI PROGETTAZIONE — 1000 CAPITOLI                 ║
 ╠══════════════════════════════════════════════════════════════════════╣
 ║                                                                     ║
 ║   G1 ✈️  ATA    000–099   Tecnologia Aerospaziale                   ║
 ║   G2 🚀  STA    100–199   Tecnologia Spaziale                      ║
 ║   G3 🛡️  DTTA   200–299   Tecnologia della Difesa                  ║
 ║   G4 🔮  DTCEC  300–399   Gemelli Digitali / Cloud / Edge          ║
 ║   G5 ⚡  EPTA   400–499   Energia e Propulsione                    ║
 ║   G6 🧬  AMTA   500–599   Materiali / Bio / Nano                   ║
 ║   G7 ⚙️  OGATA  600–699   Automazione Terrestre                    ║
 ║   G8 🏙️  ACV    700–799   Vivibilità delle Città Aeree             ║
 ║   G9 🔒  CYB    800–899   Architettura di Sicurezza Cibernetica    ║
 ║   G10 🌐 QCSAA  900–999   Computazione Quantistica / Agenza        ║
 ║                                                                     ║
 ║   SCHELETRO IDENTICO PER OGNI CAPITOLO:                            ║
 ║   SSOT (LC01–LC14) + PUB (CSDB/EXPORT/IETP) + KNOT/KNU + TT      ║
 ║                                                                     ║
 ╚══════════════════════════════════════════════════════════════════════╝
```

### 3.1–3.10 Registri per decennio

*(Registro completo: vedi Sezione 13 e documento allegato GQAOA-UTA-SUDDI-001)*

| Dominio | Decenni | Capitoli | Asse primario |
|---------|:-------:|:--------:|:-------------:|
| G1 ATA | 10 | 100 | O · P · T · S |
| G2 STA | 10 | 100 | S · I |
| G3 DTTA | 10 | 100 | T · N · S |
| G4 DTCEC | 10 | 100 | T · I · N · S |
| G5 EPTA | 10 | 100 | T |
| G6 AMTA | 10 | 100 | T · P |
| G7 OGATA | 10 | 100 | I · P · O |
| G8 ACV | 10 | 100 | T · I · O |
| G9 CYB | 10 | 100 | N · O · T |
| G10 QCSAA | 10 | 100 | T · N · S · O |
| **Totale** | **100** | **1.000** | |

---

## 4. LA GRIGLIA OPT-INS A 6 ASSI

| Asse | Sigla | Funzione | Capitoli tipici |
|------|-------|----------|-----------------|
| **O** | Organizations | Governance, politiche, navigabilità, etica, certificazione | 000–005, 290, 690, 720, 750, 760, 790, 800–809, 980–989 |
| **P** | Programs | Movimentazione, servizi, logistica, fabbricazione | 006–012, 240–249, 570–579, 640–649 |
| **T** | Technologies | Tutti i sistemi di bordo e cross-dominio | 020–089, 095, 097, 200–239, 260–269, 280–289, 300–329, 350–399, 400–499, 500–569, 580–589, 680–689, 700–709, 730–749, 770–789, 840–849, 900–919, 960–979, 990–999 |
| **I** | Infrastructures | Supporto a terra, infrastrutture, cloud, catena H₂ | 003-I, 008-I, 010-I, 012-I, 085-I, 180–189, 330–339, 600–639, 650–679, 710–719 |
| **N** | Neural Networks | Tracciabilità, DPP, registro, sicurezza cibernetica, blockchain | 096, 098, 250–259, 360–379, 810–899, 920–939 |
| **S** | SIM-TEST / Space | Simulazione, campagne di prova, spazio-specifici, sensori/sim quantistica | 090–099, 100–179, 190–199, 270–279, 340–349, 940–959 |

### Proprietà dell'appartenenza

- Un capitolo può appartenere a **più assi** contemporaneamente (es. 085 → T + I)
- L'asse **primario** determina il posizionamento fisico nella struttura del repository
- Gli assi **secondari** generano viste filtrate (query, dashboard, report)
- L'appartenenza è dichiarata nel file `CHAPTER_MANIFEST.yaml` di ogni capitolo

---

## 5. GRAMMATICA IDENTIFICATIVA UNIVERSALE

### 5.1 Codice di nodo

```
UTA-DDD-SS-ss-nn
 │   │   │  │  │
 │   │   │  │  └── Sotto-soggetto   00–99
 │   │   │  └───── Soggetto          00–99
 │   │   └──────── Sezione           00–99
 │   └──────────── Capitolo          000–999
 └──────────────── Prefisso sistema
```

**Sezioni riservate per ogni capitolo:**

| Sezione | Contenuto |
|---------|-----------|
| `xx-00` | Generale |
| `xx-10` … `xx-80` | Contenuto tecnico specifico del capitolo |
| `xx-90` | Tabelle, schemi, indice, glossario |
| `xx-91` … `xx-99` | Riservato all'operatore / programma |

### 5.2 Codici derivati

| Tipo | Formato | Esempio |
|------|---------|---------|
| Nodo | `UTA-DDD-SS-ss-nn` | `UTA-028-10-00-00` |
| KNOT | `KNOT-UTA-DDD-SS-ss-nnn` | `KNOT-UTA-028-10-00-001` |
| KNU | `KNU-UTA-DDD-SS-ss-TTT-nnn` | `KNU-UTA-028-10-00-REQ-001` |
| DM (S1000D) | `DMC-GQAOA-A-DDD-SS-ss-nn-AAA-BBB-C` | `DMC-GQAOA-A-028-10-00-00-00A-040A-D` |
| ICN | `ICN-GQAOA-A-DDD-SS-ss-nn-nnnnn-A-ccc-nn` | `ICN-GQAOA-A-028-10-00-00-00001-A-001-01` |
| TT Transazione | `TX-YYYY-nnnn` | `TX-2026-0142` |

### 5.3 Tipi KNU

| Codice | Tipo | Descrizione |
|--------|------|-------------|
| `REQ` | Requisito | Specifica di requisito (sistema, funzionale, interfaccia, prestazione) |
| `ICD` | Interface Control | Documento di controllo interfaccia |
| `ANA` | Analisi | Modello analitico (FEA, CFD, termico, prestazioni) |
| `TEST` | Prova | Procedura di prova, rapporto di prova, evidenza |
| `SAF` | Sicurezza | Analisi di sicurezza, registro pericoli, FMEA, FTA |
| `CM` | Configurazione | Baseline, effectivity, controllo modifiche |
| `PUB` | Pubblicazione | Data Module, Publication Module, ICN, deliverable |
| `DWG` | Disegno | Disegno tecnico (2D/3D), modello CAD, tavola |
| `SIM` | Simulazione | Modello di simulazione, scenario, risultati |
| `DPP` | Passaporto Digitale | Record DPP, SBOM, hash di ancoraggio |

---

## 6. SPINA DORSALE — SSOT + PUB

### 6.1 Struttura canonica del nodo foglia

Ogni sotto-soggetto nell'intero spazio UTA 000–999 porta questa struttura identica:

```
UTA-DDD-SS-ss-nn/
├── README.md                              ← Descrizione del nodo
├── CHAPTER_MANIFEST.yaml                  ← Assi OPT-INS, programmi attivi, stato
│
├── SSOT/                                  ← SISTEMA DI REGISTRAZIONE
│   ├── LC01_PROBLEM_STATEMENT/            ← ORCHESTRAZIONE INCERTEZZA
│   │   ├── KNOTS.csv                      ← Registro incertezze
│   │   ├── KNU_PLAN.csv                   ← Piano KNU attese
│   │   ├── TIMELINE.csv                   ← Pietre miliari
│   │   ├── RACI.csv                       ← Matrice responsabilità
│   │   ├── TOKENOMICS_TT.yaml            ← Pool di ricompensa
│   │   └── AWARDS_TT.csv                 ← Distribuzione effettiva
│   │
│   ├── LC02_SYSTEM_REQUIREMENTS/          ← Requisiti e tracciabilità
│   ├── LC03_SAFETY_RELIABILITY/           ← Analisi sicurezza, FMEA, FTA, registro pericoli
│   ├── LC04_DESIGN_DEFINITION/            ← Specifiche di progetto, ICD, architettura
│   │   ├── DRAWINGS/                      ← Disegni tecnici (DWG, DXF, STEP, PDF)
│   │   ├── MODELS_3D/                     ← Modelli CAD (STEP, IGES, JT, CATIA)
│   │   ├── SCHEMATICS/                    ← Schemi funzionali, P&ID, wiring diagrams
│   │   └── SPECS/                         ← Specifiche tecniche, data sheets
│   │
│   ├── LC05_ANALYSIS_MODELS/              ← FEA, CFD, termico, prestazioni, aerodinamica
│   ├── LC06_VERIFICATION/                 ← Procedure e evidenze di verifica
│   ├── LC07_VALIDATION/                   ← Integrazione e validazione
│   ├── LC08_CONFIGURATION/                ← Baseline, effectivity, controllo modifiche
│   ├── LC09_PRODUCTION/                   ← Specifiche di fabbricazione, attrezzaggio
│   ├── LC10_OPERATIONS/                   ← Fonti documentazione operativa
│   ├── LC11_MAINTENANCE/                  ← Fonti programma di manutenzione
│   ├── LC12_CUSTOMER_CARE/                ← Supporto tecnico, servizi post-consegna
│   ├── LC13_TRAINING/                     ← Fonti contenuti formativi
│   └── LC14_RETIREMENT_CIRCULARITY/       ← Fine vita, riciclaggio, DPP
│
└── PUB/                                   ← SUPERFICIE DI CONSEGNA
    └── AMM/                               ← Aircraft/System Maintenance Manual (o equivalente)
        ├── CSDB/                          ← Common Source DataBase S1000D
        │   ├── DM/                        ← Data Modules (XML)
        │   ├── PM/                        ← Publication Modules
        │   ├── DML/                       ← Data Module Lists
        │   ├── BREX/                      ← Business Rules Exchange
        │   ├── ICN/                       ← Grafici (SVG preferenziale)
        │   ├── COMMON/                    ← Primitivi riutilizzabili (avvisi, cautele, note)
        │   └── APPLICABILITY/             ← ACT / PCT / CCT
        ├── EXPORT/                        ← Render PDF / HTML
        └── IETP/                          ← Viewer interattivo, packaging, indice
```

### 6.2 Regola d'oro

| Se l'artefatto è… | Collocalo in… |
|--------------------|---------------|
| Evidenza ingegneristica autoritativa | `SSOT/LCxx/` |
| Disegno tecnico o modello CAD | `SSOT/LC04_DESIGN_DEFINITION/DRAWINGS/` o `MODELS_3D/` |
| Pubblicabile o consegnabile | `PUB/` |
| Incertezza o piano di risoluzione | `SSOT/LC01_PROBLEM_STATEMENT/` |
| Registro di ricompensa | `SSOT/LC01_PROBLEM_STATEMENT/AWARDS_TT.csv` |

---

## 7. CICLO DI VITA DELL'ARTEFATTO (LC01–LC14)

### 7.1 Le 14 fasi

| Fase | Codice | Titolo | Contenuto tipico |
|------|--------|--------|------------------|
| 1 | LC01 | Dichiarazione del Problema | KNOT, KNU plan, RACI, timeline, tokenomics |
| 2 | LC02 | Requisiti di Sistema | Requisiti funzionali, prestazionali, di interfaccia; matrice di tracciabilità |
| 3 | LC03 | Sicurezza e Affidabilità | FMEA, FTA, registro pericoli, HOB/NHOB, analisi di rischio |
| 4 | LC04 | Definizione del Progetto | Specifiche, ICD, architettura, **disegni tecnici**, modelli 3D, schemi |
| 5 | LC05 | Modelli di Analisi | FEA, CFD, termico, aerodinamico, prestazioni, trade studies |
| 6 | LC06 | Verifica | Procedure di prova, rapporti di prova, evidenze, compliance |
| 7 | LC07 | Validazione | Integrazione, validazione operativa, accettazione |
| 8 | LC08 | Configurazione | Baseline, effectivity, status delle modifiche |
| 9 | LC09 | Produzione | Specifiche di fabbricazione, processi, attrezzaggio, qualità |
| 10 | LC10 | Operazioni | Manuali operativi, procedure di volo/missione |
| 11 | LC11 | Manutenzione | Programma di manutenzione, MSG-3, condition monitoring |
| 12 | LC12 | Cura del Cliente | Supporto tecnico, AOG, bollettini, campo |
| 13 | LC13 | Formazione | Contenuti didattici, curricula, simulatori |
| 14 | LC14 | Ritiro e Circolarità | Fine vita, riciclaggio, DPP, SBOM, smaltimento |

### 7.2 Diagramma a V del SUPIA

```
LC02 Requisiti ──────────────────────────────────── LC07 Validazione
  │                                                       ▲
  ▼                                                       │
LC04 Progetto ────────────────────────────────── LC06 Verifica
  │                                                       ▲
  ▼                                                       │
LC05 Analisi ──────────────────────────────────── LC06 Verifica
  │                                                       ▲
  ▼                                                       │
LC09 Produzione ─────────► LC10 Operazioni ──► LC11 Manutenzione
                                                       │
                                              LC14 Ritiro/Circolarità

       ─── LC01 (Incertezza) attraversa tutte le fasi ───
       ─── LC03 (Sicurezza) attraversa tutte le fasi ───
       ─── LC08 (Configurazione) attraversa tutte le fasi ───
       ─── PUB (S1000D) generata a ogni gate ───
       ─── TT (Ricompensa) distribuita alla chiusura KNOT ───
```

---

## 8. ORCHESTRAZIONE DELL'INCERTEZZA (KNOT → KNU)

### 8.1 Ciclo di vita di un KNOT

```
1. IDENTIFICAZIONE    →  Incertezza registrata in KNOTS.csv (Residuo = 100)
2. PIANIFICAZIONE     →  KNU attese definite in KNU_PLAN.csv
                         Pietre miliari fissate in TIMELINE.csv
                         Pool TT allocato in TOKENOMICS_TT.yaml
3. ESECUZIONE         →  Artefatti KNU prodotti in LC02–LC14 e PUB/CSDB
                         Sforzo e impatto registrati per ogni KNU
4. CHIUSURA           →  Tutti i KNU completati, collegamenti risolti, BREX superato
                         Residuo ridotto al target (es. 100 → ≤ 10)
                         Ricompense TT distribuite: w_i = α·Ê_i + (1-α)·Î_i
                         Premi registrati in AWARDS_TT.csv + finance/ledger.json
```

### 8.2 File LC01

| File | Formato | Contenuto |
|------|---------|-----------|
| `KNOTS.csv` | CSV | Registro incertezze: ID, titolo, statement, ambito, stato, proprietario, stakeholder, residuo, target, dipendenze, scadenza |
| `KNU_PLAN.csv` | CSV | Piano KNU: ID, KNOT padre, tipo, classe artefatto, posizione attesa, criteri accettazione, metodo verifica, proprietario, scadenza, stato, sforzo previsto |
| `TIMELINE.csv` | CSV | Pietre miliari: ID, KNOT, nome, data, criteri ingresso/uscita, stato |
| `RACI.csv` | CSV | Matrice responsabilità: KNOT, attività, R, A, C, I |
| `TOKENOMICS_TT.yaml` | YAML | Pool di ricompensa: KNOT, pool TT, criteri eleggibilità, formula allocazione, parametri |
| `AWARDS_TT.csv` | CSV | Registro distribuzione effettiva: timestamp, KNOT, KNU, proprietario, sforzo, impatto, peso, token, TX ID |

### 8.3 Criteri di chiusura

Un KNOT è **CHIUSO** quando:

1. ✅ Tutti i KNU pianificati raggiungono stato `COMPLETO` o `ACCETTATO`
2. ✅ Il residuo scende al o sotto il target (es. 100 → ≤ 10)
3. ✅ Tutti gli artefatti PUB superano la validazione BREX
4. ✅ Tutti i collegamenti di tracciabilità risolvono (nessun riferimento pendente)
5. ✅ Firme acquisite nel pacchetto evidenze
6. ✅ Ricompense TT distribuite e registrate

---

## 9. TOKENOMICS — TEKNIA TOKEN (TT v3.14)

### 9.1 Parametri fondamentali

| Parametro | Valore |
|-----------|--------|
| Simbolo | TT |
| Unità | 1 TT = 360 deg |
| Offerta di genesi | 2.000.000.000 TT |
| Struttura commissioni | π-tier: 0,314% / 0,99% / 3,14% (trasferimenti); 0,5% (ricompense) |

### 9.2 Allocazione per dominio

| Dominio | Pool TT | Quota |
|---------|--------:|------:|
| G1 ATA | 400.000.000 | 20,0% |
| G2 STA | 300.000.000 | 15,0% |
| G3 DTTA | 100.000.000 | 5,0% |
| G4 DTCEC | 200.000.000 | 10,0% |
| G5 EPTA | 200.000.000 | 10,0% |
| G6 AMTA | 150.000.000 | 7,5% |
| G7 OGATA | 100.000.000 | 5,0% |
| G8 ACV | 150.000.000 | 7,5% |
| G9 CYB | 200.000.000 | 10,0% |
| G10 QCSAA | 200.000.000 | 10,0% |
| **Totale** | **2.000.000.000** | **100%** |

### 9.3 Formula di distribuzione

```
w_i = α · Ê_i + (1 - α) · Î_i
T_i = P_k · w_i
```

| Simbolo | Significato | Default |
|---------|-------------|---------|
| P_k | Pool TT per il KNOT k | definito in TOKENOMICS_TT.yaml |
| α | Peso dello sforzo | 0,30 |
| Ê_i | Sforzo normalizzato: E_i / Σ E_i | — |
| Î_i | Impatto normalizzato: I_i / Σ I_i | — |
| I_i | Impatto effettivo: ΔR_k,i + λ · S_i | — |
| ΔR_k,i | Riduzione residuo primario del KNU i sul KNOT k | — |
| S_i | Spillover: Σ(a_k→j · ΔR_j,i) per KNOT adiacenti | — |
| λ | Moltiplicatore spillover | 0,50 |

---

## 10. DISEGNO TECNICO — NORME, PROIEZIONI, TOLLERANZE

### 10.1 Norme di riferimento

| Norma | Ambito |
|-------|--------|
| ISO 128 | Principi generali di rappresentazione |
| ISO 129-1 | Quotatura — principi generali |
| ISO 1101 | Tolleranze geometriche (GD&T) |
| ISO 2768 | Tolleranze generali |
| ISO 5457 | Formati e presentazione dei fogli |
| ISO 7200 | Cartiglio (riquadro delle iscrizioni) |
| ISO 8015 | Principio di indipendenza |
| ISO 10110 | Disegno di elementi ottici |
| ISO 13715 | Spigoli — indicazione di stato |
| ISO 16792 | Documentazione tecnica di prodotto — Dati di definizione digitale |
| ASME Y14.5 | Dimensionamento e tolleranze (alternativa US) |
| ASME Y14.41 | Definizione di prodotto digitale |
| ASD-STAN prEN 9100 | Gestione qualità aerospaziale |

### 10.2 Sistema di proiezione

| Metodo | Standard | Uso nel SUPIA |
|--------|----------|---------------|
| **Primo diedro** (Metodo E) | ISO 128-30 | Primario per tutti i domini |
| **Terzo diedro** (Metodo A) | ASME Y14.3 | Ammesso per programmi US/FAA |
| Il metodo deve essere indicato nel cartiglio con il simbolo ISO appropriato | | |

### 10.3 Formati del foglio

| Formato | Dimensioni (mm) | Uso |
|---------|-----------------|-----|
| A0 | 841 × 1189 | Assemblaggi complessi, planimetrie |
| A1 | 594 × 841 | Assemblaggi, schemi di sistema |
| A2 | 420 × 594 | Sotto-assemblaggi |
| A3 | 297 × 420 | Componenti, dettagli |
| A4 | 210 × 297 | Schede tecniche, elenchi parti |

### 10.4 Cartiglio SUPIA

```
┌──────────────────────────────────────────────────────────────────┐
│                          CARTIGLIO SUPIA                         │
├────────────────────┬─────────────────────────────────────────────┤
│ TITOLO             │ [Titolo del disegno]                        │
├────────────────────┼─────────────────────────────────────────────┤
│ CODICE UTA         │ UTA-DDD-SS-ss-nn                            │
│ CODICE DISEGNO     │ DWG-GQAOA-DDD-SS-ss-nn-nnn                 │
│ FOGLIO             │ n di N                                      │
├────────────────────┼─────────────────────────────────────────────┤
│ PROGRAMMA          │ [AMPEL360 Q100 / GAIA / SPACET Q10]        │
│ DOMINIO            │ [G1–G10]                                    │
│ ASSE OPT-INS       │ [O/P/T/I/N/S]                              │
├────────────────────┼─────────────────────────────────────────────┤
│ SCALA              │ [1:1 / 1:5 / come indicato]                │
│ PROIEZIONE         │ [⊕ Primo diedro / ⊗ Terzo diedro]          │
│ UNITÀ              │ [mm / m]                                    │
│ TOLLERANZA GEN.    │ [ISO 2768-mK]                               │
├────────────────────┼─────────────────────────────────────────────┤
│ MATERIALE          │ [Designazione ISO / nome commerciale]       │
│ TRATTAMENTO SUP.   │ [Codice trattamento]                        │
│ MASSA              │ [kg]                                        │
├────────────────────┼─────────────────────────────────────────────┤
│ KNOT DI ORIGINE    │ [KNOT-UTA-DDD-SS-ss-nnn]                   │
│ KNU COLLEGATO      │ [KNU-UTA-DDD-SS-ss-DWG-nnn]                │
├────────────────────┼─────────────────────────────────────────────┤
│ REDATTO            │ [Nome]           [Data]                     │
│ VERIFICATO         │ [Nome]           [Data]                     │
│ APPROVATO          │ [Nome]           [Data]                     │
├────────────────────┼─────────────────────────────────────────────┤
│ REVISIONE          │ [Rev]  [Data]  [Descrizione]  [Autorità]   │
│ CLASSIFICAZIONE    │ [APERTO / RISERVATO / CONFIDENZIALE]        │
│ .YieldedAML        │ [sì/no — provenienza AI dichiarata]        │
└────────────────────┴─────────────────────────────────────────────┘
```

### 10.5 Tolleranze geometriche (GD&T) — sintesi

| Simbolo | Tipo | Caratteristica |
|---------|------|----------------|
| ⊥ | Orientamento | Perpendicolarità |
| ‖ | Orientamento | Parallelismo |
| ∠ | Orientamento | Angolarità |
| ○ | Forma | Circolarità |
| ⌭ | Forma | Cilindricità |
| ⏥ | Forma | Planarità |
| ⏤ | Forma | Rettilineità |
| ⊚ | Posizione | Concentricità / Coassialità |
| ⌖ | Posizione | Posizione |
| ◎ | Posizione | Simmetria |
| ↗ | Runout | Oscillazione circolare |
| ↗↗ | Runout | Oscillazione totale |
| ⌓ | Profilo | Profilo di una linea |
| ⌔ | Profilo | Profilo di una superficie |

### 10.6 Formati digitali ammessi

| Formato | Tipo | Uso |
|---------|------|-----|
| STEP AP242 | 3D | Formato aperto primario per modelli e PMI |
| JT | 3D | Visualizzazione leggera, digital mock-up |
| CATIA V5/V6 | 3D | Formato nativo per programmi Airbus |
| NX | 3D | Formato nativo per programmi alternativi |
| DXF/DWG | 2D | Disegni legacy e interfacce |
| PDF/A | 2D | Tavole archiviate per certificazione |
| SVG | 2D | Grafici per ICN (S1000D) |
| glTF/GLB | 3D | Visualizzazione web e IETP |

### 10.7 Gestione revisioni disegni

| Rev | Significato |
|-----|-------------|
| — (trattino) | Emissione iniziale |
| A, B, C… | Revisioni pre-rilascio (sviluppo) |
| 01, 02, 03… | Revisioni post-rilascio (produzione) |
| NC01, NC02… | Revisioni di non-conformità |

Ogni revisione deve essere accompagnata da:
- Data
- Descrizione della modifica
- Zona del disegno modificata (nuvola di revisione)
- Autorità che approva la modifica
- Riferimento al KNOT e/o ordine di modifica (ECO)

---

## 11. PUBBLICAZIONE TECNICA — S1000D + IETP

### 11.1 Architettura CSDB

| Componente | Funzione |
|------------|----------|
| **DM** (Data Module) | Modulo atomico di contenuto: descrittivo, procedurale, isolamento guasti, IPD |
| **PM** (Publication Module) | Struttura che assembla DM in deliverable |
| **DML** (Data Module List) | Lista controllata di DM con stato e applicabilità |
| **BREX** (Business Rules Exchange) | Regole di validazione e conformità |
| **ICN** (Information Control Number) | Grafici (SVG preferenziale) referenziati dai DM |
| **APPLICABILITY** | ACT/PCT/CCT per filtraggio prodotto/condizione |
| **COMMON** | Primitivi riutilizzabili: avvisi, cautele, note |

### 11.2 IETP (Interactive Electronic Technical Publication)

L'IETP è il "runtime" software che:
- Consuma insiemi PM/DM dalla CSDB
- Applica le regole di applicabilità (ACT/PCT/CCT)
- Fornisce navigazione interattiva, ricerca, filtraggio
- È pacchettizzato e versionato in `PUB/<PUB_ID>/IETP/`

### 11.3 Flusso SSOT → PUB

```
SSOT/LC04 (disegni, specifiche)
    │
    ▼
Authoring S1000D (XML)
    │
    ▼
CSDB/DM/ (moduli dati validati)
    │
    ├──► BREX validation (CI/CD)
    │
    ▼
CSDB/PM/ (struttura pubblicazione)
    │
    ├──► EXPORT/ (PDF/HTML renderizzati)
    │
    └──► IETP/ (packaging viewer interattivo)
```

---

## 12. PROGETTAZIONE DIGITALE — GEMELLO, SIMULAZIONE, V&V

### 12.1 Gemello digitale nel contesto SUPIA

Il gemello digitale non è un sistema separato ma una **vista computazionale** sulla SSOT:

```
SSOT/LC04 (geometria, materiali, ICD)
    +
SSOT/LC05 (modelli analitici)
    +
Dati operativi in tempo reale
    =
GEMELLO DIGITALE
    │
    ├── Previsione (prognostica)
    ├── Ottimizzazione (prescrittiva)
    └── Certificazione (evidenza virtuale)
```

### 12.2 Livelli di simulazione

| Livello | Acronimo | Descrizione | Capitolo UTA di riferimento |
|---------|----------|-------------|----------------------------|
| 1 | SIL | Software-in-the-Loop | S12-10 |
| 2 | MIL | Model-in-the-Loop | S11-50 |
| 3 | PIL | Processor-in-the-Loop | S12-30 |
| 4 | HIL | Hardware-in-the-Loop | S12-20 |
| 5 | Iron Bird | Integrazione completa a terra | S12-40 |
| 6 | FTB | Flying Test Bed | S22-10 |

### 12.3 Catena V&V

```
Requisito (LC02)
    │
    ▼
Progetto (LC04) ◄──── Analisi (LC05)
    │                      │
    ▼                      ▼
Produzione (LC09) ──► Prova a terra (S21) ──► Prova in volo (S22)
    │                      │                      │
    ▼                      ▼                      ▼
Verifica (LC06) ◄────────────────────────────────┘
    │
    ▼
Validazione (LC07)
    │
    ▼
Certificazione (S23)
```

---

## 13. REGISTRO COMPLETO DEI 1000 CAPITOLI

*(Registro esaustivo nel documento allegato [UTA-DOMAINS.md](./UTA-DOMAINS.md))*

**Sintesi:**

| Dominio | Codice | Range | Capitoli | Decenni |
|---------|--------|-------|:--------:|:-------:|
| Tecnologia Aerospaziale | ATA | 000–099 | 100 | 10 |
| Tecnologia Spaziale | STA | 100–199 | 100 | 10 |
| Tecnologia della Difesa | DTTA | 200–299 | 100 | 10 |
| Gemelli Digitali / Cloud / Edge | DTCEC | 300–399 | 100 | 10 |
| Energia e Propulsione | EPTA | 400–499 | 100 | 10 |
| Materiali / Bio / Nano | AMTA | 500–599 | 100 | 10 |
| Automazione Terrestre | OGATA | 600–699 | 100 | 10 |
| Vivibilità delle Città Aeree | ACV | 700–799 | 100 | 10 |
| Sicurezza Cibernetica | CYB | 800–899 | 100 | 10 |
| Computazione Quantistica / Agenza | QCSAA | 900–999 | 100 | 10 |
| **TOTALE** | | **000–999** | **1.000** | **100** |

---

## 14. ISTANZIAZIONE PER PROGRAMMA

### 14.1 Manifesto di programma

Ogni programma dichiara i propri capitoli attivi in un `PROGRAMME_MANIFEST.yaml`:

```yaml
programme:
  id: "AMPEL360-Q100"
  name: "AMPEL360 Q100 BWB Idrogeno-Ibrido"
  eis_target: "2040"
  type: "aircraft"
  certification_basis: "EASA CS-25 + SC per H₂"

active_domains:
  G1_ATA:   [000-089, 095-098]
  G4_DTCEC: [300-309, 320-329, 340-349]
  G5_EPTA:  [450-469]
  G6_AMTA:  [500-509, 570-579, 590-599]
  G9_CYB:   [800-809, 870-879]

opt_ins_axes:
  O: true
  P: true
  T: true
  I: true
  N: true
  S: [S1, S2]

tt_pool_allocated: 400000000
```

### 14.2 Programmi attivi

| Programma | Tipo | Capitoli attivi | Domini | Assi S |
|-----------|------|:---------------:|:------:|:------:|
| AMPEL360 Q100 | Aeromobile BWB ~100 pax | ~150 | G1, G4, G5, G6, G9 | S1, S2 |
| GAIA-SPACE-LAUNCHER | Lanciatore spaziale | ~250 | G1, G2, G4, G5, G6, G9, G10 | S1, S2, S3 |
| SPACET Q10 | Veicolo spaziale ~10 pax | ~200 | G1, G2, G4, G5, G9, G10 | S1, S2, S3 (parziale) |

---

## 15. PILA DI GOVERNANCE

### 15.1 Organi

| Organo | Responsabilità |
|--------|---------------|
| **Configuration Control Board (CCB)** | Approva modifiche alla baseline SSOT |
| **Publication Review Board (PRB)** | Approva rilascio di deliverable PUB |
| **KNOT Review Panel (KRP)** | Approva chiusura KNOT e distribuzione TT |
| **Safety Review Board (SRB)** | Approva artefatti LC03 e classificazioni HOB/NHOB |
| **Certification Liaison (CL)** | Interfaccia con autorità di certificazione (EASA/FAA/ESA) |

### 15.2 Gate di programma

| Gate | Nome | Criteri chiave |
|------|------|----------------|
| G0 | Concept Gate | Problemi dichiarati (LC01), requisiti di missione bozza |
| G1 | Requirements Gate | LC02 completo, LC03 iniziale, KNOT critici identificati |
| G2 | Design Gate | LC04 baseline, disegni preliminari rilasciati |
| G3 | Analysis Gate | LC05 completato, trade studies chiusi |
| G4 | Verification Gate | LC06 piano completo, prime evidenze di prova |
| G5 | Qualification Gate | LC06/LC07 completi, tutti i KNOT critici chiusi |
| G6 | Certification Gate | Pacchetto certificazione consegnato, TDC/STC |
| G7 | Entry Into Service | LC10/LC11 completi, IETP rilasciato, CAOS attivo |
| G8 | Maturity Gate | Feedback operativo integrato, configurazione stabile |
| G9 | End-of-Life Gate | LC14 attivato, DPP completato, circolarità pianificata |

---

## 16. ALLINEAMENTO NORMATIVO

| Norma | Ambito di applicazione nel SUPIA |
|-------|----------------------------------|
| **ATA iSpec 2200** | Struttura capitoli/sezioni G1 |
| **S1000D Issue 5.0/6.0** | PUB/CSDB su tutti i 10 domini |
| **ISO 128 / 129 / 1101** | Rappresentazione e tolleranze nel disegno tecnico |
| **ISO 5457 / 7200** | Formati foglio e cartiglio |
| **ISO 2768** | Tolleranze generali |
| **ISO 16792** | Documentazione di prodotto digitale |
| **ASME Y14.5 / Y14.41** | GD&T e definizione digitale (alternativa US) |
| **EASA CS-25 / FAA Part 25** | Aeronavigabilità |
| **DO-178C** | Assicurazione software in sistemi avionici |
| **DO-254** | Assicurazione hardware |
| **DO-160** | Qualifica ambientale |
| **ECSS-M-ST-10** | Gestione di progetto spaziale |
| **ECSS-E-ST-10** | Ingegneria dei sistemi spaziali |
| **ECSS-Q-ST-80** | Assicurazione software spaziale |
| **NASA STD 8739.8** | Assicurazione software NASA |
| **MIL-STD-882** | Sicurezza dei sistemi (difesa) |
| **MIL-STD-881** | Struttura di scomposizione del lavoro (WBS) difesa |
| **ISO 27001 / 27005** | Gestione sicurezza informazioni |
| **ISO 15926** | Dati industriali — standard di integrazione |
| **IEEE 7010** | IA etica e benessere |
| **EN 9100** | Gestione qualità aerospaziale |
| **ASD-STAN prEN 4512** | Scambio dati tecnici nell'industria aerospaziale |

---

## 17. APPENDICI

### Appendice A — Glossario dei Termini e degli Acronimi

#### A.1 Acronimi

| Acronimo | Espansione | Definizione |
|----------|-----------|-------------|
| **ACT** | Applicability Cross-reference Table | Tabella S1000D che associa condizioni di applicabilità a identificativi di prodotto |
| **ACV** | Aerial City Viability | Dominio G8 UTA — mobilità aerea urbana, vertipuertos, UAM |
| **AGV** | Automated Guided Vehicle | Veicolo a guida automatica per logistica industriale |
| **ALICE** | — | Sistema fisico nel modello di tracciabilità GQAOA (1° livello della catena) |
| **AML** | Algorithmic Machine Learning | Apprendimento automatico algoritmico; dichiarato nel campo `.YieldedAML` |
| **AMM** | Aircraft Maintenance Manual | Manuale di manutenzione dell'aeromobile (o del sistema) |
| **AMTA** | Advanced Materials Technology Architecture | Dominio G6 UTA — materiali avanzati, bio, nano |
| **AOG** | Aircraft On Ground | Stato di un aeromobile fermo per indisponibilità |
| **APU** | Auxiliary Power Unit | Unità di potenza ausiliaria |
| **ATA** | Air Transport Association | Associazione del trasporto aereo; dominio G1 UTA |
| **BOB DT** | BOB Digital Twin | Gemello digitale strutturale (2° livello della catena di tracciabilità) |
| **BOOST** | Bayesian-Optimized Output for Semantic Transformation | Motore di trasformazione semantica bayesiano (5° livello della catena) |
| **BREX** | Business Rules Exchange | Regole di validazione S1000D che definiscono la conformità per un progetto |
| **BWB** | Blended Wing Body | Configurazione aerodinamica con fusoliera integrata nell'ala |
| **C4ISR** | Command, Control, Communications, Computers, Intelligence, Surveillance, Reconnaissance | Sistema integrato di comando e controllo militare |
| **CAD** | Computer-Aided Design | Progettazione assistita dal calcolatore |
| **CAOS** | Continuous Airworthiness and Operational Support | Supporto continuo alla navigabilità e alle operazioni |
| **CCB** | Configuration Control Board | Comitato di controllo della configurazione |
| **CCT** | Condition Cross-reference Table | Tabella S1000D che associa condizioni operative a codici |
| **CFD** | Computational Fluid Dynamics | Fluidodinamica computazionale |
| **CHARLIE-T** | — | Agente digitale contestuale (3° livello della catena, T-Transforms to GENTLE) |
| **CL** | Certification Liaison | Interfaccia con l'autorità di certificazione |
| **CM** | Configuration Management | Gestione della configurazione |
| **CSDB** | Common Source DataBase | Base di dati comune S1000D contenente DM, PM, DML, BREX, ICN |
| **CYB** | Cybersecurity | Dominio G9 UTA — sicurezza cibernetica |
| **DAG** | Directed Acyclic Graph | Grafo aciclico orientato; struttura del registro AM.PEL |
| **DM** | Data Module | Modulo dati S1000D — unità atomica di contenuto tecnico |
| **DMC** | Data Module Code | Codice univoco di un Data Module secondo S1000D |
| **DML** | Data Module List | Lista controllata di Data Module con stato e applicabilità |
| **DO-160** | — | Standard RTCA per qualifica ambientale di apparecchiature avioniche |
| **DO-178C** | — | Standard RTCA per assicurazione software in sistemi avionici |
| **DO-254** | — | Standard RTCA per assicurazione hardware in sistemi avionici |
| **DPP** | Digital Product Passport | Passaporto digitale del prodotto — identità, composizione, storia |
| **DT** | Digital Twin | Gemello digitale |
| **DTCEC** | Digital Twin / Cloud / Edge Computing | Dominio G4 UTA — gemelli digitali, cloud, edge |
| **DTTA** | Defence Technology and Tactical Architecture | Dominio G3 UTA — tecnologia della difesa |
| **DWG** | Drawing | Disegno tecnico |
| **DXF** | Drawing Exchange Format | Formato di scambio per disegni 2D |
| **EASA** | European Union Aviation Safety Agency | Agenzia europea per la sicurezza aerea |
| **EC** | Eternity Continent | Specifica pan-europea di infrastruttura permanente GQAOA |
| **ECO** | Engineering Change Order | Ordine di modifica ingegneristica |
| **ECSS** | European Cooperation for Space Standardization | Cooperazione europea per la standardizzazione spaziale |
| **EIS** | Entry Into Service | Entrata in servizio |
| **EMC** | Electromagnetic Compatibility | Compatibilità elettromagnetica |
| **EPTA** | Energy and Propulsion Technology Architecture | Dominio G5 UTA — energia e propulsione |
| **ESA** | European Space Agency | Agenzia spaziale europea |
| **ESD** | Electrostatic Discharge | Scarica elettrostatica |
| **ESSA** | Earth Safety and Security Assemblies Center | Centro assemblaggio sicurezza terrestre (sede: München) |
| **FAA** | Federal Aviation Administration | Autorità aeronautica degli Stati Uniti |
| **FEA** | Finite Element Analysis | Analisi agli elementi finiti |
| **FMEA** | Failure Mode and Effects Analysis | Analisi dei modi di guasto e dei loro effetti |
| **FTA** | Fault Tree Analysis | Analisi ad albero dei guasti |
| **FTB** | Flying Test Bed | Banco prova volante |
| **FTS** | Flight Termination System | Sistema di terminazione del volo (sicurezza di range) |
| **GD&T** | Geometric Dimensioning and Tolerancing | Quotatura e tolleranze geometriche |
| **GENTLE** | Generative Engineering Narrative Transforming Language Engine | Motore di trasformazione del linguaggio ingegneristico (4° livello della catena) |
| **glTF** | GL Transmission Format | Formato aperto per modelli 3D (visualizzazione web) |
| **GNC** | Guidance, Navigation and Control | Guida, navigazione e controllo |
| **GQAOA** | GAIA Quantum Ampel Opt-Ins Architecture, Inc. | Organizzazione e architettura madre |
| **GSE** | Ground Support Equipment | Attrezzature di supporto a terra |
| **H₂** | Hydrogen (molecular) | Idrogeno molecolare |
| **HIL** | Hardware-in-the-Loop | Simulazione con hardware reale nel circuito |
| **HOB** | Hazardous On Board | Classificazione di pericolo a bordo |
| **IAM** | Identity and Access Management | Gestione identità e accessi |
| **ICD** | Interface Control Document | Documento di controllo interfaccia |
| **ICN** | Information Control Number | Numero di controllo informazione — identificativo per grafici S1000D |
| **ICS** | Industrial Control Systems | Sistemi di controllo industriale |
| **IEEE** | Institute of Electrical and Electronics Engineers | Istituto di ingegneria elettrica ed elettronica |
| **IETP** | Interactive Electronic Technical Publication | Pubblicazione tecnica elettronica interattiva |
| **IoT** | Internet of Things | Internet delle cose |
| **IPD** | Illustrated Parts Data | Dati parti illustrate |
| **iSpec** | International Specification | Specifica internazionale (ATA) |
| **ISO** | International Organization for Standardization | Organizzazione internazionale per la standardizzazione |
| **JT** | Jupiter Tessellation | Formato 3D leggero per visualizzazione |
| **KNOT** | Knowledge Nexus of Openness and Traceability | Nodo di incertezza — problema aperto registrato e tracciato |
| **KNU** | Knowledge Nexus Unit | Unità conoscitiva — artefatto prodotto per ridurre un KNOT |
| **KRP** | KNOT Review Panel | Pannello di revisione per chiusura KNOT |
| **LC** | Lifecycle (phase) | Fase del ciclo di vita (LC01–LC14) |
| **LOX** | Liquid Oxygen | Ossigeno liquido |
| **MACCHIN-AR-IA** | — | Ontologia tripartita della robotica GQAOA: MACCHIN (hardware), AR (percezione), IA (cognizione) |
| **MIL** | Model-in-the-Loop | Simulazione con modelli nel circuito |
| **MIL-STD** | Military Standard | Standard militare (US DoD) |
| **ML** | Machine Learning | Apprendimento automatico |
| **MoC** | Means of Compliance | Mezzi di conformità (certificazione) |
| **MSG-3** | Maintenance Steering Group – 3 | Metodologia per sviluppo programmi di manutenzione |
| **NASA** | National Aeronautics and Space Administration | Ente spaziale degli Stati Uniti |
| **NHOB** | Not Hazardous On Board | Classificazione di non-pericolo a bordo |
| **OEM** | Original Equipment Manufacturer | Costruttore originale dell'apparecchiatura |
| **OGATA** | Operational Ground Automation Technology Architecture | Dominio G7 UTA — automazione terrestre |
| **OPT-INS** | Opt-In System | Sistema di attivazione modulare — framework 6 assi |
| **OT** | Operational Technology | Tecnologia operativa (sistemi di controllo industriale) |
| **P&ID** | Piping and Instrumentation Diagram | Schema di tubazioni e strumentazione |
| **P&L** | Peace and Love | Pace e Amore — identità organizzativa GQAOA (non Profit and Loss) |
| **PCT** | Product Cross-reference Table | Tabella S1000D che associa prodotti a configurazioni |
| **PEM** | Proton Exchange Membrane | Membrana a scambio protonico (celle a combustibile) |
| **PIL** | Processor-in-the-Loop | Simulazione con processore target nel circuito |
| **PM** | Publication Module | Modulo di pubblicazione S1000D |
| **PMI** | Product Manufacturing Information | Informazioni di fabbricazione prodotto (annotazioni 3D) |
| **PRB** | Publication Review Board | Comitato di revisione delle pubblicazioni |
| **QASHT** | Q-ASI-HUMAN-TRANSGENTLE | Protocollo di coesistenza Q/ASI/HUMAN/TRANSGENTLE |
| **QCSAA** | Quantum Computing and Sentient Agency Architecture | Dominio G10 UTA — computazione quantistica e agenza sentiente |
| **QKD** | Quantum Key Distribution | Distribuzione quantistica delle chiavi |
| **RACI** | Responsible, Accountable, Consulted, Informed | Matrice di responsabilità |
| **RFC** | Request For Change | Richiesta di modifica |
| **ROBOT.INCs** | — | Tassonomia robotica GQAOA: 8 classi (M/C/V/A/D/G/S/Q) |
| **RTCA** | Radio Technical Commission for Aeronautics | Commissione tecnica radio per l'aeronautica |
| **S1000D** | — | Specifica internazionale per pubblicazione tecnica strutturata (Issue 5.0/6.0) |
| **SBOM** | Software Bill of Materials | Distinta base del software |
| **SC** | Special Condition | Condizione speciale (certificazione) |
| **SecOps** | Security Operations | Operazioni di sicurezza cibernetica |
| **SHA-256** | Secure Hash Algorithm 256-bit | Algoritmo di hash sicuro a 256 bit |
| **SICOCA** | Simulated Integrated Circuit for Quantum-Classical Architecture | Circuito integrato simulato per architettura quantistica-classica |
| **SIL** | Software-in-the-Loop | Simulazione con software nel circuito |
| **SSOT** | Single Source of Truth | Unica sorgente di verità — struttura di registrazione autoritativa |
| **STA** | Space Technology Architecture | Dominio G2 UTA — tecnologia spaziale |
| **STEP** | Standard for the Exchange of Product model data | Standard per lo scambio di dati di modelli di prodotto (ISO 10303) |
| **STC** | Supplemental Type Certificate | Certificato di tipo supplementare |
| **SUPIA** | Sistema Unico di Progettazione Industriale Avanzata | Il presente sistema — tassonomia eseguibile 1000 capitoli |
| **SVG** | Scalable Vector Graphics | Grafica vettoriale scalabile |
| **TDC** | Type Design Certificate | Certificato di progetto di tipo |
| **TGM** | Transgentle Model | Modello di specie transgentle (10 assiomi) |
| **TPS** | Thermal Protection System | Sistema di protezione termica |
| **TT** | Teknia Token | Token di ricompensa per contributi ingegneristici (v3.14) |
| **TVC** | Thrust Vector Control | Controllo del vettore di spinta |
| **TX** | Transaction | Transazione nel registro TT |
| **UAM** | Urban Air Mobility | Mobilità aerea urbana |
| **UR** | Union Realities | Framework di convergenza: PR ∪ VR ∪ AR ∪ MR ∪ DR ∪ XR ∪ QR |
| **UTA** | Universal Technology Architecture | Architettura tecnologica universale — 10 domini, 1000 capitoli |
| **V&V** | Verification and Validation | Verifica e validazione |
| **WBS** | Work Breakdown Structure | Struttura di scomposizione del lavoro |
| **XR** | Extended Reality | Realtà estesa (VR + AR + MR) |
| **.YieldedAML** | .YieldedAlgorithmicMachineLearning | Dichiarazione di provenienza IA nel front-matter di un artefatto |

#### A.2 Termini

| Termine | Definizione |
|---------|-------------|
| **Artefatto** | Qualsiasi entità prodotta e registrata nel SUPIA: requisito, specifica, disegno, modello, procedura, evidenza, modulo dati, registro |
| **Asse OPT-INS** | Una delle 6 dimensioni organizzative del framework: O, P, T, I, N, S |
| **Baseline** | Insieme controllato di artefatti in un dato stato di configurazione, approvato dal CCB |
| **Capitolo** | Unità di classificazione a 3 cifre (000–999) nell'architettura UTA |
| **Cartiglio** | Riquadro delle iscrizioni nel disegno tecnico (ISO 7200); nel SUPIA include codice UTA, KNOT, programma |
| **Catena di tracciabilità** | Sequenza: ALICE → BOB DT → CHARLIE-T → GENTLE → BOOST |
| **Circolarità** | Principio per cui il ritiro di un artefatto fisico alimenta il riciclo o la ri-progettazione (LC14) |
| **Decennio** | Blocco di 10 capitoli consecutivi entro un dominio (es. 020–029) |
| **Dominio** | Uno dei 10 gruppi (G1–G10) dell'architettura UTA, ciascuno con 100 capitoli |
| **Effectivity** | Condizione di applicabilità specifica per prodotto, serial, lotto o configurazione |
| **Evidenza** | Artefatto che dimostra conformità a un requisito o riduce un'incertezza |
| **Gate** | Punto decisionale nel ciclo di vita del programma (G0–G9); richiede soddisfazione di criteri |
| **Gemello digitale** | Vista computazionale sulla SSOT che integra geometria, modelli analitici e dati operativi in tempo reale |
| **Grammatica UTA** | Sistema di codifica universale `UTA-DDD-SS-ss-nn` che identifica univocamente ogni nodo nell'architettura |
| **Impatto** | Misura della riduzione di incertezza prodotta da un KNU su un KNOT (ΔR + λ·S) |
| **Incertezza** | Stato di conoscenza incompleta su un artefatto, misurato come Residuo (0–100) |
| **Iron Bird** | Banco prova a integrazione completa che replica tutti i sistemi di bordo a terra |
| **KNOT (nodo)** | Registrazione formale di un'incertezza aperta, con proprietario, target, dipendenze e pool TT |
| **KNU (unità)** | Artefatto prodotto per ridurre un KNOT; classificato per tipo (REQ, ICD, ANA, TEST, SAF, CM, PUB, DWG, SIM, DPP) |
| **Nodo foglia** | Il livello più basso della tassonomia (sotto-soggetto), che porta l'intera struttura SSOT + PUB |
| **Nuvola di revisione** | Indicazione grafica sul disegno tecnico della zona modificata da una revisione |
| **Primo diedro** | Metodo di proiezione europeo (Metodo E, ISO 128-30) |
| **Provenienza IA** | Dichiarazione `.YieldedAML` che indica se un artefatto è stato prodotto con assistenza di intelligenza artificiale |
| **Pubblicazione derivata** | Deliverable (DM, PM, PDF, IETP) generato automaticamente dalla SSOT, mai scritto indipendentemente |
| **Residuo** | Livello di incertezza rimanente su un KNOT (scala 0–100; target tipico ≤ 10) |
| **Sezione** | Livello 2 della tassonomia UTA (2 cifre, 00–99) entro un capitolo |
| **Sforzo** | Misura del lavoro investito da un contributore per produrre un KNU |
| **Soggetto** | Livello 3 della tassonomia UTA (2 cifre, 00–99) entro una sezione |
| **Sotto-soggetto** | Livello 4 della tassonomia UTA (2 cifre, 00–99) — nodo foglia |
| **Spillover** | Impatto indiretto di un KNU su KNOT adiacenti (misurato con coefficiente λ) |
| **Tassonomia eseguibile** | Tassonomia in cui la struttura stessa è la baseline operativa, non solo una classificazione |
| **Terzo diedro** | Metodo di proiezione americano (Metodo A, ASME Y14.3) |
| **Tokenomics** | Economia dei token TT: formula di distribuzione, pool, allocazione per dominio |

### Appendice B — Genealogia del SUPIA

```
ATA 100 (1956)
 └─► ATA iSpec 2200 (1993)
      └─► S1000D (2000)
           └─► OPT-IN Framework (2024)
                └─► OPT-INS 6 assi (2025)
                     └─► G1–G10 Taxonomy (2025)
                          └─► GQAOA UTA 1.0 (2026)
                               └─► ★ SUPIA 1.0 (2026)
                                   Tassonomia = Baseline = Pubblicazione = Progettazione
```

### Appendice C — Mappa delle dipendenze inter-dominio

```
G1 ATA ◄────────────► G5 EPTA         (propulsione ↔ energia)
  │                       │
  ├───► G2 STA            ├───► G6 AMTA   (materiali per propulsione)
  │       │                │
  │       └───► G3 DTTA    └───► G7 OGATA  (automazione fabbricazione)
  │              │
  ├───► G4 DTCEC ◄─────────┘               (gemello digitale difesa)
  │       │
  │       ├───► G8 ACV                      (gemelli UAM)
  │       │
  │       └───► G9 CYB                      (ciber-sicurezza per GD)
  │              │
  └───► G10 QCSAA ◄───────┘                (quantistica → cripto → tutto)
```

### Appendice D — Stime dimensionali a costruzione completa

| Livello | Conteggio stimato |
|---------|------------------:|
| Domini | 10 |
| Decenni | 100 |
| Capitoli (DDD) | 1.000 |
| Sezioni (×10/cap) | ~10.000 |
| Soggetti (×5/sez) | ~50.000 |
| Sotto-soggetti (×3/sogg) | ~150.000 |
| Cartelle SSOT per foglia (×14 LC) | ~2.100.000 |
| Cartelle PUB per foglia (×10) | ~1.500.000 |
| File seme LC01 per foglia (×6) | ~900.000 |
| **Nodi directory totali** | **~4.500.000** |

### Appendice E — Provenienza e dichiarazione .YieldedAML

Ogni artefatto prodotto con assistenza di intelligenza artificiale porta la dichiarazione di provenienza `.YieldedAlgorithmicMachineLearning` come front-matter YAML:

```yaml
---
.YieldedAlgorithmicMachineLearning: true
Last.MarkedDown: "2026-04-11T12:00:00Z"
model: "claude-opus-4-6"
human_author: "Amedeo Pelliccia"
review_status: "human_reviewed"
---
```

### Appendice F — Comandi CLI di riferimento

```bash
# Validare struttura
python tools/ci/uta_validator.py --domain G1 --check
python tools/ci/uta_validator.py --all --check

# Scaffoldare un nuovo capitolo
python tools/scaffold.py --chapter 465 --title "Progettazione Stack PEM"

# Chiudere un KNOT e distribuire TT
python tools/knu_distribution.py distribute --knot KNOT-UTA-028-10-00-001

# Verificare integrità del registro
python tools/tek_tokens.py verify

# Generare rapporto di stato per programma
python tools/programme_report.py --manifest programmes/AMPEL360-Q100/PROGRAMME_MANIFEST.yaml
```

---

## FIRMA

```
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│  SISTEMA UNICO DI PROGETTAZIONE INDUSTRIALE AVANZATA             │
│  SUPIA v1.0                                                      │
│                                                                  │
│  Emesso da:    Amedeo Pelliccia                                  │
│  Organizzazione: GQAOA .INC                                     │
│  Data:         2026-04-11                                        │
│  Stato:        BASELINE ATTIVA                                   │
│                                                                  │
│  Un sistema. Dieci domini. Mille capitoli.                       │
│  Ogni nodo eseguibile. Ogni incertezza tracciata.                │
│  Ogni contributo ricompensato.                                   │
│                                                                  │
│  "Aggiungere valore, espandere il potenziale."                   │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

*GQAOA Universal Technology Architecture — SUPIA v1.0*  
*Amedeo Pelliccia — AEROSPACEMODEL Lifecycle Operating System*
