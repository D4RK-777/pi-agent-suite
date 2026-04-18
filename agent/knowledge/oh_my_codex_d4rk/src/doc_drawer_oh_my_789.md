import {
  spawnSync,
  type SpawnSyncOptionsWithStringEncoding,
  type SpawnSyncReturns,
} from 'child_process';
import { existsSync } from 'fs';
import { arch as osArch, constants as osConstants } from 'os';
import { isAbsolute, join, resolve } from 'path';
import { getPackageRoot } from '../utils/package.js';
import { classifySpawnError } from '../utils/platform-command.js';
import { readConfiguredEnvOverrides } from '../config/models.js';
import { buildCapturePaneArgv } from '../scripts/tmux-hook-engine.js';
import {
  SPARKSHELL_BIN_ENV as SPARKSHELL_BIN_ENV_SHARED,
  getPackageVersion,
  hydrateNativeBinary,
  resolveLinuxNativeLibcPreference,
  resolveCachedNativeBinaryCandidatePaths,
} from './native-assets.js';

const OMX_SPARKSHELL_BIN_ENV = SPARKSHELL_BIN_ENV_SHARED;