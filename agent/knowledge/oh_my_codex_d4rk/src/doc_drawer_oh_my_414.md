nd } satisfies ProcessEntry;
    })
    .filter((entry): entry is ProcessEntry => entry !== null);
}

export function listOmxProcesses(): ProcessEntry[] {
  const output = execFileSync('ps', ['axww', '-o', 'pid=,ppid=,command='], {
    encoding: 'utf-8',
      windowsHide: true,
    });
  return parsePsOutput(output);
}

function isCodexSessionProcess(command: string): boolean {
  return CODEX_PROCESS_PATTERN.test(normalizeCommand(command));
}

function resolveProtectedRootPid(
  processes: readonly ProcessEntry[],
  currentPid: number,
): number {
  const parentByPid = new Map<number, number>();
  const commandByPid = new Map<number, string>();