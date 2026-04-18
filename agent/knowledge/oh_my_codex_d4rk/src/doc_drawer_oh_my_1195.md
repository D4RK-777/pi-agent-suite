2,
    command: 'node /tmp/worktree/dist/mcp/trace-server.js',
  },
  {
    pid: 811,
    ppid: 810,
    command: 'node /tmp/worktree/dist/mcp/team-server.js',
  },
  {
    pid: 900,
    ppid: 1,
    command: 'node /tmp/not-omx/other-server.js',
  },
];

describe('findCleanupCandidates', () => {
  it('selects orphaned OMX MCP processes while preserving the current session tree', () => {
    assert.deepEqual(
      findCleanupCandidates(CURRENT_SESSION_PROCESSES, 701),
      [
        {
          pid: 800,
          ppid: 1,
          command: 'node /tmp/oh-my-codex/dist/mcp/memory-server.js',
          reason: 'ppid=1',
        },
        {
          pid: 810,
          ppid: 42,
          command: 'node /tmp/worktree/dist/mcp/trace-server.js',
          reason: 'outside-current-session',