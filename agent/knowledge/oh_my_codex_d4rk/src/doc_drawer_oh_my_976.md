taffingPlan.rosterSummary}`);
    console.log(`staffing_plan: ${staffingPlan.staffingSummary}`);
  }

  const snapshot = await monitorTeam(runtime.teamName, runtime.cwd);
  if (!snapshot) {
    console.log('warning: team snapshot unavailable immediately after startup');
    return;
  }
  console.log(`tasks: total=${snapshot.tasks.total} pending=${snapshot.tasks.pending} blocked=${snapshot.tasks.blocked} in_progress=${snapshot.tasks.in_progress} completed=${snapshot.tasks.completed} failed=${snapshot.tasks.failed}`);
  if (snapshot.performance) {
    console.log(
      `monitor_perf_ms: total=${snapshot.performance.total_ms} list=${snapshot.performance.list_tasks_ms} workers=${snapshot.performance.worker_scan_ms} mailbox=${snapshot.performance.mailbox_delivery_ms}`
    );
  }