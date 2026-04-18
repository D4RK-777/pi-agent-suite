symlink(sourceNodeModules, targetNodeModules, process.platform === 'win32' ? 'junction' : 'dir');
}

function readGitShortHead(worktreePath: string): string {
  return readGit(worktreePath, ['rev-parse', '--short=7', 'HEAD']);
}

function readGitFullHead(worktreePath: string): string {
  return readGit(worktreePath, ['rev-parse', 'HEAD']);
}

function requireGitSuccess(worktreePath: string, args: string[]): void {
  const result = spawnSync('git', args, {
    cwd: worktreePath,
    encoding: 'utf-8',
      windowsHide: true,
    });
  if (result.status === 0) return;
  throw new Error((result.stderr || '').trim() || `git ${args.join(' ')} failed`);
}