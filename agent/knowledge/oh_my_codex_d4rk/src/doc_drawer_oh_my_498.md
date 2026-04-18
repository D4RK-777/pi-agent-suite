harness.md'),
    '--model-spark', sparkModel,
    '--model-fallback', getMainDefaultModel(),
  ];
}

export async function loadExplorePrompt(parsed: ParsedExploreArgs): Promise<string> {
  if (parsed.prompt) return parsed.prompt;
  if (!parsed.promptFile) throw exploreUsageError('Missing prompt. Provide --prompt or --prompt-file.');
  const content = await readFile(parsed.promptFile, 'utf-8');
  const trimmed = content.trim();
  if (!trimmed) throw exploreUsageError(`Prompt file is empty: ${parsed.promptFile}`);
  return trimmed;
}