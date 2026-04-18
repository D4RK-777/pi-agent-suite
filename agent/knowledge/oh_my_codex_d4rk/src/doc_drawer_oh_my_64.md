|| (!rel.startsWith('..') && rel !== '..')) return;
  throw contractError(MISSION_DIR_GIT_ERROR);
}

function extractFrontmatter(content: string): { frontmatter: string; body: string } {
  const match = content.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n?([\s\S]*)$/);
  if (!match) {
    throw contractError(SANDBOX_FRONTMATTER_ERROR);
  }
  return {
    frontmatter: match[1] || '',
    body: (match[2] || '').trim(),
  };
}

function parseSimpleYamlFrontmatter(frontmatter: string): Record<string, unknown> {
  const result: Record<string, unknown> = {};
  let currentSection: string | null = null;

  for (const rawLine of frontmatter.split(/\r?\n/)) {
    const line = rawLine.replace(/\t/g, '  ');
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) continue;