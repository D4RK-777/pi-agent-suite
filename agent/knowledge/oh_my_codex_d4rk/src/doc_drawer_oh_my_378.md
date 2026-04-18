(compatibility alias for run)
  omx autoresearch --resume <run-id> [codex-args...]

Arguments:
  (no args)        Launch an interactive Codex session that activates deep-interview --autoresearch,
                   writes .omx/specs artifacts, then launches only after explicit confirmation.
  --topic/...      Seed the deep-interview intake with draft values; still requires refinement/confirmation before launch.
  init             Bare init is an interactive deep-interview alias on TTYs; init with flags is the expert scaffold path.
  run              Execute a crystallized autoresearch mission, preferring tmux split-pane launch when available.
  <mission-dir>    Directory inside a git repository containing mission.md and sandbox.md