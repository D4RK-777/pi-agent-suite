,
  );
  const normalizedArgs = normalizeCodexLaunchArgs(
    notifyTempResult.passthroughArgs,
  );
  let cwd = launchCwd;
  if (parsedWorktree.mode.enabled) {
    const planned = planWorktreeTarget({
      cwd: launchCwd,
      scope: "launch",
      mode: parsedWorktree.mode,
    });
    const ensured = ensureWorktree(planned);
    if (ensured.enabled) {
      cwd = ensured.worktreePath;
    }
  }
  const sessionId = `omx-${Date.now()}-${Math.random().toString(36).slice(2, 8)}`;

  try {
    await maybeCheckAndPromptUpdate(cwd);
  } catch (err) {
    process.stderr.write(`[cli/index] operation failed: ${err}\n`);
    // Non-fatal: update checks must never block launch
  }