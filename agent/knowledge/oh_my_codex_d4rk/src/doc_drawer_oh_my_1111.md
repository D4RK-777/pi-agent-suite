import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { mkdir, mkdtemp, readFile, rm } from 'node:fs/promises';
import { join } from 'node:path';
import { tmpdir } from 'node:os';
import { parseSandboxContract } from '../../autoresearch/contracts.js';
import {
  isLaunchReadyEvaluatorCommand,
  resolveAutoresearchDeepInterviewResult,
  writeAutoresearchDeepInterviewArtifacts,
  writeAutoresearchDraftArtifact,
} from '../autoresearch-intake.js';
import {
  buildAutoresearchDeepInterviewPrompt,
  initAutoresearchMission,
  parseInitArgs,
  checkTmuxAvailable,
  runAutoresearchNoviceBridge,
  type AutoresearchQuestionIO,
} from '../autoresearch-guided.js';