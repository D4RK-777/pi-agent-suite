{
    await mkdir(dirname(dstPath), { recursive: true });
    await copyFile(srcPath, dstPath);
  }

  summary.updated += 1;
  if (options.verbose) {
    console.log(
      `  ${options.dryRun ? "would update" : "updated"} ${verboseLabel}`,
    );
  }
}

async function syncManagedContent(
  content: string,
  dstPath: string,
  summary: SetupCategorySummary,
  backupContext: SetupBackupContext,
  options: Pick<SetupOptions, "dryRun" | "verbose">,
  verboseLabel: string,
): Promise<void> {
  const destinationExists = existsSync(dstPath);
  let changed = true;
  if (destinationExists) {
    const existing = await readFile(dstPath, "utf-8");
    changed = existing !== content;
  }

  if (!changed) {
    summary.unchanged += 1;
    return;
  }