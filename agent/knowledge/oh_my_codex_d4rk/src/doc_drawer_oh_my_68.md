ror('sandbox.md frontmatter evaluator.keep_policy must be one of: score_improvement, pass_only.');
}

export function parseSandboxContract(content: string): ParsedSandboxContract {
  const { frontmatter, body } = extractFrontmatter(content);
  const parsedFrontmatter = parseSimpleYamlFrontmatter(frontmatter);
  const evaluatorRaw = parsedFrontmatter.evaluator;

  if (!evaluatorRaw || typeof evaluatorRaw !== 'object' || Array.isArray(evaluatorRaw)) {
    throw contractError(EVALUATOR_BLOCK_ERROR);
  }