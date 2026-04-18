ath) => existsSync(path));

  return resultPaths.sort((left, right) => left.localeCompare(right));
}

async function filterRecentPaths(paths: readonly string[], newerThanMs?: number, excludePaths?: ReadonlySet<string>): Promise<string[]> {
  const filtered: string[] = [];
  for (const path of paths) {
    if (excludePaths?.has(path)) {
      continue;
    }
    if (typeof newerThanMs === 'number') {
      const metadata = await stat(path).catch(() => null);
      if (!metadata || metadata.mtimeMs < newerThanMs) {
        continue;
      }
    }
    filtered.push(path);
  }
  return filtered;
}