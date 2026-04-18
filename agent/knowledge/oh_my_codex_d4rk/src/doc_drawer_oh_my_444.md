hresholdMs = 60_000;
  const shutdownThresholdMs = 30_000;
  const leaderStaleThresholdMs = 180_000;

  // Rust-first: if the runtime bridge is enabled, use Rust-authored readiness
  // and authority as the semantic truth source for runtime health.
  if (isBridgeEnabled()) {
    const bridge = getDefaultBridge(stateDir);
    const readiness = bridge.readReadiness();
    const authority = bridge.readAuthority();
    if (readiness && !readiness.ready) {
      for (const reason of readiness.reasons) {
        issues.push({
          code: 'resume_blocker',
          message: `runtime not ready: ${reason}`,
          severity: 'fail',
        });
      }
    }
    if (authority?.stale) {
      issues.push({
        code: 'stale_leader',