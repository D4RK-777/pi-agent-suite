{
    if (options.verbose) console.log("  config.toml not found, skipping.");
    return result;
  }

  const original = await readFile(configPath, "utf-8");
  const detected = detectOmxConfigArtifacts(original);

  result.mcpServersRemoved = detected.hasMcpServers;
  result.agentEntriesRemoved = detected.hasAgentEntries;
  result.tuiSectionRemoved = detected.hasTuiSection;
  result.topLevelKeysRemoved = detected.hasTopLevelKeys;
  result.featureFlagsRemoved = detected.hasFeatureFlags;

  // Strip OMX tables block (MCP servers, agents, tui)
  let config = original;
  const { cleaned } = stripExistingOmxBlocks(config);
  config = cleaned;

  // Strip top-level keys
  config = stripOmxTopLevelKeys(config);

  // Strip feature flags
  config = stripOmxFeatureFlags(config);