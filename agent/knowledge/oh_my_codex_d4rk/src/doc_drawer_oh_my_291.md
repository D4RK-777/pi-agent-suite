isRootTarget = index === 0;
    const relativeDir = relative(cwd, dir).replaceAll("\\", "/") || ".";

    const content =
      isRootTarget && targetDir === cwd
        ? await renderManagedProjectRootAgents(existingContent)
        : await renderManagedDirectoryAgents(
            dir,
            existingContent,
            dirname(dir) === targetDir,
          );

    const rootOverlayRisk =
      rootSessionGuardActive &&
      dir === cwd &&
      existsSync(destinationPath) &&
      existingContent !== content;

    const decision = await syncManagedAgentsFile(
      destinationPath,
      content,
      { dryRun, force, verbose },
      summary,
      backupRoot,
      rootOverlayRisk
        ? "active omx session detected for project root AGENTS.md"
        : undefined,
    );