0;

  let removed = 0;
  const sourceEntries = await readdir(srcSkillsDir, { withFileTypes: true });

  for (const entry of sourceEntries) {
    if (!entry.isDirectory()) continue;
    const installed = join(skillsDir, entry.name);
    if (!existsSync(installed)) continue;

    if (!options.dryRun) {
      await rm(installed, { recursive: true, force: true });
    }
    if (options.verbose)
      console.log(
        `  ${options.dryRun ? "Would remove" : "Removed"} skill: ${entry.name}/`,
      );
    removed++;
  }

  return removed;
}

async function removeAgentConfigs(
  agentsDir: string,
  options: Pick<UninstallOptions, "dryRun" | "verbose">,
): Promise<number> {
  if (!existsSync(agentsDir)) return 0;

  let removed = 0;
  const agentNames = Object.keys(AGENT_DEFINITIONS);