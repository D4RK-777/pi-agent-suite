es.join('\n'), /Killed 2 orphaned OMX MCP server process\(es\) \(1 required SIGKILL\)\./);
  });
});

describe('cleanupStaleTmpDirectories', () => {
  const tmpEntries = [
    { name: 'omx-stale-a', isDirectory: () => true },
    { name: 'omc-stale-b', isDirectory: () => true },
    { name: 'oh-my-codex-fresh', isDirectory: () => true },
    { name: 'oh-my-codex-file', isDirectory: () => false },
    { name: 'other-stale', isDirectory: () => true },
  ];

  it('supports dry-run and reports stale matching directories older than one hour', async () => {
    const lines: string[] = [];
    const removedPaths: string[] = [];
    const now = 10 * 60 * 60 * 1000;