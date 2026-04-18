apshot.teamName) : null,
    ]),
  );
  const recommendedInspectTeamPhasePaths = Object.fromEntries(
    recommendedInspectTargets.map((target) => [
      target,
      snapshot?.teamName ? join(cwd, '.omx', 'state', 'team', snapshot.teamName, 'phase.json') : null,
    ]),
  );
  const recommendedInspectTeamMonitorSnapshotPaths = Object.fromEntries(
    recommendedInspectTargets.map((target) => [
      target,
      snapshot?.teamName ? join(cwd, '.omx', 'state', 'team', snapshot.teamName, 'monitor-snapshot.json') : null,
    ]),
  );
  const recommendedInspectTeamSummarySnapshotPaths = Object.fromEntries(
    recommendedInspectTargets.map((target) => [
      target,
      snapshot?.teamName ? join(cwd, '.omx', 'state', 'team', snapshot.teamName, 'summary-snapshot.json') : null,
    ]),