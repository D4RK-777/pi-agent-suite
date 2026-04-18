y using exact case
  --json               Emit structured JSON
  -h, --help           Show this help

Examples:
  omx session search "worker inbox path"
  omx session search all_workers_idle --since 7d --limit 5
  omx session search "team api" --project current --json
`;

const HELP_TOKENS = new Set(['--help', '-h', 'help']);

export interface ParsedSessionSearchArgs {
  options: SessionSearchOptions;
  json: boolean;
}

function parsePositiveInteger(value: string, flag: string): number {
  const parsed = Number.parseInt(value, 10);
  if (!Number.isInteger(parsed) || parsed < 0) {
    throw new Error(`Invalid ${flag} value "${value}". Expected a non-negative integer.`);
  }
  return parsed;
}