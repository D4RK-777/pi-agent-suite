import { existsSync } from 'node:fs';
import { mkdir, readdir, readFile, stat, writeFile } from 'node:fs/promises';
import { dirname, join } from 'node:path';
import { type AutoresearchKeepPolicy, parseSandboxContract, slugifyMissionName } from '../autoresearch/contracts.js';

export interface AutoresearchSeedInputs {
  topic?: string;
  evaluatorCommand?: string;
  keepPolicy?: AutoresearchKeepPolicy;
  slug?: string;
}

export interface AutoresearchDraftCompileTarget {
  topic: string;
  evaluatorCommand: string;
  keepPolicy: AutoresearchKeepPolicy;
  slug: string;
  repoRoot: string;
}

export interface AutoresearchDraftArtifact {
  compileTarget: AutoresearchDraftCompileTarget;
  path: string;
  content: string;
  launchReady: boolean;
  blockedReasons: string[];
}