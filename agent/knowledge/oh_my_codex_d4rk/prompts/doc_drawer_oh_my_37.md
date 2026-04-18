omx team api cleanup --input "{\"team_name\":\"$TEAM_NAME\"}" --json

echo "E2E demo complete."
```

Expected:
- Team starts with 6 mixed workers.
- Claim-safe lifecycle succeeds end-to-end.
- Summary envelope check returns exit code 0.
- Team shuts down cleanly and state cleanup completes.

## File Inventory

| Component | Count | Location |
|-----------|-------|----------|
| Agent prompts | 30 | `~/.codex/prompts/*.md` |
| Skills | 40 | `~/.codex/skills/*/SKILL.md` |
| MCP servers | 4 | Configured in `~/.codex/config.toml` |
| CLI commands | 11+ | `omx (launch), setup, doctor, team, version, tmux-hook, hud, status, cancel, reasoning, help` |
| AGENTS.md | 1 | Project root (generated) |

## Troubleshooting

**Codex CLI not found:** Install with `npm install -g @openai/codex`