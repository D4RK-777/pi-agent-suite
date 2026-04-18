console.log(
      `  ${options.dryRun ? "would update" : "updated"} ${verboseLabel}`,
    );
  }
}

async function syncManagedAgentsContent(
  content: string,
  dstPath: string,
  summary: SetupCategorySummary,
  backupContext: SetupBackupContext,
  options: Pick<
    SetupOptions,
    "agentsOverwritePrompt" | "dryRun" | "force" | "verbose"
  >,
): Promise<"updated" | "unchanged" | "skipped"> {
  const destinationExists = existsSync(dstPath);
  let existing = "";
  let changed = true;

  if (destinationExists) {
    existing = await readFile(dstPath, "utf-8");
    changed = existing !== content;
  }

  if (!changed) {
    summary.unchanged += 1;
    return "unchanged";
  }