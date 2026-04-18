lized.push(arg);
  }

  if (wantsBypass && !hasBypass) {
    normalized.push(CODEX_BYPASS_FLAG);
  }

  if (reasoningMode) {
    normalized.push(CONFIG_FLAG, `${REASONING_KEY}="${reasoningMode}"`);
  }

  return normalized;
}

/**
 * Returns the spark model string if --spark or --madmax-spark appears in the
 * raw (pre-normalize) args, or undefined if neither flag is present.
 * Used to route the spark model to team workers without affecting the leader.
 */
export function resolveWorkerSparkModel(
  args: string[],
  codexHomeOverride?: string,
): string | undefined {
  for (const arg of args) {
    if (arg === SPARK_FLAG || arg === MADMAX_SPARK_FLAG) {
      return resolveTeamLowComplexityDefaultModel(codexHomeOverride);
    }
  }
  return undefined;
}