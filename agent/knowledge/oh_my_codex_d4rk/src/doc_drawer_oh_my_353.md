pPolicy = seedInputs.keepPolicy || '(none)';
  const seedSlug = seedInputs.slug?.trim() || '(none)';

  return [
    `# Deep Interview Autoresearch Draft — ${compileTarget.slug}`,
    '',
    '## Mission Draft',
    compileTarget.topic,
    '',
    '## Evaluator Draft',
    compileTarget.evaluatorCommand,
    '',
    '## Keep Policy',
    compileTarget.keepPolicy,
    '',
    '## Session Slug',
    compileTarget.slug,
    '',
    '## Seed Inputs',
    `- topic: ${seedTopic}`,
    `- evaluator: ${seedEvaluator}`,
    `- keep_policy: ${seedKeepPolicy}`,
    `- slug: ${seedSlug}`,
    '',
    '## Launch Readiness',
    buildLaunchReadinessSection(launchReady, blockedReasons),
    '',
    '## Confirmation Bridge',
    '- refine further',
    '- launch',
    '',
  ].join('\n');
}