import { mkdir, writeFile } from 'node:fs/promises';
import { join } from 'node:path';
import { startMode, updateModeState } from '../modes/base.js';
import { readApprovedExecutionLaunchHint, type ApprovedExecutionLaunchHint } from '../planning/artifacts.js';
import { ensureCanonicalRalphArtifacts } from '../ralph/persistence.js';
import {
  buildFollowupStaffingPlan,
  resolveAvailableAgentTypes,
} from '../team/followup-planner.js';

export const RALPH_HELP = `omx ralph - Launch Codex with ralph persistence mode active

Usage:
  omx ralph [task text...]
  omx ralph --prd "<task text>"
  omx ralph [ralph-options] [codex-args...] [task text...]