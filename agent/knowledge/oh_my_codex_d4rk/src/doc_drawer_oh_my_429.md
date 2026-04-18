(err) {
      if ((err as NodeJS.ErrnoException).code === 'ENOENT') continue;
      throw err;
    }

    if (now() - entryStat.mtimeMs <= STALE_TMP_MAX_AGE_MS) continue;
    staleDirectories.push(entryPath);
  }
  staleDirectories.sort((left, right) => left.localeCompare(right));

  if (staleDirectories.length === 0) {
    writeLine(dryRun
      ? 'Dry run: no stale OMX /tmp directories found.'
      : 'No stale OMX /tmp directories found.');
    return 0;
  }

  const summaryTarget = formatPlural(
    staleDirectories.length,
    'stale OMX /tmp directory',
    'stale OMX /tmp directories',
  );
  if (dryRun) {
    writeLine(`Dry run: would remove ${summaryTarget}:`);
    for (const directoryPath of staleDirectories) {
      writeLine(`  ${directoryPath}`);
    }
    return 0;
  }