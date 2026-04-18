{
  const parentByPid = new Map<number, number>();
  const commandByPid = new Map<number, string>();

  for (const processEntry of processes) {
    parentByPid.set(processEntry.pid, processEntry.ppid);
    commandByPid.set(processEntry.pid, processEntry.command);
  }

  let pid: number | undefined = currentPid;
  while (typeof pid === 'number' && pid > 1) {
    const command = commandByPid.get(pid);
    if (command && isCodexSessionProcess(command)) return pid;
    const parentPid = parentByPid.get(pid);
    if (typeof parentPid !== 'number' || parentPid <= 0 || parentPid === pid) break;
    pid = parentPid;
  }

  return currentPid;
}