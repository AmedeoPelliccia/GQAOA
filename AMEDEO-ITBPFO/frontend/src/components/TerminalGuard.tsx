"use client";

import { useEffect, useState } from "react";
import type { FinexStatus } from "@/lib/api";
import { getFinexStatus, getFinexDownloadUrl } from "@/lib/api";

/**
 * TerminalGuard renders a hard-lock UI overlay when the entity is finalized.
 * All interactive controls are disabled; only the .finex download is available.
 */

interface Props {
  entityId: string;
  /** Content to render when the entity is NOT finalized. */
  children: React.ReactNode;
}

export default function TerminalGuard({ entityId, children }: Props) {
  const [status, setStatus] = useState<FinexStatus | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let cancelled = false;
    (async () => {
      try {
        const data = await getFinexStatus(entityId);
        if (!cancelled) setStatus(data);
      } finally {
        if (!cancelled) setLoading(false);
      }
    })();
    return () => {
      cancelled = true;
    };
  }, [entityId]);

  if (loading) {
    return (
      <div className="flex items-center justify-center p-8">
        <div className="h-8 w-8 animate-spin rounded-full border-4 border-gray-300 border-t-blue-600" />
      </div>
    );
  }

  // Entity is sealed — show terminal lock overlay
  if (status?.finalized && status.record) {
    const record = status.record;
    return (
      <div className="rounded-xl border-4 border-red-500 bg-red-50 p-6 shadow-lg">
        <div className="mb-4 flex items-center gap-3">
          <div className="flex h-12 w-12 items-center justify-center rounded-full bg-red-600 text-2xl text-white shadow">
            🔒
          </div>
          <div>
            <h2 className="text-2xl font-extrabold text-red-800">TERMINAL STATE: FINEX SEALED</h2>
            <p className="text-sm text-red-600">
              No further transformation, derivation, or stock requests are permitted.
            </p>
          </div>
        </div>

        <div className="mb-4 grid gap-3 sm:grid-cols-2">
          <InfoField label="Entity" value={record.entity_id} />
          <InfoField label="Scope" value={record.entity_scope} />
          <InfoField label="Phase" value={record.finex_phase} />
          <InfoField label="Finalized" value={new Date(record.finalized_at).toLocaleString()} />
          <InfoField label="Reason" value={record.reason} />
          <InfoField label="Authority" value={record.authority} />
          {record.mission && <InfoField label="Mission" value={record.mission} />}
          {record.vision && <InfoField label="Vision" value={record.vision} />}
          {record.plan_summary && <InfoField label="Plan" value={record.plan_summary} />}
        </div>

        {record.compliance_refs.length > 0 && (
          <div className="mb-4">
            <span className="text-xs font-semibold uppercase tracking-wider text-red-700">Compliance</span>
            <div className="mt-1 flex flex-wrap gap-1">
              {record.compliance_refs.map((ref) => (
                <span key={ref} className="rounded bg-red-100 px-2 py-0.5 text-xs font-mono text-red-800">
                  {ref}
                </span>
              ))}
            </div>
          </div>
        )}

        <a
          href={getFinexDownloadUrl(entityId)}
          className="inline-flex items-center gap-2 rounded-lg bg-blue-600 px-5 py-3 text-sm font-semibold text-white shadow-md hover:bg-blue-700 transition"
          download
        >
          📦 Download .finex Package
        </a>
      </div>
    );
  }

  // Not finalized — render children normally
  return <>{children}</>;
}

function InfoField({ label, value }: { label: string; value: string }) {
  return (
    <div className="rounded bg-white/70 p-2">
      <span className="text-xs font-semibold uppercase tracking-wider text-red-700">{label}</span>
      <p className="text-sm text-red-900">{value}</p>
    </div>
  );
}
