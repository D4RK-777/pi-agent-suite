ing commands (install, build, test) run in background. Maximum 20 concurrent.

## Token Savings Tips

1. **Batch similar tasks** to one agent instead of spawning many
2. **Use explore (LOW tier)** for file discovery, not architect
3. **Prefer LOW-tier executor routing** for simple changes - only upgrade if it fails
4. **Use writer (LOW tier)** for all documentation tasks
5. **Avoid THOROUGH-tier agents** unless the task genuinely requires deep reasoning

## Disabling Ecomode

Ecomode can be completely disabled via config. When disabled, all ecomode keywords are ignored.

Set in `~/.codex/.omx-config.json`:
```json
{
  "ecomode": {
    "enabled": false
  }
}
```

## State Management

Use `omx_state` MCP tools for ecomode lifecycle state.