MCP server | DONE | DONE |
| Memory MCP server | DONE | DONE |
| Notify hook script | DONE | DONE |
| Keyword detector | DONE | DONE |
| Hook emulation layer | N/A | DONE |
| Mode base lifecycle | DONE | DONE |
| Verification protocol | DONE | DONE |
| Notification system | DONE | DONE |

## Known Gaps

1. **Pre-tool interception** - Cannot intercept tool calls before execution. Workaround: AGENTS.md instructs model to self-moderate.
2. **Native context injection from hooks** - Not available in Codex hooks API. Workaround: tmux prompt injection (`omx tmux-hook`) plus state files + AGENTS.md instructions (default-enabled in `v0.2.3` generated config).