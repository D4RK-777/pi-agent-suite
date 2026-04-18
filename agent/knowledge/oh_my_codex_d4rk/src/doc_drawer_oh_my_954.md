+ doc sub-tasks
 *
 * When the user specifies an explicit agent-type (e.g., `3:executor`), all tasks
 * get that role (backward compat). Otherwise, heuristic routing assigns roles.
 */
type DecompositionStrategy = 'numbered' | 'bulleted' | 'conjunction' | 'atomic';

interface DecompositionCandidate {
  subject: string;
  description: string;
}

interface DecompositionPlan {
  strategy: DecompositionStrategy;
  subtasks: DecompositionCandidate[];
}

export interface TeamExecutionPlan {
  workerCount: number;
  tasks: Array<{ subject: string; description: string; owner: string; role?: string }>;
}

function resolveImplicitTeamFallbackRole(agentType: string, explicitAgentType: boolean): string {
  return !explicitAgentType && agentType === 'executor' ? 'team-executor' : agentType;
}