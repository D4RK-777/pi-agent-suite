g = stripOmxTopLevelKeys(config);

  // Strip feature flags
  config = stripOmxFeatureFlags(config);

  // Strip OMX-managed env defaults
  config = stripOmxEnvSettings(config);

  // Normalize trailing whitespace
  config = config.trimEnd() + "\n";

  if (config !== original) {
    result.configCleaned = true;
    if (!options.dryRun) {
      await writeFile(configPath, config);
    }
    if (options.verbose) {
      console.log(
        `  ${options.dryRun ? "Would clean" : "Cleaned"} ${configPath}`,
      );
    }
  } else {
    if (options.verbose) console.log("  No OMX config entries found.");
  }

  return result;
}