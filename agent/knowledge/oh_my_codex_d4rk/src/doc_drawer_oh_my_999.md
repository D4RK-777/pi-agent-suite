figPath: string;
  created: boolean;
  usedPlaceholderTarget: boolean;
  detectedSession?: string;
}

const DEFAULT_CONFIG: TmuxHookConfig = {
  enabled: true,
  target: { type: 'pane', value: '' },
  allowed_modes: ['ralph', 'ultrawork', 'team'],
  cooldown_ms: 15000,
  max_injections_per_session: 200,
  prompt_template: 'Continue from current mode state. [OMX_TMUX_INJECT]',
  marker: '[OMX_TMUX_INJECT]',
  dry_run: false,
  log_level: 'info',
  skip_if_scrolling: true,
};

const HELP = `
Usage:
  omx tmux-hook init       Create .omx/tmux-hook.json
  omx tmux-hook status     Show config + runtime state summary
  omx tmux-hook validate   Validate config and tmux target reachability
  omx tmux-hook test       Run a synthetic notify-hook turn (end-to-end)
`;