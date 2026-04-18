candidates,
      terminatedCount: 0,
      forceKilledCount: 0,
      failedPids: [],
    };
  }

  if (dryRun) {
    writeLine(`Dry run: would terminate ${candidates.length} orphaned OMX MCP server process(es):`);
    for (const candidate of candidates) writeLine(`  ${formatCandidate(candidate)}`);
    return {
      dryRun: true,
      candidates,
      terminatedCount: 0,
      forceKilledCount: 0,
      failedPids: [],
    };
  }

  writeLine(`Found ${candidates.length} orphaned OMX MCP server process(es). Sending SIGTERM...`);
  for (const candidate of candidates) {
    try {
      sendSignal(candidate.pid, 'SIGTERM');
    } catch (err) {
      if ((err as NodeJS.ErrnoException).code !== 'ESRCH') {
        throw err;
      }
    }
  }