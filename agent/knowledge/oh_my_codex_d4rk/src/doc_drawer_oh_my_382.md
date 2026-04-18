ad of finalizing launch-ready output.',
    '</autoresearch_deep_interview_mode>',
  ].join('\n');
}

async function writeAutoresearchDeepInterviewAppendixFile(repoRoot: string): Promise<string> {
  const { mkdir, writeFile } = await import('node:fs/promises');
  const { join } = await import('node:path');
  const dir = join(repoRoot, '.omx', 'autoresearch');
  await mkdir(dir, { recursive: true });
  const path = join(dir, 'deep-interview-session-instructions.md');
  await writeFile(path, `${buildAutoresearchDeepInterviewAppendix()}\n`, 'utf-8');
  return path;
}