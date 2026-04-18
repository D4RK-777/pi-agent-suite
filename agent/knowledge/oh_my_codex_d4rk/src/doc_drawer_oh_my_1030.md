` : `agents.${name}`;
    if (config.includes(`[${tableKey}]`)) {
      hasAgentEntries++;
    }
  }

  const hasTuiSection =
    /^\[tui\]/m.test(config) &&
    config.includes("oh-my-codex (OMX) Configuration");

  const hasTopLevelKeys =
    /^\s*notify\s*=.*node/m.test(config) ||
    /^\s*model_reasoning_effort\s*=/m.test(config) ||
    /^\s*developer_instructions\s*=.*oh-my-codex/m.test(config);

  const hasFeatureFlags =
    /^\s*multi_agent\s*=\s*true/m.test(config) ||
    /^\s*child_agents_md\s*=\s*true/m.test(config);
  const hasExploreRoutingEnv = /^\s*USE_OMX_EXPLORE_CMD\s*=/m.test(config);

  return {
    hasMcpServers,
    hasAgentEntries,
    hasTuiSection,
    hasTopLevelKeys,
    hasFeatureFlags,
    hasExploreRoutingEnv,
  };
}