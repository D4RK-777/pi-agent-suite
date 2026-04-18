`candidate_commit ${resolvedCandidateCommit} does not match worktree HEAD ${headCommit}`,
    };
  }

  return {
    candidate: {
      ...candidate,
      base_commit: resolvedBaseCommit,
      candidate_commit: resolvedCandidateCommit,
    },
  };
}

async function failAutoresearchIteration(
  manifest: AutoresearchRunManifest,
  projectRoot: string,
  reason: string,
  candidate?: AutoresearchCandidateArtifact,
): Promise<'error'> {
  const headCommit = (() => {
    try {
      return readGitShortHead(manifest.worktree_path);
    } catch {
      return manifest.baseline_commit;
    }
  })();