h(arg);
  }

  if (!hasBypass) {
    normalized.push(CODEX_BYPASS_FLAG);
  }

  return normalized;
}

function runAutoresearchTurn(worktreePath: string, instructionsFile: string, codexArgs: string[]): void {
  const prompt = readFileSync(instructionsFile, 'utf-8');
  const launchArgs = ['exec', ...normalizeAutoresearchCodexArgs(codexArgs), '-'];
  const result = spawnSync('codex', launchArgs, {
    cwd: worktreePath,
    stdio: ['pipe', 'inherit', 'inherit'],
    input: prompt,
    encoding: 'utf-8',
    env: process.env,
      windowsHide: true,
    });