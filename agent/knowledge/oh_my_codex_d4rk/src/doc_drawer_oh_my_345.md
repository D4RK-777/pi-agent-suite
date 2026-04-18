pileTarget;
  path: string;
  content: string;
  launchReady: boolean;
  blockedReasons: string[];
}

export interface AutoresearchDeepInterviewResult {
  compileTarget: AutoresearchDraftCompileTarget;
  draftArtifactPath: string;
  missionArtifactPath: string;
  sandboxArtifactPath: string;
  resultPath: string;
  missionContent: string;
  sandboxContent: string;
  launchReady: boolean;
  blockedReasons: string[];
}

interface PersistedAutoresearchDeepInterviewResultV1 {
  kind: typeof AUTORESEARCH_DEEP_INTERVIEW_RESULT_KIND;
  compileTarget: AutoresearchDraftCompileTarget;
  draftArtifactPath: string;
  missionArtifactPath: string;
  sandboxArtifactPath: string;
  launchReady: boolean;
  blockedReasons: string[];
}