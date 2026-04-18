number; signal: NodeJS.Signals }> = [];
    const alive = new Set([800, 810]);
    let fakeNow = 0;

    const result = await cleanupOmxMcpProcesses([], {
      currentPid: 701,
      listProcesses: () => [
        ...CURRENT_SESSION_PROCESSES.filter((processEntry) => processEntry.pid !== 811),
      ],
      isPidAlive: (pid) => alive.has(pid),
      sendSignal: (pid, signal) => {
        signals.push({ pid, signal });
        if (signal === 'SIGTERM' && pid === 800) alive.delete(pid);
        if (signal === 'SIGKILL') alive.delete(pid);
      },
      sleep: async (ms) => {
        fakeNow += ms;
      },
      now: () => fakeNow,
      writeLine: (line) => lines.push(line),
    });