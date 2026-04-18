x-pane',
    argv: ['tmux', ...buildCapturePaneArgv(paneId, sawTailLines ? tailLines : 200)],
  };
}

function runSparkShellFallback(args: readonly string[], options: RunSparkShellFallbackOptions = {}): void {
  const { announce = true } = options;
  const invocation = parseSparkShellFallbackInvocation(args);
  if (announce) {
    process.stderr.write('[sparkshell] native sidecar unavailable; falling back to raw command execution without summary support.\n');
  }
  const result = spawnSync(invocation.argv[0], invocation.argv.slice(1), {
    cwd: process.cwd(),
    env: process.env,
    stdio: 'inherit',
    encoding: 'utf-8',
  });
  if (result.error) {
    const errno = result.error as NodeJS.ErrnoException;
    const kind = classifySpawnError(errno);
    if (kind === 'missing') {