down_ack_path: string | null;
    team_dir_path: string | null;
    team_config_path: string | null;
    team_manifest_path: string | null;
    team_events_path: string | null;
    team_dispatch_path: string | null;
    team_phase_path: string | null;
    team_monitor_snapshot_path: string | null;
    team_summary_snapshot_path: string | null;
    command: string;
  }>;
}> {
  if (!config) {
    return {
      leader_pane_id: null,
      hud_pane_id: null,
      worker_panes: {},
      sparkshell_hint: null,
      sparkshell_commands: {},
      recommended_inspect_targets: [],
      recommended_inspect_reasons: {},
      recommended_inspect_clis: {},
      recommended_inspect_roles: {},
      recommended_inspect_indexes: {},
      recommended_inspect_alive: {},