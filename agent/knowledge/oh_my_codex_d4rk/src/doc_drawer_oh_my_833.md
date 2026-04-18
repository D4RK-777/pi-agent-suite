ssage_id', 'reason', 'state', 'prev_state', 'to_worker', 'worker_count', 'source_type', 'metadata'],
  'read-events': ['after_event_id', 'wakeable_only', 'type', 'worker', 'task_id'],
  'await-event': ['after_event_id', 'timeout_ms', 'poll_ms', 'wakeable_only', 'type', 'worker', 'task_id'],
  'write-task-approval': ['required'],
};

const TEAM_API_OPERATION_NOTES: Partial<Record<TeamApiOperation, string>> = {
  'update-task': 'Only non-lifecycle task metadata can be updated.',
  'release-task-claim': 'Use this only for rollback/requeue to pending (not for completion).',
  'transition-task-status': 'Lifecycle flow is claim-safe and typically transitions in_progress -> completed|failed.',
  'cleanup': 'Uses the runtime shutdown contract; use orphan-cleanup only for known orphan recovery.',