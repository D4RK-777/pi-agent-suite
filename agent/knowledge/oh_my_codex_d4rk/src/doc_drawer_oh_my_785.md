const syncPlan = planClaudeCodeMcpSettingsSync(
    existing,
    sharedMcpRegistry.servers,
  );

  for (const warning of syncPlan.warnings) {
    console.log(`  warning: ${warning}`);
  }
  if (syncPlan.warnings.length > 0) {
    summary.skipped += 1;
    return;
  }
  if (!syncPlan.content) {
    summary.unchanged += 1;
    if (options.verbose && syncPlan.unchanged.length > 0) {
      console.log(
        `  shared MCP servers already present in Claude Code settings (${settingsPath})`,
      );
    }
    return;
  }

  await syncManagedContent(
    syncPlan.content,
    settingsPath,
    summary,
    backupContext,
    options,
    `Claude Code MCP settings ${settingsPath} (+${syncPlan.added.join(", ")})`,
  );
}