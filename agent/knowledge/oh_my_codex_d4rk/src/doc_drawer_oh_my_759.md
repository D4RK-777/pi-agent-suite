changed = existing !== content;
  }

  if (!changed) {
    summary.unchanged += 1;
    return;
  }

  if (await ensureBackup(dstPath, destinationExists, backupContext, options)) {
    summary.backedUp += 1;
  }

  if (!options.dryRun) {
    await mkdir(dirname(dstPath), { recursive: true });
    await writeFile(dstPath, content);
  }

  summary.updated += 1;
  if (options.verbose) {
    console.log(
      `  ${options.dryRun ? "would update" : "updated"} ${verboseLabel}`,
    );
  }
}