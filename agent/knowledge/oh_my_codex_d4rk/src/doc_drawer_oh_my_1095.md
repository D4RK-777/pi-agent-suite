is missing', () => {
    assert.throws(() => parseAskArgs(['claude']), /Missing prompt text/);
  });

  it('throws when --agent-prompt role is missing', () => {
    assert.throws(() => parseAskArgs(['claude', '--agent-prompt', '--prompt', 'hello']), /Missing role after --agent-prompt/);
  });
});

describe('omx ask', () => {
  it('script usage documents provider-specific long flags from CLI help', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-ask-usage-'));
    try {
      const res = runProviderAdvisorScript(wd, []);
      if (shouldSkipForSpawnPermissions(res.error)) return;