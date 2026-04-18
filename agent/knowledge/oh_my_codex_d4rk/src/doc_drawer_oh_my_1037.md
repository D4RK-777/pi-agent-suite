sSync(agentsDir)) return 0;

  let removed = 0;
  const agentNames = Object.keys(AGENT_DEFINITIONS);

  for (const name of agentNames) {
    const configFile = join(agentsDir, `${name}.toml`);
    if (!existsSync(configFile)) continue;

    if (!options.dryRun) {
      await rm(configFile, { force: true });
    }
    if (options.verbose)
      console.log(
        `  ${options.dryRun ? "Would remove" : "Removed"} agent config: ${name}.toml`,
      );
    removed++;
  }