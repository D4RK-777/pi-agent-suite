${dryRun ? "Would remove" : "Removed"} ${summary.promptsRemoved} prompt(s).`,
  );
  console.log();

  // Step 3: Remove native agent configs
  console.log("[3/5] Removing native agent configs...");
  summary.agentConfigsRemoved = await removeAgentConfigs(
    scopeDirs.nativeAgentsDir,
    { dryRun, verbose },
  );
  console.log(
    `  ${dryRun ? "Would remove" : "Removed"} ${summary.agentConfigsRemoved} agent config(s).`,
  );
  console.log();

  // Step 4: Remove installed skills
  console.log("[4/5] Removing skills...");
  summary.skillsRemoved = await removeInstalledSkills(
    scopeDirs.skillsDir,
    pkgRoot,
    { dryRun, verbose },
  );
  console.log(
    `  ${dryRun ? "Would remove" : "Removed"} ${summary.skillsRemoved} skill(s).`,
  );
  console.log();