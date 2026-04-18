]) => ({ paneId, currentCommand, startCommand }))
    .filter((pane) => pane.paneId.startsWith('%'))
    .filter((pane) => pane.paneId !== currentPaneId)
    .filter((pane) => /\bomx\b.*\bhud\b.*--watch/i.test(pane.startCommand || ''))
    .map((pane) => pane.paneId);
}

function launchAutoresearchInSplitPane(args: {
  currentPaneId: string;
  repoRoot: string;
  missionDir: string;
  codexArgs: string[];
}): boolean {
  if (!checkTmuxAvailable()) return false;

  const paneId = tmuxDisplay(args.currentPaneId, '#{pane_id}');
  if (!paneId) return false;
  const sessionName = tmuxDisplay(paneId, '#S');
  const currentCwd = tmuxDisplay(paneId, '#{pane_current_path}') || args.repoRoot;
  const existingHudPaneIds = listHudWatchPaneIdsInCurrentWindow(paneId);