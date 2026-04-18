s = {},
): string {
  if (agent.name === "executor") {
    return resolveFrontierModel(options);
  }

  switch (agent.modelClass) {
    case "frontier":
      return resolveFrontierModel(options);
    case "fast":
      return getSparkDefaultModel(options.codexHomeOverride);
    case "standard":
    default:
      return resolveStandardModel(options);
  }
}

function isExactMiniModel(resolvedModel?: string | null): boolean {
  return resolvedModel?.trim() === EXACT_GPT_5_4_MINI_MODEL;
}

export function composeRoleInstructions(
  promptContent: string,
  metadata: RoleInstructionMetadata | null,
  resolvedModel?: string,
): string {
  const instructions = stripFrontmatter(promptContent);
  const parts = [instructions];