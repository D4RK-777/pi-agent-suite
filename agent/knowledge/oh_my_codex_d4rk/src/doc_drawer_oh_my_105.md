err,
        parse_error: error instanceof Error ? error.message : String(error),
      };
    }
  }

  if (latestEvaluatorFile) {
    await writeJsonFile(latestEvaluatorFile, record);
  }
  if (ledgerFile) {
    await appendAutoresearchLedgerEntry(ledgerFile, {
      iteration: -1,
      kind: 'iteration',
      decision: record.status === 'error' ? 'error' : record.status === 'pass' ? 'keep' : 'discard',
      decision_reason: 'raw evaluator record',
      candidate_status: 'candidate',
      base_commit: readGitShortHead(worktreePath),
      candidate_commit: null,
      kept_commit: readGitShortHead(worktreePath),
      keep_policy: contract.sandbox.evaluator.keep_policy ?? 'score_improvement',
      evaluator: record,
      created_at: nowIso(),