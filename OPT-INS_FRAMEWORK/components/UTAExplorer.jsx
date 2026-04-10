/**
 * UTAExplorer — Universal Technology Architecture Explorer
 *
 * Interactive visualisation of the 10-domain, 1000-chapter UTA taxonomy
 * mapped to the OPT-INS 6-axis topology (O / P / T / I / N / S).
 *
 * Programme:  AMPEL360 Q100 · GAIA-SPACE-LAUNCHER · SPACET Q10
 * Version:    UTA v1.0
 * Generated:  2026-04-11
 * Framework:  OPT-INS_FRAMEWORK
 * Owner:      GAIA QUANTUM AMPEL OPT-INS ARCHITECTURE, INC. (GQAOA, INC.)
 */

import { useState, useMemo } from "react";

/* ────────────────────────────────────────────────────────────
 *  DOMAIN GROUPS  (G1 – G10, 100 chapters each → 1 000 total)
 * ────────────────────────────────────────────────────────── */

const DOMAINS = [
  {
    id: "G1", code: "ATA", range: "000–099",
    label: "Aerospace Technology", icon: "✈️", color: "#2563eb", chapters: 100,
    decades: [
      { r: "000–009", t: "Información General y Servicio", axis: "O" },
      { r: "010–019", t: "Manejo en Tierra & Servicio", axis: "P" },
      { r: "020–029", t: "Sistemas Core de Aeronave", axis: "T" },
      { r: "030–039", t: "Protección & Sistemas Mecánicos", axis: "T" },
      { r: "040–049", t: "Aviónica, Información & APU", axis: "T" },
      { r: "050–059", t: "Estructuras Primarias e Interfaces", axis: "T" },
      { r: "060–069", t: "Propulsión Estándar I", axis: "T" },
      { r: "070–079", t: "Propulsión Estándar II", axis: "T" },
      { r: "080–089", t: "Propulsión Alternativa & Cuántica", axis: "T" },
      { r: "090–099", t: "Tipos Específicos & Expansión", axis: "S" },
    ],
  },
  {
    id: "G2", code: "STA", range: "100–199",
    label: "Space Technology", icon: "🚀", color: "#7c3aed", chapters: 100,
    decades: [
      { r: "100–109", t: "Sistemas Generales y Soporte Vital", axis: "S" },
      { r: "110–119", t: "Estructuras y Materiales Espaciales", axis: "S" },
      { r: "120–129", t: "Propulsión Espacial", axis: "S" },
      { r: "130–139", t: "Sistemas de Energía Espacial", axis: "S" },
      { r: "140–149", t: "Aviónica y Control de Misión", axis: "S" },
      { r: "150–159", t: "Comunicaciones Espaciales", axis: "S" },
      { r: "160–169", t: "Sensores y Carga Útil", axis: "S" },
      { r: "170–179", t: "Operaciones en Órbita", axis: "S" },
      { r: "180–189", t: "Infraestructura y Logística Espacial", axis: "I" },
      { r: "190–199", t: "Sistemas Avanzados y Futuro", axis: "S" },
    ],
  },
  {
    id: "G3", code: "DTTA", range: "200–299",
    label: "Defence Technology", icon: "🛡️", color: "#dc2626", chapters: 100,
    decades: [
      { r: "200–209", t: "Sistemas de Combate y Armamento", axis: "T" },
      { r: "210–219", t: "C4ISR", axis: "T" },
      { r: "220–229", t: "Protección y Resiliencia", axis: "T" },
      { r: "230–239", t: "Robótica y Sistemas Autónomos", axis: "T" },
      { r: "240–249", t: "Logística y Mantenimiento Defensa", axis: "P" },
      { r: "250–259", t: "Ciberdefensa y Guerra Electrónica", axis: "N" },
      { r: "260–269", t: "Materiales y Sensores Defensa", axis: "T" },
      { r: "270–279", t: "Simulación y Entrenamiento Militar", axis: "S" },
      { r: "280–289", t: "Guerra Cuántica y Disruptivas", axis: "T" },
      { r: "290–299", t: "Conceptos Operacionales Futuros", axis: "O" },
    ],
  },
  {
    id: "G4", code: "DTCEC", range: "300–399",
    label: "Digital Twin / Cloud / Edge", icon: "🔮", color: "#8b5cf6", chapters: 100,
    decades: [
      { r: "300–309", t: "Fundamentos de Gemelos Digitales", axis: "T" },
      { r: "310–319", t: "Sensores e IoT para DT", axis: "T" },
      { r: "320–329", t: "IA y Machine Learning para DT", axis: "T" },
      { r: "330–339", t: "Cloud y Arquitecturas Distribuidas", axis: "I" },
      { r: "340–349", t: "Simulación y Modelado Avanzado", axis: "S" },
      { r: "350–359", t: "Realidad Extendida (XR) y Metaverso", axis: "T" },
      { r: "360–369", t: "Blockchain y Descentralización", axis: "N" },
      { r: "370–379", t: "Ciberseguridad para DT", axis: "N" },
      { r: "380–389", t: "Analytics y Business Intelligence", axis: "T" },
      { r: "390–399", t: "DT Conscientes y Evolutivos", axis: "T" },
    ],
  },
  {
    id: "G5", code: "EPTA", range: "400–499",
    label: "Energy & Propulsion", icon: "⚡", color: "#ea580c", chapters: 100,
    decades: [
      { r: "400–409", t: "Fuentes de Energía Convencionales", axis: "T" },
      { r: "410–419", t: "Energías Renovables", axis: "T" },
      { r: "420–429", t: "Almacenamiento de Energía", axis: "T" },
      { r: "430–439", t: "Gestión y Distribución de Energía", axis: "T" },
      { r: "440–449", t: "Propulsión por Combustión", axis: "T" },
      { r: "450–459", t: "Propulsión Eléctrica e Híbrida", axis: "T" },
      { r: "460–469", t: "Propulsión H₂ y Celdas de Combustible", axis: "T" },
      { r: "470–479", t: "Nuevas Formas de Propulsión", axis: "T" },
      { r: "480–489", t: "Optimización Energética y Cuántica", axis: "T" },
      { r: "490–499", t: "Recuperación de Energía", axis: "T" },
    ],
  },
  {
    id: "G6", code: "AMTA", range: "500–599",
    label: "Materials / Bio / Nano", icon: "🧬", color: "#16a34a", chapters: 100,
    decades: [
      { r: "500–509", t: "Materiales Compuestos Avanzados", axis: "T" },
      { r: "510–519", t: "Metamateriales e Inteligentes", axis: "T" },
      { r: "520–529", t: "Nanomateriales y Recubrimientos", axis: "T" },
      { r: "530–539", t: "Biotecnología y Bioingeniería", axis: "T" },
      { r: "540–549", t: "Biomateriales y Biónica", axis: "T" },
      { r: "550–559", t: "Nanotecnología y Nanorobótica", axis: "T" },
      { r: "560–569", t: "Sensores Avanzados (Bio/Nano)", axis: "T" },
      { r: "570–579", t: "Manufactura Aditiva Avanzada", axis: "P" },
      { r: "580–589", t: "Materiales y Procesos Cuánticos", axis: "T" },
      { r: "590–599", t: "Reciclaje y Sostenibilidad", axis: "T" },
    ],
  },
  {
    id: "G7", code: "OGATA", range: "600–699",
    label: "Ground Automation", icon: "⚙️", color: "#0891b2", chapters: 100,
    decades: [
      { r: "600–609", t: "Robótica Industrial y Colaborativa", axis: "I" },
      { r: "610–619", t: "Vehículos Autónomos Terrestres", axis: "I" },
      { r: "620–629", t: "Infraestructura Inteligente", axis: "I" },
      { r: "630–639", t: "Fábricas 4.0 y Manufactura", axis: "I" },
      { r: "640–649", t: "Logística y Almacenamiento Auto.", axis: "P" },
      { r: "650–659", t: "Agricultura de Precisión", axis: "I" },
      { r: "660–669", t: "Construcción Automatizada", axis: "I" },
      { r: "670–679", t: "Servicios Autónomos", axis: "I" },
      { r: "680–689", t: "Optimización IA y Cuántica", axis: "T" },
      { r: "690–699", t: "Interacción Humano-Robot", axis: "O" },
    ],
  },
  {
    id: "G8", code: "ACV", range: "700–799",
    label: "Aerial City Viability", icon: "🏙️", color: "#ca8a04", chapters: 100,
    decades: [
      { r: "700–709", t: "Vehículos UAM", axis: "T" },
      { r: "710–719", t: "Vertipuertos", axis: "I" },
      { r: "720–729", t: "Gestión Tráfico Aéreo Urbano", axis: "O" },
      { r: "730–739", t: "Ruido y Acústica Urbana", axis: "T" },
      { r: "740–749", t: "Sostenibilidad Ambiental UAM", axis: "T" },
      { r: "750–759", t: "Legal y Certificación UAM", axis: "O" },
      { r: "760–769", t: "Interfaz Urbana y Social", axis: "O" },
      { r: "770–779", t: "Seguridad Operaciones UAM", axis: "T" },
      { r: "780–789", t: "Tráfico Cuántico Urbano", axis: "T" },
      { r: "790–799", t: "Modelos de Negocio UAM", axis: "O" },
    ],
  },
  {
    id: "G9", code: "CYB", range: "800–899",
    label: "Cybersecurity", icon: "🔒", color: "#e11d48", chapters: 100,
    decades: [
      { r: "800–809", t: "Gobernanza y Gestión de Riesgos", axis: "O" },
      { r: "810–819", t: "Seguridad de Redes", axis: "N" },
      { r: "820–829", t: "Seguridad de Datos", axis: "N" },
      { r: "830–839", t: "IAM — Identidades y Acceso", axis: "N" },
      { r: "840–849", t: "Seguridad de Aplicaciones", axis: "T" },
      { r: "850–859", t: "SecOps — Ciberseguridad Operacional", axis: "N" },
      { r: "860–869", t: "Seguridad Cloud y Edge", axis: "N" },
      { r: "870–879", t: "Ciberseguridad ICS/OT", axis: "N" },
      { r: "880–889", t: "Criptografía Post-Cuántica", axis: "N" },
      { r: "890–899", t: "Inteligencia de Amenazas", axis: "N" },
    ],
  },
  {
    id: "G10", code: "QCSAA", range: "900–999",
    label: "Quantum & Sentient Agency", icon: "🌐", color: "#6d28d9", chapters: 100,
    decades: [
      { r: "900–909", t: "Fundamentos Computación Cuántica", axis: "T" },
      { r: "910–919", t: "Quantum ML y AI Cuántica", axis: "T" },
      { r: "920–929", t: "Redes Cuánticas", axis: "N" },
      { r: "930–939", t: "Ciberseguridad Cuántica", axis: "N" },
      { r: "940–949", t: "Sensores y Metrología Cuántica", axis: "S" },
      { r: "950–959", t: "Simulación Cuántica", axis: "S" },
      { r: "960–969", t: "Robótica Cuántica", axis: "T" },
      { r: "970–979", t: "Conciencia y Agencia Sentiente", axis: "T" },
      { r: "980–989", t: "Gobernanza y Ética IA/Cuántica", axis: "O" },
      { r: "990–999", t: "Futuro y Inter-Arquitectura", axis: "T" },
    ],
  },
];

/* ────────────────────────────────────────────────────────────
 *  6-AXIS DEFINITIONS  (OPT-INS topology)
 * ────────────────────────────────────────────────────────── */

const AXES = {
  O: { label: "Organizations", color: "#2563eb" },
  P: { label: "Programs", color: "#16a34a" },
  T: { label: "Technologies", color: "#ea580c" },
  I: { label: "Infrastructures", color: "#0891b2" },
  N: { label: "Neural Networks", color: "#7c3aed" },
  S: { label: "SIM-TEST / Space", color: "#e11d48" },
};

/* ────────────────────────────────────────────────────────────
 *  PROGRAMMES
 * ────────────────────────────────────────────────────────── */

const PROGRAMMES = [
  { id: "Q100",   label: "AMPEL360 Q100",       domains: ["G1","G4","G5","G6","G9"],             color: "#2563eb" },
  { id: "GAIA",   label: "GAIA-SPACE-LAUNCHER",  domains: ["G1","G2","G4","G5","G6","G9","G10"],  color: "#7c3aed" },
  { id: "SPACET", label: "SPACET Q10",           domains: ["G1","G2","G4","G5","G9","G10"],       color: "#e11d48" },
];

/* ────────────────────────────────────────────────────────────
 *  LIFECYCLE PHASES  (LC01 – LC14)
 * ────────────────────────────────────────────────────────── */

const LC_PHASES = [
  "LC01 Problem Statement",
  "LC02 Requirements",
  "LC03 Safety",
  "LC04 Design",
  "LC05 Analysis",
  "LC06 Verification",
  "LC07 Validation",
  "LC08 Configuration",
  "LC09 Production",
  "LC10 Operations",
  "LC11 Maintenance",
  "LC12 Customer Care",
  "LC13 Training",
  "LC14 Retirement/Circularity",
];

/* ────────────────────────────────────────────────────────────
 *  STAT CARD  (reusable presentational component)
 * ────────────────────────────────────────────────────────── */

function StatCard({ label, value, sub }) {
  return (
    <div style={{
      padding: "1rem",
      borderRadius: "0.5rem",
      background: "#f8fafc",
      border: "1px solid #e2e8f0",
      textAlign: "center",
      minWidth: 120,
    }}>
      <div style={{ fontSize: "0.75rem", color: "#64748b", marginBottom: 4 }}>{label}</div>
      <div style={{ fontSize: "1.5rem", fontWeight: 700 }}>{value}</div>
      {sub && <div style={{ fontSize: "0.7rem", color: "#94a3b8", marginTop: 2 }}>{sub}</div>}
    </div>
  );
}

/* ────────────────────────────────────────────────────────────
 *  MAIN COMPONENT — UTAExplorer
 * ────────────────────────────────────────────────────────── */

export default function UTAExplorer() {
  const [selected, setSelected] = useState(null);
  const [axisFilter, setAxisFilter] = useState(null);
  const [progFilter, setProgFilter] = useState(null);
  const [view, setView] = useState("grid"); // grid | backbone | stats

  /* --- derived data ---------------------------------------------------- */

  const filtered = useMemo(() => {
    let d = DOMAINS;
    if (progFilter) {
      const p = PROGRAMMES.find((x) => x.id === progFilter);
      d = d.filter((x) => p.domains.includes(x.id));
    }
    return d;
  }, [progFilter]);

  const totalDecades = filtered.reduce((a, d) => a + d.decades.length, 0);

  const axisDecades = useMemo(() => {
    const m = {};
    filtered.forEach((d) =>
      d.decades.forEach((dec) => {
        m[dec.axis] = (m[dec.axis] || 0) + 1;
      })
    );
    return m;
  }, [filtered]);

  const totalChapters = filtered.reduce((a, d) => a + d.chapters, 0);

  /* --- render ---------------------------------------------------------- */

  return (
    <div style={{ fontFamily: "system-ui, sans-serif", maxWidth: 1200, margin: "0 auto", padding: 24 }}>
      {/* ── Header ── */}
      <h1 style={{ fontSize: "1.75rem", fontWeight: 800, marginBottom: 4 }}>
        🌐 Universal Technology Architecture (UTA) Explorer
      </h1>
      <p style={{ color: "#64748b", marginBottom: 24 }}>
        OPT-INS 6-Axis · {totalChapters.toLocaleString()} chapters · {filtered.length} domains · {totalDecades} decades
      </p>

      {/* ── Controls ── */}
      <div style={{ display: "flex", gap: 8, flexWrap: "wrap", marginBottom: 24 }}>
        {/* Programme filter */}
        <select
          value={progFilter || ""}
          onChange={(e) => setProgFilter(e.target.value || null)}
          style={{ padding: "6px 12px", borderRadius: 6, border: "1px solid #cbd5e1" }}
        >
          <option value="">All Programmes</option>
          {PROGRAMMES.map((p) => (
            <option key={p.id} value={p.id}>{p.label}</option>
          ))}
        </select>

        {/* Axis filter */}
        <select
          value={axisFilter || ""}
          onChange={(e) => setAxisFilter(e.target.value || null)}
          style={{ padding: "6px 12px", borderRadius: 6, border: "1px solid #cbd5e1" }}
        >
          <option value="">All Axes</option>
          {Object.entries(AXES).map(([k, v]) => (
            <option key={k} value={k}>{k} — {v.label}</option>
          ))}
        </select>

        {/* View toggle */}
        {["grid", "backbone", "stats"].map((v) => (
          <button
            key={v}
            onClick={() => setView(v)}
            style={{
              padding: "6px 16px",
              borderRadius: 6,
              border: view === v ? "2px solid #2563eb" : "1px solid #cbd5e1",
              background: view === v ? "#eff6ff" : "#fff",
              fontWeight: view === v ? 700 : 400,
              cursor: "pointer",
              textTransform: "capitalize",
            }}
          >
            {v}
          </button>
        ))}
      </div>

      {/* ── Stat Cards ── */}
      <div style={{ display: "flex", gap: 12, flexWrap: "wrap", marginBottom: 24 }}>
        <StatCard label="Domains" value={filtered.length} sub="of 10" />
        <StatCard label="Chapters" value={totalChapters.toLocaleString()} sub="total" />
        <StatCard label="Decades" value={totalDecades} sub="decade blocks" />
        <StatCard label="Axes" value={Object.keys(AXES).length} sub="O P T I N S" />
        <StatCard label="LC Phases" value={LC_PHASES.length} sub="LC01–LC14" />
      </div>

      {/* ── Axis Legend ── */}
      <div style={{ display: "flex", gap: 12, flexWrap: "wrap", marginBottom: 24 }}>
        {Object.entries(AXES).map(([k, v]) => (
          <span
            key={k}
            onClick={() => setAxisFilter(axisFilter === k ? null : k)}
            style={{
              padding: "4px 12px",
              borderRadius: 999,
              fontSize: "0.75rem",
              fontWeight: 600,
              color: "#fff",
              background: v.color,
              cursor: "pointer",
              opacity: !axisFilter || axisFilter === k ? 1 : 0.3,
            }}
          >
            {k} — {v.label} ({axisDecades[k] || 0})
          </span>
        ))}
      </div>

      {/* ── View: GRID ── */}
      {view === "grid" && (
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(280px, 1fr))", gap: 16 }}>
          {filtered.map((dom) => (
            <div
              key={dom.id}
              onClick={() => setSelected(selected === dom.id ? null : dom.id)}
              style={{
                border: `2px solid ${dom.color}22`,
                borderRadius: 12,
                padding: 16,
                cursor: "pointer",
                background: selected === dom.id ? `${dom.color}08` : "#fff",
                transition: "all 0.15s",
              }}
            >
              <div style={{ display: "flex", alignItems: "center", gap: 8, marginBottom: 8 }}>
                <span style={{ fontSize: "1.5rem" }}>{dom.icon}</span>
                <div>
                  <div style={{ fontWeight: 700, fontSize: "0.9rem" }}>{dom.label}</div>
                  <div style={{ fontSize: "0.7rem", color: "#94a3b8" }}>
                    {dom.code} · {dom.range} · {dom.chapters} ch.
                  </div>
                </div>
              </div>
              {selected === dom.id && (
                <table style={{ width: "100%", fontSize: "0.75rem", borderCollapse: "collapse", marginTop: 8 }}>
                  <thead>
                    <tr style={{ borderBottom: "1px solid #e2e8f0" }}>
                      <th style={{ textAlign: "left", padding: 4 }}>Range</th>
                      <th style={{ textAlign: "left", padding: 4 }}>Topic</th>
                      <th style={{ textAlign: "center", padding: 4 }}>Axis</th>
                    </tr>
                  </thead>
                  <tbody>
                    {dom.decades
                      .filter((dec) => !axisFilter || dec.axis === axisFilter)
                      .map((dec, i) => (
                        <tr key={i} style={{ borderBottom: "1px solid #f1f5f9" }}>
                          <td style={{ padding: 4, fontFamily: "monospace" }}>{dec.r}</td>
                          <td style={{ padding: 4 }}>{dec.t}</td>
                          <td style={{ padding: 4, textAlign: "center" }}>
                            <span style={{
                              padding: "2px 6px",
                              borderRadius: 4,
                              fontSize: "0.65rem",
                              fontWeight: 700,
                              color: "#fff",
                              background: AXES[dec.axis]?.color || "#888",
                            }}>
                              {dec.axis}
                            </span>
                          </td>
                        </tr>
                      ))}
                  </tbody>
                </table>
              )}
            </div>
          ))}
        </div>
      )}

      {/* ── View: BACKBONE ── */}
      {view === "backbone" && (
        <div>
          <h2 style={{ fontSize: "1.1rem", fontWeight: 700, marginBottom: 12 }}>
            Backbone — Axis Distribution
          </h2>
          {Object.entries(AXES).map(([axKey, axVal]) => {
            const matchingDecades = [];
            filtered.forEach((dom) =>
              dom.decades.forEach((dec) => {
                if (dec.axis === axKey && (!axisFilter || axisFilter === axKey)) {
                  matchingDecades.push({ ...dec, domain: dom.code, domColor: dom.color });
                }
              })
            );
            if (axisFilter && axisFilter !== axKey) return null;
            return (
              <div key={axKey} style={{ marginBottom: 16 }}>
                <div style={{
                  display: "inline-block",
                  padding: "4px 12px",
                  borderRadius: 6,
                  fontSize: "0.8rem",
                  fontWeight: 700,
                  color: "#fff",
                  background: axVal.color,
                  marginBottom: 8,
                }}>
                  {axKey} — {axVal.label} ({matchingDecades.length} decades)
                </div>
                <div style={{ display: "flex", flexWrap: "wrap", gap: 4, marginLeft: 8 }}>
                  {matchingDecades.map((md, i) => (
                    <span
                      key={i}
                      title={`${md.domain} ${md.r}: ${md.t}`}
                      style={{
                        padding: "2px 8px",
                        borderRadius: 4,
                        fontSize: "0.65rem",
                        background: `${md.domColor}18`,
                        border: `1px solid ${md.domColor}44`,
                        color: md.domColor,
                        fontFamily: "monospace",
                      }}
                    >
                      {md.domain} {md.r}
                    </span>
                  ))}
                </div>
              </div>
            );
          })}
        </div>
      )}

      {/* ── View: STATS ── */}
      {view === "stats" && (
        <div>
          <h2 style={{ fontSize: "1.1rem", fontWeight: 700, marginBottom: 12 }}>
            Statistics — Axis × Domain Heat Map
          </h2>
          <table style={{ width: "100%", fontSize: "0.75rem", borderCollapse: "collapse" }}>
            <thead>
              <tr>
                <th style={{ textAlign: "left", padding: 6 }}>Domain</th>
                {Object.keys(AXES).map((a) => (
                  <th key={a} style={{ textAlign: "center", padding: 6, color: AXES[a].color }}>{a}</th>
                ))}
                <th style={{ textAlign: "center", padding: 6 }}>Total</th>
              </tr>
            </thead>
            <tbody>
              {filtered.map((dom) => {
                const counts = {};
                dom.decades.forEach((d) => { counts[d.axis] = (counts[d.axis] || 0) + 1; });
                return (
                  <tr key={dom.id} style={{ borderBottom: "1px solid #f1f5f9" }}>
                    <td style={{ padding: 6, fontWeight: 600 }}>
                      {dom.icon} {dom.code}
                    </td>
                    {Object.keys(AXES).map((a) => (
                      <td key={a} style={{
                        textAlign: "center",
                        padding: 6,
                        background: counts[a] ? `${AXES[a].color}18` : "transparent",
                        fontWeight: counts[a] ? 700 : 400,
                        color: counts[a] ? AXES[a].color : "#cbd5e1",
                      }}>
                        {counts[a] || "—"}
                      </td>
                    ))}
                    <td style={{ textAlign: "center", padding: 6, fontWeight: 700 }}>
                      {dom.decades.length}
                    </td>
                  </tr>
                );
              })}
              {/* Totals row */}
              <tr style={{ borderTop: "2px solid #e2e8f0", fontWeight: 700 }}>
                <td style={{ padding: 6 }}>TOTAL</td>
                {Object.keys(AXES).map((a) => (
                  <td key={a} style={{ textAlign: "center", padding: 6, color: AXES[a].color }}>
                    {axisDecades[a] || 0}
                  </td>
                ))}
                <td style={{ textAlign: "center", padding: 6 }}>{totalDecades}</td>
              </tr>
            </tbody>
          </table>

          {/* Programme coverage */}
          <h3 style={{ fontSize: "0.95rem", fontWeight: 700, marginTop: 24, marginBottom: 8 }}>
            Programme Coverage
          </h3>
          <table style={{ width: "100%", fontSize: "0.75rem", borderCollapse: "collapse" }}>
            <thead>
              <tr>
                <th style={{ textAlign: "left", padding: 6 }}>Programme</th>
                <th style={{ textAlign: "center", padding: 6 }}>Domains</th>
                <th style={{ textAlign: "center", padding: 6 }}>Chapters</th>
                <th style={{ textAlign: "left", padding: 6 }}>Domain Codes</th>
              </tr>
            </thead>
            <tbody>
              {PROGRAMMES.map((p) => {
                const domCount = p.domains.length;
                const chapCount = DOMAINS.filter((d) => p.domains.includes(d.id))
                  .reduce((a, d) => a + d.chapters, 0);
                const codes = DOMAINS.filter((d) => p.domains.includes(d.id))
                  .map((d) => d.code)
                  .join(", ");
                return (
                  <tr key={p.id} style={{ borderBottom: "1px solid #f1f5f9" }}>
                    <td style={{ padding: 6, fontWeight: 600, color: p.color }}>{p.label}</td>
                    <td style={{ textAlign: "center", padding: 6 }}>{domCount}</td>
                    <td style={{ textAlign: "center", padding: 6 }}>{chapCount.toLocaleString()}</td>
                    <td style={{ padding: 6, fontFamily: "monospace", fontSize: "0.7rem" }}>{codes}</td>
                  </tr>
                );
              })}
            </tbody>
          </table>

          {/* Lifecycle phases */}
          <h3 style={{ fontSize: "0.95rem", fontWeight: 700, marginTop: 24, marginBottom: 8 }}>
            Lifecycle Phases (LC01–LC14)
          </h3>
          <div style={{ display: "flex", flexWrap: "wrap", gap: 6 }}>
            {LC_PHASES.map((lc, i) => (
              <span
                key={i}
                style={{
                  padding: "4px 10px",
                  borderRadius: 6,
                  fontSize: "0.7rem",
                  background: "#f1f5f9",
                  border: "1px solid #e2e8f0",
                }}
              >
                {lc}
              </span>
            ))}
          </div>
        </div>
      )}

      {/* ── Footer ── */}
      <div style={{ marginTop: 32, padding: "12px 0", borderTop: "1px solid #e2e8f0", fontSize: "0.7rem", color: "#94a3b8" }}>
        UTA Explorer v1.0 — OPT-INS Framework · AMPEL360 Q100 · GAIA-SPACE-LAUNCHER · SPACET Q10
        <br />
        Amedeo Pelliccia — GAIA QUANTUM AMPEL OPT-INS ARCHITECTURE, INC. (GQAOA, INC.)
      </div>
    </div>
  );
}
