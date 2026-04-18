gedExploreHarnessHidden, withPackagedExploreHarnessLock } from './packaged-explore-harness-lock.js';

function runOmx(
  cwd: string,
  argv: string[],
  envOverrides: Record<string, string> = {},
): { status: number | null; stdout: string; stderr: string; error?: string } {
  const testDir = dirname(fileURLToPath(import.meta.url));
  const repoRoot = join(testDir, '..', '..', '..');
  const omxBin = join(repoRoot, 'dist', 'cli', 'omx.js');
  const mergedEnv = { ...process.env, ...envOverrides };
  if (typeof envOverrides.HOME === 'string' && typeof envOverrides.USERPROFILE !== 'string') {
    mergedEnv.USERPROFILE = envOverrides.HOME;
  }
  const r = spawnSync(process.execPath, [omxBin, ...argv], {
    cwd,
    encoding: 'utf-8',
    env: mergedEnv,
  });