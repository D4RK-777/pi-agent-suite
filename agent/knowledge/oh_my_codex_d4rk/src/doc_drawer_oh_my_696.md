import { searchSessionHistory, type SessionSearchReport, type SessionSearchOptions } from '../session-history/search.js';

const HELP = `omx session - Search prior local session history

Usage:
  omx session search <query> [options]

Options:
  --limit <n>          Maximum results to return (default: 10)
  --session <id>       Restrict to a specific session id or id fragment
  --since <spec>       Restrict by recency (examples: 7d, 24h, 2026-03-10)
  --project <scope>    Filter by project context: current | all | <cwd-fragment>
  --context <n>        Snippet context characters (default: 80)
  --case-sensitive     Match query using exact case
  --json               Emit structured JSON
  -h, --help           Show this help