vedNativeAgentName(name: string): boolean {
  return RESERVED_NATIVE_AGENT_NAMES.has(name.trim());
}

function normalizeAgentName(name: string): string {
  const trimmed = name.trim();
  if (!trimmed) {
    throw new Error('agent name must not be empty');
  }
  if (!/^[A-Za-z0-9][A-Za-z0-9_-]*$/.test(trimmed)) {
    throw new Error(`invalid agent name: ${name}`);
  }
  if (isReservedNativeAgentName(trimmed)) {
    throw new Error(`"${trimmed}" is reserved by Codex built-in agents`);
  }
  return trimmed;
}

function resolveAgentsDir(scope: AgentScope, cwd = process.cwd()): string {
  return scope === 'project' ? projectCodexAgentsDir(cwd) : codexAgentsDir();
}