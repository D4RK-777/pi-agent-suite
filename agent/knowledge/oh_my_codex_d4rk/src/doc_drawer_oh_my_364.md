}
  if (!parsed.compileTarget) {
    throw new Error(`Missing compileTarget in ${resultPath}`);
  }

  const parsedCompileTarget = parsed.compileTarget as AutoresearchDraftCompileTarget;
  const inferredRepoRoot = inferRepoRootFromResultPath(resultPath);
  const repoRoot = isUsableAbsolutePath(parsedCompileTarget.repoRoot) ? parsedCompileTarget.repoRoot : inferredRepoRoot;
  const compileTarget: AutoresearchDraftCompileTarget = {
    ...parsedCompileTarget,
    repoRoot,
  };
  const draftArtifactPath = isUsableAbsolutePath(parsed.draftArtifactPath)
    ? parsed.draftArtifactPath
    : buildDraftArtifactPath(repoRoot, compileTarget.slug);
  const missionArtifactPath = isUsableAbsolutePath(parsed.missionArtifactPath)
    ? parsed.missionArtifactPath