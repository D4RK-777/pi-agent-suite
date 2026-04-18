d: 0,
    agentConfigsRemoved: 0,
    agentsMdRemoved: false,
    cacheDirectoryRemoved: false,
  };

  // Step 1: Clean config.toml
  if (keepConfig) {
    console.log("[1/5] Skipping config.toml cleanup (--keep-config).");
  } else {
    console.log("[1/5] Cleaning config.toml...");
    const configResult = await cleanConfig(scopeDirs.codexConfigFile, {
      dryRun,
      verbose,
    });
    Object.assign(summary, configResult);
  }
  console.log();

  // Step 2: Remove installed prompts
  console.log("[2/5] Removing agent prompts...");
  summary.promptsRemoved = await removeInstalledPrompts(
    scopeDirs.promptsDir,
    pkgRoot,
    { dryRun, verbose },
  );
  console.log(
    `  ${dryRun ? "Would remove" : "Removed"} ${summary.promptsRemoved} prompt(s).`,
  );
  console.log();