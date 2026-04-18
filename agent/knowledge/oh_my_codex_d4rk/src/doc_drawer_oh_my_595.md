,
): Promise<void> {
  // 1. Generate runtime overlay + write session-scoped model instructions file
  const orchestrationMode = await resolveSessionOrchestrationMode(
    cwd,
    sessionId,
  );
  const overlay = await generateOverlay(cwd, sessionId, { orchestrationMode });
  const launchAppendix = await readLaunchAppendInstructions();
  const sessionInstructions =
    launchAppendix.trim().length > 0
      ? `${overlay}

${launchAppendix}`
      : overlay;
  await writeSessionModelInstructionsFile(cwd, sessionId, sessionInstructions);

  // 2. Write session state
  await resetSessionMetrics(cwd);
  await writeSessionStart(cwd, sessionId);