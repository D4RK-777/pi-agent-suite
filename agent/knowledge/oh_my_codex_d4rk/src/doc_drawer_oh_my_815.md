: () => StarRepoResult;
  logFn?: (message: string) => void;
  warnFn?: (message: string) => void;
}

export function starRepo(spawnSyncFn: typeof childProcess.spawnSync = childProcess.spawnSync): StarRepoResult {
  const result = spawnSyncFn('gh', ['api', '-X', 'PUT', `/user/starred/${REPO}`], {
    encoding: 'utf-8',
    stdio: ['ignore', 'pipe', 'pipe'],
    timeout: 10000,
  });
  if (result.error) return { ok: false, error: result.error.message };
  if (result.status !== 0) {
    const stderr = (result.stderr || '').trim();
    const stdout = (result.stdout || '').trim();
    return { ok: false, error: stderr || stdout || `gh exited ${result.status}` };
  }
  return { ok: true };
}