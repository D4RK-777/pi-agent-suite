import { spawnSync } from 'child_process';
import { existsSync, readFileSync } from 'fs';
import { readFile, readdir } from 'fs/promises';
import { isAbsolute, join } from 'path';
import { constants as osConstants } from 'os';
import { getPackageRoot } from '../utils/package.js';
import { codexPromptsDir } from '../utils/paths.js';

export const ASK_USAGE = [
  'Usage: omx ask <claude|gemini> <question or task>',
  '   or: omx ask <claude|gemini> -p "<prompt>"',
  '   or: omx ask claude --print "<prompt>"',
  '   or: omx ask gemini --prompt "<prompt>"',
  '   or: omx ask <claude|gemini> --agent-prompt <role> "<prompt>"',
  '   or: omx ask <claude|gemini> --agent-prompt=<role> --prompt "<prompt>"',
].join('\n');