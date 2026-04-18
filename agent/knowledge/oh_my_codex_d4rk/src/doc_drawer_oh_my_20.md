ntier',
    routingRole: 'specialist',
    tools: 'read-only',
    category: 'coordination',
  },
};

/** Get agent definition by name */
export function getAgent(name: string): AgentDefinition | undefined {
  return AGENT_DEFINITIONS[name];
}

/** Get all agents in a category */
export function getAgentsByCategory(category: AgentDefinition['category']): AgentDefinition[] {
  return Object.values(AGENT_DEFINITIONS).filter(a => a.category === category);
}

/** Get all agent names */
export function getAgentNames(): string[] {
  return Object.keys(AGENT_DEFINITIONS);
}