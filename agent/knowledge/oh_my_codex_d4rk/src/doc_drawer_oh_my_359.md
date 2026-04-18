factPath, missionContent, 'utf-8');
  await writeFile(sandboxArtifactPath, sandboxContent, 'utf-8');

  const persisted: PersistedAutoresearchDeepInterviewResultV1 = {
    kind: AUTORESEARCH_DEEP_INTERVIEW_RESULT_KIND,
    compileTarget: draft.compileTarget,
    draftArtifactPath: draft.path,
    missionArtifactPath,
    sandboxArtifactPath,
    launchReady: draft.launchReady,
    blockedReasons: draft.blockedReasons,
  };
  await writeFile(resultPath, `${JSON.stringify(persisted, null, 2)}\n`, 'utf-8');

  return {
    compileTarget: draft.compileTarget,
    draftArtifactPath: draft.path,
    missionArtifactPath,
    sandboxArtifactPath,
    resultPath,
    missionContent,
    sandboxContent,
    launchReady: draft.launchReady,
    blockedReasons: draft.blockedReasons,
  };
}