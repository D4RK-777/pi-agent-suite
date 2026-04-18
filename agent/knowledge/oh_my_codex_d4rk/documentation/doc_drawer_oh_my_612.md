that surface pane-aware inspection metadata and ready-to-run sparkshell commands for leader triage.

## What’s included
### `omx sparkshell`
- adds CLI dispatch/help for `omx sparkshell`
- adds `src/cli/sparkshell.ts` for native binary discovery and launch
- adds the Rust crate under `native/omx-sparkshell/`
- adds packaging/build helpers:
  - `scripts/build-sparkshell.mjs`
  - `scripts/test-sparkshell.mjs`
- stages the packaged native binary under `bin/native/linux-x64/omx-sparkshell`
- adds focused CLI + packaging tests