tch (err) {
    process.stderr.write(`[cli/index] operation failed: ${err}\n`);
    // Non-fatal
  }

  // 0. Flush fallback watcher once to reduce race with fast codex exit.
  try {
    await flushNotifyFallbackOnce(cwd, { codexHomeOverride, enableAuthority: enableNotifyFallbackAuthority, sessionId });
  } catch (err) {
    process.stderr.write(`[cli/index] operation failed: ${err}\n`);
    // Non-fatal
  }

  // 0. Stop notify fallback watcher first.
  try {
    await stopNotifyFallbackWatcher(cwd);
  } catch (err) {
    process.stderr.write(`[cli/index] operation failed: ${err}\n`);
    // Non-fatal
  }