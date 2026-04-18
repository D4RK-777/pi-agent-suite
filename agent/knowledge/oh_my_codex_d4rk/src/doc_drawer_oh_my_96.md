manifest.iteration,
    commit,
    pass: entry.evaluator?.pass,
    score: entry.evaluator?.score,
    status: entry.status,
    description: entry.description,
  });
  await appendAutoresearchLedgerEntry(manifest.ledger_file, {
    iteration: manifest.iteration,
    kind: 'iteration',
    decision: entry.status,
    decision_reason: entry.decisionReason,
    candidate_status: entry.candidateStatus,
    base_commit: entry.baseCommit,
    candidate_commit: entry.candidateCommit,
    kept_commit: entry.keptCommit ?? manifest.last_kept_commit,
    keep_policy: manifest.keep_policy,
    evaluator: entry.evaluator ?? null,
    created_at: entry.createdAt ?? nowIso(),
    notes: entry.notes,
    description: entry.description,
  });
}