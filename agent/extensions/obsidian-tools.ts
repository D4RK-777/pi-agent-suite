/**
 * Obsidian Tools Extension for PI Agent
 *
 * Bridges the MiniMax (or any pi) agent to OmegaD4rkMynd via the Local REST API plugin.
 * Uses the insecure (http) port 27123 — already enabled on OmegaD4rkMynd.
 * Token lives in-plugin at `OmegaD4rkMynd/.obsidian/plugins/obsidian-local-rest-api/data.json`.
 *
 * Tools:
 *   - obsidian_list:    list folder contents
 *   - obsidian_read:    read a note's body
 *   - obsidian_search:  full-text search across the vault
 *   - obsidian_append:  append content to an existing note (safe for daily notes, log.md)
 *   - obsidian_create:  create (or overwrite) a note at a given path
 *
 * Source-of-truth rule: OmegaD4rkMynd > MemPalace. When this extension and
 * mempalace-tools disagree, trust Obsidian — then re-mine to refresh MemPalace.
 */

import type { ExtensionAPI } from "@mariozechner/pi-coding-agent";
import { Type } from "@sinclair/typebox";
import { readFileSync } from "fs";
import { join } from "path";

// Prefer user-provided env; fall back to reading the plugin's data.json.
function loadObsidianToken(): { token: string; baseUrl: string } {
  const envToken = process.env.OBSIDIAN_API_KEY;
  const envBase = process.env.OBSIDIAN_BASE_URL;
  if (envToken && envBase) return { token: envToken, baseUrl: envBase };

  try {
    const home = process.env.USERPROFILE || process.env.HOME || "";
    const dataPath = join(home, "OmegaD4rkMynd", ".obsidian", "plugins", "obsidian-local-rest-api", "data.json");
    const data = JSON.parse(readFileSync(dataPath, "utf-8")) as {
      apiKey?: string;
      insecurePort?: number;
      port?: number;
      enableInsecureServer?: boolean;
    };
    const port = data.enableInsecureServer ? data.insecurePort || 27123 : data.port || 27124;
    const scheme = data.enableInsecureServer ? "http" : "https";
    return {
      token: envToken || data.apiKey || "",
      baseUrl: envBase || `${scheme}://127.0.0.1:${port}`,
    };
  } catch {
    return { token: envToken || "", baseUrl: envBase || "http://127.0.0.1:27123" };
  }
}

/**
 * Probe whether the Obsidian Local REST API is actually reachable.
 * If Obsidian isn't open, skip tool registration entirely so pi never
 * wastes turns calling a dead endpoint. Returns true if reachable.
 */
async function isObsidianAlive(baseUrl: string, token: string): Promise<boolean> {
  try {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), 2000);
    const res = await fetch(`${baseUrl}/`, {
      headers: { Authorization: `Bearer ${token}` },
      signal: controller.signal,
    });
    clearTimeout(timer);
    return res.ok || res.status === 200 || res.status === 404; // 404 is fine — API is up
  } catch {
    return false;
  }
}

export default function (pi: ExtensionAPI) {
  const { token, baseUrl } = loadObsidianToken();
  const isHttps = baseUrl.startsWith("https://");

  // Tools always register. Liveness is probed at CALL time with a small cache,
  // so Obsidian starting mid-session works without restart. If Obsidian is down
  // when a tool is called, we return a friendly error instead of hanging.
  let lastLivenessCheck = 0;
  let cachedAlive = false;
  const LIVENESS_TTL_MS = 30_000;

  async function ensureAlive(): Promise<boolean> {
    const now = Date.now();
    if (now - lastLivenessCheck < LIVENESS_TTL_MS) return cachedAlive;
    cachedAlive = await isObsidianAlive(baseUrl, token);
    lastLivenessCheck = now;
    return cachedAlive;
  }

  pi.on("session_start", async (_event, ctx) => {
    const alive = await ensureAlive();
    if (alive) {
      ctx.ui.notify("Obsidian Local REST API reachable — obsidian_* tools available.", "info");
    } else {
      ctx.ui.notify("Obsidian not running — obsidian_* tools registered but will return errors until Obsidian starts.", "warning");
    }
  });

  registerTools();

  function registerTools() {

  async function obsidianFetch(path: string, init: RequestInit = {}): Promise<Response> {
    const headers: Record<string, string> = {
      Authorization: `Bearer ${token}`,
      Accept: "application/json",
      ...((init.headers as Record<string, string>) || {}),
    };
    // For https with the plugin's self-signed cert we'd need to disable cert verification.
    // Stick with the insecure port on loopback (already localhost-only).
    if (isHttps) {
      // Node 18+ honours NODE_TLS_REJECT_UNAUTHORIZED=0 for this; document but don't set.
    }
    return fetch(`${baseUrl}${path}`, { ...init, headers });
  }

  function errorResult(e: unknown) {
    return { content: [{ type: "text" as const, text: `Obsidian error: ${e instanceof Error ? e.message : String(e)}` }] };
  }

  async function guardAlive() {
    if (await ensureAlive()) return null;
    return { content: [{ type: "text" as const, text: "Obsidian is not running. Start Obsidian (with Local REST API plugin enabled) and retry, or use MemPalace + codebase search instead." }] };
  }

  // ═══════════════════════════════════════════════════════════════════
  // LIST
  // ═══════════════════════════════════════════════════════════════════
  pi.registerTool({
    name: "obsidian_list",
    label: "Obsidian List Files",
    description: "List files/folders under an OmegaD4rkMynd path. Pass '' for vault root.",
    parameters: Type.Object({
      folder: Type.Optional(Type.String({ description: "Folder path relative to vault root. Empty for root.", default: "" })),
    }),
    async execute(_id, params) {
      const gate = await guardAlive(); if (gate) return gate;
      try {
        const folder = (params.folder || "").replace(/^\/+|\/+$/g, "");
        const path = folder ? `/vault/${encodeURI(folder)}/` : "/vault/";
        const res = await obsidianFetch(path);
        if (!res.ok) return { content: [{ type: "text", text: `HTTP ${res.status}: ${await res.text()}` }] };
        const data = (await res.json()) as { files?: string[] };
        return { content: [{ type: "text", text: (data.files || []).join("\n") || "(empty)" }] };
      } catch (e) {
        return errorResult(e);
      }
    },
  });

  // ═══════════════════════════════════════════════════════════════════
  // READ
  // ═══════════════════════════════════════════════════════════════════
  pi.registerTool({
    name: "obsidian_read",
    label: "Obsidian Read File",
    description: "Read a note from OmegaD4rkMynd. Path is relative to vault root, e.g. 'wiki/concepts/jwt.md'.",
    parameters: Type.Object({
      path: Type.String({ description: "Path relative to vault root (include .md)" }),
    }),
    async execute(_id, params) {
      const gate = await guardAlive(); if (gate) return gate;
      try {
        const res = await obsidianFetch(`/vault/${encodeURI(params.path)}`, {
          headers: { Accept: "text/markdown" },
        });
        if (!res.ok) return { content: [{ type: "text", text: `HTTP ${res.status}: ${await res.text()}` }] };
        const body = await res.text();
        return { content: [{ type: "text", text: body }] };
      } catch (e) {
        return errorResult(e);
      }
    },
  });

  // ═══════════════════════════════════════════════════════════════════
  // SEARCH (simple full-text)
  // ═══════════════════════════════════════════════════════════════════
  pi.registerTool({
    name: "obsidian_search",
    label: "Obsidian Search",
    description:
      "Full-text search across OmegaD4rkMynd. Returns matching filenames + snippets. " +
      "Use this before creating a new wiki page — append/refine existing pages rather than duplicating.",
    parameters: Type.Object({
      query: Type.String({ description: "Search string. Obsidian simple-search semantics." }),
      contextLength: Type.Optional(Type.Number({ description: "Chars of surrounding context per match", default: 120 })),
    }),
    async execute(_id, params) {
      const gate = await guardAlive(); if (gate) return gate;
      try {
        const qs = new URLSearchParams({
          query: params.query,
          contextLength: String(params.contextLength || 120),
        });
        const res = await obsidianFetch(`/search/simple/?${qs.toString()}`, { method: "POST" });
        if (!res.ok) return { content: [{ type: "text", text: `HTTP ${res.status}: ${await res.text()}` }] };
        const hits = (await res.json()) as Array<{ filename?: string; matches?: Array<{ context?: string }> }>;
        if (!hits.length) return { content: [{ type: "text", text: "No matches." }] };
        const body = hits
          .slice(0, 15)
          .map((h) => {
            const fname = h.filename || "(unknown)";
            const ctxs = (h.matches || []).map((m) => m.context?.trim() || "").filter(Boolean);
            return `📄 ${fname}\n   ${ctxs.slice(0, 2).join("\n   ")}`;
          })
          .join("\n\n");
        return { content: [{ type: "text", text: body }] };
      } catch (e) {
        return errorResult(e);
      }
    },
  });

  // ═══════════════════════════════════════════════════════════════════
  // APPEND
  // ═══════════════════════════════════════════════════════════════════
  pi.registerTool({
    name: "obsidian_append",
    label: "Obsidian Append",
    description:
      "Append content to an existing note (or create if missing). Prefer this for log files, daily notes, and wiki index updates — non-destructive.",
    parameters: Type.Object({
      path: Type.String({ description: "Path relative to vault root, e.g. 'wiki/log.md'" }),
      content: Type.String({ description: "Text to append. Will be prefixed with a newline." }),
    }),
    async execute(_id, params) {
      const gate = await guardAlive(); if (gate) return gate;
      try {
        const res = await obsidianFetch(`/vault/${encodeURI(params.path)}`, {
          method: "POST",
          headers: { "Content-Type": "text/markdown" },
          body: "\n" + params.content,
        });
        if (!res.ok && res.status !== 204) {
          return { content: [{ type: "text", text: `HTTP ${res.status}: ${await res.text()}` }] };
        }
        return { content: [{ type: "text", text: `Appended to ${params.path}` }] };
      } catch (e) {
        return errorResult(e);
      }
    },
  });

  // ═══════════════════════════════════════════════════════════════════
  // CREATE / OVERWRITE
  // ═══════════════════════════════════════════════════════════════════
  pi.registerTool({
    name: "obsidian_create",
    label: "Obsidian Create File",
    description:
      "Create a new note (or overwrite if exists) in OmegaD4rkMynd. Route by content type: " +
      "patterns/ for reusable code/design patterns, decisions/YYYY-MM-DD-{slug}.md for architectural commits, " +
      "wiki/concepts/ for atomic concepts, wiki/syntheses/ for cross-cutting analysis. " +
      "NEVER write to raw/ — it's immutable.",
    parameters: Type.Object({
      path: Type.String({ description: "Path relative to vault root. Include .md." }),
      content: Type.String({ description: "Full file body (include frontmatter if applicable)." }),
    }),
    async execute(_id, params) {
      if (params.path.startsWith("raw/") || params.path.includes("/raw/")) {
        return { content: [{ type: "text", text: "Refused: raw/ is immutable — re-routing required." }] };
      }
      const gate = await guardAlive(); if (gate) return gate;
      try {
        const res = await obsidianFetch(`/vault/${encodeURI(params.path)}`, {
          method: "PUT",
          headers: { "Content-Type": "text/markdown" },
          body: params.content,
        });
        if (!res.ok && res.status !== 204) {
          return { content: [{ type: "text", text: `HTTP ${res.status}: ${await res.text()}` }] };
        }
        return { content: [{ type: "text", text: `Wrote ${params.path}` }] };
      } catch (e) {
        return errorResult(e);
      }
    },
  });

  } // end registerTools()
}
