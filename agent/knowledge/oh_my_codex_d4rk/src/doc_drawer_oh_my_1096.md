res = runProviderAdvisorScript(wd, []);
      if (shouldSkipForSpawnPermissions(res.error)) return;

      assert.equal(res.status, 1, res.stderr || res.stdout);
      assert.match(res.stderr, /claude --print/);
      assert.match(res.stderr, /gemini --prompt/);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });

  it('preserves child stdout/stderr and exact non-zero exit code', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-ask-contract-'));
    try {
      const res = runOmx(wd, ['ask', 'claude', 'pass-through'], {
        OMX_ASK_ADVISOR_SCRIPT: 'dist/scripts/fixtures/ask-advisor-stub.js',
        OMX_ASK_STUB_STDOUT: 'artifact-path-from-stub.md\n',
        OMX_ASK_STUB_STDERR: 'stub-warning-line\n',
        OMX_ASK_STUB_EXIT_CODE: '7',