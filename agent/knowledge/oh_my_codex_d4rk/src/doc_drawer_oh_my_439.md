);

  const checks: Check[] = [];

  // Check 1: Codex CLI installed
  checks.push(checkCodexCli());

  // Check 2: Node.js version
  checks.push(checkNodeVersion());

  // Check 2.5: Explore harness readiness
  checks.push(checkExploreHarness());

  // Check 3: Codex home directory
  checks.push(checkDirectory('Codex home', paths.codexHomeDir));

  // Check 4: Config file
  checks.push(await checkConfig(paths.configPath));

  // Check 4.5: Explore routing default
  checks.push(await checkExploreRouting(paths.configPath));

  // Check 5: Prompts installed
  checks.push(await checkPrompts(paths.promptsDir));

  // Check 6: Skills installed
  checks.push(await checkSkills(paths.skillsDir));