'],
    input: prompt,
    encoding: 'utf-8',
    env: process.env,
      windowsHide: true,
    });

  if (result.error) {
    throw result.error;
  }
  if (result.status !== 0) {
    process.exitCode = typeof result.status === 'number' ? result.status : 1;
    throw new Error(`autoresearch_codex_exec_failed:${result.status ?? 'unknown'}`);
  }
}

export interface ParsedAutoresearchArgs {
  missionDir: string | null;
  runId: string | null;
  codexArgs: string[];
  guided?: boolean;
  initArgs?: string[];
  seedArgs?: ReturnType<typeof parseInitArgs>;
  runSubcommand?: boolean;
}