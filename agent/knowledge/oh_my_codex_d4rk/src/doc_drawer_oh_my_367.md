(value): value is string => typeof value === 'string' && value.trim().length > 0)
      : [],
  };
}

export async function listAutoresearchDeepInterviewDraftPaths(repoRoot: string): Promise<string[]> {
  const specsDir = join(repoRoot, '.omx', 'specs');
  if (!existsSync(specsDir)) return [];
  const entries = await readdir(specsDir, { withFileTypes: true });
  return entries
    .filter((entry) => entry.isFile() && entry.name.startsWith(DEEP_INTERVIEW_DRAFT_PREFIX) && entry.name.endsWith('.md'))
    .map((entry) => join(specsDir, entry.name));
}

export async function listAutoresearchDeepInterviewResultPaths(repoRoot: string): Promise<string[]> {
  const specsDir = join(repoRoot, '.omx', 'specs');
  if (!existsSync(specsDir)) return [];