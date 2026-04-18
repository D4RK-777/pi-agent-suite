x', 'state', 'team', snapshot.teamName, 'workers', target, 'shutdown-ack.json') : null,
    ]),
  );
  const recommendedInspectTeamConfigPaths = Object.fromEntries(
    recommendedInspectTargets.map((target) => [
      target,
      snapshot?.teamName ? join(cwd, '.omx', 'state', 'team', snapshot.teamName, 'config.json') : null,
    ]),
  );
  const recommendedInspectTeamManifestPaths = Object.fromEntries(
    recommendedInspectTargets.map((target) => [
      target,
      snapshot?.teamName ? join(cwd, '.omx', 'state', 'team', snapshot.teamName, 'manifest.v2.json') : null,
    ]),
  );
  const recommendedInspectTeamEventsPaths = Object.fromEntries(
    recommendedInspectTargets.map((target) => [
      target,