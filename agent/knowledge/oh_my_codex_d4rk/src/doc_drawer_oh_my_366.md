ndboxContent = await readFile(sandboxArtifactPath, 'utf-8');
  parseSandboxContract(sandboxContent);

  return {
    compileTarget,
    draftArtifactPath,
    missionArtifactPath,
    sandboxArtifactPath,
    resultPath,
    missionContent,
    sandboxContent,
    launchReady: parsed.launchReady === true,
    blockedReasons: Array.isArray(parsed.blockedReasons)
      ? parsed.blockedReasons.filter((value): value is string => typeof value === 'string' && value.trim().length > 0)
      : [],
  };
}