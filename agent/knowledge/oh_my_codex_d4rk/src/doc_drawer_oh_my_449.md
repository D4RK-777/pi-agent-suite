erDir, 'shutdown-request.json');
      const shutdownAckPath = join(workerDir, 'shutdown-ack.json');

      if (existsSync(statusPath) && existsSync(heartbeatPath)) {
        try {
          const [statusRaw, hbRaw] = await Promise.all([
            readFile(statusPath, 'utf-8'),
            readFile(heartbeatPath, 'utf-8'),
          ]);
          const status = JSON.parse(statusRaw) as { state?: string };
          const hb = JSON.parse(hbRaw) as { last_turn_at?: string };
          const lastTurnMs = hb.last_turn_at ? Date.parse(hb.last_turn_at) : NaN;
          if (status.state === 'working' && Number.isFinite(lastTurnMs) && nowMs - lastTurnMs > lagThresholdMs) {
            issues.push({
              code: 'delayed_status_lag',