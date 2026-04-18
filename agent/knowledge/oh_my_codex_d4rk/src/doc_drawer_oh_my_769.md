taleCandidateNativeAgentNames = new Set(
    manifest?.agents.map((agent) => agent.name) ?? [],
  );

  for (const [name, agent] of Object.entries(AGENT_DEFINITIONS)) {
    staleCandidateNativeAgentNames.add(name);
    const status = agentStatusByName?.get(name);
    if (agentStatusByName && !isInstallableStatus(status)) {
      if (options.verbose) {
        const label = status ?? "unlisted";
        console.log(`  skipped native agent ${name}.toml (status: ${label})`);
      }
      summary.skipped += 1;
      continue;
    }

    const promptPath = join(pkgRoot, "prompts", `${name}.md`);
    if (!existsSync(promptPath)) {
      continue;
    }