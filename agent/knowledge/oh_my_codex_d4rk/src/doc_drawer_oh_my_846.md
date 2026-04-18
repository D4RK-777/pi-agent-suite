w Error(`Unknown argument for "omx team api": ${token}`);
  }
  return { operation, input, json };
}

function slugifyTask(task: string): string {
  return task
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/-+/g, '-')
    .replace(/^-|-$/g, '')
    .slice(0, 30) || 'team-task';
}

function snapshotHasDeadWorkerStall(snapshot: TeamSnapshot): boolean {
  return snapshot.deadWorkers.length > 0 && (snapshot.tasks.pending + snapshot.tasks.in_progress) > 0;
}