tries,
    hasTuiSection,
    hasTopLevelKeys,
    hasFeatureFlags,
    hasExploreRoutingEnv,
  };
}

async function cleanConfig(
  configPath: string,
  options: Pick<UninstallOptions, "dryRun" | "verbose">,
): Promise<
  Pick<
    UninstallSummary,
    | "configCleaned"
    | "mcpServersRemoved"
    | "agentEntriesRemoved"
    | "tuiSectionRemoved"
    | "topLevelKeysRemoved"
    | "featureFlagsRemoved"
  >
> {
  const result = {
    configCleaned: false,
    mcpServersRemoved: [] as string[],
    agentEntriesRemoved: 0,
    tuiSectionRemoved: false,
    topLevelKeysRemoved: false,
    featureFlagsRemoved: false,
  };

  if (!existsSync(configPath)) {
    if (options.verbose) console.log("  config.toml not found, skipping.");
    return result;
  }