us !== 0) return null;
  const resolved = (result.stdout || '').trim();
  return resolved || null;
}

async function writeGitInfoExclude(worktreePath: string, pattern: string): Promise<void> {
  const excludePath = readGit(worktreePath, ['rev-parse', '--git-path', 'info/exclude']);
  const existing = existsSync(excludePath)
    ? await readFile(excludePath, 'utf-8')
    : '';
  const lines = new Set(existing.split(/\r?\n/).filter(Boolean));
  if (lines.has(pattern)) return;
  const next = `${existing}${existing.endsWith('\n') || existing.length === 0 ? '' : '\n'}${pattern}\n`;
  await ensureParentDir(excludePath);
  await writeFile(excludePath, next, 'utf-8');
}