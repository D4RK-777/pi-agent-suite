import { existsSync } from 'fs';
import { mkdir, readFile, writeFile } from 'fs/promises';
import { spawnSync } from 'child_process';
import { join } from 'path';
import { getPackageRoot } from '../utils/package.js';
import { resolveCodexPane } from '../scripts/tmux-hook-engine.js';

type TmuxTargetType = 'session' | 'pane';

interface TmuxHookConfig {
  enabled: boolean;
  target: { type: TmuxTargetType; value: string };
  allowed_modes: string[];
  cooldown_ms: number;
  max_injections_per_session: number;
  prompt_template: string;
  marker: string;
  dry_run: boolean;
  log_level: 'error' | 'info' | 'debug';
  skip_if_scrolling: boolean;
}