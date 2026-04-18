deadWorker.status.updated_at || new Date().toISOString(),
    source_type: 'await_snapshot',
  };
}

async function readTeamPaneStatus(
  config: Awaited<ReturnType<typeof readTeamConfig>>,
  cwd: string = process.cwd(),
  snapshot?: Pick<TeamSnapshot, 'teamName' | 'deadWorkers' | 'nonReportingWorkers' | 'workers' | 'tasks'>,
  tailLines: number = DEFAULT_SPARKSHELL_TAIL_LINES,
): Promise<{
  leader_pane_id: string | null;
  hud_pane_id: string | null;
  worker_panes: Record<string, string>;
  sparkshell_hint: string | null;
  sparkshell_commands: Record<string, string>;
  recommended_inspect_targets: string[];
  recommended_inspect_reasons: Record<string, string>;
  recommended_inspect_clis: Record<string, TeamWorkerCli | null>;