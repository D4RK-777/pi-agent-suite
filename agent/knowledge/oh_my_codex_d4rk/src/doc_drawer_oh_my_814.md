&& result.status === 0;
}

export type StarRepoResult = { ok: true } | { ok: false; error: string };

interface MaybePromptGithubStarDeps {
  stdinIsTTY?: boolean;
  stdoutIsTTY?: boolean;
  hasBeenPromptedFn?: () => Promise<boolean>;
  isGhInstalledFn?: () => boolean;
  markPromptedFn?: () => Promise<void>;
  askYesNoFn?: (question: string) => Promise<boolean>;
  starRepoFn?: () => StarRepoResult;
  logFn?: (message: string) => void;
  warnFn?: (message: string) => void;
}