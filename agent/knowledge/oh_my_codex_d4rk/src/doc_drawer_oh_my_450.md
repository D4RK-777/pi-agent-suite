- lastTurnMs > lagThresholdMs) {
            issues.push({
              code: 'delayed_status_lag',
              message: `${teamName}/${worker.name} working with stale heartbeat`,
              severity: 'fail',
            });
          }
        } catch {
          // ignore malformed files
        }
      }

      if (existsSync(shutdownReqPath) && !existsSync(shutdownAckPath)) {
        try {
          const reqRaw = await readFile(shutdownReqPath, 'utf-8');
          const req = JSON.parse(reqRaw) as { requested_at?: string };
          const reqMs = req.requested_at ? Date.parse(req.requested_at) : NaN;
          if (Number.isFinite(reqMs) && nowMs - reqMs > shutdownThresholdMs) {
            issues.push({
              code: 'slow_shutdown',