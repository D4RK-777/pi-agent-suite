',
  '  - add defaults to project scope when this repo is set up for project scope; otherwise user',
  '  - remove prompts for confirmation unless --force is passed',
].join('\n');

type AgentScope = 'user' | 'project';

export interface NativeAgentInfo {
  scope: AgentScope;
  path: string;
  file: string;
  name: string;
  description: string;
  model?: string;
}

function isReservedNativeAgentName(name: string): boolean {
  return RESERVED_NATIVE_AGENT_NAMES.has(name.trim());
}