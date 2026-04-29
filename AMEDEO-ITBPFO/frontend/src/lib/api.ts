/**
 * AMEDEO-ITBPFO API client.
 *
 * Communicates with the FastAPI backend through Next.js rewrites
 * (proxied from /api/* to http://localhost:8000/*).
 */

const API_BASE = "/api";

// ---------------------------------------------------------------------------
// Types
// ---------------------------------------------------------------------------

export interface PipelineStatus {
  entity_id: string;
  state: string;
  ingestion_id: string | null;
  transform_artifact_id: string | null;
  mission: string | null;
  vision: string | null;
  plan_summary: string | null;
  finalized: boolean;
}

export interface FinexRecord {
  entity_id: string;
  entity_scope: string;
  finex_phase: string;
  reason: string;
  authority: string;
  finalized_at: string;
  pipeline_state: string;
  mission: string | null;
  vision: string | null;
  plan_summary: string | null;
  finex_package_path: string | null;
  compliance_refs: string[];
}

export interface FinexStatus {
  entity_id: string;
  finalized: boolean;
  pipeline_state: string | null;
  record: FinexRecord | null;
}

export interface IngestionReceipt {
  ingestion_id: string;
  timestamp: string;
  source_type: string;
  genesis_source: string;
  filename: string | null;
  size_bytes: number;
  status: string;
  pipeline_state: string | null;
}

export interface TransformResponse {
  artifact_id: string;
  ssot_path: string;
  content: Record<string, unknown>;
  derivation: Record<string, unknown>;
  status: string;
  pipeline_state: string | null;
}

export interface FinalizeRequest {
  entity_id: string;
  entity_scope: string;
  finex_phase?: string;
  reason: string;
  authority: string;
  mission?: string;
  vision?: string;
  plan_summary?: string;
  compliance_refs?: string[];
}

// ---------------------------------------------------------------------------
// API functions
// ---------------------------------------------------------------------------

export async function getHealth(): Promise<{ status: string; model: string; version: string }> {
  const res = await fetch(`${API_BASE}/health`);
  if (!res.ok) throw new Error(`Health check failed: ${res.status}`);
  return res.json();
}

export async function getPipelineStatus(entityId: string): Promise<PipelineStatus> {
  const res = await fetch(`${API_BASE}/finex/status/${encodeURIComponent(entityId)}`);
  if (!res.ok) throw new Error(`Failed to get pipeline status: ${res.status}`);
  return res.json();
}

export async function getFinexStatus(entityId: string): Promise<FinexStatus> {
  const res = await fetch(`${API_BASE}/finex/${encodeURIComponent(entityId)}`);
  if (!res.ok) throw new Error(`Failed to get finex status: ${res.status}`);
  return res.json();
}

export async function listFinalized(): Promise<FinexRecord[]> {
  const res = await fetch(`${API_BASE}/finex`);
  if (!res.ok) throw new Error(`Failed to list finalized: ${res.status}`);
  return res.json();
}

export async function ingestFile(
  file: File,
  metadata: {
    source_type: string;
    entity_id?: string;
    genesis_source?: string;
    mission?: string;
    vision?: string;
    plan_summary?: string;
  },
): Promise<IngestionReceipt> {
  const formData = new FormData();
  formData.append("file", file);
  formData.append("metadata", JSON.stringify(metadata));
  const res = await fetch(`${API_BASE}/ingest`, { method: "POST", body: formData });
  if (!res.ok) {
    const detail = await res.json().catch(() => ({ detail: res.statusText }));
    throw new Error(detail.detail || `Ingestion failed: ${res.status}`);
  }
  return res.json();
}

export async function transformData(body: {
  raw_data?: string;
  ingestion_id?: string;
  source_type?: string;
  entity_id?: string;
  uta_chapter?: string;
  lc_phase?: string;
}): Promise<TransformResponse> {
  const res = await fetch(`${API_BASE}/transform`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  if (!res.ok) {
    const detail = await res.json().catch(() => ({ detail: res.statusText }));
    throw new Error(detail.detail || `Transform failed: ${res.status}`);
  }
  return res.json();
}

export async function finalizeEntity(body: FinalizeRequest): Promise<FinexRecord> {
  const res = await fetch(`${API_BASE}/finex`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  if (!res.ok) {
    const detail = await res.json().catch(() => ({ detail: res.statusText }));
    throw new Error(detail.detail || `Finalization failed: ${res.status}`);
  }
  return res.json();
}

export async function finalizePipeline(entityId: string, body: FinalizeRequest): Promise<FinexRecord> {
  const res = await fetch(`${API_BASE}/finex/finalize/${encodeURIComponent(entityId)}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  if (!res.ok) {
    const detail = await res.json().catch(() => ({ detail: res.statusText }));
    throw new Error(detail.detail || `Pipeline finalization failed: ${res.status}`);
  }
  return res.json();
}

export function getFinexDownloadUrl(entityId: string): string {
  return `${API_BASE}/finex/${encodeURIComponent(entityId)}/download`;
}
