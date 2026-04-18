/**
 * One-time GitHub star prompt shown at OMX startup.
 * Skipped when no TTY or when gh CLI is not installed.
 * State stored globally (~/.omx/state/star-prompt.json) so it shows once per user.
 */

import { readFile, writeFile, mkdir } from 'fs/promises';
import { existsSync } from 'fs';
import { join } from 'path';
import { homedir } from 'os';
import * as childProcess from 'child_process';
import { createInterface } from 'readline/promises';

const REPO = 'Yeachan-Heo/oh-my-codex';

interface StarPromptState {
  prompted_at: string;
}

export function starPromptStatePath(): string {
  return join(homedir(), '.omx', 'state', 'star-prompt.json');
}