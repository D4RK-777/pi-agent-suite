tTeamEventsPaths = Object.fromEntries(
    recommendedInspectTargets.map((target) => [
      target,
      snapshot?.teamName ? join(cwd, '.omx', 'state', 'team', snapshot.teamName, 'events', 'events.ndjson') : null,
    ]),
  );
  const recommendedInspectTeamDispatchPaths = Object.fromEntries(
    recommendedInspectTargets.map((target) => [
      target,
      snapshot?.teamName ? join(cwd, '.omx', 'state', 'team', snapshot.teamName, 'dispatch', 'requests.json') : null,
    ]),
  );
  const recommendedInspectTeamDirPaths = Object.fromEntries(
    recommendedInspectTargets.map((target) => [
      target,
      snapshot?.teamName ? join(cwd, '.omx', 'state', 'team', snapshot.teamName) : null,
    ]),
  );
  const recommendedInspectTeamPhasePaths = Object.fromEntries(