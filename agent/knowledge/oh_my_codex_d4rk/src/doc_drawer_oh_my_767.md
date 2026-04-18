const stalePromptPath = join(dstDir, file);
      if (!existsSync(stalePromptPath)) continue;

      if (!options.dryRun) {
        await rm(stalePromptPath, { force: true });
      }
      summary.removed += 1;
      if (options.verbose) {
        const prefix = options.dryRun
          ? "would remove stale prompt"
          : "removed stale prompt";
        const label = status ?? "unlisted";
        console.log(`  ${prefix} ${file} (status: ${label})`);
      }
    }
  }

  return summary;
}

async function refreshNativeAgentConfigs(
  pkgRoot: string,
  agentsDir: string,
  backupContext: SetupBackupContext,
  options: Pick<SetupOptions, "dryRun" | "verbose" | "force">,
): Promise<SetupCategorySummary> {
  const summary = createEmptyCategorySummary();