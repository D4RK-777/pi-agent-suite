ct_commands: recommendedInspectCommands,
    recommended_inspect_summary: recommendedInspectSummary,
    recommended_inspect_items: recommendedInspectItems,
  };
}

function renderTeamPaneStatus(
  paneStatus: Awaited<ReturnType<typeof readTeamPaneStatus>>,
): void {
  if (paneStatus.leader_pane_id || paneStatus.hud_pane_id) {
    console.log(`panes: leader=${paneStatus.leader_pane_id || '-'} hud=${paneStatus.hud_pane_id || '-'}`);
  }

  const workerPanePairs = Object.entries(paneStatus.worker_panes).map(([workerName, paneId]) => `${workerName}=${paneId}`);
  if (workerPanePairs.length > 0) {
    console.log(`worker_panes: ${workerPanePairs.join(' ')}`);
  }