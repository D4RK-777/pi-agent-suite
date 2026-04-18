name> [--force]
       omx team api <operation> [--input <json>] [--json]
       omx team api --help

Notes:
  team workers use dedicated worktrees automatically by default.
  --worktree is deprecated for omx team and is now only a backward-compatible no-op override.
  use native Codex subagents for small in-session fanout; use omx team for durable tmux/state/worktree coordination.

Examples:
  omx team 3:executor "fix failing tests"
  omx team status my-team
  omx team status my-team --json
  omx team status my-team --tail-lines 600
  omx team api send-message --input '{"team_name":"my-team","from_worker":"worker-1","to_worker":"leader-fixed","body":"ACK"}' --json
`;

const TEAM_API_HELP = `
Usage: omx team api <operation> [--input <json>] [--json]
       omx team api <operation> --help