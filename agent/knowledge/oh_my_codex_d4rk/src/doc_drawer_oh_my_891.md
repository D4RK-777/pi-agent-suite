rkerMailboxPaths = Object.fromEntries(
    recommendedInspectTargets.map((target) => [
      target,
      snapshot?.teamName ? join(cwd, '.omx', 'state', 'team', snapshot.teamName, 'mailbox', `${target}.json`) : null,
    ]),
  );
  const recommendedInspectWorkerShutdownRequestPaths = Object.fromEntries(
    recommendedInspectTargets.map((target) => [
      target,
      snapshot?.teamName ? join(cwd, '.omx', 'state', 'team', snapshot.teamName, 'workers', target, 'shutdown-request.json') : null,
    ]),
  );
  const recommendedInspectWorkerShutdownAckPaths = Object.fromEntries(
    recommendedInspectTargets.map((target) => [
      target,
      snapshot?.teamName ? join(cwd, '.omx', 'state', 'team', snapshot.teamName, 'workers', target, 'shutdown-ack.json') : null,
    ]),
  );