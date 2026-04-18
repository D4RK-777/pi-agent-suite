tes

- If you use project-scoped OMX installs, rerun:

```bash
omx setup --force --scope project
```

- Expect `omx explore` and `omx sparkshell` packaged installs to rely on release-asset hydration when no explicit binary override or repo-local artifact is present.
- `npm pack` intentionally does **not** ship staged native binaries; native archives are attached to the GitHub Release and consumed through the native-asset workflow.

## Compare stats

- Commit window: **55 non-merge commits** (`2026-03-10` to `2026-03-12`)
- Diff snapshot (`v0.8.15...dev`): **149 files changed, +12,325 / -254**

## Merged PRs in the release window