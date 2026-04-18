a structured stall summary from the existing monitor snapshot, team summary, and recent events.',
};

function sampleValueForTeamApiField(field: string): unknown {
  switch (field) {
    case 'team_name': return 'my-team';
    case 'from_worker': return 'worker-1';
    case 'to_worker': return 'leader-fixed';
    case 'worker': return 'worker-1';
    case 'body': return 'ACK';
    case 'subject': return 'Demo task';
    case 'description': return 'Created through CLI interop';
    case 'task_id': return '1';
    case 'message_id': return 'msg-123';
    case 'from': return 'in_progress';
    case 'to': return 'completed';
    case 'claim_token': return 'claim-token';
    case 'result': return 'Verification:\nPASS - example';
    case 'error': return 'Verification failed';