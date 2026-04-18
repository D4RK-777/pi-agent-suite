(err) {
    if ((err as NodeJS.ErrnoException).code === 'ESRCH') return false;
    throw err;
  }
}

async function waitForPidsToExit(
  pids: readonly number[],
  timeoutMs: number,
  isPidAlive: (pid: number) => boolean,
  sleep: (ms: number) => Promise<void>,
  now: () => number,
): Promise<Set<number>> {
  const remaining = new Set(
    pids.filter((pid) => Number.isFinite(pid) && pid > 0 && isPidAlive(pid)),
  );
  if (remaining.size === 0) return remaining;

  const deadline = now() + Math.max(0, timeoutMs);
  while (now() < deadline && remaining.size > 0) {
    await sleep(PROCESS_EXIT_POLL_MS);
    for (const pid of [...remaining]) {
      if (!isPidAlive(pid)) remaining.delete(pid);
    }
  }