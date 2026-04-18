te') {
    return recordNonEvaluatedCandidateStatus(contract, manifest, projectRoot, candidate);
  }

  const evaluation = await runAutoresearchEvaluator(contract, manifest.worktree_path);
  await writeJsonFile(manifest.latest_evaluator_file, evaluation);
  const decision = decideAutoresearchOutcome(manifest, candidate, evaluation);
  if (decision.keep) {
    manifest.last_kept_commit = readGitFullHead(manifest.worktree_path);
    manifest.last_kept_score = typeof evaluation.score === 'number' ? evaluation.score : manifest.last_kept_score;
  } else {
    resetToLastKeptCommit(manifest);
  }