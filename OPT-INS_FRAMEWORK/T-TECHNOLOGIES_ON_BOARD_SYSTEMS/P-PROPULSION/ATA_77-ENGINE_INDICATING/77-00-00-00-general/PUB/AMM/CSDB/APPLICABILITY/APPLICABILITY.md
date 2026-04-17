# Applicability Model — CSDB/APPLICABILITY

**Framework:** GQAOA OPT-INS / UTA  
**Standard di riferimento:** S1000D Issue 5.0 — Chap. 8 (Applicability)  
**Autorità:** GQAOA .INC — GAIA QUANTUM AMPEL OPT-INS ARCHITECTURE  
**Data:** 2026-04-14  
**Stato:** Baseline attiva

---

## 0. Introduzione

### 0.1 Scopo

Questo documento definisce il **modello di applicabilità** per tutti i Data Module (DM), Publication Module (PM) e artefatti contenuti nella CSDB di questo nodo. L'applicabilità determina *quali* configurazioni, prodotti, varianti e condizioni operative rendono valido ogni singolo oggetto della CSDB.

### 0.2 Ambito

- AMM (Aircraft/Asset Maintenance Manual) all'interno della CSDB multi-manual
- Tutti i Data Module pubblicati nella directory `DM/`
- Filtraggio per output renderizzato (`EXPORT/`) e viewer interattivo (`IETP/`)

---

## 1. Riferimenti Normativi e di Interfaccia

| Riferimento | Descrizione |
|---|---|
| **S1000D Issue 5.0** | Gestione dell'applicabilità nei Data Module — Identification and Status Section, ACT/PCT/CCT |
| **ASD-STE-100** | Simplified Technical English — linguaggio per descrizioni DM |
| **OPT-INS Framework** | Canonical leaf-node pattern — `PUB/AMM/CSDB/APPLICABILITY/` |
| **SUPIA v1.0** | GQAOA-UTA-SUPIA-001 — Sistema Unico di Progettazione Industriale Avanzata |
| **LUTNDR v1.0** | GQAOA-UTA-LUTNDR-001 — Libro Unico delle Tecnologie: stati tecnologici e circolarità |
| **BREX** | Business Rules Exchange (directory adiacente) — vincoli e regole di business della CSDB |

---

## 2. Modello Concettuale di Applicabilità

### 2.1 Entità

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   PRODOTTO   │────►│CONFIGURAZIONE│────►│  CONDIZIONE   │
│  (Product)   │     │ (Config)     │     │ (Condition)   │
└──────┬───────┘     └──────┬───────┘     └──────┬────────┘
       │                    │                     │
       ▼                    ▼                     ▼
 ┌───────────┐      ┌───────────┐        ┌───────────────┐
 │   ACT     │      │   PCT     │        │     CCT       │
 │Applicab.  │      │ Product   │        │  Condition    │
 │Cross-Ref  │      │Cross-Ref  │        │  Cross-Ref    │
 │  Table    │      │  Table    │        │    Table      │
 └───────────┘      └───────────┘        └───────────────┘
```

### 2.2 Relazione con i Data Module

Ogni DM nella directory `DM/` contiene nella propria **Identification and Status Section** i riferimenti alle tabelle ACT, PCT e CCT. La CSDB utilizza queste tabelle per:

1. **Filtrare** — includere/escludere task, sezioni e illustrazioni nella pubblicazione
2. **Riutilizzare** — condividere DM tra varianti diverse del prodotto
3. **Configurare** — selezionare contenuti in base alla configurazione effettiva (MSN, mod status, SB)

---

## 3. Tabelle di Applicabilità (ACT / PCT / CCT)

### 3.1 ACT — Applicability Cross-reference Table

La ACT elenca tutti gli identificatori di applicabilità utilizzati nei DM di questo nodo.

```xml
<!-- Struttura S1000D ACT -->
<applic>
  <displayText>
    <simplePara>Applicabile a: {descrizione}</simplePara>
  </displayText>
  <assert applicPropertyIdent="{ATTR}" applicPropertyType="{TYPE}" applicPropertyValues="{VAL}"/>
</applic>
```

### 3.2 PCT — Product Cross-reference Table

La PCT definisce i prodotti, modelli e varianti a cui si applicano i DM.

| Campo PCT | Descrizione | Esempio |
|---|---|---|
| `productIdent` | Codice prodotto | `AMPEL360-Q100` |
| `productModel` | Variante / modello | `Q100-LR` |
| `productSeries` | Serie o lotto | `SN-001–SN-050` |

### 3.3 CCT — Condition Cross-reference Table

La CCT definisce condizioni operative, ambientali e di stato che influenzano l'applicabilità.

| Campo CCT | Descrizione | Esempio |
|---|---|---|
| `condIdent` | Codice condizione | `ENV-COLD` |
| `condType` | Tipo | `environment` |
| `condValue` | Valore | `temp < -40°C` |

---

## 4. Attributi di Applicabilità

| Attributo | Descrizione | Tipo | Valori / Dominio | Mappatura S1000D |
|---|---|---|---|---|
| `product` | Programma / velivolo / sistema | string | `AMPEL360-Q100`, `GAIA-SPACE-LAUNCHER`, `SPACET-Q10` | `applicPropertyIdent="product"` |
| `variant` | Variante del prodotto | string | Codice modello specifico | `applicPropertyIdent="variant"` |
| `msn` | Manufacturer Serial Number | string | Pattern: `SN-NNN` | `applicPropertyIdent="msn"` |
| `modStatus` | Stato di modifica applicato | string | Codice SB/ECO (es. `SB-028-001`) | `applicPropertyIdent="modStatus"` |
| `operator` | Operatore / cliente | string | Codice ICAO o nome | `applicPropertyIdent="operator"` |
| `environment` | Condizione ambientale | enum | `STANDARD`, `COLD`, `HOT`, `HUMID`, `SALT`, `ALTITUDE` | `applicPropertyIdent="environment"` |
| `lutState` | Stato tecnologico LUTNDR | enum | `USO`, `DIS`, `NPR`, `RIC` | `applicPropertyIdent="lutState"` |
| `lcPhase` | Fase del ciclo di vita | enum | `LC01`–`LC14` | `applicPropertyIdent="lcPhase"` |
| `optAxis` | Asse OPT-INS | enum | `O`, `P`, `T`, `I`, `N`, `S` | `applicPropertyIdent="optAxis"` |

---

## 5. Espressioni di Applicabilità e Logica

### 5.1 Sintassi

Le espressioni di applicabilità combinano attributi con operatori logici:

| Operatore | Simbolo | S1000D | Esempio |
|---|---|---|---|
| AND | `∧` | `<evaluate andOr="and">` | `product=Q100 ∧ modStatus=SB-028-001` |
| OR | `∨` | `<evaluate andOr="or">` | `variant=LR ∨ variant=ER` |
| NOT | `¬` | `<evaluate not="true">` | `¬ environment=COLD` |
| Raggruppamento | `( )` | nesting `<evaluate>` | `(product=Q100 ∨ product=Q10) ∧ lcPhase=LC10` |

### 5.2 Esempi di espressioni

```
# DM applicabile solo a Q100 in fase operativa, ambiente standard
product=AMPEL360-Q100 ∧ lcPhase=LC10 ∧ environment=STANDARD

# DM per tutti i prodotti in disuso
lutState=DIS

# Task applicabile a Q100 con SB applicata OPPURE Q10
(product=AMPEL360-Q100 ∧ modStatus=SB-028-001) ∨ product=SPACET-Q10
```

### 5.3 Valutazione

1. Le espressioni vengono valutate dal motore CSDB al momento della pubblicazione (`EXPORT/`) o del rendering interattivo (`IETP/`)
2. I DM che non soddisfano l'espressione vengono **esclusi** dall'output
3. La valutazione è deterministica: dato un set di attributi, il risultato è sempre lo stesso

---

## 6. Filtraggio nelle Uscite AMM

### 6.1 EXPORT (PDF / HTML)

Il processo di pubblicazione legge le tabelle ACT/PCT/CCT e genera l'output filtrato:

```
CSDB/DM/*.xml  ──►  ACT/PCT/CCT  ──►  Filtro  ──►  EXPORT/{PDF,HTML}
                     (questo dir)      applicabilità
```

### 6.2 IETP (Interactive Electronic Technical Publication)

Il viewer IETP applica il filtraggio in tempo reale, permettendo all'utente di selezionare:
- Prodotto e variante
- Configurazione (MSN, mod status)
- Condizioni operative

---

## 7. Governance e Manutenzione

### 7.1 Proprietà

| Ruolo | Responsabilità |
|---|---|
| **Proprietario del capitolo** | Definisce e mantiene gli attributi di applicabilità |
| **Q-DATAGOV** | Approva modifiche alle tabelle ACT/PCT/CCT |
| **CCB** | Valida allineamento con configurazione di baseline |

### 7.2 Ciclo di aggiornamento

1. **Proposta** — ECO con descrizione della modifica all'applicabilità
2. **Revisione** — Impatto su DM esistenti valutato
3. **Approvazione** — CCB approva, tabelle aggiornate
4. **Propagazione** — DM coinvolti ri-pubblicati con nuova applicabilità

### 7.3 Integrità

- Ogni attributo nella ACT deve avere un valore valido nel PCT o CCT
- Nessun DM può avere espressione di applicabilità vuota (default: applicabile a tutti)
- Modifiche alle tabelle generano un nuovo hash nel registro di configurazione (`SSOT/LC08_CONFIGURATION/`)

---

## 8. File in questa Directory

| File | Formato | Descrizione |
|---|---|---|
| `APPLICABILITY.md` | Markdown | Questo documento — specifica del modello di applicabilità |
| `ACT.xml` | S1000D XML | Applicability Cross-reference Table (quando compilata) |
| `PCT.xml` | S1000D XML | Product Cross-reference Table (quando compilata) |
| `CCT.xml` | S1000D XML | Condition Cross-reference Table (quando compilata) |

---

*Documento gestito secondo il canonical leaf-node pattern OPT-INS. Riferimento: OPT-INS_FRAMEWORK/Readme.md §Canonical Leaf-Node Pattern.*
