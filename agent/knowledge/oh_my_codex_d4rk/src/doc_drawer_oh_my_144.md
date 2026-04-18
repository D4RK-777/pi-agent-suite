const sharedEntry = {
    description: candidate.description,
    candidateStatus: candidate.status,
    baseCommit: candidate.base_commit,
    candidateCommit: candidate.candidate_commit,
    notes: candidate.notes,
  };

  if (candidate.status === 'abort') {
    await recordAutoresearchIteration(manifest, {
      status: 'abort',
      decisionReason: 'candidate requested abort',
      ...sharedEntry,
    });
    await finalizeRun(manifest, projectRoot, { status: 'stopped', stopReason: 'candidate abort' });
    return 'abort';
  }