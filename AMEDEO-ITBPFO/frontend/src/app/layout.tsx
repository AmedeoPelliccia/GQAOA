import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "AMEDEO-ITBPFO | Pipeline Dashboard",
  description:
    "Autonomous Multimodal Execution — Intergenerational Transformation to Best Processable Formatted Output. Pipeline dashboard with FINEX terminal-state sealing.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-gray-50 text-gray-900 antialiased">
        <header className="border-b border-gray-200 bg-white shadow-sm">
          <div className="mx-auto flex max-w-6xl items-center justify-between px-4 py-3">
            <div>
              <h1 className="text-lg font-bold tracking-tight">
                AMEDEO-ITBPFO
              </h1>
              <p className="text-xs text-gray-500">
                GQAOA .INC — GAIA QUANTUM AMPEL OPT-INS ARCHITECTURE
              </p>
            </div>
            <span className="rounded-full bg-green-100 px-3 py-1 text-xs font-semibold text-green-800">
              v1.0.0
            </span>
          </div>
        </header>
        <main className="mx-auto max-w-6xl px-4 py-8">{children}</main>
      </body>
    </html>
  );
}
