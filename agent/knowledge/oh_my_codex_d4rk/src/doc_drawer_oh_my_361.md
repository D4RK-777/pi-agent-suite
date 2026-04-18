launchReadiness = parseLaunchReadinessSection(extractMarkdownSection(content, 'Launch Readiness'));

  if (!missionDraft) {
    throw new Error(`Missing Mission Draft section in ${draftArtifactPath}`);
  }
  if (!evaluatorDraft) {
    throw new Error(`Missing Evaluator Draft section in ${draftArtifactPath}`);
  }

  const slug = slugifyMissionName(slugRaw || missionDraft);
  const compileTarget: AutoresearchDraftCompileTarget = {
    topic: missionDraft,
    evaluatorCommand: evaluatorDraft,
    keepPolicy: normalizeKeepPolicy(keepPolicyRaw || 'score_improvement'),
    slug,
    repoRoot,
  };
  const missionContent = buildMissionContent(compileTarget.topic);
  const sandboxContent = buildSandboxContent(compileTarget.evaluatorCommand, compileTarget.keepPolicy);