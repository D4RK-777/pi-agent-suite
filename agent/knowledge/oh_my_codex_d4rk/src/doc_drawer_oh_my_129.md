date_path: candidateFile,
    keep_policy: keepPolicy,
    state_file: stateFile,
  }, projectRoot);

  const evaluation = await seedBaseline(contract, manifest);
  await updateModeState('autoresearch', {
    current_phase: 'running',
    latest_evaluator_status: evaluation.status,
    latest_evaluator_pass: evaluation.pass,
    latest_evaluator_score: evaluation.score,
    latest_evaluator_ran_at: evaluation.ran_at,
    last_kept_commit: manifest.last_kept_commit,
    last_kept_score: manifest.last_kept_score,
  }, projectRoot);

  return {
    runId,
    runTag,
    runDir,
    instructionsFile,
    manifestFile,
    ledgerFile,
    latestEvaluatorFile,
    resultsFile,
    stateFile,
    candidateFile,
    repoRoot: projectRoot,
    worktreePath,
    taskDescription,
  };
}