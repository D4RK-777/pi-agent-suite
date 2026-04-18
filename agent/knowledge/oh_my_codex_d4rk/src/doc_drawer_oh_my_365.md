sionArtifactPath = isUsableAbsolutePath(parsed.missionArtifactPath)
    ? parsed.missionArtifactPath
    : join(buildArtifactDir(repoRoot, compileTarget.slug), 'mission.md');
  const sandboxArtifactPath = isUsableAbsolutePath(parsed.sandboxArtifactPath)
    ? parsed.sandboxArtifactPath
    : join(buildArtifactDir(repoRoot, compileTarget.slug), 'sandbox.md');
  const missionContent = await readFile(missionArtifactPath, 'utf-8');
  const sandboxContent = await readFile(sandboxArtifactPath, 'utf-8');
  parseSandboxContract(sandboxContent);