id'],
  'write-task-approval': ['team_name', 'task_id', 'status', 'reviewer', 'decision_reason'],
};

const TEAM_API_OPERATION_OPTIONAL_FIELDS: Partial<Record<TeamApiOperation, string[]>> = {
  'create-task': ['owner', 'blocked_by', 'requires_code_change'],
  'update-task': ['subject', 'description', 'blocked_by', 'requires_code_change'],
  'claim-task': ['expected_version'],
  'cleanup': ['force'],
  'transition-task-status': ['result', 'error'],
  'read-shutdown-ack': ['min_updated_at'],
  'write-worker-identity': [
    'assigned_tasks', 'pid', 'pane_id', 'working_dir',
    'worktree_path', 'worktree_branch', 'worktree_detached', 'team_state_root',
  ],
  'append-event': ['task_id', 'message_id', 'reason', 'state', 'prev_state', 'to_worker', 'worker_count', 'source_type', 'metadata'],