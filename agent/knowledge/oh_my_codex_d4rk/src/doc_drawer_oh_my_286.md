summary.skipped += 1;
    return { action: "skipped", reason: skipReason, backedUp: false };
  }

  if (!destinationExists) {
    if (!options.dryRun) {
      await mkdir(dirname(destinationPath), { recursive: true });
      await writeFile(destinationPath, content);
    }
    summary.updated += 1;
    return { action: "updated", backedUp: false };
  }

  if (existingContent === content) {
    summary.unchanged += 1;
    return { action: "unchanged", backedUp: false };
  }

  if (!isManagedAgentsInitFile(existingContent ?? "") && !options.force) {
    summary.skipped += 1;
    return {
      action: "skipped",
      reason: "existing unmanaged AGENTS.md (re-run with --force to adopt it)",
      backedUp: false,
    };
  }