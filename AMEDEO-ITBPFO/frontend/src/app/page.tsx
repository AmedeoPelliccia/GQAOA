"use client";

import { useState, useCallback } from "react";
import PipelineDashboard from "@/components/PipelineDashboard";
import TerminalGuard from "@/components/TerminalGuard";
import MissionVisionCard from "@/components/MissionVisionCard";
import type { PipelineStatus, FinalizeRequest } from "@/lib/api";
import { ingestFile, transformData, finalizeEntity } from "@/lib/api";

const ENTITY_SCOPES = ["organization", "repository", "program", "company", "enterprise"] as const;

export default function HomePage() {
  const [entityId, setEntityId] = useState("");
  const [activeEntity, setActiveEntity] = useState<string | null>(null);
  const [status, setStatus] = useState<PipelineStatus | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  // Finalize form
  const [scope, setScope] = useState<string>("program");
  const [reason, setReason] = useState("");
  const [authority, setAuthority] = useState("");
  const [mission, setMission] = useState("");
  const [vision, setVision] = useState("");
  const [planSummary, setPlanSummary] = useState("");

  const handleTrack = () => {
    if (entityId.trim()) {
      setActiveEntity(entityId.trim());
      setError(null);
    }
  };

  const handleStatusChange = useCallback((s: PipelineStatus) => {
    setStatus(s);
  }, []);

  const handleIngest = async () => {
    if (!activeEntity) return;
    setBusy(true);
    setError(null);
    try {
      const blob = new Blob(["sample input data"], { type: "text/plain" });
      const file = new File([blob], "input.txt", { type: "text/plain" });
      await ingestFile(file, {
        source_type: "text",
        entity_id: activeEntity,
        mission: mission || undefined,
        vision: vision || undefined,
        plan_summary: planSummary || undefined,
      });
    } catch (err) {
      setError(err instanceof Error ? err.message : "Ingestion failed");
    } finally {
      setBusy(false);
    }
  };

  const handleTransform = async () => {
    if (!activeEntity) return;
    setBusy(true);
    setError(null);
    try {
      await transformData({
        raw_data: "sample transformation payload",
        source_type: "text",
        entity_id: activeEntity,
      });
    } catch (err) {
      setError(err instanceof Error ? err.message : "Transform failed");
    } finally {
      setBusy(false);
    }
  };

  const handleFinalize = async () => {
    if (!activeEntity || !reason || !authority) return;
    setBusy(true);
    setError(null);
    try {
      const body: FinalizeRequest = {
        entity_id: activeEntity,
        entity_scope: scope,
        reason,
        authority,
        mission: mission || undefined,
        vision: vision || undefined,
        plan_summary: planSummary || undefined,
        compliance_refs: ["STD_Metadata-Schema-Guide_rev1.1.0", "ISO_27001"],
      };
      await finalizeEntity(body);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Finalization failed");
    } finally {
      setBusy(false);
    }
  };

  const isTerminal = status?.state === "TERMINAL" || status?.finalized;
  const canIngest = activeEntity && !isTerminal && (!status || status.state === "UNKNOWN" || status.state === "PENDING");
  const canTransform = activeEntity && !isTerminal && status?.state === "INGESTED";
  const canFinalize = activeEntity && !isTerminal && status?.state === "TRANSFORMED";

  return (
    <div className="space-y-6">
      <section>
        <h2 className="mb-2 text-2xl font-bold">Pipeline Dashboard</h2>
        <p className="mb-4 text-sm text-gray-600">
          Track an entity through the AMEDEO-ITBPFO pipeline: PENDING → INGESTED → TRANSFORMED → TERMINAL.
        </p>

        <div className="flex gap-2">
          <input
            type="text"
            value={entityId}
            onChange={(e) => setEntityId(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleTrack()}
            placeholder="Enter entity ID (e.g. ORG-001)"
            className="flex-1 rounded-lg border border-gray-300 px-4 py-2 text-sm focus:border-blue-500 focus:ring-1 focus:ring-blue-500"
          />
          <button
            onClick={handleTrack}
            className="rounded-lg bg-blue-600 px-6 py-2 text-sm font-medium text-white hover:bg-blue-700"
          >
            Track
          </button>
        </div>
      </section>

      {error && (
        <div className="rounded-lg border border-red-200 bg-red-50 p-3 text-sm text-red-800">
          ⚠️ {error}
        </div>
      )}

      {activeEntity && (
        <TerminalGuard entityId={activeEntity}>
          <div className="space-y-6">
            <PipelineDashboard
              entityId={activeEntity}
              pollInterval={2000}
              onStatusChange={handleStatusChange}
            />

            <MissionVisionCard
              mission={status?.mission}
              vision={status?.vision}
              planSummary={status?.plan_summary}
            />

            {/* Mission / Vision / Plan input */}
            <section className="rounded-lg border border-gray-200 bg-white p-5">
              <h3 className="mb-3 text-lg font-bold">🎯 Mission / Vision / Plan</h3>
              <div className="grid gap-3 sm:grid-cols-3">
                <div>
                  <label className="mb-1 block text-xs font-semibold text-gray-600">Mission</label>
                  <input
                    type="text"
                    value={mission}
                    onChange={(e) => setMission(e.target.value)}
                    placeholder="Mission statement..."
                    className="w-full rounded border border-gray-300 px-3 py-2 text-sm"
                  />
                </div>
                <div>
                  <label className="mb-1 block text-xs font-semibold text-gray-600">Vision</label>
                  <input
                    type="text"
                    value={vision}
                    onChange={(e) => setVision(e.target.value)}
                    placeholder="Vision statement..."
                    className="w-full rounded border border-gray-300 px-3 py-2 text-sm"
                  />
                </div>
                <div>
                  <label className="mb-1 block text-xs font-semibold text-gray-600">Plan Summary</label>
                  <input
                    type="text"
                    value={planSummary}
                    onChange={(e) => setPlanSummary(e.target.value)}
                    placeholder="Plan summary..."
                    className="w-full rounded border border-gray-300 px-3 py-2 text-sm"
                  />
                </div>
              </div>
            </section>

            {/* Action buttons */}
            <section className="flex flex-wrap gap-3">
              <button
                onClick={handleIngest}
                disabled={!canIngest || busy}
                className="rounded-lg bg-blue-600 px-5 py-2.5 text-sm font-medium text-white shadow hover:bg-blue-700 disabled:cursor-not-allowed disabled:opacity-40"
              >
                📥 Ingest
              </button>
              <button
                onClick={handleTransform}
                disabled={!canTransform || busy}
                className="rounded-lg bg-green-600 px-5 py-2.5 text-sm font-medium text-white shadow hover:bg-green-700 disabled:cursor-not-allowed disabled:opacity-40"
              >
                ⚡ Transform
              </button>
            </section>

            {/* Finalize form */}
            {canFinalize && (
              <section className="rounded-lg border-2 border-amber-300 bg-amber-50 p-5">
                <h3 className="mb-3 text-lg font-bold text-amber-900">
                  🔐 Finalize to FINEX (Terminal Lock)
                </h3>
                <p className="mb-4 text-sm text-amber-700">
                  This action is <strong>irreversible</strong>. A sealed <code>.finex</code> package
                  will be generated and all further requests on this entity will be permanently blocked.
                </p>
                <div className="mb-4 grid gap-3 sm:grid-cols-2">
                  <div>
                    <label className="mb-1 block text-xs font-semibold text-amber-800">Entity Scope</label>
                    <select
                      value={scope}
                      onChange={(e) => setScope(e.target.value)}
                      className="w-full rounded border border-amber-300 bg-white px-3 py-2 text-sm"
                    >
                      {ENTITY_SCOPES.map((s) => (
                        <option key={s} value={s}>
                          {s}
                        </option>
                      ))}
                    </select>
                  </div>
                  <div>
                    <label className="mb-1 block text-xs font-semibold text-amber-800">Authority</label>
                    <input
                      type="text"
                      value={authority}
                      onChange={(e) => setAuthority(e.target.value)}
                      placeholder="Approving authority..."
                      className="w-full rounded border border-amber-300 px-3 py-2 text-sm"
                    />
                  </div>
                  <div className="sm:col-span-2">
                    <label className="mb-1 block text-xs font-semibold text-amber-800">Reason</label>
                    <input
                      type="text"
                      value={reason}
                      onChange={(e) => setReason(e.target.value)}
                      placeholder="Reason for finalization..."
                      className="w-full rounded border border-amber-300 px-3 py-2 text-sm"
                    />
                  </div>
                </div>
                <button
                  onClick={handleFinalize}
                  disabled={!reason || !authority || busy}
                  className="rounded-lg bg-red-600 px-6 py-2.5 text-sm font-bold text-white shadow-md hover:bg-red-700 disabled:cursor-not-allowed disabled:opacity-40"
                >
                  🔐 Seal & Lock (FINEX)
                </button>
              </section>
            )}
          </div>
        </TerminalGuard>
      )}
    </div>
  );
}
