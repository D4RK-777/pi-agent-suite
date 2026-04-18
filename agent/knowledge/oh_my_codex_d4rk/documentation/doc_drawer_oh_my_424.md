# Release notes — 0.11.9

## Summary

`0.11.9` is a focused patch release after `0.11.8` that hardens deep-interview / ralplan coordination, repairs setup behavior around Codex-managed TUI configs, and keeps live worker supervision / HUD state visibility aligned with active sessions.

## Included fixes and changes

- deep-interview lock state now suppresses fallback tmux-pane nudges
- planning handoff applies stronger deep-interview pressure before execution
- live ralplan consensus planning exposes observable runtime state for HUD / pipeline visibility
- setup no longer rebreaks Codex-managed TUI configs, and default explore-routing guidance stays aligned with setup adoption
- active stateful modes are visible in the HUD again during live sessions