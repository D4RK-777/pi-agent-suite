file,
    ledgerFile: manifest.ledger_file,
    latestEvaluatorFile: manifest.latest_evaluator_file,
    resultsFile: manifest.results_file,
    stateFile: activeRunStateFile(projectRoot),
    candidateFile: manifest.candidate_file,
    repoRoot: manifest.repo_root,
    worktreePath: manifest.worktree_path,
    taskDescription: `autoresearch resume ${runId}`,
  };
}

export function parseAutoresearchCandidateArtifact(raw: string): AutoresearchCandidateArtifact {
  let parsed: unknown;
  try {
    parsed = JSON.parse(raw);
  } catch {
    throw new Error('autoresearch candidate artifact must be valid JSON');
  }
  if (!parsed || typeof parsed !== 'object' || Array.isArray(parsed)) {
    throw new Error('autoresearch candidate artifact must be a JSON object');
  }