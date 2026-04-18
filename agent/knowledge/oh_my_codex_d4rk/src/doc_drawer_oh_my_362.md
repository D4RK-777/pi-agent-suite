onst sandboxContent = buildSandboxContent(compileTarget.evaluatorCommand, compileTarget.keepPolicy);
  parseSandboxContract(sandboxContent);

  return {
    compileTarget,
    draftArtifactPath,
    missionArtifactPath: join(buildArtifactDir(repoRoot, slug), 'mission.md'),
    sandboxArtifactPath: join(buildArtifactDir(repoRoot, slug), 'sandbox.md'),
    resultPath: buildResultPath(repoRoot, slug),
    missionContent,
    sandboxContent,
    launchReady: launchReadiness.launchReady,
    blockedReasons: launchReadiness.blockedReasons,
  };
}

function inferRepoRootFromResultPath(resultPath: string): string {
  return dirname(dirname(dirname(dirname(resultPath))));
}