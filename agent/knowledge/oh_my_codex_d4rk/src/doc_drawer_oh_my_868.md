const recommendedInspectAlive = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const worker = snapshot?.workers.find((candidate) => candidate.name === target);
      return [target, worker?.alive ?? null];
    }),
  );
  const recommendedInspectTurnCounts = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const worker = snapshot?.workers.find((candidate) => candidate.name === target);
      return [target, worker?.heartbeat?.turn_count ?? null];
    }),
  );
  const recommendedInspectTurnsWithoutProgress = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const worker = snapshot?.workers.find((candidate) => candidate.name === target);
      return [target, worker?.turnsWithoutProgress ?? null];
    }),
  );