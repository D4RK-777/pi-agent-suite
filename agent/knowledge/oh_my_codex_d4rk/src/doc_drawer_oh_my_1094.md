provider: 'claude',
      prompt: 'review this',
      agentPromptRole: 'executor',
    });
  });

  it('parses --agent-prompt=<role> with --prompt task text', () => {
    assert.deepEqual(parseAskArgs(['gemini', '--agent-prompt=planner', '--prompt', 'brainstorm', 'ideas']), {
      provider: 'gemini',
      prompt: 'brainstorm ideas',
      agentPromptRole: 'planner',
    });
  });

  it('throws for invalid provider', () => {
    assert.throws(() => parseAskArgs(['openai', 'hello']), /Invalid provider/);
  });

  it('throws when prompt is missing', () => {
    assert.throws(() => parseAskArgs(['claude']), /Missing prompt text/);
  });