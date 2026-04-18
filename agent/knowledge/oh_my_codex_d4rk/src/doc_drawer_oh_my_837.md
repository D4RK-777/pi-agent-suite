se 'result': return 'Verification:\nPASS - example';
    case 'error': return 'Verification failed';
    case 'expected_version': return 1;
    case 'pid': return 12345;
    case 'turn_count': return 12;
    case 'alive': return true;
    case 'content': return '# Inbox update\nProceed with task 2.';
    case 'index': return 1;
    case 'role': return 'executor';
    case 'assigned_tasks': return ['1', '2'];
    case 'type': return 'task_completed';
    case 'metadata':
      return {
        summary: 'worker diff report',
        worktree_path: '/tmp/team/worktrees/worker-1',
        diff_path: '/tmp/team/worktrees/worker-1/.omx/diff.md',
        full_diff_available: true,
      };
    case 'requested_by': return 'leader-fixed';
    case 'after_event_id': return 'evt-123';