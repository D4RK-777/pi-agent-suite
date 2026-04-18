};
    case 'requested_by': return 'leader-fixed';
    case 'after_event_id': return 'evt-123';
    case 'wakeable_only': return true;
    case 'timeout_ms': return 500;
    case 'poll_ms': return 100;
    case 'min_updated_at': return '2026-03-04T00:00:00.000Z';
    case 'snapshot':
      return {
        taskStatusById: { '1': 'completed' },
        workerAliveByName: { 'worker-1': true },
        workerStateByName: { 'worker-1': 'idle' },
        workerTurnCountByName: { 'worker-1': 12 },
        workerTaskIdByName: { 'worker-1': '1' },
        mailboxNotifiedByMessageId: {},
        completedEventTaskIds: { '1': true },
      };
    case 'status': return 'approved';
    case 'reviewer': return 'leader-fixed';
    case 'decision_reason': return 'approved in demo';