ing[]> {
  const specsDir = join(repoRoot, '.omx', 'specs');
  if (!existsSync(specsDir)) return [];

  const entries = await readdir(specsDir, { withFileTypes: true });
  const resultPaths = entries
    .filter((entry) => entry.isDirectory() && entry.name.startsWith(AUTORESEARCH_ARTIFACT_DIR_PREFIX))
    .map((entry) => join(specsDir, entry.name, 'result.json'))
    .filter((path) => existsSync(path));

  return resultPaths.sort((left, right) => left.localeCompare(right));
}