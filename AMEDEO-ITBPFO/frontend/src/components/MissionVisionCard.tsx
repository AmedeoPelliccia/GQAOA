"use client";

/**
 * MissionVisionCard displays the mission, vision, and plan alignment
 * for an entity, with compliance badges.
 */

interface Props {
  mission?: string | null;
  vision?: string | null;
  planSummary?: string | null;
  complianceRefs?: string[];
}

export default function MissionVisionCard({ mission, vision, planSummary, complianceRefs = [] }: Props) {
  const hasContent = mission || vision || planSummary;
  if (!hasContent) return null;

  return (
    <div className="rounded-lg border border-indigo-200 bg-indigo-50 p-5">
      <h3 className="mb-3 text-lg font-bold text-indigo-900">🎯 Mission / Vision / Plan</h3>

      <div className="grid gap-3 sm:grid-cols-3">
        {mission && (
          <Card
            title="Mission"
            icon="🚀"
            description={mission}
          />
        )}
        {vision && (
          <Card
            title="Vision"
            icon="🔭"
            description={vision}
          />
        )}
        {planSummary && (
          <Card
            title="Plan"
            icon="📋"
            description={planSummary}
          />
        )}
      </div>

      {complianceRefs.length > 0 && (
        <div className="mt-4">
          <span className="text-xs font-semibold uppercase tracking-wider text-indigo-600">
            Compliance References
          </span>
          <div className="mt-1 flex flex-wrap gap-2">
            {complianceRefs.map((ref) => (
              <span
                key={ref}
                className="inline-flex items-center rounded-full bg-indigo-100 px-3 py-1 text-xs font-mono text-indigo-800 ring-1 ring-indigo-200"
              >
                ✓ {ref}
              </span>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

function Card({ title, icon, description }: { title: string; icon: string; description: string }) {
  return (
    <div className="rounded-lg bg-white p-3 shadow-sm">
      <div className="mb-1 flex items-center gap-1">
        <span>{icon}</span>
        <span className="text-sm font-semibold text-indigo-800">{title}</span>
      </div>
      <p className="text-sm text-gray-700">{description}</p>
    </div>
  );
}
