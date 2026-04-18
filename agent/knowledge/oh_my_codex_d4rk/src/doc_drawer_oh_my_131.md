ependencies(projectRoot, manifest.worktree_path);
  assertResetSafeWorktree(manifest.worktree_path);
  await startMode('autoresearch', `autoresearch resume ${runId}`, 1, projectRoot);
  await activateAutoresearchRun(manifest);
  await updateModeState('autoresearch', {
    current_phase: 'running',
    run_id: manifest.run_id,
    run_tag: manifest.run_tag,
    mission_dir: manifest.mission_dir,
    mission_file: manifest.mission_file,
    sandbox_file: manifest.sandbox_file,
    mission_slug: manifest.mission_slug,
    repo_root: manifest.repo_root,
    worktree_path: manifest.worktree_path,
    baseline_commit: manifest.baseline_commit,
    last_kept_commit: manifest.last_kept_commit,
    last_kept_score: manifest.last_kept_score,
    results_file: manifest.results_file,