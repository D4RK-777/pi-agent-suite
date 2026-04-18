/**
 * Launch-time update checks for oh-my-codex.
 * Non-fatal and throttled; can be disabled via OMX_AUTO_UPDATE=0.
 */

import { readFile, writeFile, mkdir } from 'fs/promises';
import { existsSync } from 'fs';
import { join } from 'path';
import { spawnSync } from 'child_process';
import { createInterface } from 'readline/promises';
import { getPackageRoot } from '../utils/package.js';
import { setup } from './setup.js';

interface UpdateState {
  last_checked_at: string;
  last_seen_latest?: string;
}

interface LatestPackageInfo {
  version?: string;
}

const PACKAGE_NAME = 'oh-my-codex';
const CHECK_INTERVAL_MS = 12 * 60 * 60 * 1000; // 12h