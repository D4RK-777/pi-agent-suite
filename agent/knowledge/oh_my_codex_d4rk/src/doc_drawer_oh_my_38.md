Dir, "..");

  if (!dryRun) {
    await mkdir(agentsDir, { recursive: true });
  }

  let count = 0;

  for (const [name, agent] of Object.entries(AGENT_DEFINITIONS)) {
    const promptPath = join(pkgRoot, "prompts", `${name}.md`);
    if (!existsSync(promptPath)) {
      if (verbose) console.log(`  skip ${name} (no prompt file)`);
      continue;
    }

    const dst = join(agentsDir, `${name}.toml`);
    if (!force && existsSync(dst)) {
      if (verbose) console.log(`  skip ${name} (already exists)`);
      continue;
    }

    const promptContent = await readFile(promptPath, "utf-8");
    const toml = generateAgentToml(agent, promptContent, { codexHomeOverride });