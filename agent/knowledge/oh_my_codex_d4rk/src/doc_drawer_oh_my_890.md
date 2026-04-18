.omx', 'state', 'team', snapshot.teamName, 'workers', target, 'heartbeat.json') : null,
    ]),
  );
  const recommendedInspectWorkerIdentityPaths = Object.fromEntries(
    recommendedInspectTargets.map((target) => [
      target,
      snapshot?.teamName ? join(cwd, '.omx', 'state', 'team', snapshot.teamName, 'workers', target, 'identity.json') : null,
    ]),
  );
  const recommendedInspectWorkerInboxPaths = Object.fromEntries(
    recommendedInspectTargets.map((target) => [
      target,
      snapshot?.teamName ? join(cwd, '.omx', 'state', 'team', snapshot.teamName, 'workers', target, 'inbox.md') : null,
    ]),
  );
  const recommendedInspectWorkerMailboxPaths = Object.fromEntries(
    recommendedInspectTargets.map((target) => [
      target,