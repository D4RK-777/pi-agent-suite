ry.removed += await cleanupObsoleteNativeAgents(
    agentsDir,
    backupContext,
    options,
  );

  if (options.force && manifest && existsSync(agentsDir)) {
    const installedFiles = await readdir(agentsDir);
    for (const file of installedFiles) {
      if (!file.endsWith(".toml")) continue;
      const agentName = file.slice(0, -5);
      const agentStatus = agentStatusByName?.get(agentName);
      if (isInstallableStatus(agentStatus)) continue;
      if (
        !staleCandidateNativeAgentNames.has(agentName) &&
        agentStatus === undefined
      )
        continue;

      const staleAgentPath = join(agentsDir, file);
      if (!existsSync(staleAgentPath)) continue;