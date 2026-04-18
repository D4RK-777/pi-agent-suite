analysis
- Use `ask_codex` with `agent_role: "critic"` for plan review in consensus and review modes
- If ToolSearch finds no MCP tools or Codex is unavailable, fall back to equivalent OMX prompt agents -- never block on external tools
- **CRITICAL — Consensus mode agent calls MUST be sequential, never parallel.** Always await the Architect result before issuing the Critic call.
- In consensus mode, default to RALPLAN-DR short mode; enable deliberate mode on `--deliberate` or explicit high-risk signals (auth/security, migrations, destructive changes, production incidents, compliance/PII, public API breakage)