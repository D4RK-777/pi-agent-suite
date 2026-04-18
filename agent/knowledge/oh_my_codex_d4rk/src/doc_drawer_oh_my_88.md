(result.stdout || '')
    .split(/\r?\n/)
    .map((line) => line.trimEnd())
    .filter(Boolean);
}

function isAllowedRuntimeDirtyLine(line: string): boolean {
  const trimmed = line.trim();
  if (trimmed.length < 4) return false;
  const path = trimmed.slice(3).trim();
  return trimmed.startsWith('?? ') && AUTORESEARCH_WORKTREE_EXCLUDES.some((exclude) => exclude.endsWith('/')
    ? path.startsWith(exclude) || path === exclude.slice(0, -1)
    : path === exclude);
}