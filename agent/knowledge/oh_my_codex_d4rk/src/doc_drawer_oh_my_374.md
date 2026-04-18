a.mtimeMs)[0]?.path;
  if (newestResultPath) {
    return readPersistedResult(newestResultPath);
  }

  const draftPaths = await filterRecentPaths(
    await listAutoresearchDeepInterviewDraftPaths(repoRoot),
    options.newerThanMs,
    options.excludeDraftPaths,
  );
  const draftEntries = await Promise.all(draftPaths.map(async (path) => ({ path, metadata: await stat(path) })));
  const newestDraftPath = draftEntries.sort((left, right) => right.metadata.mtimeMs - left.metadata.mtimeMs)[0]?.path;
  if (!newestDraftPath) {
    return null;
  }

  const draftContent = await readFile(newestDraftPath, 'utf-8');
  return parseDraftArtifactContent(draftContent, repoRoot, newestDraftPath);
}