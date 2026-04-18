');
  if (!existsSync(nodeWrapper)) {
    writeFileSync(nodeWrapper, '#!/bin/sh\nexec node "$@"\n');
    chmodSync(nodeWrapper, 0o755);
  }
  const r = spawnSync(nodeWrapper, [omxBin, ...argv], {
    cwd,
    encoding: 'utf-8',
    env: { ...process.env, ...envOverrides },
  });
  return { status: r.status, stdout: r.stdout || '', stderr: r.stderr || '', error: r.error?.message };
}

function shouldSkipForSpawnPermissions(err?: string): boolean {
  return typeof err === 'string' && /(EPERM|EACCES)/i.test(err);
}