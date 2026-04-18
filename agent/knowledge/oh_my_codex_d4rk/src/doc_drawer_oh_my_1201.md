st lines: string[] = [];
    const removedPaths: string[] = [];
    const now = 10 * 60 * 60 * 1000;

    const removedCount = await cleanupStaleTmpDirectories(['--dry-run'], {
      tmpRoot: '/tmp',
      listTmpEntries: async () => tmpEntries,
      statPath: async (path) => ({
        mtimeMs:
          path === '/tmp/oh-my-codex-fresh'
            ? now - 30 * 60 * 1000
            : now - 2 * 60 * 60 * 1000,
      }),
      removePath: async (path) => {
        removedPaths.push(path);
      },
      now: () => now,
      writeLine: (line) => lines.push(line),
    });