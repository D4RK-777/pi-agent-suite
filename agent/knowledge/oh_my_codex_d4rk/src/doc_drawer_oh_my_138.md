stop_reason: updates.stopReason,
  }, projectRoot);
  await deactivateAutoresearchRun(manifest);
}

function resetToLastKeptCommit(manifest: AutoresearchRunManifest): void {
  assertResetSafeWorktree(manifest.worktree_path);
  requireGitSuccess(manifest.worktree_path, ['reset', '--hard', manifest.last_kept_commit]);
}

function validateAutoresearchCandidate(
  manifest: Pick<AutoresearchRunManifest, 'last_kept_commit' | 'worktree_path'>,
  candidate: AutoresearchCandidateArtifact,
): { candidate: AutoresearchCandidateArtifact } | { reason: string } {
  const resolvedBaseCommit = tryResolveGitCommit(manifest.worktree_path, candidate.base_commit);
  if (!resolvedBaseCommit) {
    return {
      reason: `candidate base_commit does not resolve in git: ${candidate.base_commit}`,
    };
  }