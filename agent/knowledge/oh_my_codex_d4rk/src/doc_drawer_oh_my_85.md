{pattern}\n`;
  await ensureParentDir(excludePath);
  await writeFile(excludePath, next, 'utf-8');
}

async function ensureRuntimeExcludes(worktreePath: string): Promise<void> {
  for (const file of AUTORESEARCH_WORKTREE_EXCLUDES) {
    await writeGitInfoExclude(worktreePath, file);
  }
}

async function ensureAutoresearchWorktreeDependencies(repoRoot: string, worktreePath: string): Promise<void> {
  const sourceNodeModules = join(repoRoot, 'node_modules');
  const targetNodeModules = join(worktreePath, 'node_modules');
  if (!existsSync(sourceNodeModules) || existsSync(targetNodeModules)) {
    return;
  }
  await symlink(sourceNodeModules, targetNodeModules, process.platform === 'win32' ? 'junction' : 'dir');
}