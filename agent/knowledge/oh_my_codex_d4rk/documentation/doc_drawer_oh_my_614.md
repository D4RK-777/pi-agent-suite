paths and team/worker state artifact paths
  - structured `recommended_inspect_items` JSON payloads

## Rebase / integration fixes included
- merged `experimental/dev` CLI/explore surfaces with sparkshell command routing
- excluded `native/omx-sparkshell` from the root Cargo workspace so manifest-path cargo commands work again
- refreshed/added missing compat doctor fixtures after the rebase
- hardened MCP team-job cleanup to resolve the jobs directory from the current home directory dynamically
- updated tests for newly surfaced claim-lock inspection metadata