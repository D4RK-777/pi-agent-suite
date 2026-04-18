rviewResult | null> {
  const slug = options.slug?.trim() ? slugifyMissionName(options.slug) : null;

  if (slug) {
    const resultPath = buildResultPath(repoRoot, slug);
    if (existsSync(resultPath)) {
      const metadata = await stat(resultPath).catch(() => null);
      if (!metadata || options.newerThanMs == null || metadata.mtimeMs >= options.newerThanMs) {
        return readPersistedResult(resultPath);
      }
    }