/**
 * omx doctor - Validate oh-my-codex installation
 */

import { existsSync } from 'fs';
import { readdir, readFile } from 'fs/promises';
import { join } from 'path';
import {
  codexHome, codexConfigPath, codexPromptsDir,
  userSkillsDir, projectSkillsDir, omxStateDir, detectLegacySkillRootOverlap,
} from '../utils/paths.js';
import { classifySpawnError, spawnPlatformCommandSync } from '../utils/platform-command.js';
import { getCatalogExpectations } from './catalog-contract.js';
import { parse as parseToml } from '@iarna/toml';
import { resolvePackagedExploreHarnessCommand, EXPLORE_BIN_ENV } from './explore.js';
import { getPackageRoot } from '../utils/package.js';
import { getDefaultBridge, isBridgeEnabled } from '../runtime/bridge.js';