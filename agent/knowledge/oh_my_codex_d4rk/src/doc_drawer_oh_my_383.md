await writeFile(path, `${buildAutoresearchDeepInterviewAppendix()}\n`, 'utf-8');
  return path;
}

async function runGuidedAutoresearchDeepInterview(
  repoRoot: string,
  seedArgs?: ReturnType<typeof parseInitArgs>,
): Promise<Awaited<ReturnType<typeof initAutoresearchMission>>> {
  const previousInstructionsFile = process.env[AUTORESEARCH_APPEND_INSTRUCTIONS_ENV];
  const appendixPath = await writeAutoresearchDeepInterviewAppendixFile(repoRoot);
  const existingResultPaths = new Set(await listAutoresearchDeepInterviewResultPaths(repoRoot));
  const existingDraftPaths = new Set(await listAutoresearchDeepInterviewDraftPaths(repoRoot));
  process.env[AUTORESEARCH_APPEND_INSTRUCTIONS_ENV] = appendixPath;