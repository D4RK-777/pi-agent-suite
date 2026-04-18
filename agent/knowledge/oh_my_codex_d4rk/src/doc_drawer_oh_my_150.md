ion,
    last_kept_commit: manifest.last_kept_commit,
    last_kept_score: manifest.last_kept_score,
    latest_evaluator_status: evaluation.status,
    latest_evaluator_pass: evaluation.pass,
    latest_evaluator_score: evaluation.score,
    latest_evaluator_ran_at: evaluation.ran_at,
  }, projectRoot);
  return decision.decision;
}

export async function finalizeAutoresearchRunState(
  projectRoot: string,
  runId: string,
  updates: { status: AutoresearchRunStatus; stopReason: string },
): Promise<void> {
  const manifest = await loadAutoresearchRunManifest(projectRoot, runId);
  if (manifest.status !== 'running') {
    return;
  }
  await finalizeRun(manifest, projectRoot, updates);
}