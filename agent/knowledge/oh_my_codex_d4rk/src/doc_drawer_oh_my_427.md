eLine(`Warning: ${failedPids.length} process(es) still appear alive: ${failedPids.join(', ')}`);
  }

  return {
    dryRun: false,
    candidates,
    terminatedCount,
    forceKilledCount,
    failedPids,
  };
}

export async function cleanupStaleTmpDirectories(
  args: readonly string[],
  dependencies: TmpCleanupDependencies = {},
): Promise<number> {
  const dryRun = args.includes('--dry-run');
  const tmpRoot = dependencies.tmpRoot ?? tmpdir();
  const listTmpEntries = dependencies.listTmpEntries ?? ((root: string) => readdir(root, { withFileTypes: true }));
  const statPath = dependencies.statPath ?? stat;
  const removePath = dependencies.removePath ?? ((path: string) => rm(path, { recursive: true, force: true }));
  const now = dependencies.now ?? Date.now;