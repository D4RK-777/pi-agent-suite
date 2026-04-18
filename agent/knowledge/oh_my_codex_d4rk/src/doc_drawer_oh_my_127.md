latestEvaluatorFile, {
    run_id: runId,
    status: 'not-yet-run',
    updated_at: nowIso(),
  });

  const existingModeState = await readModeState('autoresearch', projectRoot);
  if (existingModeState?.active) {
    throw new Error(`autoresearch_active_mode_exists:${String(existingModeState.run_id || 'unknown')}`);
  }
  await startMode('autoresearch', taskDescription, 1, projectRoot);
  await activateAutoresearchRun(manifest);
  await updateModeState('autoresearch', {
    current_phase: 'evaluating-baseline',
    run_id: runId,
    run_tag: runTag,
    mission_dir: contract.missionDir,
    mission_file: contract.missionFile,
    sandbox_file: contract.sandboxFile,
    mission_slug: contract.missionSlug,
    repo_root: projectRoot,
    worktree_path: worktreePath,