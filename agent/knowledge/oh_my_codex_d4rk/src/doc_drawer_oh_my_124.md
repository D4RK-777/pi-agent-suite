iteration-ledger.json');
  const latestEvaluatorFile = join(runDir, 'latest-evaluator-result.json');
  const candidateFile = join(runDir, 'candidate.json');
  const resultsFile = join(worktreePath, 'results.tsv');
  const taskDescription = `autoresearch ${contract.missionRelativeDir} (${runId})`;
  const keepPolicy = contract.sandbox.evaluator.keep_policy ?? 'score_improvement';

  await mkdir(runDir, { recursive: true });
  await initializeAutoresearchResultsFile(resultsFile);
  await writeJsonFile(candidateFile, {
    status: 'noop',
    candidate_commit: null,
    base_commit: baselineCommit,
    description: 'not-yet-written',
    notes: ['candidate artifact will be overwritten by the launched session'],
    created_at: nowIso(),
  } satisfies AutoresearchCandidateArtifact);