' ? evaluation.score : manifest.last_kept_score;
  } else {
    resetToLastKeptCommit(manifest);
  }

  await recordAutoresearchIteration(manifest, {
    status: decision.decision,
    decisionReason: decision.decisionReason,
    description: candidate.description,
    candidateStatus: candidate.status,
    baseCommit: candidate.base_commit,
    candidateCommit: candidate.candidate_commit,
    evaluator: evaluation,
    notes: [...candidate.notes, ...decision.notes],
  });
  await writeRunManifest(manifest);
  await writeInstructionsFile(contract, manifest);
  await updateModeState('autoresearch', {
    current_phase: 'running',
    iteration: manifest.iteration,
    last_kept_commit: manifest.last_kept_commit,
    last_kept_score: manifest.last_kept_score,