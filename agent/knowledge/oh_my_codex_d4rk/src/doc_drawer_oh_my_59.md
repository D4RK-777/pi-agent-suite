import { execFileSync } from 'child_process';
import { existsSync } from 'fs';
import { readFile } from 'fs/promises';
import { basename, join, relative, resolve } from 'path';

export type AutoresearchKeepPolicy = 'score_improvement' | 'pass_only';

export interface AutoresearchEvaluatorContract {
  command: string;
  format: 'json';
  keep_policy?: AutoresearchKeepPolicy;
}

export interface ParsedSandboxContract {
  frontmatter: Record<string, unknown>;
  evaluator: AutoresearchEvaluatorContract;
  body: string;
}

export interface AutoresearchEvaluatorResult {
  pass: boolean;
  score?: number;
}