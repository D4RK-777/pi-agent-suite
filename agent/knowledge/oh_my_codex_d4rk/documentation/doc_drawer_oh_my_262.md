t reliability fixes,
- use notifier output and need verbosity control.

## What changed (high level)

- Catalog consolidation for prompts/skills and cleanup of deprecated entries.
- `omx setup` now supports scope-aware install modes (`user`, `project`). Legacy `project-local` values are auto-migrated.
- Spark worker routing added for team workers (`--spark`, `--madmax-spark`).
- Notifier verbosity controls added.
- tmux runtime hardening updates landed, including post-review pane capture/input hardening.
- Stale references to removed `scientist`/`pipeline` were cleaned up.

## Removed prompts and skills

### Removed prompts

- `deep-executor`
- `scientist`

### Removed skills