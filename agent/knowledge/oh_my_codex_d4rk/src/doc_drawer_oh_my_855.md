cord<string, string | null>;
  recommended_inspect_team_events_paths: Record<string, string | null>;
  recommended_inspect_team_dispatch_paths: Record<string, string | null>;
  recommended_inspect_team_dir_paths: Record<string, string | null>;
  recommended_inspect_team_phase_paths: Record<string, string | null>;
  recommended_inspect_team_monitor_snapshot_paths: Record<string, string | null>;
  recommended_inspect_team_summary_snapshot_paths: Record<string, string | null>;
  recommended_inspect_panes: Record<string, string | null>;
  recommended_inspect_command: string | null;
  recommended_inspect_commands: string[];
  recommended_inspect_summary: string | null;
  recommended_inspect_items: Array<{
    target: string;
    pane_id: string;
    worker_cli: TeamWorkerCli | null;