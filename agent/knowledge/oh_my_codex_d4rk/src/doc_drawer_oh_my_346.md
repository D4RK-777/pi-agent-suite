ctPath: string;
  sandboxArtifactPath: string;
  launchReady: boolean;
  blockedReasons: string[];
}

const BLOCKED_EVALUATOR_PATTERNS = [
  /<[^>]+>/i,
  /\bTODO\b/i,
  /\bTBD\b/i,
  /REPLACE_ME/i,
  /CHANGEME/i,
  /your-command-here/i,
] as const;

const DEEP_INTERVIEW_DRAFT_PREFIX = 'deep-interview-autoresearch-';
const AUTORESEARCH_ARTIFACT_DIR_PREFIX = 'autoresearch-';
export const AUTORESEARCH_DEEP_INTERVIEW_RESULT_KIND = 'omx.autoresearch.deep-interview/v1';

function defaultDraftEvaluator(topic: string): string {
  const detail = topic.trim() || 'the mission';
  return `TODO replace with evaluator command for: ${detail}`;
}

function escapeRegex(value: string): string {
  return value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}