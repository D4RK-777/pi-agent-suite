ync(process.execPath, [omxBin, ...argv], {
    cwd,
    encoding: 'utf-8',
    env: mergedEnv,
  });
  return { status: r.status, stdout: r.stdout || '', stderr: r.stderr || '', error: r.error?.message };
}

function shouldSkipForSpawnPermissions(err?: string): boolean {
  return typeof err === 'string' && /(EPERM|EACCES)/i.test(err);
}

describe('omx doctor onboarding warning copy', () => {
  it('explains first-setup expectation for config and MCP onboarding warnings', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-doctor-copy-'));
    try {
      const home = join(wd, 'home');
      const codexDir = join(home, '.codex');
      await mkdir(codexDir, { recursive: true });
      await writeFile(
        join(codexDir, 'config.toml'),
        `
[mcp_servers.non_omx]