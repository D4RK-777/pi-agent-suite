workers: {
          total: snapshot.workers.length,
          dead: snapshot.deadWorkers.length,
          non_reporting: snapshot.nonReportingWorkers.length,
        },
        tasks: {
          total: snapshot.tasks.total,
          pending: snapshot.tasks.pending,
          blocked: snapshot.tasks.blocked,
          in_progress: snapshot.tasks.in_progress,
          completed: snapshot.tasks.completed,
          failed: snapshot.tasks.failed,
        },
        performance: snapshot.performance ?? null,
        panes: paneStatus,
      }));
      return;
    }
    console.log(`team=${snapshot.teamName} phase=${snapshot.phase}`);
    if (config?.workspace_mode) {
      console.log(`workspace_mode: ${config.workspace_mode}`);
    }