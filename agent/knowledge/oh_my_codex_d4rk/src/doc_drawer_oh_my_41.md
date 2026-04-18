nst names = getAgentNames();
    assert.ok(names.length > 20, 'expected non-trivial agent catalog');

    for (const name of names) {
      const agent = AGENT_DEFINITIONS[name];
      assert.equal(agent.name, name);
      assert.ok(agent.description.length > 0);
      assert.ok(agent.reasoningEffort.length > 0);
      assert.ok(agent.posture.length > 0);
      assert.ok(agent.modelClass.length > 0);
      assert.ok(agent.routingRole.length > 0);
    }
  });

  it('filters agents by category', () => {
    const buildAgents = getAgentsByCategory('build');
    assert.ok(buildAgents.length > 0);
    assert.ok(buildAgents.some((agent) => agent.name === 'executor'));
    assert.ok(buildAgents.some((agent) => agent.name === 'team-executor'));