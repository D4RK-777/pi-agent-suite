'brainstorm', 'ideas']), {
      provider: 'gemini',
      prompt: 'brainstorm ideas',
    });
  });

  it('parses --print prompt form', () => {
    assert.deepEqual(parseAskArgs(['claude', '--print', 'review', 'this']), {
      provider: 'claude',
      prompt: 'review this',
    });
  });

  it('parses --prompt prompt form', () => {
    assert.deepEqual(parseAskArgs(['gemini', '--prompt', 'brainstorm', 'ideas']), {
      provider: 'gemini',
      prompt: 'brainstorm ideas',
    });
  });

  it('parses --agent-prompt with positional task text', () => {
    assert.deepEqual(parseAskArgs(['claude', '--agent-prompt', 'executor', 'review', 'this']), {
      provider: 'claude',
      prompt: 'review this',
      agentPromptRole: 'executor',
    });
  });