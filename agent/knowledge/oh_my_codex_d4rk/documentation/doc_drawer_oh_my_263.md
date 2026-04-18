Removed prompts and skills

### Removed prompts

- `deep-executor`
- `scientist`

### Removed skills

- `deepinit`
- `learn-about-omx`
- `learner`
- `pipeline`
- `project-session-manager`
- `psm`
- `release`
- `ultrapilot`
- `writer-memory`

## Mapping old references to current ones

Use these replacements in docs, scripts, and personal shortcuts.

| Old reference | Use now | Notes |
|---|---|---|
| `/prompts:deep-executor` | `/prompts:executor` | `deep-executor` was a deprecated alias to executor behavior. |
| `/prompts:scientist` | `/prompts:researcher` | Use researcher for research-focused workflows in current catalog. |
| `$pipeline` | `$team` (or explicit `/prompts:*` sequencing) | Team is the default orchestrator pipeline surface. |