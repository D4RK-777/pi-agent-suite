import { createInterface } from 'readline/promises';
import { execFileSync, spawnSync } from 'child_process';
import { existsSync } from 'fs';
import { mkdir, writeFile } from 'fs/promises';
import { dirname, join, relative, resolve } from 'path';
import { fileURLToPath } from 'url';
import { type AutoresearchKeepPolicy, parseSandboxContract, slugifyMissionName } from '../autoresearch/contracts.js';
import {
  buildMissionContent,
  buildSandboxContent,
  type AutoresearchDeepInterviewResult,
  type AutoresearchSeedInputs,
  isLaunchReadyEvaluatorCommand,
  writeAutoresearchDeepInterviewArtifacts,
} from './autoresearch-intake.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);