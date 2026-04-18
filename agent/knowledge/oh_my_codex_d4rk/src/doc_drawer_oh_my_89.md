With('/')
    ? path.startsWith(exclude) || path === exclude.slice(0, -1)
    : path === exclude);
}

export function assertResetSafeWorktree(worktreePath: string): void {
  const lines = gitStatusLines(worktreePath);
  const blocking = lines.filter((line) => !isAllowedRuntimeDirtyLine(line));
  if (blocking.length === 0) return;
  throw new Error(`autoresearch_reset_requires_clean_worktree:${worktreePath}:${blocking.join(' | ')}`);
}

async function ensureParentDir(filePath: string): Promise<void> {
  await mkdir(dirname(filePath), { recursive: true });
}

async function writeJsonFile(filePath: string, value: unknown): Promise<void> {
  await ensureParentDir(filePath);
  await writeFile(filePath, `${JSON.stringify(value, null, 2)}\n`, 'utf-8');
}