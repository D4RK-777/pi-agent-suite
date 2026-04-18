number,
): CleanupCandidate[] {
  const protectedPids = buildProtectedPidSet(processes, currentPid);

  return processes
    .filter((processEntry) => processEntry.pid !== currentPid)
    .filter((processEntry) => isOmxMcpProcess(processEntry.command))
    .filter((processEntry) => !protectedPids.has(processEntry.pid))
    .sort((left, right) => left.pid - right.pid)
    .map((processEntry) => ({
      ...processEntry,
      reason: processEntry.ppid <= 1 ? 'ppid=1' : 'outside-current-session',
    }));
}

function defaultIsPidAlive(pid: number): boolean {
  if (!Number.isFinite(pid) || pid <= 0) return false;
  try {
    process.kill(pid, 0);
    return true;
  } catch (err) {
    if ((err as NodeJS.ErrnoException).code === 'ESRCH') return false;
    throw err;
  }
}