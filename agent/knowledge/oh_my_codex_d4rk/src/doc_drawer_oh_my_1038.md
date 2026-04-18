ptions.dryRun ? "Would remove" : "Removed"} agent config: ${name}.toml`,
      );
    removed++;
  }

  // If the agents dir is now empty, remove it too
  if (!options.dryRun && existsSync(agentsDir)) {
    try {
      const remaining = await readdir(agentsDir);
      if (remaining.length === 0) {
        await rm(agentsDir, { recursive: true, force: true });
        if (options.verbose) console.log("  Removed empty agents directory.");
      }
    } catch {
      // Ignore errors when cleaning up empty dir
    }
  }

  return removed;
}

async function removeAgentsMd(
  agentsMdPath: string,
  options: Pick<UninstallOptions, "dryRun" | "verbose">,
): Promise<boolean> {
  if (!existsSync(agentsMdPath)) return false;