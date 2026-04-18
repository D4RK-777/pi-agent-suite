g('utf-8').trim()
        : '';
    throw new Error(stderr || `git ${args.join(' ')} failed`);
  }
}

function tryResolveGitCommit(worktreePath: string, ref: string): string | null {
  const result = spawnSync('git', ['rev-parse', '--verify', `${ref}^{commit}`], {
    cwd: worktreePath,
    encoding: 'utf-8',
  });
  if (result.status !== 0) return null;
  const resolved = (result.stdout || '').trim();
  return resolved || null;
}