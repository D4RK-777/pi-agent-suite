# Release notes — 0.11.12

## Summary

`0.11.12` is a patch release after `0.11.11` that removes more Windows terminal flicker paths, closes additional team/runtime seam gaps, makes Node test execution cross-platform, and aligns workflow docs around the current OMX onboarding path.

## Included fixes and changes

- Windows child-process launches now use broader `windowsHide` coverage
- git metadata reads fall back to filesystem reads where needed to avoid Windows conhost flicker
- team cwd metadata resolution is canonicalized to the current manifest v2 source of truth
- dispatch / mailbox transitions close more of the runtime thin-adapter dual-write seam gaps
- tmux readiness and auto-nudge behavior stay scoped to OMX-managed sessions