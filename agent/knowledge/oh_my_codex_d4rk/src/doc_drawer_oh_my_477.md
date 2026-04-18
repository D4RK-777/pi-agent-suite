import { readFile } from 'fs/promises';
import { isAbsolute, join } from 'path';
import { existsSync, readFileSync } from 'fs';
import { getPackageRoot } from '../utils/package.js';
import { spawnPlatformCommandSync } from '../utils/platform-command.js';
import {
  isSparkShellNativeCompatibilityFailure,
  resolveSparkShellBinaryPathWithHydration,
  runSparkShellBinary,
} from './sparkshell.js';
import { getMainDefaultModel, getSparkDefaultModel } from '../config/models.js';
import {
  EXPLORE_BIN_ENV as EXPLORE_BIN_ENV_SHARED,
  hydrateNativeBinary,
  isRepositoryCheckout,
  resolveCachedNativeBinaryCandidatePaths,
  getPackageVersion,
} from './native-assets.js';