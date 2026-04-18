if (config?.workspace_mode) {
      console.log(`workspace_mode: ${config.workspace_mode}`);
    }
    console.log(`workers: total=${snapshot.workers.length} dead=${snapshot.deadWorkers.length} non_reporting=${snapshot.nonReportingWorkers.length}`);
    if (snapshot.deadWorkers.length > 0) {
      console.log(`dead_workers: ${snapshot.deadWorkers.join(' ')}`);
    }
    if (snapshot.nonReportingWorkers.length > 0) {
      console.log(`non_reporting_workers: ${snapshot.nonReportingWorkers.join(' ')}`);
    }
    console.log(`tasks: total=${snapshot.tasks.total} pending=${snapshot.tasks.pending} blocked=${snapshot.tasks.blocked} in_progress=${snapshot.tasks.in_progress} completed=${snapshot.tasks.completed} failed=${snapshot.tasks.failed}`);
    if (snapshot.performance) {