ONS.vision.modelClass, 'frontier');

    assert.equal(AGENT_DEFINITIONS.explore.modelClass, 'fast');

    for (const name of [
      'researcher',
      'debugger',
      'designer',
      'writer',
      'git-master',
      'build-fixer',
      'executor',
      'verifier',
      'dependency-expert',
    ] as const) {
      assert.equal(AGENT_DEFINITIONS[name].modelClass, 'standard');
      assert.equal(AGENT_DEFINITIONS[name].reasoningEffort, 'high');
    }
  });
});