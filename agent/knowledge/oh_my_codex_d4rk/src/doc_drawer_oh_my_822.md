ount: number;
  explicitWorkerCount: boolean;
  agentType?: string;
  explicitAgentType?: boolean;
}

function readPersistedTeamFollowupState(cwd: string): {
  task?: string;
  task_description?: string;
  workerCount?: number;
  agent_count?: number;
  agentType?: string;
  agent_types?: string;
  linkedRalph?: boolean;
} | null {
  const path = join(cwd, '.omx', 'state', 'team-state.json');
  if (!existsSync(path)) return null;
  try {
    return JSON.parse(readFileSync(path, 'utf-8')) as {
      task?: string;
      workerCount?: number;
      agentType?: string;
      linkedRalph?: boolean;
      task_description?: string;
      agent_count?: number;
      agent_types?: string;
    };
  } catch {
    return null;
  }
}