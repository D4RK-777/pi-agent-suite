mise<boolean> {
  const omxDir = join(projectRoot, ".omx");
  if (!existsSync(omxDir)) return false;

  if (!options.dryRun) {
    await rm(omxDir, { recursive: true, force: true });
  }
  if (options.verbose)
    console.log(`  ${options.dryRun ? "Would remove" : "Removed"} ${omxDir}`);
  return true;
}

function printSummary(summary: UninstallSummary, dryRun: boolean): void {
  const prefix = dryRun ? "[dry-run] Would remove" : "Removed";

  console.log("\nUninstall summary:");