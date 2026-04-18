function normalizeCommand(command: string): string {
  return command.replace(/\\+/g, '/').trim();
}

function formatPlural(count: number, singular: string, plural = `${singular}s`): string {
  return `${count} ${count === 1 ? singular : plural}`;
}

export function isOmxMcpProcess(command: string): boolean {
  const normalized = normalizeCommand(command);
  return normalized.includes('oh-my-codex/dist/mcp') || OMX_MCP_SERVER_PATTERN.test(normalized);
}