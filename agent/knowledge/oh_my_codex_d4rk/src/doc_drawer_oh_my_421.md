andidates: [],
      terminatedCount: 0,
      forceKilledCount: 0,
      failedPids: [],
    };
  }

  const dryRun = args.includes('--dry-run');
  const writeLine = dependencies.writeLine ?? ((line: string) => console.log(line));
  const currentPid = dependencies.currentPid ?? process.pid;
  const listProcessesImpl = dependencies.listProcesses ?? listOmxProcesses;
  const isPidAlive = dependencies.isPidAlive ?? defaultIsPidAlive;
  const sendSignal = dependencies.sendSignal ?? ((pid: number, signal: NodeJS.Signals) => process.kill(pid, signal));
  const sleep = dependencies.sleep ?? ((ms: number) => new Promise((resolve) => setTimeout(resolve, ms)));
  const now = dependencies.now ?? Date.now;