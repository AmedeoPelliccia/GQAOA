# LIBRO UNICO DELLE TECNOLOGIE

## In Uso · Disuso · Nuova Progettazione · Riassetti (RICICLATI)

**Acronimo:** LUTNDR  
**Codice:** GQAOA-UTA-LUTNDR-001  
**Versione:** 1.0  
**Autorità:** GQAOA .INC — GAIA QUANTUM AMPEL OPT-INS ARCHITECTURE  
**Architetto:** Amedeo Pelliccia  
**Data:** 2026-04-14  
**Stato:** Baseline attiva  
**Documento padre:** SUPIA v1.0 (GQAOA-UTA-SUPIA-001)  
**Lingue operative:** IT (primaria) · EN · ES · DE · FR

---

> *"Nessuna tecnologia muore. Si trasforma, si ricombina, si trascende."*
>
> Ogni tecnologia è un nodo nel continuo: nasce, serve, declina, e — nel paradigma circolare — rinasce in forma nuova. Il Libro Unico registra questo intero arco con la stessa disciplina con cui si registra un requisito o un disegno.

---

## INDICE

0. [Scopo e Necessità](#0-scopo-e-necessità)
1. [Le Quattro Ere di una Tecnologia](#1-le-quattro-ere-di-una-tecnologia)
2. [Architettura del Registro](#2-architettura-del-registro)
3. [Classificazione degli Stati Tecnologici](#3-classificazione-degli-stati-tecnologici)
4. [Grammatica Identificativa](#4-grammatica-identificativa)
5. [Schema del Record Tecnologico](#5-schema-del-record-tecnologico)
6. [Governance delle Transizioni](#6-governance-delle-transizioni)
7. [Integrazione con SSOT e Ciclo di Vita](#7-integrazione-con-ssot-e-ciclo-di-vita)
8. [Tracciabilità e Passaporto Digitale (DPP)](#8-tracciabilità-e-passaporto-digitale-dpp)
9. [Tokenomics della Circolarità](#9-tokenomics-della-circolarità)
10. [File Canonici](#10-file-canonici)
11. [Flusso Operativo](#11-flusso-operativo)
12. [Allineamento Normativo](#12-allineamento-normativo)
13. [Glossario](#13-glossario)

---

## 0. SCOPO E NECESSITÀ

### 0.1 Perché un Libro Unico

Nell'architettura UTA/OPT-INS ogni tecnologia — dal singolo componente al sistema completo, dal materiale avanzato all'algoritmo software — attraversa un arco di vita che il SUPIA scandisce in 14 fasi (LC01–LC14). Ma nessun artefatto del SUPIA rispondeva alla domanda fondamentale:

> *Qual è lo stato corrente di questa tecnologia, dove è stata, e dove può andare?*

Il **Libro Unico delle Tecnologie** (LUT) colma questa lacuna. È il registro centralizzato e immutabile che traccia ogni tecnologia, componente, sottosistema e materiale attraverso il suo intero ciclo di vita — dall'adozione iniziale al riutilizzo circolare.

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

## 1. LE QUATTRO ERE DI UNA TECNOLOGIA

Ogni tecnologia nel LUT attraversa quattro ere fondamentali — non necessariamente in sequenza lineare, ma in un ciclo che può ripetersi:

| Era | Nome | Codice | Colore | Fase dominante |
|-----|------|--------|--------|----------------|
| I | **In Uso** | `USO` | 🟢 Verde | LC09–LC12 |
| II | **Disuso** | `DIS` | 🟠 Arancione | LC14 (ingresso) |
| III | **Nuova Progettazione** | `NPR` | 🔵 Blu | LC01–LC08 |
| IV | **Riassetti (RICICLATI)** | `RIC` | 🟣 Viola | LC14 (circolare) |

### 1.1 Il Ciclo Continuo

```
         ┌──────────── Riprogettazione ────────────┐
         │                                          │
         ▼                                          │
   ┌──────────┐       ┌──────────┐       ┌──────────┐       ┌──────────┐
   │  NUOVA   │ G5/G6 │          │  G8   │          │  G9   │RIASSETTI │
   │  PROG.   │──────►│  IN USO  │──────►│  DISUSO  │──────►│RICICLATI │
   │ (NPR) 🔵 │       │ (USO) 🟢 │       │ (DIS) 🟠 │       │ (RIC) 🟣 │
   └──────────┘       └────┬─────┘       └──────────┘       └────┬─────┘
                           ▲                                      │
                           └────────── Riuso diretto ─────────────┘
```

### 1.2 Metafora

- **NPR** = Nascita — La tecnologia viene concepita, progettata, qualificata
- **USO** = Vita — La tecnologia serve, produce, opera
- **DIS** = Declino — La tecnologia viene superata, ritirata progressivamente
- **RIC** = Rinascita — La tecnologia si trasforma, si ricombina, si trascende

---

## 2. ARCHITETTURA DEL REGISTRO

### 2.1 Posizionamento nell'ecosistema

```
┌─────────────────────────────────────────────┐
│              SUPIA (Sistema Unico)          │
│  ┌─────────┐  ┌─────────┐  ┌─────────────┐ │
│  │  SSOT   │  │   PUB   │  │    LUTNDR   │ │
│  │ LC01–14 │  │ S1000D  │  │ Libro Unico │ │
│  │ Artefatti│  │ DM/PM   │  │ Tecnologie  │ │
│  └─────────┘  └─────────┘  └─────────────┘ │
│         │           │             │         │
│         └───────────┼─────────────┘         │
│                     │                       │
│              KNOT / KNU / TT                │
└─────────────────────────────────────────────┘
```

### 2.2 Struttura logica

Il LUT è organizzato in tre livelli:

| Livello | Contenuto | Esempio |
|---------|-----------|---------|
| **Registro globale** | Indice consolidato di tutte le tecnologie | `LUTNDR-GLOBAL-INDEX.yaml` |
| **Registro di capitolo** | Tecnologie di un singolo capitolo UTA | `LUT_REGISTER.yaml` in `LC08_CONFIGURATION` |
| **Record individuale** | Singola tecnologia con stato, DPP, lineage | Record YAML nel registro di capitolo |

### 2.3 Relazione con i nodi foglia

Ogni nodo foglia della struttura OPT-INS ospita il proprio registro di capitolo:

```
<nodo-foglia>/
├── SSOT/
│   ├── LC08_CONFIGURATION/
│   │   └── LUT_REGISTER.yaml      ← Registro tecnologie del capitolo
│   └── LC14_RETIREMENT_CIRCULARITY/
│       ├── LUT_CIRCULARITY.yaml    ← Piano di circolarità
│       ├── DPP_RECORDS/            ← Passaporti digitali
│       └── SBOM/                   ← Bill of Materials
└── PUB/AMM/CSDB/DM/
    └── DMC-...-LUTNDR-*.xml       ← Data Module LUTNDR pubblicato
```

---

## 3. CLASSIFICAZIONE DEGLI STATI TECNOLOGICI

### 3.1 Stati primari

| Stato | Codice | Colore | Descrizione |
|-------|--------|--------|-------------|
| **In Uso** | `USO` | 🟢 Verde | Tecnologia attiva in produzione, operazione o manutenzione |
| **Disuso** | `DIS` | 🟠 Arancione | Tecnologia deprecata, in fase di sostituzione progressiva |
| **Nuova Progettazione** | `NPR` | 🔵 Blu | Tecnologia in fase di progettazione, prototipazione o qualifica |
| **Riassetti (RICICLATI)** | `RIC` | 🟣 Viola | Tecnologia ritirata e trasformata per riutilizzo circolare |

### 3.2 Sotto-stati

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

### 3.3 Matrice delle transizioni

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

## 4. GRAMMATICA IDENTIFICATIVA

### 4.1 Codice del record tecnologico

```
LUTNDR-UTA-DDD-SS-ss-Tnnn
  │     │   │   │  │  │
  │     │   │   │  │  └── Numero sequenziale (001–999)
  │     │   │   │  └───── Soggetto (00–99)
  │     │   │   └──────── Sezione (00–99)
  │     │   └──────────── Capitolo UTA (000–999)
  │     └──────────────── Prefisso sistema
  └────────────────────── Prefisso LUTNDR
```

**Esempio:** `LUTNDR-UTA-028-10-00-T001` — prima tecnologia registrata nel capitolo 028 (Fuel), sezione 10, soggetto 00.

### 4.2 Codici collegati

| Tipo | Formato | Esempio |
|------|---------|---------|
| Record LUT | `LUTNDR-UTA-DDD-SS-ss-Tnnn` | `LUTNDR-UTA-028-10-00-T001` |
| DPP | `DPP-UTA-DDD-SS-ss-Tnnn` | `DPP-UTA-028-10-00-T001` |
| ECO di transizione | `ECO-YYYY-nnnn` | `ECO-2026-0028` |
| KNOT associato | `KNOT-UTA-DDD-SS-ss-nnn` | `KNOT-UTA-028-10-00-001` |
| DM pubblicato | `DMC-GQAOA-A-DDD-SS-ss-nn-LUT-nnnA-D` | `DMC-GQAOA-A-028-10-00-00-LUT-001A-D` |

### 4.3 Classi tecnologiche

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

## 5. SCHEMA DEL RECORD TECNOLOGICO

### 5.1 Struttura completa

Ogni tecnologia nel LUT è identificata da un record univoco:

```yaml
# LUTNDR Record — Esempio
lutndr_id: "LUTNDR-UTA-028-10-00-T001"
uta_chapter: "028"
uta_node: "UTA-028-10-00-00"
technology_name: "Sistema di Alimentazione a Idrogeno Liquido (LH₂)"
technology_class: "SUBSYSTEM"
current_state: "USO"
current_substate: "USO-OPR"
era: "I"
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
traceability:
  alice_ref: "ALICE-028-LH2-SYS-001"
  bob_dt_ref: "BOB-DT-028-LH2-SYS-001"
  charlie_t_ref: "CHARLIE-T-028-LH2-SYS-001"
circularity:
  recyclability_index: 0.87
  reuse_potential: "HIGH"
  hazardous_materials: false
  sbom_ref: "SBOM-028-LH2-001"
transition_history:
  - from: "NPR"
    to: "USO"
    date: "2026-03-20"
    eco: "ECO-2026-0028"
    gate: "G5"
    authority: "CCB"
```

### 5.2 Campi obbligatori

| Campo | Tipo | Descrizione |
|-------|------|-------------|
| `lutndr_id` | string | Identificativo univoco nel formato LUTNDR |
| `uta_chapter` | string | Capitolo UTA di appartenenza |
| `technology_name` | string | Nome descrittivo della tecnologia |
| `technology_class` | enum | Classe tecnologica (§4.3) |
| `current_state` | enum | Stato primario corrente (USO/DIS/NPR/RIC) |
| `current_substate` | enum | Sotto-stato corrente (§3.2) |
| `era` | enum | Era corrente (I/II/III/IV) |
| `lifecycle_phase` | string | Fase LC corrente (LC01–LC14) |
| `first_registered` | date | Data di prima registrazione nel LUT |
| `dpp_hash` | string | Hash SHA-256 del DPP corrente |

---

## 6. GOVERNANCE DELLE TRANSIZIONI

### 6.1 Autorità

| Transizione | Autorità decisionale | Approvazione |
|-------------|---------------------|-------------|
| NPR → USO | Comitato Tecnico di Programma | CCB + Autorità di Certificazione |
| USO → DIS | Q-DATAGOV + Proprietario del Capitolo | CCB |
| DIS → RIC | Responsabile Circolarità + Q-DATAGOV | CCB + Responsabile Ambientale |
| RIC → NPR | Architetto di Sistema | CCB |
| RIC → USO | Comitato Tecnico + Responsabile Qualità | CCB |

### 6.2 Processo di transizione

```
1. PROPOSTA        →  ECO (Engineering Change Order) con giustificazione
2. VALUTAZIONE     →  Impatto su programmi, costi, sicurezza, circolarità
3. APPROVAZIONE    →  CCB vota, DPP aggiornato
4. ESECUZIONE      →  Transizione registrata nel LUTNDR, KNOT aggiornati
5. VERIFICA        →  Stato post-transizione verificato, TT distribuiti
```

### 6.3 Vincoli di integrità

- Nessuna tecnologia può essere in due stati primari simultaneamente
- Ogni transizione deve avere un ECO tracciabile
- Il DPP deve essere aggiornato **prima** della transizione effettiva
- La catena di tracciabilità (ALICE → BOOST) deve essere coerente in tutti gli stati

---

## 7. INTEGRAZIONE CON SSOT E CICLO DI VITA

### 7.1 Posizionamento nel nodo foglia

Il registro LUTNDR si materializza all'interno della struttura SSOT di ogni nodo foglia:

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
    └── DMC-...-LUTNDR-*.xml  ← Data Module LUTNDR pubblicato
```

### 7.2 Collegamento ai file LC01

Nel `KNOTS.csv`, ogni KNOT può dichiarare lo stato LUT corrente:

```csv
knot_id,title,type,status,priority,owner,created,lut_state,lut_substate
KNOT-UTA-028-10-00-001,LH₂ System Qualification,TECH,OPEN,HIGH,Propulsion-Lead,2026-01-15,NPR,NPR-QUA
```

### 7.3 Flusso LC14 → RIC

Quando un artefatto raggiunge LC14:

```
LC14 attivato
    │
    ├── 1. DPP completato e firmato
    ├── 2. SBOM estratto e verificato
    ├── 3. Indice di riciclabilità calcolato
    ├── 4. Piano di circolarità approvato (LUT_CIRCULARITY.yaml)
    ├── 5. Transizione DIS → RIC registrata nel LUTNDR
    └── 6. Sotto-stato RIC assegnato:
             RIC-SMO → RIC-VAL → {RIC-RIU | RIC-RCL | RIC-RPR}
```

---

## 8. TRACCIABILITÀ E PASSAPORTO DIGITALE (DPP)

### 8.1 Passaporto Digitale del Prodotto (DPP)

Ogni tecnologia nel LUTNDR genera un DPP conforme alla normativa EU per la circolarità:

```yaml
# DPP Record
dpp_id: "DPP-UTA-028-10-00-T001"
lutndr_ref: "LUTNDR-UTA-028-10-00-T001"
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

### 8.2 Catena di tracciabilità nel LUTNDR

```
ALICE (fisico)    →  Componente / sistema installato
BOB DT (gemello)  →  Modello digitale con stato LUTNDR
CHARLIE-T (agente)→  Monitoraggio stato e suggerimento transizioni
GENTLE (motore)   →  Generazione documentazione di transizione
BOOST (output)    →  Report di circolarità e DPP pubblicato
```

---

## 9. TOKENOMICS DELLA CIRCOLARITÀ

### 9.1 Incentivi TT per transizioni virtuose

| Azione | Ricompensa TT | Condizione |
|--------|----------:|-----------|
| Registrazione iniziale nel LUTNDR | 10 TT | Record completo e verificato |
| Transizione USO → DIS documentata | 25 TT | Piano di sostituzione approvato |
| Completamento DPP | 50 TT | DPP completo con SBOM e indice circolarità |
| Transizione DIS → RIC con piano | 75 TT | Piano di circolarità approvato |
| Riuso diretto (RIC-RIU) | 100 TT | Componente riutilizzato con evidenza |
| Riciclo materiale (RIC-RCL) | 80 TT | Materiale reintrodotto nella catena |
| Riprogettazione (RIC-RPR) | 150 TT | Nuovo KNOT aperto basato su esperienza operativa |
| Indice circolarità ≥ 0.90 | 50 TT bonus | Calcolato e verificato |

### 9.2 Pool dedicato

Dal pool TT complessivo di 2.000.000.000 TT (cfr. [SUPIA §9.1](./GQAOA-UTA-SUPIA-001.md#91-parametri-fondamentali)), il **2%** (40.000.000 TT) è riservato alla circolarità e distribuito attraverso il meccanismo LUTNDR.

---

## 10. FILE CANONICI

### 10.1 LUT_REGISTER.yaml

Posizione: `SSOT/LC08_CONFIGURATION/LUT_REGISTER.yaml`

```yaml
# LUT Register — Capitolo UTA-028
chapter: "028"
chapter_name: "Fuel"
last_updated: "2026-04-14"
technologies:
  - lutndr_id: "LUTNDR-UTA-028-10-00-T001"
    name: "LH₂ Fuel System"
    class: "SUBSYSTEM"
    state: "USO"
    substate: "USO-OPR"
    era: "I"
    programmes: ["AMPEL360-Q100"]
    lc_phase: "LC10"
    dpp_ref: "DPP-UTA-028-10-00-T001"

  - lutndr_id: "LUTNDR-UTA-028-10-00-T002"
    name: "Jet-A1 Fuel System (Legacy)"
    class: "SUBSYSTEM"
    state: "DIS"
    substate: "DIS-PLN"
    era: "II"
    programmes: []
    lc_phase: "LC14"
    dpp_ref: "DPP-UTA-028-10-00-T002"
    replacement: "LUTNDR-UTA-028-10-00-T001"
```

### 10.2 LUT_CIRCULARITY.yaml

Posizione: `SSOT/LC14_RETIREMENT_CIRCULARITY/LUT_CIRCULARITY.yaml`

```yaml
# Piano di Circolarità — Capitolo UTA-028
chapter: "028"
last_updated: "2026-04-14"
retired_technologies:
  - lutndr_id: "LUTNDR-UTA-028-10-00-T002"
    name: "Jet-A1 Fuel System (Legacy)"
    state: "RIC"
    substate: "RIC-VAL"
    era: "IV"
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

## 11. FLUSSO OPERATIVO

### 11.1 Ciclo completo

```
┌─────────────────────────────────────────────────────────────────┐
│                    LIBRO UNICO DELLE TECNOLOGIE                 │
│                              LUTNDR                             │
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

### 11.2 Metriche di circolarità

| Metrica | Formula | Target |
|---------|---------|--------|
| Indice di Circolarità | `IC = (massa_riusata + massa_riciclata) / massa_totale` | ≥ 0.85 |
| Tasso di Riuso | `TR = componenti_riusati / componenti_totali` | ≥ 0.30 |
| Risparmio CO₂ | `ΔCO₂ = CO₂_produzione_vergine − CO₂_circolare` | Positivo |
| Copertura DPP | `CDPP = tecnologie_con_DPP / tecnologie_totali` | 1.00 |
| Velocità di Transizione | `VT = tempo_medio_transizione` | ≤ 90 giorni |

---

## 12. ALLINEAMENTO NORMATIVO

| Norma | Ambito | Applicazione nel LUTNDR |
|-------|--------|------------------------|
| **EU Reg. 2024/1781** (Ecodesign) | Passaporto digitale del prodotto | DPP obbligatorio per ogni tecnologia |
| **EU Reg. 2023/1542** (Batterie) | Circolarità batterie | Sottostati RIC per celle energetiche |
| **ISO 14040/14044** | Valutazione del ciclo di vita (LCA) | Calcolo impronta carbonio |
| **ISO 14001** | Gestione ambientale | Gestione materiali pericolosi |
| **REACH** (EC 1907/2006) | Sostanze chimiche | Dichiarazione materiali nel DPP |
| **RoHS** (EU 2011/65) | Sostanze pericolose | Flag `hazardous_materials` |
| **S1000D** | Documentazione tecnica | Data Module LUTNDR in PUB/CSDB |
| **ASD-STE** | Linguaggio semplificato | Descrizioni in DM leggibili |
| **EN 9100** | Qualità aerospaziale | Gestione configurazione (LC08) |
| **ECSS-Q-ST-40** | Assicurazione prodotto spaziale | Tracciabilità componenti |

---

## 13. GLOSSARIO

### 13.1 Acronimi specifici LUTNDR

| Acronimo | Espansione | Definizione |
|----------|-----------|-------------|
| **LUTNDR** | Libro Unico delle Tecnologie: in uso, Nuova progettazione, Disuso, Riassetti | Registro centralizzato dello stato di tutte le tecnologie nelle quattro ere |
| **RICICLATI** | Registro Integrato delle Configurazioni Industriali per il Ciclo di vita, Lineage, Aggiornamento Tecnologico e Innovazione | Qualificatore del paradigma circolare |
| **DPP** | Digital Product Passport | Passaporto digitale del prodotto |
| **SBOM** | Software/Hardware Bill of Materials | Distinta componenti software e hardware |
| **ECO** | Engineering Change Order | Ordine di modifica ingegneristica |
| **IC** | Indice di Circolarità | Rapporto materiale circolare su totale |
| **LCA** | Life Cycle Assessment | Valutazione del ciclo di vita |

### 13.2 Termini specifici

| Termine | Definizione |
|---------|-------------|
| **Circolarità** | Principio per cui il ritiro di un artefatto fisico alimenta il riciclo o la ri-progettazione, generando valore rinnovato (LC14 → NPR/USO) |
| **Disuso** | Stato (Era II) in cui una tecnologia è deprecata e in fase di sostituzione progressiva, ma non ancora ritirata |
| **Era** | Ciascuna delle quattro fasi macroscopiche del ciclo tecnologico (I–IV) |
| **In Uso** | Stato (Era I) operativo attivo di una tecnologia in uno o più programmi |
| **Lineage** | Tracciabilità completa della storia di una tecnologia attraverso tutti gli stati e transizioni |
| **Nuova Progettazione** | Stato (Era III) di una tecnologia in fase di concezione, sviluppo, qualifica o industrializzazione |
| **Riassetti** | Riorganizzazione e trasformazione di una tecnologia ritirata per riuso, riciclo o riprogettazione |
| **RICICLATI** | L'insieme delle azioni di trasformazione circolare: smontaggio, valutazione, riuso, riciclo, riprogettazione |
| **Transizione** | Cambio di stato governato di una tecnologia nel LUTNDR, sempre tracciabile e approvato dal CCB |

---

*Fine del documento GQAOA-UTA-LUTNDR-001 v1.0*
