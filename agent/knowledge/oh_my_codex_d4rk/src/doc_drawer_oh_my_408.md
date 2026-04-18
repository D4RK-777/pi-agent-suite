import { execFileSync } from 'child_process';
import { readdir, rm, stat } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const HELP = [
  'Usage: omx cleanup [--dry-run]',
  '',
  'Kill orphaned OMX MCP server processes and remove stale OMX /tmp directories left behind by previous Codex App sessions.',
  '',
  'Options:',
  '  --dry-run  List matching orphaned processes and stale /tmp directories without removing them',
  '  --help     Show this help message',
].join('\n');