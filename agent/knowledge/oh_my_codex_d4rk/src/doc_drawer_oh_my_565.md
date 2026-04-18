ctRaw,
        }
      : codexEnvBase;
    runCodexBlocking(cwd, codexArgs, codexEnv);
  } finally {
    await postLaunch(cwd, sessionId, codexHomeOverride, true);
  }
}

export function normalizeCodexLaunchArgs(args: string[]): string[] {
  const parsed = parseWorktreeMode(args);
  const normalized: string[] = [];
  let wantsBypass = false;
  let hasBypass = false;
  let reasoningMode: ReasoningMode | null = null;

  for (const arg of parsed.remainingArgs) {
    if (arg === MADMAX_FLAG) {
      wantsBypass = true;
      continue;
    }

    if (arg === CODEX_BYPASS_FLAG) {
      wantsBypass = true;
      if (!hasBypass) {
        normalized.push(arg);
        hasBypass = true;
      }
      continue;
    }