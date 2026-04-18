ne.replace(/^-\s+/, '').trim())
      .filter(Boolean);

  return { launchReady, blockedReasons };
}

function normalizeKeepPolicy(raw: string): AutoresearchKeepPolicy {
  return raw.trim().toLowerCase() === 'pass_only' ? 'pass_only' : 'score_improvement';
}

function buildArtifactDir(repoRoot: string, slug: string): string {
  return join(repoRoot, '.omx', 'specs', `${AUTORESEARCH_ARTIFACT_DIR_PREFIX}${slug}`);
}

function buildDraftArtifactPath(repoRoot: string, slug: string): string {
  return join(repoRoot, '.omx', 'specs', `${DEEP_INTERVIEW_DRAFT_PREFIX}${slug}.md`);
}

function buildResultPath(repoRoot: string, slug: string): string {
  return join(buildArtifactDir(repoRoot, slug), 'result.json');
}