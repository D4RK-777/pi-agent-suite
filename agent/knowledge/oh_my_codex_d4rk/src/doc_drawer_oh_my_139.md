reason: `candidate base_commit does not resolve in git: ${candidate.base_commit}`,
    };
  }
  if (resolvedBaseCommit !== manifest.last_kept_commit) {
    return {
      reason: `candidate base_commit ${resolvedBaseCommit} does not match last kept commit ${manifest.last_kept_commit}`,
    };
  }

  if (candidate.status !== 'candidate') {
    return {
      candidate: {
        ...candidate,
        base_commit: resolvedBaseCommit,
      },
    };
  }