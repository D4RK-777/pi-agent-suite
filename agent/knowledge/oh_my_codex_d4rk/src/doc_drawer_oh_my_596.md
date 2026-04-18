2. Write session state
  await resetSessionMetrics(cwd);
  await writeSessionStart(cwd, sessionId);

  // 3. Start notify fallback watcher (best effort)
  try {
    await startNotifyFallbackWatcher(cwd, { codexHomeOverride, enableAuthority: enableNotifyFallbackAuthority, sessionId });
  } catch (err) {
    process.stderr.write(`[cli/index] operation failed: ${err}\n`);
    // Non-fatal
  }

  // 4. Start derived watcher (best effort, opt-in)
  try {
    await startHookDerivedWatcher(cwd);
  } catch (err) {
    process.stderr.write(`[cli/index] operation failed: ${err}\n`);
    // Non-fatal
  }