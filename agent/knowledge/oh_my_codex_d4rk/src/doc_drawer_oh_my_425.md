gAfterTerm.has(candidate.pid),
  );
  let terminatedCount = candidates.length - stillRunning.length;

  let forceKilledCount = 0;
  const failedPids: number[] = [];
  if (stillRunning.length > 0) {
    writeLine(`Escalating to SIGKILL for ${stillRunning.length} process(es) still alive after ${SIGTERM_GRACE_MS / 1000}s.`);
    for (const candidate of stillRunning) {
      try {
        sendSignal(candidate.pid, 'SIGKILL');
      } catch (err) {
        if ((err as NodeJS.ErrnoException).code !== 'ESRCH') {
          throw err;
        }
      }
    }