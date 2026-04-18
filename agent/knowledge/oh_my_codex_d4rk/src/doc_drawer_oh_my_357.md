(path, content, 'utf-8');

  return { compileTarget, path, content, launchReady, blockedReasons };
}

export async function writeAutoresearchDeepInterviewArtifacts(input: {
  repoRoot: string;
  topic: string;
  evaluatorCommand?: string;
  keepPolicy: AutoresearchKeepPolicy;
  slug?: string;
  seedInputs?: AutoresearchSeedInputs;
}): Promise<AutoresearchDeepInterviewResult> {
  const draft = await writeAutoresearchDraftArtifact(input);
  const artifactDir = buildArtifactDir(input.repoRoot, draft.compileTarget.slug);
  await mkdir(artifactDir, { recursive: true });