# LIBRO UNICO DELLE TECNOLOGIE — RICICLATI

**Acronimo:** LUT-RICICLATI  
**Codice:** GQAOA-LUT-RICICLATI-001  
**Versione:** 1.0  
**Autorità:** GQAOA .INC — GAIA QUANTUM AMPEL OPT-INS ARCHITECTURE  
**Architetto:** Amedeo Pelliccia  
**Data:** 2026-04-14  
**Stato:** Baseline attiva  
**Lingue operative:** IT (primaria) · EN · ES · DE · FR  
**Riferimento padre:** [GQAOA-UTA-SUPIA-001](./GQAOA-UTA-SUPIA-001.md)

---

> *"Nulla si crea, nulla si distrugge, tutto si trasforma."*
> — Antoine-Laurent de Lavoisier

---

## INDICE

0. [Scopo e Campo di Applicazione](#0-scopo-e-campo-di-applicazione)
1. [Acronimo RICICLATI](#1-acronimo-riciclati)
2. [Stati del Ciclo Tecnologico](#2-stati-del-ciclo-tecnologico)
3. [Struttura del Registro](#3-struttura-del-registro)
4. [Governance delle Transizioni](#4-governance-delle-transizioni)
5. [Integrazione con SSOT e LC14](#5-integrazione-con-ssot-e-lc14)
6. [Tracciabilità e DPP](#6-tracciabilità-e-dpp)
7. [Tokenomics della Circolarità](#7-tokenomics-della-circolarità)
8. [File Canonici](#8-file-canonici)
9. [Flusso Operativo](#9-flusso-operativo)
10. [Allineamento Normativo](#10-allineamento-normativo)
11. [Glossario](#11-glossario)

---

## 0. SCOPO E CAMPO DI APPLICAZIONE

### 0.1 Scopo

Il **Libro Unico delle Tecnologie** (LUT) è il registro centralizzato e immutabile che traccia ogni tecnologia, componente, sottosistema e materiale all'interno dell'architettura UTA/OPT-INS attraverso il suo intero ciclo di vita — dall'adozione iniziale al riutilizzo circolare.

Il LUT non è un catalogo statico. È un **registro vivente** che riflette in tempo reale lo stato corrente di ogni tecnologia nei quattro stati fondamentali: **In Uso**, **Disuso**, **Nuova Progettazione** e **Riassetti (RICICLATI)**.

### 0.2 Campo di Applicazione

Il LUT si applica a:

- Tutti i 1.000 capitoli dell'architettura UTA (G1–G10)
- Tutti i 6 assi OPT-INS (O, P, T, I, N, S)
- Tutti i programmi attivi (AMPEL360 Q100, GAIA-SPACE-LAUNCHER, SPACET Q10)
- Ogni artefatto fisico, digitale o ibrido registrato nel SUPIA

### 0.3 Principio Fondante

```
Circolarità ≠ Smaltimento
Circolarità = Trasformazione → Riuso → Valore rinnovato
```

Ogni tecnologia che raggiunge lo stato LC14 (Ritiro e Circolarità) non termina il suo ciclo — **lo rinnova**.

---

## 1. ACRONIMO RICICLATI

**RICICLATI** = **R**egistro **I**ntegrato delle **C**onfigurazioni **I**ndustriali per il **C**iclo di vita, **L**ineage, **A**ggiornamento **T**ecnologico e **I**nnovazione

```
R — Registro          → Libro Unico, fonte autoritativa
I — Integrato         → Attraversa tutti i domini e assi
C — Configurazioni    → Stato di configurazione di ogni tecnologia
I — Industriali       → Applicazione industriale e operativa
C — Ciclo di vita     → LC01–LC14 completo
L — Lineage           → Tracciabilità completa (ALICE → BOOST)
A — Aggiornamento     → Transizioni di stato governate
T — Tecnologico       → Ogni tecnologia, materiale, sottosistema
I — Innovazione       → Nuova progettazione e ri-progettazione
```

---

## 2. STATI DEL CICLO TECNOLOGICO

### 2.1 I quattro stati fondamentali

| Stato | Codice | Colore | Descrizione |
|-------|--------|--------|-------------|
| **In Uso** | `USO` | 🟢 Verde | Tecnologia attiva in produzione, operazione o manutenzione |
| **Disuso** | `DIS` | 🟠 Arancione | Tecnologia deprecata, in fase di sostituzione progressiva |
| **Nuova Progettazione** | `NPR` | 🔵 Blu | Tecnologia in fase di progettazione, prototipazione o qualifica |
| **Riassetti (RICICLATI)** | `RIC` | 🟣 Viola | Tecnologia ritirata e trasformata per riutilizzo circolare |

### 2.2 Sotto-stati

| Stato padre | Sotto-stato | Codice | Descrizione |
|-------------|-------------|--------|-------------|
| USO | Operativo | `USO-OPR` | In servizio attivo |
| USO | Manutenzione | `USO-MNT` | Sotto manutenzione programmata |
| USO | Monitorato | `USO-MON` | In servizio con condition monitoring attivo |
| DIS | Pianificato | `DIS-PLN` | Ritiro pianificato, sostituzione in corso |
| DIS | Parziale | `DIS-PAR` | Parzialmente dismesso, alcune istanze ancora in uso |
| DIS | Completo | `DIS-CMP` | Completamente dismesso da tutti i programmi |
| NPR | Concezione | `NPR-CON` | Fase concettuale (LC01–LC02) |
| NPR | Sviluppo | `NPR-SVL` | In sviluppo e analisi (LC03–LC05) |
| NPR | Qualifica | `NPR-QUA` | In verifica e validazione (LC06–LC07) |
| NPR | Industrializzazione | `NPR-IND` | In transizione alla produzione (LC08–LC09) |
| RIC | Smontaggio | `RIC-SMO` | In fase di smontaggio controllato |
| RIC | Valutazione | `RIC-VAL` | In valutazione per riuso / riciclo / riprogettazione |
| RIC | Riuso | `RIC-RIU` | Componente riutilizzato tal quale in altro contesto |
| RIC | Riciclo | `RIC-RCL` | Materiale riciclato e reintrodotto nella catena |
| RIC | Riprogettazione | `RIC-RPR` | Tecnologia ri-progettata basata sull'esperienza operativa |

### 2.3 Diagramma delle transizioni

```
                        ┌─────────────────────────┐
                        │                         │
                        ▼                         │
              ┌──────────────┐          ┌──────────────┐
              │              │          │              │
         ┌───►│  NUOVA PROG. │──G5/G6──►│    IN USO    │◄───┐
         │    │   (NPR) 🔵   │          │   (USO) 🟢   │    │
         │    └──────────────┘          └──────┬───────┘    │
         │                                     │            │
         │                                     │ G8/G9      │
         │                                     ▼            │
         │                             ┌──────────────┐     │
         │                             │              │     │
         │                             │    DISUSO    │     │
         │                             │   (DIS) 🟠   │     │
         │                             └──────┬───────┘     │
         │                                     │            │
         │                                     │ G9         │
         │                                     ▼            │
         │                             ┌──────────────┐     │
         │                             │  RIASSETTI   │     │
         └─────────────────────────────│ (RIC) 🟣     │─────┘
              RIC-RPR → NPR            │  RICICLATI   │  RIC-RIU → USO
                                       └──────────────┘
```

**Regole di transizione:**

| Da | A | Gate richiesto | Condizioni |
|----|---|---------------|------------|
| NPR → USO | G5 (Production) o G6 (Service) | Qualifica completata, certificazione ottenuta |
| USO → DIS | G8 (Obsolescence) | Piano di sostituzione approvato, alternativa qualificata |
| DIS → RIC | G9 (End-of-Life) | DPP completato, piano di circolarità approvato |
| RIC → NPR | — | Decisione di riprogettazione (RIC-RPR), nuovo KNOT aperto |
| RIC → USO | — | Valutazione positiva per riuso diretto (RIC-RIU) |
| NPR → DIS | G8 | Progetto cancellato prima della qualifica |

---

## 3. STRUTTURA DEL REGISTRO

### 3.1 Schema del record tecnologico

Ogni tecnologia nel LUT è identificata da un record univoco con la seguente struttura:

```yaml
# LUT Record — Esempio
lut_id: "LUT-UTA-028-10-00-T001"
uta_chapter: "028"
uta_node: "UTA-028-10-00-00"
technology_name: "Sistema di Alimentazione a Idrogeno Liquido (LH₂)"
technology_class: "SUBSYSTEM"
current_state: "USO"
current_substate: "USO-OPR"
programmes:
  - id: "AMPEL360-Q100"
    role: "PRIMARY"
  - id: "GAIA-SPACE-LAUNCHER"
    role: "SECONDARY"
lifecycle_phase: "LC10"
first_registered: "2026-01-15"
last_transition: "2026-03-20"
dpp_hash: "sha256:a1b2c3d4..."
knot_refs:
  - "KNOT-UTA-028-10-00-001"
  - "KNOT-UTA-028-10-00-003"
alice_ref: "ALICE-028-LH2-SYS-001"
bob_dt_ref: "BOB-DT-028-LH2-SYS-001"
charlie_t_ref: "CHARLIE-T-028-LH2-SYS-001"
circularity:
  recyclability_index: 0.87
  reuse_potential: "HIGH"
  hazardous_materials: false
  sbom_ref: "SBOM-028-LH2-001"
```

### 3.2 Classi tecnologiche

| Classe | Codice | Descrizione |
|--------|--------|-------------|
| Sistema | `SYSTEM` | Sistema completo (es. ATA 28 — Fuel) |
| Sottosistema | `SUBSYSTEM` | Sottosistema funzionale |
| Componente | `COMPONENT` | Componente fisico o unità sostituibile |
| Materiale | `MATERIAL` | Materiale o sostanza |
| Software | `SOFTWARE` | Modulo software, algoritmo, modello AI |
| Processo | `PROCESS` | Processo produttivo o operativo |
| Strumento | `TOOL` | Attrezzatura, GSE, strumento di prova |
| Standard | `STANDARD` | Norma, specifica, regolamento |

---

## 4. GOVERNANCE DELLE TRANSIZIONI

### 4.1 Autorità

| Transizione | Autorità decisionale | Approvazione |
|-------------|---------------------|-------------|
| NPR → USO | Comitato Tecnico di Programma | CCB + Autorità di Certificazione |
| USO → DIS | Q-DATAGOV + Proprietario del Capitolo | CCB |
| DIS → RIC | Responsabile Circolarità + Q-DATAGOV | CCB + Responsabile Ambientale |
| RIC → NPR | Architetto di Sistema | CCB |
| RIC → USO | Comitato Tecnico + Responsabile Qualità | CCB |

### 4.2 Processo di transizione

```
1. PROPOSTA        →  ECO (Engineering Change Order) con giustificazione
2. VALUTAZIONE     →  Impatto su programmi, costi, sicurezza, circolarità
3. APPROVAZIONE    →  CCB vota, DPP aggiornato
4. ESECUZIONE      →  Transizione registrata nel LUT, KNOT aggiornati
5. VERIFICA        →  Stato post-transizione verificato, TT distribuiti
```

### 4.3 Vincoli di integrità

- Nessuna tecnologia può essere in due stati primari simultaneamente
- Ogni transizione deve avere un ECO tracciabile
- Il DPP deve essere aggiornato **prima** della transizione effettiva
- La catena di tracciabilità (ALICE → BOOST) deve essere coerente in tutti gli stati

---

## 5. INTEGRAZIONE CON SSOT E LC14

### 5.1 Posizionamento nel nodo foglia

Il registro LUT si materializza all'interno della struttura SSOT di ogni nodo foglia:

```
<nodo-foglia>/
├── SSOT/
│   ├── LC01_PROBLEM_STATEMENT/
│   │   └── KNOTS.csv         ← KNOT con tag LUT-STATE
│   ├── LC08_CONFIGURATION/
│   │   └── LUT_REGISTER.yaml ← Registro tecnologie del capitolo
│   └── LC14_RETIREMENT_CIRCULARITY/
│       ├── LUT_CIRCULARITY.yaml  ← Piano di circolarità
│       ├── DPP_RECORDS/          ← Passaporti digitali
│       └── SBOM/                 ← Software/Hardware Bill of Materials
└── PUB/AMM/CSDB/DM/
    └── DMC-...-LUT-*.xml    ← Data Module LUT pubblicato
```

### 5.2 Collegamento ai file LC01

Nel `KNOTS.csv`, ogni KNOT può dichiarare lo stato LUT corrente:

```csv
knot_id,title,type,status,priority,owner,created,lut_state,lut_substate
KNOT-UTA-028-10-00-001,LH₂ System Qualification,TECH,OPEN,HIGH,Propulsion-Lead,2026-01-15,NPR,NPR-QUA
```

### 5.3 Flusso LC14 → RIC

Quando un artefatto raggiunge LC14:

```
LC14 attivato
    │
    ├── 1. DPP completato e firmato
    ├── 2. SBOM estratto e verificato
    ├── 3. Indice di riciclabilità calcolato
    ├── 4. Piano di circolarità approvato (LUT_CIRCULARITY.yaml)
    ├── 5. Transizione DIS → RIC registrata nel LUT
    └── 6. Sotto-stato RIC assegnato:
             RIC-SMO → RIC-VAL → {RIC-RIU | RIC-RCL | RIC-RPR}
```

---

## 6. TRACCIABILITÀ E DPP

### 6.1 Passaporto Digitale del Prodotto (DPP)

Ogni tecnologia nel LUT genera un DPP conforme alla normativa EU per la circolarità:

```yaml
# DPP Record
dpp_id: "DPP-UTA-028-10-00-T001"
lut_ref: "LUT-UTA-028-10-00-T001"
product_identity:
  name: "LH₂ Fuel System Assembly"
  manufacturer: "GQAOA / P&L Inc."
  serial: "LH2-SYS-001-A360"
  batch: "B2026-Q1"
composition:
  materials:
    - name: "Inconel 718"
      percentage: 45
      recyclable: true
    - name: "CFRP"
      percentage: 30
      recyclable: true
    - name: "PTFE Seals"
      percentage: 5
      recyclable: false
  hazardous: false
lifecycle_history:
  - state: "NPR"
    date: "2025-06-01"
    eco: "ECO-2025-0142"
  - state: "USO"
    date: "2026-03-20"
    eco: "ECO-2026-0028"
carbon_footprint:
  manufacturing_kg_co2: 1250
  operational_kg_co2_per_year: 85
circularity_index: 0.87
hash: "sha256:e3b0c44298fc1c149afbf4c8996fb924..."
```

### 6.2 Catena di tracciabilità nel LUT

```
ALICE (fisico)    →  Componente / sistema installato
BOB DT (gemello)  →  Modello digitale con stato LUT
CHARLIE-T (agente)→  Monitoraggio stato e suggerimento transizioni
GENTLE (motore)   →  Generazione documentazione di transizione
BOOST (output)    →  Report di circolarità e DPP pubblicato
```

---

## 7. TOKENOMICS DELLA CIRCOLARITÀ

### 7.1 Incentivi TT per transizioni virtuose

| Azione | Ricompensa TT | Condizione |
|--------|----------:|-----------|
| Registrazione iniziale nel LUT | 10 TT | Record completo e verificato |
| Transizione USO → DIS documentata | 25 TT | Piano di sostituzione approvato |
| Completamento DPP | 50 TT | DPP completo con SBOM e indice circolarità |
| Transizione DIS → RIC con piano | 75 TT | Piano di circolarità approvato |
| Riuso diretto (RIC-RIU) | 100 TT | Componente riutilizzato con evidenza |
| Riciclo materiale (RIC-RCL) | 80 TT | Materiale reintrodotto nella catena |
| Riprogettazione (RIC-RPR) | 150 TT | Nuovo KNOT aperto basato su esperienza operativa |
| Indice circolarità ≥ 0.90 | 50 TT bonus | Calcolato e verificato |

### 7.2 Pool dedicato

Dal pool TT complessivo, il **2%** (40.000.000 TT) è riservato alla circolarità e distribuito attraverso il meccanismo LUT-RICICLATI.

---

## 8. FILE CANONICI

### 8.1 LUT_REGISTER.yaml

Posizione: `SSOT/LC08_CONFIGURATION/LUT_REGISTER.yaml`

```yaml
# LUT Register — Capitolo UTA-028
chapter: "028"
chapter_name: "Fuel"
last_updated: "2026-04-14"
technologies:
  - lut_id: "LUT-UTA-028-10-00-T001"
    name: "LH₂ Fuel System"
    class: "SUBSYSTEM"
    state: "USO"
    substate: "USO-OPR"
    programmes: ["AMPEL360-Q100"]
    lc_phase: "LC10"
    dpp_ref: "DPP-UTA-028-10-00-T001"
    
  - lut_id: "LUT-UTA-028-10-00-T002"
    name: "Jet-A1 Fuel System (Legacy)"
    class: "SUBSYSTEM"
    state: "DIS"
    substate: "DIS-PLN"
    programmes: []
    lc_phase: "LC14"
    dpp_ref: "DPP-UTA-028-10-00-T002"
    replacement: "LUT-UTA-028-10-00-T001"
```

### 8.2 LUT_CIRCULARITY.yaml

Posizione: `SSOT/LC14_RETIREMENT_CIRCULARITY/LUT_CIRCULARITY.yaml`

```yaml
# Piano di Circolarità — Capitolo UTA-028
chapter: "028"
last_updated: "2026-04-14"
retired_technologies:
  - lut_id: "LUT-UTA-028-10-00-T002"
    name: "Jet-A1 Fuel System (Legacy)"
    state: "RIC"
    substate: "RIC-VAL"
    circularity_plan:
      reusable_components:
        - part: "Fuel Pumps"
          destination: "RIC-RIU → Ground Test Equipment"
          quantity: 4
        - part: "Fuel Lines (Ti-6Al-4V)"
          destination: "RIC-RCL → Materiale titanio riciclato"
          quantity: 24
      recyclable_materials:
        - material: "Aluminum 7075"
          kg: 120
          destination: "Fonderia certificata"
        - material: "Stainless Steel 316L"
          kg: 85
          destination: "Rifusione"
      non_recyclable:
        - material: "Elastomer Seals"
          kg: 3
          destination: "Smaltimento controllato"
      circularity_index: 0.94
      carbon_saved_kg_co2: 890
```

---

## 9. FLUSSO OPERATIVO

### 9.1 Ciclo completo

```
┌─────────────────────────────────────────────────────────────────┐
│                    LIBRO UNICO DELLE TECNOLOGIE                 │
│                                                                 │
│   1. IDENTIFICAZIONE                                            │
│      └─ Nuova tecnologia → LUT_REGISTER.yaml (stato: NPR)      │
│         └─ KNOT aperto, KNU pianificati                         │
│                                                                 │
│   2. QUALIFICA E ADOZIONE                                       │
│      └─ V&V completata → Transizione NPR → USO                 │
│         └─ DPP creato, TT distribuiti                           │
│                                                                 │
│   3. VITA OPERATIVA                                             │
│      └─ Condition monitoring via CHARLIE-T                      │
│         └─ Stato USO-OPR / USO-MNT / USO-MON                   │
│                                                                 │
│   4. OBSOLESCENZA                                               │
│      └─ Piano di sostituzione → Transizione USO → DIS           │
│         └─ Alternative qualificate, migrazione avviata          │
│                                                                 │
│   5. RITIRO E CIRCOLARITÀ                                       │
│      └─ LC14 attivato → Transizione DIS → RIC                  │
│         └─ DPP completato, SBOM estratto                        │
│         └─ Piano di circolarità (LUT_CIRCULARITY.yaml)          │
│                                                                 │
│   6. TRASFORMAZIONE                                             │
│      ├─ RIC-RIU → Riuso diretto → USO (nuovo contesto)         │
│      ├─ RIC-RCL → Riciclo materiale → Catena produttiva        │
│      └─ RIC-RPR → Riprogettazione → NPR (nuovo ciclo)          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 9.2 Metriche di circolarità

| Metrica | Formula | Target |
|---------|---------|--------|
| Indice di Circolarità | `IC = (massa_riusata + massa_riciclata) / massa_totale` | ≥ 0.85 |
| Tasso di Riuso | `TR = componenti_riusati / componenti_totali` | ≥ 0.30 |
| Risparmio CO₂ | `ΔCO₂ = CO₂_produzione_vergine − CO₂_circolare` | Positivo |
| Copertura DPP | `CDPP = tecnologie_con_DPP / tecnologie_totali` | 1.00 |
| Velocità di Transizione | `VT = tempo_medio_transizione` | ≤ 90 giorni |

---

## 10. ALLINEAMENTO NORMATIVO

| Norma | Ambito | Applicazione nel LUT |
|-------|--------|---------------------|
| **EU Reg. 2024/1781** (Ecodesign) | Passaporto digitale del prodotto | DPP obbligatorio per ogni tecnologia |
| **EU Reg. 2023/1542** (Batterie) | Circolarità batterie | Sottostati RIC per celle energetiche |
| **ISO 14040/14044** | Valutazione del ciclo di vita (LCA) | Calcolo impronta carbonio |
| **ISO 14001** | Gestione ambientale | Gestione materiali pericolosi |
| **REACH** (EC 1907/2006) | Sostanze chimiche | Dichiarazione materiali nel DPP |
| **RoHS** (EU 2011/65) | Sostanze pericolose | Flag `hazardous_materials` |
| **S1000D** | Documentazione tecnica | Data Module LUT in PUB/CSDB |
| **ASD-STE** | Linguaggio semplificato | Descrizioni in DM leggibili |
| **EN 9100** | Qualità aerospaziale | Gestione configurazione (LC08) |
| **ECSS-Q-ST-40** | Assicurazione prodotto spaziale | Tracciabilità componenti |

---

## 11. GLOSSARIO

### 11.1 Acronimi specifici LUT

| Acronimo | Espansione | Definizione |
|----------|-----------|-------------|
| **LUT** | Libro Unico delle Tecnologie | Registro centralizzato dello stato di tutte le tecnologie |
| **RICICLATI** | Registro Integrato delle Configurazioni Industriali per il Ciclo di vita, Lineage, Aggiornamento Tecnologico e Innovazione | Acronimo completo del sistema |
| **DPP** | Digital Product Passport | Passaporto digitale del prodotto |
| **SBOM** | Software/Hardware Bill of Materials | Distinta componenti software e hardware |
| **ECO** | Engineering Change Order | Ordine di modifica ingegneristica |
| **IC** | Indice di Circolarità | Rapporto materiale circolare su totale |
| **LCA** | Life Cycle Assessment | Valutazione del ciclo di vita |

### 11.2 Termini specifici

| Termine | Definizione |
|---------|-------------|
| **Circolarità** | Principio per cui il ritiro di un artefatto fisico alimenta il riciclo o la ri-progettazione, generando valore rinnovato (LC14 → NPR/USO) |
| **Disuso** | Stato in cui una tecnologia è deprecata e in fase di sostituzione progressiva, ma non ancora ritirata |
| **In Uso** | Stato operativo attivo di una tecnologia in uno o più programmi |
| **Lineage** | Tracciabilità completa della storia di una tecnologia attraverso tutti gli stati e transizioni |
| **Nuova Progettazione** | Stato di una tecnologia in fase di concezione, sviluppo, qualifica o industrializzazione |
| **Riassetti** | Riorganizzazione e trasformazione di una tecnologia ritirata per riuso, riciclo o riprogettazione |
| **RICICLATI** | L'insieme delle azioni di trasformazione circolare: smontaggio, valutazione, riuso, riciclo, riprogettazione |
| **Transizione** | Cambio di stato governato di una tecnologia nel LUT, sempre tracciabile e approvato dal CCB |

---

*Fine del documento GQAOA-LUT-RICICLATI-001 v1.0*
