{
      if ((err as NodeJS.ErrnoException).code !== 'ESRCH') {
        throw err;
      }
    }
  }

  const remainingAfterTerm = await waitForPidsToExit(
    candidates.map((candidate) => candidate.pid),
    SIGTERM_GRACE_MS,
    isPidAlive,
    sleep,
    now,
  );
  const stillRunning = candidates.filter((candidate) =>
    remainingAfterTerm.has(candidate.pid),
  );
  let terminatedCount = candidates.length - stillRunning.length;