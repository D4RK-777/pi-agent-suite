:"worker-1","expected_version":1}' --json
`;

const HELP_TOKENS = new Set(['--help', '-h', 'help']);

const TEAM_API_OPERATION_REQUIRED_FIELDS: Record<TeamApiOperation, string[]> = {
  'send-message': ['team_name', 'from_worker', 'to_worker', 'body'],
  'broadcast': ['team_name', 'from_worker', 'body'],
  'mailbox-list': ['team_name', 'worker'],
  'mailbox-mark-delivered': ['team_name', 'worker', 'message_id'],
  'mailbox-mark-notified': ['team_name', 'worker', 'message_id'],
  'create-task': ['team_name', 'subject', 'description'],
  'read-task': ['team_name', 'task_id'],
  'list-tasks': ['team_name'],
  'update-task': ['team_name', 'task_id'],
  'claim-task': ['team_name', 'task_id', 'worker'],
  'transition-task-status': ['team_name', 'task_id', 'from', 'to', 'claim_token'],