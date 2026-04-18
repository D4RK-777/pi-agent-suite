t: string, slug: string): string {
  return join(buildArtifactDir(repoRoot, slug), 'result.json');
}

export function buildMissionContent(topic: string): string {
  return `# Mission\n\n${topic}\n`;
}

export function buildSandboxContent(evaluatorCommand: string, keepPolicy: AutoresearchKeepPolicy): string {
  const safeCommand = evaluatorCommand.replace(/[\r\n]/g, ' ').trim();
  return `---\nevaluator:\n  command: ${safeCommand}\n  format: json\n  keep_policy: ${keepPolicy}\n---\n`;
}

export function isLaunchReadyEvaluatorCommand(command: string): boolean {
  const normalized = command.trim();
  if (!normalized) {
    return false;
  }
  return !BLOCKED_EVALUATOR_PATTERNS.some((pattern) => pattern.test(normalized));
}