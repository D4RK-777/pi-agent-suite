=== 0) return;
  throw new Error((result.stderr || '').trim() || `git ${args.join(' ')} failed`);
}

function gitStatusLines(worktreePath: string): string[] {
  const result = spawnSync('git', ['status', '--porcelain', '--untracked-files=all'], {
    cwd: worktreePath,
    encoding: 'utf-8',
      windowsHide: true,
    });
  if (result.status !== 0) {
    throw new Error((result.stderr || '').trim() || `git status failed for ${worktreePath}`);
  }
  return (result.stdout || '')
    .split(/\r?\n/)
    .map((line) => line.trimEnd())
    .filter(Boolean);
}