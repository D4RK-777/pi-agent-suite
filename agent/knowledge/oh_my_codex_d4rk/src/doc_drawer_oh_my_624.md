tch (err) {
    process.stderr.write(`[cli/index] operation failed: ${err}\n`);
    // Non-fatal
  }

  // 0. Flush derived watcher once on shutdown (opt-in, best effort).
  try {
    await flushHookDerivedWatcherOnce(cwd);
  } catch (err) {
    process.stderr.write(`[cli/index] operation failed: ${err}\n`);
    // Non-fatal
  }

  // 0.1 Stop derived watcher first (opt-in, best effort).
  try {
    await stopHookDerivedWatcher(cwd);
  } catch (err) {
    process.stderr.write(`[cli/index] operation failed: ${err}\n`);
    // Non-fatal
  }