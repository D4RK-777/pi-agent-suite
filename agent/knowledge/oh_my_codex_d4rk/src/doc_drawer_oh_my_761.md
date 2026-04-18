existing !== content;
  }

  if (!changed) {
    summary.unchanged += 1;
    return "unchanged";
  }

  if (destinationExists && !options.force) {
    if (options.dryRun) {
      summary.skipped += 1;
      if (options.verbose) {
        console.log(`  would prompt before overwriting ${dstPath}`);
      }
      return "skipped";
    }

    const shouldOverwrite = options.agentsOverwritePrompt
      ? await options.agentsOverwritePrompt(dstPath)
      : await promptForAgentsOverwrite(dstPath);