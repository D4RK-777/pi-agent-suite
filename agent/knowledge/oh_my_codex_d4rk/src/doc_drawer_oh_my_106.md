x.evaluator.keep_policy ?? 'score_improvement',
      evaluator: record,
      created_at: nowIso(),
      notes: ['raw evaluator invocation'],
      description: 'raw evaluator record',
    });
  }
  return record;
}

function comparableScore(previousScore: number | null, nextScore: number | undefined): boolean {
  return typeof previousScore === 'number' && typeof nextScore === 'number';
}

export function decideAutoresearchOutcome(
  manifest: Pick<AutoresearchRunManifest, 'keep_policy' | 'last_kept_score'>,
  candidate: AutoresearchCandidateArtifact,
  evaluation: AutoresearchEvaluationRecord | null,
): AutoresearchDecision {
  if (candidate.status === 'abort') {
    return {
      decision: 'abort',
      decisionReason: 'candidate requested abort',
      keep: false,