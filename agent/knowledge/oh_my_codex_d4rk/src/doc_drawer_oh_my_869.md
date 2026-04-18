andidate.name === target);
      return [target, worker?.turnsWithoutProgress ?? null];
    }),
  );
  const recommendedInspectLastTurnAt = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const worker = snapshot?.workers.find((candidate) => candidate.name === target);
      return [target, worker?.heartbeat?.last_turn_at ?? null];
    }),
  );
  const recommendedInspectStatusUpdatedAt = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const worker = snapshot?.workers.find((candidate) => candidate.name === target);
      return [target, worker?.status.updated_at ?? null];
    }),
  );
  const recommendedInspectPids = Object.fromEntries(
    recommendedInspectTargets.map((target) => {