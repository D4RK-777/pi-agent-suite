log("[dry-run mode] No files will be modified.\n");
  }
  console.log(`Resolved scope: ${scope}\n`);

  const summary: UninstallSummary = {
    configCleaned: false,
    mcpServersRemoved: [],
    agentEntriesRemoved: 0,
    tuiSectionRemoved: false,
    topLevelKeysRemoved: false,
    featureFlagsRemoved: false,
    promptsRemoved: 0,
    skillsRemoved: 0,
    agentConfigsRemoved: 0,
    agentsMdRemoved: false,
    cacheDirectoryRemoved: false,
  };