nspectTargets.length > 0
    ? sparkshellCommands[recommendedInspectTargets[0]!] ?? null
    : null;
  const recommendedInspectCommands = recommendedInspectTargets
    .map((target) => sparkshellCommands[target])
    .filter((command): command is string => typeof command === 'string' && command.length > 0);
  const recommendedInspectSummary = recommendedInspectTargets.length > 0
    ? [
      `target=${recommendedInspectTargets[0]}`,
      recommendedInspectPanes[recommendedInspectTargets[0]!] ? `pane=${recommendedInspectPanes[recommendedInspectTargets[0]!]}` : '',
      recommendedInspectClis[recommendedInspectTargets[0]!] ? `cli=${recommendedInspectClis[recommendedInspectTargets[0]!]}` : '',