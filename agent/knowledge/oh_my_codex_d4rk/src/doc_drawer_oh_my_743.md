copeDirs.codexConfigFile,
    pkgRoot,
    sharedMcpRegistry,
    summary.config,
    backupContext,
    { codexVersionProbe: options.codexVersionProbe, dryRun, verbose, modelUpgradePrompt },
  );
  const resolvedConfig = managedConfig.finalConfig;
  if (resolvedScope.scope === "user") {
    await syncClaudeCodeMcpSettings(
      sharedMcpRegistry,
      summary.config,
      backupContext,
      { dryRun, verbose },
    );
  }
  console.log(`  Config refresh complete (${scopeDirs.codexConfigFile}).\n`);