string) => rm(path, { recursive: true, force: true }));
  const now = dependencies.now ?? Date.now;
  const writeLine = dependencies.writeLine ?? ((line: string) => console.log(line));

  const staleDirectories: string[] = [];
  for (const entry of await listTmpEntries(tmpRoot)) {
    if (!entry.isDirectory() || !OMX_TMP_DIRECTORY_PATTERN.test(entry.name)) continue;

    const entryPath = join(tmpRoot, entry.name);
    let entryStat: { mtimeMs: number };
    try {
      entryStat = await statPath(entryPath);
    } catch (err) {
      if ((err as NodeJS.ErrnoException).code === 'ENOENT') continue;
      throw err;
    }