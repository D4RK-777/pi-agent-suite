ber' || parentPid <= 0 || parentPid === pid) break;
    pid = parentPid;
  }

  return currentPid;
}

export function buildProtectedPidSet(
  processes: readonly ProcessEntry[],
  currentPid: number,
): Set<number> {
  const childrenByPid = new Map<number, number[]>();

  for (const processEntry of processes) {
    const siblings = childrenByPid.get(processEntry.ppid) ?? [];
    siblings.push(processEntry.pid);
    childrenByPid.set(processEntry.ppid, siblings);
  }

  const protectedRootPid = resolveProtectedRootPid(processes, currentPid);
  const protectedPids = new Set<number>();
  const descendants = [protectedRootPid];