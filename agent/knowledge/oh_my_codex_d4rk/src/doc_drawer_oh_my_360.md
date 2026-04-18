sandboxContent,
    launchReady: draft.launchReady,
    blockedReasons: draft.blockedReasons,
  };
}

function parseDraftArtifactContent(content: string, repoRoot: string, draftArtifactPath: string): AutoresearchDeepInterviewResult {
  const missionDraft = extractMarkdownSection(content, 'Mission Draft').trim();
  const evaluatorDraft = extractMarkdownSection(content, 'Evaluator Draft').trim().replace(/[\r\n]+/g, ' ');
  const keepPolicyRaw = extractMarkdownSection(content, 'Keep Policy').trim();
  const slugRaw = extractMarkdownSection(content, 'Session Slug').trim();
  const launchReadiness = parseLaunchReadinessSection(extractMarkdownSection(content, 'Launch Readiness'));