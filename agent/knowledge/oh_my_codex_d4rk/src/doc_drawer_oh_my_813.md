tarPromptStatePath(),
    JSON.stringify({ prompted_at: new Date().toISOString() }, null, 2),
  );
}

export function isGhInstalled(): boolean {
  const result = childProcess.spawnSync('gh', ['--version'], {
    encoding: 'utf-8',
    stdio: ['ignore', 'ignore', 'ignore'],
    timeout: 3000,
      windowsHide: true,
    });
  return !result.error && result.status === 0;
}

export type StarRepoResult = { ok: true } | { ok: false; error: string };