ateFile,
    candidateFile,
    repoRoot: projectRoot,
    worktreePath,
    taskDescription,
  };
}

export async function resumeAutoresearchRuntime(projectRoot: string, runId: string): Promise<PreparedAutoresearchRuntime> {
  await assertAutoresearchLockAvailable(projectRoot);
  const manifest = await loadAutoresearchRunManifest(projectRoot, runId);
  if (manifest.status !== 'running') {
    throw new Error(`autoresearch_resume_terminal_run:${runId}`);
  }
  if (!existsSync(manifest.worktree_path)) {
    throw new Error(`autoresearch_resume_missing_worktree:${manifest.worktree_path}`);
  }
  await ensureRuntimeExcludes(manifest.worktree_path);
  await ensureAutoresearchWorktreeDependencies(projectRoot, manifest.worktree_path);
  assertResetSafeWorktree(manifest.worktree_path);