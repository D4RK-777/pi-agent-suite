kept_commit: manifest.last_kept_commit,
    keep_policy: manifest.keep_policy,
    evaluator: null,
    created_at: nowIso(),
    notes: [...(candidate?.notes ?? []), `validation_error:${reason}`],
    description: candidate?.description || 'candidate validation failed',
  });
  await finalizeRun(manifest, projectRoot, { status: 'failed', stopReason: reason });
  return 'error';
}

async function recordNonEvaluatedCandidateStatus(
  contract: AutoresearchMissionContract,
  manifest: AutoresearchRunManifest,
  projectRoot: string,
  candidate: AutoresearchCandidateArtifact,
): Promise<Extract<AutoresearchDecisionStatus, 'abort' | 'interrupted' | 'noop' | 'error'>> {
  const sharedEntry = {
    description: candidate.description,
    candidateStatus: candidate.status,