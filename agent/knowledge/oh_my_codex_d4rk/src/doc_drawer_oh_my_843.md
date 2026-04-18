LL_TAIL_LINES}>]`);
      }
      return parsed;
    }
  }
  return DEFAULT_SPARKSHELL_TAIL_LINES;
}

export interface ParsedTeamStartArgs {
  parsed: ParsedTeamArgs;
  worktreeMode: WorktreeMode;
}

function resolveDefaultTeamWorktreeMode(mode: WorktreeMode): WorktreeMode {
  if (mode.enabled) return mode;
  return { enabled: true, detached: true, name: null };
}

function parseTeamApiArgs(args: string[]): {
  operation: TeamApiOperation;
  input: Record<string, unknown>;
  json: boolean;
} {
  const operation = resolveTeamApiOperation(args[0] || '');
  if (!operation) {
    throw new Error(`Usage: omx team api <operation> [--input <json>] [--json]\nSupported operations: ${TEAM_API_OPERATIONS.join(', ')}`);
  }
  let input: Record<string, unknown> = {};
  let json = false;