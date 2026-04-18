nagesTui) {
    console.log("  StatusLine configured in config.toml via [tui] section.");
  } else {
    console.log("  Codex CLI >= 0.107.0 manages [tui]; OMX left that section untouched.");
  }
  console.log();

  console.log("Setup refresh summary:");
  logCategorySummary("prompts", summary.prompts);
  logCategorySummary("skills", summary.skills);
  logCategorySummary("native_agents", summary.nativeAgents);
  logCategorySummary("agents_md", summary.agentsMd);
  logCategorySummary("config", summary.config);
  console.log();

  const legacySkillOverlapNotice = await buildLegacySkillOverlapNotice(resolvedScope.scope);
  if (legacySkillOverlapNotice.shouldWarn) {
    console.log(`Migration hint: ${legacySkillOverlapNotice.message}`);
    console.log();
  }