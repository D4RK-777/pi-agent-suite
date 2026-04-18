ntry.name))
      .sort((a, b) => a.localeCompare(b));
    return [targetDir, ...childDirs];
  });
}

async function syncManagedAgentsFile(
  destinationPath: string,
  content: string,
  options: Required<Pick<AgentsInitOptions, "dryRun" | "force" | "verbose">>,
  summary: AgentsInitSummary,
  backupRoot: string,
  skipReason?: string,
): Promise<ManagedFileDecision> {
  const destinationExists = existsSync(destinationPath);
  const existingContent = destinationExists
    ? await readFile(destinationPath, "utf-8")
    : undefined;

  if (skipReason) {
    summary.skipped += 1;
    return { action: "skipped", reason: skipReason, backedUp: false };
  }