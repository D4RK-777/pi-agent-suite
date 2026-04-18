# `omx autoresearch` parity contract

`omx autoresearch` is a thin supervisor that drives one Codex experiment session per iteration while OMX owns the durable keep/discard/reset loop.

## CLI

```bash
omx autoresearch <mission-dir> [codex-args...]
omx autoresearch --resume <run-id> [codex-args...]
omx autoresearch --help
```

- Fresh launch always creates a new run-tagged lane.
- `--resume <run-id>` loads `.omx/logs/autoresearch/<run-id>/manifest.json`.
- A second launch is rejected while repo-root `.omx/state/autoresearch-state.json` points at an active run.

## Mission / sandbox contract

`<mission-dir>` must be inside a git repo and contain `mission.md` plus `sandbox.md`.