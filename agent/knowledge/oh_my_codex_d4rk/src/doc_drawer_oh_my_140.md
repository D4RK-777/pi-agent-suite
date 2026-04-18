candidate: {
        ...candidate,
        base_commit: resolvedBaseCommit,
      },
    };
  }

  if (!candidate.candidate_commit) {
    return {
      reason: 'candidate status requires a non-null candidate_commit',
    };
  }
  const resolvedCandidateCommit = tryResolveGitCommit(manifest.worktree_path, candidate.candidate_commit);
  if (!resolvedCandidateCommit) {
    return {
      reason: `candidate_commit does not resolve in git: ${candidate.candidate_commit}`,
    };
  }
  const headCommit = readGitFullHead(manifest.worktree_path);
  if (resolvedCandidateCommit !== headCommit) {
    return {
      reason: `candidate_commit ${resolvedCandidateCommit} does not match worktree HEAD ${headCommit}`,
    };
  }