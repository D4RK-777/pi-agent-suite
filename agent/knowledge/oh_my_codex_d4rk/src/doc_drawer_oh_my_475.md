message: 'not found in project root (run omx agents-init . or omx setup --scope project)',
  };
}

async function checkMcpServers(configPath: string): Promise<Check> {
  if (!existsSync(configPath)) {
    return { name: 'MCP Servers', status: 'warn', message: 'config.toml not found' };
  }
  try {
    const content = await readFile(configPath, 'utf-8');
    const mcpCount = (content.match(/\[mcp_servers\./g) || []).length;
    if (mcpCount > 0) {
      const hasOmx = content.includes('omx_state') || content.includes('omx_memory');
      if (hasOmx) {
        return { name: 'MCP Servers', status: 'pass', message: `${mcpCount} servers configured (OMX present)` };
      }
      return {
        name: 'MCP Servers',
        status: 'warn',