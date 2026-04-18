) continue;
    const promptName = file.slice(0, -3);
    staleCandidatePromptNames.add(promptName);

    const status = agentStatusByName?.get(promptName);
    if (agentStatusByName && !isInstallableStatus(status)) {
      summary.skipped += 1;
      if (options.verbose) {
        const label = status ?? "unlisted";
        console.log(`  skipped ${file} (status: ${label})`);
      }
      continue;
    }

    const src = join(srcDir, file);
    const dst = join(dstDir, file);
    const srcStat = await stat(src);
    if (!srcStat.isFile()) continue;
    await syncManagedFileFromDisk(
      src,
      dst,
      summary,
      backupContext,
      options,
      `prompt ${file}`,
    );
  }