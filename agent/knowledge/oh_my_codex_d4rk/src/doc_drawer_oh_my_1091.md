urn { status: r.status, stdout: r.stdout || '', stderr: r.stderr || '', error: r.error?.message };
}

function runProviderAdvisorScript(
  cwd: string,
  argv: string[],
): { status: number | null; stdout: string; stderr: string; error?: string } {
  const testDir = dirname(fileURLToPath(import.meta.url));
  const repoRoot = join(testDir, '..', '..', '..');
  const scriptPath = join(repoRoot, 'dist', 'scripts', 'run-provider-advisor.js');
  const r = spawnSync(process.execPath, [scriptPath, ...argv], {
    cwd,
    encoding: 'utf-8',
    env: process.env,
  });
  return { status: r.status, stdout: r.stdout || '', stderr: r.stderr || '', error: r.error?.message };
}