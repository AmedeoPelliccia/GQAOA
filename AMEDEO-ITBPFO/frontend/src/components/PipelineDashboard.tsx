"use client";

import { useEffect, useState, useCallback } from "react";
import type { PipelineStatus } from "@/lib/api";
import { getPipelineStatus, getFinexDownloadUrl } from "@/lib/api";

// ---------------------------------------------------------------------------
// Pipeline state → visual config
// ---------------------------------------------------------------------------

const STATE_CONFIG: Record<string, { label: string; color: string; icon: string }> = {
  UNKNOWN: { label: "Not Started", color: "bg-gray-100 text-gray-700 border-gray-300", icon: "⏳" },
  PENDING: { label: "Pending", color: "bg-yellow-50 text-yellow-800 border-yellow-400", icon: "📋" },
  INGESTED: { label: "Ingested", color: "bg-blue-50 text-blue-800 border-blue-400", icon: "📥" },
  TRANSFORMED: { label: "Transformed", color: "bg-green-50 text-green-800 border-green-400", icon: "⚡" },
  TERMINAL: { label: "🔒 TERMINAL — FINEX SEALED", color: "bg-red-50 text-red-800 border-red-500", icon: "🔒" },
};

const STEP_ORDER = ["PENDING", "INGESTED", "TRANSFORMED", "TERMINAL"];

// ---------------------------------------------------------------------------
// Component
// ---------------------------------------------------------------------------

interface Props {
  entityId: string;
  /** Polling interval in milliseconds (0 = no polling). */
  pollInterval?: number;
  /** Called when status changes. */
  onStatusChange?: (status: PipelineStatus) => void;
}

export default function PipelineDashboard({ entityId, pollInterval = 3000, onStatusChange }: Props) {
  const [status, setStatus] = useState<PipelineStatus | null>(null);
  const [error, setError] = useState<string | null>(null);

  const fetchStatus = useCallback(async () => {
    try {
      const data = await getPipelineStatus(entityId);
      setStatus(data);
      setError(null);
      onStatusChange?.(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to fetch status");
    }
  }, [entityId, onStatusChange]);

  useEffect(() => {
    fetchStatus();
    if (pollInterval > 0) {
      const timer = setInterval(fetchStatus, pollInterval);
      return () => clearInterval(timer);
    }
  }, [fetchStatus, pollInterval]);

  if (error) {
    return (
      <div className="rounded-lg border border-amber-300 bg-amber-50 p-4">
        <p className="text-sm text-amber-800">⚠️ {error}</p>
      </div>
    );
  }

  if (!status) {
    return (
      <div className="animate-pulse rounded-lg border border-gray-200 bg-gray-50 p-6">
        <div className="h-4 w-48 rounded bg-gray-200" />
      </div>
    );
  }

  const currentState = status.state;
  const config = STATE_CONFIG[currentState] ?? STATE_CONFIG.UNKNOWN;
  const isTerminal = currentState === "TERMINAL";
  const currentIdx = STEP_ORDER.indexOf(currentState);

  return (
    <div className={`rounded-lg border-2 p-6 ${config.color}`}>
      {/* Header */}
      <div className="mb-4 flex items-center justify-between">
        <h2 className="text-xl font-bold">
          {config.icon} {config.label}
        </h2>
        <span className="rounded-full bg-white/60 px-3 py-1 text-xs font-mono">{entityId}</span>
      </div>

      {/* Pipeline progress bar */}
      <div className="mb-6">
        <div className="flex items-center justify-between">
          {STEP_ORDER.map((step, idx) => {
            const stepConfig = STATE_CONFIG[step];
            const isActive = idx <= currentIdx;
            const isCurrent = step === currentState;
            return (
              <div key={step} className="flex flex-1 items-center">
                <div
                  className={`flex h-10 w-10 items-center justify-center rounded-full text-sm font-bold transition-all ${
                    isCurrent
                      ? "ring-2 ring-offset-2 ring-current bg-white shadow-lg scale-110"
                      : isActive
                        ? "bg-white/80 shadow"
                        : "bg-gray-200 text-gray-400"
                  }`}
                >
                  {stepConfig.icon}
                </div>
                {idx < STEP_ORDER.length - 1 && (
                  <div
                    className={`mx-1 h-1 flex-1 rounded ${
                      idx < currentIdx ? "bg-current opacity-40" : "bg-gray-200"
                    }`}
                  />
                )}
              </div>
            );
          })}
        </div>
        <div className="mt-2 flex justify-between text-xs">
          {STEP_ORDER.map((step) => (
            <span key={step} className="flex-1 text-center">
              {step}
            </span>
          ))}
        </div>
      </div>

      {/* Mission / Vision / Plan */}
      {(status.mission || status.vision || status.plan_summary) && (
        <div className="mb-4 grid gap-2 sm:grid-cols-3">
          {status.mission && (
            <div className="rounded bg-white/50 p-2">
              <span className="text-xs font-semibold uppercase tracking-wider">Mission</span>
              <p className="text-sm">{status.mission}</p>
            </div>
          )}
          {status.vision && (
            <div className="rounded bg-white/50 p-2">
              <span className="text-xs font-semibold uppercase tracking-wider">Vision</span>
              <p className="text-sm">{status.vision}</p>
            </div>
          )}
          {status.plan_summary && (
            <div className="rounded bg-white/50 p-2">
              <span className="text-xs font-semibold uppercase tracking-wider">Plan</span>
              <p className="text-sm">{status.plan_summary}</p>
            </div>
          )}
        </div>
      )}

      {/* Download button (terminal only) */}
      {isTerminal && (
        <a
          href={getFinexDownloadUrl(entityId)}
          className="mt-2 inline-flex items-center gap-2 rounded bg-blue-600 px-4 py-2 text-sm font-medium text-white shadow hover:bg-blue-700 transition"
          download
        >
          📦 Download .finex Package
        </a>
      )}
    </div>
  );
}
