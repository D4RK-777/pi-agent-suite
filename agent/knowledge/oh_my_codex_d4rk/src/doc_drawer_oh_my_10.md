odelClass: 'standard',
    routingRole: 'leader',
    tools: 'analysis',
    category: 'build',
  },

  // Review Lane
  'style-reviewer': {
    name: 'style-reviewer',
    description: 'Formatting, naming, idioms, lint conventions',
    reasoningEffort: 'low',
    posture: 'fast-lane',
    modelClass: 'fast',
    routingRole: 'specialist',
    tools: 'read-only',
    category: 'review',
  },
  'quality-reviewer': {
    name: 'quality-reviewer',
    description: 'Logic defects, maintainability, anti-patterns',
    reasoningEffort: 'medium',
    posture: 'frontier-orchestrator',
    modelClass: 'standard',
    routingRole: 'leader',
    tools: 'read-only',
    category: 'review',
  },
  'api-reviewer': {
    name: 'api-reviewer',