for (const pid of [...remaining]) {
      if (!isPidAlive(pid)) remaining.delete(pid);
    }
  }

  for (const pid of [...remaining]) {
    if (!isPidAlive(pid)) remaining.delete(pid);
  }

  return remaining;
}

function formatCandidate(candidate: CleanupCandidate): string {
  return `PID ${candidate.pid} (PPID ${candidate.ppid}, ${candidate.reason}) ${candidate.command}`;
}

export async function cleanupOmxMcpProcesses(
  args: readonly string[],
  dependencies: CleanupDependencies = {},
): Promise<CleanupResult> {
  if (args.includes('--help') || args.includes('-h')) {
    dependencies.writeLine?.(HELP) ?? console.log(HELP);
    return {
      dryRun: true,
      candidates: [],
      terminatedCount: 0,
      forceKilledCount: 0,
      failedPids: [],
    };
  }