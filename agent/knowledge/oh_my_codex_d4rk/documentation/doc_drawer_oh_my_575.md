Legacy readers continue to read the same state files, but only as
Rust-authored compatibility views.

| Reader | Compatibility files | Compatibility guarantee |
|---|---|---|
| `omx team status` | `.omx/state/team/<team>/config.json`, `manifest.v2.json`, `tasks/*.json`, `approvals/*.json`, `workers/*` | Manifest-backed team config is authoritative when both config and manifest exist. |
| `omx doctor --team` | `.omx/state/team/<team>/config.json`, `manifest.v2.json`, `workers/*/status.json`, `workers/*/heartbeat.json`, `.omx/state/hud-state.json` | Manifest-backed tmux/session identity is authoritative when both config and manifest exist. |