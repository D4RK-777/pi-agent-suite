import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import { realpathSync } from 'node:fs';
import { mkdtemp, mkdir, rm, writeFile } from 'node:fs/promises';
import { execFileSync } from 'node:child_process';
import { join } from 'node:path';
import { tmpdir } from 'node:os';
import {
  loadAutoresearchMissionContract,
  parseEvaluatorResult,
  parseSandboxContract,
  slugifyMissionName,
} from '../contracts.js';