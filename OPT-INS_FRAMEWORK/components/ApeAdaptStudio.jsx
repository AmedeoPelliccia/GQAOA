/**
 * ApeAdaptStudio — Aided Prompt Engineering to Aerospace Digital
 *                   Applications and Programming Technologies
 *                   User Interface Studio
 *
 * Interactive prompt engineering interface for the UTA/SUPIA ecosystem.
 * Connects prompts to KNOT uncertainties and produces traceable KNU artefacts
 * through the CHARLIE-T → GENTLE → BOOST pipeline.
 *
 * Specification: GQAOA-APE-ADAPT-001
 * Version:       1.0
 * Generated:     2026-04-11
 * Framework:     OPT-INS_FRAMEWORK / SUPIA
 * Owner:         GAIA QUANTUM AMPEL OPT-INS ARCHITECTURE, INC. (GQAOA, INC.)
 */

import { useState, useMemo, useCallback } from "react";

/* ────────────────────────────────────────────────────────────
 *  CONSTANTS
 * ────────────────────────────────────────────────────────── */

const DOMAINS = [
  { id: "G1",  code: "ATA",   range: "000–099", label: "Aerospace Technology",        icon: "✈️",  color: "#2563eb" },
  { id: "G2",  code: "STA",   range: "100–199", label: "Space Technology",             icon: "🚀",  color: "#7c3aed" },
  { id: "G3",  code: "DTTA",  range: "200–299", label: "Defence Technology",           icon: "🛡️", color: "#dc2626" },
  { id: "G4",  code: "DTCEC", range: "300–399", label: "Digital Twin / Cloud / Edge",  icon: "🔮",  color: "#8b5cf6" },
  { id: "G5",  code: "EPTA",  range: "400–499", label: "Energy & Propulsion",          icon: "⚡",  color: "#ea580c" },
  { id: "G6",  code: "AMTA",  range: "500–599", label: "Materials / Bio / Nano",       icon: "🧬",  color: "#16a34a" },
  { id: "G7",  code: "OGATA", range: "600–699", label: "Ground Automation",            icon: "⚙️",  color: "#0891b2" },
  { id: "G8",  code: "ACV",   range: "700–799", label: "Aerial City Viability",        icon: "🏙️",  color: "#ca8a04" },
  { id: "G9",  code: "CYB",   range: "800–899", label: "Cybersecurity",                icon: "🔒",  color: "#e11d48" },
  { id: "G10", code: "QCSAA", range: "900–999", label: "Quantum & Sentient Agency",    icon: "🌐",  color: "#6d28d9" },
];

const AXES = {
  O: { label: "Organizations",   color: "#2563eb" },
  P: { label: "Programs",        color: "#16a34a" },
  T: { label: "Technologies",    color: "#ea580c" },
  I: { label: "Infrastructures", color: "#0891b2" },
  N: { label: "Neural Networks", color: "#7c3aed" },
  S: { label: "SIM-TEST / Space", color: "#e11d48" },
};

const PROGRAMMES = [
  { id: "Q100",   label: "AMPEL360 Q100",       domains: ["G1","G4","G5","G6","G9"] },
  { id: "GAIA",   label: "GAIA-SPACE-LAUNCHER", domains: ["G1","G2","G4","G5","G6","G9","G10"] },
  { id: "SPACET", label: "SPACET Q10",          domains: ["G1","G2","G4","G5","G9","G10"] },
];

const LC_PHASES = [
  { id: "LC01", label: "Problem Statement" },
  { id: "LC02", label: "Requirements" },
  { id: "LC03", label: "Safety" },
  { id: "LC04", label: "Design" },
  { id: "LC05", label: "Analysis" },
  { id: "LC06", label: "Verification" },
  { id: "LC07", label: "Validation" },
  { id: "LC08", label: "Configuration" },
  { id: "LC09", label: "Production" },
  { id: "LC10", label: "Operations" },
  { id: "LC11", label: "Maintenance" },
  { id: "LC12", label: "Customer Care" },
  { id: "LC13", label: "Training" },
  { id: "LC14", label: "Retirement/Circularity" },
];

const KNU_TYPES = [
  { code: "REQ",  label: "Requisito" },
  { code: "ICD",  label: "Interface Control" },
  { code: "ANA",  label: "Analisi" },
  { code: "TEST", label: "Prova" },
  { code: "SAF",  label: "Sicurezza" },
  { code: "CM",   label: "Configurazione" },
  { code: "PUB",  label: "Pubblicazione" },
  { code: "DWG",  label: "Disegno" },
  { code: "SIM",  label: "Simulazione" },
  { code: "DPP",  label: "Passaporto Digitale" },
];

const APE_VERBS = [
  { id: "genera",    label: "Genera",    icon: "✨", desc: "Crea un artefatto nuovo" },
  { id: "analizza",  label: "Analizza",  icon: "🔍", desc: "Esamina un artefatto esistente" },
  { id: "verifica",  label: "Verifica",  icon: "✅", desc: "Controlla conformità a criteri" },
  { id: "confronta", label: "Confronta", icon: "⚖️",  desc: "Compara due o più artefatti" },
  { id: "sintetizza", label: "Sintetizza", icon: "📋", desc: "Consolida informazioni da più fonti" },
  { id: "trasforma", label: "Trasforma", icon: "🔄", desc: "Converte in formato diverso" },
  { id: "ottimizza", label: "Ottimizza", icon: "📈", desc: "Migliora un artefatto" },
  { id: "documenta", label: "Documenta", icon: "📄", desc: "Produce documentazione S1000D" },
  { id: "revisiona", label: "Revisiona", icon: "🔎", desc: "Rileva errori o lacune" },
  { id: "predice",   label: "Predice",   icon: "🔮", desc: "Stima comportamento futuro" },
];

const TEMPLATES = [
  { id: "TPL-LC01-KNOT",     name: "Dichiarazione KNOT",     phase: "LC01", knu: "KNOT", domains: "all" },
  { id: "TPL-LC02-REQ",      name: "Generazione Requisiti",  phase: "LC02", knu: "REQ",  domains: "all" },
  { id: "TPL-LC02-TRACE",    name: "Matrice Tracciabilità",  phase: "LC02", knu: "REQ",  domains: "all" },
  { id: "TPL-LC03-FMEA",     name: "Analisi FMEA",           phase: "LC03", knu: "SAF",  domains: "all" },
  { id: "TPL-LC03-FTA",      name: "Analisi FTA",            phase: "LC03", knu: "SAF",  domains: "all" },
  { id: "TPL-LC04-ICD",      name: "Interface Control Doc",  phase: "LC04", knu: "ICD",  domains: "all" },
  { id: "TPL-LC04-DWG-CART", name: "Disegno con Cartiglio",  phase: "LC04", knu: "DWG",  domains: "all" },
  { id: "TPL-LC05-TRADE",    name: "Trade Study",            phase: "LC05", knu: "ANA",  domains: "all" },
  { id: "TPL-LC06-TEST",     name: "Piano di Prova",         phase: "LC06", knu: "TEST", domains: "all" },
  { id: "TPL-LC07-REPORT",   name: "Rapporto Validazione",   phase: "LC07", knu: "TEST", domains: "all" },
  { id: "TPL-LC08-DELTA",    name: "Analisi Impatto Modifica", phase: "LC08", knu: "CM",  domains: "all" },
  { id: "TPL-LC11-TASK",     name: "Task Card Manutenzione", phase: "LC11", knu: "PUB",  domains: "G1,G2" },
  { id: "TPL-LC14-DPP",      name: "Passaporto Digitale",    phase: "LC14", knu: "DPP",  domains: "all" },
  { id: "TPL-PUB-DM-DESC",   name: "DM Descrittivo S1000D",  phase: "PUB",  knu: "PUB",  domains: "all" },
  { id: "TPL-PUB-DM-PROC",   name: "DM Procedurale S1000D",  phase: "PUB",  knu: "PUB",  domains: "all" },
];

/* ────────────────────────────────────────────────────────────
 *  HELPER: Prompt Quality Score calculator
 * ────────────────────────────────────────────────────────── */

function calculatePQS(prompt) {
  let s = 0, c = 0, v = 0, a = 0, t = 0;

  // Specificity (25%): instruction length, verb, knu_type
  if (prompt.instruction && prompt.instruction.length > 40) s += 50;
  if (prompt.instruction && prompt.instruction.length > 120) s += 30;
  if (prompt.verb) s += 20;

  // Context (20%): chapter, domain, axis, programme, lc_phase
  if (prompt.chapter) c += 20;
  if (prompt.domain) c += 20;
  if (prompt.axis) c += 20;
  if (prompt.programme) c += 20;
  if (prompt.lcPhase) c += 20;

  // Constraints (20%): standards, format
  if (prompt.standards && prompt.standards.length > 0) v += 50;
  if (prompt.format && prompt.format.length > 10) v += 50;

  // Acceptance (20%): criteria defined
  if (prompt.acceptance && prompt.acceptance.length > 20) a += 70;
  if (prompt.residueTarget) a += 30;

  // Traceability (15%): knot linked
  if (prompt.knotParent) t += 60;
  if (prompt.knuType) t += 40;

  return Math.round(0.25 * s + 0.20 * c + 0.20 * v + 0.20 * a + 0.15 * t);
}

function pqsClass(score) {
  if (score >= 90) return { label: "Eccellente", emoji: "✅", color: "#16a34a" };
  if (score >= 70) return { label: "Buono", emoji: "🟡", color: "#ca8a04" };
  if (score >= 50) return { label: "Sufficiente", emoji: "🟠", color: "#ea580c" };
  return { label: "Insufficiente", emoji: "🔴", color: "#dc2626" };
}

/* ────────────────────────────────────────────────────────────
 *  STYLES (shared)
 * ────────────────────────────────────────────────────────── */

const inputStyle = {
  padding: "6px 10px",
  borderRadius: 6,
  border: "1px solid #cbd5e1",
  fontSize: "0.8rem",
  width: "100%",
  boxSizing: "border-box",
};

const selectStyle = { ...inputStyle, width: "auto", minWidth: 140 };

const labelStyle = {
  display: "block",
  fontSize: "0.7rem",
  fontWeight: 600,
  color: "#64748b",
  marginBottom: 3,
};

const cardStyle = {
  border: "1px solid #e2e8f0",
  borderRadius: 10,
  padding: 14,
  background: "#fff",
};

const badgeStyle = (color) => ({
  display: "inline-block",
  padding: "2px 8px",
  borderRadius: 999,
  fontSize: "0.65rem",
  fontWeight: 700,
  color: "#fff",
  background: color,
});

/* ────────────────────────────────────────────────────────────
 *  SUB-COMPONENTS
 * ────────────────────────────────────────────────────────── */

function PqsGauge({ score }) {
  const cls = pqsClass(score);
  return (
    <div style={{ textAlign: "center" }}>
      <div style={{ fontSize: "2rem", fontWeight: 800, color: cls.color }}>{score}</div>
      <div style={{ fontSize: "0.7rem", color: cls.color }}>
        {cls.emoji} {cls.label}
      </div>
    </div>
  );
}

function PipelineVisual({ stage }) {
  const stages = [
    { key: "compose", label: "Compose", icon: "✏️" },
    { key: "charlie", label: "CHARLIE-T", icon: "🤖" },
    { key: "gentle",  label: "GENTLE", icon: "⚡" },
    { key: "boost",   label: "BOOST", icon: "🚀" },
    { key: "validate", label: "Validate", icon: "✅" },
    { key: "register", label: "Register", icon: "📝" },
  ];
  const idx = stages.findIndex((s) => s.key === stage);
  return (
    <div style={{ display: "flex", gap: 4, alignItems: "center" }}>
      {stages.map((s, i) => (
        <div key={s.key} style={{ display: "flex", alignItems: "center", gap: 4 }}>
          <div style={{
            padding: "4px 8px",
            borderRadius: 6,
            fontSize: "0.65rem",
            fontWeight: 600,
            background: i <= idx ? "#2563eb" : "#f1f5f9",
            color: i <= idx ? "#fff" : "#94a3b8",
          }}>
            {s.icon} {s.label}
          </div>
          {i < stages.length - 1 && (
            <span style={{ color: i < idx ? "#2563eb" : "#cbd5e1", fontSize: "0.7rem" }}>→</span>
          )}
        </div>
      ))}
    </div>
  );
}

function TracabilityChain() {
  const chain = [
    { name: "ALICE", desc: "Physical System", color: "#16a34a" },
    { name: "BOB DT", desc: "Structural Twin", color: "#2563eb" },
    { name: "CHARLIE-T", desc: "Contextual Agent", color: "#7c3aed" },
    { name: "GENTLE", desc: "Language Engine", color: "#ea580c" },
    { name: "BOOST", desc: "Semantic Optimizer", color: "#e11d48" },
  ];
  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 4 }}>
      {chain.map((c, i) => (
        <div key={c.name} style={{ display: "flex", alignItems: "center", gap: 6 }}>
          <div style={{
            width: 8, height: 8, borderRadius: "50%",
            background: c.color, flexShrink: 0,
          }} />
          <div>
            <div style={{ fontSize: "0.7rem", fontWeight: 700, color: c.color }}>{c.name}</div>
            <div style={{ fontSize: "0.6rem", color: "#94a3b8" }}>{c.desc}</div>
          </div>
          {i < chain.length - 1 && (
            <div style={{ fontSize: "0.5rem", color: "#cbd5e1", marginLeft: "auto" }}>▼</div>
          )}
        </div>
      ))}
    </div>
  );
}

/* ────────────────────────────────────────────────────────────
 *  MAIN COMPONENT
 * ────────────────────────────────────────────────────────── */

export default function ApeAdaptStudio() {
  // ── State ──
  const [activeTab, setActiveTab] = useState("compose"); // compose | templates | history | metrics
  const [prompt, setPrompt] = useState({
    knotParent: "",
    chapter: "",
    domain: "",
    axis: "",
    programme: "",
    lcPhase: "",
    verb: "",
    knuType: "",
    instruction: "",
    standards: "",
    format: "",
    acceptance: "",
    residueTarget: "",
  });
  const [history, setHistory] = useState([]);
  const [pipelineStage, setPipelineStage] = useState("compose");

  // ── Derived ──
  const pqs = useMemo(() => calculatePQS(prompt), [prompt]);
  const pqsCls = pqsClass(pqs);

  const filteredTemplates = useMemo(() => {
    return TEMPLATES.filter((t) => {
      if (prompt.lcPhase && t.phase !== prompt.lcPhase && t.phase !== "PUB") return false;
      if (prompt.domain && t.domains !== "all" && !t.domains.includes(prompt.domain)) return false;
      return true;
    });
  }, [prompt.lcPhase, prompt.domain]);

  // ── Handlers ──
  const updatePrompt = useCallback((field, value) => {
    setPrompt((prev) => ({ ...prev, [field]: value }));
    setPipelineStage("compose");
  }, []);

  const applyTemplate = useCallback((tpl) => {
    setPrompt((prev) => ({
      ...prev,
      lcPhase: tpl.phase === "PUB" ? prev.lcPhase : tpl.phase,
      knuType: tpl.knu,
      verb: "genera",
    }));
    setActiveTab("compose");
  }, []);

  const executePrompt = useCallback(() => {
    if (pqs < 50) return;

    // Simulate pipeline stages
    setPipelineStage("charlie");
    const timer1 = setTimeout(() => setPipelineStage("gentle"), 600);
    const timer2 = setTimeout(() => setPipelineStage("boost"), 1200);
    const timer3 = setTimeout(() => setPipelineStage("validate"), 1800);
    const timer4 = setTimeout(() => {
      setPipelineStage("register");
      const entry = {
        id: `APE-2026-${String(history.length + 1).padStart(4, "0")}`,
        timestamp: new Date().toISOString(),
        knot: prompt.knotParent,
        chapter: prompt.chapter,
        domain: prompt.domain,
        lcPhase: prompt.lcPhase,
        knuType: prompt.knuType,
        verb: prompt.verb,
        pqs,
        status: pqs >= 70 ? "ACCEPTED" : "REVIEW",
      };
      setHistory((prev) => [entry, ...prev]);
    }, 2400);

    return () => {
      clearTimeout(timer1);
      clearTimeout(timer2);
      clearTimeout(timer3);
      clearTimeout(timer4);
    };
  }, [prompt, pqs, history.length]);

  const resetPrompt = useCallback(() => {
    setPrompt({
      knotParent: "", chapter: "", domain: "", axis: "",
      programme: "", lcPhase: "", verb: "", knuType: "",
      instruction: "", standards: "", format: "",
      acceptance: "", residueTarget: "",
    });
    setPipelineStage("compose");
  }, []);

  // ── Metrics ──
  const metrics = useMemo(() => {
    if (history.length === 0) return { avgPqs: 0, accepted: 0, total: 0, rate: 0 };
    const avgPqs = Math.round(history.reduce((a, h) => a + h.pqs, 0) / history.length);
    const accepted = history.filter((h) => h.status === "ACCEPTED").length;
    return { avgPqs, accepted, total: history.length, rate: Math.round((accepted / history.length) * 100) };
  }, [history]);

  // ── Render ──
  return (
    <div style={{ fontFamily: "system-ui, sans-serif", maxWidth: 1200, margin: "0 auto", padding: 24 }}>
      {/* ── Header ── */}
      <div style={{ display: "flex", alignItems: "center", gap: 12, marginBottom: 4 }}>
        <span style={{ fontSize: "1.75rem" }}>🧠</span>
        <div>
          <h1 style={{ fontSize: "1.5rem", fontWeight: 800, margin: 0 }}>
            APE ADAPT UI STUDIO
          </h1>
          <p style={{ fontSize: "0.7rem", color: "#64748b", margin: 0 }}>
            Aided Prompt Engineering to Aerospace Digital Applications and Programming Technologies — Enhancing user interaction, streamlining development
          </p>
        </div>
      </div>
      <p style={{ color: "#94a3b8", fontSize: "0.75rem", marginBottom: 16 }}>
        CHARLIE-T → GENTLE → BOOST pipeline · {DOMAINS.length} domains · {TEMPLATES.length} templates · SUPIA v1.0
      </p>

      {/* ── Pipeline Visual ── */}
      <div style={{ marginBottom: 16 }}>
        <PipelineVisual stage={pipelineStage} />
      </div>

      {/* ── Tabs ── */}
      <div style={{ display: "flex", gap: 4, marginBottom: 16, borderBottom: "2px solid #e2e8f0", paddingBottom: 8 }}>
        {[
          { id: "compose", label: "✏️ Compose", desc: "Prompt Composer" },
          { id: "templates", label: "📑 Templates", desc: "Template Gallery" },
          { id: "history", label: "📜 History", desc: "Prompt Registry" },
          { id: "metrics", label: "📊 Metrics", desc: "Quality Metrics" },
        ].map((tab) => (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id)}
            title={tab.desc}
            style={{
              padding: "8px 16px",
              borderRadius: "8px 8px 0 0",
              border: "none",
              background: activeTab === tab.id ? "#2563eb" : "transparent",
              color: activeTab === tab.id ? "#fff" : "#64748b",
              fontWeight: activeTab === tab.id ? 700 : 400,
              fontSize: "0.85rem",
              cursor: "pointer",
            }}
          >
            {tab.label}
          </button>
        ))}
      </div>

      {/* ════════════════════════════════════════════════════════
       *  TAB: COMPOSE
       * ═══════════════════════════════════════════════════════ */}
      {activeTab === "compose" && (
        <div style={{ display: "grid", gridTemplateColumns: "1fr 240px", gap: 16 }}>
          {/* ── Left: Prompt Composer ── */}
          <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
            {/* Context row */}
            <div style={cardStyle}>
              <div style={{ fontSize: "0.8rem", fontWeight: 700, marginBottom: 8 }}>📍 Contesto</div>
              <div style={{ display: "grid", gridTemplateColumns: "repeat(3, 1fr)", gap: 8 }}>
                <div>
                  <label style={labelStyle}>KNOT Padre</label>
                  <input
                    style={inputStyle}
                    placeholder="KNOT-UTA-028-10-00-001"
                    value={prompt.knotParent}
                    onChange={(e) => updatePrompt("knotParent", e.target.value)}
                  />
                </div>
                <div>
                  <label style={labelStyle}>Capitolo UTA</label>
                  <input
                    style={inputStyle}
                    placeholder="028"
                    value={prompt.chapter}
                    onChange={(e) => updatePrompt("chapter", e.target.value)}
                  />
                </div>
                <div>
                  <label style={labelStyle}>Dominio</label>
                  <select
                    style={inputStyle}
                    value={prompt.domain}
                    onChange={(e) => updatePrompt("domain", e.target.value)}
                  >
                    <option value="">—</option>
                    {DOMAINS.map((d) => (
                      <option key={d.id} value={d.id}>{d.icon} {d.code} ({d.range})</option>
                    ))}
                  </select>
                </div>
                <div>
                  <label style={labelStyle}>Asse OPT-INS</label>
                  <select
                    style={inputStyle}
                    value={prompt.axis}
                    onChange={(e) => updatePrompt("axis", e.target.value)}
                  >
                    <option value="">—</option>
                    {Object.entries(AXES).map(([k, v]) => (
                      <option key={k} value={k}>{k} — {v.label}</option>
                    ))}
                  </select>
                </div>
                <div>
                  <label style={labelStyle}>Programma</label>
                  <select
                    style={inputStyle}
                    value={prompt.programme}
                    onChange={(e) => updatePrompt("programme", e.target.value)}
                  >
                    <option value="">—</option>
                    {PROGRAMMES.map((p) => (
                      <option key={p.id} value={p.id}>{p.label}</option>
                    ))}
                  </select>
                </div>
                <div>
                  <label style={labelStyle}>Fase LC</label>
                  <select
                    style={inputStyle}
                    value={prompt.lcPhase}
                    onChange={(e) => updatePrompt("lcPhase", e.target.value)}
                  >
                    <option value="">—</option>
                    {LC_PHASES.map((lc) => (
                      <option key={lc.id} value={lc.id}>{lc.id} {lc.label}</option>
                    ))}
                  </select>
                </div>
              </div>
            </div>

            {/* Action row */}
            <div style={cardStyle}>
              <div style={{ fontSize: "0.8rem", fontWeight: 700, marginBottom: 8 }}>⚡ Azione</div>
              <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 8, marginBottom: 8 }}>
                <div>
                  <label style={labelStyle}>Verbo APE</label>
                  <select
                    style={inputStyle}
                    value={prompt.verb}
                    onChange={(e) => updatePrompt("verb", e.target.value)}
                  >
                    <option value="">— Seleziona verbo —</option>
                    {APE_VERBS.map((v) => (
                      <option key={v.id} value={v.id}>{v.icon} {v.label} — {v.desc}</option>
                    ))}
                  </select>
                </div>
                <div>
                  <label style={labelStyle}>Tipo KNU</label>
                  <select
                    style={inputStyle}
                    value={prompt.knuType}
                    onChange={(e) => updatePrompt("knuType", e.target.value)}
                  >
                    <option value="">— Tipo —</option>
                    {KNU_TYPES.map((k) => (
                      <option key={k.code} value={k.code}>{k.code} — {k.label}</option>
                    ))}
                  </select>
                </div>
              </div>
              <div>
                <label style={labelStyle}>Istruzione</label>
                <textarea
                  style={{ ...inputStyle, height: 100, resize: "vertical" }}
                  placeholder="Genera i requisiti funzionali per il sistema di distribuzione carburante del serbatoio ala-fusoliera (BWB), considerando..."
                  value={prompt.instruction}
                  onChange={(e) => updatePrompt("instruction", e.target.value)}
                />
              </div>
            </div>

            {/* Constraints row */}
            <div style={cardStyle}>
              <div style={{ fontSize: "0.8rem", fontWeight: 700, marginBottom: 8 }}>🔒 Vincoli</div>
              <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 8 }}>
                <div>
                  <label style={labelStyle}>Standard applicabili</label>
                  <input
                    style={inputStyle}
                    placeholder="EASA CS-25.952, SAE ARP4754A"
                    value={prompt.standards}
                    onChange={(e) => updatePrompt("standards", e.target.value)}
                  />
                </div>
                <div>
                  <label style={labelStyle}>Formato output</label>
                  <input
                    style={inputStyle}
                    placeholder="tabella requisiti con ID, descrizione, MoC"
                    value={prompt.format}
                    onChange={(e) => updatePrompt("format", e.target.value)}
                  />
                </div>
              </div>
            </div>

            {/* Acceptance row */}
            <div style={cardStyle}>
              <div style={{ fontSize: "0.8rem", fontWeight: 700, marginBottom: 8 }}>✅ Accettazione</div>
              <div style={{ display: "grid", gridTemplateColumns: "3fr 1fr", gap: 8 }}>
                <div>
                  <label style={labelStyle}>Criteri di accettazione</label>
                  <input
                    style={inputStyle}
                    placeholder="tutti i sotto-sistemi coperti, ogni requisito verificabile"
                    value={prompt.acceptance}
                    onChange={(e) => updatePrompt("acceptance", e.target.value)}
                  />
                </div>
                <div>
                  <label style={labelStyle}>Residuo target</label>
                  <input
                    style={inputStyle}
                    type="number"
                    min="0"
                    max="100"
                    placeholder="≤ 30"
                    value={prompt.residueTarget}
                    onChange={(e) => updatePrompt("residueTarget", e.target.value)}
                  />
                </div>
              </div>
            </div>

            {/* Actions */}
            <div style={{ display: "flex", gap: 8, alignItems: "center" }}>
              <button
                onClick={executePrompt}
                disabled={pqs < 50}
                style={{
                  padding: "10px 24px",
                  borderRadius: 8,
                  border: "none",
                  background: pqs >= 50 ? "#2563eb" : "#94a3b8",
                  color: "#fff",
                  fontWeight: 700,
                  fontSize: "0.9rem",
                  cursor: pqs >= 50 ? "pointer" : "not-allowed",
                }}
              >
                🚀 Esegui Pipeline C→G→B
              </button>
              <button
                onClick={resetPrompt}
                style={{
                  padding: "10px 16px",
                  borderRadius: 8,
                  border: "1px solid #cbd5e1",
                  background: "#fff",
                  cursor: "pointer",
                  fontSize: "0.85rem",
                }}
              >
                ↺ Reset
              </button>
              <div style={{ marginLeft: "auto", fontSize: "0.75rem", color: pqsCls.color, fontWeight: 600 }}>
                PQS: {pqs}/100 {pqsCls.emoji}
              </div>
            </div>
          </div>

          {/* ── Right: Context Panel ── */}
          <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
            {/* PQS Gauge */}
            <div style={cardStyle}>
              <div style={{ fontSize: "0.75rem", fontWeight: 700, color: "#64748b", marginBottom: 6 }}>
                Prompt Quality Score
              </div>
              <PqsGauge score={pqs} />
              <div style={{ fontSize: "0.6rem", color: "#94a3b8", marginTop: 6, textAlign: "center" }}>
                {pqs < 50 ? "Completa i campi per abilitare l'esecuzione" : "Pronto per l'esecuzione"}
              </div>
            </div>

            {/* Traceability Chain */}
            <div style={cardStyle}>
              <div style={{ fontSize: "0.75rem", fontWeight: 700, color: "#64748b", marginBottom: 6 }}>
                Catena di Tracciabilità
              </div>
              <TracabilityChain />
            </div>

            {/* Context summary */}
            <div style={cardStyle}>
              <div style={{ fontSize: "0.75rem", fontWeight: 700, color: "#64748b", marginBottom: 6 }}>
                Contesto Attivo
              </div>
              <div style={{ display: "flex", flexDirection: "column", gap: 4 }}>
                {[
                  { label: "UTA", value: prompt.chapter || "—" },
                  { label: "Dominio", value: prompt.domain ? DOMAINS.find((d) => d.id === prompt.domain)?.code : "—" },
                  { label: "Asse", value: prompt.axis || "—" },
                  { label: "Programma", value: prompt.programme || "—" },
                  { label: "Fase", value: prompt.lcPhase || "—" },
                  { label: "KNOT", value: prompt.knotParent ? "✅" : "—" },
                  { label: "Verbo", value: prompt.verb || "—" },
                  { label: "KNU", value: prompt.knuType || "—" },
                ].map((item) => (
                  <div key={item.label} style={{ display: "flex", justifyContent: "space-between", fontSize: "0.7rem" }}>
                    <span style={{ color: "#64748b" }}>{item.label}</span>
                    <span style={{ fontWeight: 600, fontFamily: "monospace" }}>{item.value}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      )}

      {/* ════════════════════════════════════════════════════════
       *  TAB: TEMPLATES
       * ═══════════════════════════════════════════════════════ */}
      {activeTab === "templates" && (
        <div>
          <div style={{ display: "flex", gap: 8, marginBottom: 16, flexWrap: "wrap" }}>
            <select
              style={selectStyle}
              value={prompt.lcPhase}
              onChange={(e) => updatePrompt("lcPhase", e.target.value)}
            >
              <option value="">Tutte le fasi</option>
              {LC_PHASES.map((lc) => (
                <option key={lc.id} value={lc.id}>{lc.id} {lc.label}</option>
              ))}
            </select>
            <select
              style={selectStyle}
              value={prompt.domain}
              onChange={(e) => updatePrompt("domain", e.target.value)}
            >
              <option value="">Tutti i domini</option>
              {DOMAINS.map((d) => (
                <option key={d.id} value={d.id}>{d.icon} {d.code}</option>
              ))}
            </select>
          </div>
          <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(260px, 1fr))", gap: 12 }}>
            {filteredTemplates.map((tpl) => (
              <div
                key={tpl.id}
                style={{ ...cardStyle, cursor: "pointer", transition: "box-shadow 0.15s" }}
                onClick={() => applyTemplate(tpl)}
              >
                <div style={{ display: "flex", alignItems: "center", gap: 6, marginBottom: 6 }}>
                  <span style={badgeStyle("#2563eb")}>{tpl.phase}</span>
                  <span style={badgeStyle("#7c3aed")}>{tpl.knu}</span>
                </div>
                <div style={{ fontWeight: 700, fontSize: "0.85rem" }}>{tpl.name}</div>
                <div style={{ fontSize: "0.65rem", color: "#94a3b8", marginTop: 4 }}>
                  {tpl.id} · Domini: {tpl.domains}
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* ════════════════════════════════════════════════════════
       *  TAB: HISTORY
       * ═══════════════════════════════════════════════════════ */}
      {activeTab === "history" && (
        <div>
          {history.length === 0 ? (
            <div style={{ textAlign: "center", padding: 40, color: "#94a3b8" }}>
              Nessun prompt eseguito in questa sessione.
            </div>
          ) : (
            <table style={{ width: "100%", fontSize: "0.75rem", borderCollapse: "collapse" }}>
              <thead>
                <tr style={{ borderBottom: "2px solid #e2e8f0" }}>
                  <th style={{ textAlign: "left", padding: 6 }}>ID</th>
                  <th style={{ textAlign: "left", padding: 6 }}>Timestamp</th>
                  <th style={{ textAlign: "center", padding: 6 }}>Chapter</th>
                  <th style={{ textAlign: "center", padding: 6 }}>Domain</th>
                  <th style={{ textAlign: "center", padding: 6 }}>Phase</th>
                  <th style={{ textAlign: "center", padding: 6 }}>KNU</th>
                  <th style={{ textAlign: "center", padding: 6 }}>PQS</th>
                  <th style={{ textAlign: "center", padding: 6 }}>Status</th>
                </tr>
              </thead>
              <tbody>
                {history.map((h) => {
                  const cls = pqsClass(h.pqs);
                  return (
                    <tr key={h.id} style={{ borderBottom: "1px solid #f1f5f9" }}>
                      <td style={{ padding: 6, fontFamily: "monospace", fontWeight: 600 }}>{h.id}</td>
                      <td style={{ padding: 6, fontSize: "0.65rem" }}>{h.timestamp.slice(0, 19)}</td>
                      <td style={{ padding: 6, textAlign: "center", fontFamily: "monospace" }}>{h.chapter || "—"}</td>
                      <td style={{ padding: 6, textAlign: "center" }}>{h.domain || "—"}</td>
                      <td style={{ padding: 6, textAlign: "center" }}>{h.lcPhase || "—"}</td>
                      <td style={{ padding: 6, textAlign: "center" }}>
                        <span style={badgeStyle("#7c3aed")}>{h.knuType || "—"}</span>
                      </td>
                      <td style={{ padding: 6, textAlign: "center", color: cls.color, fontWeight: 700 }}>
                        {h.pqs} {cls.emoji}
                      </td>
                      <td style={{ padding: 6, textAlign: "center" }}>
                        <span style={badgeStyle(h.status === "ACCEPTED" ? "#16a34a" : "#ca8a04")}>
                          {h.status}
                        </span>
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          )}
        </div>
      )}

      {/* ════════════════════════════════════════════════════════
       *  TAB: METRICS
       * ═══════════════════════════════════════════════════════ */}
      {activeTab === "metrics" && (
        <div>
          <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(160px, 1fr))", gap: 12, marginBottom: 24 }}>
            {[
              { label: "Prompt Eseguiti", value: metrics.total, sub: "sessione corrente" },
              { label: "PQS Medio", value: metrics.avgPqs || "—", sub: "target ≥ 80" },
              { label: "Accettati", value: `${metrics.accepted}/${metrics.total}`, sub: `${metrics.rate}%` },
              { label: "Templates", value: TEMPLATES.length, sub: "disponibili" },
              { label: "Domini", value: DOMAINS.length, sub: "G1–G10" },
              { label: "Verbi APE", value: APE_VERBS.length, sub: "azioni disponibili" },
            ].map((m) => (
              <div key={m.label} style={{ ...cardStyle, textAlign: "center" }}>
                <div style={{ fontSize: "0.7rem", color: "#64748b", marginBottom: 4 }}>{m.label}</div>
                <div style={{ fontSize: "1.5rem", fontWeight: 800 }}>{m.value}</div>
                {m.sub && <div style={{ fontSize: "0.6rem", color: "#94a3b8" }}>{m.sub}</div>}
              </div>
            ))}
          </div>

          {/* Verb usage */}
          <div style={cardStyle}>
            <div style={{ fontSize: "0.85rem", fontWeight: 700, marginBottom: 8 }}>Verbi APE disponibili</div>
            <div style={{ display: "flex", flexWrap: "wrap", gap: 6 }}>
              {APE_VERBS.map((v) => (
                <span
                  key={v.id}
                  style={{
                    padding: "6px 12px",
                    borderRadius: 6,
                    fontSize: "0.75rem",
                    background: "#f1f5f9",
                    border: "1px solid #e2e8f0",
                  }}
                >
                  {v.icon} {v.label}
                  <span style={{ fontSize: "0.6rem", color: "#94a3b8", marginLeft: 6 }}>{v.desc}</span>
                </span>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* ── Footer ── */}
      <div style={{
        marginTop: 32,
        padding: "12px 0",
        borderTop: "1px solid #e2e8f0",
        fontSize: "0.7rem",
        color: "#94a3b8",
      }}>
        APE ADAPT UI Studio v1.0 — GQAOA-APE-ADAPT-001 · SUPIA v1.0 · OPT-INS Framework
        <br />
        Amedeo Pelliccia — GAIA QUANTUM AMPEL OPT-INS ARCHITECTURE, INC. (GQAOA, INC.)
      </div>
    </div>
  );
}
