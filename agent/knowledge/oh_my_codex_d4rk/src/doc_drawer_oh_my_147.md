_file);
  } catch (error) {
    return failAutoresearchIteration(
      manifest,
      projectRoot,
      error instanceof Error ? error.message : String(error),
    );
  }

  const validation = validateAutoresearchCandidate(manifest, candidate);
  if ('reason' in validation) {
    return failAutoresearchIteration(manifest, projectRoot, validation.reason, candidate);
  }
  candidate = validation.candidate;
  manifest.latest_candidate_commit = candidate.candidate_commit;

  if (candidate.status !== 'candidate') {
    return recordNonEvaluatedCandidateStatus(contract, manifest, projectRoot, candidate);
  }