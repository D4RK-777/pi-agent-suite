Scope, cwd = process.cwd()): string {
  return join(resolveAgentsDir(scope, cwd), `${name}.toml`);
}

function scaffoldAgentToml(name: string): string {
  const normalized = normalizeAgentName(name);
  return [
    `# Codex native agent: ${normalized}`,
    `name = "${normalized}"`,
    'description = "TODO: describe this agent\'s purpose"',
    'developer_instructions = """',
    'TODO: add the operating instructions for this agent.',
    '"""',
    '',
    '# Optional fields:',
    `# model = "${DEFAULT_AGENT_MODEL}"`,
    '# model_reasoning_effort = "medium"',
    '# temperature = 0.2',
    '# tools = ["shell", "apply_patch"]',
    '',
  ].join('\n');
}