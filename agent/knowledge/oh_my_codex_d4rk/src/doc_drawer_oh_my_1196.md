command: 'node /tmp/worktree/dist/mcp/trace-server.js',
          reason: 'outside-current-session',
        },
        {
          pid: 811,
          ppid: 810,
          command: 'node /tmp/worktree/dist/mcp/team-server.js',
          reason: 'outside-current-session',
        },
      ],
    );
  });
});

describe('cleanupOmxMcpProcesses', () => {
  it('supports dry-run without sending signals', async () => {
    const lines: string[] = [];
    let signalCount = 0;

    const result = await cleanupOmxMcpProcesses(['--dry-run'], {
      currentPid: 701,
      listProcesses: () => CURRENT_SESSION_PROCESSES,
      sendSignal: () => {
        signalCount += 1;
      },
      writeLine: (line) => lines.push(line),
    });