(
  codexArgs: string[],
): string[] {
  return collectInheritableTeamWorkerArgsShared(codexArgs);
}

export function resolveTeamWorkerLaunchArgsEnv(
  existingRaw: string | undefined,
  codexArgs: string[],
  inheritLeaderFlags = true,
  defaultModel?: string,
): string | null {
  const inheritedArgs = inheritLeaderFlags
    ? collectInheritableTeamWorkerArgs(codexArgs)
    : [];
  const normalized = resolveTeamWorkerLaunchArgs({
    existingRaw,
    inheritedArgs,
    fallbackModel: defaultModel,
  });
  if (normalized.length === 0) return null;
  return normalized.join(" ");
}