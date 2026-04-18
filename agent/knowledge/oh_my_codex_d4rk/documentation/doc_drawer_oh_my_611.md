# PR Draft: Rebase `feat/omx-sparkshell` onto `experimental/dev`

## Target branch
`experimental/dev`

## Summary
This PR rebases the `omx sparkshell` feature line onto `experimental/dev` and preserves the follow-on team-status inspection work built on top of it.

It adds the native Rust-backed `omx sparkshell <command> [args...]` flow, plus a long sequence of `omx team status` improvements that surface pane-aware inspection metadata and ready-to-run sparkshell commands for leader triage.