mand=${recommendedInspectCommand}` : '',
    ]
      .filter(Boolean)
      .join(' ')
      .trim()
    : null;
  const recommendedInspectItems = recommendedInspectTargets
    .map((target) => {
      const command = sparkshellCommands[target];
      const paneId = recommendedInspectPanes[target];
      if (!command || !paneId) return null;
      return {
        target,
        pane_id: paneId,
        worker_cli: recommendedInspectClis[target] ?? null,
        role: recommendedInspectRoles[target] ?? null,
        index: recommendedInspectIndexes[target] ?? null,
        alive: recommendedInspectAlive[target] ?? null,
        turn_count: recommendedInspectTurnCounts[target] ?? null,
        turns_without_progress: recommendedInspectTurnsWithoutProgress[target] ?? null,