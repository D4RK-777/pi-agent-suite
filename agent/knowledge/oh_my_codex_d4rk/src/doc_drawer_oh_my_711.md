return {
    updated: 0,
    unchanged: 0,
    backedUp: 0,
    skipped: 0,
    removed: 0,
  };
}

function createEmptyRunSummary(): SetupRunSummary {
  return {
    prompts: createEmptyCategorySummary(),
    skills: createEmptyCategorySummary(),
    nativeAgents: createEmptyCategorySummary(),
    agentsMd: createEmptyCategorySummary(),
    config: createEmptyCategorySummary(),
  };
}

function getBackupContext(
  scope: SetupScope,
  projectRoot: string,
): SetupBackupContext {
  const timestamp = new Date().toISOString().replace(/[:]/g, "-");
  if (scope === "project") {
    return {
      backupRoot: join(projectRoot, ".omx", "backups", "setup", timestamp),
      baseRoot: projectRoot,
    };
  }
  return {
    backupRoot: join(homedir(), ".omx", "backups", "setup", timestamp),