meExcludes(worktreePath);
  await ensureAutoresearchWorktreeDependencies(projectRoot, worktreePath);
  assertResetSafeWorktree(worktreePath);

  const runTag = options.runTag || buildAutoresearchRunTag();
  const runId = buildRunId(contract.missionSlug, runTag);
  const baselineCommit = readGitShortHead(worktreePath);
  const branchName = readGit(worktreePath, ['symbolic-ref', '--quiet', '--short', 'HEAD']);
  const runDir = join(projectRoot, '.omx', 'logs', 'autoresearch', runId);
  const stateFile = activeRunStateFile(projectRoot);
  const instructionsFile = join(runDir, 'bootstrap-instructions.md');
  const manifestFile = join(runDir, 'manifest.json');
  const ledgerFile = join(runDir, 'iteration-ledger.json');
  const latestEvaluatorFile = join(runDir, 'latest-evaluator-result.json');