ifactDir(input.repoRoot, draft.compileTarget.slug);
  await mkdir(artifactDir, { recursive: true });

  const missionArtifactPath = join(artifactDir, 'mission.md');
  const sandboxArtifactPath = join(artifactDir, 'sandbox.md');
  const resultPath = buildResultPath(input.repoRoot, draft.compileTarget.slug);
  const missionContent = buildMissionContent(draft.compileTarget.topic);
  const sandboxContent = buildSandboxContent(draft.compileTarget.evaluatorCommand, draft.compileTarget.keepPolicy);

  parseSandboxContract(sandboxContent);
  await writeFile(missionArtifactPath, missionContent, 'utf-8');
  await writeFile(sandboxArtifactPath, sandboxContent, 'utf-8');