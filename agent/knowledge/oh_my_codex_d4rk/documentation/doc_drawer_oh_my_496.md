focused work, `dev` also picked up supporting improvements that make the release feel more complete:

- worker mailbox/trigger wording now nudges workers to report progress and continue execution instead of stopping after a reply (`#805`)
- centralized default model resolution (`94769c1`, PR `#787`)
- local help routing cleanup for `ask` and `hud` (`6b0b560`, `6dc245e`, PR `#786`)
- team runtime lifecycle and cleanup hardening (`a0a9626`, PR `#785`)
- Windows Codex command shim probing fix (`8fc859c`, PR `#793`)
- aspect-task distribution fix for team workers (`ce35d37`, PR `#789`)

## Upgrade notes

- If you use project-scoped OMX installs, rerun:

```bash
omx setup --force --scope project
```