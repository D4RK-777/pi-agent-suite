eckout,
  resolveCachedNativeBinaryCandidatePaths,
  getPackageVersion,
} from './native-assets.js';

export const EXPLORE_USAGE = [
  'Usage: omx explore --prompt "<prompt>"',
  '   or: omx explore --prompt-file <file>',
].join('\n');

const PROMPT_FLAG = '--prompt';
const PROMPT_FILE_FLAG = '--prompt-file';
export const EXPLORE_BIN_ENV = EXPLORE_BIN_ENV_SHARED;
const EXPLORE_SPARK_MODEL_ENV = 'OMX_EXPLORE_SPARK_MODEL';

export interface ParsedExploreArgs {
  prompt?: string;
  promptFile?: string;
}

interface ExploreHarnessCommand {
  command: string;
  args: string[];
}


interface ExploreHarnessMetadata {
  binaryName?: string;
  platform?: string;
  arch?: string;
}


const READ_ONLY_GIT_SUBCOMMANDS = new Set([
  'log',
  'diff',
  'status',
  'show',
  'branch',
  'rev-parse',
]);