{
  it('runs tmp cleanup after orphaned MCP cleanup', async () => {
    const calls: string[] = [];

    await cleanupCommand(['--dry-run'], {
      cleanupProcesses: async () => {
        calls.push('processes');
        return {
          dryRun: true,
          candidates: [],
          terminatedCount: 0,
          forceKilledCount: 0,
          failedPids: [],
        };
      },
      cleanupTmpDirectories: async () => {
        calls.push('tmp');
        return 0;
      },
    });

    assert.deepEqual(calls, ['processes', 'tmp']);
  });

  it('skips tmp cleanup when showing help', async () => {
    const calls: string[] = [];