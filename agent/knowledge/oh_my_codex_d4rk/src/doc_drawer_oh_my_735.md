setup-scope.json)" : "";
  const backupContext = getBackupContext(resolvedScope.scope, projectRoot);

  console.log("oh-my-codex setup");
  console.log("=================\n");
  console.log(
    `Using setup scope: ${resolvedScope.scope}${scopeSourceMessage}\n`,
  );

  // Step 1: Ensure directories exist
  console.log("[1/8] Creating directories...");
  const dirs = [
    scopeDirs.codexHomeDir,
    scopeDirs.promptsDir,
    scopeDirs.skillsDir,
    scopeDirs.nativeAgentsDir,
    omxStateDir(projectRoot),
    omxPlansDir(projectRoot),
    omxLogsDir(projectRoot),
  ];
  for (const dir of dirs) {
    if (!dryRun) {
      await mkdir(dir, { recursive: true });
    }
    if (verbose) console.log(`  mkdir ${dir}`);
  }
  await persistSetupScope(projectRoot, resolvedScope.scope, {
    dryRun,