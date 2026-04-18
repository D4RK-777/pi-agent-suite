onst prefix = dryRun ? "[dry-run] Would remove" : "Removed";

  console.log("\nUninstall summary:");

  if (summary.configCleaned) {
    console.log(`  ${prefix} OMX configuration block from config.toml`);
    if (summary.mcpServersRemoved.length > 0) {
      console.log(`    MCP servers: ${summary.mcpServersRemoved.join(", ")}`);
    }
    if (summary.agentEntriesRemoved > 0) {
      console.log(`    Agent entries: ${summary.agentEntriesRemoved}`);
    }
    if (summary.tuiSectionRemoved) {
      console.log("    TUI status line section");
    }
    if (summary.topLevelKeysRemoved) {
      console.log(
        "    Top-level keys (notify, model_reasoning_effort, developer_instructions)",
      );
    }
    if (summary.featureFlagsRemoved) {