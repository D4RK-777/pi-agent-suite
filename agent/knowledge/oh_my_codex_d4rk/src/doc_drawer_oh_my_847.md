turn snapshot.deadWorkers.length > 0 && (snapshot.tasks.pending + snapshot.tasks.in_progress) > 0;
}

function buildDeadWorkerAwaitEvent(teamName: string, snapshot: TeamSnapshot): TeamEvent | null {
  const deadWorker = snapshot.workers.find((worker) => worker.alive === false);
  if (!deadWorker) return null;
  return {
    event_id: `snapshot-${Date.now()}`,
    team: sanitizeTeamName(teamName),
    type: 'worker_stopped',
    worker: deadWorker.name,
    task_id: deadWorker.status.current_task_id,
    message_id: null,
    reason: deadWorker.status.reason ?? 'dead_worker_detected_during_await',
    created_at: deadWorker.status.updated_at || new Date().toISOString(),
    source_type: 'await_snapshot',
  };
}