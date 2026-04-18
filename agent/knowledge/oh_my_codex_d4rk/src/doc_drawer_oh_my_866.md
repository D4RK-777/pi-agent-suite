Lines}`,
      ] as const),
    ].filter((entry): entry is [string, string] => entry !== null),
  );

  const recommendedInspectTargets = [
    ...(snapshot?.deadWorkers ?? []),
    ...(snapshot?.nonReportingWorkers ?? []),
  ].filter((workerName, index, values) => (
    Object.hasOwn(workerPanes, workerName) && values.indexOf(workerName) === index
  ));
  const recommendedInspectReasons = Object.fromEntries(
    recommendedInspectTargets.map((target) => [
      target,
      (snapshot?.deadWorkers ?? []).includes(target) ? 'dead_worker' : 'non_reporting_worker',
    ]),
  );
  const recommendedInspectClis = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const worker = config.workers.find((candidate) => candidate.name === target);