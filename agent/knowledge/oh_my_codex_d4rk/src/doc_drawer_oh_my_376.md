rializeAutoresearchDeepInterviewResult,
  parseInitArgs,
} from './autoresearch-guided.js';
import {
  listAutoresearchDeepInterviewDraftPaths,
  listAutoresearchDeepInterviewResultPaths,
  resolveAutoresearchDeepInterviewResult,
} from './autoresearch-intake.js';
import { CODEX_BYPASS_FLAG, MADMAX_FLAG } from './constants.js';
import { restoreStandaloneHudPane, enableMouseScrolling } from '../team/tmux-session.js';

export const AUTORESEARCH_HELP = `omx autoresearch - Launch OMX autoresearch with thin-supervisor parity semantics