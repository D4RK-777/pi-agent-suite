recommended_inspect_team_phase_paths: {},
      recommended_inspect_team_monitor_snapshot_paths: {},
      recommended_inspect_team_summary_snapshot_paths: {},
      recommended_inspect_panes: {},
      recommended_inspect_command: null,
      recommended_inspect_commands: [],
      recommended_inspect_summary: null,
      recommended_inspect_items: [],
    };
  }

  const leaderPaneId = config.leader_pane_id?.trim() || null;
  const hudPaneId = config.hud_pane_id?.trim() || null;

  const workerPanes = Object.fromEntries(
    config.workers
      .map((worker) => {
        const paneId = worker.pane_id?.trim();
        return paneId ? [worker.name, paneId] : null;
      })
      .filter((entry): entry is [string, string] => entry !== null),
  );