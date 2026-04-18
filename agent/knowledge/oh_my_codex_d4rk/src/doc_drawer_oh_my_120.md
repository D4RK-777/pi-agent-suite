.results_file,
      candidateFile: manifest.candidate_file,
      keepPolicy: manifest.keep_policy,
      previousIterationOutcome: instructionContext.previousIterationOutcome,
      recentLedgerSummary: instructionContext.recentLedgerSummary,
    })}\n`,
    'utf-8',
  );
}

async function seedBaseline(
  contract: AutoresearchMissionContract,
  manifest: AutoresearchRunManifest,
): Promise<AutoresearchEvaluationRecord> {
  const evaluation = await runAutoresearchEvaluator(contract, manifest.worktree_path);
  await writeJsonFile(manifest.latest_evaluator_file, evaluation);
  await appendAutoresearchResultsRow(manifest.results_file, {
    iteration: 0,
    commit: readGitShortHead(manifest.worktree_path),
    pass: evaluation.pass,
    score: evaluation.score,