odeSettingsPath(homeDir = homedir()): string {
  return join(homeDir, ".claude", "settings.json");
}

async function syncClaudeCodeMcpSettings(
  sharedMcpRegistry: UnifiedMcpRegistryLoadResult,
  summary: SetupCategorySummary,
  backupContext: SetupBackupContext,
  options: Pick<SetupOptions, "dryRun" | "verbose">,
): Promise<void> {
  if (sharedMcpRegistry.servers.length === 0) return;

  const settingsPath = getClaudeCodeSettingsPath();
  const existing = existsSync(settingsPath)
    ? await readFile(settingsPath, "utf-8")
    : "";
  const syncPlan = planClaudeCodeMcpSettingsSync(
    existing,
    sharedMcpRegistry.servers,
  );