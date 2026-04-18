pprovedHint.testSpecPaths.join(', ')}`);
  }
  if (approvedHint.deepInterviewSpecPaths.length > 0) {
    lines.push(`- deep-interview specs: ${approvedHint.deepInterviewSpecPaths.join(', ')}`);
    lines.push('- Carry forward the approved deep-interview requirements and constraints during Ralph execution and final verification.');
  }
  return lines;
}

export function normalizeRalphCliArgs(args: readonly string[]): string[] {
  const normalized: string[] = [];
  let i = 0;
  while (i < args.length) {
    const token = args[i];
    if (token === '--prd') {
      const next = args[i + 1];
      if (next && next !== '--' && !next.startsWith('-')) {
        normalized.push(next);
        i += 2;
        continue;
      }
      i++;
      continue;
    }
    if (token.startsWith('--prd=')) {