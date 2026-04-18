elClass: 'frontier',
    routingRole: 'leader',
    tools: 'read-only',
    category: 'review',
  },

  // Domain Specialists
  'dependency-expert': {
    name: 'dependency-expert',
    description: 'External SDK/API/package evaluation',
    reasoningEffort: 'high',
    posture: 'frontier-orchestrator',
    modelClass: 'standard',
    routingRole: 'specialist',
    tools: 'analysis',
    category: 'domain',
  },
  'test-engineer': {
    name: 'test-engineer',
    description: 'Test strategy, coverage, flaky-test hardening',
    reasoningEffort: 'medium',
    posture: 'deep-worker',
    modelClass: 'frontier',
    routingRole: 'executor',
    tools: 'execution',
    category: 'domain',
  },
  'quality-strategist': {
    name: 'quality-strategist',