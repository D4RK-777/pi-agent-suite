cope (authoritative scope), never broadcast to unrelated sessions.

## Consumer compatibility matrix

| Consumer | Responsibility under frozen scope/phase contract |
|---|---|
| `src/hud/state.ts` | Read session scope first when current session is known; fall back to root only when scoped file is absent. |
| `src/mcp/trace-server.ts` | Build mode timeline from authoritative scope paths resolved via state-path helpers. |
| `scripts/notify-hook.js` | Update lifecycle counters only in the authoritative session scope (or root fallback), never all sessions. |
| `src/hooks/agents-overlay.ts` | Summarize active modes from scope-preferred mode files (session overrides root). |