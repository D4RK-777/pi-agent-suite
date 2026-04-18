{ workerCount, agentType, explicitAgentType, explicitWorkerCount, task: effectiveTask, teamName };
}

export function parseTeamStartArgs(args: string[]): ParsedTeamStartArgs {
  const parsedWorktree = parseWorktreeMode(args);
  return {
    parsed: parseTeamArgs(parsedWorktree.remainingArgs),
    worktreeMode: resolveDefaultTeamWorktreeMode(parsedWorktree.mode),
  };
}

/**
 * Decompose a compound task string into distinct sub-tasks with role assignments.
 *
 * Decomposition strategy:
 * 1. Numbered list detection: "1. ... 2. ... 3. ..."
 * 2. Conjunction splitting: split on " and ", ", ", "; "
 * 3. Fallback for atomic tasks: create implementation + test + doc sub-tasks
 *
 * When the user specifies an explicit agent-type (e.g., `3:executor`), all tasks