;
  initArgs?: string[];
  seedArgs?: ReturnType<typeof parseInitArgs>;
  runSubcommand?: boolean;
}

function resolveRepoRoot(cwd: string): string {
  return execFileSync('git', ['rev-parse', '--show-toplevel'], {
    cwd,
    encoding: 'utf-8',
    stdio: ['ignore', 'pipe', 'pipe'],
      windowsHide: true,
    }).trim();
}

export function parseAutoresearchArgs(args: readonly string[]): ParsedAutoresearchArgs {
  const values = [...args];
  if (values.length === 0) {
    if (!process.stdin.isTTY) {
      throw new Error(`mission-dir is required.\n${AUTORESEARCH_HELP}`);
    }
    return { missionDir: null, runId: null, codexArgs: [], guided: true };
  }