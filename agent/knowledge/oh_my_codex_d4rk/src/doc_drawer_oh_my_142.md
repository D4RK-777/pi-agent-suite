hortHead(manifest.worktree_path);
    } catch {
      return manifest.baseline_commit;
    }
  })();

  await appendAutoresearchResultsRow(manifest.results_file, {
    iteration: manifest.iteration,
    commit: headCommit,
    status: 'error',
    description: candidate?.description || 'candidate validation failed',
  });
  await appendAutoresearchLedgerEntry(manifest.ledger_file, {
    iteration: manifest.iteration,
    kind: 'iteration',
    decision: 'error',
    decision_reason: reason,
    candidate_status: candidate?.status ?? 'candidate',
    base_commit: candidate?.base_commit ?? manifest.last_kept_commit,
    candidate_commit: candidate?.candidate_commit ?? null,
    kept_commit: manifest.last_kept_commit,
    keep_policy: manifest.keep_policy,
    evaluator: null,