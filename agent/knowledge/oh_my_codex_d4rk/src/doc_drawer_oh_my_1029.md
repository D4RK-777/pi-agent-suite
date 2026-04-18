n;
}

const OMX_MCP_SERVERS = [
  "omx_state",
  "omx_memory",
  "omx_code_intel",
  "omx_trace",
];

function detectOmxConfigArtifacts(config: string): {
  hasMcpServers: string[];
  hasAgentEntries: number;
  hasTuiSection: boolean;
  hasTopLevelKeys: boolean;
  hasFeatureFlags: boolean;
  hasExploreRoutingEnv: boolean;
} {
  const hasMcpServers = OMX_MCP_SERVERS.filter((name) =>
    new RegExp(`\\[mcp_servers\\.${name}\\]`).test(config),
  );

  const agentNames = Object.keys(AGENT_DEFINITIONS);
  let hasAgentEntries = 0;
  for (const name of agentNames) {
    const tableKey = name.includes("-") ? `agents."${name}"` : `agents.${name}`;
    if (config.includes(`[${tableKey}]`)) {
      hasAgentEntries++;
    }
  }