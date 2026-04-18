autoresearch v1.';

function contractError(message: string): Error {
  return new Error(message);
}

function readGit(repoPath: string, args: string[]): string {
  try {
    return execFileSync('git', args, {
      cwd: repoPath,
      encoding: 'utf-8',
      stdio: ['ignore', 'pipe', 'pipe'],
      windowsHide: true,
    }).trim();
  } catch (error) {
    const err = error as NodeJS.ErrnoException & { stderr?: string | Buffer };
    const stderr = typeof err.stderr === 'string'
      ? err.stderr.trim()
      : err.stderr instanceof Buffer
        ? err.stderr.toString('utf-8').trim()
        : '';
    throw contractError(stderr || MISSION_DIR_GIT_ERROR);
  }
}