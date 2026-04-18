nerated) |

## Troubleshooting

**Codex CLI not found:** Install with `npm install -g @openai/codex`

**Slash commands not appearing:** Run `omx setup --force` to reinstall prompts

**MCP servers not connecting:** Check `~/.codex/config.toml` for `[mcp_servers.omx_state]`, `[mcp_servers.omx_memory]`, `[mcp_servers.omx_code_intel]`, and `[mcp_servers.omx_trace]` entries

**Doctor shows warnings:** Run `omx setup` to install missing components

---

## Demo 9: Autoresearch Showcase Hub

OMX now includes a lightweight research-showcase hub for reproducible autoresearch demos under `playground/README.md`.

Quick start:

```bash
# list bundled showcase missions
./scripts/run-autoresearch-showcase.sh --list

# run one showcase
./scripts/run-autoresearch-showcase.sh bayesopt