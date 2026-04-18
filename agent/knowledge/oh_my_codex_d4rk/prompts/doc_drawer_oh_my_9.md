r | DONE | ~/.codex/skills/worker/SKILL.md |

### Hook Pipeline (6 full + 3 partial out of 9 = ~89%)

| OMC Hook Event | OMX Equivalent | Capability |
|---------------|---------------|------------|
| SessionStart | AGENTS.md native + runtime overlay (preLaunch) | FULL+ |
| PreToolUse | AGENTS.md inline guidance | PARTIAL (no interception) |
| PostToolUse | notify config hook + tmux prompt injection workaround | FULL* |
| UserPromptSubmit | AGENTS.md self-detection | PARTIAL (model-side detection) |
| SubagentStart | Codex CLI multi_agent native | FULL |
| SubagentStop | Codex CLI multi_agent native | FULL |
| PreCompact | AGENTS.md overlay compaction protocol | PARTIAL (instructions only) |
| Stop | notify config + postLaunch cleanup | FULL |