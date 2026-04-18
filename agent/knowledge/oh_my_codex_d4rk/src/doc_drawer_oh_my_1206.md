]);
  });

  it('skips tmp cleanup when showing help', async () => {
    const calls: string[] = [];

    await cleanupCommand(['--help'], {
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

    assert.deepEqual(calls, ['processes']);
  });
});