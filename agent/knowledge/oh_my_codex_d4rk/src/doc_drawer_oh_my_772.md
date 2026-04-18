const staleAgentPath = join(agentsDir, file);
      if (!existsSync(staleAgentPath)) continue;

      if (!options.dryRun) {
        await rm(staleAgentPath, { force: true });
      }
      summary.removed += 1;
      if (options.verbose) {
        const prefix = options.dryRun
          ? "would remove stale native agent"
          : "removed stale native agent";
        const label = agentStatus ?? "unlisted";
        console.log(`  ${prefix} ${file} (status: ${label})`);
      }
    }
  }

  return summary;
}

async function cleanupObsoleteNativeAgents(
  agentsDir: string,
  backupContext: SetupBackupContext,
  options: Pick<SetupOptions, "dryRun" | "verbose">,
): Promise<number> {
  if (!existsSync(agentsDir)) return 0;