t.name === 'executor'));
    assert.ok(buildAgents.some((agent) => agent.name === 'team-executor'));

    const allowed: AgentDefinition['category'][] = [
      'build',
      'review',
      'domain',
      'product',
      'coordination',
    ];

    for (const category of allowed) {
      const agents = getAgentsByCategory(category);
      assert.ok(agents.every((agent) => agent.category === category));
    }
  });