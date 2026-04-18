Id !== currentPaneId)
    .filter((pane) => isHudWatchPane(pane))
    .map((pane) => pane.paneId);
}

export function buildHudPaneCleanupTargets(
  existingPaneIds: string[],
  createdPaneId: string | null,
  leaderPaneId?: string,
): string[] {
  const targets = new Set<string>(
    existingPaneIds.filter((id) => id.startsWith("%")),
  );
  if (createdPaneId && createdPaneId.startsWith("%")) {
    targets.add(createdPaneId);
  }
  // Guard: never kill the leader's own pane under any circumstances.
  if (leaderPaneId && leaderPaneId.startsWith("%")) {
    targets.delete(leaderPaneId);
  }
  return [...targets];
}