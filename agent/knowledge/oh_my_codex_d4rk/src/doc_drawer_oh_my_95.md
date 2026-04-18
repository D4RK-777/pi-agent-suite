ow.pass)}\t${resultScoreValue(row.score)}\t${row.status}\t${row.description}\n`,
    'utf-8',
  );
}

async function recordAutoresearchIteration(
  manifest: AutoresearchRunManifest,
  entry: {
    status: AutoresearchDecisionStatus;
    decisionReason: string;
    description: string;
    candidateStatus: AutoresearchCandidateArtifact['status'];
    baseCommit: string;
    candidateCommit: string | null;
    keptCommit?: string;
    evaluator?: AutoresearchEvaluationRecord | null;
    notes: string[];
    createdAt?: string;
  },
): Promise<void> {
  const commit = readGitShortHead(manifest.worktree_path);
  await appendAutoresearchResultsRow(manifest.results_file, {
    iteration: manifest.iteration,
    commit,
    pass: entry.evaluator?.pass,
    score: entry.evaluator?.score,