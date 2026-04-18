import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import { mkdir, readFile, readdir, rm, writeFile } from 'node:fs/promises';
import { spawnSync } from 'node:child_process';
import { createInterface } from 'node:readline/promises';
import { basename, join } from 'node:path';
import TOML from '@iarna/toml';
import { codexAgentsDir, projectCodexAgentsDir } from '../utils/paths.js';