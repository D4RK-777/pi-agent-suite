{
    await mkdir(dirname(dstPath), { recursive: true });
    await writeFile(dstPath, content);
  }

  summary.updated += 1;
  if (options.verbose) {
    console.log(
      `  ${options.dryRun ? "would update" : "updated"} AGENTS ${dstPath}`,
    );
  }
  return "updated";
}

async function installPrompts(
  srcDir: string,
  dstDir: string,
  backupContext: SetupBackupContext,
  options: SetupOptions,
): Promise<SetupCategorySummary> {
  const summary = createEmptyCategorySummary();
  if (!existsSync(srcDir)) return summary;