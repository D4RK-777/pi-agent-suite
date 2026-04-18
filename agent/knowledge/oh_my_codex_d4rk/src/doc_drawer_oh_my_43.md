tegory(category);
      assert.ok(agents.every((agent) => agent.category === category));
    }
  });

  it('keeps the installable agent model split aligned with the OMX subagent matrix', () => {
    assert.equal(AGENT_DEFINITIONS.architect.modelClass, 'frontier');
    assert.equal(AGENT_DEFINITIONS['security-reviewer'].modelClass, 'frontier');
    assert.equal(AGENT_DEFINITIONS['test-engineer'].modelClass, 'frontier');
    assert.equal(AGENT_DEFINITIONS['team-executor'].modelClass, 'frontier');
    assert.equal(AGENT_DEFINITIONS.vision.modelClass, 'frontier');

    assert.equal(AGENT_DEFINITIONS.explore.modelClass, 'fast');