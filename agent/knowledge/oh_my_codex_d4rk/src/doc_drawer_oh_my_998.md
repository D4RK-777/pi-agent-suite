string;
  dry_run: boolean;
  log_level: 'error' | 'info' | 'debug';
  skip_if_scrolling: boolean;
}

interface TmuxHookState {
  total_injections?: number;
  session_counts?: Record<string, number>;
  pane_counts?: Record<string, number>;
  last_injection_ts?: number;
  last_reason?: string;
  last_event_at?: string;
  last_target?: string;
}

interface InitialTargetDetection {
  target: { type: TmuxTargetType; value: string };
  sessionName?: string;
}

interface InitConfigResult {
  configPath: string;
  created: boolean;
  usedPlaceholderTarget: boolean;
  detectedSession?: string;
}