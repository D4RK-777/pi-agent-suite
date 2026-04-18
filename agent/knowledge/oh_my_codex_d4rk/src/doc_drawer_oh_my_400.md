RunTag();
  const plan = planWorktreeTarget({
    cwd: contract.repoRoot,
    scope: 'autoresearch',
    mode: { enabled: true, detached: false, name: contract.missionSlug },
    worktreeTag: runTag,
  });
  const ensured = ensureWorktree(plan);
  if (!ensured.enabled) {
    throw new Error('autoresearch worktree planning unexpectedly disabled');
  }

  const worktreeContract = await materializeAutoresearchMissionToWorktree(contract, ensured.worktreePath);
  const runtime = await prepareAutoresearchRuntime(worktreeContract, contract.repoRoot, ensured.worktreePath, { runTag });
  await runAutoresearchLoop(codexArgs, runtime, worktreeContract.missionDir);
}