Yeachan-Heo/oh-my-codex/pull/643)

### Scale-up task bootstrap now preserves canonical task identity

Dynamic scaling now writes new tasks through canonical team state before worker bootstrap, so scaled workers receive stable task ids, persisted roles, and inbox/task metadata that matches the runtime contract used by initial team startup.

This release:
- persists scaled tasks before worker bootstrap instead of reconstructing synthetic inbox-only task metadata
- preserves role/owner/task-id fidelity during scale-up
- adds regression coverage for canonical scale-up task state and inbox ids

## Upgrade note

If you use project-scoped OMX installs, rerun:

```bash
omx setup --force --scope project
```

after upgrading so managed project config/native-agent paths are refreshed.