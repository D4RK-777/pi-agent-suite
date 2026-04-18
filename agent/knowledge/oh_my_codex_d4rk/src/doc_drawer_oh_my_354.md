'',
    '## Confirmation Bridge',
    '- refine further',
    '- launch',
    '',
  ].join('\n');
}

export async function writeAutoresearchDraftArtifact(input: {
  repoRoot: string;
  topic: string;
  evaluatorCommand?: string;
  keepPolicy: AutoresearchKeepPolicy;
  slug?: string;
  seedInputs?: AutoresearchSeedInputs;
}): Promise<AutoresearchDraftArtifact> {
  const topic = input.topic.trim();
  if (!topic) {
    throw new Error('Research topic is required.');
  }