.map((s) => s.trim())
    .filter((s) => s.startsWith('omx-team-'));
  return new Set(sessions);
}

function checkCodexCli(): Check {
  const { result } = spawnPlatformCommandSync('codex', ['--version'], {
    encoding: 'utf-8',
    stdio: ['pipe', 'pipe', 'pipe'],
  });
  if (result.error) {
    const code = (result.error as NodeJS.ErrnoException).code;
    const kind = classifySpawnError(result.error as NodeJS.ErrnoException);
    if (kind === 'missing') {
      return { name: 'Codex CLI', status: 'fail', message: 'not found - install from https://github.com/openai/codex' };
    }
    if (kind === 'blocked') {
      return {
        name: 'Codex CLI',
        status: 'fail',
        message: `found but could not be executed in this environment (${code || 'blocked'})`,
      };
    }