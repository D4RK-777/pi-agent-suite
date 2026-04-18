tale /tmp directories without removing them',
  '  --help     Show this help message',
].join('\n');

const PROCESS_EXIT_POLL_MS = 100;
const SIGTERM_GRACE_MS = 5_000;
const STALE_TMP_MAX_AGE_MS = 60 * 60 * 1000;
const OMX_MCP_SERVER_PATTERN = /(?:^|[\\/])dist[\\/]mcp[\\/](?:state|memory|code-intel|trace|team)-server\.(?:[cm]?js|ts)\b/i;
const CODEX_PROCESS_PATTERN = /(?:^|[\\/\s])codex(?:\.js)?(?:\s|$)|@openai[\\/]codex/i;
const OMX_TMP_DIRECTORY_PATTERN = /^(omc|omx|oh-my-codex)-/;

export interface ProcessEntry {
  pid: number;
  ppid: number;
  command: string;
}

export interface CleanupCandidate extends ProcessEntry {
  reason: 'ppid=1' | 'outside-current-session';
}