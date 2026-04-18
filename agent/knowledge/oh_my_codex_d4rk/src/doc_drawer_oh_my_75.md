import { execFileSync, spawnSync } from 'child_process';
import { existsSync } from 'fs';
import { mkdir, readFile, symlink, writeFile } from 'fs/promises';
import { dirname, join } from 'path';
import { cancelMode, readModeState, startMode, updateModeState } from '../modes/base.js';
import {
  parseEvaluatorResult,
  type AutoresearchKeepPolicy,
  type AutoresearchMissionContract,
} from './contracts.js';

export type AutoresearchCandidateStatus = 'candidate' | 'noop' | 'abort' | 'interrupted';
export type AutoresearchDecisionStatus = 'baseline' | 'keep' | 'discard' | 'ambiguous' | 'noop' | 'abort' | 'interrupted' | 'error';
export type AutoresearchRunStatus = 'running' | 'stopped' | 'completed' | 'failed';