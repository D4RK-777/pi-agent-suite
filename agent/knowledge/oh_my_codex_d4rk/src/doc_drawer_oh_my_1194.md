import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import {
  cleanupCommand,
  cleanupOmxMcpProcesses,
  cleanupStaleTmpDirectories,
  findCleanupCandidates,
  type ProcessEntry,
} from '../cleanup.js';

const CURRENT_SESSION_PROCESSES: ProcessEntry[] = [
  { pid: 700, ppid: 500, command: 'codex' },
  { pid: 701, ppid: 700, command: 'node /repo/bin/omx.js cleanup --dry-run' },
  {
    pid: 710,
    ppid: 700,
    command: 'node /repo/oh-my-codex/dist/mcp/state-server.js',
  },
  {
    pid: 800,
    ppid: 1,
    command: 'node /tmp/oh-my-codex/dist/mcp/memory-server.js',
  },
  {
    pid: 810,
    ppid: 42,
    command: 'node /tmp/worktree/dist/mcp/trace-server.js',
  },
  {
    pid: 811,
    ppid: 810,