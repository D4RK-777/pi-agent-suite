Options, "dryRun" | "verbose">,
): Promise<boolean> {
  if (!existsSync(agentsMdPath)) return false;

  try {
    const content = await readFile(agentsMdPath, "utf-8");
    if (!isOmxGeneratedAgentsMd(content)) {
      if (options.verbose)
        console.log("  AGENTS.md is not OMX-generated, skipping.");
      return false;
    }
  } catch {
    return false;
  }

  if (!options.dryRun) {
    await rm(agentsMdPath, { force: true });
  }
  if (options.verbose)
    console.log(`  ${options.dryRun ? "Would remove" : "Removed"} AGENTS.md`);
  return true;
}

async function removeCacheDirectory(
  projectRoot: string,
  options: Pick<UninstallOptions, "dryRun" | "verbose">,
): Promise<boolean> {
  const omxDir = join(projectRoot, ".omx");
  if (!existsSync(omxDir)) return false;