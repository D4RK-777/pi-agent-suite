# QA Plan — v0.4.2 (dev vs deployed main)

Date: 2026-02-18  
Scope: validate delta between `origin/main` (deployed, `v0.4.1`) and current `dev`.

## 1) Parity Validation Summary

Run:

```bash
git fetch origin --prune
git rev-list --left-right --count origin/main...dev
git log --oneline origin/main..dev
git diff --name-status origin/main...dev
```

Expected at time of writing:
- `origin/main` is deployed at `v0.4.1`.
- `dev` is ahead with feature/fix/test commits (auto-nudge improvements, all-workers-idle leader notification, tmux input/scrolling fixes, and coverage expansion).
- No non-merge functional commits were found on `main` that are missing from `dev`.

## 2) Risk-Based Focus Areas