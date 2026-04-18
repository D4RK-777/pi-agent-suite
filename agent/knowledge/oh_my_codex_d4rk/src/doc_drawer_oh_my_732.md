: "";

  if (hasGitignoreEntry(existing, PROJECT_OMX_GITIGNORE_ENTRY)) {
    return "unchanged";
  }

  const nextContent = destinationExists
    ? `${existing}${existing.endsWith("\n") || existing.length === 0 ? "" : "\n"}${PROJECT_OMX_GITIGNORE_ENTRY}\n`
    : `${PROJECT_OMX_GITIGNORE_ENTRY}\n`;

  if (
    await ensureBackup(gitignorePath, destinationExists, backupContext, options)
  ) {
    // backup created when refreshing a pre-existing .gitignore
  }

  if (!options.dryRun) {
    await writeFile(gitignorePath, nextContent);
  }

  if (options.verbose) {
    console.log(
      `  ${options.dryRun ? "would update" : destinationExists ? "updated" : "created"} .gitignore (${PROJECT_OMX_GITIGNORE_ENTRY})`,
    );
  }

  return destinationExists ? "updated" : "created";
}