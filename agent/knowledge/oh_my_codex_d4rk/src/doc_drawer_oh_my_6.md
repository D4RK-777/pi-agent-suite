* Category for grouping */
  category: 'build' | 'review' | 'domain' | 'product' | 'coordination';
}

const EXECUTOR_AGENT: AgentDefinition = {
  name: 'executor',
  description: 'Code implementation, refactoring, feature work',
  reasoningEffort: 'high',
  posture: 'deep-worker',
  modelClass: 'standard',
  routingRole: 'executor',
  tools: 'execution',
  category: 'build',
};

const TEAM_EXECUTOR_AGENT: AgentDefinition = {
  name: 'team-executor',
  description: 'Supervised team execution for conservative delivery lanes',
  reasoningEffort: 'medium',
  posture: 'deep-worker',
  modelClass: 'frontier',
  routingRole: 'executor',
  tools: 'execution',
  category: 'build',
};