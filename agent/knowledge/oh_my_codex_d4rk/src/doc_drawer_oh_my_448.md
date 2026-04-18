teamName} references missing tmux session ${tmuxSession}`,
        severity: 'fail',
      });
    }

    // delayed_status_lag + slow_shutdown checks
    const workersRoot = join(teamDir, 'workers');
    if (!existsSync(workersRoot)) continue;
    const workers = await readdir(workersRoot, { withFileTypes: true });
    for (const worker of workers) {
      if (!worker.isDirectory()) continue;
      const workerDir = join(workersRoot, worker.name);
      const statusPath = join(workerDir, 'status.json');
      const heartbeatPath = join(workerDir, 'heartbeat.json');
      const shutdownReqPath = join(workerDir, 'shutdown-request.json');
      const shutdownAckPath = join(workerDir, 'shutdown-ack.json');