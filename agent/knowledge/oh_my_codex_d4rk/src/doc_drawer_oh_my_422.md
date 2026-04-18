) => new Promise((resolve) => setTimeout(resolve, ms)));
  const now = dependencies.now ?? Date.now;

  const candidates = findCleanupCandidates(listProcessesImpl(), currentPid);
  if (candidates.length === 0) {
    writeLine(dryRun
      ? 'Dry run: no orphaned OMX MCP server processes found.'
      : 'No orphaned OMX MCP server processes found.');
    return {
      dryRun,
      candidates,
      terminatedCount: 0,
      forceKilledCount: 0,
      failedPids: [],
    };
  }