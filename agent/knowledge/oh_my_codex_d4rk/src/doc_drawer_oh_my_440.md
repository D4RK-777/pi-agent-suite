ths.promptsDir));

  // Check 6: Skills installed
  checks.push(await checkSkills(paths.skillsDir));

  // Check 6.5: Legacy/current skill-root overlap
  if (scopeResolution.scope === 'user') {
    checks.push(await checkLegacySkillRootOverlap());
  }

  // Check 7: AGENTS.md in project
  checks.push(checkAgentsMd(scopeResolution.scope, paths.codexHomeDir));

  // Check 8: State directory
  checks.push(checkDirectory('State dir', paths.stateDir));

  // Check 9: MCP servers configured
  checks.push(await checkMcpServers(paths.configPath));

  // Print results
  let passCount = 0;
  let warnCount = 0;
  let failCount = 0;