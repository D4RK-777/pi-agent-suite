command,
      };
    })
    .filter((item): item is Exclude<typeof item, null> => item !== null);

  return {
    leader_pane_id: leaderPaneId,
    hud_pane_id: hudPaneId,
    worker_panes: workerPanes,
    sparkshell_hint: Object.keys(workerPanes).length > 0
      ? 'omx sparkshell --tmux-pane <pane-id> --tail-lines 400'
      : null,
    sparkshell_commands: sparkshellCommands,
    recommended_inspect_targets: recommendedInspectTargets,
    recommended_inspect_reasons: recommendedInspectReasons,
    recommended_inspect_clis: recommendedInspectClis,
    recommended_inspect_roles: recommendedInspectRoles,
    recommended_inspect_indexes: recommendedInspectIndexes,
    recommended_inspect_alive: recommendedInspectAlive,
    recommended_inspect_turn_counts: recommendedInspectTurnCounts,