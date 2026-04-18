tWorkerStateDirs = Object.fromEntries(
    recommendedInspectTargets.map((target) => [
      target,
      snapshot?.teamName ? join(cwd, '.omx', 'state', 'team', snapshot.teamName, 'workers', target) : null,
    ]),
  );
  const recommendedInspectWorkerStatusPaths = Object.fromEntries(
    recommendedInspectTargets.map((target) => [
      target,
      snapshot?.teamName ? join(cwd, '.omx', 'state', 'team', snapshot.teamName, 'workers', target, 'status.json') : null,
    ]),
  );
  const recommendedInspectWorkerHeartbeatPaths = Object.fromEntries(
    recommendedInspectTargets.map((target) => [
      target,
      snapshot?.teamName ? join(cwd, '.omx', 'state', 'team', snapshot.teamName, 'workers', target, 'heartbeat.json') : null,
    ]),
  );