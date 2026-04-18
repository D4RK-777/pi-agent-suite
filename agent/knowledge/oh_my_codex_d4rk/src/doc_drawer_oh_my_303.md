um"',
    '# temperature = 0.2',
    '# tools = ["shell", "apply_patch"]',
    '',
  ].join('\n');
}

function parseAgentInfo(
  content: string,
  path: string,
  scope: AgentScope,
): NativeAgentInfo {
  const fallbackName = basename(path, '.toml');
  try {
    const parsed = TOML.parse(content) as Record<string, unknown>;
    return {
      scope,
      path,
      file: basename(path),
      name: typeof parsed.name === 'string' && parsed.name.trim() !== '' ? parsed.name : fallbackName,
      description: typeof parsed.description === 'string' ? parsed.description : '',
      model: typeof parsed.model === 'string' ? parsed.model : undefined,
    };
  } catch {
    return {
      scope,
      path,
      file: basename(path),
      name: fallbackName,