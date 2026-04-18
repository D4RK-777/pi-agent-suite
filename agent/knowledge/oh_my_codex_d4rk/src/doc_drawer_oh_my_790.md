didatePaths,
} from './native-assets.js';

const OMX_SPARKSHELL_BIN_ENV = SPARKSHELL_BIN_ENV_SHARED;

export const SPARKSHELL_USAGE = [
  'Usage: omx sparkshell <command> [args...]',
  '   or: omx sparkshell --tmux-pane <pane-id> [--tail-lines <100-1000>]',
  'Runs the native omx-sparkshell sidecar with direct argv execution or explicit tmux pane summarization.',
  'Shell metacharacters such as pipes and redirects are not interpreted in v1.',
  'Tmux pane mode is explicit opt-in and captures a larger pane tail before applying raw-vs-summary behavior.',
].join('\n');