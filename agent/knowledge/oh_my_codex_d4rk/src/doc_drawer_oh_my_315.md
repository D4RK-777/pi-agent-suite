ompt>"',
  '   or: omx ask <claude|gemini> --agent-prompt=<role> --prompt "<prompt>"',
].join('\n');

const ASK_PROVIDERS = ['claude', 'gemini'] as const;
type AskProvider = typeof ASK_PROVIDERS[number];
const ASK_PROVIDER_SET = new Set<string>(ASK_PROVIDERS);
const ASK_ADVISOR_SCRIPT_ENV = 'OMX_ASK_ADVISOR_SCRIPT';
const ASK_AGENT_PROMPT_FLAG = '--agent-prompt';
const ASK_ORIGINAL_TASK_ENV = 'OMX_ASK_ORIGINAL_TASK';
const SAFE_ROLE_PATTERN = /^[a-z][a-z0-9-]*$/;

export interface ParsedAskArgs {
  provider: AskProvider;
  prompt: string;
  agentPromptRole?: string;
}

function askUsageError(reason: string): Error {
  return new Error(`${reason}\n${ASK_USAGE}`);
}