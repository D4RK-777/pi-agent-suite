? await options.agentsOverwritePrompt(dstPath)
      : await promptForAgentsOverwrite(dstPath);

    if (!shouldOverwrite) {
      summary.skipped += 1;
      if (options.verbose) {
        const managedLabel = isOmxGeneratedAgentsMd(existing)
          ? "managed"
          : "unmanaged";
        console.log(`  skipped ${managedLabel} AGENTS.md at ${dstPath}`);
      }
      return "skipped";
    }
  }

  if (await ensureBackup(dstPath, destinationExists, backupContext, options)) {
    summary.backedUp += 1;
  }

  if (!options.dryRun) {
    await mkdir(dirname(dstPath), { recursive: true });
    await writeFile(dstPath, content);
  }