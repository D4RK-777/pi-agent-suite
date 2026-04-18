,
  modelClass: 'frontier',
  routingRole: 'executor',
  tools: 'execution',
  category: 'build',
};

export const AGENT_DEFINITIONS: Record<string, AgentDefinition> = {
  // Build/Analysis Lane
  'explore': {
    name: 'explore',
    description: 'Fast codebase search and file/symbol mapping',
    reasoningEffort: 'low',
    posture: 'fast-lane',
    modelClass: 'fast',
    routingRole: 'specialist',
    tools: 'read-only',
    category: 'build',
  },
  'analyst': {
    name: 'analyst',
    description: 'Requirements clarity, acceptance criteria, hidden constraints',
    reasoningEffort: 'medium',
    posture: 'frontier-orchestrator',
    modelClass: 'frontier',
    routingRole: 'leader',
    tools: 'analysis',
    category: 'build',
  },
  'planner': {
    name: 'planner',