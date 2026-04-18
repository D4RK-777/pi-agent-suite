est_file: manifestFile,
    ledger_file: ledgerFile,
    latest_evaluator_file: latestEvaluatorFile,
    candidate_file: candidateFile,
    evaluator: contract.sandbox.evaluator,
    keep_policy: keepPolicy,
    status: 'running',
    stop_reason: null,
    iteration: 0,
    created_at: nowIso(),
    updated_at: nowIso(),
    completed_at: null,
  };

  await writeInstructionsFile(contract, manifest);
  await writeRunManifest(manifest);
  await writeJsonFile(ledgerFile, {
    schema_version: 1,
    run_id: runId,
    created_at: nowIso(),
    updated_at: nowIso(),
    entries: [],
  });
  await writeJsonFile(latestEvaluatorFile, {
    run_id: runId,
    status: 'not-yet-run',
    updated_at: nowIso(),
  });