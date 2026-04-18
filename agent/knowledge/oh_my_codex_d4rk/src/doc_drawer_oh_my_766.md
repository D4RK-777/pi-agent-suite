rc,
      dst,
      summary,
      backupContext,
      options,
      `prompt ${file}`,
    );
  }

  if (options.force && manifest && existsSync(dstDir)) {
    const installedFiles = await readdir(dstDir);
    for (const file of installedFiles) {
      if (!file.endsWith(".md")) continue;
      const promptName = file.slice(0, -3);
      const status = agentStatusByName?.get(promptName);
      if (isInstallableStatus(status)) continue;
      if (!staleCandidatePromptNames.has(promptName) && status === undefined)
        continue;

      const stalePromptPath = join(dstDir, file);
      if (!existsSync(stalePromptPath)) continue;