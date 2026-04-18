uth", "status"], { stdio: "ignore",
      windowsHide: true,
    });
  return result.status === 0;
}

async function syncManagedFileFromDisk(
  srcPath: string,
  dstPath: string,
  summary: SetupCategorySummary,
  backupContext: SetupBackupContext,
  options: Pick<SetupOptions, "dryRun" | "verbose">,
  verboseLabel: string,
): Promise<void> {
  const destinationExists = existsSync(dstPath);
  const changed = !destinationExists || (await filesDiffer(srcPath, dstPath));

  if (!changed) {
    summary.unchanged += 1;
    return;
  }

  if (await ensureBackup(dstPath, destinationExists, backupContext, options)) {
    summary.backedUp += 1;
  }

  if (!options.dryRun) {
    await mkdir(dirname(dstPath), { recursive: true });
    await copyFile(srcPath, dstPath);
  }