ale OMX /tmp directory',
      'stale OMX /tmp directories',
    )}.`,
  );
  return removedCount;
}

export async function cleanupCommand(
  args: string[],
  dependencies: CleanupCommandDependencies = {},
): Promise<void> {
  const cleanupProcesses = dependencies.cleanupProcesses ?? cleanupOmxMcpProcesses;
  const cleanupTmpDirectories = dependencies.cleanupTmpDirectories ?? cleanupStaleTmpDirectories;

  await cleanupProcesses(args);
  if (args.includes('--help') || args.includes('-h')) return;
  await cleanupTmpDirectories(args);
}