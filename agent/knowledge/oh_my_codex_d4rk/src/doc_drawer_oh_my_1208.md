, [omxBin, ...argv], {
    cwd,
    encoding: 'utf-8',
    env: { ...process.env, ...envOverrides },
  });
  return { status: r.status, stdout: r.stdout || '', stderr: r.stderr || '', error: r.error?.message };
}

function shouldSkipForSpawnPermissions(err?: string): boolean {
  return typeof err === 'string' && /(EPERM|EACCES)/i.test(err);
}

describe('omx doctor invalid config detection', () => {
  it('fails when config.toml contains duplicate [tui] tables', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-doctor-invalid-config-'));
    try {
      const home = join(wd, 'home');
      const codexDir = join(home, '.codex');
      await mkdir(codexDir, { recursive: true });

      await writeFile(
        join(codexDir, 'config.toml'),
        `
model = "gpt-5.4"