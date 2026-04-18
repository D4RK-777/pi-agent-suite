you specifically need durable tmux/worktree coordination, not as the default way to begin using OMX.

```bash
omx team 3:executor "fix the failing tests with verification"
omx team status <team-name>
omx team resume <team-name>
omx team shutdown <team-name>
```

### Setup, doctor, and HUD

These are operator/support surfaces:
- `omx setup` installs prompts, skills, config, and AGENTS scaffolding
- `omx doctor` verifies the install when something seems wrong
- `omx hud --watch` is a monitoring/status surface, not the primary user workflow

### Explore and sparkshell

- `omx explore --prompt "..."` is for read-only repository lookup
- `omx sparkshell <command>` is for shell-native inspection and bounded verification

Examples: