`  ${dryRun ? "Would remove" : "Removed"} ${summary.skillsRemoved} skill(s).`,
  );
  console.log();

  // Step 5: Remove AGENTS.md and optionally .omx/ cache directory
  console.log("[5/5] Cleaning up...");
  const agentsMdPath =
    scope === "project"
      ? join(projectRoot, "AGENTS.md")
      : join(scopeDirs.codexHomeDir, "AGENTS.md");
  summary.agentsMdRemoved = await removeAgentsMd(agentsMdPath, {
    dryRun,
    verbose,
  });
  if (purge) {
    summary.cacheDirectoryRemoved = await removeCacheDirectory(projectRoot, {
      dryRun,
      verbose,
    });
  } else {
    // Always clean up setup-scope.json and hud-config.json
    const scopeFile = join(projectRoot, ".omx", "setup-scope.json");
    const hudConfig = join(projectRoot, ".omx", "hud-config.json");