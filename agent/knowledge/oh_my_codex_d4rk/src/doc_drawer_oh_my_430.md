directoryPath of staleDirectories) {
      writeLine(`  ${directoryPath}`);
    }
    return 0;
  }

  let removedCount = 0;
  for (const directoryPath of staleDirectories) {
    try {
      await removePath(directoryPath);
      removedCount += 1;
      writeLine(`Removed stale /tmp directory: ${directoryPath}`);
    } catch (err) {
      if ((err as NodeJS.ErrnoException).code === 'ENOENT') continue;
      throw err;
    }
  }

  writeLine(
    `Removed ${formatPlural(
      removedCount,
      'stale OMX /tmp directory',
      'stale OMX /tmp directories',
    )}.`,
  );
  return removedCount;
}