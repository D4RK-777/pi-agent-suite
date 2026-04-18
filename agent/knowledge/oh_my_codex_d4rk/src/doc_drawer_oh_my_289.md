`agents-init target must stay inside the current working directory: ${requestedTarget}`,
    );
  }

  const targetStat = await stat(targetDir).catch(() => null);
  if (!targetStat)
    throw new Error(`agents-init target not found: ${requestedTarget}`);
  if (!targetStat.isDirectory())
    throw new Error(
      `agents-init target must be a directory: ${requestedTarget}`,
    );

  const summary = createEmptySummary();
  const plannedDirs = await resolveTargetDirectories(targetDir);
  const backupRoot = join(
    cwd,
    ".omx",
    "backups",
    "agents-init",
    new Date().toISOString().replaceAll(":", "-"),
  );
  const activeSession = await readSessionState(cwd);
  const rootSessionGuardActive = Boolean(
    activeSession && !isSessionStale(activeSession),
  );