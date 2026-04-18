rn [
    'Launch-ready: no',
    ...blockedReasons.map((reason) => `- ${reason}`),
  ].join('\n');
}

export function buildAutoresearchDraftArtifactContent(
  compileTarget: AutoresearchDraftCompileTarget,
  seedInputs: AutoresearchSeedInputs,
  launchReady: boolean,
  blockedReasons: readonly string[],
): string {
  const seedTopic = seedInputs.topic?.trim() || '(none)';
  const seedEvaluator = seedInputs.evaluatorCommand?.trim() || '(none)';
  const seedKeepPolicy = seedInputs.keepPolicy || '(none)';
  const seedSlug = seedInputs.slug?.trim() || '(none)';