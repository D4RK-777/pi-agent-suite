ap((target) => {
      const worker = config.workers.find((candidate) => candidate.name === target);
      return [target, worker?.worker_cli ?? null];
    }),
  );
  const recommendedInspectRoles = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const worker = config.workers.find((candidate) => candidate.name === target);
      return [target, worker?.role ?? null];
    }),
  );
  const recommendedInspectIndexes = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const worker = config.workers.find((candidate) => candidate.name === target);
      return [target, worker?.index ?? null];
    }),
  );
  const recommendedInspectAlive = Object.fromEntries(
    recommendedInspectTargets.map((target) => {