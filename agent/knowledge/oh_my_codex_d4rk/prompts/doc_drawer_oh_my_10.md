action protocol | PARTIAL (instructions only) |
| Stop | notify config + postLaunch cleanup | FULL |
| SessionEnd | omx postLaunch lifecycle phase | PARTIAL (post-exit cleanup) |

`*` FULL via terminal automation workaround (default-enabled in `v0.2.3` generated `.omx/tmux-hook.json`), not native hook context injection.

### Infrastructure

| Component | OMC | OMX Status |
|-----------|-----|-----------|
| CLI (setup) | DONE | DONE |
| CLI (doctor) | DONE | DONE |
| CLI (help) | DONE | DONE |
| CLI (version) | DONE | DONE |
| CLI (status) | DONE | DONE |
| CLI (cancel) | DONE | DONE |
| Config generator | DONE | DONE |
| AGENTS.md template | DONE | DONE |
| State MCP server | DONE | DONE |
| Memory MCP server | DONE | DONE |
| Notify hook script | DONE | DONE |