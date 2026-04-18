ame ? join(cwd, '.omx', 'state', 'team', snapshot.teamName, 'summary-snapshot.json') : null,
    ]),
  );
  const recommendedInspectStates = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const worker = snapshot?.workers.find((candidate) => candidate.name === target);
      return [target, worker?.status.state ?? null];
    }),
  );
  const recommendedInspectStateReasons = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const worker = snapshot?.workers.find((candidate) => candidate.name === target);
      return [target, worker?.status.reason ?? null];
    }),
  );
  const recommendedInspectCommand = recommendedInspectTargets.length > 0
    ? sparkshellCommands[recommendedInspectTargets[0]!] ?? null
    : null;