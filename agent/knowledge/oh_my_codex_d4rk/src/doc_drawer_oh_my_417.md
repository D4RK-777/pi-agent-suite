s, currentPid);
  const protectedPids = new Set<number>();
  const descendants = [protectedRootPid];

  while (descendants.length > 0) {
    const pid = descendants.pop()!;
    if (protectedPids.has(pid)) continue;
    protectedPids.add(pid);
    for (const childPid of childrenByPid.get(pid) ?? []) {
      if (!protectedPids.has(childPid)) descendants.push(childPid);
    }
  }

  return protectedPids;
}

export function findCleanupCandidates(
  processes: readonly ProcessEntry[],
  currentPid: number,
): CleanupCandidate[] {
  const protectedPids = buildProtectedPidSet(processes, currentPid);