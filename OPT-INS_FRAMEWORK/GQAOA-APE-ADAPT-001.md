# AIDED PROMPT ENGINEERING TO AEROSPACE DIGITAL APPLICATIONS AND PROGRAMMING TECHNOLOGIES — USER INTERFACE STUDIO

**Acronimo:** APE ADAPT UI STUDIO  
**Codice:** GQAOA-APE-ADAPT-001  
**Versione:** 1.0  
**Autorità:** GQAOA .INC — GAIA QUANTUM AMPEL OPT-INS ARCHITECTURE  
**Architetto:** Amedeo Pelliccia  
**Data:** 2026-04-11  
**Stato:** Baseline attiva  
**Lingue operative:** IT (primaria) · EN · ES · DE · FR  
**UTA Capitoli:** DTCEC 320-10 (AI/ML per DT) · QCSAA 910-10 (Quantum AI) · QCSAA 970-10 (Agenza Sentiente)

---

> **Mission & Vision:** *Transforming aided prompt engineering into traceable aerospace digital applications and programming technologies, so that every engineering instruction reduces uncertainty, produces measurable artefacts, and rewards every contributor — one prompt, one artefact, one token at a time.*

> *"L'ingegnere non scrive prompt — progetta istruzioni ingegneristiche tracciabili."*  
> P(t) = KNOT → Prompt → KNU  
> dove il prompt è l'atto di definizione che fissa lo stato dell'artefatto.

### Funzione di trasformazione

```
APE  ──────────────►  ADAPT
Aided Prompt           Aerospace Digital Applications
Engineering            and Programming Technologies

       T: APE → ADAPT
       T(prompt) = KNU ∈ SSOT
       ∀ prompt ∈ APE: ∃! KNU ∈ ADAPT
       dove ADAPT = { artefatti tracciabili × domini UTA × fasi LC }
```

---

## INDICE

0. [Scopo e Campo di Applicazione](#0-scopo-e-campo-di-applicazione)
1. [Filosofia — Il Prompt come Atto Ingegneristico](#1-filosofia--il-prompt-come-atto-ingegneristico)
2. [Architettura del Sistema](#2-architettura-del-sistema)
3. [Anatomia di un Prompt Ingegneristico](#3-anatomia-di-un-prompt-ingegneristico)
4. [Catalogo dei Tipi di Prompt](#4-catalogo-dei-tipi-di-prompt)
5. [Pipeline CHARLIE-T → GENTLE → BOOST](#5-pipeline-charlie-t--gentle--boost)
6. [Interfaccia Utente — APE ADAPT Studio](#6-interfaccia-utente--ape-adapt-studio)
7. [Validazione e Qualità del Prompt](#7-validazione-e-qualità-del-prompt)
8. [Integrazione con SUPIA](#8-integrazione-con-supia)
9. [Template Library](#9-template-library)
10. [Governance e Tracciabilità](#10-governance-e-tracciabilità)
11. [Glossario APE ADAPT](#11-glossario-ape-adapt)

---

## 0. SCOPO E CAMPO DI APPLICAZIONE

### 0.1 Scopo

APE ADAPT UI STUDIO (Aided Prompt Engineering **to** Aerospace Digital **Applications** and Programming Technologies — User Interface Studio) è il **sistema di interfaccia umano-IA** per la creazione, validazione, esecuzione e tracciabilità di prompt ingegneristici entro l'architettura SUPIA/UTA.

La funzione di trasformazione **APE → ADAPT** converte ogni prompt ingegneristico strutturato in un artefatto digitale tracciabile (KNU), collocato nella tassonomia universale UTA (1000 capitoli), registrato nella SSOT, e ricompensato tramite Teknia Token.

APE ADAPT non è un chatbot né un assistente generico. È uno **studio di progettazione di istruzioni** in cui ogni prompt:

- È collegato a un KNOT (incertezza da risolvere)
- Produce un KNU (artefatto misurabile)
- È validato contro regole BREX
- È registrato nella catena di tracciabilità ALICE → BOB DT → CHARLIE-T → GENTLE → BOOST
- Genera ricompensa TT proporzionale all'impatto

### 0.2 Campo di applicazione

| Dimensione | Copertura |
|------------|-----------|
| Utenti | Ingegneri di sistema, progettisti, analisti, verificatori, manutentori |
| Domini UTA | Tutti i 10 domini (G1–G10), 1000 capitoli |
| Fasi LC | LC01–LC14 — ogni fase può generare e consumare prompt |
| Programmi | AMPEL360 Q100, GAIA-SPACE-LAUNCHER, SPACET Q10, futuri |
| Modelli IA | GENTLE (Generative Engineering Narrative Transforming Language Engine), BOOST (Bayesian-Optimized Output for Semantic Transformation) |

### 0.3 Documenti correlati

| Codice | Titolo |
|--------|--------|
| GQAOA-UTA-SUPIA-001 | Sistema Unico di Progettazione Industriale Avanzata |
| GQAOA-UTA-SUDDI-001 | Sistema Universale di Documentazione e Disegno Tecnico Industriale |
| GQAOA-OPT-INS-STD-1.1 | OPT-INS Framework Standard |
| GQAOA-ASIT-NIB-SPEC-001 | NeuronBit Information Specification |

---

## 1. FILOSOFIA — IL PROMPT COME ATTO INGEGNERISTICO

### 1.1 I cinque principi APE

| # | Principio | Enunciazione | Conseguenza |
|---|-----------|-------------|-------------|
| A1 | **Prompt = Definizione** | Un prompt ingegneristico non è una domanda — è un atto di definizione che fissa lo stato di un artefatto | Il prompt è registrato come KNU, non come chiacchierata |
| A2 | **Contesto Esplicito** | Ogni prompt porta con sé il suo contesto: capitolo UTA, asse OPT-INS, programma, fase LC, KNOT padre | Il modello non deve indovinare; il contesto è strutturato |
| A3 | **Output Tipizzato** | L'output atteso è dichiarato: tipo KNU, formato, criteri di accettazione, metodo di verifica | Nessun output ambiguo; ogni prodotto è classificabile |
| A4 | **Tracciabilità Integrale** | Ogni prompt e ogni risposta sono collegati alla catena di tracciabilità e al registro TT | Il prompt ha un ID, un proprietario, un timestamp, un hash |
| A5 | **Miglioramento Misurabile** | L'efficacia del prompt è misurata dalla riduzione di residuo sul KNOT padre | Il prompt engineering ha metriche, non opinioni |

### 1.2 Cosa NON è APE ADAPT

| APE ADAPT NON è… | APE ADAPT È… |
|-------------------|-------------|
| Un chatbot conversazionale | Uno studio di istruzioni ingegneristiche strutturate |
| Un editor di testo libero | Un compositore con template, vincoli e validazione |
| Un'interfaccia generica per LLM | Un'interfaccia specializzata per la catena CHARLIE-T → GENTLE → BOOST |
| Un sistema scollegato dalla baseline | Un nodo eseguibile nella tassonomia SUPIA |
| Un gioco di parole | Un atto che riduce incertezza e genera valore misurabile |

### 1.3 Il modello concettuale

```
┌─────────────────────────────────────────────────────────┐
│               APE ADAPT UI STUDIO                        │
│                                                          │
│   KNOT ──► PROMPT ──► MODELLO ──► KNU ──► VALIDAZIONE  │
│     │        │           │          │          │         │
│     │    contesto     pipeline   artefatto   BREX       │
│     │    strutturato  C→G→B      tipizzato  regole     │
│     │                                                    │
│     └──────────── TRACCIABILITÀ ──────────────────┘      │
│                         │                                │
│                    TT REWARD                             │
└─────────────────────────────────────────────────────────┘
```

---

## 2. ARCHITETTURA DEL SISTEMA

### 2.1 Vista a strati

```
┌─────────────────────────────────────────────────────────────────┐
│  STRATO 5 — PRESENTAZIONE                                       │
│  APE ADAPT UI Studio · React Components · Dashboard             │
│  Prompt Composer · Template Gallery · Validation Panel          │
├─────────────────────────────────────────────────────────────────┤
│  STRATO 4 — ORCHESTRAZIONE                                      │
│  Prompt Router · Context Injector · Pipeline Manager            │
│  CHARLIE-T Dispatcher · GENTLE Engine · BOOST Optimizer         │
├─────────────────────────────────────────────────────────────────┤
│  STRATO 3 — VALIDAZIONE                                         │
│  BREX Validator · Schema Checker · KNU Type Verifier            │
│  Quality Scorer · Residue Calculator                            │
├─────────────────────────────────────────────────────────────────┤
│  STRATO 2 — TRACCIABILITÀ                                       │
│  Prompt Registry · KNOT Linker · KNU Classifier                │
│  TT Calculator · Hash Chain                                     │
├─────────────────────────────────────────────────────────────────┤
│  STRATO 1 — DATI                                                │
│  SSOT/LC01–LC14 · PUB/CSDB · Template Library                  │
│  PROGRAMME_MANIFEST.yaml · CHAPTER_MANIFEST.yaml                │
├─────────────────────────────────────────────────────────────────┤
│  STRATO 0 — INFRASTRUTTURA                                      │
│  UTA 000–999 Registry · OPT-INS 6-Axis Grid                    │
│  SUPIA Backbone · S1000D CSDB                                   │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 Flusso di informazione

```
Utente                     APE ADAPT Studio                    SUPIA
  │                             │                                │
  │  1. Seleziona KNOT ────────►│                                │
  │                             │ 2. Carica contesto ───────────►│
  │  3. Compone prompt ────────►│    (UTA, LC, asse, programma)  │
  │                             │                                │
  │                             │ 4. Valida prompt               │
  │                             │    (struttura, completezza)     │
  │                             │                                │
  │                             │ 5. Invia a pipeline C→G→B      │
  │                             │                                │
  │  6. Riceve output ◄────────│                                │
  │                             │ 7. Classifica KNU              │
  │  8. Revisiona e approva ──►│                                │
  │                             │ 9. Registra in SSOT ──────────►│
  │                             │ 10. Calcola TT ──────────────►│
  │                             │                                │
  └─────────────────────────────┘                                │
```

---

## 3. ANATOMIA DI UN PROMPT INGEGNERISTICO

### 3.1 Struttura del prompt APE

Ogni prompt nel sistema APE ADAPT ha 7 sezioni obbligatorie:

```yaml
prompt:
  # ── IDENTITÀ ──
  id: "APE-2026-0142"
  knot_parent: "KNOT-UTA-028-10-00-001"
  author: "amedeo.pelliccia"
  timestamp: "2026-04-11T14:30:00Z"

  # ── CONTESTO ──
  context:
    uta_chapter: 028                    # Capitolo UTA
    uta_section: "028-10-00-00"         # Nodo specifico
    domain: "G1"                        # Dominio
    axis: "T"                           # Asse OPT-INS
    programme: "AMPEL360-Q100"          # Programma
    lc_phase: "LC04"                    # Fase del ciclo di vita
    language: "IT"                      # Lingua dell'output

  # ── ISTRUZIONE ──
  instruction:
    action: "genera"                    # Verbo: genera, analizza, verifica, confronta, sintetizza
    knu_type: "REQ"                     # Tipo KNU atteso
    description: >
      Genera i requisiti funzionali per il sistema di distribuzione
      carburante del serbatoio ala-fusoliera (BWB), considerando:
      - Pressione operativa nominale 3.5 bar
      - Temperatura -40°C a +85°C
      - Doppia ridondanza su ogni linea critica
      - Compatibilità con idrogeno liquido LH₂

  # ── VINCOLI ──
  constraints:
    standards: ["EASA CS-25.952", "EASA CS-25.963", "SAE ARP4754A"]
    format: "tabella requisiti con ID, descrizione, razionale, MoC, priorità"
    max_items: 20
    traceability: "collegare a KNOT-UTA-028-10-00-001"

  # ── CRITERI DI ACCETTAZIONE ──
  acceptance:
    completeness: "tutti i sotto-sistemi coperti"
    verifiability: "ogni requisito ha metodo di verifica definito"
    traceability: "ogni requisito collegato a KNOT e a sotto-requisito"
    residue_target: 30   # Riduzione residuo attesa (da 80 a ≤30)

  # ── PIPELINE ──
  pipeline:
    model: "GENTLE"                     # Modello primario
    boost: true                         # Applicare ottimizzazione BOOST
    validation: "BREX-G1-028"           # Set di regole BREX applicabile

  # ── HASH ──
  hash: "sha256:a1b2c3d4..."            # Hash del prompt per integrità
```

### 3.2 I verbi APE

| Verbo | Azione | KNU tipico | Fase LC tipica |
|-------|--------|-----------|----------------|
| `genera` | Crea un artefatto nuovo | REQ, ICD, ANA, DWG, SIM | LC02, LC04, LC05 |
| `analizza` | Esamina un artefatto esistente | ANA, SAF | LC03, LC05 |
| `verifica` | Controlla conformità a criteri | TEST, SAF | LC06 |
| `confronta` | Compara due o più artefatti | ANA, CM | LC05, LC08 |
| `sintetizza` | Consolida informazioni da più fonti | PUB, REQ | LC02, LC07 |
| `trasforma` | Converte un artefatto in formato diverso | PUB, DWG | LC04, PUB |
| `ottimizza` | Migliora un artefatto esistente | ANA, SIM | LC05, LC09 |
| `documenta` | Produce documentazione S1000D | PUB, DM | PUB |
| `revisiona` | Rileva errori o lacune | SAF, CM | LC06, LC08 |
| `predice` | Stima comportamento futuro | SIM, ANA | LC05, LC11 |

### 3.3 Il punteggio di qualità del prompt (PQS)

Ogni prompt riceve un punteggio di qualità da 0 a 100:

| Dimensione | Peso | Criteri |
|-----------|:----:|---------|
| **Specificità** | 25% | Il prompt è specifico al nodo UTA, non generico |
| **Contesto** | 20% | Tutti i campi del contesto sono compilati correttamente |
| **Vincoli** | 20% | Standard, formato, tracciabilità dichiarati |
| **Verificabilità** | 20% | Criteri di accettazione chiari e misurabili |
| **Tracciabilità** | 15% | Collegamento a KNOT, KNU plan, pipeline |

```
PQS = 0.25·S + 0.20·C + 0.20·V + 0.20·A + 0.15·T
```

| PQS | Classificazione | Azione |
|:---:|----------------|--------|
| 90–100 | ✅ Eccellente | Esecuzione immediata |
| 70–89 | 🟡 Buono | Esecuzione con note |
| 50–69 | 🟠 Sufficiente | Richiede miglioramento |
| 0–49 | 🔴 Insufficiente | Rifiutato — riscrivere |

---

## 4. CATALOGO DEI TIPI DI PROMPT

### 4.1 Per fase del ciclo di vita

| Fase | Tipo di prompt | Template ID | Descrizione |
|------|---------------|-------------|-------------|
| LC01 | Dichiarazione KNOT | `TPL-LC01-KNOT` | Registrazione strutturata di un'incertezza |
| LC02 | Generazione requisiti | `TPL-LC02-REQ` | Produzione requisiti da KNOT con tracciabilità |
| LC02 | Analisi requisiti | `TPL-LC02-ANA` | Esame completezza/coerenza di un set di requisiti |
| LC03 | FMEA/FTA | `TPL-LC03-SAF` | Analisi sicurezza per un sistema/sotto-sistema |
| LC04 | Specifica di progetto | `TPL-LC04-ICD` | Documento di controllo interfaccia |
| LC04 | Generazione disegno | `TPL-LC04-DWG` | Istruzioni per disegno tecnico (cartiglio SUPIA) |
| LC05 | Trade study | `TPL-LC05-ANA` | Confronto multi-criterio tra alternative |
| LC06 | Piano di verifica | `TPL-LC06-TEST` | Procedura di prova con criteri pass/fail |
| LC07 | Rapporto validazione | `TPL-LC07-VAL` | Sintesi evidenze di validazione |
| LC08 | Baseline delta | `TPL-LC08-CM` | Analisi impatto di una modifica di configurazione |
| LC09 | Specifica di fabbricazione | `TPL-LC09-MFG` | Istruzioni per processo produttivo |
| LC10 | Procedura operativa | `TPL-LC10-OPS` | Procedura operativa standard |
| LC11 | Task card manutenzione | `TPL-LC11-MNT` | Istruzione di manutenzione con intervalli |
| LC12 | Bollettino di servizio | `TPL-LC12-SB` | Comunicazione post-consegna |
| LC13 | Modulo formativo | `TPL-LC13-TRN` | Contenuto didattico strutturato |
| LC14 | Piano di circolarità | `TPL-LC14-EOL` | Fine vita, riciclaggio, DPP |
| PUB | Data Module S1000D | `TPL-PUB-DM` | Generazione DM in formato S1000D XML |

### 4.2 Per dominio

Ogni dominio G1–G10 ha template specializzati che pre-compilano i vincoli normativi applicabili:

| Dominio | Template specializzati | Standard pre-caricati |
|---------|----------------------|----------------------|
| G1 ATA | Aeronavigabilità, sistemi di bordo | EASA CS-25, DO-178C, DO-160 |
| G2 STA | Spaziali, missione, orbita | ECSS-E-ST-10, ECSS-Q-ST-80 |
| G3 DTTA | Difesa, C4ISR, autonomia | MIL-STD-882, MIL-STD-881 |
| G4 DTCEC | Gemelli digitali, cloud, IA | ISO 27001, IEEE 7010 |
| G5 EPTA | Energia, propulsione, H₂ | ISO 14687, EASA SC per H₂ |
| G6 AMTA | Materiali, nano, bio | ISO 14040, REACH |
| G7 OGATA | Automazione, robotica | ISO 10218, IEC 62443 |
| G8 ACV | UAM, vertipuertos | EASA SC-VTOL, SESAR U-space |
| G9 CYB | Sicurezza cibernetica | ISO 27001, NIST CSF, IEC 62443 |
| G10 QCSAA | Quantistica, agenza | IEEE 7010, QASHT protocol |

---

## 5. PIPELINE CHARLIE-T → GENTLE → BOOST

### 5.1 Ruoli nella pipeline

```
┌────────────────────────────────────────────────────────────────┐
│                                                                 │
│   UTENTE                                                        │
│     │                                                           │
│     ▼                                                           │
│   CHARLIE-T (Agente Digitale Contestuale)                      │
│     │  - Riceve il prompt strutturato APE                       │
│     │  - Inietta il contesto UTA/OPT-INS/LC/Programma          │
│     │  - Seleziona il template appropriato                      │
│     │  - Prepara il payload per GENTLE                          │
│     ▼                                                           │
│   GENTLE (Generative Engineering Narrative Transforming         │
│           Language Engine)                                       │
│     │  - Esegue la generazione dell'artefatto                   │
│     │  - Applica le regole di dominio e gli standard            │
│     │  - Produce il KNU grezzo                                  │
│     │  - Dichiara .YieldedAML                                   │
│     ▼                                                           │
│   BOOST (Bayesian-Optimized Output for Semantic                │
│          Transformation)                                        │
│     │  - Ottimizza l'output per precisione e coerenza           │
│     │  - Verifica contro BREX                                   │
│     │  - Calcola il punteggio di qualità                        │
│     │  - Formatta il KNU finale                                 │
│     ▼                                                           │
│   VALIDAZIONE → REGISTRAZIONE → TT REWARD                      │
│                                                                 │
└────────────────────────────────────────────────────────────────┘
```

### 5.2 Flusso dati

| Passo | Input | Output | Responsabile |
|:-----:|-------|--------|-------------|
| 1 | KNOT aperto | Prompt APE strutturato | Utente via Studio |
| 2 | Prompt APE | Prompt arricchito + contesto | CHARLIE-T |
| 3 | Prompt arricchito | KNU grezzo | GENTLE |
| 4 | KNU grezzo | KNU ottimizzato + PQS | BOOST |
| 5 | KNU ottimizzato | KNU validato + hash | Validatore BREX |
| 6 | KNU validato | Registrazione SSOT + TT | Sistema SUPIA |

### 5.3 Ciclo di feedback

```
                    ┌──────────────────┐
                    │  Prompt APE      │
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
                    │  C → G → B       │
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
             ┌──────│  KNU prodotto    │
             │      └────────┬─────────┘
             │               │
             │      ┌────────▼─────────┐
             │      │  Validazione     │──── PQS < 70 ──┐
             │      └────────┬─────────┘                │
             │               │                          │
             │          PQS ≥ 70                        │
             │               │                          │
             │      ┌────────▼─────────┐       ┌───────▼────────┐
             │      │  Registrazione   │       │  Feedback al   │
             │      │  SSOT + TT       │       │  prompt (loop) │
             │      └──────────────────┘       └───────┬────────┘
             │                                         │
             └────── metriche per ─────────────────────┘
                     miglioramento
                     prompt
```

---

## 6. INTERFACCIA UTENTE — APE ADAPT STUDIO

### 6.1 Layout dello studio

```
┌──────────────────────────────────────────────────────────────────┐
│  APE ADAPT UI STUDIO                               [⚙️] [👤]   │
├───────────┬──────────────────────────────────────┬───────────────┤
│           │                                      │               │
│  NAVIGA   │         WORKSPACE                    │   PANNELLO    │
│  TORE     │                                      │   CONTESTO    │
│           │  ┌──────────────────────────────┐    │               │
│  📁 KNOT  │  │     PROMPT COMPOSER           │    │  UTA: 028    │
│  📁 KNU   │  │                               │    │  Asse: T     │
│  📁 Template│  │  [Contesto] [Istruzione]    │    │  Prog: Q100  │
│  📁 Cronol│  │  [Vincoli]  [Accettazione]   │    │  LC: LC04    │
│           │  │  [Pipeline] [Anteprima]       │    │  KNOT: 001   │
│  ─────── │  │                               │    │              │
│  FILTRI   │  └──────────────────────────────┘    │  Residuo: 80 │
│           │                                      │  Target: ≤30  │
│  G1–G10   │  ┌──────────────────────────────┐    │              │
│  O P T I  │  │     OUTPUT / KNU              │    │  ─────────  │
│  N S      │  │                               │    │  STANDARD    │
│  LC01–14  │  │  [Artefatto generato]         │    │  CS-25.952  │
│  Q100     │  │  [PQS: 87 🟡]                │    │  CS-25.963  │
│  GAIA     │  │  [Validazione BREX: ✅]       │    │  ARP4754A   │
│  SPACET   │  │                               │    │              │
│           │  └──────────────────────────────┘    │  ─────────  │
│           │                                      │  CATENA      │
│           │  ┌──────────────────────────────┐    │  ALICE       │
│           │  │     METRICHE                  │    │  BOB DT      │
│           │  │  PQS: 87  Residuo: 80→28     │    │  CHARLIE-T   │
│           │  │  TT: 142.5  Feedback: 3/5    │    │  GENTLE      │
│           │  └──────────────────────────────┘    │  BOOST       │
│           │                                      │              │
├───────────┴──────────────────────────────────────┴───────────────┤
│  Status: Connesso · GENTLE v2.1 · BREX-G1 caricato · TT pool: 400M │
└──────────────────────────────────────────────────────────────────┘
```

### 6.2 Moduli dell'interfaccia

| Modulo | Funzione | Interazione |
|--------|----------|-------------|
| **Navigatore** | Albero dei KNOT aperti, KNU prodotti, template disponibili | Click per selezionare; filtri per dominio/asse/LC/programma |
| **Prompt Composer** | Editor strutturato con 7 sezioni del prompt APE | Tab per sezione; auto-completamento; validazione in tempo reale |
| **Output Viewer** | Visualizzazione dell'artefatto KNU prodotto | Syntax highlighting; confronto versioni; export |
| **Pannello Contesto** | Informazioni contestuali del nodo UTA selezionato | Auto-popolato dal KNOT; modificabile |
| **Metriche** | PQS, riduzione residuo, TT guadagnati, cronologia | Aggiornamento in tempo reale dopo ogni esecuzione |
| **Template Gallery** | Catalogo template per fase/dominio | Ricerca; anteprima; clona e personalizza |

### 6.3 Modalità operative

| Modalità | Descrizione | Utente tipico |
|----------|-------------|---------------|
| **Guidata** | Il sistema guida l'utente passo-passo nella compilazione del prompt | Utenti nuovi |
| **Esperta** | Editor YAML diretto con validazione in tempo reale | Ingegneri esperti |
| **Batch** | Esecuzione di più prompt in sequenza da un piano KNU | Automazione CI/CD |
| **Revisione** | Visualizzazione e approvazione di KNU prodotti | Revisori, CCB |

---

## 7. VALIDAZIONE E QUALITÀ DEL PROMPT

### 7.1 Regole di validazione

| Livello | Regola | Descrizione |
|---------|--------|-------------|
| **L1 Struttura** | Tutti i 7 campi obbligatori presenti | Il prompt non può essere inviato senza struttura completa |
| **L2 Contesto** | Il nodo UTA esiste nel registro | Capitolo, sezione, asse validati contro UTA 000–999 |
| **L3 Coerenza** | Il tipo KNU è coerente con la fase LC | Non si può generare un TEST in LC02 |
| **L4 Standard** | Gli standard dichiarati esistono e sono applicabili | Verifica contro il registro normativo del dominio |
| **L5 BREX** | L'output rispetta le regole BREX del progetto | Validazione XML per DM S1000D |

### 7.2 Anti-pattern del prompt

| Anti-pattern | Esempio | Problema | Soluzione |
|-------------|---------|----------|-----------|
| **Vago** | "Fammi i requisiti del sistema" | Nessun contesto, nessun vincolo | Usare template `TPL-LC02-REQ` con nodo UTA specifico |
| **Sconnesso** | Prompt senza KNOT padre | Artefatto orfano, non tracciabile | Collegare sempre a un KNOT aperto |
| **Sovraccarico** | Un prompt che chiede 5 tipi di KNU diversi | Output disperso, non classificabile | Un prompt = un tipo KNU |
| **Non verificabile** | "Fai qualcosa di buono" | Nessun criterio di accettazione | Dichiarare criteri misurabili |
| **Senza standard** | Prompt senza riferimento normativo | Output non certificabile | Dichiarare standard applicabili |

### 7.3 Metriche di efficacia del prompt engineering

| Metrica | Formula | Target |
|---------|---------|--------|
| **PQS medio** | Σ PQS_i / n | ≥ 80 |
| **Tasso di prima accettazione** | KNU accettati al primo tentativo / KNU totali | ≥ 70% |
| **Riduzione residuo media** | Σ ΔR_i / n | ≥ 40 punti |
| **Cicli di feedback** | Numero medio di iterazioni per KNU accettato | ≤ 2 |
| **Copertura KNOT** | KNOT con almeno un KNU prodotto / KNOT totali | ≥ 90% |

---

## 8. INTEGRAZIONE CON SUPIA

### 8.1 Punti di integrazione

```
SUPIA                          APE ADAPT
─────                          ──────────
SSOT/LC01/KNOTS.csv  ◄──────►  Navigatore KNOT
SSOT/LC01/KNU_PLAN.csv ◄────►  Template selector
SSOT/LCxx/             ◄────►  Output KNU destination
PUB/CSDB/DM/           ◄────►  DM generator
CHAPTER_MANIFEST.yaml  ◄────►  Contesto auto-loader
TOKENOMICS_TT.yaml    ◄────►  TT reward calculator
AWARDS_TT.csv          ◄────►  TT distribution
PROGRAMME_MANIFEST.yaml ◄───►  Programme filter
```

### 8.2 Posizionamento nell'architettura a 6 livelli SUPIA

| Livello SUPIA | Ruolo di APE ADAPT |
|--------------|-------------------|
| L6 Registro | Registra prompt e KNU nel ledger TT |
| L5 Pubblicazione | Genera DM S1000D via template PUB |
| L4 V&V | Valida KNU contro BREX e criteri |
| L3 Evidenze | Produce artefatti LC02–LC14 |
| L2 Incertezza | Si collega ai KNOT e calcola riduzione residuo |
| L1 Tassonomia | Usa la grammatica UTA per navigazione e contesto |
| L0 Ontologia | Opera sopra il livello ontologico NeuronBit |

### 8.3 File APE generati

Per ogni prompt eseguito, APE ADAPT genera:

```
SSOT/LC01_PROBLEM_STATEMENT/
├── APE_PROMPTS/                       ← Nuovo: registro prompt
│   ├── APE-2026-0142.yaml             ← Prompt strutturato
│   ├── APE-2026-0142-output.md        ← KNU grezzo
│   ├── APE-2026-0142-validated.md     ← KNU validato
│   └── APE-2026-0142-metrics.json     ← PQS, residuo, TT
```

---

## 9. TEMPLATE LIBRARY

### 9.1 Struttura di un template

```yaml
template:
  id: "TPL-LC02-REQ"
  name: "Generazione Requisiti da KNOT"
  version: "1.0"
  domain: ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "G10"]
  lc_phase: "LC02"
  knu_type: "REQ"

  # Contesto pre-compilato
  context_defaults:
    action: "genera"
    format: "tabella requisiti con ID, descrizione, razionale, MoC, priorità"
    traceability: "collegare a KNOT padre"

  # Istruzione parametrizzata
  instruction_template: >
    Genera i requisiti {req_type} per il sistema {system_name}
    nel contesto del capitolo UTA-{chapter}, considerando:
    {considerations}

  # Parametri da compilare
  parameters:
    - name: "req_type"
      type: "enum"
      options: ["funzionali", "prestazionali", "di interfaccia", "di sicurezza", "ambientali"]
    - name: "system_name"
      type: "text"
      description: "Nome del sistema o sotto-sistema"
    - name: "chapter"
      type: "uta_chapter"
      description: "Capitolo UTA (000–999)"
    - name: "considerations"
      type: "multiline"
      description: "Condizioni, vincoli, parametri specifici"

  # Standard suggeriti per dominio
  suggested_standards:
    G1: ["EASA CS-25", "SAE ARP4754A", "DO-178C"]
    G2: ["ECSS-E-ST-10", "NASA STD 8739.8"]
    G5: ["ISO 14687", "EASA SC per H₂"]

  # Criteri di accettazione pre-compilati
  default_acceptance:
    completeness: "tutti i sotto-sistemi coperti"
    verifiability: "ogni requisito ha metodo di verifica definito"
```

### 9.2 Catalogo template di base

| ID | Nome | Fase | Tipo KNU | Dominio |
|----|------|------|----------|---------|
| `TPL-LC01-KNOT` | Dichiarazione KNOT | LC01 | KNOT | Tutti |
| `TPL-LC02-REQ` | Generazione Requisiti | LC02 | REQ | Tutti |
| `TPL-LC02-TRACE` | Matrice di Tracciabilità | LC02 | REQ | Tutti |
| `TPL-LC03-FMEA` | Analisi FMEA | LC03 | SAF | Tutti |
| `TPL-LC03-FTA` | Analisi FTA | LC03 | SAF | Tutti |
| `TPL-LC03-HAZARD` | Registro Pericoli | LC03 | SAF | Tutti |
| `TPL-LC04-ICD` | Interfaccia Controllo | LC04 | ICD | Tutti |
| `TPL-LC04-DWG-CART` | Disegno con Cartiglio | LC04 | DWG | Tutti |
| `TPL-LC04-ARCH` | Specifica Architettura | LC04 | ICD | Tutti |
| `TPL-LC05-TRADE` | Trade Study | LC05 | ANA | Tutti |
| `TPL-LC05-FEA` | Analisi FEA | LC05 | ANA | G1, G2, G5 |
| `TPL-LC05-CFD` | Analisi CFD | LC05 | ANA | G1, G2, G5 |
| `TPL-LC06-TEST` | Piano di Prova | LC06 | TEST | Tutti |
| `TPL-LC07-REPORT` | Rapporto Validazione | LC07 | TEST | Tutti |
| `TPL-LC08-DELTA` | Analisi Impatto Modifica | LC08 | CM | Tutti |
| `TPL-LC09-MFG` | Specifica Produzione | LC09 | CM | G1, G6, G7 |
| `TPL-LC10-OPS` | Procedura Operativa | LC10 | PUB | Tutti |
| `TPL-LC11-TASK` | Task Card Manutenzione | LC11 | PUB | G1, G2 |
| `TPL-LC12-SB` | Bollettino di Servizio | LC12 | PUB | G1, G2 |
| `TPL-LC13-CBT` | Modulo Formativo | LC13 | PUB | Tutti |
| `TPL-LC14-DPP` | Passaporto Digitale | LC14 | DPP | Tutti |
| `TPL-PUB-DM-DESC` | DM Descrittivo S1000D | PUB | PUB | Tutti |
| `TPL-PUB-DM-PROC` | DM Procedurale S1000D | PUB | PUB | Tutti |
| `TPL-PUB-DM-FI` | DM Fault Isolation | PUB | PUB | Tutti |
| `TPL-PUB-DM-IPD` | DM Illustrated Parts | PUB | PUB | Tutti |

---

## 10. GOVERNANCE E TRACCIABILITÀ

### 10.1 Ruoli nel sistema APE ADAPT

| Ruolo | Responsabilità | Permessi |
|-------|---------------|----------|
| **Prompt Author** | Crea e sottomette prompt strutturati | Creare, eseguire, visualizzare |
| **KNU Reviewer** | Revisiona e approva KNU prodotti | Visualizzare, approvare, rigettare |
| **Template Curator** | Gestisce il catalogo template | Creare/modificare template |
| **APE Administrator** | Gestisce il sistema, le pipeline, le metriche | Tutti i permessi |
| **KNOT Owner** | Responsabile della chiusura del KNOT | Approvare chiusura, distribuire TT |

### 10.2 Registro dei prompt

Ogni prompt eseguito è registrato nel file `APE_REGISTRY.csv`:

```csv
prompt_id,timestamp,author,knot_parent,uta_chapter,axis,programme,lc_phase,knu_type,pqs,residue_before,residue_after,tt_awarded,status,hash
APE-2026-0142,2026-04-11T14:30:00Z,amedeo.pelliccia,KNOT-UTA-028-10-00-001,028,T,AMPEL360-Q100,LC04,REQ,87,80,28,142.5,ACCEPTED,sha256:a1b2c3d4
```

### 10.3 Dichiarazione .YieldedAML per KNU generati da APE

Ogni KNU prodotto tramite APE ADAPT porta il front-matter esteso:

```yaml
---
.YieldedAlgorithmicMachineLearning: true
Last.MarkedDown: "2026-04-11T14:32:00Z"
model: "GENTLE-v2.1"
boost_applied: true
boost_model: "BOOST-v1.3"
prompt_id: "APE-2026-0142"
knot_parent: "KNOT-UTA-028-10-00-001"
pqs: 87
human_author: "Amedeo Pelliccia"
review_status: "human_reviewed"
ape_version: "1.0"
---
```

---

## 11. GLOSSARIO APE ADAPT

### 11.1 Acronimi

| Acronimo | Espansione | Definizione |
|----------|-----------|-------------|
| **ADAPT** | Aerospace Digital Applications and Programming Technologies | Tecnologie di applicazioni e programmazione digitale aerospaziale |
| **APE** | Aided Prompt Engineering | Ingegneria assistita dei prompt |
| **BOOST** | Bayesian-Optimized Output for Semantic Transformation | Ottimizzazione bayesiana dell'output per trasformazione semantica (5° livello della catena) |
| **BREX** | Business Rules Exchange | Regole di validazione S1000D |
| **C→G→B** | CHARLIE-T → GENTLE → BOOST | Pipeline di elaborazione del prompt |
| **CHARLIE-T** | — | Agente digitale contestuale (3° livello della catena di tracciabilità) |
| **GENTLE** | Generative Engineering Narrative Transforming Language Engine | Motore generativo per narrativa ingegneristica (4° livello della catena) |
| **KNOT** | Knowledge Nexus of Openness and Traceability | Nodo di incertezza aperta |
| **KNU** | Knowledge Nexus Unit | Unità conoscitiva — artefatto prodotto per ridurre un KNOT |
| **PQS** | Prompt Quality Score | Punteggio di qualità del prompt (0–100) |
| **SSOT** | Single Source of Truth | Unica sorgente di verità |
| **SUPIA** | Sistema Unico di Progettazione Industriale Avanzata | Sistema di progettazione a 1000 capitoli |
| **TPL** | Template | Modello pre-compilato di prompt |
| **TT** | Teknia Token | Token di ricompensa per contributi ingegneristici |
| **UTA** | Universal Technology Architecture | Architettura tecnologica universale (10 domini, 1000 capitoli) |

### 11.2 Termini

| Termine | Definizione |
|---------|-------------|
| **Prompt ingegneristico** | Istruzione strutturata con contesto UTA, vincoli normativi, criteri di accettazione e collegamento a KNOT — non una domanda generica |
| **Prompt Composer** | Modulo dell'interfaccia APE ADAPT per la creazione guidata di prompt strutturati |
| **Pipeline C→G→B** | Sequenza di elaborazione: CHARLIE-T (contesto) → GENTLE (generazione) → BOOST (ottimizzazione) |
| **Template Gallery** | Catalogo di template parametrizzati per tipo di prompt, organizzati per fase LC e dominio |
| **Ciclo di feedback** | Iterazione tra prompt e output fino al raggiungimento del PQS e della riduzione di residuo target |
| **Prompt Quality Score (PQS)** | Punteggio composito (0–100) basato su specificità, contesto, vincoli, verificabilità e tracciabilità |
| **Anti-pattern** | Schema di prompt noto per produrre risultati scadenti, da evitare |
| **Verbo APE** | Azione dichiarata nel prompt: genera, analizza, verifica, confronta, sintetizza, trasforma, ottimizza, documenta, revisiona, predice |
| **Modalità guidata** | Modo operativo in cui il sistema guida l'utente passo-passo nella compilazione del prompt |
| **Modalità esperta** | Modo operativo in cui l'utente scrive direttamente il YAML del prompt con validazione in tempo reale |
| **Modalità batch** | Modo operativo per esecuzione automatica di più prompt in sequenza |

---

## FIRMA

```
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│  AIDED PROMPT ENGINEERING TO AEROSPACE DIGITAL                   │
│  APPLICATIONS AND PROGRAMMING TECHNOLOGIES                       │
│  USER INTERFACE STUDIO                                           │
│  APE ADAPT UI STUDIO v1.0                                        │
│                                                                  │
│  Emesso da:    Amedeo Pelliccia                                  │
│  Organizzazione: GQAOA .INC                                     │
│  Data:         2026-04-11                                        │
│  Stato:        BASELINE ATTIVA                                   │
│                                                                  │
│  "L'ingegnere non scrive prompt —                                │
│   progetta istruzioni ingegneristiche tracciabili."              │
│                                                                  │
│  Ogni prompt è un atto di definizione.                           │
│  Ogni output è un artefatto misurabile.                          │
│  Ogni contributo è ricompensato.                                 │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

*GQAOA Universal Technology Architecture — APE ADAPT UI STUDIO v1.0*  
*Amedeo Pelliccia — AEROSPACEMODEL Lifecycle Operating System*
