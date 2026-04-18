;
  return normalized.includes('oh-my-codex/dist/mcp') || OMX_MCP_SERVER_PATTERN.test(normalized);
}

export function parsePsOutput(output: string): ProcessEntry[] {
  return output
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter(Boolean)
    .map((line) => {
      const match = line.match(/^(\d+)\s+(\d+)\s+(.+)$/);
      if (!match) return null;
      const pid = Number.parseInt(match[1], 10);
      const ppid = Number.parseInt(match[2], 10);
      const command = match[3]?.trim();
      if (!Number.isInteger(pid) || pid <= 0) return null;
      if (!Number.isInteger(ppid) || ppid < 0) return null;
      if (!command) return null;
      return { pid, ppid, command } satisfies ProcessEntry;
    })
    .filter((entry): entry is ProcessEntry => entry !== null);
}