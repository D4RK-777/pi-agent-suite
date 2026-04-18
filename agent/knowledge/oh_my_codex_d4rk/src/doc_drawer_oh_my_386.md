view result and retry.'}`,
    );
  }
  return materializeAutoresearchDeepInterviewResult(result);
}

export function normalizeAutoresearchCodexArgs(codexArgs: readonly string[]): string[] {
  const normalized: string[] = [];
  let hasBypass = false;

  for (const arg of codexArgs) {
    if (arg === MADMAX_FLAG) {
      if (!hasBypass) {
        normalized.push(CODEX_BYPASS_FLAG);
        hasBypass = true;
      }
      continue;
    }
    if (arg === CODEX_BYPASS_FLAG) {
      if (!hasBypass) {
        normalized.push(arg);
        hasBypass = true;
      }
      continue;
    }
    normalized.push(arg);
  }

  if (!hasBypass) {
    normalized.push(CODEX_BYPASS_FLAG);
  }

  return normalized;
}