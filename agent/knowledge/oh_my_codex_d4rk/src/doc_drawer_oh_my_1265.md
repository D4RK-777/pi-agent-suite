ExploreHarnessCommand,
  resolveExploreHarnessCommandWithHydration,
  resolveExploreSparkShellRoute,
  resolvePackagedExploreHarnessCommand,
} from '../explore.js';
import { withPackagedExploreHarnessHidden, withPackagedExploreHarnessLock } from './packaged-explore-harness-lock.js';

function runOmx(
  cwd: string,
  argv: string[],
  envOverrides: Record<string, string> = {},
): { status: number | null; stdout: string; stderr: string; error?: string } {
  const testDir = dirname(fileURLToPath(import.meta.url));
  const repoRoot = join(testDir, '..', '..', '..');
  const omxBin = join(repoRoot, 'dist', 'cli', 'omx.js');
  const nodeWrapper = join(cwd, '.omx-test-node.sh');
  if (!existsSync(nodeWrapper)) {
    writeFileSync(nodeWrapper, '#!/bin/sh\nexec node "$@"\n');