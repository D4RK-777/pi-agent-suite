if ((err as NodeJS.ErrnoException).code !== 'ESRCH') {
          throw err;
        }
      }
    }

    const remainingAfterKill = await waitForPidsToExit(
      stillRunning.map((candidate) => candidate.pid),
      PROCESS_EXIT_POLL_MS,
      isPidAlive,
      sleep,
      now,
    );
    forceKilledCount = stillRunning.length - remainingAfterKill.size;
    terminatedCount += forceKilledCount;
    failedPids.push(...remainingAfterKill);
  }

  writeLine(`Killed ${terminatedCount} orphaned OMX MCP server process(es)${forceKilledCount > 0 ? ` (${forceKilledCount} required SIGKILL)` : ''}.`);
  if (failedPids.length > 0) {
    writeLine(`Warning: ${failedPids.length} process(es) still appear alive: ${failedPids.join(', ')}`);
  }