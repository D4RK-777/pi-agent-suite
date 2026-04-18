ntry.kind !== 'iteration' || entry.decision !== 'noop') break;
    count += 1;
  }
  return count;
}

function formatAutoresearchInstructionSummary(
  entries: AutoresearchLedgerEntry[],
  maxEntries = 3,
): AutoresearchInstructionLedgerSummary[] {
  return entries
    .slice(-maxEntries)
    .map((entry) => ({
      iteration: entry.iteration,
      decision: entry.decision,
      reason: trimContent(entry.decision_reason, 160),
      kept_commit: entry.kept_commit,
      candidate_commit: entry.candidate_commit,
      evaluator_status: entry.evaluator?.status ?? null,
      evaluator_score: typeof entry.evaluator?.score === 'number' ? entry.evaluator.score : null,
      description: trimContent(entry.description, 120),
    }));
}