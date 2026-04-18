leted=${snapshot.tasks.completed} failed=${snapshot.tasks.failed}`);
    if (snapshot.performance) {
      console.log(
        `monitor_perf_ms: total=${snapshot.performance.total_ms} list=${snapshot.performance.list_tasks_ms} workers=${snapshot.performance.worker_scan_ms} mailbox=${snapshot.performance.mailbox_delivery_ms}`
      );
    }
    renderTeamPaneStatus(paneStatus);
    return;
  }

  if (subcommand === 'await') {
    const name = teamArgs[1];
    if (!name) throw new Error('Usage: omx team await <team-name> [--timeout-ms <ms>] [--after-event-id <id>] [--json]');
    const wantsJson = teamArgs.includes('--json');
    const timeoutIdx = teamArgs.indexOf('--timeout-ms');
    const afterIdx = teamArgs.indexOf('--after-event-id');