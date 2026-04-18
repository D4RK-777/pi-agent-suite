h = join(pkgRoot, "prompts", `${name}.md`);
    if (!existsSync(promptPath)) {
      continue;
    }

    const promptContent = await readFile(promptPath, "utf-8");
    const toml = generateAgentToml(agent, promptContent, {
      codexHomeOverride: join(agentsDir, ".."),
    });
    const dst = join(agentsDir, `${name}.toml`);
    await syncManagedContent(
      toml,
      dst,
      summary,
      backupContext,
      options,
      `native agent ${name}.toml`,
    );
  }

  summary.removed += await cleanupObsoleteNativeAgents(
    agentsDir,
    backupContext,
    options,
  );