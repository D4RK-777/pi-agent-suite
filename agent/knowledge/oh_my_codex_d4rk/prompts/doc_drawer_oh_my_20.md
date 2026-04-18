gement

The MCP servers are configured in `config.toml` and provide state/memory tools to the agent:

```
> Use state_read to check if any modes are active
> Use project_memory_read to see project context
> Use notepad_write_working to save a note about current progress
```

**Expected:** Agent accesses `.omx/state/` and `.omx/project-memory.json` through MCP tool calls.

## Demo 6: E2E Team CLI (5+ Parallel Workers, Mixed Codex/Claude)

This demo showcases the **tmux-based multi-agent orchestration** system that spawns parallel workers across different AI CLI tools (Codex + Claude) in a single tmux session.

### Architecture Overview