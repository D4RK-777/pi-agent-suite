agentType: approvedHint.agentType,
    explicitAgentType: approvedHint.agentType != null,
  };
}

const MIN_WORKER_COUNT = 1;
const DEFAULT_SPARKSHELL_TAIL_LINES = 400;
const MIN_SPARKSHELL_TAIL_LINES = 100;
const MAX_SPARKSHELL_TAIL_LINES = 1000;
const TEAM_HELP = `
Usage: omx team [N:agent-type] "<task description>"
       omx team status <team-name> [--json] [--tail-lines <100-1000>]
       omx team await <team-name> [--timeout-ms <ms>] [--after-event-id <id>] [--json]
       omx team resume <team-name>
       omx team shutdown <team-name> [--force]
       omx team api <operation> [--input <json>] [--json]
       omx team api --help