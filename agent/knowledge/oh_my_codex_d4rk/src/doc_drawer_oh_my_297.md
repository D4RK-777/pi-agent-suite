TOML from '@iarna/toml';
import { codexAgentsDir, projectCodexAgentsDir } from '../utils/paths.js';

export const RESERVED_NATIVE_AGENT_NAMES = new Set(['default', 'worker', 'explorer']);
const DEFAULT_AGENT_MODEL = 'gpt-5.4';
const AGENTS_USAGE = [
  'Usage:',
  '  omx agents list [--scope user|project]',
  '  omx agents add <name> [--scope user|project] [--force]',
  '  omx agents edit <name> [--scope user|project]',
  '  omx agents remove <name> [--scope user|project] [--force]',
  '',
  'Manage Codex native agent TOML files under ~/.codex/agents/ or ./.codex/agents/.',
  '',
  'Notes:',
  '  - list shows project + user agents by default',
  '  - add defaults to project scope when this repo is set up for project scope; otherwise user',